---
title: Tổ tiên chung gần nhất - O(sqrt(N)) và O(log N) với tiền xử lý O(N)
tags:
  - Translated
e_maxx_link: lca
lang: vi
---
# Tổ tiên chung gần nhất - $O(\sqrt{N})$ và $O(\log N)$ với tiền xử lý $O(N)$

Cho một cây $G$. Cho các truy vấn dạng $(v_1, v_2)$, với mỗi truy vấn bạn cần tìm tổ tiên chung gần nhất (Lowest Common Ancestor - LCA), tức là một đỉnh $v$ nằm trên đường đi từ gốc đến $v_1$ và đường đi từ gốc đến $v_2$, và đỉnh này phải ở vị trí thấp nhất. Nói cách khác, đỉnh $v$ cần tìm là tổ tiên thấp nhất (xa gốc nhất) của $v_1$ và $v_2$. Rõ ràng là tổ tiên chung gần nhất của chúng nằm trên đường đi ngắn nhất giữa $v_1$ và $v_2$. Ngoài ra, nếu $v_1$ là tổ tiên của $v_2$, thì $v_1$ chính là tổ tiên chung gần nhất của chúng.

### Ý tưởng thuật toán

Trước khi trả lời các truy vấn, chúng ta cần **tiền xử lý** (preprocess) cây.
Chúng ta thực hiện một chuyến duyệt [DFS](depth-first-search.md) bắt đầu từ gốc và xây dựng danh sách $\text{euler}$ để lưu thứ tự các đỉnh được duyệt qua (một đỉnh được thêm vào danh sách khi chúng ta ghé thăm nó lần đầu tiên, và sau khi duyệt DFS quay về từ các nút con của nó).
Đây còn được gọi là đường đi Euler (Euler tour) của cây.
Rõ ràng kích thước của danh sách này sẽ là $O(N)$.
Chúng ta cũng cần xây dựng mảng $\text{first}[0..N-1]$ để lưu vị trí xuất hiện đầu tiên của mỗi đỉnh $i$ trong $\text{euler}$.
Tức là, vị trí đầu tiên trong $\text{euler}$ sao cho $\text{euler}[\text{first}[i]] = i$.
Bằng cách sử dụng DFS, chúng ta cũng có thể tìm chiều cao của mỗi nút (khoảng cách từ gốc đến nút đó) và lưu vào mảng $\text{height}[0..N-1]$.

Vậy làm thế nào để trả lời các truy vấn bằng đường đi Euler và hai mảng bổ sung này?
Giả sử truy vấn là một cặp đỉnh $v_1$ và $v_2$.
Hãy xem xét các đỉnh mà chúng ta ghé thăm trong đường đi Euler từ lần đầu tiên duyệt qua $v_1$ đến lần đầu tiên duyệt qua $v_2$.
Dễ thấy rằng, $\text{LCA}(v_1, v_2)$ là đỉnh có chiều cao nhỏ nhất trên đoạn này.
Chúng ta đã lưu ý rằng, LCA phải thuộc đường đi ngắn nhất giữa $v_1$ và $v_2$.
Rõ ràng nó cũng phải là đỉnh có chiều cao nhỏ nhất.
Và trong đường đi Euler, về cơ bản chúng ta đi dọc theo đường đi ngắn nhất, ngoại trừ việc chúng ta duyệt thêm qua tất cả các cây con trên đường đi đó.
Tuy nhiên, tất cả các đỉnh trong những cây con này đều nằm ở vị trí thấp hơn LCA trong cây, do đó chúng có chiều cao lớn hơn.
Vì vậy, $\text{LCA}(v_1, v_2)$ có thể được xác định duy nhất bằng cách tìm đỉnh có chiều cao nhỏ nhất trong đường đi Euler giữa $\text{first}(v_1)$ và $\text{first}(v_2)$.

Hãy minh họa ý tưởng này.
Xét đồ thị sau và đường đi Euler cùng chiều cao tương ứng:
<div style="text-align: center;" markdown="1">

![LCA_Euler_Tour](LCA_Euler.png)

</div>

$$\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\text{Vertices:}   & 1 & 2 & 5 & 2 & 6 & 2 & 1 & 3 & 1 & 4 & 7 & 4 & 1 \\ \hline
\text{Heights:} & 1 & 2 & 3 & 2 & 3 & 2 & 1 & 2 & 1 & 2 & 3 & 2 & 1 \\ \hline
\end{array}$$

Với đường đi bắt đầu từ đỉnh $6$ và kết thúc ở $4$, chúng ta duyệt qua các đỉnh $[6, 2, 1, 3, 1, 4]$.
Trong số các đỉnh này, đỉnh $1$ có chiều cao nhỏ nhất, vì vậy $\text{LCA(6, 4) = 1}$.

