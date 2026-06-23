---
tags:
  - Translated
e_maxx_link: dijkstra_sparse
lang: vi
---

# Thuật toán Dijkstra trên đồ thị thưa

Bạn có thể tìm hiểu phát biểu bài toán, thuật toán cùng phần cài đặt cơ bản và chứng minh tại bài viết [Thuật toán Dijkstra](dijkstra.md).

## Thuật toán

Hãy nhớ lại rằng khi phân tích độ phức tạp của thuật toán Dijkstra, chúng ta dựa trên hai thao tác chính:
thao tác tìm đỉnh chưa được đánh dấu có khoảng cách $d[v]$ nhỏ nhất, và thao tác tối ưu hóa (relaxation), tức là cập nhật lại giá trị $d[\text{to}]$.

Trong cách cài đặt đơn giản nhất, các thao tác này lần lượt tốn thời gian $O(n)$ và $O(1)$.
Vì chúng ta thực hiện thao tác thứ nhất $O(n)$ lần và thao tác thứ hai $O(m)$ lần, tổng độ phức tạp thu được là $O(n^2 + m)$.

Độ phức tạp này là tối ưu đối với đồ thị dày (đồ thị mật độ cao), tức là khi số lượng cạnh $m \approx n^2$.
Tuy nhiên, trên các đồ thị thưa, khi số lượng cạnh $m$ nhỏ hơn nhiều so với số lượng cạnh tối đa $n^2$, độ phức tạp trên trở nên kém tối ưu do số hạng đầu tiên ($n^2$) quyết định.
Vì vậy, việc cải thiện thời gian thực hiện của thao tác thứ nhất là rất cần thiết (và tất nhiên không được làm ảnh hưởng quá nhiều đến thời gian của thao tác thứ hai).

Để đạt được điều đó, chúng ta có thể sử dụng nhiều cấu trúc dữ liệu bổ trợ khác nhau.
Cấu trúc hiệu quả nhất trên lý thuyết là **Fibonacci heap**, cho phép thực hiện thao tác thứ nhất trong thời gian $O(\log n)$, và thao tác thứ hai trong $O(1)$.
Nhờ đó chúng ta thu được độ phức tạp $O(n \log n + m)$ cho thuật toán Dijkstra, đây cũng là cận dưới lý thuyết cho bài toán tìm đường đi ngắn nhất.
Do đó, thuật toán này hoạt động tối ưu, và Fibonacci heap là cấu trúc dữ liệu tối ưu nhất cho bài toán này.
Không tồn tại cấu trúc dữ liệu nào có thể thực hiện cả hai thao tác trên trong thời gian $O(1)$, vì nếu có, chúng ta có thể sắp xếp một danh sách các số ngẫu nhiên trong thời gian tuyến tính, điều này đã được chứng minh là bất khả thi.
Điều thú vị là có một thuật toán của Thorup tìm đường đi ngắn nhất trong thời gian $O(m)$, tuy nhiên nó chỉ hoạt động với trọng số nguyên và sử dụng một ý tưởng hoàn toàn khác.
Vì vậy điều này không dẫn đến bất kỳ mâu thuẫn nào.
Tóm lại, Fibonacci heap mang lại độ phức tạp tối ưu nhất cho bài toán này.
Tuy nhiên, chúng rất phức tạp để cài đặt và có hằng số ẩn tương đối lớn trong thực tế.

Một giải pháp dung hòa là sử dụng các cấu trúc dữ liệu cho phép thực hiện cả hai loại thao tác (lấy ra phần tử nhỏ nhất và cập nhật phần tử) trong thời gian $O(\log n)$.
Khi đó, độ phức tạp của thuật toán Dijkstra sẽ là $O(n \log n + m \log n) = O(m \log n)$.

C++ cung cấp hai cấu trúc dữ liệu như vậy: `set` và `priority_queue`.
Cấu trúc thứ nhất dựa trên cây đỏ-đen, và cấu trúc thứ hai dựa trên heap nhị phân.
Do đó, `priority_queue` có hằng số ẩn nhỏ hơn, nhưng lại có một nhược điểm:
nó không hỗ trợ thao tác xóa một phần tử bất kỳ.
Vì điều này, chúng ta cần sử dụng một mẹo nhỏ, dẫn đến hệ số $\log m$ thay vì $\log n$ (mặc dù về mặt độ phức tạp tiệm cận thì chúng là như nhau).

## Cài đặt

### set

Hãy bắt đầu với container `set`.
Vì chúng ta cần lưu trữ các đỉnh được sắp xếp theo giá trị khoảng cách $d[]$ của chúng, cách thuận tiện là lưu trữ các cặp (`pair`): khoảng cách và chỉ số của đỉnh.
Nhờ đó, các cặp trong `set` sẽ tự động được sắp xếp tăng dần theo khoảng cách.

```{.cpp file=dijkstra_sparse_set}
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);

    d[s] = 0;
    set<pair<int, int>> q;
    q.insert({0, s});
    while (!q.empty()) {
        int v = q.begin()->second;
        q.erase(q.begin());

        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;
            
            if (d[v] + len < d[to]) {
                q.erase({d[to], to});
                d[to] = d[v] + len;
                p[to] = v;
                q.insert({d[to], to});
            }
        }
    }
}
```

