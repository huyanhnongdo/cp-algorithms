---
tags:
  - Translated
e_maxx_link: ternary_search
lang: vi
---

# Tìm kiếm tam phân (Ternary Search)

Cho một hàm số $f(x)$ đơn đỉnh (unimodal) trên đoạn $[l, r]$. Hàm đơn đỉnh là hàm số có một trong hai tính chất sau: 

1. Hàm số tăng ngặt trước tiên, đạt giá trị cực đại (tại một điểm duy nhất hoặc trên một khoảng), sau đó giảm ngặt.

2. Hàm số giảm ngặt trước tiên, đạt giá trị cực tiểu, sau đó tăng ngặt.

Trong bài viết này, chúng ta sẽ giả định trường hợp đầu tiên. Trường hợp thứ hai hoàn toàn đối xứng với trường hợp thứ nhất.

Nhiệm vụ là tìm giá trị cực đại của hàm số $f(x)$ trên đoạn $[l, r]$.

## Thuật toán

Xét 2 điểm bất kỳ $m_1$ và $m_2$ trong đoạn này: $l < m_1 < m_2 < r$. Chúng ta tính giá trị hàm số tại $m_1$ và $m_2$, tức là tìm các giá trị $f(m_1)$ và $f(m_2)$. Khi đó, có một trong ba trường hợp xảy ra:

-   $f(m_1) < f(m_2)$

    Cực đại cần tìm không thể nằm ở phía bên trái của $m_1$, tức là trên đoạn $[l, m_1]$, vì cả hai điểm $m_1$ và $m_2$ hoặc chỉ riêng $m_1$ thuộc vùng hàm số đồng biến. Trong cả hai trường hợp, điều này có nghĩa là chúng ta phải tìm kiếm cực đại trong đoạn $[m_1, r]$.

-   $f(m_1) > f(m_2)$

    Trường hợp này đối xứng với trường hợp trước: cực đại không thể nằm ở phía bên phải của $m_2$, tức là trên đoạn $[m_2, r]$, và không gian tìm kiếm được thu hẹp lại thành đoạn $[l, m_2]$.

-   $f(m_1) = f(m_2)$

    Ta có thể thấy rằng cả hai điểm này đều thuộc vùng hàm số đạt giá trị cực đại, hoặc $m_1$ thuộc vùng đồng biến và $m_2$ thuộc vùng nghịch biến (ở đây chúng ta sử dụng tính chất tăng/giảm ngặt của hàm số). Do đó, không gian tìm kiếm được thu hẹp về $[m_1, m_2]$. Để đơn giản hóa mã nguồn, trường hợp này có thể được kết hợp với bất kỳ trường hợp nào trong hai trường hợp trên.

Do đó, dựa trên việc so sánh giá trị tại hai điểm nằm trong đoạn, chúng ta có thể thay thế đoạn hiện tại $[l, r]$ bằng một đoạn mới ngắn hơn $[l^\prime, r^\prime]$. Áp dụng lặp đi lặp lại quy trình trên, chúng ta có thể thu được một đoạn ngắn tùy ý. Cuối cùng, độ dài của nó sẽ nhỏ hơn một hằng số định sẵn (độ chính xác), và quá trình có thể dừng lại. Đây là một phương pháp số (numerical method), vì vậy chúng ta có thể coi như hàm số đạt cực đại tại mọi điểm của đoạn cuối cùng $[l, r]$. Không mất tính tổng quát, chúng ta có thể lấy $f(l)$ làm giá trị trả về.

Chúng ta không áp dụng bất kỳ ràng buộc nào lên việc chọn các điểm $m_1$ và $m_2$. Sự lựa chọn này sẽ quyết định tốc độ hội tụ và độ chính xác của cài đặt. Cách phổ biến nhất là chọn các điểm sao cho chúng chia đoạn $[l, r]$ thành ba phần bằng nhau. Do đó, ta có:

$$m_1 = l + \frac{(r - l)}{3}$$

$$m_2 = r - \frac{(r - l)}{3}$$ 

