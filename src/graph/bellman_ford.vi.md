---
tags:
  - Translated
e_maxx_link: ford_bellman
lang: vi
---

# Thuật toán Bellman-Ford

**Đường đi ngắn nhất từ một nguồn với các cạnh có trọng số âm**

Cho một đồ thị có hướng có trọng số $G$ gồm $n$ đỉnh, $m$ cạnh, và một đỉnh nguồn $v$. Nhiệm vụ là tìm độ dài đường đi ngắn nhất từ đỉnh nguồn $v$ đến tất cả các đỉnh còn lại của đồ thị.

Không giống như thuật toán Dijkstra, thuật toán này có thể áp dụng cho cả các đồ thị chứa các cạnh có trọng số âm. Tuy nhiên, nếu đồ thị chứa chu trình âm (chu trình có tổng trọng số các cạnh là âm), thì rõ ràng đường đi ngắn nhất tới một số đỉnh có thể không tồn tại (do độ dài đường đi ngắn nhất giảm xuống vô cùng bé, tương đương bằng $-\infty$); dù vậy, thuật toán này có thể cải tiến để phát hiện sự hiện diện của chu trình âm, hoặc thậm chí khôi phục lại chu trình này.

Thuật toán mang tên của hai nhà khoa học Mỹ: Richard Bellman và Lester Ford. Ford thực chất đã phát minh ra thuật toán này vào năm 1956 trong quá trình nghiên cứu một bài toán toán học khác, bài toán đó sau cùng được quy về bài toán tìm đường đi ngắn nhất trên đồ thị, và Ford đã đưa ra phác thảo thuật toán để giải bài toán đó. Bellman vào năm 1958 đã công bố một bài viết dành riêng cho bài toán tìm đường đi ngắn nhất, và trong bài viết đó ông đã phát biểu rõ ràng thuật toán dưới dạng mà chúng ta biết đến ngày nay.

## Mô tả thuật toán

Trước hết, chúng ta giả định rằng đồ thị không chứa chu trình âm nào (cụ thể là chu trình âm đi tới được từ đỉnh nguồn $v$, còn đối với các chu trình âm không thể đi tới được, thuật toán không bị ảnh hưởng). Trường hợp đồ thị chứa chu trình âm sẽ được thảo luận ở một phần riêng biệt dưới đây.

Chúng ta tạo một mảng khoảng cách $d[0 \ldots n-1]$, mảng này sau khi chạy xong thuật toán sẽ lưu kết quả của bài toán. Ban đầu chúng ta gán: $d[v] = 0$, và tất cả các phần tử còn lại của $d[]$ bằng vô cùng $\infty$.

Thuật toán gồm một số giai đoạn (phase). Mỗi giai đoạn duyệt qua tất cả các cạnh của đồ thị, và thuật toán cố gắng thực hiện phép **tối ưu hóa** (relaxation) dọc theo mỗi cạnh $(a, b)$ có trọng số $c$. Phép tối ưu hóa dọc theo cạnh là nỗ lực nhằm cải thiện giá trị $d[b]$ bằng cách sử dụng giá trị $d[a] + c$. Thực chất, điều này có nghĩa là chúng ta cố gắng tối ưu hóa khoảng cách tới đỉnh $b$ thông qua cạnh $(a, b)$ và khoảng cách hiện tại tới đỉnh $a$.

Người ta chứng minh được rằng $n-1$ giai đoạn là đủ để tính toán chính xác độ dài của tất cả các đường đi ngắn nhất trên đồ thị (dưới điều kiện không có chu trình âm). Đối với các đỉnh không thể đi tới được từ nguồn, khoảng cách $d[]$ của chúng sẽ giữ nguyên bằng vô cùng $\infty$.

## Cài đặt

