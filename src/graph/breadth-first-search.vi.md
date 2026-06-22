---
tags:
  - Translated
e_maxx_link: bfs
lang: vi
---

# Tìm kiếm theo chiều rộng (Breadth-first search - BFS)

**Tìm kiếm theo chiều rộng (Breadth-first search - BFS)** là một trong những thuật toán duyệt và tìm kiếm cơ bản và thiết yếu trên đồ thị.

Kết quả của thuật toán này là đường đi tìm được bằng BFS tới bất kỳ đỉnh nào đều là đường đi ngắn nhất tới đỉnh đó, tức là đường đi chứa ít cạnh nhất trong đồ thị không trọng số.

Thuật toán hoạt động trong thời gian $O(n + m)$, với $n$ là số đỉnh và $m$ là số cạnh của đồ thị.

## Mô tả thuật toán

Thuật toán nhận đầu vào là một đồ thị không trọng số và đỉnh xuất phát $s$. Đồ thị đầu vào có thể là đồ thị có hướng hoặc vô hướng, điều này không ảnh hưởng đến hoạt động của thuật toán.

Thuật toán có thể được hình dung như một đám cháy lan truyền trên đồ thị: ở bước thứ 0, chỉ có đỉnh xuất phát $s$ bị cháy. Tại mỗi bước tiếp theo, ngọn lửa từ các đỉnh đang cháy sẽ lan truyền sang tất cả các đỉnh kề với chúng. Sau mỗi vòng lặp của thuật toán, "vòng lửa" sẽ mở rộng ra xa thêm một đơn vị khoảng cách (đó là lý do thuật toán có tên gọi duyệt theo chiều rộng).

Chính xác hơn, thuật toán hoạt động như sau: Khởi tạo một hàng đợi $q$ chứa các đỉnh sẽ được xử lý và một mảng boolean $used[]$ đánh dấu trạng thái một đỉnh đã bị cháy (được ghé thăm) hay chưa.

Ban đầu, đẩy đỉnh xuất phát $s$ vào hàng đợi, gán $used[s] = true$, và với tất cả các đỉnh $v$ còn lại, gán $used[v] = false$.
Sau đó lặp cho đến khi hàng đợi rỗng. Tại mỗi bước lặp, lấy một đỉnh ở đầu hàng đợi ra. Duyệt qua tất cả các cạnh đi ra từ đỉnh này. Nếu cạnh nối tới một đỉnh chưa bị cháy, ta đánh dấu đỉnh đó đã cháy ($used = true$) và đẩy nó vào hàng đợi.

Kết quả là khi hàng đợi rỗng, tất cả các đỉnh có thể đi tới được từ đỉnh xuất phát $s$ đều đã được duyệt qua, và mỗi đỉnh được tiếp cận theo con đường ngắn nhất có thể.
Chúng ta cũng có thể tính toán độ dài đường đi ngắn nhất (chỉ cần duy trì một mảng khoảng cách $d[]$) cũng như lưu thông tin để truy vết lại toàn bộ đường đi ngắn nhất (bằng cách duy trì mảng cha $p[]$, lưu đỉnh trực tiếp dẫn tới đỉnh hiện tại).

## Cài đặt

