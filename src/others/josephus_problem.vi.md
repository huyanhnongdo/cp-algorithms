---
tags:
  - Translated
e_maxx_link: joseph_problem
lang: vi
---
# Bài toán Josephus

## Đề bài

Cho các số tự nhiên $n$ và $k$.
Tất cả các số tự nhiên từ $1$ đến $n$ được xếp thành một vòng tròn.
Đầu tiên, đếm đến số thứ $k$ bắt đầu từ số đầu tiên và loại bỏ nó.
Sau đó, tiếp tục đếm $k$ số bắt đầu từ số tiếp theo và loại bỏ số thứ $k$, và cứ tiếp tục như vậy.
Quá trình dừng lại khi chỉ còn một số duy nhất.
Yêu cầu tìm số cuối cùng còn lại.

Bài toán này được đặt ra bởi **Flavius Josephus** vào thế kỷ thứ nhất (tuy nhiên với một công thức hẹp hơn: cho $k = 2$).

Bài toán này có thể được giải bằng cách mô phỏng quy trình.
Mô phỏng vét cạn (Brute Force) sẽ có độ phức tạp $O(n^{2})$. Sử dụng Cây phân đoạn (Segment Tree) [](../data_structures/segment_tree.md), chúng ta có thể cải thiện nó lên $O(n \log n)$.
Tuy nhiên, chúng ta muốn một giải pháp tốt hơn.

## Mô phỏng giải pháp $O(n)$

Chúng ta sẽ cố gắng tìm ra một quy luật thể hiện đáp án cho bài toán $J_{n, k}$ thông qua các bài toán trước đó.

Sử dụng mô phỏng vét cạn, chúng ta có thể lập một bảng các giá trị, ví dụ như sau:

$$\begin{array}{ccccccccccc}
n\setminus k & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
2 & 2 & 1 & 2 & 1 & 2 & 1 & 2 & 1 & 2 & 1 \\
3 & 3 & 3 & 2 & 2 & 1 & 1 & 3 & 3 & 2 & 2 \\
4 & 4 & 1 & 1 & 2 & 2 & 3 & 2 & 3 & 3 & 4 \\
5 & 5 & 3 & 4 & 1 & 2 & 4 & 4 & 1 & 2 & 4 \\
6 & 6 & 5 & 1 & 5 & 1 & 4 & 5 & 3 & 5 & 2 \\
7 & 7 & 7 & 4 & 2 & 6 & 3 & 5 & 4 & 7 & 5 \\
8 & 8 & 1 & 7 & 6 & 3 & 1 & 4 & 4 & 8 & 7 \\
9 & 9 & 3 & 1 & 1 & 8 & 7 & 2 & 3 & 8 & 8 \\
10 & 10 & 5 & 4 & 5 & 3 & 3 & 9 & 1 & 7 & 8 \\
\end{array}$$

Và ở đây, chúng ta có thể thấy rõ **quy luật** sau:

$$J_{n,k} = \left( (J_{n-1,k} + k - 1) \bmod n \right) + 1$$

$$J_{1,k} = 1$$

Ở đây, việc đánh số từ 1 làm cho công thức trở nên hơi phức tạp; nếu bạn đánh số các vị trí bắt đầu từ 0, bạn sẽ nhận được một công thức rất thanh lịch:

$$J_{n,k} = (J_{n-1,k} + k) \bmod n$$

Như vậy, chúng ta đã tìm ra giải pháp cho bài toán Josephus với độ phức tạp $O(n)$ phép toán.

## Cài đặt

**Cài đặt đệ quy** đơn giản (đánh số từ 1)

```{.cpp file=josephus_rec}
int josephus(int n, int k) {
    return n > 1 ? (josephus(n-1, k) + k - 1) % n + 1 : 1;
}
```

**Dạng không đệ quy**:

```{.cpp file=josephus_iter}
int josephus(int n, int k) {
    int res = 0;
    for (int i = 1; i <= n; ++i)
  	  res = (res + k) % i;
    return res + 1;
}
```

Công thức này cũng có thể được tìm thấy bằng phân tích giải tích.
Ở đây ta giả sử đánh số từ 0.
Sau khi loại bỏ số đầu tiên, chúng ta còn lại $n-1$ số.
Khi lặp lại quy trình, chúng ta sẽ bắt đầu với số mà ban đầu có chỉ số là $k \bmod n$.
$J_{n-1, k}$ sẽ là câu trả lời cho vòng tròn còn lại nếu chúng ta bắt đầu đếm tại $0$, nhưng vì thực tế chúng ta bắt đầu tại $k$, ta có $J_{n, k} = (J_{n-1,k} + k) \ \bmod n$.

## Mô phỏng giải pháp $O(k \log n)$