Không giống như nhiều thuật toán đồ thị khác, đối với thuật toán Bellman-Ford, cách biểu diễn đồ thị thuận tiện nhất là sử dụng một danh sách duy nhất chứa tất cả các cạnh (thay vì $n$ danh sách kề). Chúng ta bắt đầu cài đặt với cấu trúc `Edge` để đại diện cho các cạnh. Đầu vào của thuật toán là số đỉnh $n$, số cạnh $m$, danh sách cạnh $e$ và đỉnh nguồn $v$. Tất cả các đỉnh được đánh số từ $0$ đến $n-1$.

### Cài đặt đơn giản nhất

Hằng số $\rm INF$ biểu thị giá trị "vô cùng" — nó cần được chọn đủ lớn để lớn hơn mọi độ dài đường đi khả dĩ trên đồ thị.

```cpp
struct Edge {
    int a, b, cost;
};

int n, m, v;
vector<Edge> edges;
const int INF = 1000000000;

void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    for (int i = 0; i < n - 1; ++i)
        for (Edge e : edges)
            if (d[e.a] < INF)
                d[e.b] = min(d[e.b], d[e.a] + e.cost);
    // display d, for example, on the screen
}
```

Kiểm tra `if (d[e.a] < INF)` chỉ cần thiết nếu đồ thị chứa các cạnh có trọng số âm: nếu không có kiểm tra này, phép tối ưu hóa sẽ được thực hiện từ các đỉnh chưa thể đi tới được từ nguồn, dẫn đến việc xuất hiện các khoảng cách sai lệch có dạng $\infty - 1$, $\infty - 2$, v.v.

### Cài đặt cải tiến

Thuật toán này có thể được tăng tốc đáng kể trong thực tế: thông thường chúng ta thu được kết quả chính xác chỉ sau một vài giai đoạn đầu tiên, và việc tiếp tục chạy các giai đoạn còn lại chỉ gây lãng phí thời gian duyệt qua các cạnh. Vì thế, chúng ta duy trì một biến cờ để kiểm tra xem có bất kỳ thay đổi nào xảy ra trong giai đoạn hiện tại hay không. Nếu ở một giai đoạn nào đó không có khoảng cách nào được tối ưu hóa, thuật toán có thể dừng lại ngay lập tức. (Tối ưu hóa này không làm thay đổi độ phức tạp trong trường hợp xấu nhất, tức là vẫn có đồ thị yêu cầu chạy đủ $n-1$ giai đoạn, nhưng nó giúp tăng tốc độ đáng kể trong trường hợp trung bình, ví dụ trên các đồ thị ngẫu nhiên).

Với tối ưu hóa này, chúng ta không cần phải giới hạn số vòng lặp tối đa là $n-1$ một cách thủ công — thuật toán sẽ tự động dừng lại khi đạt trạng thái tối ưu.

```cpp
void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    for (;;) {
        bool any = false;

        for (Edge e : edges)
            if (d[e.a] < INF)
                if (d[e.b] > d[e.a] + e.cost) {
                    d[e.b] = d[e.a] + e.cost;
                    any = true;
                }

        if (!any)
            break;
    }
    // display d, for example, on the screen
}
```

### Khôi phục đường đi

Bây giờ hãy xem xét cách sửa đổi thuật toán để không chỉ tìm độ dài đường đi ngắn nhất mà còn có thể khôi phục lại đường đi đó.

Để làm điều này, chúng ta tạo thêm một mảng cha $p[0 \ldots n-1]$, trong đó với mỗi đỉnh chúng ta lưu trữ đỉnh cha của nó, tức là đỉnh liền trước nó trên đường đi ngắn nhất. Thực chất, đường đi ngắn nhất tới đỉnh $a$ chính là đường đi ngắn nhất tới đỉnh $p[a]$ được nối thêm đỉnh $a$ ở cuối đường đi.

Lưu ý rằng thuật toán hoạt động dựa trên logic: nó giả định khoảng cách ngắn nhất tới một đỉnh đã được tính toán, và cố gắng cải thiện khoảng cách tới các đỉnh kề từ đỉnh đó. Do đó, tại thời điểm tối ưu hóa thành công, chúng ta chỉ cần ghi nhớ đỉnh cha $p[]$, tức là đỉnh mà từ đó phép tối ưu hóa này được thực hiện.

