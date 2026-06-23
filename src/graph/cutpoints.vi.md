---
title: Tìm khớp của đồ thị trong O(N+M)
tags:
  - Translated
e_maxx_link: cutpoints
---

# Tìm khớp của đồ thị trong $O(N+M)$

Cho một đồ thị vô hướng. Một **khớp** (hay **điểm cắt** - articulation point / cut vertex) được định nghĩa là một đỉnh mà khi loại bỏ nó cùng với các cạnh liên kết, đồ thị sẽ mất tính liên thông (hay nói một cách chính xác hơn là số thành phần liên thông của đồ thị sẽ tăng lên). Nhiệm vụ là tìm tất cả các khớp trong đồ thị đã cho.

Thuật toán được mô tả ở đây dựa trên [tìm kiếm theo chiều sâu](depth-first-search.md) (DFS) và có độ phức tạp là $O(N+M)$, trong đó $N$ là số đỉnh và $M$ là số cạnh của đồ thị.

## Thuật toán

Chọn một đỉnh bất kỳ làm $root$ và chạy [tìm kiếm theo chiều sâu](depth-first-search.md) từ đỉnh đó. Hãy lưu ý thực tế sau đây (rất dễ chứng minh):

- Giả sử chúng ta đang ở trong DFS, xem xét các cạnh đi ra từ đỉnh $v \ne root$.
  Nếu cạnh hiện tại $(v, to)$ thỏa mãn không có đỉnh $to$ hay bất kỳ đỉnh con cháu nào của nó trong cây duyệt DFS có cạnh ngược đến bất kỳ tổ tiên nào của $v$, thì $v$ là một khớp. Ngược lại, $v$ không phải là khớp.

- Xét trường hợp còn lại khi $v = root$.
  Đỉnh này sẽ là một khớp khi và chỉ khi nó có nhiều hơn một con trong cây DFS.

Bây giờ chúng ta cần kiểm tra tính chất này cho mỗi đỉnh một cách hiệu quả. Chúng ta sẽ sử dụng "thời điểm bắt đầu thăm đỉnh" được tính toán bởi thuật toán tìm kiếm theo chiều sâu.

Gọi $tin[v]$ là thời điểm bắt đầu thăm đỉnh $v$. Chúng ta đưa vào một mảng $low[v]$ để kiểm tra tính chất này cho mỗi đỉnh $v$. $low[v]$ là giá trị nhỏ nhất của $tin[v]$, thời điểm bắt đầu thăm $tin[p]$ của các đỉnh $p$ kết nối trực tiếp với $v$ qua cạnh ngược $(v, p)$, và các giá trị $low[to]$ của các đỉnh con trực tiếp $to$ của $v$ trong cây DFS:

$$low[v] = \min \begin{cases} tin[v] \\ tin[p] &\text{ với mọi }p\text{ mà }(v, p)\text{ là cạnh ngược} \\ low[to]& \text{ với mọi }to\text{ mà }(v, to)\text{ là cạnh cây DFS} \end{cases}$$

Khi đó, tồn tại một cạnh ngược từ đỉnh $v$ hoặc một trong các con cháu của nó đến một trong các tổ tiên của nó khi và chỉ khi đỉnh $v$ có một con $to$ thỏa mãn $low[to] < tin[v]$. Nếu $low[to] = tin[v]$, cạnh ngược đi trực tiếp đến $v$, ngược lại nó đi đến một trong các tổ tiên của $v$.

Do đó, đỉnh $v$ trong cây DFS là một khớp khi và chỉ khi $low[to] \geq tin[v]$.

## Cài đặt

Bản cài đặt cần phân biệt ba trường hợp: khi đi xuống một cạnh trong cây DFS, khi phát hiện một cạnh ngược đến một tổ tiên của đỉnh và khi quay trở lại đỉnh cha của đỉnh hiện tại. Cụ thể:

- $visited[to] = false$ - cạnh thuộc cây DFS;
- $visited[to] = true$ && $to \neq parent$ - cạnh ngược đến một trong các tổ tiên;
- $to = parent$ - cạnh dẫn ngược về đỉnh cha trong cây DFS.

Để cài đặt điều này, hàm tìm kiếm theo chiều sâu cần nhận thêm tham số là đỉnh cha của nút hiện tại.

```cpp
int n; // number of nodes
vector<vector<int>> adj; // adjacency list of graph

vector<bool> visited;
vector<int> tin, low;
int timer;
 
void dfs(int v, int p = -1) {
    visited[v] = true;
    tin[v] = low[v] = timer++;
    int children=0;
    for (int to : adj[v]) {
        if (to == p) continue;
        if (visited[to]) {
            low[v] = min(low[v], tin[to]);
        } else {
            dfs(to, v);
            low[v] = min(low[v], low[to]);
            if (low[to] >= tin[v] && p!=-1)
                IS_CUTPOINT(v);
            ++children;
        }
    }
    if(p == -1 && children > 1)
        IS_CUTPOINT(v);
}
 
void find_cutpoints() {
    timer = 0;
    visited.assign(n, false);
    tin.assign(n, -1);
    low.assign(n, -1);
    for (int i = 0; i < n; ++i) {
        if (!visited[i])
            dfs (i);
    }
}
```

Hàm chính là `find_cutpoints`; hàm này thực hiện các khởi tạo cần thiết và bắt đầu tìm kiếm theo chiều sâu trong mỗi thành phần liên thông của đồ thị.

Hàm `IS_CUTPOINT(a)` là hàm xử lý thông tin khi phát hiện đỉnh $a$ là một khớp, ví dụ như in nó ra màn hình. (Lưu ý rằng hàm này có thể được gọi nhiều lần cho cùng một đỉnh).

## Bài tập luyện tập

- [UVA #10199 "Tourist Guide"](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1140) [độ khó: thấp]
- [UVA #315 "Network"](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=5&page=show_problem&problem=251) [độ khó: thấp]
- [SPOJ - Submerging Islands](http://www.spoj.com/problems/SUBMERGE/)
- [Codeforces - Cutting Figure](https://codeforces.com/problemset/problem/193/A)
