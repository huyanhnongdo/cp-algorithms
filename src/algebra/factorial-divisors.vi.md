---
tags:
  - Translated
e_maxx_link: factorial_divisors
---

# Tìm số mũ của ước số giai thừa

Cho hai số nguyên $n$ và $k$. Tìm số nguyên $x$ lớn nhất sao cho $k^x$ chia hết cho $n!$.

## Trường hợp $k$ là số nguyên tố {data-toc-label="k là số nguyên tố"}

Trước tiên, hãy xem xét trường hợp $k$ là số nguyên tố. Khai triển tường minh của giai thừa:

$$n! = 1 \cdot 2 \cdot 3 \ldots (n-1) \cdot n$$

Lưu ý rằng mỗi phần tử thứ $k$ của tích này chia hết cho $k$, nghĩa là nó đóng góp $+1$ vào câu trả lời; số lượng các phần tử như vậy là $\Bigl\lfloor\dfrac{n}{k}\Bigr\rfloor$.

Tiếp theo, mỗi phần tử thứ $k^2$ chia hết cho $k^2$, đóng góp thêm $+1$ vào câu trả lời (lũy thừa đầu tiên của $k$ đã được đếm ở bước trên). Số lượng các phần tử như vậy là $\Bigl\lfloor\dfrac{n}{k^2}\Bigr\rfloor$.

Tương tự, với mỗi $i$, mỗi phần tử thứ $k^i$ đóng góp thêm $+1$ vào câu trả lời, và có $\Bigl\lfloor\dfrac{n}{k^i}\Bigr\rfloor$ phần tử như vậy.

Kết quả cuối cùng là:

$$\Bigl\lfloor\dfrac{n}{k}\Bigr\rfloor + \Bigl\lfloor\dfrac{n}{k^2}\Bigr\rfloor + \ldots + \Bigl\lfloor\dfrac{n}{k^i}\Bigr\rfloor + \ldots$$

Kết quả này còn được gọi là [Công thức Legendre (Legendre's formula)](https://en.wikipedia.org/wiki/Legendre%27s_formula).
Tổng này là hữu hạn, vì chỉ có khoảng $\log_k n$ phần tử đầu tiên là khác không. Do đó, thời gian chạy của thuật toán này là $O(\log_k n)$.

### Cài đặt

```cpp

int fact_pow (int n, int k) {
	int res = 0;
	while (n) {
		n /= k;
		res += n;
	}
	return res;
}

```

## Trường hợp $k$ là hợp số {data-toc-label="k là hợp số"}

Chúng ta không thể áp dụng trực tiếp ý tưởng trên. Thay vào đó, chúng ta có thể phân tích $k$ thành thừa số nguyên tố: $k = k_1^{p_1} \cdot \ldots \cdot k_m^{p_m}$. Với mỗi $k_i$, chúng ta tìm số lần nó xuất hiện trong $n!$ bằng thuật toán được mô tả ở trên — gọi giá trị này là $a_i$. Kết quả cho trường hợp $k$ là hợp số sẽ là:

$$\min_ {i=1 \ldots m} \dfrac{a_i}{p_i}$$
