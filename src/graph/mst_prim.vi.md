---
tags:
  - Translated
e_maxx_link: mst_prim
---

# Cây khung nhỏ nhất - Thuật toán Prim

Cho một đồ thị vô hướng có trọng số $G$ gồm $n$ đỉnh và $m$ cạnh.
Bạn muốn tìm một cây khung (spanning tree) của đồ thị này kết nối tất cả các đỉnh và có tổng trọng số nhỏ nhất (tức là tổng trọng số của các cạnh trong cây khung là tối thiểu).
Một cây khung là một tập hợp các cạnh sao cho bất kỳ đỉnh nào cũng có thể đi tới đỉnh khác bằng đúng một đường đi đơn duy nhất.
Cây khung có tổng trọng số nhỏ nhất được gọi là cây khung nhỏ nhất (minimum spanning tree - MST).

Trong hình bên trái, bạn có thể thấy một đồ thị vô hướng có trọng số, và ở hình bên phải là cây khung nhỏ nhất tương ứng.

<div style="text-align: center;" markdown="1">

![Đồ thị ngẫu nhiên](MST_before.png)
![MST của đồ thị](MST_after.png)

</div>

Dễ dàng thấy rằng bất kỳ cây khung nào cũng sẽ chứa đúng $n-1$ cạnh.

Bài toán này xuất hiện rất tự nhiên trong nhiều ứng dụng thực tế.
Ví dụ như bài toán sau:
có $n$ thành phố và với mỗi cặp thành phố, chúng ta được cho biết chi phí để xây dựng con đường nối giữa chúng (hoặc biết rằng không thể xây dựng con đường giữa hai thành phố đó do địa hình).
Chúng ta phải xây dựng các con đường sao cho từ thành phố bất kỳ đều có thể đi tới tất cả các thành phố khác, và tổng chi phí xây dựng đường là tối thiểu.

## Thuật toán Prim

Thuật toán này ban đầu được phát hiện bởi nhà toán học người Séc Vojtěch Jarník vào năm 1930.
Tuy nhiên, thuật toán này chủ yếu được biết đến với tên gọi Thuật toán Prim, theo tên của nhà toán học người Mỹ Robert Clay Prim, người đã phát hiện lại và công bố nó vào năm 1957.
Ngoài ra, Edsger Dijkstra cũng đã công bố thuật toán này vào năm 1959.

### Mô tả thuật toán

Ở đây chúng ta mô tả thuật toán ở dạng đơn giản nhất của nó.
Cây khung nhỏ nhất được xây dựng dần dần bằng cách thêm từng cạnh một tại mỗi bước.
Ban đầu, cây khung chỉ gồm một đỉnh duy nhất (được chọn ngẫu nhiên).
Sau đó, cạnh có trọng số nhỏ nhất đi ra từ đỉnh này được lựa chọn và thêm vào cây khung.
Sau thao tác đó, cây khung đã gồm hai đỉnh.
Bây giờ, chọn và thêm cạnh có trọng số nhỏ nhất có một đầu thuộc tập các đỉnh đã chọn (tức là các đỉnh đã thuộc cây khung), và đầu còn lại thuộc tập các đỉnh chưa chọn.
Và cứ tiếp tục như vậy, mỗi lần chúng ta chọn và thêm cạnh có trọng số nhỏ nhất kết nối một đỉnh đã chọn với một đỉnh chưa chọn.
Quy trình này được lặp lại cho đến khi cây khung chứa tất cả các đỉnh (hoặc tương đương khi chúng ta đã chọn được $n - 1$ cạnh).

Cuối cùng, cây khung thu được sẽ là tối tiểu.
Nếu đồ thị ban đầu không liên thông, thì không tồn tại cây khung, nên số cạnh được chọn sẽ ít hơn $n - 1$.

### Chứng minh

Giả sử đồ thị $G$ liên thông, tức là đáp án tồn tại.
Ta ký hiệu $T$ là đồ thị kết quả tìm được bởi thuật toán Prim, và $S$ là cây khung nhỏ nhất thực tế.
Rõ ràng $T$ thực sự là một cây khung và là đồ thị con của $G$.
Chúng ta chỉ cần chứng minh rằng tổng trọng số của $S$ và $T$ bằng nhau.

Xét lần đầu tiên trong thuật toán khi chúng ta thêm một cạnh vào $T$ mà cạnh đó không thuộc $S$.
Ta ký hiệu cạnh này là $e$, hai đầu của nó là $a$ và $b$, và tập hợp các đỉnh đã được chọn trước đó là $V$ ($a \in V$ và $b \notin V$, hoặc ngược lại).

Trong cây khung nhỏ nhất $S$, hai đỉnh $a$ và $b$ được kết nối bởi một đường đi $P$ nào đó.
Trên đường đi này, chúng ta có thể tìm thấy một cạnh $f$ sao cho một đầu của $f$ nằm trong $V$ và đầu còn lại nằm ngoài $V$.
Vì thuật toán đã chọn cạnh $e$ thay vì $f$, điều đó có nghĩa là trọng số của $f$ lớn hơn hoặc bằng trọng số của $e$.

