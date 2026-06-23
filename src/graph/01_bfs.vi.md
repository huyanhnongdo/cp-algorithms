---
tags:
  - Translated
lang: vi
---

# Thuật toán 0-1 BFS

Như chúng ta đã biết, việc tìm đường đi ngắn nhất giữa một đỉnh nguồn duy nhất và tất cả các đỉnh khác trên một **đồ thị không trọng số** có thể thực hiện trong $O(|E|)$ bằng cách sử dụng thuật toán [Tìm kiếm theo chiều rộng (Breadth First Search - BFS)](breadth-first-search.md). Khi đó, khoảng cách được hiểu là số lượng cạnh tối thiểu cần đi qua để đến được đỉnh đích.
Chúng ta cũng có thể coi đồ thị này là một đồ thị có trọng số, trong đó mọi cạnh đều có trọng số bằng $1$.
Nếu các cạnh trong đồ thị không có cùng một trọng số, chúng ta phải sử dụng một thuật toán tổng quát hơn, chẳng hạn như thuật toán [Dijkstra](dijkstra.md) hoạt động trong thời gian $O(|V|^2 + |E|)$ hoặc $O(|E| \log |V|)$.

Tuy nhiên, nếu trọng số của các cạnh bị giới hạn hơn, chúng ta thường có thể làm tốt hơn.
Trong bài viết này, chúng tôi sẽ trình bày cách sử dụng BFS để giải quyết bài toán đường đi ngắn nhất từ một nguồn (SSSP - Single-Source Shortest Path) trong thời gian $O(|E|)$, nếu trọng số của mỗi cạnh chỉ có thể là $0$ hoặc $1$.

## Thuật toán

Chúng ta có thể phát triển thuật toán này bằng cách nghiên cứu kỹ thuật toán Dijkstra và suy nghĩ về các hệ quả từ đồ thị đặc biệt này mang lại.
Dạng tổng quát của thuật toán Dijkstra là (ở đây cấu trúc `set` được dùng làm hàng đợi ưu tiên):

```cpp
d.assign(n, INF);
d[s] = 0;
set<pair<int, int>> q;
q.insert({0, s});
while (!q.empty()) {
    int v = q.begin()->second;
    q.erase(q.begin());

    for (auto edge : adj[v]) {
        int u = edge.first;
        int w = edge.second;

        if (d[v] + w < d[u]) {
            q.erase({d[u], u});
            d[u] = d[v] + w;
            q.insert({d[u], u});
        }
    }
}
```

Chúng ta nhận thấy rằng hiệu khoảng cách từ đỉnh nguồn `s` tới hai đỉnh bất kỳ nằm trong hàng đợi chênh lệch nhau tối đa là $1$.
Đặc biệt, ta biết rằng $d[v] \le d[u] \le d[v] + 1$ với mọi $u \in Q$.
Nguyên nhân là do trong mỗi bước lặp, chúng ta chỉ thêm các đỉnh mới có khoảng cách bằng khoảng cách hiện tại hoặc bằng khoảng cách hiện tại cộng một vào hàng đợi.
Giả sử tồn tại một đỉnh $u$ trong hàng đợi có $d[u] - d[v] > 1$, thì $u$ phải được đưa vào hàng đợi thông qua một đỉnh trung gian $t$ khác thỏa mãn $d[t] \ge d[u] - 1 > d[v]$.
Tuy nhiên điều này là bất khả thi, vì thuật toán Dijkstra luôn duyệt qua các đỉnh theo thứ tự khoảng cách tăng dần.

Điều này có nghĩa là, thứ tự các phần tử trong hàng đợi có dạng:

$$Q = \underbrace{v}_{d[v]}, \dots, \underbrace{u}_{d[v]}, \underbrace{m}_{d[v]+1} \dots \underbrace{n}_{d[v]+1}$$

Cấu trúc này cực kỳ đơn giản, đến mức chúng ta không cần đến một hàng đợi ưu tiên thực sự (sử dụng cây nhị phân cân bằng như `set` là dư thừa).
Chúng ta chỉ cần sử dụng một hàng đợi hai đầu thông thường (`std::deque`), và thêm đỉnh mới vào đầu hàng đợi nếu cạnh tương ứng có trọng số $0$ (tức là $d[u] = d[v]$), hoặc thêm vào cuối hàng đợi nếu cạnh có trọng số $1$ (tức là $d[u] = d[v] + 1$).
Bằng cách này, hàng đợi luôn được đảm bảo duy trì trạng thái đã sắp xếp tại mọi thời điểm.

```cpp
vector<int> d(n, INF);
d[s] = 0;
deque<int> q;
q.push_front(s);
while (!q.empty()) {
    int v = q.front();
    q.pop_front();
    for (auto edge : adj[v]) {
        int u = edge.first;
        int w = edge.second;
        if (d[v] + w < d[u]) {
            d[u] = d[v] + w;
            if (w == 1)
                q.push_back(u);
            else
                q.push_front(u);
        }
    }
}
```

## Thuật toán Dial (Dial's algorithm)

Chúng ta có thể mở rộng thuật toán này xa hơn nữa nếu chúng ta cho phép trọng số các cạnh lớn hơn.
Nếu mọi cạnh trên đồ thị có trọng số $\le k$, thì khoảng cách của các đỉnh trong hàng đợi sẽ chênh lệch tối đa là $k$ so với khoảng cách từ $v$ đến đỉnh nguồn.
Do đó, chúng ta có thể duy trì $k + 1$ ngăn chứa (buckets) cho các đỉnh trong hàng đợi. Bất cứ khi nào ngăn chứa ứng với khoảng cách nhỏ nhất trống, chúng ta thực hiện dịch chuyển vòng tròn để lấy ngăn chứa có khoảng cách lớn hơn tiếp theo.
Sự mở rộng này được gọi là **Thuật toán Dial**.

## Bài tập áp dụng

- [Labyrinth](https://codeforces.com/contest/1063/problem/B)
- [KATHTHI](http://www.spoj.com/problems/KATHTHI/)
- [DoNotTurn](https://community.topcoder.com/stat?c=problem_statement&pm=10337)
- [Ocean Currents](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2620)
- [Olya and Energy Drinks](https://codeforces.com/problemset/problem/877/D)
- [Three States](https://codeforces.com/problemset/problem/590/C)
- [Colliding Traffic](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2621)
- [CHamber of Secrets](https://codeforces.com/problemset/problem/173/B)
- [Spiral Maximum](https://codeforces.com/problemset/problem/173/C)
- [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid)
