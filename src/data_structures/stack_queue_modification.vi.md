---
tags:
  - Translated
e_maxx_link: stacks_for_minima
lang: vi
---
# Ngăn xếp cực tiểu / Hàng đợi cực tiểu

Trong bài viết này, chúng ta sẽ xem xét ba vấn đề: đầu tiên chúng ta sẽ sửa đổi một ngăn xếp (Stack) theo cách cho phép tìm phần tử (Element) nhỏ nhất của ngăn xếp trong $O(1)$, sau đó chúng ta sẽ làm tương tự với một hàng đợi (Queue), và cuối cùng chúng ta sẽ sử dụng các cấu trúc dữ liệu (Data Structure) này để tìm giá trị cực tiểu trong tất cả các mảng con (Subarray) có độ dài cố định trong một mảng (Array) với độ phức tạp $O(n)$.

## Sửa đổi ngăn xếp

Chúng ta muốn sửa đổi cấu trúc dữ liệu ngăn xếp (Stack) theo cách mà có thể tìm thấy phần tử nhỏ nhất trong ngăn xếp trong thời gian $O(1)$, đồng thời duy trì hành vi tiệm cận (Asymptotic Behavior) tương tự cho việc thêm và xóa phần tử khỏi ngăn xếp.
Nhắc lại nhanh, trên một ngăn xếp chúng ta chỉ thêm và xóa các phần tử ở một đầu.

Để làm điều này, chúng ta sẽ không chỉ lưu trữ các phần tử trong ngăn xếp, mà chúng ta sẽ lưu trữ chúng dưới dạng các cặp: bản thân phần tử và giá trị cực tiểu trong ngăn xếp bắt đầu từ phần tử này trở xuống.

```cpp
stack<pair<int, int>> st;
```

Rõ ràng là việc tìm giá trị cực tiểu trong toàn bộ ngăn xếp chỉ bao gồm việc nhìn vào giá trị `stack.top().second`.

Cũng hiển nhiên là việc thêm hoặc xóa một phần tử mới vào ngăn xếp có thể được thực hiện trong thời gian hằng số.

Cài đặt (Implementation):

* Thêm một phần tử:
```cpp
int new_min = st.empty() ? new_elem : min(new_elem, st.top().second);
st.push({new_elem, new_min});
```

* Xóa một phần tử:
```cpp
int removed_element = st.top().first;
st.pop();
```

* Tìm giá trị cực tiểu:
```cpp
int minimum = st.top().second;
```

## Sửa đổi hàng đợi (phương pháp 1)

Bây giờ chúng ta muốn thực hiện các thao tác tương tự với một hàng đợi (Queue), tức là chúng ta muốn thêm phần tử vào cuối và xóa chúng khỏi đầu.

Ở đây chúng ta xem xét một phương pháp đơn giản để sửa đổi hàng đợi.
Tuy nhiên, nó có một nhược điểm lớn, bởi vì hàng đợi đã sửa đổi sẽ không thực sự lưu trữ tất cả các phần tử.

Ý tưởng chính là chỉ lưu trữ các mục trong hàng đợi cần thiết để xác định giá trị cực tiểu.
Cụ thể, chúng ta sẽ giữ hàng đợi theo thứ tự không giảm (tức là giá trị nhỏ nhất sẽ được lưu trữ ở đầu), và tất nhiên không theo bất kỳ cách tùy ý nào, giá trị cực tiểu thực sự phải luôn được chứa trong hàng đợi.
Bằng cách này, phần tử nhỏ nhất sẽ luôn ở đầu hàng đợi.
Trước khi thêm một phần tử mới vào hàng đợi, chỉ cần thực hiện một "cắt":
chúng ta sẽ loại bỏ tất cả các phần tử ở cuối hàng đợi lớn hơn phần tử mới, và sau đó thêm phần tử mới vào hàng đợi.
Bằng cách này, chúng ta không phá vỡ thứ tự của hàng đợi, và chúng ta cũng sẽ không mất phần tử hiện tại nếu nó là giá trị cực tiểu ở bất kỳ bước tiếp theo nào.
Tất cả các phần tử mà chúng ta đã xóa không bao giờ có thể tự nó là giá trị cực tiểu, vì vậy thao tác này được phép.
Khi chúng ta muốn trích xuất một phần tử từ đầu, nó thực sự có thể không còn ở đó (vì chúng ta đã xóa nó trước đó khi thêm một phần tử nhỏ hơn).
Do đó, khi xóa một phần tử khỏi hàng đợi, chúng ta cần biết giá trị của phần tử đó.
Nếu đầu hàng đợi có cùng giá trị, chúng ta có thể an toàn xóa nó, nếu không thì chúng ta không làm gì cả.

Xem xét việc triển khai (Implementation) các thao tác trên:

```cpp
deque<int> q;
```

* Tìm giá trị cực tiểu:
```cpp
int minimum = q.front();
```

* Thêm một phần tử:
```cpp
while (!q.empty() && q.back() > new_element)
    q.pop_back();
q.push_back(new_element);
```

* Xóa một phần tử:
```cpp
if (!q.empty() && q.front() == remove_element)
    q.pop_front();
```

Rõ ràng là trung bình tất cả các thao tác này chỉ mất thời gian $O(1)$ (vì mỗi phần tử chỉ có thể được đẩy vào và lấy ra một lần).