Chúng ta thêm cạnh $e$ vào cây khung nhỏ nhất $S$ và loại bỏ cạnh $f$.
Khi thêm $e$, chúng ta tạo ra một chu trình đơn, và vì $f$ cũng là một phần của chu trình duy nhất này, nên khi loại bỏ nó, đồ thị thu được lại không có chu trình.
Và vì chúng ta chỉ loại bỏ một cạnh thuộc chu trình, đồ thị kết quả vẫn liên thông.

Cây khung mới thu được không thể có tổng trọng số lớn hơn, vì trọng số của $e$ không lớn hơn trọng số của $f$, và nó cũng không thể có tổng trọng số nhỏ hơn vì $S$ là cây khung nhỏ nhất.
Điều này nghĩa là bằng cách thay thế cạnh $f$ bằng $e$, chúng ta đã tạo ra một cây khung nhỏ nhất khác.
Và $e$ phải có cùng trọng số với $f$.

Do đó, tất cả các cạnh chúng ta chọn trong thuật toán Prim đều có trọng số bằng với các cạnh của một cây khung nhỏ nhất bất kỳ, nghĩa là thuật toán Prim thực sự tạo ra một cây khung nhỏ nhất.

## Cài đặt

Độ phức tạp của thuật toán phụ thuộc vào cách chúng ta tìm kiếm cạnh nhỏ nhất tiếp theo trong số các cạnh hợp lệ.
Có nhiều cách tiếp cận dẫn đến độ phức tạp và bản cài đặt khác nhau.

### Cài đặt thông thường: $O(n m)$ và $O(n^2 + m \log n)$

Nếu chúng ta tìm cạnh bằng cách duyệt qua tất cả các cạnh có thể có, thì mất $O(m)$ thời gian để tìm cạnh có trọng số nhỏ nhất.
Tổng độ phức tạp sẽ là $O(n m)$.
Trong trường hợp xấu nhất, đây là $O(n^3)$, thực sự rất chậm.

Thuật toán này có thể được cải tiến nếu chúng ta chỉ xem xét một cạnh nhỏ nhất từ mỗi đỉnh đã chọn.
Ví dụ, chúng ta có thể sắp xếp các cạnh từ mỗi đỉnh theo thứ tự tăng dần của trọng số, và lưu một con trỏ tới cạnh hợp lệ đầu tiên (tức là cạnh đi tới một đỉnh chưa được chọn).
Sau khi tìm và chọn được cạnh nhỏ nhất, chúng ta cập nhật các con trỏ.
Cách này cho độ phức tạp là $O(n^2 + m)$, và cần thêm $O(m \log n)$ để sắp xếp các cạnh, dẫn đến độ phức tạp trong trường hợp xấu nhất là $O(n^2 \log n)$.

Dưới đây chúng ta xem xét hai biến thể thuật toán tối ưu hơn, một cho đồ thị dày và một cho đồ thị thưa.

### Đồ thị dày: $O(n^2)$

Chúng ta tiếp cận bài toán từ một góc nhìn khác:
với mỗi đỉnh chưa được chọn, chúng ta sẽ lưu cạnh nhỏ nhất nối nó tới tập các đỉnh đã chọn.

Khi đó, tại mỗi bước chúng ta chỉ cần tìm kiếm trên các cạnh nhỏ nhất này, thao tác này có độ phức tạp là $O(n)$.

Sau khi thêm một đỉnh mới vào cây khung, một số con trỏ cạnh nhỏ nhất phải được tính toán lại.
Lưu ý rằng trọng số chỉ có thể giảm đi, tức là cạnh nhỏ nhất của mỗi đỉnh chưa chọn sẽ giữ nguyên hoặc được cập nhật bằng cạnh nối tới đỉnh vừa mới được chọn.
Do đó, bước cập nhật này cũng có thể được thực hiện trong $O(n)$.

Như vậy, chúng ta có phiên bản thuật toán Prim với độ phức tạp $O(n^2)$.

Đặc biệt, bản cài đặt này rất thuận tiện cho bài toán Cây khung nhỏ nhất Euclid:
chúng ta có $n$ điểm trên mặt phẳng và khoảng cách giữa mỗi cặp điểm là khoảng cách Euclid giữa chúng, và chúng ta muốn tìm cây khung nhỏ nhất cho đồ thị đầy đủ này.
Bài toán này có thể được giải quyết bằng thuật toán mô tả ở trên trong thời gian $O(n^2)$ và bộ nhớ $O(n)$, điều không thể thực hiện được với [thuật toán Kruskal](mst_kruskal.md).

