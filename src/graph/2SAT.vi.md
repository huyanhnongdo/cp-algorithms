---
tags:
  - Translated
e_maxx_link: 2_sat
lang: vi
---

# 2-SAT

SAT (Bài toán thỏa mãn công thức Boolean - Boolean satisfiability problem) là bài toán gán các giá trị Boolean cho các biến để thỏa mãn một công thức Boolean cho trước.
Công thức Boolean thường được cho dưới dạng CNF (dạng chuẩn hội - conjunctive normal form), là hội của nhiều mệnh đề, trong đó mỗi mệnh đề là tuyển của các biến hoặc phủ định của biến (literal).
2-SAT (2-satisfiability) là một trường hợp hạn chế của bài toán SAT, trong đó mỗi mệnh đề có chính xác hai literal.
Dưới đây là một ví dụ về bài toán 2-SAT như vậy.
Tìm một cách gán trị cho $a, b, c$ sao cho công thức sau nhận giá trị đúng (true):

$$(a \lor \lnot b) \land (\lnot a \lor b) \land (\lnot a \lor \lnot b) \land (a \lor \lnot c)$$

SAT là một bài toán NP-đầy đủ, hiện chưa có giải pháp hiệu quả nào được biết đến cho nó.
Tuy nhiên, bài toán 2-SAT có thể được giải quyết hiệu quả trong thời gian $O(n + m)$, với $n$ là số lượng biến và $m$ là số lượng mệnh đề.

## Thuật toán:

Trước tiên chúng ta cần chuyển đổi bài toán sang một dạng khác, gọi là dạng chuẩn kéo theo (implicative normal form).
Lưu ý rằng biểu thức $a \lor b$ tương đương với $\lnot a \Rightarrow b \land \lnot b \Rightarrow a$ (nếu một trong hai biến là sai, thì biến còn lại bắt buộc phải đúng).

Bây giờ chúng ta xây dựng một đồ thị có hướng đại diện cho các phép kéo theo này:
với mỗi biến $x$ sẽ có hai đỉnh $v_x$ và $v_{\lnot x}$.
Các cạnh sẽ tương ứng với các phép kéo theo.

Hãy xem xét ví dụ ở dạng 2-CNF:

$$(a \lor \lnot b) \land (\lnot a \lor b) \land (\lnot a \lor \lnot b) \land (a \lor \lnot c)$$

Đồ thị có hướng sẽ chứa các đỉnh và cạnh sau:

$$\begin{array}{cccc}
\lnot a \Rightarrow \lnot b & a \Rightarrow b & a \Rightarrow \lnot b & \lnot a \Rightarrow \lnot c\\
b \Rightarrow a & \lnot b \Rightarrow \lnot a & b \Rightarrow \lnot a & c \Rightarrow a
\end{array}$$

Bạn có thể quan sát đồ thị kéo theo trong hình dưới đây:

<div style="text-align: center;" markdown="1">

![Implication Graph of 2-SAT example](2SAT.png)

</div>

Một tính chất quan trọng của đồ thị kéo theo đáng để chúng ta chú ý là:
nếu tồn tại cạnh $a \Rightarrow b$, thì chắc chắn cũng tồn tại cạnh $\lnot b \Rightarrow \lnot a$.

Cũng cần lưu ý rằng, nếu từ $\lnot x$ có thể đi tới $x$, và từ $x$ cũng có thể đi tới $\lnot x$, thì bài toán vô nghiệm.
Dù chúng ta chọn giá trị nào cho biến $x$, nó luôn dẫn đến mâu thuẫn - nếu gán $x = \text{true}$ thì phép kéo theo chỉ ra rằng $\lnot x$ cũng phải bằng $\text{true}$ và ngược lại.
Hóa ra điều kiện này không chỉ là cần thiết, mà còn là đủ.
Chúng ta sẽ chứng minh điều này ở các đoạn dưới đây.
Đầu tiên, hãy nhắc lại rằng nếu một đỉnh có thể đi tới đỉnh thứ hai, và đỉnh thứ hai cũng có thể đi tới đỉnh thứ nhất, thì hai đỉnh này nằm trong cùng một thành phần liên thông mạnh.
Do đó, chúng ta có thể phát biểu tiêu chí tồn tại nghiệm như sau:

Để bài toán 2-SAT có nghiệm, điều kiện cần và đủ là với mọi biến $x$, hai đỉnh $x$ và $\lnot x$ phải thuộc các thành phần liên thông mạnh khác nhau trên đồ thị kéo theo.

