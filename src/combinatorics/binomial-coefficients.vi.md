---
tags:
  - Translated
e_maxx_link: binomial_coeff
lang: vi
---

# Hệ số nhị thức (Binomial Coefficients)

Hệ số nhị thức $\binom n k$ là số cách để chọn ra một tập hợp gồm $k$ phần tử từ $n$ phần tử khác nhau mà không quan tâm đến thứ tự sắp xếp của các phần tử này (tức là số lượng tập hợp không có thứ tự).

Hệ số nhị thức cũng chính là các hệ số xuất hiện trong khai triển của biểu thức $(a + b) ^ n$ (được gọi là định lý nhị thức - binomial theorem):

$$ (a+b)^n = \binom n 0 a^n + \binom n 1 a^{n-1} b + \binom n 2 a^{n-2} b^2 + \cdots + \binom n k a^{n-k} b^k + \cdots + \binom n n b^n $$

Người ta tin rằng công thức này, cũng như hình tam giác giúp tính toán nhanh các hệ số, đã được Blaise Pascal phát hiện ra vào thế kỷ 17. Tuy nhiên, nó cũng đã được biết đến trước đó bởi nhà toán học Trung Quốc Dương Huy (Yang Hui), sống vào thế kỷ 13. Có lẽ nó cũng đã được phát hiện bởi học giả người Ba Tư Omar Khayyam. Hơn nữa, nhà toán học Ấn Độ Pingala, sống từ thế kỷ thứ 3 trước Công nguyên, đã thu được các kết quả tương tự. Công lao của Newton là ông đã tổng quát hóa công thức này cho các số mũ không phải là số tự nhiên.

## Tính toán

**Công thức giải tích** để tính toán:

$$ \binom n k = \frac {n!} {k!(n-k)!} $$

Công thức này có thể dễ dàng suy ra từ bài toán chỉnh hợp (số cách chọn ra $k$ phần tử khác nhau có thứ tự từ $n$ phần tử khác nhau). Đầu tiên, hãy đếm số lượng cách chọn có thứ tự $k$ phần tử. Có $n$ cách chọn phần tử đầu tiên, $n-1$ cách chọn phần tử thứ hai, $n-2$ cách chọn phần tử thứ ba, v.v. Kết quả là, chúng ta thu được công thức tính số chỉnh hợp: $n (n-1) (n-2) \cdots (n - k + 1) = \frac {n!} {(n-k)!}$. Chúng ta có thể chuyển sang tổ hợp không có thứ tự bằng cách lưu ý rằng mỗi tổ hợp không thứ tự tương ứng với đúng $k!$ chỉnh hợp có thứ tự ($k!$ là số hoán vị của $k$ phần tử). Chúng ta có công thức cuối cùng bằng cách chia $\frac {n!} {(n-k)!}$ cho $k!$.

**Công thức truy hồi** (gần với "Tam giác Pascal" nổi tiếng):

$$ \binom n k = \binom {n-1} {k-1} + \binom {n-1} k $$

Dễ dàng chứng minh công thức này bằng cách sử dụng công thức giải tích.

Lưu ý rằng với $n \lt k$, giá trị của $\binom n k$ được mặc định bằng không.

## Tính chất

Hệ số nhị thức có nhiều tính chất khác nhau. Dưới đây là những tính chất đơn giản nhất của chúng:

*   Quy tắc đối xứng:

    \[ \binom n k = \binom n {n-k} \]

*   Rút thừa số (hệ thức hấp thụ):

    \[ \binom n k = \frac n k \binom {n-1} {k-1} \]

*   Tổng theo $k$:

    \[ \sum_{k = 0}^n \binom n k = 2 ^ n \]

*   Tổng theo $n$:

    \[ \sum_{m = 0}^n \binom m k = \binom {n + 1} {k + 1} \]

*   Tổng theo $n$ và $k$:

    \[ \sum_{k = 0}^m  \binom {n + k} k = \binom {n + m + 1} m \]

*   Tổng các bình phương:

    \[ {\binom n 0}^2 + {\binom n 1}^2 + \cdots + {\binom n n}^2 = \binom {2n} n \]

*   Tổng có trọng số:

    \[ 1 \binom n 1 + 2 \binom n 2 + \cdots + n \binom n n = n 2^{n-1} \]

*   Mối liên hệ với [Số Fibonacci](../algebra/fibonacci-numbers.md):

    \[ \binom n 0 + \binom {n-1} 1 + \cdots + \binom {n-k} k + \cdots + \binom 0 n = F_{n+1} \]

## Tính toán

### Tính toán trực tiếp bằng công thức giải tích

