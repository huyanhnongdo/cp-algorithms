---
tags:
  - Translated
e_maxx_link: strong_connected_components
---

# Thành phần liên thông mạnh và Đồ thị ngưng tụ

## Định nghĩa

Cho một đồ thị có hướng $G=(V,E)$ với tập đỉnh $V$ và tập cạnh $E \subseteq V \times V$. Ta ký hiệu $n=|V|$ là số đỉnh và $m=|E|$ là số cạnh trong $G$. Việc mở rộng các định nghĩa trong bài viết này cho đa đồ thị là rất dễ dàng, nhưng chúng ta sẽ không đi sâu vào phần đó.

Một tập con các đỉnh $C \subseteq V$ được gọi là một **thành phần liên thông mạnh** (strongly connected component - SCC) nếu các điều kiện sau đây được thỏa mãn:

- với mọi $u,v\in C$, nếu $u \neq v$ thì tồn tại một đường đi từ $u$ đến $v$ và một đường đi từ $v$ đến $u$, và
- $C$ là tối đại (maximal), theo nghĩa là không thể thêm bất kỳ đỉnh nào khác vào mà không vi phạm điều kiện trên.

Ta ký hiệu $\text{SCC}(G)$ là tập hợp các thành phần liên thông mạnh của $G$. Các thành phần liên thông mạnh này không giao nhau và bao phủ toàn bộ các đỉnh trong đồ thị. Do đó, tập hợp $\text{SCC}(G)$ tạo thành một phân hoạch của $V$.

Xét đồ thị ví dụ $G_\text{example}$ dưới đây, trong đó các thành phần liên thông mạnh được làm nổi bật:

<div style="text-align: center;" markdown="1">

![drawing](strongly-connected-components-tikzpicture/graph.svg)

</div>

Ở đây chúng ta có $\text{SCC}(G_\text{example})=\{\{0,7\},\{1,2,3,5,6\},\{4,9\},\{8\}\}.$ Chúng ta có thể xác nhận rằng trong mỗi thành phần liên thông mạnh, tất cả các đỉnh đều có thể đi tới được từ nhau.

Chúng ta định nghĩa **đồ thị ngưng tụ** (condensation graph) $G^{\text{SCC}}=(V^{\text{SCC}}, E^{\text{SCC}})$ như sau:

- các đỉnh của $G^{\text{SCC}}$ là các thành phần liên thông mạnh của $G$; tức là, $V^{\text{SCC}} = \text{SCC}(G)$, và
- đối với mọi cặp đỉnh $C_i,C_j$ của đồ thị ngưng tụ, có một cạnh từ $C_i$ đến $C_j$ khi và chỉ khi $C_i \neq C_j$ và tồn tại $a\in C_i$ và $b\in C_j$ sao cho tồn tại một cạnh từ $a$ đến $b$ trong $G$.

Đồ thị ngưng tụ của $G_\text{example}$ trông như sau:

<div style="text-align: center;" markdown="1">

![drawing](strongly-connected-components-tikzpicture/cond_graph.svg)

</div>

Tính chất quan trọng nhất của đồ thị ngưng tụ là nó **không có chu trình** (acyclic). Thực vậy, đồ thị ngưng tụ theo định nghĩa không chứa các 'khuyên' (self-loops), và nếu có một chu trình đi qua hai hoặc nhiều đỉnh (thành phần liên thông mạnh) của đồ thị ngưng tụ, thì do tính liên thông, hợp của các thành phần liên thông mạnh này cũng phải là một thành phần liên thông mạnh: điều này mâu thuẫn với giả thiết tối đại.

Thuật toán mô tả trong phần tiếp theo tìm tất cả các thành phần liên thông mạnh của một đồ thị cho trước. Sau đó, đồ thị ngưng tụ có thể được xây dựng từ kết quả đó.

## Thuật toán Kosaraju

### Mô tả thuật toán

Thuật toán được mô tả dưới đây được đề xuất độc lập bởi Kosaraju và Sharir vào khoảng năm 1980. Nó dựa trên hai lượt duyệt [tìm kiếm theo chiều sâu](depth-first-search.md) (DFS), với thời gian chạy là $O(n + m)$.

Trong bước đầu tiên của thuật toán, chúng ta thực hiện một chuỗi các cuộc tìm kiếm theo chiều sâu (`dfs`) duyệt qua toàn bộ đồ thị. Nghĩa là, chừng nào vẫn còn đỉnh chưa được ghé thăm, chúng ta chọn một đỉnh trong số đó và bắt đầu tìm kiếm theo chiều sâu từ đỉnh đó. Với mỗi đỉnh, chúng ta ghi lại *thời điểm thoát* (exit time) $t_\text{out}[v]$. Đây là 'mốc thời gian' (timestamp) mà tại đó việc thực thi `dfs` trên đỉnh $v$ kết thúc, tức là thời điểm mà tất cả các đỉnh có thể đi tới từ $v$ đều đã được ghé thăm và thuật toán quay trở lại $v$. Bộ đếm mốc thời gian *không* được đặt lại giữa các lần gọi liên tiếp tới `dfs`. Thời điểm thoát đóng vai trò cốt lõi trong thuật toán, điều này sẽ trở nên rõ ràng hơn khi chúng ta thảo luận về định lý sau đây.