Tiêu chí này có thể được kiểm tra trong thời gian $O(n + m)$ bằng cách tìm tất cả các thành phần liên thông mạnh.

Hình dưới đây cho thấy tất cả các thành phần liên thông mạnh của ví dụ nêu trên.
Như chúng ta có thể kiểm tra dễ dàng, không có thành phần nào trong số bốn thành phần liên thông mạnh chứa cả đỉnh $x$ và phủ định của nó $\lnot x$, do đó ví dụ này có nghiệm.
Chúng ta sẽ học cách tính toán bộ giá trị hợp lệ trong các đoạn tiếp theo, nhưng chỉ để minh họa, lời giải ở đây là $a = \text{false}$, $b = \text{false}$, $c = \text{false}$.

<div style="text-align: center;" markdown="1">

![Strongly Connected Components of the 2-SAT example](2SAT_SCC.png)

</div>

Bây giờ chúng ta xây dựng thuật toán tìm nghiệm của bài toán 2-SAT với giả định rằng nghiệm tồn tại.

Lưu ý rằng, mặc dù nghiệm tồn tại, việc $\lnot x$ có thể đi tới được từ $x$ trên đồ thị kéo theo vẫn có thể xảy ra, hoặc ngược lại (nhưng không xảy ra đồng thời) $x$ có thể đi tới được từ $\lnot x$.
Trong trường hợp đó, việc chọn $\text{true}$ hay $\text{false}$ cho $x$ sẽ dẫn đến mâu thuẫn, trong khi lựa chọn còn lại thì không.
Hãy tìm hiểu cách chọn giá trị để không tạo ra mâu thuẫn.

Hãy sắp xếp các thành phần liên thông mạnh theo thứ tự topo (tức là $\text{comp}[v] \le \text{comp}[u]$ nếu có đường đi từ $v$ đến $u$) và gọi $\text{comp}[v]$ là chỉ số của thành phần liên thông mạnh chứa đỉnh $v$.
Khi đó, nếu $\text{comp}[x] < \text{comp}[\lnot x]$, chúng ta gán $x$ bằng $\text{false}$, và ngược lại gán bằng $\text{true}$.

Hãy chứng minh rằng việc gán giá trị như thế này không dẫn đến mâu thuẫn.
Giả sử $x$ được gán bằng $\text{true}$.
Trường hợp còn lại có thể chứng minh hoàn toàn tương tự.

Đầu tiên chúng ta chứng minh rằng từ đỉnh $x$ không thể đi tới đỉnh $\lnot x$.
Vì chúng ta đã gán giá trị $\text{true}$, nên chỉ số thành phần liên thông mạnh của $x$ phải lớn hơn chỉ số của thành phần chứa $\lnot x$.
Điều này có nghĩa là thành phần chứa $\lnot x$ nằm bên trái của thành phần chứa $x$ (theo thứ tự topo), do đó từ đỉnh sau không thể đi tới đỉnh trước.

Thứ hai, chúng ta chứng minh rằng không tồn tại biến $y$ nào sao cho cả hai đỉnh $y$ và $\lnot y$ đều có thể đi tới được từ $x$ trên đồ thị kéo theo.
Điều này nếu xảy ra sẽ tạo ra mâu thuẫn, vì $x = \text{true}$ sẽ kéo theo $y = \text{true}$ và $\lnot y = \text{true}$.
Hãy chứng minh điều này bằng phản chứng.
Giả sử cả $y$ và $\lnot y$ đều đi tới được từ $x$, khi đó theo tính chất của đồ thị kéo theo, $\lnot x$ sẽ đi tới được từ cả $y$ và $\lnot y$.
Theo tính chất bắc cầu, ta suy ra $\lnot x$ đi tới được từ $x$, mâu thuẫn với giả định ban đầu.

Như vậy, chúng ta đã xây dựng một thuật toán tìm các giá trị biến thỏa mãn với giả định rằng với mọi biến $x$, hai đỉnh $x$ và $\lnot x$ nằm ở các thành phần liên thông mạnh khác nhau.
Phần trên đã chỉ ra tính đúng đắn của thuật toán này.
Đồng thời, chúng ta cũng đã chứng minh tiêu chí tồn tại nghiệm nêu ở trên.

## Cài đặt:

