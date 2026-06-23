---
tags:
  - Translated
e_maxx_link: lca_linear_offline
lang: vi
---

# Tổ tiên chung gần nhất - Thuật toán ngoại tuyến của Tarjan

Chúng ta có một cây $G$ với $n$ nút và $m$ truy vấn có dạng $(u, v)$.
Với mỗi truy vấn $(u, v)$, chúng ta muốn tìm tổ tiên chung gần nhất (Lowest Common Ancestor - LCA) của hai đỉnh $u$ và $v$, tức là nút vừa là tổ tiên của cả $u$ và $v$ vừa có độ sâu lớn nhất trong cây.
Bản thân nút $v$ cũng được coi là tổ tiên của $v$, do đó LCA cũng có thể chính là một trong hai nút này.

Trong bài viết này, chúng ta sẽ giải quyết bài toán dưới dạng ngoại tuyến (off-line), tức là chúng ta giả định rằng tất cả các truy vấn đều đã được biết trước, và do đó chúng ta có thể trả lời chúng theo bất kỳ thứ tự nào mong muốn.
Thuật toán dưới đây cho phép trả lời toàn bộ $m$ truy vấn trong tổng thời gian $O(n + m)$, nghĩa là với $m$ đủ lớn, thời gian cho mỗi truy vấn sẽ là $O(1)$.

## Thuật toán

Thuật toán này được đặt tên theo Robert Tarjan, người đã phát hiện ra nó vào năm 1979 và cũng đóng góp rất nhiều vào cấu trúc dữ liệu [Hợp nhất tập rời rạc (DSU)](../data_structures/disjoint_set_union.md) - cấu trúc dữ liệu được sử dụng chính trong thuật toán này.

Thuật toán trả lời tất cả các truy vấn thông qua đúng một lần duyệt [DFS](depth-first-search.md) trên cây.
Cụ thể, truy vấn $(u, v)$ được trả lời tại nút $u$ nếu nút $v$ đã được ghé thăm trước đó, hoặc ngược lại.

Vì vậy, giả sử chúng ta hiện đang ở nút $v$, chúng ta đã thực hiện các lệnh gọi đệ quy DFS, và cũng đã ghé thăm nút thứ hai $u$ từ truy vấn $(u, v)$.
Chúng ta hãy xem cách tìm LCA của hai nút này.

Lưu ý rằng $\text{LCA}(u, v)$ có thể là nút $v$ hoặc một trong các tổ tiên của nó.
Do đó, chúng ta cần tìm nút thấp nhất trong số các tổ tiên của $v$ (tính cả $v$) sao cho nút $u$ là hậu duệ của nó.
Đồng thời, với một nút $v$ cố định, các nút đã ghé thăm của cây sẽ chia thành một họ các tập hợp rời rạc.
Mỗi tổ tiên $p$ của nút $v$ có một tập hợp riêng chứa chính nó và toàn bộ các cây con có gốc tại các nút con của nó không nằm trên đường đi từ $v$ đến gốc cây.
Tập hợp chứa nút $u$ sẽ xác định $\text{LCA}(u, v)$:
LCA chính là đại diện của tập hợp đó, cụ thể là nút nằm trên đường đi giữa $v$ và gốc cây.

Chúng ta chỉ cần học cách duy trì hiệu quả tất cả các tập hợp này.
Để làm được điều này, chúng ta áp dụng cấu trúc dữ liệu DSU.
Để có thể áp dụng kỹ thuật Hợp nhất theo hạng (Union by rank), chúng ta lưu trữ đại diện thực tế (nút nằm trên đường đi từ $v$ đến gốc cây) của mỗi tập hợp trong mảng `ancestor`.

Hãy thảo luận về việc cài đặt hàm DFS.
Giả sử chúng ta đang ghé thăm nút $v$.
Chúng ta đưa nút này vào một tập hợp mới trong DSU, `ancestor[v] = v`.
Như thường lệ, chúng ta duyệt qua tất cả các nút con của $v$.
Với mỗi nút con, trước tiên chúng ta phải gọi đệ quy DFS cho nó, rồi sau đó thêm nút này cùng toàn bộ cây con của nó vào tập hợp của $v$.
Điều này có thể được thực hiện bằng hàm `union_sets` và gán tiếp theo `ancestor[find_set(v)] = v` (điều này là cần thiết vì `union_sets` có thể thay đổi phần tử đại diện của tập hợp).

Cuối cùng, sau khi đã xử lý tất cả các nút con, chúng ta có thể trả lời mọi truy vấn dạng $(u, v)$ mà $u$ đã được ghé thăm.
Kết quả của truy vấn, tức là LCA của $u$ và $v$, sẽ là nút `ancestor[find_set(u)]`.
Dễ thấy rằng mỗi truy vấn sẽ chỉ được trả lời đúng một lần.

Hãy xác định độ phức tạp thời gian của thuật toán này.
Đầu tiên, chúng ta mất $O(n)$ do lượt duyệt DFS.
Thứ hai, chúng ta gọi hàm `union_sets` tổng cộng $n$ lần, tương ứng với $O(n)$.
Thứ ba, chúng ta gọi `find_set` cho mỗi truy vấn, tương ứng với $O(m)$.
Do đó, tổng độ phức tạp thời gian là $O(n + m)$, có nghĩa là với $m$ đủ lớn, độ phức tạp trung bình cho mỗi truy vấn là $O(1)$.

## Cài đặt

Dưới đây là cài đặt của thuật toán này.
Phần cài đặt DSU không được bao gồm ở đây, vì nó có thể được sử dụng trực tiếp mà không cần sửa đổi nào.

```cpp
vector<vector<int>> adj;
vector<vector<int>> queries;
vector<int> ancestor;
vector<bool> visited;

void dfs(int v)
{
    visited[v] = true;
    ancestor[v] = v;
    for (int u : adj[v]) {
        if (!visited[u]) {
            dfs(u);
            union_sets(v, u);
            ancestor[find_set(v)] = v;
        }
    }
    for (int other_node : queries[v]) {
        if (visited[other_node])
            cout << "LCA of " << v << " and " << other_node
                 << " is " << ancestor[find_set(other_node)] << ".\n";
    }
}

void compute_LCAs() {
    // initialize n, adj and DSU
    // for (each query (u, v)) {
    //    queries[u].push_back(v);
    //    queries[v].push_back(u);
    // }

    ancestor.resize(n);
    visited.assign(n, false);
    dfs(0);
}
```
