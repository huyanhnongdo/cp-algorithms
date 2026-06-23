---
tags:
  - Translated
e_maxx_link: min_cost_flow
lang: vi
---

# Luồng chi phí tối thiểu - Thuật toán đường đi ngắn nhất tăng dần

Cho mạng $G$ gồm $n$ đỉnh và $m$ cạnh.
Với mỗi cạnh (nói chung là các cạnh có hướng, xem thêm bên dưới), chúng ta được biết sức chứa (một số nguyên không âm) và chi phí trên một đơn vị luồng dọc theo cạnh này (một số nguyên nào đó).
Đỉnh nguồn $s$ và đỉnh đích $t$ cũng được xác định trước.

Với một giá trị $K$ cho trước, chúng ta phải tìm một luồng có giá trị bằng lượng này, và trong tất cả các luồng có cùng lượng như vậy, chúng ta phải chọn luồng có tổng chi phí thấp nhất.
Bài toán này được gọi là **bài toán luồng chi phí tối thiểu** (minimum-cost flow problem).

Đôi khi bài toán được phát biểu hơi khác một chút:
bạn muốn tìm luồng cực đại, và trong số các luồng cực đại đó, tìm luồng có chi phí nhỏ nhất.
Bài toán này được gọi là **bài toán luồng cực đại chi phí tối thiểu** (minimum-cost maximum-flow problem).

Cả hai bài toán này đều có thể được giải quyết hiệu quả bằng thuật toán tìm các đường đi ngắn nhất tăng dần (successive shortest paths).

## Thuật toán

Thuật toán này rất giống với thuật toán [Edmonds-Karp](edmonds_karp.md) dùng để tính luồng cực đại.

### Trường hợp đơn giản nhất

Trước tiên, chúng ta chỉ xem xét trường hợp đơn giản nhất, trong đó đồ thị là có hướng và có tối đa một cạnh giữa bất kỳ cặp đỉnh nào (ví dụ: nếu $(i, j)$ là một cạnh trong đồ thị, thì $(j, i)$ không thể là một cạnh thuộc đồ thị đó).

Gọi $U_{i j}$ là sức chứa của cạnh $(i, j)$ nếu cạnh này tồn tại.
Gọi $C_{i j}$ là chi phí trên một đơn vị luồng dọc theo cạnh $(i, j)$.
Và cuối cùng gọi $F_{i, j}$ là luồng hiện tại trên cạnh $(i, j)$.
Ban đầu, tất cả các giá trị luồng đều bằng 0.

Chúng ta **sửa đổi** mạng như sau:
với mỗi cạnh $(i, j)$, chúng ta thêm **cạnh ngược** $(j, i)$ vào mạng với sức chứa $U_{j i} = 0$ và chi phí $C_{j i} = -C_{i j}$.
Theo hạn chế của chúng ta, vì cạnh $(j, i)$ ban đầu không có trong mạng, mạng thu được vẫn không phải là một đa đồ thị (multigraph - đồ thị có nhiều cạnh giữa hai đỉnh).
Ngoài ra, chúng ta sẽ luôn duy trì điều kiện $F_{j i} = -F_{i j}$ trong suốt các bước của thuật toán.

Chúng ta định nghĩa **mạng thặng dư** đối với một luồng cố định $F$ như sau (giống như trong thuật toán Ford-Fulkerson):
mạng thặng dư chỉ chứa các cạnh chưa bão hòa (tức là các cạnh thỏa mãn $F_{i j} < U_{i j}$), và sức chứa thặng dư của mỗi cạnh như vậy là $R_{i j} = U_{i j} - F_{i j}$.

Bây giờ chúng ta thảo luận về **thuật toán** tính luồng chi phí tối thiểu.
Tại mỗi bước lặp của thuật toán, chúng ta tìm đường đi ngắn nhất trên đồ thị thặng dư từ $s$ đến $t$.
Khác với thuật toán Edmonds-Karp, chúng ta tìm đường đi ngắn nhất theo nghĩa tổng chi phí của đường đi, thay vì theo số lượng cạnh.
Nếu không còn tìm thấy đường đi nào nữa, thuật toán kết thúc và luồng $F$ thu được chính là luồng cần tìm.
Nếu tìm thấy đường đi, chúng ta tăng luồng dọc theo nó nhiều nhất có thể (tức là tìm sức chứa thặng dư nhỏ nhất $R$ của các cạnh trên đường đi, tăng luồng trên các cạnh xuôi thêm $R$, và giảm luồng trên các cạnh ngược một lượng tương ứng $R$).
Nếu tại một thời điểm nào đó, tổng lượng luồng đạt đến giá trị $K$, chúng ta dừng thuật toán (lưu ý rằng ở bước lặp cuối cùng, ta chỉ cần tăng luồng một lượng vừa đủ để tổng luồng không vượt quá $K$).

Không khó để nhận thấy rằng nếu đặt $K$ bằng vô cùng, thuật toán sẽ tìm được luồng cực đại chi phí tối thiểu.
Do đó, cả hai biến thể của bài toán đều có thể được giải quyết bằng cùng một thuật toán.

### Đồ thị vô hướng / Đa đồ thị

Trường hợp đồ thị vô hướng hoặc đa đồ thị không có khác biệt về mặt ý tưởng so với thuật toán trên.
Thuật toán vẫn hoạt động bình thường trên các đồ thị này.
Tuy nhiên, việc cài đặt sẽ phức tạp hơn một chút.