Đầu tiên, chúng ta định nghĩa thời điểm thoát $t_\text{out}[C]$ của một thành phần liên thông mạnh $C$ là giá trị lớn nhất của $t_\text{out}[v]$ với mọi $v \in C.$ Ngoài ra, trong chứng minh của định lý, chúng ta sẽ đề cập đến *thời điểm vào* (entry time) $t_{\text{in}}[v]$ của mỗi đỉnh $v\in G$. Giá trị $t_{\text{in}}[v]$ đại diện cho 'mốc thời gian' mà hàm đệ quy `dfs` được gọi trên đỉnh $v$ trong bước đầu tiên của thuật toán. Đối với một thành phần liên thông mạnh $C$, chúng ta định nghĩa $t_{\text{in}}[C]$ là giá trị nhỏ nhất của $t_{\text{in}}[v]$ với mọi $v \in C$.

!!! info "Định lý"

    Cho $C$ và $C'$ là hai thành phần liên thông mạnh khác nhau, và giả sử có một cạnh từ $C$ đến $C'$ trong đồ thị ngưng tụ. Khi đó, $t_\text{out}[C] > t_\text{out}[C']$.

??? note "Chứng minh"

    Có hai trường hợp khác nhau tùy thuộc vào thành phần nào được tìm kiếm theo chiều sâu ghé thăm trước:

    - Trường hợp 1: thành phần $C$ được ghé thăm trước (tức là $t_{\text{in}}[C] < t_{\text{in}}[C']$). Trong trường hợp này, tìm kiếm theo chiều sâu ghé thăm đỉnh $v \in C$ nào đó tại thời điểm mà toàn bộ các đỉnh khác của cả hai thành phần $C$ và $C'$ đều chưa được ghé thăm. Vì có một cạnh từ $C$ đến $C'$ trong đồ thị ngưng tụ, nên từ $v$ không những có thể đi tới toàn bộ các đỉnh khác trong $C$, mà còn có thể đi tới mọi đỉnh trong $C'$. Điều này có nghĩa là lượt thực thi `dfs` bắt đầu từ đỉnh $v$ này cũng sẽ ghé thăm toàn bộ các đỉnh của hai thành phần $C$ và $C'$ trong tương lai, nên các đỉnh này sẽ là con cháu của $v$ trong cây tìm kiếm theo chiều sâu. Điều này ngụ ý rằng với mỗi đỉnh $u \in (C \cup C')\setminus \{v\},$ chúng ta có $t_\text{out}[v] > t_\text{out}[u]$. Do đó, $t_\text{out}[C] > t_\text{out}[C']$, hoàn thành chứng minh cho trường hợp này.

    - Trường hợp 2: thành phần $C'$ được ghé thăm trước (tức là $t_{\text{in}}[C] > t_{\text{in}}[C']$). Trong trường hợp này, tìm kiếm theo chiều sâu ghé thăm đỉnh $v \in C'$ nào đó tại thời điểm mà tất cả các đỉnh khác của cả hai thành phần $C$ và $C'$ đều chưa được ghé thăm. Vì có một cạnh từ $C$ đến $C'$ trong đồ thị ngưng tụ, nên $C$ không thể đi tới được từ $C'$ theo tính chất không có chu trình của đồ thị ngưng tụ. Do đó, lượt thực thi `dfs` từ đỉnh $v$ sẽ không tiếp cận được bất kỳ đỉnh nào của $C$, nhưng nó sẽ ghé thăm toàn bộ các đỉnh của $C'$. Các đỉnh của $C$ sẽ được ghé thăm bởi một lượt thực thi `dfs` khác muộn hơn trong bước này của thuật toán, nên thực tế ta có $t_\text{out}[C] > t_\text{out}[C']$. Chứng minh hoàn tất.

Định lý vừa chứng minh là rất quan trọng để tìm các thành phần liên thông mạnh. Nó có nghĩa là bất kỳ cạnh nào trong đồ thị ngưng tụ cũng đều đi từ một thành phần có giá trị $t_\text{out}$ lớn hơn đến một thành phần có giá trị $t_\text{out}$ nhỏ hơn.