Công thức đầu tiên rất dễ lập trình, nhưng phương pháp này dễ dẫn đến tràn số ngay cả với các giá trị $n$ và $k$ tương đối nhỏ (ngay cả khi kết quả cuối cùng hoàn toàn nằm trong giới hạn của kiểu dữ liệu, các giá trị giai thừa trung gian vẫn có thể gây tràn số). Do đó, phương pháp này thường chỉ có thể được sử dụng kết hợp với [số học số lớn](../algebra/big-integer.md):

```cpp
int C(int n, int k) {
    int res = 1;
    for (int i = n - k + 1; i <= n; ++i)
        res *= i;
    for (int i = 2; i <= k; ++i)
        res /= i;
    return res;
}
```

### Cài đặt cải tiến

Lưu ý rằng trong cách cài đặt trên, tử số và mẫu số có cùng số lượng thừa số ($k$), và mỗi thừa số đều lớn hơn hoặc bằng 1. Vì vậy, chúng ta có thể thay thế phân số của mình bằng tích của $k$ phân số số thực. Tuy nhiên, ở mỗi bước sau khi nhân đáp án hiện tại với phân số tiếp theo, kết quả vẫn sẽ luôn là số nguyên (điều này suy ra từ tính chất rút thừa số).

Cài đặt C++:

```cpp
int C(int n, int k) {
    double res = 1;
    for (int i = 1; i <= k; ++i)
        res = res * (n - k + i) / i;
    return (int)(res + 0.01);
}
```

Ở đây chúng ta cần ép kiểu số thực sang số nguyên một cách cẩn thận, có tính đến việc sai số tích lũy có thể làm cho giá trị thực tế nhỏ hơn một chút so với giá trị đúng (ví dụ: $2.99999$ thay vì $3$).

### Tam giác Pascal

Bằng cách sử dụng hệ thức truy hồi, chúng ta có thể dựng bảng các hệ số nhị thức (Tam giác Pascal) và lấy kết quả trực tiếp từ bảng đó. Ưu điểm của phương pháp này là các kết quả trung gian không bao giờ vượt quá đáp án cuối cùng, và việc tính toán mỗi phần tử mới chỉ yêu cầu duy nhất một phép cộng. Nhược điểm của nó là tốc độ thực hiện chậm đối với các giá trị $n$ và $k$ lớn nếu bạn chỉ cần một giá trị đơn lẻ chứ không cần cả bảng (vì để tính $\binom n k$ bạn sẽ phải dựng toàn bộ bảng cho $\binom i j, 1 \le i \le n, 1 \le j \le n$, hoặc ít nhất là đến $1 \le j \le \min (i, 2k)$). Độ phức tạp thời gian có thể được coi là $\mathcal{O}(n^2)$.

Cài đặt C++:

```cpp
const int maxn = ...;
int C[maxn + 1][maxn + 1];
C[0][0] = 1;
for (int n = 1; n <= maxn; ++n) {
    C[n][0] = C[n][n] = 1;
    for (int k = 1; k < n; ++k)
        C[n][k] = C[n - 1][k - 1] + C[n - 1][k];
}
```

Nếu không cần thiết phải lưu giữ toàn bộ bảng giá trị, bạn chỉ cần lưu trữ hai dòng cuối cùng của bảng (dòng hiện tại thứ $n$ và dòng trước đó thứ $n-1$).

### Tính toán trong $O(1)$ {data-toc-label="Tính toán trong O(1)"}

Cuối cùng, trong một số tình huống, việc tiền xử lý tất cả các giai thừa là rất hữu ích để có thể tính bất kỳ hệ số nhị thức nào sau đó chỉ với hai phép chia. Cách này đặc biệt có lợi khi kết hợp với [số học số lớn](../algebra/big-integer.md), khi mà bộ nhớ không cho phép lưu trữ toàn bộ Tam giác Pascal.

## Tính hệ số nhị thức modulo $m$ {data-toc-label="Tính hệ số nhị thức modulo m"}

Chúng ta rất thường xuyên bắt gặp bài toán tính hệ số nhị thức modulo một số $m$ nào đó.

### Hệ số nhị thức với $n$ nhỏ {data-toc-label="Hệ số nhị thức với n nhỏ"}

Cách tiếp cận sử dụng Tam giác Pascal đã thảo luận trước đó có thể dùng để tính tất cả các giá trị $\binom{n}{k} \bmod m$ cho các giá trị $n$ nhỏ hợp lý, vì nó có độ phức tạp thời gian là $\mathcal{O}(n^2)$. Cách tiếp cận này có thể xử lý với bất kỳ modulo nào vì chỉ sử dụng các phép cộng.

