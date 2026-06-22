---
tags:
  - Translated
e_maxx_link: reverse_element
lang: vi
---

# Nghịch đảo modular (Modular Multiplicative Inverse)

## Định nghĩa

Một **nghịch đảo modular (modular multiplicative inverse)** của số nguyên $a$ là một số nguyên $x$ sao cho $a \cdot x$ đồng dư với $1$ theo một modulo $m$ nào đó.
Viết một cách chính thức: chúng ta muốn tìm một số nguyên $x$ thỏa mãn:

$$a \cdot x \equiv 1 \mod m.$$

Chúng ta cũng sẽ ký hiệu $x$ đơn giản là $a^{-1}$.

Cần lưu ý rằng nghịch đảo modular không phải lúc nào cũng tồn tại. Ví dụ, cho $m = 4$, $a = 2$.
Bằng cách kiểm tra tất cả các giá trị đồng dư có thể theo modulo $m$, rõ ràng chúng ta không thể tìm thấy bất kỳ $a^{-1}$ nào thỏa mãn phương trình trên.
Có thể chứng minh được rằng nghịch đảo modular tồn tại nếu và chỉ nếu $a$ và $m$ nguyên tố cùng nhau (tức là $\gcd(a, m) = 1$).

Trong bài viết này, chúng ta sẽ giới thiệu hai phương pháp tìm nghịch đảo modular trong trường hợp nó tồn tại, và một phương pháp tìm nghịch đảo modular cho tất cả các số trong thời gian tuyến tính.

## Tìm nghịch đảo modular bằng Thuật toán Euclid mở rộng

Xét phương trình sau (với các ẩn số $x$ và $y$):

$$a \cdot x + m \cdot y = 1$$

Đây là một [Phương trình Diophantine tuyến tính hai ẩn](linear-diophantine-equation.md).
Như đã trình bày trong bài viết liên quan, khi $\gcd(a, m) = 1$, phương trình có nghiệm và có thể tìm thấy bằng cách sử dụng [Thuật toán Euclid mở rộng](extended-euclid-algorithm.md).
Lưu ý rằng $\gcd(a, m) = 1$ cũng chính là điều kiện để nghịch đảo modular tồn tại.

Bây giờ, nếu lấy modulo $m$ cả hai vế, chúng ta có thể loại bỏ số hạng $m \cdot y$, và phương trình trở thành:

$$a \cdot x \equiv 1 \mod m$$

Do đó, nghịch đảo modular của $a$ chính là $x$.

Mã nguồn cài đặt như sau:

```cpp
int x, y;
int g = extended_euclidean(a, m, x, y);
if (g != 1) {
    cout << "No solution!";
}
else {
    x = (x % m + m) % m;
    cout << x << endl;
}
```

Hãy chú ý cách chúng ta hiệu chỉnh biến `x`.
Giá trị `x` thu được từ thuật toán Euclid mở rộng có thể âm, nên phép toán `x % m` cũng có thể cho kết quả âm, do đó chúng ta phải cộng thêm `m` trước để đưa nó về giá trị dương.

<div id="fermat-euler"></div>
## Tìm nghịch đảo modular bằng Lũy thừa nhị phân

