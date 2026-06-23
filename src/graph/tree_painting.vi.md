---
tags:
  - Translated
e_maxx_link: tree_painting
---

# Tô màu các cạnh của cây

Đây là một bài toán khá phổ biến. Cho một cây $G$ gồm $N$ đỉnh. Có hai loại truy vấn: loại thứ nhất là tô màu một cạnh, loại thứ hai là truy vấn số lượng cạnh được tô màu trên đường đi giữa hai đỉnh.

Ở đây chúng ta mô tả một lời giải khá đơn giản (sử dụng [cây phân đoạn (segment tree)](../data_structures/segment_tree.md)) cho phép trả lời mỗi truy vấn trong thời gian $O(\log N)$.
Bước tiền xử lý tốn $O(N)$ thời gian.

## Thuật toán

Đầu tiên, chúng ta cần tìm [LCA](lca.md) để quy mỗi truy vấn loại thứ hai $(i,j)$ về hai truy vấn con là $(l,i)$ và $(l,j)$, với $l$ là LCA của $i$ và $j$.
Câu trả lời cho truy vấn $(i,j)$ sẽ là tổng kết quả của cả hai truy vấn con.
Cả hai truy vấn con này đều có cấu trúc đặc biệt: đỉnh thứ nhất là tổ tiên của đỉnh thứ hai.
Trong phần còn lại của bài viết, chúng ta sẽ chỉ thảo luận về loại truy vấn đặc biệt này.

Chúng ta bắt đầu bằng mô tả bước **tiền xử lý**.
Chạy tìm kiếm theo chiều sâu (DFS) từ gốc của cây và ghi lại Euler tour của lượt DFS này (mỗi đỉnh được thêm vào danh sách khi DFS ghé thăm nó lần đầu tiên và mỗi lần chúng ta quay trở lại từ một trong các con của nó).
Kỹ thuật tương tự cũng có thể được áp dụng trong bước tiền xử lý LCA.

Danh sách này sẽ chứa mọi cạnh (theo nghĩa là nếu $i$ và $j$ là hai đầu của cạnh, thì sẽ có một vị trí trong danh sách mà $i$ và $j$ kề nhau), và mỗi cạnh xuất hiện chính xác hai lần: theo chiều xuôi (từ $i$ đến $j$, trong đó đỉnh $i$ gần gốc hơn đỉnh $j$) và theo chiều ngược lại (từ $j$ đến $i$).

Chúng ta sẽ xây dựng hai danh sách cho các cạnh này.
Danh sách thứ nhất lưu màu của tất cả các cạnh theo chiều xuôi, và danh sách thứ hai lưu màu của tất cả các cạnh theo chiều ngược.
Chúng ta sử dụng giá trị $1$ nếu cạnh được tô màu, và $0$ nếu ngược lại.
Trên mỗi danh sách này chúng ta dựng một cây phân đoạn (để truy vấn tổng với thao tác cập nhật điểm), gọi chúng là $T1$ và $T2$.

Bây giờ hãy trả lời truy vấn có dạng $(i,j)$, trong đó $i$ là tổ tiên của $j$.
Chúng ta cần xác định xem có bao nhiêu cạnh trên đường đi từ $i$ đến $j$ được tô màu.
Tìm vị trí xuất hiện đầu tiên của $i$ và $j$ trong Euler tour, gọi các vị trí đó là $p$ và $q$ (việc này có thể thực hiện trong $O(1)$ nếu ta tính trước các vị trí này trong bước tiền xử lý).
Khi đó, **câu trả lời** cho truy vấn là tổng $T1[p..q-1]$ trừ đi tổng $T2[p..q-1]$.

**Tại sao lại như vậy?**
Xét đoạn $[p;q]$ trong Euler tour.
Đoạn này chứa tất cả các cạnh của đường đi cần tìm từ $i$ đến $j$, nhưng cũng chứa một số cạnh nằm trên các đường đi khác đi ra từ $i$.
Tuy nhiên, có một điểm khác biệt lớn giữa các cạnh cần tìm và các cạnh còn lại: các cạnh cần tìm chỉ xuất hiện đúng một lần theo chiều xuôi, trong khi tất cả các cạnh còn lại xuất hiện hai lần: một lần theo chiều xuôi và một lần theo chiều ngược.
Do đó, hiệu số $T1[p..q-1] - T2[p..q-1]$ sẽ cho chúng ta câu trả lời chính xác (trừ đi 1 ở cận trên là cần thiết vì nếu không ta sẽ tính thêm một cạnh đi ra từ đỉnh $j$).
Truy vấn tổng trên cây phân đoạn được thực hiện trong thời gian $O(\log N)$.

Trả lời **truy vấn loại thứ nhất** (tô màu một cạnh) thậm chí còn dễ hơn - chúng ta chỉ cần cập nhật $T1$ và $T2$, cụ thể là thực hiện cập nhật điểm trên phần tử tương ứng với cạnh đó (việc tìm vị trí của cạnh trong danh sách cũng có thể thực hiện trong $O(1)$ nếu ta lưu lại vị trí này trong bước tiền xử lý).
Một thao tác cập nhật điểm trên cây phân đoạn được thực hiện trong $O(\log N)$.

## Cài đặt

Dưới đây là mã nguồn cài đặt hoàn chỉnh của lời giải, bao gồm cả việc tính LCA:

```cpp
const int INF = 1000 * 1000 * 1000;

typedef vector<vector<int>> graph;

vector<int> dfs_list;
vector<int> edges_list;
vector<int> h;

void dfs(int v, const graph& g, const graph& edge_ids, int cur_h = 1) {
    h[v] = cur_h;
    dfs_list.push_back(v);
    for (size_t i = 0; i < g[v].size(); ++i) {
        if (h[g[v][i]] == -1) {
            edges_list.push_back(edge_ids[v][i]);
            dfs(g[v][i], g, edge_ids, cur_h + 1);
            edges_list.push_back(edge_ids[v][i]);
            dfs_list.push_back(v);
        }
    }
}

vector<int> lca_tree;
vector<int> first;

void lca_tree_build(int i, int l, int r) {
    if (l == r) {
        lca_tree[i] = dfs_list[l];
    } else {
        int m = (l + r) >> 1;
        lca_tree_build(i + i, l, m);
        lca_tree_build(i + i + 1, m + 1, r);
        int lt = lca_tree[i + i], rt = lca_tree[i + i + 1];
        lca_tree[i] = h[lt] < h[rt] ? lt : rt;
    }
}

void lca_prepare(int n) {
    lca_tree.assign(dfs_list.size() * 8, -1);
    lca_tree_build(1, 0, (int)dfs_list.size() - 1);

    first.assign(n, -1);
    for (int i = 0; i < (int)dfs_list.size(); ++i) {
        int v = dfs_list[i];
        if (first[v] == -1)
            first[v] = i;
    }
}

int lca_tree_query(int i, int tl, int tr, int l, int r) {
    if (tl == l && tr == r)
        return lca_tree[i];
    int m = (tl + tr) >> 1;
    if (r <= m)
        return lca_tree_query(i + i, tl, m, l, r);
    if (l > m)
        return lca_tree_query(i + i + 1, m + 1, tr, l, r);
    int lt = lca_tree_query(i + i, tl, m, l, m);
    int rt = lca_tree_query(i + i + 1, m + 1, tr, m + 1, r);
    return h[lt] < h[rt] ? lt : rt;
}

int lca(int a, int b) {
    if (first[a] > first[b])
        swap(a, b);
    return lca_tree_query(1, 0, (int)dfs_list.size() - 1, first[a], first[b]);
}

vector<int> first1, first2;
vector<char> edge_used;
vector<int> tree1, tree2;

void query_prepare(int n) {
    first1.resize(n - 1, -1);
    first2.resize(n - 1, -1);
    for (int i = 0; i < (int)edges_list.size(); ++i) {
        int j = edges_list[i];
        if (first1[j] == -1)
            first1[j] = i;
        else
            first2[j] = i;
    }

    edge_used.resize(n - 1);
    tree1.resize(edges_list.size() * 8);
    tree2.resize(edges_list.size() * 8);
}

void sum_tree_update(vector<int>& tree, int i, int l, int r, int j, int delta) {
    tree[i] += delta;
    if (l < r) {
        int m = (l + r) >> 1;
        if (j <= m)
            sum_tree_update(tree, i + i, l, m, j, delta);
        else
            sum_tree_update(tree, i + i + 1, m + 1, r, j, delta);
    }
}

int sum_tree_query(const vector<int>& tree, int i, int tl, int tr, int l, int r) {
    if (l > r || tl > tr)
        return 0;
    if (tl == l && tr == r)
        return tree[i];
    int m = (tl + tr) >> 1;
    if (r <= m)
        return sum_tree_query(tree, i + i, tl, m, l, r);
    if (l > m)
        return sum_tree_query(tree, i + i + 1, m + 1, tr, l, r);
    return sum_tree_query(tree, i + i, tl, m, l, m) +
           sum_tree_query(tree, i + i + 1, m + 1, tr, m + 1, r);
}

int query(int v1, int v2) {
    return sum_tree_query(tree1, 1, 0, (int)edges_list.size() - 1, first[v1], first[v2] - 1) -
           sum_tree_query(tree2, 1, 0, (int)edges_list.size() - 1, first[v1], first[v2] - 1);
}

int main() {
    // reading the graph
    int n;
    scanf("%d", &n);
    graph g(n), edge_ids(n);
    for (int i = 0; i < n - 1; ++i) {
        int v1, v2;
        scanf("%d%d", &v1, &v2);
        --v1, --v2;
        g[v1].push_back(v2);
        g[v2].push_back(v1);
        edge_ids[v1].push_back(i);
        edge_ids[v2].push_back(i);
    }

    h.assign(n, -1);
    dfs(0, g, edge_ids);
    lca_prepare(n);
    query_prepare(n);

    for (;;) {
        if () {
            // request for painting edge x;
            // if start = true, then the edge is painted, otherwise the painting
            // is removed
            edge_used[x] = start;
            sum_tree_update(tree1, 1, 0, (int)edges_list.size() - 1, first1[x],
                            start ? 1 : -1);
            sum_tree_update(tree2, 1, 0, (int)edges_list.size() - 1, first2[x],
                            start ? 1 : -1);
        } else {
            // query the number of colored edges on the path between v1 and v2
            int l = lca(v1, v2);
            int result = query(l, v1) + query(l, v2);
            // result - the answer to the request
        }
    }
}
```