Dưới đây là mã nguồn cài đặt thuật toán Bellman-Ford kèm khôi phục đường đi ngắn nhất tới một đỉnh đích $t$:

```cpp
void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    vector<int> p(n, -1);

    for (;;) {
        bool any = false;
        for (Edge e : edges)
            if (d[e.a] < INF)
                if (d[e.b] > d[e.a] + e.cost) {
                    d[e.b] = d[e.a] + e.cost;
                    p[e.b] = e.a;
                    any = true;
                }
        if (!any)
            break;
    }

    if (d[t] == INF)
        cout << "No path from " << v << " to " << t << ".";
    else {
        vector<int> path;
        for (int cur = t; cur != -1; cur = p[cur])
            path.push_back(cur);
        reverse(path.begin(), path.end());

        cout << "Path from " << v << " to " << t << ": ";
        for (int u : path)
            cout << u << ' ';
    }
}
```

Tại đây, xuất phát từ đỉnh đích $t$, chúng ta đi ngược qua các đỉnh cha cho đến khi gặp đỉnh nguồn (không có cha), và lưu tất cả các đỉnh này vào danh sách $\rm path$. Danh sách này là đường đi ngắn nhất từ $v$ đến $t$ nhưng theo thứ tự ngược, vì vậy chúng ta gọi hàm $\rm reverse()$ trên $\rm path$ rồi in kết quả ra màn hình.

## Chứng minh thuật toán

Đầu tiên, lưu ý rằng đối với tất cả các đỉnh $u$ không thể đi tới được từ nguồn, thuật toán hoạt động chính xác: nhãn khoảng cách $d[u]$ sẽ giữ nguyên bằng vô cùng (vì thuật toán Bellman-Ford sẽ tìm được đường đi tới mọi đỉnh liên thông với đỉnh nguồn $v$, và phép tối ưu hóa cho các đỉnh không liên thông còn lại sẽ không bao giờ được kích hoạt).

Chúng ta chứng minh khẳng định sau: Sau khi kết thúc giai đoạn thứ $i$, thuật toán Bellman-Ford tính toán chính xác tất cả các đường đi ngắn nhất có số lượng cạnh không vượt quá $i$.

Nói cách khác, với mỗi đỉnh $a$, gọi $k$ là số cạnh của đường đi ngắn nhất tới nó (nếu có nhiều đường đi như vậy, chọn một đường đi bất kỳ). Theo khẳng định trên, thuật toán đảm bảo rằng sau giai đoạn thứ $k$, đường đi ngắn nhất tới đỉnh $a$ sẽ được tìm thấy chính xác.

**Chứng minh**:
Xét một đỉnh $a$ bất kỳ có thể đi tới được từ đỉnh nguồn $v$, và xét một đường đi ngắn nhất tới nó là $(p_0=v, p_1, \ldots, p_k=a)$. Trước giai đoạn thứ nhất, đường đi ngắn nhất tới đỉnh $p_0 = v$ đã được tính chính xác (d[v] = 0). Trong giai đoạn thứ nhất, cạnh $(p_0, p_1)$ được thuật toán kiểm tra, và do đó khoảng cách tới đỉnh $p_1$ được tính chính xác sau giai đoạn thứ nhất. Lặp lại lập luận này $k$ lần, chúng ta thấy rằng sau giai đoạn thứ $k$, khoảng cách tới đỉnh $p_k = a$ được tính chính xác, đó là điều cần chứng minh.

Điểm cuối cùng cần lưu ý là bất kỳ đường đi ngắn nhất nào cũng không thể chứa nhiều hơn $n-1$ cạnh. Do đó, thuật toán chỉ cần thực hiện tối đa đến giai đoạn thứ $n-1$. Sau đó, chắc chắn không có phép tối ưu hóa nào có thể cải thiện thêm khoảng cách của bất kỳ đỉnh nào.