Với $k$ tương đối nhỏ, chúng ta có thể đưa ra giải pháp tốt hơn giải pháp đệ quy ở trên với độ phức tạp $O(n)$.
Nếu $k$ nhỏ hơn nhiều so với $n$, chúng ta có thể xóa nhiều số ($\lfloor \frac{n}{k} \rfloor$) trong một lượt mà không cần lặp qua từng bước.
Sau đó, chúng ta còn lại $n - \lfloor \frac{n}{k} \rfloor$ số và bắt đầu từ số thứ $(\lfloor \frac{n}{k} \rfloor \cdot k)$.
Vì vậy, chúng ta phải dịch chuyển vị trí tương ứng.
Chúng ta có thể nhận thấy $\lfloor \frac{n}{k} \rfloor \cdot k$ đơn giản là $-n \bmod k$.
Và vì chúng ta đã loại bỏ mỗi số thứ $k$, chúng ta phải thêm số lượng các số đã bị loại bỏ trước chỉ số kết quả.
Giá trị này có thể được tính bằng cách chia chỉ số kết quả cho $k - 1$.

Ngoài ra, chúng ta cần xử lý trường hợp $n$ trở nên nhỏ hơn $k$. Trong trường hợp này, việc tối ưu hóa trên sẽ gây ra vòng lặp vô tận.

**Cài đặt** (để thuận tiện, sử dụng đánh số từ 0):

```{.cpp file=josephus_fast0}
int josephus(int n, int k) {
    if (n == 1)
        return 0;
    if (k == 1)
        return n-1;
    if (k > n)
        return (josephus(n-1, k) + k) % n;
    int cnt = n / k;
    int res = josephus(n - cnt, k);
    res -= n % k;
    if (res < 0)
        res += n;
    else
        res += res / (k - 1);
    return res;
}
```

Hãy ước tính **độ phức tạp** của thuật toán này. Lưu ý ngay rằng trường hợp $n < k$ được giải quyết bằng giải pháp cũ với độ phức tạp $O(k)$. Bây giờ, hãy xem xét thuật toán chính. Thực tế, sau mỗi lần lặp, thay vì còn $n$ số, chúng ta còn lại $n \left( 1 - \frac{1}{k} \right)$ số, do đó tổng số lần lặp $x$ của thuật toán có thể được tìm thấy xấp xỉ từ phương trình sau:

$$ n \left(1 - \frac{1}{k} \right) ^ x = 1, $$

Lấy logarit hai vế, ta thu được:

$$\ln n + x \ln \left(1 - \frac{1}{k} \right) = 0,$$ 
$$x = - \frac{\ln n}{\ln \left(1 - \frac{1}{k} \right)},$$

Sử dụng khai triển chuỗi Taylor cho logarit, ta thu được ước tính xấp xỉ:

$$x \approx k \ln n$$

Như vậy, độ phức tạp của thuật toán thực tế là $O (k \log n)$.

## Giải pháp giải tích cho $k = 2$

Trong trường hợp cụ thể này (bài toán ban đầu do Josephus Flavius đặt ra), bài toán được giải quyết dễ dàng hơn nhiều.

Với $n$ là số chẵn, tất cả các số chẵn sẽ bị loại bỏ, sau đó bài toán quy về $\frac{n}{2}$. Đáp án cho $n$ sẽ thu được từ đáp án của $\frac{n}{2}$ bằng cách nhân hai và trừ đi một (do dịch chuyển vị trí):

$$ J_{2n, 2} = 2 J_{n, 2} - 1 $$

Tương tự, trong trường hợp $n$ là số lẻ, tất cả các số chẵn sẽ bị loại bỏ, sau đó là số đầu tiên, và bài toán còn lại cho $\frac{n-1}{2}$. Tính đến sự dịch chuyển vị trí, ta có công thức thứ hai:

$$J_{2n+1,2} = 2 J_{n, 2} + 1 $$

Chúng ta có thể sử dụng trực tiếp sự phụ thuộc đệ quy này trong cài đặt. Quy luật này có thể được dịch sang một dạng khác: $J_{n, 2}$ đại diện cho một dãy gồm tất cả các số lẻ, "khởi động lại" từ một bất cứ khi nào $n$ trở thành một lũy thừa của hai. Điều này có thể được viết thành một công thức duy nhất:

$$J_{n, 2} = 1 + 2 \left(n-2^{\lfloor \log_2 n \rfloor} \right)$$

## Giải pháp giải tích cho $k > 2$

Mặc dù bài toán có dạng đơn giản và có rất nhiều bài viết về nó cũng như các vấn đề liên quan, nhưng một công thức giải tích đơn giản cho bài toán Josephus tổng quát vẫn chưa được tìm ra. Đối với $k$ nhỏ, một số công thức đã được rút ra, nhưng dường như tất cả đều khó áp dụng trong thực tế (ví dụ: xem Halbeisen, Hungerbuhler "The Josephus Problem" và Odlyzko, Wilf "Functional iteration and the Josephus problem").