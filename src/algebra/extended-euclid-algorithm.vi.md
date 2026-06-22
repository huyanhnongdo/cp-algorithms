---
tags:
  - Translated
e_maxx_link: extended_euclid_algorithm
lang: vi
---

# Thuật toán Euclid mở rộng

Trong khi [Thuật toán Euclid](euclid-algorithm.md) chỉ tính toán ước chung lớn nhất (GCD) của hai số nguyên không âm $a$ và $b$, phiên bản mở rộng của thuật toán này còn tìm cách biểu diễn GCD thông qua $a$ và $b$, tức là tìm các hệ số $x$ và $y$ thỏa mãn:

$$a \cdot x + b \cdot y = \gcd(a, b)$$

Cần lưu ý rằng theo [Đồng nhất thức Bézout](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity), chúng ta luôn có thể tìm thấy một biểu diễn như vậy. Ví dụ, $\gcd(55, 80) = 5$, vì vậy chúng ta có thể biểu diễn $5$ dưới dạng một tổ hợp tuyến tính của $55$ và $80$: $55 \cdot 3 + 80 \cdot (-2) = 5$.

Dạng tổng quát hơn của bài toán này được thảo luận trong bài viết về [Phương trình Diophantine tuyến tính](linear-diophantine-equation.md). Bài viết đó sẽ được xây dựng dựa trên thuật toán này.

## Thuật toán

Chúng ta sẽ ký hiệu ước chung lớn nhất (GCD) của $a$ và $b$ là $g$ trong phần này.

Những thay đổi đối với thuật toán gốc là rất đơn giản.
Nếu nhớ lại thuật toán gốc, ta thấy nó kết thúc khi $b = 0$ và $a = g$.
Với các tham số này, ta có thể dễ dàng tìm thấy các hệ số thỏa mãn, cụ thể là $g \cdot 1 + 0 \cdot 0 = g$.

Bắt đầu từ các hệ số này $(x, y) = (1, 0)$, chúng ta có thể đi ngược lại các lời gọi đệ quy.
Tất cả những gì chúng ta cần làm là xác định xem các hệ số $x$ và $y$ thay đổi như thế nào trong quá trình chuyển đổi từ $(a, b)$ sang $(b, a \bmod b)$.

Giả sử chúng ta đã tìm thấy các hệ số $(x_1, y_1)$ cho $(b, a \bmod b)$:

$$b \cdot x_1 + (a \bmod b) \cdot y_1 = g$$

và chúng ta muốn tìm cặp hệ số $(x, y)$ cho $(a, b)$:

$$ a \cdot x + b \cdot y = g$$

Chúng ta có thể biểu diễn $a \bmod b$ dưới dạng:

$$ a \bmod b = a - \left\lfloor \frac{a}{b} \right\rfloor \cdot b$$

Thay biểu thức này vào phương trình hệ số của $(x_1, y_1)$, ta được:

$$ g = b \cdot x_1 + (a \bmod b) \cdot y_1 = b \cdot x_1 + \left(a - \left\lfloor \frac{a}{b} \right\rfloor \cdot b \right) \cdot y_1$$

và sau khi sắp xếp lại các hạng tử:

$$g = a \cdot y_1 + b \cdot \left( x_1 - y_1 \cdot \left\lfloor \frac{a}{b} \right\rfloor \right)$$

Từ đó, ta tìm được các giá trị của $x$ và $y$:

$$\begin{cases}
x = y_1 \\
y = x_1 - y_1 \cdot \left\lfloor \frac{a}{b} \right\rfloor
\end{cases} $$

## Cài đặt

```{.cpp file=extended_gcd}
int gcd(int a, int b, int& x, int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d = gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}
```

Hàm đệ quy trên trả về GCD và gán giá trị của các hệ số vào `x` và `y` (được truyền bằng tham chiếu vào hàm).

Cài đặt này của thuật toán Euclid mở rộng cũng hoạt động chính xác với cả các số nguyên âm.

## Phiên bản vòng lặp

Chúng ta cũng có thể viết thuật toán Euclid mở rộng dưới dạng vòng lặp (iterative).
Do tránh được đệ quy, phiên bản này sẽ chạy nhanh hơn một chút so với phiên bản đệ quy.

```{.cpp file=extended_gcd_iter}
int gcd(int a, int b, int& x, int& y) {
    x = 1, y = 0;
    int x1 = 0, y1 = 1, a1 = a, b1 = b;
    while (b1) {
        int q = a1 / b1;
        tie(x, x1) = make_tuple(x1, x - q * x1);
        tie(y, y1) = make_tuple(y1, y - q * y1);
        tie(a1, b1) = make_tuple(b1, a1 - q * b1);
    }
    return a1;
}
```

Nếu quan sát kỹ các biến `a1` và `b1`, bạn sẽ nhận thấy chúng nhận các giá trị hoàn toàn giống như trong phiên bản vòng lặp của [Thuật toán Euclid](euclid-algorithm.md#implementation) thông thường. Vì vậy, thuật toán chắc chắn sẽ tính ra GCD chính xác.

Để hiểu tại sao thuật toán tính ra các hệ số chính xác, hãy xem xét các bất biến (invariants) sau đây luôn được duy trì tại mọi thời điểm (trước khi bắt đầu vòng lặp while và tại cuối mỗi vòng lặp):

$$x \cdot a + y \cdot b = a_1$$

$$x_1 \cdot a + y_1 \cdot b = b_1$$

Ký hiệu các giá trị ở cuối một vòng lặp bằng dấu phẩy ($'$), và giả sử $q = \frac{a_1}{b_1}$. Từ [Thuật toán Euclid](euclid-algorithm.md), ta có:

$$a_1' = b_1$$

$$b_1' = a_1 - q \cdot b_1$$

Để bất biến đầu tiên tiếp tục được duy trì, điều sau đây phải đúng:

$$x' \cdot a + y' \cdot b = a_1' = b_1$$

$$x' \cdot a + y' \cdot b = x_1 \cdot a + y_1 \cdot b$$

Tương tự đối với bất biến thứ hai, điều sau đây phải được duy trì:

$$x_1' \cdot a + y_1' \cdot b = a_1 - q \cdot b_1$$

$$x_1' \cdot a + y_1' \cdot b = (x - q \cdot x_1) \cdot a + (y - q \cdot y_1) \cdot b$$

Bằng cách so sánh các hệ số của $a$ và $b$, chúng ta có thể rút ra các phương trình cập nhật cho từng biến, đảm bảo các bất biến luôn được duy trì trong suốt thuật toán.

Khi kết thúc vòng lặp, ta biết $a_1$ chứa GCD, do đó $x \cdot a + y \cdot b = g$. Điều này có nghĩa là chúng ta đã tìm thấy các hệ số cần thiết.

Bạn có thể tối ưu hóa mã nguồn hơn nữa bằng cách loại bỏ các biến $a_1$ và $b_1$, và chỉ sử dụng lại $a$ và $b$. Tuy nhiên, nếu làm vậy, bạn sẽ mất đi khả năng lập luận dựa trên các bất biến.

## Bài tập thực hành

* [UVA - 10104 - Euclid Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1045)
* [GYM - (J) Once Upon A Time](http://codeforces.com/gym/100963)
* [UVA - 12775 - Gift Dilemma](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4628)
