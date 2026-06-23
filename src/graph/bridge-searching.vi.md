---
title: Tìm cầu của đồ thị trong O(N+M)
tags:
  - Translated
e_maxx_link: bridge_searching
---
# Tìm cầu của đồ thị trong $O(N+M)$

Cho một đồ thị vô hướng. Một **cầu** (bridge) được định nghĩa là một cạnh mà khi loại bỏ nó, đồ thị sẽ mất tính liên thông (hay nói một cách chính xác hơn là số thành phần liên thông của đồ thị sẽ tăng lên). Nhiệm vụ là tìm tất cả các cầu trong đồ thị đã cho.

Một cách trực quan, bài toán có thể được phát biểu như sau: cho bản đồ gồm các thành phố được kết nối bởi các con đường, hãy tìm tất cả các con đường "quan trạng", tức là các con đường mà khi loại bỏ sẽ làm biến mất đường đi giữa một cặp thành phố nào đó.

Thuật toán được mô tả ở đây dựa trên [tìm kiếm theo chiều sâu](depth-first-search.md) (DFS) và có độ phức tạp là $O(N+M)$, trong đó $N$ là số đỉnh và $M$ là số cạnh của đồ thị.

Lưu ý rằng còn có bài viết [Tìm cầu trực tuyến](bridge-searching-online.md) - khác với thuật toán ngoại tuyến (offline) được mô tả ở đây, thuật toán trực tuyến có thể duy trì danh sách tất cả các cầu trong một đồ thị thay đổi liên tục (giả sử rằng loại thay đổi duy nhất là thêm các cạnh mới).

## Thuật toán

Chọn một đỉnh bất kỳ làm $root$ và chạy [tìm kiếm theo chiều sâu](depth-first-search.md) từ đỉnh đó. Hãy lưu ý thực tế sau đây (rất dễ chứng minh):

- Giả sử chúng ta đang ở trong DFS, xem xét các cạnh đi ra từ đỉnh $v$. Cạnh hiện tại $(v, to)$ là một cầu khi và chỉ khi không có đỉnh $to$ hay bất kỳ đỉnh con cháu (descendants) nào của nó trong cây duyệt DFS có cạnh ngược (back-edge) đến đỉnh $v$ hoặc bất kỳ tổ tiên (ancestors) nào của $v$. Thực vậy, điều kiện này có nghĩa là không có con đường nào khác đi từ $v$ đến $to$ ngoại trừ cạnh $(v, to)$.

Bây giờ chúng ta cần kiểm tra tính chất này cho mỗi đỉnh một cách hiệu quả. Chúng ta sẽ sử dụng "thời điểm bắt đầu thăm đỉnh" được tính toán bởi thuật toán tìm kiếm theo chiều sâu.

Gọi $\mathtt{tin}[v]$ là thời điểm bắt đầu thăm đỉnh $v$. Chúng ta đưa vào một mảng $\mathtt{low}$ dùng để lưu thời điểm bắt đầu thăm nhỏ nhất của đỉnh mà từ $v$ có thể đi tới bằng tối đa một cạnh ngược từ chính nó hoặc từ các đỉnh con cháu của nó. $\mathtt{low}[v]$ là giá trị nhỏ nhất của $\mathtt{tin}[v]$, các thời điểm bắt đầu thăm $\mathtt{tin}[p]$ cho mỗi nút $p$ kết nối với $v$ qua cạnh ngược $(v, p)$ và các giá trị $\mathtt{low}[to]$ cho mỗi đỉnh $to$ là con trực tiếp của $v$ trong cây DFS:

$$\mathtt{low}[v] = \min \left\{ 
    \begin{array}{l}
    \mathtt{tin}[v] \\ 
    \mathtt{tin}[p]  &\text{ với mọi }p\text{ mà }(v, p)\text{ là cạnh ngược} \\ 
    \mathtt{low}[to] &\text{ với mọi }to\text{ mà }(v, to)\text{ là cạnh cây DFS}
    \end{array}
\right\}$$

Khi đó, tồn tại một cạnh ngược từ đỉnh $v$ hoặc một trong các con cháu của nó đến một trong các tổ tiên của nó khi và chỉ khi đỉnh $v$ có một đỉnh con $to$ thỏa mãn $\mathtt{low}[to] \leq \mathtt{tin}[v]$. Nếu $\mathtt{low}[to] = \mathtt{tin}[v]$, cạnh ngược đi trực tiếp đến $v$, ngược lại nó đi đến một trong các tổ tiên của $v$.

