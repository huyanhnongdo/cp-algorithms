---
tags:
  - Translated
e_maxx_link: roots_newton
lang: vi
---

# Phương pháp Newton để tìm nghiệm

Đây là một phương pháp lặp được Isaac Newton phát minh vào khoảng năm 1664. Tuy nhiên, phương pháp này đôi khi còn được gọi là phương pháp Raphson, vì Raphson đã phát minh ra thuật toán tương tự vài năm sau Newton, nhưng bài viết của ông được xuất bản sớm hơn nhiều.

Bài toán đặt ra như sau. Cho phương trình:

$$f(x) = 0$$

Chúng ta muốn giải phương trình này. Chính xác hơn là muốn tìm một nghiệm của nó (giả định rằng nghiệm đó tồn tại). Ta giả định rằng hàm số $f(x)$ liên tục và khả vi (differentiable) trên đoạn $[a, b]$.

## Thuật toán

Các tham số đầu vào của thuật toán không chỉ bao gồm hàm số $f(x)$ mà còn cả giá trị xấp xỉ ban đầu - một giá trị $x_0$ nào đó mà thuật toán sẽ bắt đầu.

<p align="center" markdown="1">

![plot_f(x)](roots_newton.png)

</p>

Giả sử chúng ta đã tính được $x_i$, ta tính $x_{i+1}$ như sau. Vẽ tiếp tuyến với đồ thị hàm số $f(x)$ tại điểm $x = x_i$, và tìm giao điểm của tiếp tuyến này với trục hoành (trục $x$). Giá trị $x_{i+1}$ được gán bằng hoành độ của giao điểm tìm được, và chúng ta lặp lại toàn bộ quá trình từ đầu.

Không khó để rút ra công thức sau:

$$ x_{i+1} = x_i - \frac{f(x_i)}{f^\prime(x_i)} $$

Đầu tiên, chúng ta tính hệ số góc $f'(x)$, đạo hàm của $f(x)$, rồi sau đó xác định phương trình tiếp tuyến:

$$ y - f(x_i) = f'(x_i)(x - x_i) $$ 

Tiếp tuyến cắt trục hoành tại tọa độ $y = 0$ và $x = x_{i+1}$:

$$ - f(x_i) = f'(x_i)(x_{i+1} - x_i) $$ 

Giải phương trình trên, chúng ta thu được giá trị của $x_{i+1}$.

Trực giác cho thấy nếu hàm số $f(x)$ "tốt" (trơn), và $x_i$ đủ gần nghiệm, thì $x_{i+1}$ sẽ còn gần nghiệm cần tìm hơn nữa.

Tốc độ hội tụ của thuật toán là bậc hai (quadratic), có nghĩa là số chữ số chính xác trong giá trị xấp xỉ $x_i$ sẽ tăng gấp đôi sau mỗi vòng lặp.

## Ứng dụng tính căn bậc hai

Chúng ta hãy lấy việc tính căn bậc hai làm ví dụ cho phương pháp Newton.

Nếu thay $f(x) = x^2 - n$, sau khi rút gọn biểu thức, ta thu được:

$$ x_{i+1} = \frac{x_i + \frac{n}{x_i}}{2} $$

Biến thể điển hình đầu tiên của bài toán là cho trước một số hữu tỉ $n$, và cần tính căn bậc hai của nó với một độ chính xác `eps` cho trước:

```cpp
double sqrt_newton(double n) {
	const double eps = 1E-15;
	double x = 1;
	for (;;) {
		double nx = (x + n / x) / 2;
		if (abs(x - nx) < eps)
			break;
		x = nx;
	}
	return x;
}
```

Một biến thể phổ biến khác của bài toán là khi chúng ta cần tính căn nguyên (cho số nguyên $n$, tìm số nguyên $x$ lớn nhất sao cho $x^2 \le n$). Ở đây chúng ta cần thay đổi một chút điều kiện dừng của thuật toán, vì có khả năng giá trị $x$ sẽ bắt đầu "dao động" quanh đáp án. Do đó, chúng ta thêm điều kiện là nếu giá trị $x$ đã giảm ở bước trước đó, và lại cố gắng tăng lên ở bước hiện tại, thì thuật toán phải dừng lại.

```cpp
int isqrt_newton(int n) {
	int x = 1;
	bool decreased = false;
	for (;;) {
		int nx = (x + n / x) >> 1;
		if (x == nx || nx > x && decreased)
			break;
		decreased = nx < x;
		x = nx;
	}
	return x;
}
```

Cuối cùng là biến thể thứ ba - dành cho trường hợp số lớn (bignum arithmetic). Vì số $n$ có thể rất lớn, việc chú ý đến giá trị xấp xỉ ban đầu là vô cùng hợp lý. Rõ ràng, giá trị này càng gần nghiệm thì kết quả đạt được càng nhanh. Một cách đơn giản và hiệu quả là chọn xấp xỉ ban đầu bằng số $2^{\textrm{bits}/2}$, trong đó $\textrm{bits}$ là số lượng bit của số $n$. Dưới đây là mã Java minh họa cho biến thể này:

```java
public static BigInteger isqrtNewton(BigInteger n) {
	BigInteger a = BigInteger.ONE.shiftLeft(n.bitLength() / 2);
	boolean p_dec = false;
	for (;;) {
		BigInteger b = n.divide(a).add(a).shiftRight(1);
		if (a.compareTo(b) == 0 || a.compareTo(b) < 0 && p_dec)
			break;
		p_dec = a.compareTo(b) > 0;
		a = b;
	}
	return a;
}
```

Ví dụ, đoạn mã này thực thi trong khoảng $60$ mili-giây với $n = 10^{1000}$. Nếu bỏ qua việc tối ưu chọn xấp xỉ ban đầu (chỉ bắt đầu từ $1$), thời gian thực thi sẽ tăng lên khoảng $120$ mili-giây.

## Bài tập thực hành
- [UVa 10428 - The Roots](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=16&page=show_problem&problem=1369)