## Trường hợp đồ thị chứa chu trình âm

Ở trên chúng ta giả định rằng đồ thị không chứa chu trình âm nào. Khi đồ thị chứa chu trình âm, mọi thứ trở nên phức tạp hơn do khoảng cách tới các đỉnh thuộc chu trình này, cũng như khoảng cách tới các đỉnh có thể đi tới được từ chu trình đó không được xác định — chúng phải bằng âm vô cùng $(-\infty)$.

Dễ thấy thuật toán Bellman-Ford có thể thực hiện tối ưu hóa vô hạn lần giữa các đỉnh thuộc chu trình này và các đỉnh đi tới được từ nó. Do đó, nếu không giới hạn số giai đoạn tối đa là $n-1$, thuật toán sẽ chạy vô hạn và liên tục làm giảm khoảng cách tới các đỉnh này.

Từ đó chúng ta có **tiêu chí để phát hiện chu trình âm đi tới được từ đỉnh nguồn $v$**: nếu sau giai đoạn thứ $n-1$, chúng ta chạy thêm một giai đoạn nữa và nó vẫn thực hiện được ít nhất một phép tối ưu hóa, thì đồ thị chứa chu trình âm đi tới được từ $v$; ngược lại, chu trình như vậy không tồn tại.

Hơn nữa, nếu phát hiện chu trình âm, thuật toán Bellman-Ford có thể sửa đổi để tìm và khôi phục chu trình này dưới dạng một chuỗi các đỉnh. Để làm điều đó, chỉ cần ghi nhớ đỉnh cuối cùng $x$ mà tại đó phép tối ưu hóa xảy ra ở giai đoạn thứ $n$. Đỉnh này chắc chắn nằm trên chu trình âm hoặc đi tới được từ chu trình âm đó. Để tìm được một đỉnh chắc chắn nằm trên chu trình, xuất phát từ $x$, chúng ta đi ngược qua các đỉnh cha $n$ lần. Bằng cách này, chúng ta sẽ dừng lại ở một đỉnh $y$ chắc chắn thuộc chu trình âm. Chúng ta chỉ cần đi tiếp từ đỉnh này qua các đỉnh cha của nó cho đến khi quay lại chính đỉnh $y$ (điều này chắc chắn xảy ra vì phép tối ưu hóa trên chu trình âm diễn ra theo vòng tròn).

### Cài đặt:

```cpp
void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    vector<int> p(n, -1);
    int x;
    for (int i = 0; i < n; ++i) {
        x = -1;
        for (Edge e : edges)
            if (d[e.a] < INF)
                if (d[e.b] > d[e.a] + e.cost) {
                    d[e.b] = max(-INF, d[e.a] + e.cost);
                    p[e.b] = e.a;
                    x = e.b;
                }
    }

    if (x == -1)
        cout << "No negative cycle from " << v;
    else {
        int y = x;
        for (int i = 0; i < n; ++i)
            y = p[y];

        vector<int> path;
        for (int cur = y;; cur = p[cur]) {
            path.push_back(cur);
            if (cur == y && path.size() > 1)
                break;
        }
        reverse(path.begin(), path.end());

        cout << "Negative cycle: ";
        for (int u : path)
            cout << u << ' ';
    }
}
```

Do sự hiện diện của chu trình âm, qua $n$ bước lặp, khoảng cách có thể giảm xuống rất sâu dưới khoảng số âm (khoảng $-n m W$, với $W$ là trị tuyệt đối lớn nhất của trọng số cạnh trên đồ thị). Vì vậy trong đoạn mã, chúng ta áp dụng thêm biện pháp tránh tràn số nguyên như sau:

```cpp
d[e.b] = max(-INF, d[e.a] + e.cost);
```

