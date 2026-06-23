---
tags:
  - Translated
e_maxx_link: maximum_zero_submatrix
lang: vi
---
# Tìm ma trận con toàn số 0 lớn nhất

Bạn được cho một ma trận với `n` hàng và `m` cột. Hãy tìm ma trận con lớn nhất chỉ bao gồm các số 0 (ma trận con là một vùng chữ nhật của ma trận).

## Thuật toán

Các phần tử của ma trận sẽ là `a[i][j]`, với `i = 0...n - 1`, `j = 0... m - 1`. Để đơn giản, chúng ta sẽ coi tất cả các phần tử khác 0 đều bằng 1.

### Bước 1: Quy hoạch động phụ trợ

Đầu tiên, chúng ta tính toán ma trận phụ trợ sau: `d[i][j]` là hàng gần nhất có chứa số 1 nằm phía trên `a[i][j]`. Nói một cách hình thức, `d[i][j]` là số thứ tự hàng lớn nhất (từ `0` đến `i - 1`) mà tại đó cột `j` có một phần tử bằng `1`.
Trong khi duyệt từ trên xuống dưới, trái sang phải, khi đang đứng ở hàng `i`, chúng ta đã biết các giá trị từ hàng trước đó, vì vậy chỉ cần cập nhật các phần tử có giá trị `1`. Chúng ta có thể lưu các giá trị trong một mảng đơn giản `d[i]` với `i = 1...m - 1`, vì trong phần tiếp theo của thuật toán, chúng ta sẽ xử lý ma trận theo từng hàng và chỉ cần các giá trị của hàng hiện tại.

```cpp
vector<int> d(m, -1);
for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
        if (a[i][j] == 1) {
            d[j] = i;
        }
    }
}
```

### Bước 2: Giải bài toán

Chúng ta có thể giải bài toán trong $O(n m^2)$ bằng cách duyệt qua các hàng, xem xét mọi khả năng cho cột trái và cột phải của một ma trận con. Đáy của hình chữ nhật sẽ là hàng hiện tại, và sử dụng `d[i][j]` chúng ta có thể tìm được hàng trên cùng. Tuy nhiên, chúng ta có thể tiến xa hơn và cải thiện đáng kể độ phức tạp của lời giải.

Rõ ràng là ma trận con toàn số 0 mong muốn được giới hạn ở cả bốn phía bởi các số 1, thứ ngăn cản nó tăng kích thước và cải thiện kết quả. Do đó, chúng ta sẽ không bỏ lỡ kết quả nếu thực hiện như sau: với mỗi ô `j` trong hàng `i` (hàng dưới cùng của ma trận con toàn số 0 tiềm năng), chúng ta sẽ có `d[i][j]` là hàng trên cùng của ma trận con toàn số 0 hiện tại. Bây giờ chỉ còn việc xác định các biên trái và phải tối ưu của ma trận con toàn số 0, tức là đẩy ma trận con này xa nhất có thể sang trái và phải của cột `j`.

Đẩy tối đa sang trái nghĩa là gì? Nghĩa là tìm một chỉ số `k1` sao cho `d[i][k1] > d[i][j]`, và đồng thời `k1` là chỉ số gần nhất bên trái chỉ số `j`. Rõ ràng là `k1 + 1` sẽ cho ta số thứ tự cột bên trái của ma trận con toàn số 0 cần tìm. Nếu không tồn tại chỉ số như vậy, ta đặt `k1 = -1` (điều này có nghĩa là chúng ta có thể mở rộng ma trận con toàn số 0 hiện tại sang trái đến tận biên của ma trận `a`).

Tương tự, bạn có thể xác định chỉ số `k2` cho biên phải: đây là chỉ số gần nhất bên phải của `j` sao cho `d[i][k2] > d[i][j]` (hoặc `m`, nếu không tồn tại chỉ số đó).

Vậy, các chỉ số `k1` và `k2`, nếu chúng ta biết cách tìm kiếm chúng hiệu quả, sẽ cung cấp cho chúng ta mọi thông tin cần thiết về ma trận con toàn số 0 hiện tại. Đặc biệt, diện tích của nó sẽ bằng `(i - d[i][j]) * (k2 - k1 - 1)`.

Làm thế nào để tìm các chỉ số `k1` và `k2` này hiệu quả với `i` và `j` cố định? Chúng ta có thể thực hiện điều đó trong $O(1)$ trung bình.

Để đạt được độ phức tạp này, bạn có thể sử dụng ngăn xếp (Stack) như sau. Trước hết, hãy tìm hiểu cách tìm chỉ số `k1` và lưu giá trị của nó cho mỗi chỉ số `j` trong hàng `i` hiện tại vào ma trận `d1[i][j]`. Để làm điều này, chúng ta sẽ duyệt qua tất cả các cột `j` từ trái sang phải, và chỉ lưu vào ngăn xếp những cột có giá trị `d` nghiêm ngặt lớn hơn `d[i][j]`. Rõ ràng là khi di chuyển từ cột `j` sang cột tiếp theo, cần phải cập nhật nội dung của ngăn xếp. Khi có một phần tử không phù hợp ở đỉnh ngăn xếp (tức là `d[][] <= d[i][j]`), hãy loại bỏ (pop) nó. Dễ dàng hiểu rằng chỉ cần loại bỏ từ đỉnh ngăn xếp là đủ, không cần từ bất kỳ vị trí nào khác (bởi vì ngăn xếp sẽ luôn chứa một dãy các cột có giá trị `d` tăng dần).

Giá trị `d1[i][j]` cho mỗi `j` sẽ bằng giá trị đang nằm ở đỉnh ngăn xếp tại thời điểm đó.

Quy hoạch động `d2[i][j]` để tìm các chỉ số `k2` cũng được xem xét tương tự, chỉ khác là bạn cần duyệt các cột từ phải sang trái.

Rõ ràng là vì mỗi hàng có đúng `m` phần tử được thêm vào ngăn xếp, nên cũng sẽ không có quá nhiều thao tác xóa, tổng độ phức tạp sẽ là tuyến tính, vì vậy độ phức tạp cuối cùng của thuật toán là $O(nm)$.

Cũng cần lưu ý rằng thuật toán này tiêu tốn $O(m)$ bộ nhớ (không tính dữ liệu đầu vào - ma trận `a[][]`).

### Cài đặt

```cpp
int zero_matrix(vector<vector<int>> a) {
    int n = a.size();
    int m = a[0].size();

    int ans = 0;
    vector<int> d(m, -1), d1(m), d2(m);
    stack<int> st;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == 1)
                d[j] = i;
        }

        for (int j = 0; j < m; ++j) {
            while (!st.empty() && d[st.top()] <= d[j])
                st.pop();
            d1[j] = st.empty() ? -1 : st.top();
            st.push(j);
        }
        while (!st.empty())
            st.pop();

        for (int j = m - 1; j >= 0; --j) {
            while (!st.empty() && d[st.top()] <= d[j])
                st.pop();
            d2[j] = st.empty() ? m : st.top();
            st.push(j);
        }
        while (!st.empty())
            st.pop();

        for (int j = 0; j < m; ++j)
            ans = max(ans, (i - d[j]) * (d2[j] - d1[j] - 1));
    }
    return ans;
}
```