Nếu chúng ta sắp xếp tất cả các đỉnh $v \in V$ theo thứ tự giảm dần của thời điểm thoát $t_\text{out}[v]$, thì đỉnh đầu tiên $u$ sẽ thuộc về thành phần liên thông mạnh "gốc" (root), là thành phần không có cạnh đi vào trong đồ thị ngưng tụ. Bây giờ chúng ta muốn chạy một kiểu tìm kiếm nào đó từ đỉnh $u$ này sao cho nó chỉ ghé thăm các đỉnh trong cùng thành phần liên thông mạnh với nó mà không đi sang các đỉnh khác. Bằng cách lặp lại quy trình này, chúng ta có thể dần dần tìm được mọi thành phần liên thông mạnh: chúng ta loại bỏ tất cả các đỉnh thuộc thành phần vừa tìm được đầu tiên, sau đó chọn đỉnh còn lại có giá trị $t_\text{out}$ lớn nhất tiếp theo và chạy tìm kiếm từ đó, v.v. Cuối cùng, chúng ta sẽ tìm được tất cả các thành phần liên thông mạnh. Để tìm một phương pháp tìm kiếm hoạt động theo đúng mong muốn, chúng ta xem xét định lý sau:

!!! info "Định lý"

    Ký hiệu $G^T$ là *đồ thị chuyển vị* (transpose graph) của $G$, thu được bằng cách đảo ngược hướng các cạnh trong $G$. Khi đó, $\text{SCC}(G)=\text{SCC}(G^T)$. Hơn nữa, đồ thị ngưng tụ của $G^T$ là chuyển vị của đồ thị ngưng tụ của $G$.

Chứng minh của định lý này được lược bỏ (nhưng rất trực tiếp). Hệ quả của định lý này là: không có cạnh nào đi từ thành phần "gốc" sang các thành phần khác trong đồ thị chuyển vị $G^T$. Do đó, để duyệt qua toàn bộ thành phần liên thông mạnh "gốc" chứa đỉnh $v$, chúng ta chỉ cần chạy tìm kiếm theo chiều sâu bắt đầu từ đỉnh $v$ trên đồ thị chuyển vị $G^T$! Thao tác này sẽ ghé thăm chính xác toàn bộ các đỉnh của thành phần liên thông mạnh này. Như đã đề cập ở trên, sau đó chúng ta có thể loại bỏ các đỉnh này khỏi đồ thị. Tiếp theo, chọn đỉnh có giá trị $t_\text{out}[v]$ lớn nhất còn lại và chạy tìm kiếm trên đồ thị chuyển vị từ đỉnh đó để tìm thành phần liên thông mạnh tiếp theo. Lặp lại quy trình này, ta sẽ tìm ra toàn bộ các thành phần liên thông mạnh.

Tóm lại, thuật toán tìm các thành phần liên thông mạnh gồm các bước:

- Bước 1. Chạy một chuỗi các tìm kiếm theo chiều sâu trên $G$ để thu được một danh sách các đỉnh (ví dụ: `order`) được sắp xếp theo thứ tự thời điểm thoát $t_\text{out}$ tăng dần.

- Bước 2. Xây dựng đồ thị chuyển vị $G^T$, và chạy một chuỗi các tìm kiếm theo chiều sâu trên các đỉnh theo thứ tự ngược lại (tức là theo thứ tự thời điểm thoát giảm dần). Mỗi lượt tìm kiếm theo chiều sâu sẽ xác định một thành phần liên thông mạnh.

- Bước 3 (tùy chọn). Xây dựng đồ thị ngưng tụ.

Độ phức tạp thời gian chạy của thuật toán là $O(n + m)$ vì tìm kiếm theo chiều sâu được thực hiện hai lần. Việc dựng đồ thị ngưng tụ cũng tốn $O(n + m)$.

Cuối cùng, ở đây cũng nên đề cập đến [sắp xếp topo](topological-sort.md). Trong bước 1, chúng ta tìm các đỉnh theo thứ tự thời điểm thoát tăng dần. Nếu $G$ không có chu trình, điều này tương ứng với thứ tự sắp xếp topo ngược của $G$. Trong bước 2, thuật toán tìm các thành phần liên thông mạnh theo thứ tự thời điểm thoát giảm dần. Do đó, nó tìm ra các thành phần — tức là các đỉnh của đồ thị ngưng tụ — theo một thứ tự tương ứng với sắp xếp topo của đồ thị ngưng tụ.

### Cài đặt

