---
tags:
  - Translated
e_maxx_link: primitive_root
---

# Căn nguyên thủy

## Định nghĩa

Trong số học mô-đun, một số $g$ được gọi là `căn nguyên thủy mô-đun n` (primitive root modulo n) nếu mọi số nguyên tố cùng nhau với $n$ đều đồng dư với một lũy thừa của $g$ theo mô-đun $n$. Dưới góc độ toán học, $g$ là một `căn nguyên thủy mô-đun n` khi và chỉ khi với mọi số nguyên $a$ thỏa mãn $\gcd(a, n) = 1$, tồn tại một số nguyên $k$ sao cho:

$g^k \equiv a \pmod n$.

Khi đó $k$ được gọi là `chỉ số` (index) hoặc `logarit rời rạc` (discrete logarithm) của $a$ cơ số $g$ theo mô-đun $n$. $g$ cũng được gọi là `phần tử sinh` (generator) của nhóm nhân các số nguyên modulo $n$.

Đặc biệt, trong trường hợp $n$ là một số nguyên tố, các lũy thừa của căn nguyên thủy sẽ quét qua tất cả các số từ $1$ đến $n-1$.

## Sự tồn tại

Căn nguyên thủy mô-đun $n$ tồn tại khi và chỉ khi:

* $n$ là 1, 2, 4, hoặc
* $n$ là lũy thừa của một số nguyên tố lẻ $(n = p^k)$, hoặc
* $n$ là hai lần lũy thừa của một số nguyên tố lẻ $(n = 2 \cdot p^k)$.

Định lý này đã được chứng minh bởi Gauss vào năm 1801.

## Mối liên hệ với hàm Euler

Gọi $g$ là một căn nguyên thủy mô-đun $n$. Khi đó chúng ta có thể chứng minh rằng số $k$ nhỏ nhất thỏa mãn $g^k \equiv 1 \pmod n$ là bằng $\phi (n)$. Hơn nữa, điều ngược lại cũng đúng, và tính chất này sẽ được sử dụng trong bài viết này để tìm một căn nguyên thủy.

Ngoài ra, số lượng các căn nguyên thủy mô-đun $n$ (nếu có) bằng $\phi (\phi (n) )$.

## Thuật toán tìm căn nguyên thủy

Một thuật toán thô sơ là duyệt qua tất cả các số trong khoảng $[1, n-1]$. Và kiểm tra xem mỗi số có phải là một căn nguyên thủy hay không bằng cách tính tất cả các lũy thừa của nó để xem chúng có khác nhau đôi một hay không. Thuật toán này có độ phức tạp là $O(g \cdot n)$, quá chậm để áp dụng trong thực tế. Trong phần này, chúng tôi đề xuất một thuật toán nhanh hơn sử dụng một số định lý nổi tiếng.

Từ phần trước, chúng ta biết rằng nếu số $k$ nhỏ nhất thỏa mãn $g^k \equiv 1 \pmod n$ là $\phi (n)$, thì $g$ là một căn nguyên thủy. Vì với bất kỳ số $a$ nào nguyên tố cùng nhau với $n$, chúng ta biết từ định lý Euler rằng $a ^ { \phi (n) } \equiv 1 \pmod n$, nên để kiểm tra xem $g$ có phải là căn nguyên thủy hay không, ta chỉ cần kiểm tra xem với mọi $d$ nhỏ hơn $\phi (n)$, $g^d \not \equiv 1 \pmod n$. Tuy nhiên, thuật toán này vẫn còn quá chậm.

Từ định lý Lagrange, chúng ta biết rằng bậc của 1 của bất kỳ số nào theo mô-đun $n$ phải là một ước của $\phi (n)$. Do đó, chỉ cần kiểm tra với mọi ước thực sự $d \mid \phi (n)$ sao cho $g^d \not \equiv 1 \pmod n$. Đây đã là một thuật toán nhanh hơn nhiều, nhưng chúng ta vẫn có thể cải tiến tốt hơn nữa.

Phân tích thừa số nguyên tố $\phi (n) = p_1 ^ {a_1} \cdots p_s ^ {a_s}$. Chúng ta chứng minh rằng trong thuật toán trước đó, chỉ cần xem xét các giá trị của $d$ có dạng $\frac { \phi (n) } {p_j}$. Thật vậy, gọi $d$ là một ước thực sự bất kỳ của $\phi (n)$. Khi đó, rõ ràng tồn tại chỉ số $j$ sao cho $d \mid \frac { \phi (n) } {p_j}$, tức là $d \cdot k = \frac { \phi (n) } {p_j}$. Tuy nhiên, nếu $g^d \equiv 1 \pmod n$, chúng ta sẽ thu được:

$g ^ { \frac { \phi (n)} {p_j} } \equiv g ^ {d \cdot k} \equiv (g^d) ^k \equiv 1^k \equiv 1 \pmod n$.

tức là trong số các số có dạng $\frac {\phi (n)} {p_i}$, sẽ có ít nhất một số mà tại đó điều kiện không được thỏa mãn.

Bây giờ chúng ta có thuật toán hoàn chỉnh để tìm căn nguyên thủy:

* Đầu tiên, tìm $\phi (n)$ và phân tích thừa số nguyên tố của nó.
* Sau đó duyệt qua tất cả các số $g \in [1, n]$, và với mỗi số, để kiểm tra xem nó có phải là căn nguyên thủy hay không, chúng ta thực hiện như sau:

    * Tính tất cả các giá trị $g ^ { \frac {\phi (n)} {p_i}} \pmod n$.
    * Nếu tất cả các giá trị tính được đều khác $1$, thì $g$ là một căn nguyên thủy.

    Thời gian chạy của thuật toán này là $O(Ans \cdot \log \phi (n) \cdot \log n)$ (giả định rằng $\phi (n)$ có $\log \phi (n)$ ước số).

Shoup (1990, 1992) đã chứng minh rằng, với giả thiết Riemann tổng quát (generalized Riemann hypothesis) được thỏa mãn, thì $g$ có độ lớn $O(\log^6 p)$.

## Cài đặt

Đoạn mã sau giả định rằng mô-đun `p` là một số nguyên tố. Để đoạn mã hoạt động với mọi giá trị của `p`, chúng ta phải bổ sung thêm phần tính $\phi (p)$.

```cpp
int powmod (int a, int b, int p) {
	int res = 1;
	while (b)
		if (b & 1)
			res = int (res * 1ll * a % p),  --b;
		else
			a = int (a * 1ll * a % p),  b >>= 1;
	return res;
}
 
int generator (int p) {
	vector<int> fact;
	int phi = p-1,  n = phi;
	for (int i=2; i*i<=n; ++i)
		if (n % i == 0) {
			fact.push_back (i);
			while (n % i == 0)
				n /= i;
		}
	if (n > 1)
		fact.push_back (n);
 
	for (int res=2; res<=p; ++res) {
		bool ok = true;
		for (size_t i=0; i<fact.size() && ok; ++i)
			ok &= powmod (res, phi / fact[i], p) != 1;
		if (ok)  return res;
	}
	return -1;
}
```