Chúng ta không cần sử dụng mảng đánh dấu các đỉnh đã duyệt $u[]$ như trong thuật toán Dijkstra thông thường nữa.
Chúng ta sử dụng `set` để lưu trữ thông tin đó, đồng thời tìm đỉnh có khoảng cách nhỏ nhất thông qua nó.
Nó hoạt động tương tự như một hàng đợi.
Vòng lặp chính thực hiện cho đến khi không còn đỉnh nào trong tập hợp/hàng đợi.
Đỉnh có khoảng cách nhỏ nhất được lấy ra, và với mỗi lần tối ưu hóa thành công, trước tiên chúng ta xóa cặp cũ khỏi hàng đợi, và sau khi cập nhật khoảng cách thì chèn cặp mới vào hàng đợi.

### priority_queue

Điểm khác biệt chính so với cách cài đặt bằng `set` là trong nhiều ngôn ngữ lập trình, bao gồm cả C++, chúng ta không thể xóa các phần tử nằm ở giữa hàng đợi ưu tiên `priority_queue` (mặc dù về mặt lý thuyết cấu trúc dữ liệu heap có thể hỗ trợ thao tác này).
Do đó, chúng ta phải sử dụng một mẹo nhỏ:
Chúng ta đơn giản là không xóa cặp cũ khỏi hàng đợi.
Kết quả là một đỉnh có thể xuất hiện nhiều lần trong hàng đợi với các giá trị khoảng cách khác nhau tại cùng một thời điểm.
Trong số các cặp này, chúng ta chỉ quan tâm đến cặp có giá trị khoảng cách thực tế (phần tử thứ nhất của cặp) bằng với giá trị khoảng cách lưu trong mảng $d[]$, tất cả các cặp khác của đỉnh đó đều đã cũ và lỗi thời.
Vì vậy, chúng ta cần bổ sung một thay đổi nhỏ:
ở đầu mỗi bước lặp, sau khi lấy ra cặp tiếp theo từ hàng đợi, chúng ta kiểm tra xem nó có phải là cặp hợp lệ hay không, hay nó là một cặp cũ đã được xử lý từ trước.
Kiểm tra này là vô cùng quan trọng, nếu không độ phức tạp thuật toán có thể tăng lên thành $O(n m)$.

Mặc định, `priority_queue` sắp xếp các phần tử theo thứ tự giảm dần.
Để nó sắp xếp theo thứ tự tăng dần, chúng ta có thể lưu trữ giá trị âm của khoảng cách, hoặc truyền vào nó một hàm so sánh khác.
Ở đây chúng ta chọn cách thứ hai.

```{.cpp file=dijkstra_sparse_pq}
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);

    d[s] = 0;
    using pii = pair<int, int>;
    priority_queue<pii, vector<pii>, greater<pii>> q;
    q.push({0, s});
    while (!q.empty()) {
        int v = q.top().second;
        int d_v = q.top().first;
        q.pop();
        if (d_v != d[v])
            continue;

        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;
            
            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
                q.push({d[to], to});
            }
        }
    }
}
```

Trong thực tế, phiên bản sử dụng `priority_queue` chạy nhanh hơn một chút so với phiên bản sử dụng `set`.

Điều thú vị là, một [báo cáo kỹ thuật năm 2007](https://www3.cs.stonybrook.edu/~rezaul/papers/TR-07-54.pdf) đã kết luận rằng phiên bản thuật toán không sử dụng thao tác cập nhật trực tiếp khóa (decrease-key) chạy nhanh hơn so với phiên bản có sử dụng decrease-key, và sự chênh lệch hiệu năng này càng rõ rệt đối với các đồ thị thưa.

### Loại bỏ việc lưu trữ cặp (pair)

Bạn có thể cải thiện hiệu năng thêm một chút nữa nếu không lưu trữ các cặp trong container, mà chỉ lưu trữ chỉ số của các đỉnh.
Trong trường hợp này, chúng ta phải viết đè toán tử so sánh:
nó phải so sánh hai đỉnh dựa trên khoảng cách lưu trữ trong mảng $d[]$.

Khi thực hiện tối ưu hóa, khoảng cách của một số đỉnh sẽ thay đổi.
Tuy nhiên, cấu trúc dữ liệu không tự động sắp xếp lại.
Thực tế, việc thay đổi khoảng cách của các đỉnh đang nằm trong hàng đợi có thể làm hỏng tính đúng đắn của cấu trúc dữ liệu.
Do đó, tương tự như trước, chúng ta cần xóa đỉnh ra khỏi hàng đợi trước khi tối ưu hóa nó, và chèn lại vào hàng đợi sau đó.

Vì chúng ta chỉ có thể xóa phần tử tùy ý khỏi cấu trúc `set`, tối ưu hóa này chỉ áp dụng được cho phương pháp dùng `set` và không thể áp dụng cho cách cài đặt dùng `priority_queue`.
Trong thực tế, tối ưu hóa này giúp tăng hiệu năng đáng kể, đặc biệt khi sử dụng các kiểu dữ liệu lớn hơn để lưu trữ khoảng cách như `long long` hoặc `double`.