```{.cpp file=strongly_connected_components}
vector<bool> visited; // keeps track of which vertices are already visited

// runs depth first search starting at vertex v.
// each visited vertex is appended to the output vector when dfs leaves it.
void dfs(int v, vector<vector<int>> const& adj, vector<int> &output) {
    visited[v] = true;
    for (auto u : adj[v])
        if (!visited[u])
            dfs(u, adj, output);
    output.push_back(v);
}

// input: adj -- adjacency list of G
// output: components -- the strongy connected components in G
// output: adj_cond -- adjacency list of G^SCC (by root vertices)
void strongly_connected_components(vector<vector<int>> const& adj,
                                  vector<vector<int>> &components,
                                  vector<vector<int>> &adj_cond) {
    int n = adj.size();
    components.clear(), adj_cond.clear();

    vector<int> order; // will be a sorted list of G's vertices by exit time

    visited.assign(n, false);

    // first series of depth first searches
    for (int i = 0; i < n; i++)
        if (!visited[i])
            dfs(i, adj, order);

    // create adjacency list of G^T
    vector<vector<int>> adj_rev(n);
    for (int v = 0; v < n; v++)
        for (int u : adj[v])
            adj_rev[u].push_back(v);

    visited.assign(n, false);
    reverse(order.begin(), order.end());

    vector<int> roots(n, 0); // gives the root vertex of a vertex's SCC

    // second series of depth first searches
    for (auto v : order)
        if (!visited[v]) {
            std::vector<int> component;
            dfs(v, adj_rev, component);
            components.push_back(component);
            int root = *component.begin();
            for (auto u : component)
                roots[u] = root;
        }

    // add edges to condensation graph
    adj_cond.assign(n, {});
    for (int v = 0; v < n; v++)
        for (auto u : adj[v])
            if (roots[v] != roots[u])
                adj_cond[roots[v]].push_back(roots[u]);
}
```

Hàm `dfs` thực hiện thuật toán tìm kiếm theo chiều sâu. Nó nhận vào danh sách kề và đỉnh bắt đầu. Nó cũng nhận tham chiếu đến vector `output`: mỗi đỉnh được ghé thăm sẽ được thêm vào cuối `output` khi `dfs` rời khỏi đỉnh đó.

Lưu ý rằng chúng ta sử dụng hàm `dfs` này trong cả bước thứ nhất và bước thứ hai của thuật toán. Trong bước thứ nhất, chúng ta truyền vào danh sách kề của $G$, và qua các lần gọi liên tiếp tới `dfs`, chúng ta tiếp tục truyền vào cùng một 'vector đầu ra' `order` để cuối cùng có được danh sách các đỉnh theo thứ tự thời điểm thoát tăng dần. Trong bước thứ hai, chúng ta truyền vào danh sách kề của $G^T$, và trong mỗi lần gọi, chúng ta truyền vào một 'vector đầu ra' rỗng `component` để thu được từng thành phần liên thông mạnh một.

## Thuật toán Tarjan tìm thành phần liên thông mạnh

### Mô tả thuật toán

Thuật toán được mô tả ở đây được đề xuất lần đầu tiên bởi Tarjan vào năm 1972.
Nó dựa trên việc thực hiện một chuỗi các cuộc gọi DFS, sử dụng thông tin nội tại trong cấu trúc của nó để xác định các thành phần liên thông mạnh (SCC), với thời gian chạy là $O(n+m)$.

Khi áp dụng DFS lên một đỉnh, chúng ta sẽ duyệt qua danh sách kề của nó, và trong trường hợp phát hiện một đỉnh chưa được ghé thăm, chúng ta sẽ gọi đệ quy DFS trên đỉnh đó.

Hãy xem xét cây được sinh ra bởi chuỗi các cuộc gọi DFS này, ta gọi đó là **cây DFS**.
Khi chúng ta gọi DFS lần đầu tiên trên một đỉnh thuộc một SCC nào đó, toàn bộ các đỉnh của SCC đó sẽ được ghé thăm trước khi cuộc gọi này kết thúc, bởi vì chúng đều có thể đi tới được lẫn nhau.
Trong cây DFS, đỉnh đầu tiên này sẽ là tổ tiên chung của tất cả các đỉnh khác thuộc SCC; chúng ta định nghĩa đỉnh này là **gốc của SCC** (root of the SCC).

!!! info "Định lý"

    Tất cả các đỉnh của một SCC tạo thành một đồ thị con liên thông của cây DFS.

??? note "Chứng minh"

    Chúng ta đã xác định rằng tất cả các đỉnh của một SCC đều có chung một tổ tiên, đó là đỉnh đầu tiên được ghé thăm bởi cuộc gọi DFS.
    Hãy xem xét một đỉnh $v$ và gốc của nó, đỉnh $r$.
    Mọi đỉnh trên đường đi từ $r$ đến $v$ đều thuộc cùng một SCC. Tất cả các đỉnh này đều đi tới được từ $r$, và tất cả chúng đều đi tới được $v$, và vì theo định nghĩa $v$ đi tới được $r$, nên tất cả các đỉnh này đều đi tới được nhau.
    Vì mọi đường đi từ một gốc đến mỗi đỉnh khác của SCC đều thuộc cùng một SCC, đồ thị con được tạo thành là liên thông.

