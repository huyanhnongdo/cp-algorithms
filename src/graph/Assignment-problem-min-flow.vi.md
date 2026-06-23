---
tags:
  - Translated
e_maxx_link: assignment_mincostflow
lang: vi
---

# Giải quyết bài toán phân công bằng luồng chi phí tối thiểu

**Bài toán phân công** (assignment problem) có hai cách phát biểu tương đương:

   - Cho một ma trận vuông $A[1..N, 1..N]$, bạn cần chọn $N$ phần tử trong đó sao cho mỗi hàng và mỗi cột có chính xác một phần tử được chọn, và tổng giá trị của các phần tử được chọn là nhỏ nhất.
   - Có $N$ đơn hàng và $N$ máy móc. Chi phí sản xuất của mỗi máy ứng với từng đơn hàng đã được biết trước. Mỗi máy chỉ có thể thực hiện tối đa một đơn hàng. Yêu cầu phân công toàn bộ các đơn hàng cho các máy sao cho tổng chi phí là nhỏ nhất.

Ở đây chúng ta sẽ xem xét giải pháp cho bài toán dựa trên thuật toán tìm [luồng chi phí tối thiểu (min-cost-flow)](min_cost_flow.md), giải quyết bài toán phân công trong thời gian $\mathcal{O}(N^3)$.

## Mô tả

Hãy xây dựng một mạng hai phía (bipartite network): gồm một đỉnh nguồn $S$, một đỉnh đích $T$, phần thứ nhất gồm $N$ đỉnh (tương ứng với các hàng của ma trận, hoặc các đơn hàng), phần thứ hai cũng gồm $N$ đỉnh (tương ứng với các cột của ma trận, hoặc các máy móc). Giữa mỗi đỉnh $i$ của phần thứ nhất và mỗi đỉnh $j$ của phần thứ hai, chúng ta vẽ một cạnh có sức chứa là 1 và chi phí là $A_{ij}$. Từ nguồn $S$, chúng ta vẽ các cạnh đến tất cả các đỉnh $i$ của phần thứ nhất với sức chứa là 1 và chi phí là 0. Chúng ta vẽ cạnh có sức chứa là 1 và chi phí là 0 từ mỗi đỉnh $j$ của phần thứ hai đến đích $T$.

Chúng ta tìm trên mạng thu được luồng cực đại có chi phí tối thiểu. Rõ ràng, giá trị luồng sẽ là $N$. Hơn nữa, với mỗi đỉnh $i$ thuộc phần thứ nhất, có chính xác một đỉnh $j$ thuộc phần thứ hai sao cho luồng $F_{ij} = 1$. Cuối cùng, đây là một tương ứng một-một giữa các đỉnh của phần thứ nhất và các đỉnh của phần thứ hai, vốn là lời giải cho bài toán (vì luồng tìm được có chi phí tối thiểu, nên tổng chi phí của các cạnh được chọn sẽ là nhỏ nhất có thể, đạt tiêu chí tối ưu).

Độ phức tạp của giải pháp này đối với bài toán phân công phụ thuộc vào thuật toán được sử dụng để tìm luồng cực đại chi phí tối thiểu. Độ phức tạp sẽ là $\mathcal{O}(N^3)$ nếu sử dụng thuật toán [Dijkstra](dijkstra.md) hoặc $\mathcal{O}(N^4)$ nếu sử dụng thuật toán [Bellman-Ford](bellman_ford.md). Điều này là do kích thước luồng là $O(N)$ và mỗi bước lặp của thuật toán Dijkstra có thể được thực hiện trong $O(N^2)$, trong khi đối với Bellman-Ford là $O(N^3)$.

## Cài đặt

Cài đặt được đưa ra ở đây khá dài, có thể được rút gọn đi đáng kể.
Nó sử dụng [Thuật toán SPFA](bellman_ford.md) để tìm các đường đi ngắn nhất.

```cpp
const int INF = 1000 * 1000 * 1000;

vector<int> assignment(vector<vector<int>> a) {
    int n = a.size();
    int m = n * 2 + 2;
    vector<vector<int>> f(m, vector<int>(m));
    int s = m - 2, t = m - 1;
    int cost = 0;
    while (true) {
        vector<int> dist(m, INF);
        vector<int> p(m);
        vector<bool> inq(m, false);
        queue<int> q;
        dist[s] = 0;
        p[s] = -1;
        q.push(s);
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            inq[v] = false;
            if (v == s) {
                for (int i = 0; i < n; ++i) {
                    if (f[s][i] == 0) {
                        dist[i] = 0;
                        p[i] = s;
                        inq[i] = true;
                        q.push(i);
                    }
                }
            } else {
                if (v < n) {
                    for (int j = n; j < n + n; ++j) {
                        if (f[v][j] < 1 && dist[j] > dist[v] + a[v][j - n]) {
                            dist[j] = dist[v] + a[v][j - n];
                            p[j] = v;
                            if (!inq[j]) {
                                q.push(j);
                                inq[j] = true;
                            }
                        }
                    }
                } else {
                    for (int j = 0; j < n; ++j) {
                        if (f[v][j] < 0 && dist[j] > dist[v] - a[j][v - n]) {
                            dist[j] = dist[v] - a[j][v - n];
                            p[j] = v;
                            if (!inq[j]) {
                                q.push(j);
                                inq[j] = true;
                            }
                        }
                    }
                }
            }
        }

        int curcost = INF;
        for (int i = n; i < n + n; ++i) {
            if (f[i][t] == 0 && dist[i] < curcost) {
                curcost = dist[i];
                p[t] = i;
            }
        }
        if (curcost == INF)
            break;
        cost += curcost;
        for (int cur = t; cur != -1; cur = p[cur]) {
            int prev = p[cur];
            if (prev != -1)
                f[cur][prev] = -(f[prev][cur] = 1);
        }
    }

    vector<int> answer(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (f[i][j + n] == 1)
                answer[i] = j;
        }
    }
    return answer;
}
```