Do đó, cạnh hiện tại $(v, to)$ trong cây DFS là một cầu khi và chỉ khi $\mathtt{low}[to] > \mathtt{tin}[v]$.

## Cài đặt

Bản cài đặt cần phân biệt ba trường hợp: khi đi xuống một cạnh trong cây DFS, khi phát hiện một cạnh ngược đến một tổ tiên của đỉnh và khi quay trở lại đỉnh cha của đỉnh hiện tại. Cụ thể:

- $\mathtt{visited}[to] = false$ - cạnh thuộc cây DFS;
- $\mathtt{visited}[to] = true$ && $to \neq parent$ - cạnh ngược đến một trong các tổ tiên;
- $to = parent$ - cạnh dẫn ngược về đỉnh cha trong cây DFS.

Để cài đặt điều này, hàm tìm kiếm theo chiều sâu cần nhận thêm tham số là đỉnh cha của nút hiện tại.

Đối với trường hợp đồ thị có đa cạnh (multiple edges), chúng ta cần cẩn thận khi bỏ qua cạnh từ đỉnh cha. Để giải quyết vấn đề này, chúng ta có thể thêm một cờ `parent_skipped` để đảm bảo chỉ bỏ qua đỉnh cha đúng một lần.

```{.cpp file=bridge_searching_offline}
void IS_BRIDGE(int v,int to); // some function to process the found bridge
int n; // number of nodes
vector<vector<int>> adj; // adjacency list of graph

vector<bool> visited;
vector<int> tin, low;
int timer;
 
void dfs(int v, int p = -1) {
    visited[v] = true;
    tin[v] = low[v] = timer++;
    bool parent_skipped = false;
    for (int to : adj[v]) {
        if (to == p && !parent_skipped) {
            parent_skipped = true;
            continue;
        }
        if (visited[to]) {
            low[v] = min(low[v], tin[to]);
        } else {
            dfs(to, v);
            low[v] = min(low[v], low[to]);
            if (low[to] > tin[v])
                IS_BRIDGE(v, to);
        }
    }
}
 
void find_bridges() {
    timer = 0;
    visited.assign(n, false);
    tin.assign(n, -1);
    low.assign(n, -1);
    for (int i = 0; i < n; ++i) {
        if (!visited[i])
            dfs(i);
    }
}
```

Hàm chính là `find_bridges`; hàm này thực hiện các khởi tạo cần thiết và bắt đầu tìm kiếm theo chiều sâu trong mỗi thành phần liên thông của đồ thị.

Hàm `IS_BRIDGE(a, b)` là hàm xử lý thông tin khi phát hiện cạnh $(a, b)$ là một cầu, ví dụ như in nó ra màn hình.

Lưu ý rằng bản cài đặt này có thể hoạt động không chính xác nếu đồ thị có đa cạnh (multiple edges), vì nó bỏ qua chúng. Tất nhiên, đa cạnh không bao giờ có thể là cầu, vì thế `IS_BRIDGE` có thể kiểm tra thêm để đảm bảo cầu được báo cáo không phải là đa cạnh. Một cách khác là truyền vào `dfs` chỉ số của cạnh được sử dụng để đi vào đỉnh hiện tại thay vì đỉnh cha (và lưu lại chỉ số của tất cả các đỉnh).

## Bài tập luyện tập

- [UVA #796 "Critical Links"](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=737) [độ khó: thấp]
- [UVA #610 "Street Directions"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=551) [độ khó: trung bình]
- [Case of the Computer Network (Codeforces Round #310 Div. 1 E)](http://codeforces.com/problemset/problem/555/E) [độ khó: khó]
* [UVA 12363 - Hedge Mazes](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3785)
* [UVA 315 - Network](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=251)
* [GYM - Computer Network (J)](http://codeforces.com/gym/100114)
* [SPOJ - King Graffs Defense](http://www.spoj.com/problems/GRAFFDEF/)
* [SPOJ - Critical Edges](http://www.spoj.com/problems/EC_P/)
* [Codeforces - Break Up](http://codeforces.com/contest/700/problem/C)
* [Codeforces - Tourist Reform](http://codeforces.com/contest/732/problem/F)
* [Codeforces - Non-academic problem](https://codeforces.com/contest/1986/problem/F)