Lưu ý rằng các SCC phân chia cây DFS thành các đồ thị con liên thông một cách hoàn hảo.

Ý tưởng của thuật toán như sau:

- Chúng ta thực hiện một chuỗi các cuộc gọi DFS, gọi đệ quy trên các đỉnh trong danh sách kề.

- Khi kết thúc việc duyệt danh sách kề của một đỉnh, bằng cách nào đó chúng ta có thể xác định đỉnh đó có phải là gốc hay không.
Phương pháp này sẽ được giải thích sau.

- Trong trường hợp đỉnh đó là gốc, chúng ta sẽ ngay lập tức xác định và lấy toàn bộ các đỉnh thuộc SCC của nó.

Khi tất cả các cuộc gọi kết thúc, toàn bộ các gốc sẽ được phát hiện và tất cả các đỉnh sẽ được gán vào SCC tương ứng của chúng.

Bây giờ chúng ta hãy phân tích các tính chất của DFS khi quy trình xác định này được đưa vào.

!!! info "Định lý"

    Xét đỉnh $v$ và giả sử chúng ta vừa kết thúc việc duyệt danh sách kề của nó.
    Tất cả các đỉnh chưa được nhận (unclaimed) trong cây con của nó đều thuộc về cùng một SCC.

??? note "Chứng minh"

    Thuật toán sẽ nhận các đỉnh của một SCC khi tìm thấy gốc của nó.
    Vì danh sách kề của $v$ đã được duyệt qua, tất cả các cuộc gọi DFS trên cây con của nó đã kết thúc, các gốc đã được phát hiện và các đỉnh thuộc SCC của chúng đã được nhận.
    Gốc của các đỉnh chưa được nhận còn lại sẽ là một tổ tiên có quy trình nhận chưa được thực hiện, vì vậy nó có thể là $v$ hoặc một tổ tiên của $v$.
    Vì $v$ nằm trên đường đi từ mọi đỉnh đến gốc của chúng và các SCC phải tạo thành một đồ thị con liên thông của cây, nên cả $v$ và tất cả các đỉnh chưa nhận còn lại đều thuộc cùng một SCC.

!!! info "Định lý"

    Xét đỉnh $v$ và giả sử chúng ta đang duyệt danh sách kề của nó, hiện tại đang xử lý cạnh $(v, u)$.
    Nếu $u$ đã được ghé thăm bởi một cuộc gọi DFS nào đó và vẫn chưa được nhận, thì $v$ và $u$ thuộc cùng một SCC.

??? note "Chứng minh"

    Có các trường hợp khác nhau tùy thuộc vào loại cạnh:

    - Cạnh cây DFS (Tree-edge): nếu đây là cạnh cây DFS, đây là lần đầu tiên chúng ta tìm thấy đỉnh $u$. Điều này có nghĩa là trước tiên chúng ta phải gọi đệ quy DFS trên $u$ và xem xét nó sau khi cuộc gọi DFS của nó hoàn thành. Nếu đỉnh $u$ vẫn chưa được nhận, gốc của nó có thể là $v$ hoặc một tổ tiên của $v$, do đó chúng phải thuộc cùng một SCC.

    - Cạnh ngược (Back-edge): đây là trường hợp đơn giản hơn, nếu $u$ là tổ tiên của $v$, chúng có thể đi tới được lẫn nhau và theo định nghĩa thuộc cùng một SCC.

    - Cạnh xuôi (Forward-edge): trước khi cạnh này được xử lý, đã có một chuỗi các cuộc gọi DFS kết thúc mà không tìm thấy gốc của $u$, sau đó quay lại $v$ và cuộc gọi DFS của $v$ tiếp tục chạy.
    Gốc của $u$ khi đó sẽ là một tổ tiên có quy trình nhận chưa được thực thi, vì vậy nó có thể là $v$ hoặc một tổ tiên của $v$, do đó chúng phải thuộc cùng một SCC.

    - Cạnh chéo (Cross-edge): tương tự, trước khi cạnh này được xử lý, đã có một chuỗi các cuộc gọi DFS kết thúc mà không tìm thấy gốc của $u$, quay trở lại một tổ tiên chung của $u$ và $v$ mà cuộc gọi DFS của tổ tiên đó tiếp tục thực thi và bắt đầu một chuỗi các cuộc gọi DFS mới dẫn đến cuộc gọi trên $v$.
    Gốc của $u$ khi đó sẽ là một tổ tiên có quy trình nhận chưa được thực thi, và tất cả các ứng cử viên khả dĩ đều là tổ tiên chung với $v$.
    Vì gốc của $u$ là tổ tiên của $v$, nó có thể đi tới $v$, và vì $v$ hiện tại có thể đi tới $u$, chúng phải thuộc cùng một SCC.