Nếu $m_1$ và $m_2$ được chọn gần nhau hơn, tốc độ hội tụ sẽ tăng lên một chút.

### Phân tích thời gian chạy

$$T(n) = T({2n}/{3}) + O(1) = \Theta(\log n)$$

Chúng ta có thể hình dung như sau: mỗi lần sau khi tính giá trị hàm số tại các điểm $m_1$ và $m_2$, về cơ bản chúng ta sẽ bỏ đi khoảng một phần ba đoạn tìm kiếm (ở bên trái hoặc bên phải). Do đó kích thước của không gian tìm kiếm chỉ còn bằng ${2n}/{3}$ so với ban đầu.

Áp dụng [Định lý Thợ (Master's Theorem)](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)), ta thu được ước lượng độ phức tạp mong muốn.

### Trường hợp đối số nguyên

Nếu $f(x)$ nhận tham số nguyên, đoạn $[l, r]$ trở nên rời rạc. Vì chúng ta không đưa ra bất kỳ ràng buộc nào đối với việc lựa chọn các điểm $m_1$ và $m_2$, tính đúng đắn của thuật toán không bị ảnh hưởng. $m_1$ và $m_2$ vẫn có thể được chọn để chia đoạn $[l, r]$ thành 3 phần xấp xỉ bằng nhau.

Sự khác biệt xảy ra ở điều kiện dừng của thuật toán. Tìm kiếm tam phân sẽ phải dừng lại khi $(r - l) < 3$, bởi vì trong trường hợp đó chúng ta không thể chọn $m_1$ và $m_2$ khác biệt với nhau cũng như khác biệt với $l$ và $r$, điều này có thể dẫn đến vòng lặp vô hạn. Khi $(r - l) < 3$, ta chỉ cần duyệt qua các điểm ứng viên còn lại $(l, l + 1, \dots, r)$ để tìm điểm mang lại giá trị lớn nhất cho hàm số $f(x)$.

### Tìm kiếm tỷ lệ vàng (Golden section search)

Trong một số trường hợp, việc tính giá trị $f(x)$ có thể khá chậm, nhưng việc giảm số lượng vòng lặp là không khả thi do vấn đề về độ chính xác. May mắn thay, chúng ta có thể chỉ cần tính $f(x)$ một lần duy nhất ở mỗi vòng lặp (ngoại trừ vòng lặp đầu tiên).

Để thấy cách thực hiện, chúng ta hãy xem lại phương pháp chọn $m_1$ và $m_2$. Giả sử ta chọn $m_1$ và $m_2$ trên đoạn $[l, r]$ sao cho $\frac{r - l}{r - m_1} = \frac{r - l}{m_2 - l} = \varphi$, với $\varphi$ là một hằng số nào đó. Để giảm thiểu khối lượng tính toán, ta muốn chọn $\varphi$ sao cho ở vòng lặp tiếp theo, một trong các điểm đánh giá mới $m_1'$, $m_2'$ sẽ trùng với $m_1$ hoặc $m_2$, nhờ đó ta có thể tái sử dụng giá trị hàm số đã tính.

Bây giờ giả sử sau vòng lặp hiện tại, chúng ta gán $l = m_1$. Khi đó điểm $m_1'$ sẽ thỏa mãn $\frac{r - m_1}{r - m_1'} = \varphi$. Chúng ta muốn điểm này trùng với $m_2$, tức là $\frac{r - m_1}{r - m_2} = \varphi$.

Nhân cả hai vế của phương trình $\frac{r - m_1}{r - m_2} = \varphi$ với $\frac{r - m_2}{r - l}$, ta thu được $\frac{r - m_1}{r - l} = \varphi\frac{r - m_2}{r - l}$. Lưu ý rằng $\frac{r - m_1}{r - l} = \frac{1}{\varphi}$ và $\frac{r - m_2}{r - l} = \frac{r - l + l - m_2}{r - l} = 1 - \frac{1}{\varphi}$. Thay vào phương trình và nhân với $\varphi$, ta thu được phương trình sau:

$\varphi^2 - \varphi - 1 = 0$

Đây chính là phương trình tỷ lệ vàng quen thuộc. Giải phương trình này ta được $\frac{1 \pm \sqrt{5}}{2}$. Vì $\varphi$ phải là số dương, ta chọn $\varphi = \frac{1 + \sqrt{5}}{2}$. Áp dụng suy luận tương tự cho trường hợp ta gán $r = m_2$ và muốn $m_2'$ trùng với $m_1$, ta cũng thu được giá trị $\varphi$ tương tự. Như vậy, nếu ta chọn $m_1 = l + \frac{r - l}{1 + \varphi}$ và $m_2 = r - \frac{r - l}{1 + \varphi}$, ở mỗi vòng lặp ta có thể tái sử dụng một trong các giá trị $f(x)$ đã được tính ở vòng lặp trước.

## Cài đặt

```cpp
double ternary_search(double l, double r) {
	double eps = 1e-9;				//set the error limit here
	while (r - l > eps) {
		double m1 = l + (r - l) / 3;
		double m2 = r - (r - l) / 3;
		double f1 = f(m1);		//evaluates the function at m1
		double f2 = f(m2);		//evaluates the function at m2
		if (f1 < f2)
			l = m1;
		else
			r = m2;
	}
	return f(l);					//return the maximum of f(x) in [l, r]
}
```

Ở đây `eps` chính là sai số tuyệt đối (chưa tính đến các sai số do việc tính toán không chính xác của hàm số).

Thay vì sử dụng điều kiện `r - l > eps`, chúng ta có thể chọn số lượng vòng lặp cố định làm điều kiện dừng. Số lượng vòng lặp nên được lựa chọn để đảm bảo độ chính xác yêu cầu. Thông thường, trong hầu hết các bài toán lập trình thi đấu, giới hạn sai số là ${10}^{-6}$, do đó khoảng 200 - 300 vòng lặp là đủ. Hơn nữa, số lượng vòng lặp này không phụ thuộc vào giá trị của $l$ và $r$, vì vậy số lượng vòng lặp tương ứng trực tiếp với sai số tương đối mong muốn.

## Bài tập thực hành

- [Codeforces - New Bakery](https://codeforces.com/problemset/problem/1978/B)
- [Codechef - Race time](https://www.codechef.com/problems/AMCS03)
- [Hackerearth - Rescuer](https://www.hackerearth.com/problem/algorithm/rescuer-2d2495cb/)
- [Spoj - Building Construction](http://www.spoj.com/problems/KOPC12A/)
- [Codeforces - Weakness and Poorness](http://codeforces.com/problemset/problem/578/C)
* [LOJ - Closest Distance](http://lightoj.com/volume_showproblem.php?problem=1146)
* [GYM - Dome of Circus (D)](http://codeforces.com/gym/101309)
* [UVA - Galactic Taxes](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4898)
* [GYM - Chasing the Cheetahs (A)](http://codeforces.com/gym/100829)
* [UVA - 12197 - Trick or Treat](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3349)
* [SPOJ - Building Construction](http://www.spoj.com/problems/KOPC12A/)
* [Codeforces - Devu and his Brother](https://codeforces.com/problemset/problem/439/D)
* [Codechef - Is This JEE ](https://www.codechef.com/problems/ICM2003)
* [Codeforces - Restorer Distance](https://codeforces.com/contest/1355/problem/E)
* [TIMUS 1058 Chocolate](https://acm.timus.ru/problem.aspx?space=1&num=1058)
* [TIMUS 1436 Billboard](https://acm.timus.ru/problem.aspx?space=1&num=1436)
* [TIMUS 1451 Beerhouse Tale](https://acm.timus.ru/problem.aspx?space=1&num=1451)
* [TIMUS 1719 Kill the Shaitan-Boss](https://acm.timus.ru/problem.aspx?space=1&num=1719)
* [TIMUS 1913 Titan Ruins: Alignment of Forces](https://acm.timus.ru/problem.aspx?space=1&num=1913)