Bản cài đặt ở trên tìm kiếm chu trình âm đi tới được từ đỉnh nguồn $v$ cho trước; tuy nhiên, thuật toán có thể sửa đổi để tìm bất kỳ chu trình âm nào trên đồ thị. Để làm điều này, chúng ta chỉ cần gán tất cả khoảng cách ban đầu $d[i] = 0$ thay vì vô cùng — giống như việc tìm đường đi ngắn nhất từ tất cả các đỉnh cùng một lúc; tính đúng đắn của việc phát hiện chu trình âm không bị ảnh hưởng.

Để biết thêm về chủ đề này — xem bài viết riêng [Tìm chu trình âm trong đồ thị](finding-negative-cycle-in-graph.md).

## Thuật toán tối ưu hóa đường đi ngắn nhất (SPFA)

SPFA (Shortest Path Faster Algorithm) là một cải tiến của thuật toán Bellman-Ford, tận dụng thực tế là không phải mọi lần thử tối ưu hóa cạnh đều thành công.
Ý tưởng chính là duy trì một hàng đợi chỉ chứa các đỉnh đã được tối ưu hóa khoảng cách và vẫn có khả năng tiếp tục tối ưu hóa các đỉnh kề của nó.
Bất cứ khi nào bạn tối ưu hóa được khoảng cách tới một đỉnh kề, bạn sẽ thêm đỉnh kề đó vào hàng đợi. Thuật toán này cũng có thể dùng để phát hiện chu trình âm tương tự như Bellman-Ford.

Trong trường hợp xấu nhất, độ phức tạp của thuật toán này vẫn bằng $O(n m)$ của Bellman-Ford, nhưng trong thực tế nó chạy nhanh hơn rất nhiều và [một số người khẳng định nó chạy trong thời gian trung bình $O(m)$](https://en.wikipedia.org/wiki/Shortest_Path_Faster_Algorithm#Average-case_performance). Tuy nhiên hãy cẩn thận, vì thuật toán này mang tính tất định và người ta có thể dễ dàng dựng các bộ dữ liệu thử nghiệm khiến thuật toán chạy mất $O(n m)$.

Cần lưu ý khi cài đặt: thuật toán sẽ chạy vô hạn nếu đồ thị chứa chu trình âm.
Để tránh điều này, chúng ta có thể đếm số lần một đỉnh được tối ưu hóa và dừng thuật toán ngay khi có một đỉnh bất kỳ được tối ưu hóa đến lần thứ $n$.
Ngoài ra, không cần thiết phải thêm một đỉnh vào hàng đợi nếu đỉnh đó đã có sẵn trong hàng đợi.

```{.cpp file=spfa}
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

bool spfa(int s, vector<int>& d) {
    int n = adj.size();
    d.assign(n, INF);
    vector<int> cnt(n, 0);
    vector<bool> inqueue(n, false);
    queue<int> q;

    d[s] = 0;
    q.push(s);
    inqueue[s] = true;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        inqueue[v] = false;

        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;

            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                if (!inqueue[to]) {
                    q.push(to);
                    inqueue[to] = true;
                    cnt[to]++;
                    if (cnt[to] > n)
                        return false;  // negative cycle
                }
            }
        }
    }
    return true;
}
```

## Bài tập áp dụng

Danh sách các bài toán có thể giải bằng thuật toán Bellman-Ford:

* [E-OLYMP #1453 "Ford-Bellman" [độ khó: thấp]](https://www.e-olymp.com/en/problems/1453)
* [UVA #423 "MPI Maelstrom" [độ khó: thấp]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=364)
* [UVA #534 "Frogger" [độ khó: trung bình]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=7&page=show_problem&problem=475)
* [UVA #10099 "The Tourist Guide" [độ khó: trung bình]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=12&page=show_problem&problem=1040)
* [UVA #515 "King" [độ khó: trung bình]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=456)
* [UVA 12519 - The Farnsworth Parabox](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3964)

Xem thêm danh sách bài tập tại bài viết [Tìm chu trình âm trong đồ thị](finding-negative-cycle-in-graph.md).
* [CSES - High Score](https://cses.fi/problemset/task/1673)
* [CSES - Cycle Finding](https://cses.fi/problemset/task/1197)
