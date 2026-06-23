---
tags:
  - Translated
e_maxx_link: lca_simpler
lang: vi
---

# Tổ tiên chung gần nhất - Nhảy nhị phân

Cho $G$ là một cây.
Với mỗi truy vấn có dạng `(u, v)`, chúng ta muốn tìm tổ tiên chung gần nhất (Lowest Common Ancestor - LCA) của các nút `u` và `v`, tức là chúng ta muốn tìm một nút `w` vừa nằm trên đường đi từ `u` về nút gốc, vừa nằm trên đường đi từ `v` về nút gốc, và nếu có nhiều nút như vậy thì chúng ta chọn nút ở xa gốc nhất.
Nói cách khác, nút `w` cần tìm là tổ tiên thấp nhất của `u` và `v`.
Đặc biệt, nếu `u` là tổ tiên của `v`, thì `u` chính là tổ tiên chung gần nhất của chúng.

Thuật toán được mô tả trong bài viết này cần $O(N \log N)$ cho việc tiền xử lý cây, và sau đó mất $O(\log N)$ cho mỗi truy vấn LCA.

## Thuật toán

Với mỗi nút, chúng ta sẽ tính trước tổ tiên thứ 1 phía trên nó, tổ tiên thứ 2 phía trên nó, tổ tiên thứ 4 phía trên nó, v.v.
Hãy lưu chúng trong mảng `up`, nghĩa là `up[i][j]` là tổ tiên thứ `2^j` phía trên nút `i` với `i=1...N`, `j=0...ceil(log(N))`.
Thông tin này cho phép chúng ta nhảy từ bất kỳ nút nào đến bất kỳ tổ tiên nào phía trên nó trong thời gian $O(\log N)$.
Chúng ta có thể tính toán mảng này bằng cách duyệt [DFS](depth-first-search.md) trên cây.

Với mỗi nút, chúng ta cũng lưu lại thời điểm ghé thăm nó lần đầu tiên (tức là thời điểm DFS phát hiện ra nút), và thời điểm rời khỏi nó (tức là sau khi đã duyệt qua toàn bộ các nút con và thoát khỏi hàm DFS).
Chúng ta có thể sử dụng thông tin này để xác định xem một nút có phải là tổ tiên của một nút khác hay không trong thời gian hằng số.

Bây giờ giả sử chúng ta nhận được một truy vấn `(u, v)`.
Chúng ta có thể ngay lập tức kiểm tra xem nút này có phải là tổ tiên của nút kia hay không.
Nếu có, thì nút đó chính là LCA luôn.
Nếu `u` không phải là tổ tiên của `v` và `v` cũng không phải là tổ tiên của `u`, chúng ta sẽ đi lên các tổ tiên của `u` cho đến khi tìm thấy nút cao nhất (tức là gần gốc nhất) mà không phải là tổ tiên của `v` (nghĩa là một nút `x` sao cho `x` không phải là tổ tiên của `v`, nhưng `up[x][0]` thì có).
Chúng ta có thể tìm nút `x` này trong thời gian $O(\log N)$ bằng cách sử dụng mảng `up`.

Chúng ta sẽ mô tả chi tiết hơn quá trình này.
Đặt `L = ceil(log(N))`.
Ban đầu giả sử `i = L`.
Nếu `up[u][i]` không phải là tổ tiên của `v`, thì ta có thể gán `u = up[u][i]` và giảm `i`.
Nếu `up[u][i]` là tổ tiên của `v`, thì chúng ta chỉ cần giảm `i`.
Rõ ràng, sau khi thực hiện việc này cho tất cả các `i` không âm, nút `u` sẽ là nút cần tìm - nghĩa là `u` vẫn không phải là tổ tiên của `v`, nhưng `up[u][0]` thì có.

Bây giờ, câu trả lời cho LCA chắc chắn sẽ là `up[u][0]` - tức là nút nhỏ nhất trong số các tổ tiên của nút `u` mà cũng là tổ tiên của `v`.

Vì vậy, việc trả lời một truy vấn LCA sẽ duyệt `i` từ `ceil(log(N))` về `0` và kiểm tra ở mỗi bước lặp xem nút này có phải là tổ tiên của nút kia hay không.
Do đó, mỗi truy vấn có thể được trả lời trong $O(\log N)$.

## Cài đặt

```cpp
int n, l;
vector<vector<int>> adj;

int timer;
vector<int> tin, tout;
vector<vector<int>> up;

void dfs(int v, int p)
{
    tin[v] = ++timer;
    up[v][0] = p;
    for (int i = 1; i <= l; ++i)
        up[v][i] = up[up[v][i-1]][i-1];

    for (int u : adj[v]) {
        if (u != p)
            dfs(u, v);
    }

    tout[v] = ++timer;
}

bool is_ancestor(int u, int v)
{
    return tin[u] <= tin[v] && tout[u] >= tout[v];
}

int lca(int u, int v)
{
    if (is_ancestor(u, v))
        return u;
    if (is_ancestor(v, u))
        return v;
    for (int i = l; i >= 0; --i) {
        if (!is_ancestor(up[u][i], v))
            u = up[u][i];
    }
    return up[u][0];
}

void preprocess(int root) {
    tin.resize(n);
    tout.resize(n);
    timer = 0;
    l = ceil(log2(n));
    up.assign(n, vector<int>(l + 1));
    dfs(root, root);
}
```
## Bài tập thực hành

* [LeetCode -  Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node)
* [Codechef - Longest Good Segment](https://www.codechef.com/problems/LGSEG)
* [HackerEarth - Optimal Connectivity](https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/optimal-connectivity-c6ae79ca/)