Bây giờ chúng ta có thể cài đặt toàn bộ thuật toán.
Đầu tiên, chúng ta xây dựng đồ thị kéo theo và tìm tất cả các thành phần liên thông mạnh.
Điều này có thể thực hiện bằng thuật toán Kosaraju trong thời gian $O(n + m)$.
Trong lượt duyệt đồ thị thứ hai, thuật toán Kosaraju duyệt qua các thành phần liên thông mạnh theo thứ tự topo, do đó việc tính toán $\text{comp}[v]$ cho mỗi đỉnh $v$ là rất dễ dàng.

Sau đó, chúng ta có thể chọn giá trị gán cho $x$ bằng cách so sánh $\text{comp}[x]$ và $\text{comp}[\lnot x]$.
Nếu $\text{comp}[x] = \text{comp}[\lnot x]$, chúng ta trả về `false` để chỉ ra rằng không tồn tại bộ giá trị hợp lệ nào thỏa mãn bài toán 2-SAT.

Dưới đây là cài đặt giải bài toán 2-SAT cho đồ thị kéo theo $adj$ đã được xây dựng sẵn và đồ thị chuyển vị $adj^{\intercal}$ (trong đó hướng của mỗi cạnh được đảo ngược).
Trong đồ thị, các đỉnh có chỉ số $2k$ và $2k+1$ là hai đỉnh tương ứng với biến $k$, với $2k+1$ tương ứng với biến phủ định.

```{.cpp file=2sat}
struct TwoSatSolver {
    int n_vars;
    int n_vertices;
    vector<vector<int>> adj, adj_t;
    vector<bool> used;
    vector<int> order, comp;
    vector<bool> assignment;

    TwoSatSolver(int _n_vars) : n_vars(_n_vars), n_vertices(2 * n_vars), adj(n_vertices), adj_t(n_vertices), used(n_vertices), order(), comp(n_vertices, -1), assignment(n_vars) {
        order.reserve(n_vertices);
    }
    void dfs1(int v) {
        used[v] = true;
        for (int u : adj[v]) {
            if (!used[u])
                dfs1(u);
        }
        order.push_back(v);
    }

    void dfs2(int v, int cl) {
        comp[v] = cl;
        for (int u : adj_t[v]) {
            if (comp[u] == -1)
                dfs2(u, cl);
        }
    }

    bool solve_2SAT() {
        order.clear();
        used.assign(n_vertices, false);
        for (int i = 0; i < n_vertices; ++i) {
            if (!used[i])
                dfs1(i);
        }

        comp.assign(n_vertices, -1);
        for (int i = 0, j = 0; i < n_vertices; ++i) {
            int v = order[n_vertices - i - 1];
            if (comp[v] == -1)
                dfs2(v, j++);
        }

        assignment.assign(n_vars, false);
        for (int i = 0; i < n_vertices; i += 2) {
            if (comp[i] == comp[i + 1])
                return false;
            assignment[i / 2] = comp[i] > comp[i + 1];
        }
        return true;
    }

    void add_disjunction(int a, bool na, int b, bool nb) {
        // na and nb signify whether a and b are to be negated 
        a = 2 * a ^ na;
        b = 2 * b ^ nb;
        int neg_a = a ^ 1;
        int neg_b = b ^ 1;
        adj[neg_a].push_back(b);
        adj[neg_b].push_back(a);
        adj_t[b].push_back(neg_a);
        adj_t[a].push_back(neg_b);
    }

    static void example_usage() {
        TwoSatSolver solver(3); // a, b, c
        solver.add_disjunction(0, false, 1, true);  //     a  v  not b
        solver.add_disjunction(0, true, 1, true);   // not a  v  not b
        solver.add_disjunction(1, false, 2, false); //     b  v      c
        solver.add_disjunction(0, false, 0, false); //     a  v      a
        assert(solver.solve_2SAT() == true);
        auto expected = vector<bool>{{true, false, true}};
        assert(solver.assignment == expected);
    }
};
```

## Bài tập thực hành
 * [Codeforces: The Door Problem](http://codeforces.com/contest/776/problem/D)
 * [Kattis: Illumination](https://open.kattis.com/problems/illumination)
 * [UVA: Rectangles](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3081)
 * [Codeforces : Radio Stations](https://codeforces.com/problemset/problem/1215/F)
 * [CSES : Giant Pizza](https://cses.fi/problemset/task/1684)
 * [Codeforces: +-1](https://codeforces.com/contest/1971/problem/H)
 * [Gym: (C) Colorful Village](https://codeforces.com/gym/104772/problem/C)
 * [POI: Renovation](https://szkopul.edu.pl/problemset/problem/xNjwUvwdHQoQTFBrmyG8vD1O/site/?key=statement)