Lưu ý rằng khi hai đỉnh thuộc cùng một thành phần liên thông mạnh, gốc của chúng phải là tổ tiên chung của cả hai đỉnh.

!!! info "Định lý"

    Cho $v$ là một đỉnh. Các phát biểu sau đây là tương đương:

    1. Một đỉnh nào đó trong cây con của $v$ có thể đi tới một đỉnh chưa nhận ở ngoài cây con đó.
    2. $v$ không phải là gốc của một SCC.

??? note "Chứng minh"

    - $1. \implies 2.$:
    Giả sử một đỉnh $u$ nào đó trong cây con của $v$ có thể đi tới một đỉnh chưa nhận $w$ ở ngoài cây con đó.
    Chúng ta đã xác định rằng $u$ and $w$ thuộc cùng một SCC và gốc của chúng phải là tổ tiên chung của cả hai.
    Tổ tiên chung này bắt buộc phải nằm ngoài cây con, và nó cũng sẽ là tổ tiên của $v$.
    Vì $v$ nằm trên đường đi từ gốc đến $u$, nó phải thuộc cùng một SCC mà gốc của nó không phải là $v$.

    - $\neg 1. \implies \neg 2.$:
    Giả sử không có đỉnh nào trong cây con của $v$ có thể đi tới một đỉnh chưa nhận ở ngoài cây con.
    Điều này nghĩa là không có đỉnh nào trong cây con của $v$ đi tới được một tổ tiên của $v$.
    Các cạnh duy nhất có thể dẫn tới các đỉnh ngoài cây con là các cạnh chéo dẫn đến các đỉnh đã được nhận;
    các đỉnh này không thể đi tới bất kỳ tổ tiên nào của $v$, vì nếu đi tới được, chúng sẽ thuộc cùng một SCC với $v$, điều này là không thể vì SCC của chúng đã được xác định từ trước.
    Vì không có tổ tiên nào của $v$ có thể đi tới được từ cây con của nó, nên gốc của $v$ phải là chính $v$.

Bây giờ chúng ta cần tìm phương pháp cho phép xác định một đỉnh có phải là gốc hay không, và các tính chất của quy trình nhận là cần thiết cho tính đúng đắn của nó.
Để đạt được mục đích này, chúng ta định nghĩa thời điểm vào $t_{in}[v]$ cho mỗi đỉnh $v \in G$ tương ứng với 'mốc thời gian' mà DFS được gọi trên $v$.
Theo định nghĩa, gốc là đỉnh đầu tiên của một SCC được ghé thăm bởi DFS nên nó sẽ có giá trị $t_{in}$ nhỏ nhất trong SCC của nó.

Xét đỉnh $v$ và cây con của nó.
Tại thời điểm chúng ta kết thúc duyệt danh sách kề của nó, bất kỳ đỉnh nào đã được ghé thăm bởi DFS nằm ngoài cây con sẽ có giá trị $t_{in}$ nhỏ hơn, vì DFS được gọi trên chúng trước khi nó bắt đầu trên $v$.

Khi xem xét quy trình nhận, giá trị $t_{in}$ của tất cả các đỉnh chưa được nhận nằm ngoài cây con của $v$ đều nhỏ hơn $t_{in}[v]$.
Bây giờ chúng ta có thể thấy cách sử dụng $t_{in}$ để xác định các gốc.
Chúng ta xem xét giá trị nhỏ nhất của $t_{in}$ trong số các đỉnh chưa được nhận mà chúng ta có thể đi tới và lan truyền thông tin này lên các tổ tiên thông qua các cạnh cây DFS.
Chúng ta gọi giá trị được lan truyền này là $t_{low}$.

Cụ thể hơn, chúng ta định nghĩa $t_{low}[v]$ là giá trị $t_{in}$ nhỏ nhất mà một đỉnh trong cây con của $v$ có thể đi tới thông qua một cạnh trực tiếp.
Do đó, chúng ta có thể phát hiện xem một đỉnh $v$ có phải là gốc hay không bằng cách kiểm tra nếu $t_{low}[v] < t_{in}[v]$.

Cuối cùng, để nhận các đỉnh, có nhiều cách để thực hiện như sử dụng một thuật toán duyệt đồ thị khác, nhưng cũng có thể sử dụng một cấu trúc dữ liệu đơn giản để theo dõi các đỉnh chưa được nhận.
Để xác định cấu trúc dữ liệu này, hãy xem xét các thao tác mà nó cần thực hiện, chỉ gồm hai thao tác:

- Khi lần đầu tiên ghé thăm một đỉnh, chúng ta chỉ cần chèn nó vào cấu trúc dữ liệu, vì đỉnh này chưa được nhận.