## Sửa đổi hàng đợi (phương pháp 2)

Đây là một sửa đổi của phương pháp 1.
Chúng ta muốn có thể xóa các phần tử mà không cần biết phần tử nào chúng ta phải xóa.
Chúng ta có thể thực hiện điều đó bằng cách lưu trữ chỉ số (Index) cho mỗi phần tử trong hàng đợi.
Và chúng ta cũng nhớ số lượng phần tử đã thêm và đã xóa.

```cpp
deque<pair<int, int>> q;
int cnt_added = 0;
int cnt_removed = 0;
```

* Tìm giá trị cực tiểu:
```cpp
int minimum = q.front().first;
```

* Thêm một phần tử:
```cpp
while (!q.empty() && q.back().first > new_element)
    q.pop_back();
q.push_back({new_element, cnt_added});
cnt_added++;
```

* Xóa một phần tử:
```cpp
if (!q.empty() && q.front().second == cnt_removed) 
    q.pop_front();
cnt_removed++;
```

## Sửa đổi hàng đợi (phương pháp 3)

Ở đây chúng ta xem xét một cách khác để sửa đổi hàng đợi để tìm giá trị cực tiểu trong thời gian $O(1)$.
Cách này phức tạp hơn một chút để triển khai (Implementation), nhưng lần này chúng ta thực sự lưu trữ tất cả các phần tử.
Và chúng ta cũng có thể xóa một phần tử từ đầu mà không cần biết giá trị của nó.

Ý tưởng là giảm bài toán này về bài toán ngăn xếp, mà chúng ta đã giải quyết.
Vì vậy, chúng ta chỉ cần học cách mô phỏng một hàng đợi bằng cách sử dụng hai ngăn xếp.

Chúng ta tạo hai ngăn xếp, `s1` và `s2`.
Tất nhiên các ngăn xếp này sẽ ở dạng đã sửa đổi, để chúng ta có thể tìm giá trị cực tiểu trong $O(1)$.
Chúng ta sẽ thêm các phần tử mới vào ngăn xếp `s1`, và xóa các phần tử khỏi ngăn xếp `s2`.
Nếu bất kỳ lúc nào ngăn xếp `s2` trống, chúng ta di chuyển tất cả các phần tử từ `s1` sang `s2` (điều này về cơ bản đảo ngược thứ tự của các phần tử đó).
Cuối cùng, việc tìm giá trị cực tiểu trong hàng đợi chỉ đơn giản là tìm giá trị cực tiểu của cả hai ngăn xếp.

Do đó, chúng ta thực hiện tất cả các thao tác trong $O(1)$ trung bình (mỗi phần tử sẽ được thêm vào ngăn xếp `s1` một lần, được chuyển sang `s2` một lần, và được lấy ra khỏi `s2` một lần)

Cài đặt:

```cpp
stack<pair<int, int>> s1, s2;
```

* Tìm giá trị cực tiểu:
```cpp
if (s1.empty() || s2.empty()) 
    minimum = s1.empty() ? s2.top().second : s1.top().second;
else
    minimum = min(s1.top().second, s2.top().second);
```

* Thêm phần tử:
```cpp
int minimum = s1.empty() ? new_element : min(new_element, s1.top().second);
s1.push({new_element, minimum});
```

* Xóa một phần tử:
```cpp
if (s2.empty()) {
    while (!s1.empty()) {
        int element = s1.top().first;
        s1.pop();
        int minimum = s2.empty() ? element : min(element, s2.top().second);
        s2.push({element, minimum});
    }
}
int remove_element = s2.top().first;
s2.pop();
```

## Tìm giá trị cực tiểu cho tất cả các mảng con có độ dài cố định

Giả sử chúng ta được cho một mảng (Array) $A$ có độ dài $N$ và một $M \le N$ cho trước.
Chúng ta phải tìm giá trị cực tiểu của mỗi mảng con (Subarray) có độ dài $M$ trong mảng này, tức là chúng ta phải tìm:

$$\min_{0 \le i \le M-1} A[i], \min_{1 \le i \le M} A[i], \min_{2 \le i \le M+1} A[i],~\dots~, \min_{N-M \le i \le N-1} A[i]$$

Chúng ta phải giải quyết bài toán này trong thời gian tuyến tính (Linear Time), tức là $O(n)$.

Chúng ta có thể sử dụng bất kỳ hàng đợi đã sửa đổi nào trong ba phương pháp trên để giải quyết bài toán.
Các giải pháp phải rõ ràng:
chúng ta thêm $M$ phần tử đầu tiên của mảng, tìm và xuất giá trị cực tiểu của nó, sau đó thêm phần tử tiếp theo vào hàng đợi và xóa phần tử đầu tiên của mảng, tìm và xuất giá trị cực tiểu của nó, v.v.
Vì tất cả các thao tác với hàng đợi được thực hiện trong thời gian hằng số (Constant Time) trung bình, độ phức tạp thời gian (Time Complexity) của toàn bộ thuật toán (Algorithm) sẽ là $O(n)$.

## Các bài tập thực hành
* [Truy vấn với độ dài cố định](https://www.hackerrank.com/challenges/queries-with-fixed-length/problem)
* [Giá trị cực tiểu trên cửa sổ trượt](https://cses.fi/problemset/task/3221)
* [Binary Land](https://www.codechef.com/MAY20A/problems/BINLAND)