Tóm lại:
Để trả lời một truy vấn, chúng ta chỉ cần **tìm đỉnh có chiều cao nhỏ nhất** trong mảng $\text{euler}$ trong đoạn từ $\text{first}[v_1]$ đến $\text{first}[v_2]$.
Như vậy, **bài toán LCA được đưa về bài toán RMQ** (truy vấn giá trị nhỏ nhất trên đoạn - Range Minimum Query).

Sử dụng [Chia căn (Sqrt Decomposition)](../data_structures/sqrt_decomposition.md), ta có thể thu được một lời giải trả lời mỗi truy vấn trong $O(\sqrt{N})$ với thời gian tiền xử lý $O(N)$.

Sử dụng [Cây phân đoạn (Segment Tree)](../data_structures/segment_tree.md), bạn có thể trả lời mỗi truy vấn trong $O(\log N)$ với thời gian tiền xử lý $O(N)$.

Vì hầu như không có cập nhật nào đối với các giá trị được lưu trữ, [Bảng thưa (Sparse Table)](../data_structures/sparse-table.md) có thể là một lựa chọn tốt hơn, cho phép trả lời truy vấn trong $O(1)$ với thời gian xây dựng $O(N\log N)$.

### Cài đặt

Trong cài đặt thuật toán LCA dưới đây, Cây phân đoạn (Segment Tree) được sử dụng.

```{.cpp file=lca}
struct LCA {
    vector<int> height, euler, first, segtree;
    vector<bool> visited;
    int n;

    LCA(vector<vector<int>> &adj, int root = 0) {
        n = adj.size();
        height.resize(n);
        first.resize(n);
        euler.reserve(n * 2);
        visited.assign(n, false);
        dfs(adj, root);
        int m = euler.size();
        segtree.resize(m * 4);
        build(1, 0, m - 1);
    }

    void dfs(vector<vector<int>> &adj, int node, int h = 0) {
        visited[node] = true;
        height[node] = h;
        first[node] = euler.size();
        euler.push_back(node);
        for (auto to : adj[node]) {
            if (!visited[to]) {
                dfs(adj, to, h + 1);
                euler.push_back(node);
            }
        }
    }

    void build(int node, int b, int e) {
        if (b == e) {
            segtree[node] = euler[b];
        } else {
            int mid = (b + e) / 2;
            build(node << 1, b, mid);
            build(node << 1 | 1, mid + 1, e);
            int l = segtree[node << 1], r = segtree[node << 1 | 1];
            segtree[node] = (height[l] < height[r]) ? l : r;
        }
    }

    int query(int node, int b, int e, int L, int R) {
        if (b > R || e < L)
            return -1;
        if (b >= L && e <= R)
            return segtree[node];
        int mid = (b + e) >> 1;

        int left = query(node << 1, b, mid, L, R);
        int right = query(node << 1 | 1, mid + 1, e, L, R);
        if (left == -1) return right;
        if (right == -1) return left;
        return height[left] < height[right] ? left : right;
    }

    int lca(int u, int v) {
        int left = first[u], right = first[v];
        if (left > right)
            swap(left, right);
        return query(1, 0, euler.size() - 1, left, right);
    }
};

```

## Bài tập thực hành
 - [SPOJ: LCA](http://www.spoj.com/problems/LCA/)
 - [SPOJ: DISQUERY](http://www.spoj.com/problems/DISQUERY/)
 - [TIMUS: 1471. Distance in the Tree](http://acm.timus.ru/problem.aspx?space=1&num=1471)
 - [CODEFORCES: Design Tutorial: Inverse the Problem](http://codeforces.com/problemset/problem/472/D)
 - [CODECHEF: Lowest Common Ancestor](https://www.codechef.com/problems/TALCA)
 * [SPOJ - Lowest Common Ancestor](http://www.spoj.com/problems/LCASQ/)
 * [SPOJ - Ada and Orange Tree](http://www.spoj.com/problems/ADAORANG/)
 * [DevSkill - Motoku (archived)](http://web.archive.org/web/20200922005503/https://devskill.com/CodingProblems/ViewProblem/141)
 * [UVA 12655 - Trucks](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=4384)
 * [Codechef - Pishty and Tree](https://www.codechef.com/problems/PSHTTR)
 * [UVA - 12533 - Joining Couples](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=441&page=show_problem&problem=3978)
 * [Codechef - So close yet So Far](https://www.codechef.com/problems/CLOSEFAR)
 * [Codeforces - Drivers Dissatisfaction](http://codeforces.com/contest/733/problem/F)
 * [UVA 11354 - Bond](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2339)
 * [SPOJ - Query on a tree II](http://www.spoj.com/problems/QTREE2/)
 * [Codeforces - Best Edge Weight](http://codeforces.com/contest/828/problem/F)
 * [Codeforces - Misha, Grisha and Underground](http://codeforces.com/contest/832/problem/D)
 * [SPOJ - Nlogonian Tickets](http://www.spoj.com/problems/NTICKETS/)
 * [Codeforces - Rowena Rawenclaws Diadem](http://codeforces.com/contest/855/problem/D)