```cpp
int n;
vector<vector<int>> adj; // adjacency matrix of graph
const int INF = 1000000000; // weight INF means there is no edge

struct Edge {
    int w = INF, to = -1;
};

void prim() {
    int total_weight = 0;
    vector<bool> selected(n, false);
    vector<Edge> min_e(n);
    min_e[0].w = 0;

    for (int i=0; i<n; ++i) {
        int v = -1;
        for (int j = 0; j < n; ++j) {
            if (!selected[j] && (v == -1 || min_e[j].w < min_e[v].w))
                v = j;
        }

        if (min_e[v].w == INF) {
            cout << "No MST!" << endl;
            exit(0);
        }

        selected[v] = true;
        total_weight += min_e[v].w;
        if (min_e[v].to != -1)
            cout << v << " " << min_e[v].to << endl;

        for (int to = 0; to < n; ++to) {
            if (adj[v][to] < min_e[to].w)
                min_e[to] = {adj[v][to], v};
        }
    }

    cout << total_weight << endl;
}
```

Ma trận kề `adj[][]` kích thước $n \times n$ lưu trữ trọng số của các cạnh, và nó sử dụng trọng số `INF` nếu không tồn tại cạnh giữa hai đỉnh.
Thuật toán sử dụng hai mảng: mảng đánh dấu `selected[]` cho biết đỉnh nào đã được chọn, và mảng `min_e[]` lưu trữ cạnh có trọng số nhỏ nhất nối đỉnh chưa chọn với tập các đỉnh đã chọn (lưu trọng số và đỉnh đích).
Thuật toán thực hiện $n$ bước, ở mỗi bước đỉnh có trọng số cạnh nhỏ nhất trong `min_e[]` sẽ được chọn, và giá trị `min_e[]` của các đỉnh khác được cập nhật.

### Đồ thị thưa: $O(m \log n)$

Trong thuật toán mô tả ở trên, chúng ta có thể coi các thao tác tìm kiếm giá trị nhỏ nhất và cập nhật giá trị là các thao tác trên tập hợp.
Hai thao tác cổ điển này được hỗ trợ bởi nhiều cấu trúc dữ liệu, ví dụ như `std::set` trong C++ (được cài đặt bằng cây đỏ-đen).

Thuật toán chính vẫn giữ nguyên, nhưng bây giờ chúng ta có thể tìm cạnh nhỏ nhất trong thời gian $O(\log n)$.
Mặt khác, việc cập nhật các giá trị bây giờ sẽ tốn $O(n \log n)$ thời gian nếu duyệt toàn bộ, điều này tệ hơn thuật toán trước đó.

Nhưng khi nhận thấy rằng chúng ta chỉ cần cập nhật tối đa $O(m)$ lần tổng cộng, và thực hiện $O(n)$ lần tìm kiếm cạnh nhỏ nhất, tổng độ phức tạp sẽ là $O(m \log n)$.
Đối với đồ thị thưa, cách này tốt hơn thuật toán trên, nhưng đối với đồ thị dày thì nó sẽ chậm hơn.

```cpp
const int INF = 1000000000;

struct Edge {
    int w = INF, to = -1;
    bool operator<(Edge const& other) const {
        return make_pair(w, to) < make_pair(other.w, other.to);
    }
};

int n;
vector<vector<Edge>> adj;

void prim() {
    int total_weight = 0;
    vector<Edge> min_e(n);
    min_e[0].w = 0;
    set<Edge> q;
    q.insert({0, 0});
    vector<bool> selected(n, false);
    for (int i = 0; i < n; ++i) {
        if (q.empty()) {
            cout << "No MST!" << endl;
            exit(0);
        }

        int v = q.begin()->to;
        selected[v] = true;
        total_weight += q.begin()->w;
        q.erase(q.begin());

        if (min_e[v].to != -1)
            cout << v << " " << min_e[v].to << endl;

        for (Edge e : adj[v]) {
            if (!selected[e.to] && e.w < min_e[e.to].w) {
                q.erase({min_e[e.to].w, e.to});
                min_e[e.to] = {e.w, v};
                q.insert({e.w, e.to});
            }
        }
    }

    cout << total_weight << endl;
}
```

Ở đây, đồ thị được biểu diễn bằng một danh sách kề `adj[]`, trong đó `adj[v]` chứa tất cả các cạnh (dưới dạng các cặp trọng số và đỉnh đích) đi ra từ đỉnh `v`.
`min_e[v]` sẽ lưu trọng số của cạnh nhỏ nhất từ đỉnh `v` tới một đỉnh đã chọn (cũng dưới dạng cặp trọng số và đỉnh đích).
Ngoài ra, hàng đợi `q` chứa tất cả các đỉnh chưa được chọn theo thứ tự trọng số `min_e` tăng dần.
Thuật toán thực hiện `n` bước, ở mỗi bước nó chọn đỉnh `v` có trọng số `min_e` nhỏ nhất (bằng cách lấy ra từ đầu hàng đợi `q`), sau đó duyệt qua toàn bộ các cạnh từ đỉnh này để cập nhật giá trị trong `min_e` (trong quá trình cập nhật, chúng ta cũng cần xóa cạnh cũ khỏi hàng đợi `q` và chèn vào cạnh mới).