- Khi tìm thấy một gốc, chúng ta cần tìm tất cả các đỉnh chưa nhận còn lại trong cây con của nó và loại bỏ chúng khỏi cấu trúc dữ liệu.

Chúng ta có thể tìm cách khác để mô tả thao tác loại bỏ bằng cách nhận thấy rằng ngay sau khi duyệt qua danh sách kề của đỉnh $v$, tất cả các đỉnh được đưa vào cấu trúc dữ liệu sau $v$ đều thuộc về cây con của nó.
If $v$ là gốc, tất cả các đỉnh còn lại được chèn vào sau $v$ phải được loại bỏ.
Vì vậy, thao tác loại bỏ có thể được mô tả như sau:

- Khi tìm thấy một gốc, chúng ta phải tìm và loại bỏ tất cả các đỉnh còn lại được chèn vào sau nó.

Bây giờ chúng ta có thể thấy rằng điều này có thể được cài đặt bằng một ngăn xếp (stack):

- Khi lần đầu ghé thăm một đỉnh, chúng ta đẩy (push) nó vào ngăn xếp.

- Khi tìm thấy một gốc, chúng ta lấy ra (pop) tất cả các phần tử cho đến khi lấy ra chính đỉnh gốc đó.

Điều này cuối cùng cho phép chúng ta cài đặt thuật toán.

Độ phức tạp thời gian chạy của chuỗi các cuộc gọi DFS là $O(n + m)$.
Xét về ngăn xếp, độ phức tạp của nó được tính khấu hao là $O(n)$ vì mỗi nút chỉ được đẩy vào và lấy ra đúng một lần.
Tổng độ phức tạp thời gian chạy do đó là $O(n + m)$.

Lưu ý thêm, các gốc được tìm thấy theo thứ tự topo đảo ngược.
Trong thuật toán, đỉnh là gốc nếu không có cạnh nào đi tới các đỉnh chưa được nhận bên ngoài cây con của nó, nghĩa là tất cả các thành phần đi tới được khác đều nằm trong cây con của nó (và do đó gốc của chúng đã được tìm thấy trước) hoặc chúng kết nối với các đỉnh đã được nhận ở ngoài cây con (gốc của chúng cũng đã được tìm thấy trước).
Vì vậy, tất cả các thành phần đi tới được đều đã được tìm thấy từ trước, nghĩa là chúng được đưa ra theo thứ tự topo đảo ngược hợp lệ của đồ thị ngưng tụ.

### Cài đặt

```{.cpp file=tarjan_scc}
vector<int> st;    // - stack holding the unclaimed vertices
vector<int> roots; // - keeps track of the SCC roots of the vertices
int timer;         // - dfs timestamp counter
vector<int> t_in;  // - keeps track of the dfs timestamp of the vertices
vector<int> t_low; // - keeps track of the lowest t_in of unclaimed vertices
                   // reachable in the subtree

// implements the tarjan algorithm for strongly connected components
void dfs(int v, vector<vector<int>> const &adj, vector<vector<int>> &components) {

  t_low[v] = t_in[v] = timer++;
  st.push_back(v);

  for (auto u : adj[v]) {
    if (t_in[u] == -1) { // tree-edge
      dfs(u, adj, components);
      t_low[v] = min(t_low[v], t_low[u]);
    } else if (roots[u] == -1) { // back-edge, cross-edge or forward-edge to an unclaimed vertex
      t_low[v] = min(t_low[v], t_in[u]);
    }
  }

  if (t_low[v] == t_in[v]) { // vertex is a root
    components.push_back({v}); // initializes a new component with root v
    while (true) {
      int u = st.back();
      st.pop_back();
      roots[u] = v; // claims the vertex
      if (u == v)
        break;
      components.back().push_back(u); // adds vertex u to the component of v
    }
  }
}

// input: adj -- adjacency list of G
// output: components -- the strongy connected components in G
// output: adj_cond -- adjacency list of G^SCC (by root vertices)
void strongly_connected_components(vector<vector<int>> const &adj,
                                   vector<vector<int>> &components,
                                   vector<vector<int>> &adj_cond) {
  components.clear();
  adj_cond.clear();

  int n = adj.size();

  st.clear();
  roots.assign(n, -1);
  timer = 0;
  t_in.assign(n, -1);
  t_low.assign(n, -1);

  // applies the tarjan algorithm to all the vertices
  // adds vertices to the components in reverse topological order
  for (int v = 0; v < n; v++) {
    if (t_in[v] == -1) {
      dfs(v, adj, components);
    }
  }

  // adds edges to the condensation graph
  adj_cond.assign(n, {});
  for (int v = 0; v < n; v++) {
    for (auto u : adj[v])
      if (roots[v] != roots[u])
        adj_cond[roots[v]].push_back(roots[u]);
  }
}
```