Dưới đây là mã nguồn thuật toán bằng C++ và Java.

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // adjacency list representation
    int n; // number of nodes
    int s; // source vertex

    queue<int> q;
    vector<bool> used(n);
    vector<int> d(n), p(n);

    q.push(s);
    used[s] = true;
    p[s] = -1;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : adj[v]) {
            if (!used[u]) {
                used[u] = true;
                q.push(u);
                d[u] = d[v] + 1;
                p[u] = v;
            }
        }
    }
    ```
=== "Java"
    ```java
    ArrayList<ArrayList<Integer>> adj = new ArrayList<>(); // adjacency list representation
        
    int n; // number of nodes
    int s; // source vertex


    LinkedList<Integer> q = new LinkedList<Integer>();
    boolean used[] = new boolean[n];
    int d[] = new int[n];
    int p[] = new int[n];

    q.push(s);
    used[s] = true;
    p[s] = -1;
    while (!q.isEmpty()) {
        int v = q.pop();
        for (int u : adj.get(v)) {
            if (!used[u]) {
                used[u] = true;
                q.push(u);
                d[u] = d[v] + 1;
                p[u] = v;
            }
        }
    }
    ```
    
Để truy vết và hiển thị đường đi ngắn nhất từ đỉnh nguồn $s$ tới đỉnh $u$, ta có thể thực hiện như sau:
    
=== "C++"
    ```cpp
    if (!used[u]) {
        cout << "No path!";
    } else {
        vector<int> path;
        for (int v = u; v != -1; v = p[v])
            path.push_back(v);
        reverse(path.begin(), path.end());
        cout << "Path: ";
        for (int v : path)
            cout << v << " ";
    }
    ```
=== "Java"
    ```java
    if (!used[u]) {
        System.out.println("No path!");
    } else {
        ArrayList<Integer> path = new ArrayList<Integer>();
        for (int v = u; v != -1; v = p[v])
            path.add(v);
        Collections.reverse(path);
        for(int v : path)
            System.out.println(v);
    }
    ```
    
## Ứng dụng của BFS

* Tìm đường đi ngắn nhất từ đỉnh nguồn tới các đỉnh khác trong đồ thị không trọng số.

* Tìm tất cả các thành phần liên thông trong đồ thị vô hướng trong thời gian $O(n + m)$:
Để làm việc này, ta thực hiện BFS bắt đầu từ mỗi đỉnh chưa được ghé thăm từ các lượt duyệt trước.
Nghĩa là chúng ta chạy BFS thông thường từ mỗi đỉnh, nhưng không reset mảng $used[]$ mỗi khi chuyển sang thành phần liên thông mới. Tổng thời gian chạy vẫn là $O(n + m)$ (việc chạy nhiều lần BFS mà không reset mảng $used[]$ gọi là chuỗi các phép tìm kiếm theo chiều rộng).

* Tìm lời giải cho một bài toán hoặc một trò chơi với số bước di chuyển ít nhất, nếu mỗi trạng thái của trò chơi có thể biểu diễn bằng một đỉnh của đồ thị và phép chuyển trạng thái đóng vai trò là các cạnh.

* Tìm đường đi ngắn nhất trên đồ thị có trọng số 0 hoặc 1:
Cách này chỉ cần sửa đổi nhẹ thuật toán BFS thông thường: thay vì dùng mảng $used[]$, ta sẽ kiểm tra xem khoảng cách mới tới đỉnh có ngắn hơn khoảng cách đã biết hay không. Nếu cạnh hiện tại có trọng số bằng 0, ta đẩy đỉnh mới vào đầu hàng đợi; ngược lại (trọng số bằng 1), ta đẩy vào cuối hàng đợi. Chi tiết về sửa đổi này được trình bày cụ thể trong bài viết [BFS 0-1 (0-1 BFS)](01_bfs.md).

* Tìm chu trình ngắn nhất trong đồ thị có hướng không trọng số:
Chạy BFS từ mỗi đỉnh trên đồ thị.
Ngay khi chúng ta cố gắng đi từ đỉnh hiện tại quay trở lại đỉnh xuất phát ban đầu, ta đã tìm được chu trình ngắn nhất chứa đỉnh xuất phát đó.
Tại thời điểm này, ta có thể dừng lượt chạy BFS hiện tại và bắt đầu lượt chạy BFS mới từ đỉnh tiếp theo.
Trong tất cả các chu trình tìm được (tối đa một chu trình từ mỗi đỉnh), chọn chu trình ngắn nhất.

* Tìm tất cả các cạnh nằm trên bất kỳ đường đi ngắn nhất nào giữa cặp đỉnh $(a, b)$ cho trước.
Để làm việc này, ta thực hiện hai phép duyệt BFS:
một từ $a$ và một từ $b$.
Gọi $d_a[]$ là mảng chứa khoảng cách ngắn nhất nhận được từ BFS xuất phát từ $a$, và $d_b[]$ là mảng khoảng cách ngắn nhất nhận được từ BFS xuất phát từ $b$.
Bây giờ, với mỗi cạnh $(u, v)$, dễ dàng kiểm tra xem cạnh đó có nằm trên đường đi ngắn nhất nào giữa $a$ và $b$ không bằng cách kiểm tra điều kiện: $d_a[u] + 1 + d_b[v] = d_a[b]$.

* Tìm tất cả các đỉnh nằm trên bất kỳ đường đi ngắn nhất nào giữa cặp đỉnh $(a, b)$ cho trước.
Tương tự như trên, thực hiện hai phép duyệt BFS từ $a$ và từ $b$.
Gọi $d_a[]$ là mảng khoảng cách từ $a$ và $d_b[]$ là mảng khoảng cách từ $b$.
Với mỗi đỉnh $v$, điều kiện để nó thuộc một đường đi ngắn nhất giữa $a$ và $b$ là: $d_a[v] + d_b[v] = d_a[b]$.

* Tìm hành trình (walk) ngắn nhất có độ dài chẵn từ đỉnh xuất phát $s$ tới đỉnh đích $t$ trên đồ thị không trọng số:
Để giải bài toán này, ta xây dựng đồ thị phụ có các đỉnh đại diện cho trạng thái $(v, c)$, trong đó $v$ là đỉnh hiện tại và $c \in \{0, 1\}$ đại diện cho tính chẵn lẻ của độ dài đường đi hiện tại.
Mỗi cạnh $(u, v)$ của đồ thị gốc sẽ được chuyển thành hai cạnh trên đồ thị phụ: nối giữa $((u, 0), (v, 1))$ và giữa $((u, 1), (v, 0))$.
Sau đó, ta chạy BFS để tìm đường đi ngắn nhất từ đỉnh bắt đầu $(s, 0)$ tới đỉnh kết thúc $(t, 0)$.
**Lưu ý**: Mục này sử dụng thuật ngữ "_hành trình (walk)_" thay vì "_đường đi (path)_" vì các đỉnh có thể bị lặp lại trong hành trình tìm được để đảm bảo tổng độ dài của nó là một số chẵn. Bài toán tìm _đường đi (path)_ ngắn nhất có độ dài chẵn là bài toán NP-Khó (NP-Complete) trên đồ thị có hướng, nhưng [có thể giải được trong thời gian tuyến tính](https://onlinelibrary.wiley.com/doi/abs/10.1002/net.3230140403) trên đồ thị vô hướng với phương pháp phức tạp hơn rất nhiều.

## Bài tập thực hành

* [SPOJ: AKBAR](http://spoj.com/problems/AKBAR)
* [SPOJ: NAKANJ](http://www.spoj.com/problems/NAKANJ/)
* [SPOJ: WATER](http://www.spoj.com/problems/WATER)
* [SPOJ: MICE AND MAZE](http://www.spoj.com/problems/MICEMAZE/)
* [Timus: Caravans](http://acm.timus.ru/problem.aspx?space=1&num=2034)
* [DevSkill - Holloween Party (archived)](http://web.archive.org/web/20200930162803/http://www.devskill.com/CodingProblems/ViewProblem/60)
* [DevSkill - Ohani And The Link Cut Tree (archived)](http://web.archive.org/web/20170216192002/http://devskill.com:80/CodingProblems/ViewProblem/150)
* [SPOJ - Spiky Mazes](http://www.spoj.com/problems/SPIKES/)
* [SPOJ - Four Chips (hard)](http://www.spoj.com/problems/ADV04F1/)
* [SPOJ - Inversion Sort](http://www.spoj.com/problems/INVESORT/)
* [Codeforces - Shortest Path](http://codeforces.com/contest/59/problem/E)
* [SPOJ - Yet Another Multiple Problem](http://www.spoj.com/problems/MULTII/)
* [UVA 11392 - Binary 3xType Multiple](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2387)
* [UVA 10968 - KuPellaKeS](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1909)
* [Codeforces - Police Stations](http://codeforces.com/contest/796/problem/D)
* [Codeforces - Okabe and City](http://codeforces.com/contest/821/problem/D)
* [SPOJ - Find the Treasure](http://www.spoj.com/problems/DIGOKEYS/)
* [Codeforces - Bear and Forgotten Tree 2](http://codeforces.com/contest/653/problem/E)
* [Codeforces - Cycle in Maze](http://codeforces.com/contest/769/problem/C)
* [UVA - 11312 - Flipping Frustration](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2287)
* [SPOJ - Ada and Cycle](http://www.spoj.com/problems/ADACYCLE/)
* [CSES - Labyrinth](https://cses.fi/problemset/task/1193)
* [CSES - Message Route](https://cses.fi/problemset/task/1667/)
* [CSES - Monsters](https://cses.fi/problemset/task/1194)