Một phương pháp khác để tìm nghịch đảo modular là sử dụng Định lý Euler (Euler's theorem). Định lý này phát biểu rằng đồng dư thức sau luôn đúng nếu $a$ và $m$ nguyên tố cùng nhau:

$$a^{\phi (m)} \equiv 1 \mod m$$

Trong đó $\phi$ là [Hàm phi Euler (Euler's Totient function)](phi-function.md).
Một lần nữa, lưu ý rằng việc $a$ và $m$ nguyên tố cùng nhau cũng là điều kiện cần và đủ để nghịch đảo modular tồn tại.

Nếu $m$ là số nguyên tố, định lý này thu hẹp về [Định lý nhỏ Fermat (Fermat's little theorem)](http://en.wikipedia.org/wiki/Fermat's_little_theorem):

$$a^{m - 1} \equiv 1 \mod m$$

Nhân cả hai vế của các phương trình trên với $a^{-1}$, ta thu được:

* Với một modulo $m$ bất kỳ (nhưng nguyên tố cùng nhau với $a$): $a ^ {\phi (m) - 1} \equiv a ^{-1} \mod m$
* Với một modulo $m$ là số nguyên tố: $a ^ {m - 2} \equiv a ^ {-1} \mod m$

Từ kết quả này, chúng ta có thể dễ dàng tìm thấy nghịch đảo modular bằng [Thuật toán lũy thừa nhị phân (Binary Exponentiation)](binary-exp.md), chạy trong thời gian $O(\log m)$.

Mặc dù phương pháp này dễ hiểu hơn phương pháp sử dụng thuật toán Euclid mở rộng ở phần trước, nhưng trong trường hợp $m$ không phải là số nguyên tố, chúng ta cần phải tính toán hàm phi Euler. Phép tính này đòi hỏi phải phân tích thừa số nguyên tố của $m$, một bài toán có thể rất khó. Nếu đã biết trước phân tích thừa số nguyên tố của $m$, độ phức tạp của phương pháp này sẽ là $O(\log m)$.

<div id="finding-the-modular-inverse-using-euclidean-division"></div>
## Tìm nghịch đảo modular với modulo nguyên tố sử dụng Phép chia Euclid

Cho trước một modulo nguyên tố $m > a$ (hoặc chúng ta có thể lấy dư trước để đưa nó về khoảng này trong 1 bước), theo [Phép chia Euclid (Euclidean Division)](https://en.wikipedia.org/wiki/Euclidean_division):

$$m = k \cdot a + r$$

trong đó $k = \left\lfloor \frac{m}{a} \right\rfloor$ và $r = m \bmod a$. Khi đó:

$$
\begin{align*}
& \implies & 0          & \equiv k \cdot a + r   & \mod m \\
& \iff & r              & \equiv -k \cdot a      & \mod m \\
& \iff & r \cdot a^{-1} & \equiv -k              & \mod m \\
& \iff & a^{-1}         & \equiv -k \cdot r^{-1} & \mod m
\end{align*}
$$

Lưu ý rằng lập luận này không đúng nếu $m$ không phải là số nguyên tố, bởi sự tồn tại của $a^{-1}$ không đồng nghĩa với việc tồn tại $r^{-1}$ trong trường hợp tổng quát. Để thấy rõ điều này, hãy thử tính $5^{-1}$ modulo $12$ bằng công thức trên. Chúng ta muốn có đáp án là $5$, vì $5 \cdot 5 \equiv 1 \bmod 12$. Tuy nhiên, $12 = 2 \cdot 5 + 2$, ta có $k=2$ và $r=2$, nhưng số $2$ không có nghịch đảo modular theo modulo $12$.

Tuy nhiên, nếu modulus là số nguyên tố, tất cả các số $a$ thỏa mãn $0 < a < m$ đều nghịch đảo được theo modulo $m$. Khi đó, chúng ta có thể viết hàm đệ quy sau (bằng C++) để tính nghịch đảo modular cho số $a$ đối với modulo $m$:

```{.cpp file=modular_inverse_euclidean_division}
int inv(int a) {
  return a <= 1 ? a : m - (long long)(m/a) * inv(m % a) % m;
}
```

Độ phức tạp thời gian chạy chính xác của hàm đệ quy này hiện vẫn chưa được làm rõ hoàn toàn. Nó nằm trong khoảng từ $O(\frac{\log m}{\log\log m})$ đến $O(m^{\frac{1}{3} - \frac{2}{177} + \epsilon})$.
Xem [On the length of Pierce expansions](https://arxiv.org/abs/2211.08374).
Trong thực tế, cách cài đặt này chạy rất nhanh. Ví dụ với modulo $10^9 + 7$, nó sẽ luôn hoàn thành trong ít hơn 50 lần lặp đệ quy.

<div id="mod-inv-all-num"></div>
Áp dụng công thức này, chúng ta cũng có thể tính toán trước (precompute) nghịch đảo modular cho mọi số trong phạm vi $[1, m-1]$ trong thời gian $O(m)$:

```{.cpp file=modular_inverse_euclidean_division_all}
inv[1] = 1;
for(int a = 2; a < m; ++a)
    inv[a] = m - (long long)(m/a) * inv[m%a] % m;
```

## Tìm nghịch đảo modular cho một mảng số theo modulo $m$

Giả sử chúng ta được cho một mảng và muốn tìm nghịch đảo modular cho tất cả các số trong mảng đó (giả định rằng tất cả các phần tử đều có nghịch đảo).
Thay vì tính nghịch đảo độc lập cho từng số, chúng ta có thể nhân cả tử và mẫu của phân số với tích tiền tố (prefix product) (không bao gồm chính nó) và tích hậu tố (suffix product) (không bao gồm chính nó), cuối cùng chỉ cần thực hiện tính một nghịch đảo duy nhất.

$$
\begin{align}
x_i^{-1} &= \frac{1}{x_i} = \frac{\overbrace{x_1 \cdot x_2 \cdots x_{i-1}}^{\text{prefix}_{i-1}} \cdot ~1~ \cdot \overbrace{x_{i+1} \cdot x_{i+2} \cdots x_n}^{\text{suffix}_{i+1}}}{x_1 \cdot x_2 \cdots x_{i-1} \cdot x_i \cdot x_{i+1} \cdot x_{i+2} \cdots x_n} \\
&= \text{prefix}_{i-1} \cdot \text{suffix}_{i+1} \cdot \left(x_1 \cdot x_2 \cdots x_n\right)^{-1}
\end{align}
$$

Trong mã nguồn cài đặt, chúng ta chỉ cần tạo một mảng tích tiền tố (không bao gồm chính phần tử đó, bắt đầu từ phần tử đơn vị), tính nghịch đảo modular cho tích của tất cả các số, và sau đó nhân nó với tích tiền tố và tích hậu tố (không bao gồm chính nó).
Tích hậu tố được tính bằng cách duyệt mảng từ cuối lên đầu.

```cpp
std::vector<int> invs(const std::vector<int> &a, int m) {
    int n = a.size();
    if (n == 0) return {};
    std::vector<int> b(n);
    int v = 1;
    for (int i = 0; i != n; ++i) {
        b[i] = v;
        v = static_cast<long long>(v) * a[i] % m;
    }
    int x, y;
    extended_euclidean(v, m, x, y);
    x = (x % m + m) % m;
    for (int i = n - 1; i >= 0; --i) {
        b[i] = static_cast<long long>(x) * b[i] % m;
        x = static_cast<long long>(x) * a[i] % m;
    }
    return b;
}
```

## Bài tập thực hành

* [UVa 11904 - One Unit Machine](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3055)
* [Hackerrank - Longest Increasing Subsequence Arrays](https://www.hackerrank.com/contests/world-codesprint-5/challenges/longest-increasing-subsequence-arrays)
* [Codeforces 300C - Beautiful Numbers](http://codeforces.com/problemset/problem/300/C)
* [Codeforces 622F - The Sum of the k-th Powers](http://codeforces.com/problemset/problem/622/F)
* [Codeforces 717A - Festival Organization](http://codeforces.com/problemset/problem/717/A)
* [Codeforces 896D - Nephren Runs a Cinema](http://codeforces.com/problemset/problem/896/D)
