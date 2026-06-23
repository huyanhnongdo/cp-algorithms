---
tags:
  - Translated
---

# Các phép toán trên đa thức và chuỗi lũy thừa

Các bài toán trong lập trình thi đấu, đặc biệt là các bài toán liên quan đến đếm tổ hợp, thường được giải quyết bằng cách đưa về tính toán trên đa thức và chuỗi lũy thừa hình thức (formal power series).

Điều này bao gồm các khái niệm như nhân đa thức, nội suy đa thức, và các phép toán phức tạp hơn như hàm logarit và hàm mũ của đa thức. Trong bài viết này, chúng tôi sẽ trình bày một cái nhìn tổng quan ngắn gọn về các phép toán này và các cách tiếp cận phổ biến cho chúng.

## Các khái niệm cơ bản và tính chất

Trong phần này, chúng ta tập trung hơn vào các định nghĩa và tính chất trực quan của các phép toán đa thức khác nhau. Chi tiết kỹ thuật về việc cài đặt và độ phức tạp của chúng sẽ được đề cập ở các phần sau.

### Nhân đa thức

!!! info "Định nghĩa"
	**Đa thức một biến (univariate polynomial)** là một biểu thức có dạng $A(x) = a_0 + a_1 x + \dots + a_n x^n$.

Các giá trị $a_0, \dots, a_n$ là các hệ số của đa thức, thường được lấy từ một tập hợp các số hoặc các cấu trúc giống số. Trong bài viết này, chúng tôi giả định rằng các hệ số được lấy từ một [trường (field)](https://en.wikipedia.org/wiki/Field_(mathematics)), nghĩa là các phép toán cộng, trừ, nhân và chia được định nghĩa rõ ràng trên chúng (ngoại trừ phép chia cho $0$) và chúng nhìn chung hoạt động tương tự như số thực.
	
Một ví dụ điển hình về trường như vậy là trường các số dư theo mô-đun của một số nguyên tố $p$.

Để đơn giản, chúng ta sẽ bỏ từ *một biến*, vì đây là loại đa thức duy nhất chúng ta xem xét trong bài viết này. Chúng ta cũng sẽ viết $A$ thay vì $A(x)$ bất cứ khi nào có thể, điều này sẽ dễ hiểu từ ngữ cảnh. Giả định rằng $a_n \neq 0$ hoặc $A(x)=0$.

!!! info "Định nghĩa"
	**Tích (product)** của hai đa thức được định nghĩa bằng cách khai triển nó dưới dạng một biểu thức số học:

	$$
	A(x) B(x) = \left(\sum\limits_{i=0}^n a_i x^i \right)\left(\sum\limits_{j=0}^m b_j x^j\right) = \sum\limits_{i,j} a_i b_j x^{i+j} = \sum\limits_{k=0}^{n+m} c_k x^k = C(x).
	$$

	Dãy $c_0, c_1, \dots, c_{n+m}$ gồm các hệ số của $C(x)$ được gọi là **tích chập (convolution)** của $a_0, \dots, a_n$ và $b_0, \dots, b_m$.

!!! info "Định nghĩa"
	**Bậc (degree)** của một đa thức $A$ với $a_n \neq 0$ được định nghĩa là $\deg A = n$.
	
	Để nhất quán, bậc của đa thức $A(x) = 0$ được định nghĩa là $\deg A = -\infty$.

Theo quy ước này, $\deg AB = \deg A + \deg B$ với mọi đa thức $A$ và $B$.

Tích chập là cơ sở để giải quyết nhiều bài toán đếm tổ hợp.

!!! Example
	Bạn có $n$ đối tượng thuộc loại thứ nhất và $m$ đối tượng thuộc loại thứ hai.

	Các đối tượng thuộc loại thứ nhất có giá trị lần lượt là $a_1, \dots, a_n$, và các đối tượng thuộc loại thứ hai có giá trị là $b_1, \dots, b_m$.

	Bạn chọn một đối tượng thuộc loại thứ nhất và một đối tượng thuộc loại thứ hai. Có bao nhiêu cách để nhận được tổng giá trị là $k$?

??? hint "Lời giải"
	Xét tích $(x^{a_1} + \dots + x^{a_n})(x^{b_1} + \dots + x^{b_m})$. If you expand it, each monomial will correspond to the pair $(a_i, b_j)$ and contribute to the coefficient near $x^{a_i+b_j}$. Nói cách khác, câu trả lời chính là hệ số của số hạng $x^k$ trong tích đa thức thu được.

!!! Example
	Bạn gieo một con xúc xắc $6$-mặt $n$ lần và cộng tổng số điểm thu được. Xác suất để nhận được tổng điểm bằng $k$ là bao nhiêu?

??? hint "Lời giải"
	Câu trả lời là số lượng kết quả có tổng bằng $k$, chia cho tổng số kết quả có thể xảy ra, tức là $6^n$.

	Số lượng kết quả có tổng bằng $k$ là bao nhiêu? Với $n=1$, nó có thể được biểu diễn bằng đa thức $A(x) = x^1+x^2+\dots+x^6$.

	Với $n=2$, sử dụng cách tiếp cận tương tự như trong ví dụ trên, chúng ta kết luận rằng nó được biểu diễn bởi đa thức $(x^1+x^2+\dots+x^6)^2$.

	Như vậy, câu trả lời cho bài toán chính là hệ số thứ $k$ của đa thức $(x^1+x^2+\dots+x^6)^n$, chia cho $6^n$.

Hệ số của số hạng $x^k$ trong đa thức $A(x)$ được ký hiệu ngắn gọn là $[x^k]A$.

### Chuỗi lũy thừa hình thức

!!! info "Định nghĩa"
	**Chuỗi lũy thừa hình thức (formal power series)** là một tổng vô hạn $A(x) = a_0 + a_1 x + a_2 x^2 + \dots$, được xem xét mà không cần quan tâm đến tính hội tụ của nó.

Nói cách khác, khi chúng ta xét ví dụ tổng $1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\dots=2$, chúng ta ngầm hiểu rằng nó *hội tụ* về $2$ khi số lượng số hạng tiến tới vô cùng. Tuy nhiên, chuỗi hình thức chỉ được xem xét dưới dạng các dãy số tạo nên chúng.

!!! info "Định nghĩa"
	**Tích (product)** của hai chuỗi lũy thừa hình thức $A(x)$ and $B(x)$ cũng được định nghĩa bằng cách khai triển nó như một biểu thức số học:

	$$
	A(x) B(x) = \left(\sum\limits_{i=0}^\infty a_i x^i \right)\left(\sum\limits_{j=0}^\infty b_j x^j\right) = \sum\limits_{i,j} a_i b_j x^{i+j} = \sum\limits_{k=0}^{\infty} c_k x^k = C(x),
	$$

	trong đó các hệ số $c_0, c_1, \dots$ được định nghĩa là các tổng hữu hạn:

	$$
	c_k = \sum\limits_{i=0}^k a_i b_{k-i}.
	$$

	Dãy $c_0, c_1, \dots$ cũng được gọi là **tích chập (convolution)** của $a_0, a_1, \dots$ và $b_0, b_1, \dots$, mở rộng khái niệm này cho các dãy vô hạn.

Như vậy, đa thức có thể được coi là chuỗi lũy thừa hình thức nhưng chỉ có một số hữu hạn các hệ số khác không.

Chuỗi lũy thừa hình thức đóng vai trò quan trọng trong tổ hợp đếm, nơi chúng được nghiên cứu dưới dạng các [hàm sinh (generating functions)](https://en.wikipedia.org/wiki/Generating_function) cho các dãy số khác nhau. Việc giải thích chi tiết về hàm sinh và ý nghĩa trực quan của chúng nằm ngoài phạm vi bài viết này, do đó độc giả tò mò có thể tham khảo thêm [tại đây](https://codeforces.com/blog/entry/103979) để biết chi tiết về ý nghĩa tổ hợp của chúng.

Tuy nhiên, chúng tôi sẽ đề cập ngắn gọn rằng nếu $A(x)$ và $B(x)$ là các hàm sinh cho các dãy số đếm một số đối tượng theo số lượng "nguyên tử" trong chúng (ví dụ: cây theo số lượng đỉnh), thì tích $A(x) B(x)$ sẽ đếm các đối tượng có thể được mô tả dưới dạng các cặp đối tượng thuộc loại $A$ và $B$, được đếm theo tổng số "nguyên tử" trong cặp đó.

!!! Example
	Gọi $A(x) = \sum\limits_{i=0}^\infty 2^i x^i$ là hàm sinh đếm các túi đá, mỗi viên đá được tô bằng một trong $2$ màu (do đó, có $2^i$ túi như vậy có kích thước $i$) và $B(x) = \sum\limits_{j=0}^{\infty} 3^j x^j$ đếm các túi đá, mỗi viên đá được tô bằng một trong $3$ màu. Khi đó $C(x) = A(x) B(x) = \sum\limits_{k=0}^\infty c_k x^k$ sẽ đếm các đối tượng có thể được mô tả là "hai túi đá, túi thứ nhất chỉ gồm các viên đá loại $A$, túi thứ hai chỉ gồm các viên đá loại $B$, với tổng số viên đá là $k$" cho hệ số $c_k$.

Tương tự như vậy, có một ý nghĩa trực quan cho một số hàm số khác trên chuỗi lũy thừa hình thức.

### Phép chia đa thức (Euclide)

Tương tự như số nguyên, chúng ta có thể định nghĩa phép chia có dư cho các đa thức.

!!! info "Định nghĩa"
	Với mọi đa thức $A$ và $B \neq 0$, người ta có thể biểu diễn $A$ dưới dạng:

	$$
	A = D \cdot B + R,~ \deg R < \deg B,
	$$

	trong đó $R$ được gọi là **số dư (remainder)** của $A$ chia cho $B$ và $D$ được gọi là **thương (quotient)**.

Ký hiệu $\deg A = n$ và $\deg B = m$. Cách sơ cấp để thực hiện phép chia là đặt tính chia đa thức, trong đó bạn nhân $B$ với đơn thức $\frac{a_n}{b_m} x^{n - m}$ rồi trừ nó khỏi $A$, cho đến khi bậc của $A$ nhỏ hơn bậc của $B$. Đa thức còn lại cuối cùng của $A$ sẽ là số dư, và các đa thức dùng để nhân với $B$ trong quá trình đó, cộng lại với nhau, sẽ tạo thành đa thức thương.

!!! info "Định nghĩa"
	Nếu $A$ và $B$ có cùng số dư khi chia cho $C$, chúng được gọi là **đồng dư** theo mô-đun $C$, ký hiệu là:
	
	$$
	A \equiv B \pmod{C}.
	$$
	
Phép chia đa thức rất hữu ích vì nó có nhiều tính chất quan trọng:

- $A$ chia hết cho $B$ khi và chỉ khi $A \equiv 0 \pmod B$.

- Từ đó suy ra $A \equiv B \pmod C$ khi và chỉ khi $A-B$ chia hết cho $C$.

- Đặc biệt, $A \equiv B \pmod{C \cdot D}$ suy ra $A \equiv B \pmod{C}$.

- Với đa thức bậc nhất $x-r$, ta luôn có $A(x) \equiv A(r) \pmod{x-r}$.

- Từ đó suy ra $A$ chia hết cho $x-r$ khi và chỉ khi $A(r)=0$.

- Đối với mô-đun $x^k$, ta có $A \equiv a_0 + a_1 x + \dots + a_{k-1} x^{k-1} \pmod{x^k}$.

Lưu ý rằng phép chia đa thức có dư không thể được định nghĩa chính xác cho chuỗi lũy thừa hình thức. Thay vào đó, đối với bất kỳ chuỗi $A(x)$ nào có $a_0 \neq 0$, luôn tồn tại một chuỗi lũy thừa hình thức nghịch đảo $A^{-1}(x)$ sao cho $A(x) A^{-1}(x) = 1$. Thực tế này có thể được sử dụng để tính kết quả của phép chia đa thức.

## Cài đặt cơ bản
[Tại đây](https://cp-algorithms.github.io/cp-algorithms-aux/cp-algo/math/poly.hpp) bạn có thể tìm thấy cài đặt cơ bản của đại số đa thức.

Nó hỗ trợ tất cả các phép toán thông thường và một số phương thức hữu ích khác. Lớp chính là `poly<T>` cho các đa thức có hệ số thuộc kiểu dữ liệu `T`.

Tất cả các phép toán số học `+`, `-`, `*`, `%` và `/` đều được hỗ trợ, trong đó `%` và `/` biểu thị cho số dư và thương trong phép chia Euclide.

Ngoài ra còn có lớp `modular<m>` để thực hiện các phép toán số học trên các số dư theo mô-đun của một số nguyên tố `m`.

Các hàm hữu ích khác:

- `deriv()`: tính đạo hàm $P'(x)$ của đa thức $P(x)$.
- `integr()`: tính nguyên hàm $Q(x) = \int P(x)$ của đa thức $P(x)$ sao cho $Q(0)=0$.
- `inv(size_t n)`: tính $n$ hệ số đầu tiên của đa thức nghịch đảo $P^{-1}(x)$ trong thời gian $O(n \log n)$.
- `log(size_t n)`: tính $n$ hệ số đầu tiên của $\ln P(x)$ trong thời gian $O(n \log n)$.
- `exp(size_t n)`: tính $n$ hệ số đầu tiên của $\exp P(x)$ trong thời gian $O(n \log n)$.
- `pow(size_t k, size_t n)`: tính $n$ hệ số đầu tiên của $P^{k}(x)$ trong thời gian $O(n \log nk)$.
- `deg()`: trả về bậc của đa thức $P(x)$.
- `lead()`: trả về hệ số của số hạng có bậc cao nhất $x^{\deg P(x)}$.
- `resultant(poly<T> a, poly<T> b)`: tính kết quả thức (resultant) của hai đa thức $a$ và $b$ trong thời gian $O(|a| \cdot |b|)$.
- `bpow(T x, size_t n)`: tính $x^n$.
- `bpow(T x, size_t n, T m)`: tính $x^n \pmod{m}$.
- `chirpz(T z, size_t n)`: tính giá trị đa thức $P(1), P(z), P(z^2), \dots, P(z^{n-1})$ trong thời gian $O(n \log n)$.
- `vector<T> eval(vector<T> x)`: tính giá trị đa thức tại nhiều điểm $P(x_1), \dots, P(x_n)$ trong thời gian $O(n \log^2 n)$.
- `poly<T> inter(vector<T> x, vector<T> y)`: nội suy đa thức từ tập hợp các cặp điểm $P(x_i) = y_i$ trong thời gian $O(n \log^2 n)$.
- Và một số hàm khác, hãy tự do khám phá mã nguồn!

## Số học đa thức

### Phép nhân

Phép toán cốt lõi nhất là phép nhân hai đa thức. Nghĩa là, cho hai đa thức $A$ và $B$:

$$A = a_0 + a_1 x + \dots + a_n x^n$$

$$B = b_0 + b_1 x + \dots + b_m x^m$$

Bạn cần tính đa thức tích $C = A \cdot B$, được định nghĩa là:

$$\boxed{C = \sum\limits_{i=0}^n \sum\limits_{j=0}^m a_i b_j x^{i+j}}  = c_0 + c_1 x + \dots + c_{n+m} x^{n+m}.$$

Nó có thể được tính toán trong thời gian $O(n \log n)$ thông qua [Biến đổi Fourier nhanh (FFT)](fft.md) và hầu hết các phương pháp ở đây sẽ sử dụng nó như một chương trình con.

### Chuỗi nghịch đảo

Nếu $A(0) \neq 0$, luôn tồn tại một chuỗi lũy thừa hình thức vô hạn $A^{-1}(x) = q_0+q_1 x + q_2 x^2 + \dots$ sao cho $A^{-1} A = 1$. Thường ta sẽ cần tính $k$ hệ số đầu tiên của $A^{-1}$ (tức là tính nó theo mô-đun $x^k$). Có hai phương pháp chính để thực hiện việc này.

#### Chia để trị

Thuật toán này đã được đề cập trong [bài viết của Schönhage](http://algo.inria.fr/seminars/sem00-01/schoenhage.pdf) và lấy cảm hứng từ [phương pháp Graeffe](https://en.wikipedia.org/wiki/Graeffe's_method). Đã biết rằng đối với đa thức $B(x)=A(x)A(-x)$, ta có $B(x)=B(-x)$, tức là $B(x)$ là một đa thức chẵn. Điều này có nghĩa là nó chỉ có các hệ số khác không tại các bậc chẵn và có thể được biểu diễn dưới dạng $B(x)=T(x^2)$. Do đó, chúng ta có phép biến đổi sau:

$$A^{-1}(x) \equiv \frac{1}{A(x)} \equiv \frac{A(-x)}{A(x)A(-x)} \equiv \frac{A(-x)}{T(x^2)} \pmod{x^k}$$

Lưu ý rằng đa thức $T(x)$ có thể được tính bằng một phép nhân duy nhất, sau đó chúng ta chỉ quan tâm đến nửa đầu tiên của các hệ số của chuỗi nghịch đảo của nó. Điều này giúp giảm bài toán ban đầu tính $A^{-1} \pmod{x^k}$ về việc tính $T^{-1} \pmod{x^{\lceil k / 2 \rceil}}$.

Độ phức tạp của phương pháp này có thể được ước tính là:

$$T(n) = T(n/2) + O(n \log n) = O(n \log n).$$

#### Thuật toán Sieveking–Kung

Quá trình tổng quát được mô tả ở đây được gọi là nâng Hensel (Hensel lifting), theo bổ đề Hensel. Chúng ta sẽ tìm hiểu chi tiết hơn ở phần dưới, nhưng hiện tại hãy tập trung vào giải pháp đặc thù này. Phần "nâng" (lifting) ở đây có nghĩa là chúng ta bắt đầu với xấp xỉ ban đầu $B_0=q_0=a_0^{-1}$ (chính là $A^{-1} \pmod x$) rồi nâng dần mô-đun từ $\bmod x^a$ lên $\bmod x^{2a}$.

Gọi $B_k \equiv A^{-1} \pmod{x^a}$. Bước xấp xỉ tiếp theo cần thỏa mãn phương trình $A B_{k+1} \equiv 1 \pmod{x^{2a}}$ và có thể biểu diễn dưới dạng $B_{k+1} = B_k + x^a C$. Từ đây ta có phương trình:

$$A(B_k + x^{a}C) \equiv 1 \pmod{x^{2a}}.$$

Gọi $A B_k \equiv 1 + x^a D \pmod{x^{2a}}$, phương trình trên tương đương với:

$$x^a(D+AC) \equiv 0 \pmod{x^{2a}} \implies D \equiv -AC \pmod{x^a} \implies C \equiv -B_k D \pmod{x^a}.$$

Từ đây, ta có công thức cuối cùng là:

$$x^a C \equiv -B_k x^a D  \equiv B_k(1-AB_k) \pmod{x^{2a}} \implies \boxed{B_{k+1} \equiv B_k(2-AB_k) \pmod{x^{2a}}}$$

Do đó, bắt đầu từ $B_0 \equiv a_0^{-1} \pmod x$, chúng ta sẽ tính được dãy $B_k$ sao cho $AB_k \equiv 1 \pmod{x^{2^k}}$ với độ phức tạp là:

$$T(n) = T(n/2) + O(n \log n) = O(n \log n).$$

Thuật toán ở đây thoạt nhìn có vẻ phức tạp hơn thuật toán thứ nhất, nhưng nó có cơ sở thực tế rất vững chắc cũng như khả năng tổng quát hóa tuyệt vời khi nhìn từ một góc độ khác, điều này sẽ được giải thích rõ hơn ở phần dưới.

### Phép chia Euclide

Xét hai đa thức $A(x)$ và $B(x)$ có bậc là $n$ và $m$. Như đã nói ở trước, bạn có thể viết lại $A(x)$ dưới dạng:

$$A(x) = B(x) D(x) + R(x), \deg R < \deg B.$$

Giả sử $n \geq m$, điều này có nghĩa là $\deg D = n - m$ và $n-m+1$ hệ số lớn nhất của $A$ không ảnh hưởng đến đa thức dư $R$. Có nghĩa là bạn có thể khôi phục $D(x)$ từ $n-m+1$ hệ số lớn nhất của $A(x)$ và $B(x)$ nếu coi nó là một hệ phương trình.

Hệ phương trình tuyến tính đang nói đến có thể được viết dưới dạng như sau:

$$\begin{bmatrix} a_n \\ \vdots \\ a_{m+1} \\ a_{m} \end{bmatrix} = \begin{bmatrix}
b_m & \dots & 0 & 0 \\
\vdots & \ddots & \vdots & \vdots \\
\dots & \dots & b_m & 0 \\
\dots & \dots & b_{m-1} & b_m
\end{bmatrix} \begin{bmatrix}d_{n-m} \\ \vdots \\ d_1 \\ d_0\end{bmatrix}$$

Nhìn vào hệ này, chúng ta có thể kết luận rằng bằng cách đưa vào các đa thức đảo ngược:

$$A^R(x) = x^nA(x^{-1})= a_n + a_{n-1} x + \dots + a_0 x^n$$

$$B^R(x) = x^m B(x^{-1}) = b_m + b_{m-1} x + \dots + b_0 x^m$$

$$D^R(x) = x^{n-m}D(x^{-1}) = d_{n-m} + d_{n-m-1} x + \dots + d_0 x^{n-m}$$

hệ phương trình có thể viết lại thành:

$$A^R(x) \equiv B^R(x) D^R(x) \pmod{x^{n-m+1}}.$$

Từ đây bạn có thể khôi phục một cách duy nhất tất cả các hệ số của đa thức $D(x)$:

$$\boxed{D^R(x) \equiv A^R(x) (B^R(x))^{-1} \pmod{x^{n-m+1}}}$$

Và từ kết quả này, ta khôi phục được số dư $R(x)$ bằng công thức $R(x) = A(x) - B(x)D(x)$.

Lưu ý rằng ma trận ở trên là một ma trận tam giác [Toeplitz matrix](https://en.wikipedia.org/wiki/Toeplitz_matrix), và như chúng ta thấy ở đây, việc giải hệ phương trình tuyến tính với ma trận Toeplitz bất kỳ thực chất tương đương với phép đảo ngược đa thức. Hơn nữa, ma trận nghịch đảo của nó cũng là ma trận tam giác Toeplitz và các phần tử của nó chính là các hệ số của đa thức $(B^R(x))^{-1} \pmod{x^{n-m+1}}$.

## Tính toán các hàm số của đa thức

### Phương pháp Newton

Hãy tổng quát hóa thuật toán Sieveking–Kung. Xét phương trình $F(P) = 0$ trong đó $P(x)$ là đa thức cần tìm và $F(x)$ là một hàm nhận giá trị đa thức được định nghĩa là:

$$F(x) = \sum\limits_{i=0}^\infty \alpha_i (x-\beta)^i,$$

với $\beta$ là một hằng số. Có thể chứng minh được rằng nếu ta đưa vào một biến hình thức mới $y$, chúng ta có thể biểu diễn $F(x)$ dưới dạng:

$$F(x) = F(y) + (x-y)F'(y) + (x-y)^2 G(x,y),$$

trong đó $F'(x)$ là chuỗi đạo hàm hình thức được định nghĩa là:

$$F'(x) = \sum\limits_{i=0}^\infty (i+1)\alpha_{i+1}(x-\beta)^i,$$

và $G(x, y)$ là một chuỗi lũy thừa hình thức của $x$ và $y$. Với kết quả này, chúng ta có thể tìm nghiệm bằng phương pháp lặp.

Gọi $F(Q_k) \equiv 0 \pmod{x^{a}}$. Chúng ta cần tìm $Q_{k+1} \equiv Q_k + x^a C \pmod{x^{2a}}$ sao cho $F(Q_{k+1}) \equiv 0 \pmod{x^{2a}}$.

Thay thế $x = Q_{k+1}$ và $y=Q_k$ vào công thức trên, ta được:

$$F(Q_{k+1}) \equiv F(Q_k) + (Q_{k+1} - Q_k) F'(Q_k) + (Q_{k+1} - Q_k)^2 G(x, y) \pmod x^{2a}.$$

Vì $Q_{k+1} - Q_k \equiv 0 \pmod{x^a}$, ta cũng có $(Q_{k+1} - Q_k)^2 \equiv 0 \pmod{x^{2a}}$, do đó:

$$0 \equiv F(Q_{k+1}) \equiv F(Q_k) + (Q_{k+1} - Q_k) F'(Q_k) \pmod{x^{2a}}.$$

Công thức cuối cùng cho chúng ta giá trị của $Q_{k+1}$:

$$\boxed{Q_{k+1} = Q_k - \dfrac{F(Q_k)}{F'(Q_k)} \pmod{x^{2a}}}$$

Như vậy, khi biết cách đảo ngược đa thức và cách tính $F(Q_k)$, chúng ta có thể tìm được $n$ hệ số của $P$ với độ phức tạp:

$$T(n) = T(n/2) + f(n),$$

trong đó $f(n)$ là thời gian cần thiết để tính $F(Q_k)$ và $F'(Q_k)^{-1}$, thường là $O(n \log n)$.

Quy tắc lặp ở trên được biết đến trong giải tích số với tên gọi là [phương pháp Newton (Newton's method)](https://en.wikipedia.org/wiki/Newton%27s_method).

#### Bổ đề Hensel

Như đã đề cập ở trước, về mặt hình thức và tổng quát, kết quả này được gọi là [Bổ đề Hensel (Hensel's lemma)](https://en.wikipedia.org/wiki/Hensel%27s_lemma) và nó thực tế có thể được sử dụng trong phạm vi rộng hơn khi làm việc với chuỗi các vành lồng nhau. Trong trường hợp cụ thể này, chúng ta làm việc với chuỗi các đa thức dư theo mô-đun $x$, $x^2$, $x^3$ và vân vân.

Một ví dụ khác mà phép nâng Hensel có thể hữu ích là các [số p-adic (p-adic numbers)](https://en.wikipedia.org/wiki/P-adic_number), tại đó chúng ta làm việc với chuỗi các số dư nguyên theo mô-đun $p$, $p^2$, $p^3$ và vân vân. Ví dụ, phương pháp Newton có thể được sử dụng để tìm tất cả các [số tự hình (automorphic numbers)](https://en.wikipedia.org/wiki/Automorphic_number) có thể (các số mà khi bình phương lên sẽ có tận cùng là chính nó) với một cơ số cho trước. Bài toán này được để lại như một bài tập cho bạn đọc. Bạn có thể tham khảo bài toán [này](https://timus.online/problem.aspx?space=1&num=1698) để kiểm tra xem giải pháp của mình có hoạt động với các số ở hệ cơ số $10$ hay không.

### Hàm Logarit

Đối với hàm $\ln P(x)$, ta đã biết công thức đạo hàm:

$$
\boxed{(\ln P(x))' = \dfrac{P'(x)}{P(x)}}
$$

Do đó chúng ta có thể tính $n$ hệ số của đa thức $\ln P(x)$ trong thời gian $O(n \log n)$.

### Chuỗi nghịch đảo

Hóa ra, chúng ta có thể tìm lại công thức tính đa thức nghịch đảo $A^{-1}$ bằng cách sử dụng phương pháp Newton.
Với bài toán này, ta xét phương trình $A=Q^{-1}$, do đó:

$$F(Q) = Q^{-1} - A$$

$$F'(Q) = -Q^{-2}$$

$$\boxed{Q_{k+1} \equiv Q_k(2-AQ_k) \pmod{x^{2^{k+1}}}}$$

### Hàm Mũ (Exponent)

Hãy tìm cách tính $e^{P(x)}=Q(x)$. Phương trình tương đương là $\ln Q = P$, do đó:

$$F(Q) = \ln Q - P$$

$$F'(Q) = Q^{-1}$$

$$\boxed{Q_{k+1} \equiv Q_k(1 + P - \ln Q_k) \pmod{x^{2^{k+1}}}}$$

### Lũy thừa bậc $k$ { data-toc-label="Lũy thừa bậc k" }

Bây giờ chúng ta cần tính $P^k(x)=Q$. Phép tính này có thể được thực hiện thông qua công thức sau:

$$Q = \exp\left[k \ln P(x)\right]$$

Tuy nhiên, lưu ý rằng bạn chỉ có thể tính toán chính xác hàm logarit và hàm mũ nếu bạn tìm được một xấp xỉ ban đầu $Q_0$ phù hợp.

Để tìm nó, bạn cần tính logarit hoặc mũ của hệ số tự do của đa thức.

Nhưng cách duy nhất hợp lý để thực hiện là nếu $P(0)=1$ đối với $Q = \ln P$ để có $Q(0)=0$, và nếu $P(0)=0$ đối với $Q = e^P$ để có $Q(0)=1$.

Vì vậy, bạn chỉ có thể sử dụng công thức trên nếu $P(0) = 1$. Trong trường hợp ngược lại, nếu $P(x) = \alpha x^t T(x)$ với $T(0)=1$, bạn có thể viết:

$$\boxed{P^k(x) = \alpha^kx^{kt} \exp[k \ln T(x)]}$$

Lưu ý rằng bạn cũng có thể tính căn bậc $k$ của một đa thức nếu bạn có thể tính được $\sqrt[k]{\alpha}$, ví dụ như khi $\alpha=1$.

## Tính giá trị và Nội suy

### Biến đổi Chirp-z

Đối với trường hợp cụ thể khi bạn cần tính giá trị đa thức tại các điểm $x_r = z^{2r}$, bạn có thể làm như sau:

$$A(z^{2r}) = \sum\limits_{k=0}^n a_k z^{2kr}$$

Hãy thay thế $2kr = r^2+k^2-(r-k)^2$. Khi đó tổng này được viết lại thành:

$$\boxed{A(z^{2r}) = z^{r^2}\sum\limits_{k=0}^n (a_k z^{k^2}) z^{-(r-k)^2}}$$

Biểu thức này (ngoại trừ nhân tử $z^{r^2}$ phía trước) tương đương với tích chập của hai dãy số $u_k = a_k z^{k^2}$ và $v_k = z^{-k^2}$.

Lưu ý rằng $u_k$ có chỉ số từ $0$ đến $n$ ở đây, và $v_k$ có chỉ số từ $-n$ đến $m$, với $m$ là lũy thừa lớn nhất của $z$ mà bạn cần tính.

Bây giờ, nếu bạn cần tính giá trị đa thức tại các điểm $x_r = z^{2r+1}$, bạn có thể đưa nó về bài toán trước đó bằng phép biến đổi hệ số $a_k \to a_k z^k$.

Điều này mang lại cho chúng ta một thuật toán độ phức tạp $O(n \log n)$ để tính giá trị đa thức tại các điểm lũy thừa của $z$, do đó bạn có thể tính DFT cho các kích thước không phải là lũy thừa của 2.

Một quan sát khác là $kr = \binom{k+r}{2} - \binom{k}{2} - \binom{r}{2}$. Khi đó ta có:

$$\boxed{A(z^r) = z^{-\binom{r}{2}}\sum\limits_{k=0}^n \left(a_k z^{-\binom{k}{2}}\right)z^{\binom{k+r}{2}}}$$

Hệ số của số hạng $x^{n+r}$ trong tích của hai đa thức $A_0(x) = \sum\limits_{k=0}^n a_{n-k}z^{-\binom{n-k}{2}}x^k$ và $A_1(x) = \sum\limits_{k\geq 0}z^{\binom{k}{2}}x^k$ chính bằng $z^{\binom{r}{2}}A(z^r)$. Bạn có thể sử dụng công thức $z^{\binom{k+1}{2}}=z^{\binom{k}{2}+k}$ để tính nhanh các hệ số của $A_0(x)$ và $A_1(x)$.

### Tính giá trị đa thức tại nhiều điểm
Giả sử bạn cần tính $A(x_1), \dots, A(x_n)$. Như đã đề cập ở trước, $A(x) \equiv A(x_i) \pmod{x-x_i}$. Do đó, bạn có thể thực hiện như sau:

1. Dựng một cây phân đoạn (segment tree) sao cho ở đoạn $[l,r)$ lưu trữ đa thức tích $P_{l, r}(x) = (x-x_l)(x-x_{l+1})\dots(x-x_{r-1})$.
2. Bắt đầu với nút gốc quản lý đoạn $l=1$ và $r=n+1$. Đặt $m=\lfloor(l+r)/2\rfloor$. Đi xuống nút con bên trái $[l,m)$ với đa thức cần tính là $A(x) \pmod{P_{l,m}(x)}$.
3. Lời gọi này sẽ tính đệ quy các giá trị $A(x_l), \dots, A(x_{m-1})$, tiếp theo làm tương tự cho con bên phải $[m,r)$ với đa thức $A(x) \pmod{P_{m,r}(x)}$.
4. Nối kết quả từ hai lời gọi đệ quy trái và phải lại và trả về.

Toàn bộ quy trình này sẽ chạy trong thời gian $O(n \log^2 n)$.

### Nội suy đa thức

Có một công thức trực tiếp của Lagrange để nội suy đa thức, cho trước một tập hợp các cặp điểm $(x_i, y_i)$:

$$\boxed{A(x) = \sum\limits_{i=1}^n y_i \prod\limits_{j \neq i}\dfrac{x-x_j}{x_i - x_j}}$$

Việc tính toán trực tiếp công thức này là rất khó, nhưng hóa ra chúng ta có thể tính nó trong thời gian $O(n \log^2 n)$ bằng phương pháp chia để trị:

Xét đa thức tích $P(x) = (x-x_1)\dots(x-x_n)$. Để biết các hệ số dưới mẫu số của $A(x)$, chúng ta cần tính các tích có dạng:

$$
P_i = \prod\limits_{j \neq i} (x_i-x_j)
$$

Nhưng nếu bạn lấy đạo hàm $P'(x)$, bạn sẽ thấy rằng $P'(x_i) = P_i$. Do đó bạn có thể tính nhanh các giá trị $P_i$ thông qua thuật toán tính giá trị đa thức tại nhiều điểm trong thời gian $O(n \log^2 n)$.

Bây giờ xét thuật toán đệ quy được thực hiện trên cùng cây phân đoạn như trong thuật toán tính giá trị tại nhiều điểm. Nó bắt đầu ở các lá với giá trị $\dfrac{y_i}{P_i}$ ở mỗi lá.

Khi chúng ta quay lui từ lời gọi đệ quy, chúng ta sẽ gộp kết quả từ các đỉnh con bên trái và bên phải theo công thức: $A_{l,r} = A_{l,m}P_{m,r} + P_{l,m} A_{m,r}$.

Bằng cách này, khi bạn quay trở lại nút gốc, bạn sẽ thu được chính xác đa thức $A(x)$ ở nút đó.
Tổng độ phức tạp của quy trình này cũng là $O(n \log^2 n)$.

## Ước chung lớn nhất (GCD) và Kết quả thức (Resultants)

Giả sử bạn được cho hai đa thức $A(x) = a_0 + a_1 x + \dots + a_n x^n$ và $B(x) = b_0 + b_1 x + \dots + b_m x^m$.

Gọi $\lambda_0, \dots, \lambda_n$ là các nghiệm của $A(x)$ và $\mu_0, \dots, \mu_m$ là các nghiệm của $B(x)$ tính cả số lần lặp (multiplicities).

Bạn muốn biết liệu $A(x)$ và $B(x)$ có nghiệm chung nào hay không. Có hai cách liên hệ chặt chẽ với nhau để thực hiện việc này.

### Thuật toán Euclid

Chúng ta đã có một [bài viết](euclid-algorithm.md) nói về nó. Đối với một miền đa thức bất kỳ, bạn có thể viết thuật toán Euclid đơn giản như sau:

```cpp
template<typename T>
T gcd(const T &a, const T &b) {
	return b == T(0) ? a : gcd(b, a % b);
}
```

Có thể chứng minh được rằng đối với các đa thức $A(x)$ and $B(x)$, thuật toán này hoạt động trong thời gian $O(nm)$.

### Kết quả thức (Resultant)

Hãy tính tích $A(\mu_0)\cdots A(\mu_m)$. Tích này sẽ bằng không khi và chỉ khi có nghiệm $\mu_i$ nào đó cũng là nghiệm của $A(x)$.

Để đảm bảo tính đối xứng, chúng ta có thể nhân tích này với $b_m^n$ và viết lại toàn bộ tích dưới dạng sau:

$$\boxed{\mathcal{R}(A, B) = b_m^n\prod\limits_{j=0}^m A(\mu_j) = b_m^n a_m^n \prod\limits_{i=0}^n \prod\limits_{j=0}^m (\mu_j - \lambda_i)= (-1)^{mn}a_n^m \prod\limits_{i=0}^n B(\lambda_i)}$$

Giá trị được định nghĩa ở trên được gọi là kết quả thức (resultant) của hai đa thức $A(x)$ và $B(x)$. Từ định nghĩa, bạn có thể tìm thấy các tính chất sau:

1. $\mathcal R(A, B) = (-1)^{nm} \mathcal R(B, A)$.
2. $\mathcal R(A, B)= a_n^m b_m^n$ khi $n=0$ hoặc $m=0$.
3. Nếu $b_m=1$ thì $\mathcal R(A - CB, B) = \mathcal R(A, B)$ với đa thức $C(x)$ bất kỳ và $n,m \geq 1$.
4. Từ đây suy ra $\mathcal R(A, B) = b_m^{\deg(A) - \deg(A-CB)}\mathcal R(A - CB, B)$ với các đa thức $A(x)$, $B(x)$, $C(x)$ bất kỳ.

Một điều kỳ diệu là kết quả thức của hai đa thức thực chất luôn thuộc cùng một vành với các hệ số của chúng!

Ngoài ra, các tính chất này cho phép chúng ta tính toán kết quả thức song song với thuật toán Euclid, hoạt động trong thời gian $O(nm)$.

```cpp
template<typename T>
T resultant(poly<T> a, poly<T> b) {
	if(b.is_zero()) {
		return 0;
	} else if(b.deg() == 0) {
		return bpow(b.lead(), a.deg());
	} else {
		int pw = a.deg();
		a %= b;
		pw -= a.deg();
		base mul = bpow(b.lead(), pw) * base((b.deg() & a.deg() & 1) ? -1 : 1);
		base ans = resultant(b, a);
		return ans * mul;
	}
}
```

### Thuật toán nửa GCD (Half-GCD)

Có một phương pháp giúp tính toán ước chung lớn nhất GCD và kết quả thức resultant trong thời gian $O(n \log^2 n)$.

Thủ tục để làm điều đó triển khai một phép biến đổi tuyến tính $2 \times 2$ ánh xạ một cặp đa thức $a(x)$, $b(x)$ thành một cặp đa thức khác $c(x), d(x)$ sao cho $\deg d(x) \leq \frac{\deg a(x)}{2}$. Nếu cẩn thận, bạn có thể tính toán nửa GCD của bất kỳ cặp đa thức nào với tối đa $2$ lời gọi đệ quy cho các đa thức nhỏ hơn ít nhất $2$ lần.

Chi tiết cụ thể của thuật toán khá tẻ nhạt để giải thích, tuy nhiên bạn có thể tìm thấy cài đặt của nó trong thư viện, dưới dạng hàm `half_gcd`.

Sau khi cài đặt nửa GCD, bạn có thể áp dụng lặp đi lặp lại nó cho các đa thức cho đến khi bài toán được đưa về cặp đa thức $\gcd(a, b)$ và $0$.

## Bài tập luyện tập

- [CodeChef - RNG](https://www.codechef.com/problems/RNG)
- [CodeForces - Basis Change](https://codeforces.com/gym/102129/problem/D)
- [CodeForces - Permutant](https://codeforces.com/gym/102129/problem/G)
- [CodeForces - Medium Hadron Collider](https://codeforces.com/gym/102129/problem/C)