Chúng ta đã có một [bài nộp được chấp nhận](https://judge.yosupo.jp/submission/334251) với mã nguồn này trên Library Checker.

Lưu ý cuối cùng, có một cách khác để duyệt qua danh sách kề.
Hiện tại, chúng ta đang làm như sau:

```c++
for (auto u : adj[v]) {
  if (t_in[u] == -1) { // tree-edge
    dfs(u, adj);
    t_low[v] = min(t_low[v], t_low[u]);
  } else if (roots[u] == -1) { // back-edge, cross-edge or forward-edge to an unclaimed vertex
    t_low[v] = min(t_low[v], t_in[u]);
  }
}
```

Thay vào đó, chúng ta có thể làm:

```c++
for (auto u : adj[v]) {
  if (t_in[u] == -1) // vertex is not visited
    dfs(u, adj);
  if (roots[u] == -1) // vertex has not been claimed
    t_low[v] = min(t_low[v], t_low[u]);
}
```

Giá trị $t_{low}$ được sử dụng để lan truyền thông tin lên đỉnh gốc, và khi chúng ta thực hiện `t_low[v] = min(t_low[v], t_in[u])`, chúng ta biết rằng $u$ và $v$ thuộc cùng một SCC.
Nếu $t_{low}[u]$ được lan truyền cho đến gốc của $u$, nó cũng có thể được lan truyền qua $v$ vì chúng có chung một gốc.
Vì $t_{low}[u] \leq t_{in}[u]$, điều này không gây ra bất kỳ xung đột nào, thay vào đó chỉ cải thiện cận dưới của gốc của $v$.

## Xây dựng Đồ thị Ngưng tụ

Khi xây dựng danh sách kề của đồ thị ngưng tụ, chúng ta chọn *gốc* của mỗi thành phần làm đỉnh đầu tiên trong danh sách các đỉnh của nó (đây là một lựa chọn tùy ý). Đỉnh gốc này đại diện cho toàn bộ SCC của nó. Đối với mỗi đỉnh `v`, giá trị `roots[v]` cho biết đỉnh gốc của SCC mà `v` thuộc về.

Đồ thị ngưng tụ của chúng ta hiện được cho bởi các đỉnh `components` (một thành phần liên thông mạnh tương ứng với một đỉnh trong đồ thị ngưng tụ), và danh sách kề được cho bởi `adj_cond`, chỉ sử dụng các đỉnh gốc của các thành phần liên thông mạnh. Lưu ý rằng chúng ta tạo ra một cạnh từ $C$ đến $C'$ trong $G^\text{SCC}$ cho mỗi cạnh từ một đỉnh $a\in C$ nào đó đến một đỉnh $b\in C'$ trong $G$ (nếu $C\neq C'$). Điều này có nghĩa là trong bản cài đặt của chúng ta, có thể tồn tại nhiều cạnh giữa hai thành phần trong đồ thị ngưng tụ.

## Tài liệu tham khảo

* Thomas Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein. Introduction to Algorithms [2005].
* M. Sharir. A strong-connectivity algorithm and its applications in data-flow analysis [1979].
* Robert Tarjan. Depth-first search and linear graph algorithms [1972].

## Bài tập luyện tập

* [SPOJ - Good Travels](http://www.spoj.com/problems/GOODA/)
* [SPOJ - Lego](http://www.spoj.com/problems/LEGO/)
* [Codechef - Chef and Round Run](https://www.codechef.com/AUG16/problems/CHEFRRUN)
* [UVA - 11838 - Come and Go](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2938)
* [UVA 247 - Calling Circles](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=183)
* [UVA 13057 - Prove Them All](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4955)
* [UVA 12645 - Water Supply](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4393)
* [UVA 11770 - Lighting Away](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2870)
* [UVA 12926 - Trouble in Terrorist Town](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4805)
* [UVA 11324 - The Largest Clique](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2299)
* [UVA 11709 - Trust groups](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2756)
* [UVA 12745 - Wishmaster](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4598)
* [SPOJ - True Friends](http://www.spoj.com/problems/TFRIENDS/)
* [SPOJ - Capital City](http://www.spoj.com/problems/CAPCITY/)
* [Codeforces - Scheme](http://codeforces.com/contest/22/problem/E)
* [SPOJ - Ada and Panels](http://www.spoj.com/problems/ADAPANEL/)
* [CSES - Flight Routes Check](https://cses.fi/problemset/task/1682)
* [CSES - Planets and Kingdoms](https://cses.fi/problemset/task/1683)
* [CSES - Coin Collector](https://cses.fi/problemset/task/1686)
* [Codeforces - Checkposts](https://codeforces.com/problemset/problem/427/C)
