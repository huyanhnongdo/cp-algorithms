---
tags:
  - Translated
e_maxx_link: discrete_root
---

# Căn rời rạc

Bài toán tìm căn rời rạc được phát biểu như sau. Cho số nguyên tố $n$ và hai số nguyên $a$ và $k$, tìm tất cả các số $x$ sao cho:

$x^k \equiv a \pmod n$

## Thuật toán

Chúng ta sẽ giải bài toán này bằng cách đưa nó về [bài toán logarit rời rạc](discrete-log.md).

Hãy áp dụng khái niệm [căn nguyên thủy](primitive-root.md) mô-đun $n$. Gọi $g$ là một căn nguyên thủy mô-đun $n$. Lưu ý rằng vì $n$ là số nguyên tố, căn nguyên thủy này chắc chắn tồn tại và có thể được tìm thấy trong thời gian $O(Ans \cdot \log \phi (n) \cdot \log n) = O(Ans \cdot \log^2 n)$ cộng với thời gian phân tích thừa số nguyên tố $\phi (n)$.

Chúng ta có thể dễ dàng loại bỏ trường hợp $a = 0$. Trong trường hợp này, rõ ràng chỉ có một nghiệm duy nhất: $x = 0$.

Vì biết $n$ là số nguyên tố nên bất kỳ số nào từ 1 đến $n-1$ đều có thể biểu diễn dưới dạng lũy thừa của căn nguyên thủy, ta có thể biểu diễn bài toán căn rời rạc như sau:

$(g^y)^k \equiv a \pmod n$

trong đó

$x \equiv g^y \pmod n$

Phương trình trên có thể được viết lại thành

$(g^k)^y \equiv a \pmod n$

Bây giờ chúng ta chỉ còn một ẩn chưa biết là $y$, đây chính là bài toán logarit rời rạc. Nghiệm có thể được tìm thấy bằng cách sử dụng thuật toán baby-step giant-step của Shanks trong thời gian $O(\sqrt {n} \log n)$ (hoặc ta có thể xác định được rằng phương trình vô nghiệm).

Sau khi tìm thấy một nghiệm $y_0$, một nghiệm của bài toán căn rời rạc sẽ là $x_0 = g^{y_0} \pmod n$.

## Tìm tất cả các nghiệm từ một nghiệm đã biết

Để giải quyết trọn vẹn bài toán đã cho, chúng ta cần tìm tất cả các nghiệm khi biết một nghiệm của chúng: $x_0 = g^{y_0} \pmod n$.

Hãy nhớ lại tính chất rằng căn nguyên thủy luôn có bậc (order) là $\phi (n)$, tức là số mũ nhỏ nhất $g$ để cho kết quả đồng dư với 1 là $\phi (n)$. Do đó, nếu ta cộng thêm số hạng $\phi (n)$ vào số mũ, giá trị nhận được vẫn không đổi:

$x^k \equiv g^{ y_0 \cdot k + l \cdot \phi (n)} \equiv a \pmod n \forall l \in Z$

Vì vậy, tất cả các nghiệm đều có dạng:

$x = g^{y_0 + \frac {l \cdot \phi (n)}{k}} \pmod n \forall l \in Z$.

trong đó $l$ được chọn sao cho phân số phải là một số nguyên. Để điều này xảy ra, tử số phải chia hết cho bội chung nhỏ nhất (LCM) của $\phi (n)$ và $k$. Nhớ lại rằng bội chung nhỏ nhất của hai số $lcm(a, b) = \frac{a \cdot b}{gcd(a, b)}$; ta thu được:

$x = g^{y_0 + i \frac {\phi (n)}{gcd(k, \phi (n))}} \pmod n \forall i \in Z$.

Đây là công thức cuối cùng cho tất cả các nghiệm của bài toán căn rời rạc.

## Cài đặt

Dưới đây là cài đặt đầy đủ, bao gồm các thủ tục tìm căn nguyên thủy, logarit rời rạc cũng như tìm và in ra tất cả các nghiệm.

```cpp
int gcd(int a, int b) {
	return a ? gcd(b % a, a) : b;
}
 
int powmod(int a, int b, int p) {
	int res = 1;
	while (b > 0) {
		if (b & 1) {
			res = res * a % p;
		}
		a = a * a % p;
		b >>= 1;
	}
	return res;
}
 
// Finds the primitive root modulo p
int generator(int p) {
	vector<int> fact;
	int phi = p-1, n = phi;
	for (int i = 2; i * i <= n; ++i) {
		if (n % i == 0) {
			fact.push_back(i);
			while (n % i == 0)
				n /= i;
		}
	}
	if (n > 1)
		fact.push_back(n);
 
	for (int res = 2; res <= p; ++res) {
		bool ok = true;
		for (int factor : fact) {
			if (powmod(res, phi / factor, p) == 1) {
				ok = false;
				break;
			}
		}
		if (ok) return res;
	}
	return -1;
}
 
// This program finds all numbers x such that x^k = a (mod n)
int main() {
	int n, k, a;
	scanf("%d %d %d", &n, &k, &a);
	if (a == 0) {
		puts("1\n0");
		return 0;
	}
 
	int g = generator(n);
 
	// Baby-step giant-step discrete logarithm algorithm
	int sq = (int) sqrt (n + .0) + 1;
	vector<pair<int, int>> dec(sq);
	for (int i = 1; i <= sq; ++i)
		dec[i-1] = {powmod(g, i * sq * k % (n - 1), n), i};
	sort(dec.begin(), dec.end());
	int any_ans = -1;
	for (int i = 0; i < sq; ++i) {
		int my = powmod(g, i * k % (n - 1), n) * a % n;
		auto it = lower_bound(dec.begin(), dec.end(), make_pair(my, 0));
		if (it != dec.end() && it->first == my) {
			any_ans = it->second * sq - i;
			break;
		}
	}
	if (any_ans == -1) {
		puts("0");
		return 0;
	}
 
	// Print all possible answers
	int delta = (n-1) / gcd(k, n-1);
	vector<int> ans;
	for (int cur = any_ans % delta; cur < n-1; cur += delta)
		ans.push_back(powmod(g, cur, n));
	sort(ans.begin(), ans.end());
	printf("%d\n", ans.size());
	for (int answer : ans)
		printf("%d ", answer);
}
```

## Bài tập luyện tập

* [Codeforces - Lunar New Year and a Recursive Sequence](https://codeforces.com/contest/1106/problem/F)
