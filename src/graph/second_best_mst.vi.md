---
tags:
  - Translated
---

# Cây khung nhỏ nhất thứ hai

Một Cây khung nhỏ nhất $T$ là một cây của đồ thị $G$ cho trước sao cho nó bao phủ tất cả các đỉnh và có tổng trọng số các cạnh nhỏ nhất trong số tất cả các cây khung có thể có của đồ thị.
Một cây khung nhỏ nhất thứ hai $T'$ là một cây khung có tổng trọng số các cạnh nhỏ thứ hai trong số tất cả các cây khung có thể có của đồ thị $G$.

## Nhận xét

Gọi $T$ là Cây khung nhỏ nhất của đồ thị $G$.
Ta có nhận xét rằng cây khung nhỏ nhất thứ hai chỉ khác $T$ đúng một cặp cạnh thay thế. (Để xem chứng minh cho phát biểu này, bạn có thể tham khảo bài toán 23-1 [tại đây](http://www-bcf.usc.edu/~shanghua/teaching/Spring2010/public_html/files/HW2_Solutions_A.pdf)).

Do đó, chúng ta cần tìm một cạnh mới $e_{new}$ không thuộc $T$ và thay thế nó bằng một cạnh thuộc $T$ (gọi là $e_{old}$) sao cho đồ thị mới $T' = (T \cup \{e_{new}\}) \setminus \{e_{old}\}$ là một cây khung và chênh lệch trọng số ($e_{new} - e_{old}$) là nhỏ nhất.

## Sử dụng thuật toán Kruskal

Chúng ta có thể sử dụng thuật toán Kruskal để tìm MST trước, sau đó thử loại bỏ từng cạnh trong MST và thay thế bằng một cạnh khác.

1. Sắp xếp các cạnh trong $O(E \log E)$, sau đó tìm MST bằng thuật toán Kruskal trong $O(E)$.
2. Với mỗi cạnh trong MST (chúng ta sẽ có $V-1$ cạnh), tạm thời loại bỏ nó khỏi danh sách cạnh để không thể chọn cạnh này nữa.
3. Sau đó, tiếp tục tìm MST trong $O(E)$ bằng các cạnh còn lại.
4. Thực hiện việc này cho tất cả các cạnh trong MST, và lấy kết quả tốt nhất.

Lưu ý: chúng ta không cần phải sắp xếp lại các cạnh ở Bước 3.

Do đó, tổng độ phức tạp thời gian sẽ là $O(E \log V + E + V E)$ = $O(V E)$.

## Quy về bài toán Tìm tổ tiên chung gần nhất (LCA)

Trong cách tiếp cận trước, chúng ta đã thử tất cả các khả năng loại bỏ một cạnh của MST.
Ở đây chúng ta sẽ làm điều ngược lại:
thử thêm từng cạnh chưa thuộc MST vào MST.

1. Sắp xếp các cạnh trong $O(E \log E)$, sau đó tìm MST bằng thuật toán Kruskal trong $O(E)$.
2. Với mỗi cạnh $e$ chưa thuộc MST, tạm thời thêm nó vào MST để tạo thành một chu trình. Chu trình này sẽ đi qua đỉnh LCA.
3. Tìm cạnh $k$ có trọng số lớn nhất trong chu trình đó mà khác $e$, bằng cách đi dọc các đỉnh cha của hai đầu cạnh $e$ lên đến đỉnh LCA.
4. Loại bỏ cạnh $k$ này để tạo thành một cây khung mới.
5. Tính chênh lệch trọng số $\delta = weight(e) - weight(k)$, và ghi nhớ giá trị này cùng với cạnh bị thay đổi.
6. Lặp lại bước 2 cho tất cả các cạnh khác, và trả về cây khung có chênh lệch trọng số nhỏ nhất so với MST.

Độ phức tạp thời gian của thuật toán phụ thuộc vào cách chúng ta tính toán các cạnh $k$ có trọng số lớn nhất ở bước 2.
Một cách để tính toán chúng hiệu quả trong $O(E \log V)$ là chuyển đổi bài toán này thành bài toán Tìm tổ tiên chung gần nhất (LCA).

Chúng ta sẽ tiền xử lý LCA bằng cách chọn gốc cho MST và tính trọng số cạnh lớn nhất cho mỗi nút trên đường đi tới các tổ tiên của chúng.
Việc này có thể thực hiện bằng phương pháp [Nhảy nhị phân](lca_binary_lifting.md) cho LCA.

Tổng độ phức tạp thời gian của phương pháp này là $O(E \log V)$.

Ví dụ:

<div style="text-align: center;" markdown="1">

![MST](second_best_mst_1.png)
![Second best MST](second_best_mst_2.png)
  <br />

*Trong hình, bên trái là MST và bên phải là cây khung nhỏ nhất thứ hai.*
</div>

Trong đồ thị đã cho, giả sử chúng ta đặt gốc của MST tại đỉnh màu xanh dương ở phía trên cùng, sau đó chạy thuật toán bằng cách bắt đầu chọn các cạnh không thuộc MST.
Giả sử cạnh được chọn đầu tiên là cạnh $(u, v)$ có trọng số 36.
Thêm cạnh này vào cây sẽ tạo ra một chu trình 36 - 7 - 2 - 34.

Bây giờ chúng ta sẽ tìm cạnh có trọng số lớn nhất trong chu trình này bằng cách tìm $\text{LCA}(u, v) = p$.
Chúng ta tính trọng số cạnh lớn nhất trên các đường đi từ $u$ đến $p$ và từ $v$ đến $p$.
Lưu ý: $\text{LCA}(u, v)$ cũng có thể trùng với $u$ hoặc $v$ trong một số trường hợp.
Trong ví dụ này, chúng ta sẽ tìm được cạnh có trọng số 34 là cạnh có trọng số lớn nhất trong chu trình.
Bằng cách loại bỏ cạnh này, chúng ta thu được một cây khung mới có chênh lệch trọng số chỉ là 2.

Sau khi thực hiện việc này cho toàn bộ các cạnh không thuộc MST ban đầu, chúng ta có thể thấy rằng đây cũng chính là cây khung nhỏ nhất thứ hai của toàn đồ thị.
Chọn cạnh có trọng số 14 sẽ làm tăng trọng số của cây thêm 7, chọn cạnh có trọng số 27 làm tăng thêm 14, chọn cạnh có trọng số 28 làm tăng thêm 21, và chọn cạnh có trọng số 39 sẽ làm tăng trọng số cây thêm 5.

## Cài đặt

```cpp
struct edge {
    int s, e, w, id;
    bool operator<(const struct edge& other) { return w < other.w; }
};
typedef struct edge Edge;

const int N = 2e5 + 5;
long long res = 0, ans = 1e18;
int n, m, a, b, w, id, l = 21;
vector<Edge> edges;
vector<int> h(N, 0), parent(N, -1), size(N, 0), present(N, 0);
vector<vector<pair<int, int>>> adj(N), dp(N, vector<pair<int, int>>(l));
vector<vector<int>> up(N, vector<int>(l, -1));

pair<int, int> combine(pair<int, int> a, pair<int, int> b) {
    vector<int> v = {a.first, a.second, b.first, b.second};
    int topTwo = -3, topOne = -2;
    for (int c : v) {
        if (c > topOne) {
            topTwo = topOne;
            topOne = c;
        } else if (c > topTwo && c < topOne) {
            topTwo = c;
        }
    }
    return {topOne, topTwo};
}

void dfs(int u, int par, int d) {
    h[u] = 1 + h[par];
    up[u][0] = par;
    dp[u][0] = {d, -1};
    for (auto v : adj[u]) {
        if (v.first != par) {
            dfs(v.first, u, v.second);
        }
    }
}

pair<int, int> lca(int u, int v) {
    pair<int, int> ans = {-2, -3};
    if (h[u] < h[v]) {
        swap(u, v);
    }
    for (int i = l - 1; i >= 0; i--) {
        if (h[u] - h[v] >= (1 << i)) {
            ans = combine(ans, dp[u][i]);
            u = up[u][i];
        }
    }
    if (u == v) {
        return ans;
    }
    for (int i = l - 1; i >= 0; i--) {
        if (up[u][i] != -1 && up[v][i] != -1 && up[u][i] != up[v][i]) {
            ans = combine(ans, combine(dp[u][i], dp[v][i]));
            u = up[u][i];
            v = up[v][i];
        }
    }
    ans = combine(ans, combine(dp[u][0], dp[v][0]));
    return ans;
}

int main(void) {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
        size[i] = 1;
    }
    for (int i = 1; i <= m; i++) {
        cin >> a >> b >> w; // 1-indexed
        edges.push_back({a, b, w, i - 1});
    }
    sort(edges.begin(), edges.end());
    for (int i = 0; i <= m - 1; i++) {
        a = edges[i].s;
        b = edges[i].e;
        w = edges[i].w;
        id = edges[i].id;
        if (unite_set(a, b)) { 
            adj[a].emplace_back(b, w);
            adj[b].emplace_back(a, w);
            present[id] = 1;
            res += w;
        }
    }
    dfs(1, 0, 0);
    for (int i = 1; i <= l - 1; i++) {
        for (int j = 1; j <= n; ++j) {
            if (up[j][i - 1] != -1) {
                int v = up[j][i - 1];
                up[j][i] = up[v][i - 1];
                dp[j][i] = combine(dp[j][i - 1], dp[v][i - 1]);
            }
        }
    }
    for (int i = 0; i <= m - 1; i++) {
        id = edges[i].id;
        w = edges[i].w;
        if (!present[id]) {
            auto rem = lca(edges[i].s, edges[i].e);
            if (rem.first != w) {
                if (ans > res + w - rem.first) {
                    ans = res + w - rem.first;
                }
            } else if (rem.second != -1) {
                if (ans > res + w - rem.second) {
                    ans = res + w - rem.second;
                }
            }
        }
    }
    cout << ans << "\n";
    return 0;
}
```

## Tài liệu tham khảo

1. Competitive Programming-3, tác giả Steven Halim
2. [web.mit.edu](http://web.mit.edu/6.263/www/quiz1-f05-sol.pdf)

## Bài tập

* [Codeforces - Minimum spanning tree for each edge](https://codeforces.com/problemset/problem/609/E)
