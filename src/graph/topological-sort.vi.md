---
tags:
  - Translated
e_maxx_link: topological_sort
lang: vi
---

# Sắp xếp topo (Topological Sorting)

Cho một đồ thị có hướng với $n$ đỉnh và $m$ cạnh.
Chúng ta cần tìm một **thứ tự sắp xếp các đỉnh** sao cho mỗi cạnh đều đi từ đỉnh có chỉ số nhỏ hơn đến đỉnh có chỉ số lớn hơn.

Nói cách khác, chúng ta muốn tìm một hoán vị của các đỉnh (**thứ tự topo**) tương thích với hướng của tất cả các cạnh trong đồ thị.

Dưới đây là một đồ thị minh họa cùng với thứ tự topo của nó:

<div style="text-align: center;" markdown="1">

![đồ thị có hướng ví dụ](topological_1.png)
![một thứ tự topo](topological_2.png)

</div>

Thứ tự topo có thể **không duy nhất** (ví dụ, nếu tồn tại ba đỉnh $a$, $b$, $c$ sao cho có đường đi từ $a$ đến $b$ và từ $a$ đến $c$ nhưng không có đường đi giữa $b$ và $c$).
Đồ thị ví dụ trên cũng có nhiều thứ tự topo, một thứ tự topo thứ hai như sau:
<div style="text-align: center;" markdown="1">

![thứ tự topo thứ hai](topological_3.png)

</div>

Thứ tự topo có thể **không tồn tại**.
Nó chỉ tồn tại nếu đồ thị có hướng không chứa chu trình.
Ngược lại, sẽ xảy ra mâu thuẫn: nếu có chu trình chứa các đỉnh $a$ và $b$, thì $a$ vừa phải đứng trước $b$ (vì có đường đi từ $a$ đến $b$) lại vừa phải đứng sau $b$ (vì có đường đi từ $b$ đến $a$).
Thuật toán được mô tả trong bài viết này cũng đồng thời chứng minh bằng cách xây dựng rằng mọi đồ thị có hướng không chu trình (DAG - Directed Acyclic Graph) đều có ít nhất một thứ tự topo.

Một bài toán thực tế thường gặp sử dụng sắp xếp topo là: Có $n$ biến chưa biết giá trị. Với một số cặp biến, chúng ta biết biến này nhỏ hơn biến kia. Chúng ta phải kiểm tra xem các ràng buộc này có mâu thuẫn hay không, và nếu không mâu thuẫn, hãy in các biến theo thứ tự tăng dần (nếu có nhiều kết quả hợp lệ, chỉ cần in một trong số đó). Dễ thấy đây chính xác là bài toán tìm thứ tự topo của đồ thị có $n$ đỉnh.

## Thuật toán

Để giải quyết bài toán này, chúng ta sẽ sử dụng [thuật toán tìm kiếm theo chiều sâu (depth-first search - DFS)](depth-first-search.md).

Giả thiết đồ thị không có chu trình. Hãy xem thuật toán DFS hoạt động như thế nào?

Khi bắt đầu từ một đỉnh $v$, DFS cố gắng đi theo tất cả các cạnh đi ra từ $v$.
Nó sẽ bỏ qua các cạnh có đỉnh đích đã được duyệt trước đó, và đi tiếp theo các cạnh còn lại để gọi đệ quy tại các đỉnh đích.

Do đó, tại thời điểm cuộc gọi hàm $\text{dfs}(v)$ hoàn thành, tất cả các đỉnh có thể đi tới từ $v$ (trực tiếp hoặc gián tiếp) đều đã được duyệt qua bởi thuật toán tìm kiếm.