Một **cạnh vô hướng** $(i, j)$ thực chất tương đương với hai cạnh có hướng $(i, j)$ và $(j, i)$ có cùng sức chứa và chi phí.
Vì thuật toán luồng chi phí tối thiểu mô tả ở trên tạo ra một cạnh ngược cho mỗi cạnh có hướng, nó sẽ chia cạnh vô hướng thành $4$ cạnh có hướng, và chúng ta thực sự thu được một **đa đồ thị** (multigraph).

Làm thế nào để xử lý **đa cạnh** (multiple edges)?
Thứ nhất, luồng của mỗi đa cạnh phải được lưu trữ riêng biệt.
Thứ hai, khi tìm đường đi ngắn nhất, cần phải lưu ý xem đa cạnh nào đang được sử dụng trong đường đi.
Vì vậy, thay vì chỉ lưu mảng đỉnh cha (ancestor) như thông thường, chúng ta phải lưu thêm chỉ số của cạnh đã đi qua để đến đỉnh đó cùng với đỉnh cha.
Thứ ba, khi luồng tăng trên một cạnh nào đó, ta phải giảm luồng trên cạnh ngược tương ứng.
Vì đồ thị có đa cạnh, chúng ta phải lưu trữ thêm chỉ số cạnh ngược cho mỗi cạnh.

Không có trở ngại nào khác đối với đồ thị vô hướng hay đa đồ thị.

### Độ phức tạp

Thuật toán này nói chung có độ phức tạp thời gian mũ theo kích thước đầu vào. Cụ thể, trong trường hợp xấu nhất, nó có thể chỉ đẩy được đúng $1$ đơn vị luồng ở mỗi bước lặp, mất $O(F)$ bước lặp để tìm luồng chi phí tối thiểu có giá trị $F$, dẫn tới tổng thời gian chạy là $O(F \cdot T)$, với $T$ là thời gian cần thiết để tìm đường đi ngắn nhất từ nguồn đến đích.

Nếu sử dụng thuật toán [Bellman-Ford](bellman_ford.md) cho việc này, thời gian chạy sẽ là $O(F mn)$. Chúng ta cũng có thể sửa đổi [Thuật toán Dijkstra](dijkstra.md) để nó chỉ mất $O(nm)$ thời gian tiền xử lý ở bước ban đầu và sau đó chạy trong $O(m \log n)$ cho mỗi bước lặp, giúp tổng thời gian chạy là $O(mn + F m \log n)$. [Tại đây](http://web.archive.org/web/20211009144446/https://min-25.hatenablog.com/entry/2018/03/19/235802) là một bộ sinh đồ thị mà trên đó thuật toán như vậy sẽ mất thời gian $O(2^{n/2} n^2 \log n)$.

Thuật toán Dijkstra cải tiến sử dụng khái niệm gọi là thế (potentials) từ [Thuật toán Johnson](https://en.wikipedia.org/wiki/Johnson%27s_algorithm). Ta có thể kết hợp ý tưởng của thuật toán này với thuật toán Dinic để giảm số lượng bước lặp từ $F$ xuống còn $\min(F, nC)$, với $C$ là chi phí lớn nhất của các cạnh trên đồ thị. Bạn có thể đọc thêm về thế và cách kết hợp với thuật toán Dinic [tại đây](https://codeforces.com/blog/entry/105658).

## Cài đặt

Dưới đây là một cài đặt sử dụng [Thuật toán SPFA](bellman_ford.md) cho trường hợp đơn giản nhất.

```{.cpp file=min_cost_flow_successive_shortest_path}
struct Edge
{
    int from, to, capacity, cost;
};

vector<vector<int>> adj, cost, capacity;

const int INF = 1e9;

void shortest_paths(int n, int v0, vector<int>& d, vector<int>& p) {
    d.assign(n, INF);
    d[v0] = 0;
    vector<bool> inq(n, false);
    queue<int> q;
    q.push(v0);
    p.assign(n, -1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        inq[u] = false;
        for (int v : adj[u]) {
            if (capacity[u][v] > 0 && d[v] > d[u] + cost[u][v]) {
                d[v] = d[u] + cost[u][v];
                p[v] = u;
                if (!inq[v]) {
                    inq[v] = true;
                    q.push(v);
                }
            }
        }
    }
}

int min_cost_flow(int N, vector<Edge> edges, int K, int s, int t) {
    adj.assign(N, vector<int>());
    cost.assign(N, vector<int>(N, 0));
    capacity.assign(N, vector<int>(N, 0));
    for (Edge e : edges) {
        adj[e.from].push_back(e.to);
        adj[e.to].push_back(e.from);
        cost[e.from][e.to] = e.cost;
        cost[e.to][e.from] = -e.cost;
        capacity[e.from][e.to] = e.capacity;
    }

    int flow = 0;
    int cost = 0;
    vector<int> d, p;
    while (flow < K) {
        shortest_paths(N, s, d, p);
        if (d[t] == INF)
            break;
        
        // find max flow on that path
        int f = K - flow;
        int cur = t;
        while (cur != s) {
            f = min(f, capacity[p[cur]][cur]);
            cur = p[cur];
        }

        // apply flow
        flow += f;
        cost += f * d[t];
        cur = t;
        while (cur != s) {
            capacity[p[cur]][cur] -= f;
            capacity[cur][p[cur]] += f;
            cur = p[cur];
        }
    }

    if (flow < K)
        return -1;
    else
        return cost;
}
```

## Bài tập thực hành

* [CSES - Task Assignment](https://cses.fi/problemset/task/2129)
* [CSES - Grid Puzzle II](https://cses.fi/problemset/task/2131)
* [AtCoder - Dream Team](https://atcoder.jp/contests/abc247/tasks/abc247_g)