### Hệ số nhị thức modulo một số nguyên tố lớn

Công thức tính hệ số nhị thức là:

$$\binom n k = \frac {n!} {k!(n-k)!},$$

nên nếu chúng ta muốn tính giá trị này modulo một số nguyên tố $m > n$, ta có:

$$\binom n k \equiv n! \cdot (k!)^{-1} \cdot ((n-k)!)^{-1} \mod m.$$

Đầu tiên chúng ta tính trước tất cả các giai thừa modulo $m$ lên tới $\text{MAXN}!$ trong thời gian $O(\text{MAXN})$.

```cpp
factorial[0] = 1;
for (int i = 1; i <= MAXN; i++) {
    factorial[i] = factorial[i - 1] * i % m;
}
```

Và sau đó, chúng ta có thể tính hệ số nhị thức trong thời gian $O(\log m)$.

```cpp
long long binomial_coefficient(int n, int k) {
    return factorial[n] * inverse(factorial[k] * factorial[n - k] % m) % m;
}
```

Chúng ta thậm chí có thể tính hệ số nhị thức trong thời gian $O(1)$ nếu tiền xử lý các nghịch đảo của giai thừa trong $O(\text{MAXN} \log m)$ bằng phương pháp thông thường, hoặc thậm chí trong $O(\text{MAXN})$ sử dụng đồng dư $(x!)^{-1} \equiv ((x-1)!)^{-1} \cdot x^{-1}$ và phương pháp [tính tất cả các nghịch đảo](../algebra/module-inverse.md#mod-inv-all-num) trong $O(n)$.

```cpp
long long binomial_coefficient(int n, int k) {
    return factorial[n] * inverse_factorial[k] % m * inverse_factorial[n - k] % m;
}
```

### Hệ số nhị thức modulo lũy thừa số nguyên tố { #mod-prime-pow}

Ở đây chúng ta muốn tính hệ số nhị thức modulo một lũy thừa số nguyên tố, tức là $m = p^b$ với số nguyên tố $p$.
Nếu $p > \max(k, n-k)$, chúng ta có thể áp dụng trực tiếp phương pháp ở phần trước.
Nhưng nếu $p \le \max(k, n-k)$, thì ít nhất một trong hai giá trị $k!$ và $(n-k)!$ sẽ không nguyên tố cùng nhau với $m$, do đó chúng ta không thể tính nghịch đảo modular — chúng không tồn tại.
Tuy nhiên, chúng ta vẫn có thể tính được hệ số nhị thức.

Ý tưởng như sau:
Với mỗi $x!$, chúng ta tìm lũy thừa $c$ lớn nhất sao cho $p^c$ chia hết cho $x!$, tức là $p^c ~|~ x!$.
Gọi $c(x)$ là số đó.
Và định nghĩa $g(x) := \frac{x!}{p^{c(x)}}$.
Khi đó chúng ta có thể viết hệ số nhị thức dưới dạng:

$$\binom n k = \frac {g(n) p^{c(n)}} {g(k) p^{c(k)} g(n-k) p^{c(n-k)}} = \frac {g(n)} {g(k) g(n-k)}p^{c(n) - c(k) - c(n-k)}$$

Điều thú vị là giá trị $g(x)$ bây giờ hoàn toàn không còn chứa ước nguyên tố $p$ nữa.
Do đó $g(x)$ nguyên tố cùng nhau với $m$, và chúng ta có thể tính nghịch đảo modular của $g(k)$ và $g(n-k)$.

Sau khi tiền xử lý tất cả các giá trị của $g$ và $c$ bằng quy hoạch động trong thời gian $\mathcal{O}(n)$, chúng ta có thể tính hệ số nhị thức trong thời gian $O(\log m)$.
Hoặc tiền xử lý tất cả các nghịch đảo và tất cả các lũy thừa của $p$, để tính hệ số nhị thức trong thời gian $O(1)$.

Lưu ý rằng nếu $c(n) - c(k) - c(n-k) \ge b$, thì $p^b ~|~ p^{c(n) - c(k) - c(n-k)}$, và hệ số nhị thức sẽ bằng $0$ modulo $m$.

### Hệ số nhị thức modulo một số bất kỳ

Bây giờ chúng ta tính hệ số nhị thức modulo một số $m$ bất kỳ.

Phân tích thừa số nguyên tố của $m$ là $m = p_1^{e_1} p_2^{e_2} \cdots p_h^{e_h}$.
Chúng ta có thể tính hệ số nhị thức modulo $p_i^{e_i}$ cho mỗi $i$.
Việc này cho chúng ta $h$ hệ phương trình đồng dư khác nhau.
Vì tất cả các cơ số $p_i^{e_i}$ nguyên tố cùng nhau từng đôi một, chúng ta có thể áp dụng [Định lý thặng dư Trung Hoa](../algebra/chinese-remainder-theorem.md) để tính hệ số nhị thức modulo tích các cơ số đó, chính là hệ số nhị thức modulo $m$ cần tìm.

### Hệ số nhị thức với $n$ lớn và modulo nhỏ {data-toc-label="Hệ số nhị thức với n lớn và modulo nhỏ"}

Khi $n$ quá lớn, các thuật toán $\mathcal{O}(n)$ thảo luận ở trên không thể áp dụng được nữa. Tuy nhiên, nếu modulo $m$ nhỏ, chúng ta vẫn có cách để tính $\binom{n}{k} \bmod m$.

Khi modulo $m$ là số nguyên tố, có 2 lựa chọn:

* Áp dụng [Định lý Lucas (Lucas's theorem)](https://en.wikipedia.org/wiki/Lucas's_theorem) để phân tách bài toán tính $\binom{n}{k} \bmod m$ thành $\log_m n$ bài toán nhỏ có dạng $\binom{x_i}{y_i} \bmod m$ với $x_i, y_i < m$. Nếu mỗi hệ số nhị thức nhỏ được tính bằng cách sử dụng các giai thừa và nghịch đảo giai thừa được tiền xử lý trước, độ phức tạp là $\mathcal{O}(m + \log_m n)$.
* Sử dụng phương pháp tính [giai thừa modulo P](../algebra/factorial-modulo.md) để tìm các giá trị $g$ và $c$ cần thiết, rồi tính như mô tả ở phần [modulo lũy thừa số nguyên tố](#mod-prime-pow). Cách này tốn thời gian $\mathcal{O}(m \log_m n)$.

Khi $m$ không phải là số nguyên tố nhưng là tích của các số nguyên tố phân biệt (square-free), các ước nguyên tố của $m$ có thể được tìm thấy và tính hệ số nhị thức modulo từng ước nguyên tố bằng một trong hai phương pháp trên, sau đó dùng Định lý thặng dư Trung Hoa để có câu trả lời cuối cùng.

Khi $m$ chứa ước chính phương (không phải square-free), chúng ta có thể áp dụng một bản [tổng quát hóa định lý Lucas cho lũy thừa số nguyên tố](https://web.archive.org/web/20170202003812/http://www.dms.umontreal.ca/~andrew/PDF/BinCoeff.pdf) thay cho định lý Lucas thông thường.

## Bài tập thực hành
* [Codechef - Number of ways](https://www.codechef.com/LTIME24/problems/NWAYS/)
* [Codeforces - Curious Array](http://codeforces.com/problemset/problem/407/C)
* [LightOj - Necklaces](http://www.lightoj.com/volume_showproblem.php?problem=1419)
* [HACKEREARTH: Binomial Coefficient](https://www.hackerearth.com/problem/algorithm/binomial-coefficient-1/description/)
* [SPOJ - Ada and Teams](http://www.spoj.com/problems/ADATEAMS/)
* [SPOJ - Greedy Walking](http://www.spoj.com/problems/UCV2013E/)
* [UVa 13214 - The Robot's Grid](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=5137)
* [SPOJ - Good Predictions](http://www.spoj.com/problems/GOODB/)
* [SPOJ - Card Game](http://www.spoj.com/problems/HC12/)
* [SPOJ - Topper Rama Rao](http://www.spoj.com/problems/HLP_RAMS/)
* [UVa 13184 - Counting Edges and Graphs](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=5095)
* [Codeforces - Anton and School 2](http://codeforces.com/contest/785/problem/D)
* [Codeforces - Bacterial Melee](http://codeforces.com/contest/760/problem/F)
* [Codeforces - Points, Lines and Ready-made Titles](http://codeforces.com/contest/872/problem/E)
* [SPOJ - The Ultimate Riddle](https://www.spoj.com/problems/DCEPC13D/)
* [CodeChef - Long Sandwich](https://www.codechef.com/MAY17/problems/SANDWICH/)
* [Codeforces - Placing Jinas](https://codeforces.com/problemset/problem/1696/E)

## Tài liệu tham khảo
* [Blog fishi.devtail.io](https://fishi.devtail.io/weblog/2015/06/25/computing-large-binomial-coefficients-modulo-prime-non-prime/)
* [Question on Mathematics StackExchange](https://math.stackexchange.com/questions/95491/n-choose-k-bmod-m-using-chinese-remainder-theorem)
* [Question on CodeChef Discuss](https://discuss.codechef.com/questions/98129/your-approach-to-solve-sandwich)