Vì vậy, nếu chúng ta thêm đỉnh $v$ vào một danh sách khi kết thúc cuộc gọi $\text{dfs}(v)$, thì tất cả các đỉnh đi tới được từ $v$ đều đã nằm trong danh sách trước khi $v$ được thêm vào.
Chúng ta lặp lại điều này cho mỗi đỉnh của đồ thị, chạy qua một hoặc nhiều lượt DFS.
Với mỗi cạnh có hướng $v \rightarrow u$ trong đồ thị, đỉnh $u$ sẽ luôn xuất hiện trước đỉnh $v$ trong danh sách này, vì $u$ đi tới được từ $v$.
Do đó, nếu chúng ta đánh số các đỉnh trong danh sách này theo thứ tự từ cuối lên $n-1, n-2, \dots, 1, 0$, chúng ta sẽ thu được một thứ tự topo của đồ thị.
Nói cách khác, danh sách thu được chính là thứ tự topo đảo ngược.

Những giải thích này cũng có thể trình bày thông qua thời điểm hoàn thành (exit times) của thuật toán DFS.
Thời điểm hoàn thành của đỉnh $v$ là thời điểm cuộc gọi hàm $\text{dfs}(v)$ kết thúc (các thời điểm này có thể đánh số từ $0$ đến $n-1$).
Dễ hiểu là thời điểm hoàn thành của bất kỳ đỉnh $v$ nào cũng luôn lớn hơn thời điểm hoàn thành của bất kỳ đỉnh nào đi tới được từ nó (vì chúng được duyệt trước hoặc trong quá trình gọi $\text{dfs}(v)$). Do đó, thứ tự topo cần tìm chính là thứ tự các đỉnh xếp theo chiều giảm dần của thời điểm hoàn thành.

## Cài đặt

Dưới đây là mã nguồn cài đặt giả định đồ thị không có chu trình, tức là thứ tự topo luôn tồn tại. Nếu cần thiết, bạn có thể dễ dàng kiểm tra xem đồ thị có chu trình hay không như mô tả trong bài viết về [thuật toán tìm kiếm theo chiều sâu (DFS)](depth-first-search.md).

```cpp
int n; // number of vertices
vector<vector<int>> adj; // adjacency list of graph
vector<bool> visited;
vector<int> ans;

void dfs(int v) {
    visited[v] = true;
    for (int u : adj[v]) {
        if (!visited[u]) {
            dfs(u);
        }
    }
    ans.push_back(v);
}

void topological_sort() {
    visited.assign(n, false);
    ans.clear();
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    reverse(ans.begin(), ans.end());
}
```

Hàm chính của giải pháp là `topological_sort`, thực hiện khởi tạo các biến duyệt DFS, chạy DFS và nhận kết quả lưu tại vector `ans`. Cần lưu ý rằng khi đồ thị chứa chu trình, kết quả của `topological_sort` vẫn có ý nghĩa nhất định: nếu đỉnh $u$ đi tới được từ đỉnh $v$, nhưng không có chiều ngược lại, thì đỉnh $v$ sẽ luôn xuất hiện trước trong mảng kết quả. Tính chất này của bản cài đặt được ứng dụng trong [thuật toán Kosaraju](./strongly-connected-components.md) để tìm các thành phần liên thông mạnh và sắp xếp topo của chúng trong đồ thị có hướng chứa chu trình.

## Bài tập áp dụng

- [SPOJ TOPOSORT - Topological Sorting [độ khó: dễ]](http://www.spoj.com/problems/TOPOSORT/)
- [UVA 10305 - Ordering Tasks [độ khó: dễ]](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1246)
- [UVA 124 - Following Orders [độ khó: dễ]](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=60)
- [UVA 200 - Rare Order [độ khó: dễ]](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=136)
- [Codeforces 510C - Fox and Names [độ khó: dễ]](http://codeforces.com/problemset/problem/510/C)
- [SPOJ RPLA - Answer the boss!](https://www.spoj.com/problems/RPLA/)
- [CSES - Course Schedule](https://cses.fi/problemset/task/1679)
- [CSES - Longest Flight Route](https://cses.fi/problemset/task/1680)
- [CSES - Game Routes](https://cses.fi/problemset/task/1681)
