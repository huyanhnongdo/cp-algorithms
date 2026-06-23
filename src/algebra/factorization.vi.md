---
tags:
  - Translated
lang: vi
---

# Phân tích thừa số nguyên (Integer factorization)

Trong bài viết này, chúng tôi liệt kê một số thuật toán để phân tích số nguyên thành thừa số nguyên tố. Mỗi thuật toán có thể chạy nhanh hoặc chậm tùy thuộc vào đầu vào của chúng.

Lưu ý rằng nếu số bạn muốn phân tích thực tế là một số nguyên tố, hầu hết các thuật toán dưới đây sẽ chạy rất chậm. Điều này đặc biệt đúng đối với phương pháp Fermat, phương pháp $p - 1$ của Pollard và thuật toán rho của Pollard.
Do đó, điều hợp lý nhất là thực hiện một phép [kiểm tra tính nguyên tố](primality_tests.md) xác suất (hoặc tất định nhanh) trước khi cố gắng phân tích số đó.

## Phép chia thử (Trial division)

Đây là thuật toán cơ bản nhất để tìm phân tích thừa số nguyên tố.

Chúng ta chia thử số $n$ cho từng ước số $d$ có thể.
Dễ nhận thấy rằng một hợp số $n$ không thể có tất cả các ước nguyên tố lớn hơn $\sqrt{n}$.
Do đó, chúng ta chỉ cần kiểm tra các ước số $2 \le d \le \sqrt{n}$, giúp tìm được phân tích thừa số nguyên tố trong thời gian $O(\sqrt{n})$.
(Đây là [thời gian giả đa thức (pseudo-polynomial time)](https://en.wikipedia.org/wiki/Pseudo-polynomial_time), tức là đa thức theo giá trị đầu vào nhưng là lũy thừa theo số lượng bit của đầu vào.)

Ước số nhỏ nhất tìm được chắc chắn phải là một số nguyên tố.
Chúng ta chia bỏ ước số đó khỏi $n$ và tiếp tục quá trình.
Nếu chúng ta không tìm thấy bất kỳ ước số nào trong khoảng $[2; \sqrt{n}]$, thì bản thân số đó phải là số nguyên tố.

```{.cpp file=factorization_trial_division1}
vector<long long> trial_division1(long long n) {
    vector<long long> factorization;
    for (long long d = 2; d * d <= n; d++) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
```

### Phương pháp bánh xe (Wheel factorization)

Đây là một cải tiến của phép chia thử.
Một khi biết số đó không chia hết cho 2, chúng ta không cần kiểm tra các số chẵn khác.
Điều này giúp giảm $50\%$ số lượng số cần kiểm tra.
Sau khi chia hết cho 2 và thu được một số lẻ, chúng ta chỉ cần bắt đầu thử từ 3 và tăng bước nhảy lên 2 (chỉ kiểm tra các số lẻ).

```{.cpp file=factorization_trial_division2}
vector<long long> trial_division2(long long n) {
    vector<long long> factorization;
    while (n % 2 == 0) {
        factorization.push_back(2);
        n /= 2;
    }
    for (long long d = 3; d * d <= n; d += 2) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
```

Phương pháp này có thể được mở rộng hơn nữa.
Nếu số đó không chia hết cho 3, chúng ta cũng có thể bỏ qua tất cả các bội số của 3 trong các phép thử tiếp theo.
Do đó, chúng ta chỉ cần kiểm tra các số $5, 7, 11, 13, 17, 19, 23, \dots$.
Các số này tuân theo một quy luật: chúng là các số có dạng $d \bmod 6 = 1$ hoặc $d \bmod 6 = 5$.
Cách này chỉ cần kiểm tra $33.3\%$ lượng số ban đầu.
Chúng ta có thể cài đặt bằng cách chia sạch các ước số 2 và 3 trước, sau đó bắt đầu từ 5 và chỉ kiểm tra các số dư $1$ và $5$ modulo $6$ (tức là bắt đầu từ 5 và tăng bước nhảy xen kẽ 2 và 4).

Dưới đây là một bản cài đặt mở rộng cho các số nguyên tố 2, 3 và 5.
Chúng ta lưu trữ các khoảng tăng bước nhảy (stride) trong một mảng.

```{.cpp file=factorization_trial_division3}
vector<long long> trial_division3(long long n) {
    vector<long long> factorization;
    for (int d : {2, 3, 5}) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    static array<int, 8> increments = {4, 2, 4, 2, 4, 6, 2, 6};
    int i = 0;
    for (long long d = 7; d * d <= n; d += increments[i++]) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
        if (i == 8)
            i = 0;
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
```

Nếu chúng ta tiếp tục mở rộng phương pháp này cho nhiều số nguyên tố hơn nữa, tỷ lệ số cần kiểm tra sẽ còn giảm nhiều hơn, nhưng kích thước danh sách bước nhảy sẽ lớn lên nhanh chóng.

### Sử dụng danh sách số nguyên tố tính trước

Nếu mở rộng phương pháp bánh xe đến vô hạn, chúng ta sẽ chỉ còn lại các số nguyên tố để kiểm tra.
Một cách tốt là tính trước tất cả các số nguyên tố bằng [sàng Eratosthenes](sieve-of-eratosthenes.md) lên tới $\sqrt{n}$, rồi kiểm tra từng số nguyên tố này.

```{.cpp file=factorization_trial_division4}
vector<long long> primes;

vector<long long> trial_division4(long long n) {
    vector<long long> factorization;
    for (long long d : primes) {
        if (d * d > n)
            break;
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
```

## Phương pháp phân tích Fermat (Fermat's factorization method)

Chúng ta có thể biểu diễn một số hợp số lẻ $n = p \cdot q$ dưới dạng hiệu của hai số chính phương $n = a^2 - b^2$:

$$n = \left(\frac{p + q}{2}\right)^2 - \left(\frac{p - q}{2}\right)^2$$

Phương pháp phân tích Fermat cố gắng khai thác tính chất này bằng cách đoán số chính phương thứ nhất $a^2$, sau đó kiểm tra xem phần còn lại $b^2 = a^2 - n$ có phải là một số chính phương hay không.
Nếu phải, chúng ta đã tìm thấy các ước số là $a - b$ và $a + b$ của $n$.

```cpp
int fermat(int n) {
    int a = ceil(sqrt(n));
    int b2 = a*a - n;
    int b = round(sqrt(b2));
    while (b * b != b2) {
        a = a + 1;
        b2 = a*a - n;
        b = round(sqrt(b2));
    }
    return a - b;
}
```

Phương pháp này chạy rất nhanh nếu hiệu giữa hai ước số $p$ và $q$ nhỏ.
Thuật toán chạy trong thời gian $O(|p - q|)$.
Tuy nhiên, trong thực tế phương pháp này hiếm khi được sử dụng vì nếu hai ước số nằm xa nhau, nó sẽ chạy cực kỳ chậm.

Dù vậy, vẫn có nhiều cách tối ưu hóa cho hướng tiếp cận này.
Bằng cách xem xét các số chính phương $a^2$ mô-đun cho một số nhỏ cố định, chúng ta có thể bỏ qua một số giá trị $a$ không thể tạo ra số chính phương $a^2 - n$.

## Phương pháp $p - 1$ của Pollard (Pollard's $p - 1$ method) { data-toc-label="Pollard's <script type='math/tex'>p - 1</script> method" }

Một số $n$ rất có khả năng có ít nhất một ước nguyên tố $p$ sao cho $p - 1$ là số **trơn lũy thừa $\mathrm{B}$ (B-powersmooth)** với giá trị $\mathrm{B}$ nhỏ. Một số nguyên $m$ được gọi là trơn lũy thừa $\mathrm{B}$ nếu mọi lũy thừa số nguyên tố chia hết $m$ đều không vượt quá $\mathrm{B}$. Định nghĩa chính thức: cho $\mathrm{B} \geqslant 1$ và một số nguyên dương $m$. Giả sử phân tích thừa số nguyên tố của $m$ là $m = \prod {q_i}^{e_i}$, trong đó mỗi $q_i$ là số nguyên tố và $e_i \geqslant 1$. Khi đó $m$ là trơn lũy thừa $\mathrm{B}$ nếu ${q_i}^{e_i} \leqslant \mathrm{B}$ với mọi $i$.

Ví dụ: phân tích thừa số nguyên tố của $4817191$ là $1303 \cdot 3697$.
Các giá trị $1303 - 1$ và $3697 - 1$ tương ứng là trơn lũy thừa $31$ và trơn lũy thừa $16$, vì $1303 - 1 = 2 \cdot 3 \cdot 7 \cdot 31$ và $3697 - 1 = 2^4 \cdot 3 \cdot 7 \cdot 11$.
Vào năm 1974, John Pollard đã phát minh ra một phương pháp tách ước số $p$ từ hợp số $n$ dựa trên điều kiện $p-1$ là số trơn lũy thừa $\mathrm{B}$.

Ý tưởng xuất phát từ [Định lý nhỏ Fermat](phi-function.md#application).
Giả sử $n$ có phân tích là $n = p \cdot q$.
Nếu $a$ nguyên tố cùng nhau với $p$, mệnh đề sau luôn đúng:

$$a^{p - 1} \equiv 1 \pmod{p}$$

Điều này cũng có nghĩa là:

$${\left(a^{(p - 1)}\right)}^k \equiv a^{k \cdot (p - 1)} \equiv 1 \pmod{p}.$$

Do đó, với bất kỳ số $M$ nào chia hết cho $p - 1$, chúng ta có $a^M \equiv 1 \pmod{p}$.
Điều này kéo theo $a^M - 1 = p \cdot r$, vì vậy $p ~|~ \gcd(a^M - 1, n)$.

Vì vậy, nếu $p - 1$ của một ước số $p$ của $n$ chia hết cho $M$, chúng ta có thể tìm được ước số đó bằng [thuật toán GCD của Euclid](euclid-algorithm.md).

Rõ ràng, số $M$ nhỏ nhất là bội số của mọi số trơn lũy thừa $\mathrm{B}$ là $\text{lcm}(1,~2~,3~,4~,~\dots,~B)$.
Hoặc biểu diễn cách khác:

$$M = \prod_{\text{số nguyên tố } q \le B} q^{\lfloor \log_q B \rfloor}$$

Lưu ý rằng nếu $p-1$ chia hết cho $M$ với mọi ước nguyên tố $p$ của $n$, thì giá trị $\gcd(a^M - 1, n)$ sẽ bằng $n$.
Trong trường hợp này, chúng ta không tách được ước số thực sự.
Do đó, chúng ta sẽ thực hiện phép tính $\gcd$ nhiều lần trong quá trình tính toán $M$.

Một số hợp số không có ước số $p$ nào thỏa mãn $p-1$ là trơn lũy thừa $\mathrm{B}$ với $\mathrm{B}$ nhỏ.
Ví dụ đối với hợp số $100~000~000~000~000~493 = 763~013 \cdot 131~059~365~961$, các giá trị $p-1$ tương ứng là trơn lũy thừa $190~753$ và trơn lũy thừa $1~092~161~383$.
Chúng ta sẽ phải chọn $B \geq 190~753$ để phân tích được số này.

Trong bản cài đặt dưới đây, chúng ta bắt đầu với $\mathrm{B} = 10$ và tăng dần $\mathrm{B}$ sau mỗi vòng lặp.

```{.cpp file=factorization_p_minus_1}
long long pollards_p_minus_1(long long n) {
    int B = 10;
    long long g = 1;
    while (B <= 1000000 && g < n) {
        long long a = 2 + rand() %  (n - 3);
        g = gcd(a, n);
        if (g > 1)
            return g;

        // compute a^M
        for (int p : primes) {
            if (p >= B)
                continue;
            long long p_power = 1;
            while (p_power * p <= B)
                p_power *= p;
            a = power(a, p_power, n);

            g = gcd(a - 1, n);
            if (g > 1 && g < n)
                return g;
        }
        B *= 2;
    }
    return 1;
}

```

Lưu ý rằng đây là một thuật toán xác suất, nghĩa là có khả năng thuật toán không thể tìm thấy ước số nào.

Độ phức tạp là $O(B \log B \log^2 n)$ cho mỗi vòng lặp.

## Thuật toán rho của Pollard (Pollard's rho algorithm)

Thuật toán Rho của Pollard là một thuật toán phân tích số nguyên khác cũng của tác giả John Pollard.

Giả sử phân tích thừa số nguyên tố của số đó là $n = p q$.
Thuật toán xây dựng một dãy giả ngẫu nhiên $\{x_i\} = \{x_0,~f(x_0),~f(f(x_0)),~\dots\}$, trong đó $f$ là một hàm đa thức, thường chọn $f(x) = (x^2 + c) \bmod n$ với $c = 1$.

Thực tế, chúng ta không quan tâm trực tiếp đến dãy $\{x_i\}$, mà quan tâm đến dãy $\{x_i \bmod p\}$.
Vì $f$ là hàm đa thức và mọi giá trị nằm trong khoảng $[0;~p)$, dãy này cuối cùng sẽ lặp lại tạo thành một chu trình.
**Nghịch lý ngày sinh (birthday paradox)** chỉ ra rằng số lượng phần tử dự kiến trước khi bắt đầu lặp lại là $O(\sqrt{p})$.
Nếu $p$ nhỏ hơn $\sqrt{n}$, chu trình sẽ bắt đầu sau khoảng $O(\sqrt[4]{n})$ bước.

Dưới đây là hình ảnh minh họa cho dãy $\{x_i \bmod p\}$ với $n = 2206637$, $p = 317$, $x_0 = 2$ và $f(x) = x^2 + 1$.
Từ hình dáng của dãy, bạn có thể thấy rõ tại sao thuật toán này được gọi là thuật toán $\rho$ (rho) của Pollard.

<div style="text-align: center;" markdown="1">

![Pollard's rho visualization](pollard_rho.png)

</div>

Câu hỏi đặt ra là làm thế nào chúng ta tận dụng tính chất của dãy $\{x_i \bmod p\}$ khi không biết trước giá trị $p$?

Cách làm rất đơn giản.
Một chu trình xuất hiện trong dãy $\{x_i \bmod p\}_{i \le j}$ khi và chỉ khi có hai chỉ số $s, t \le j$ sao cho $x_s \equiv x_t \bmod p$.
Phương trình này tương đương với $x_s - x_t \equiv 0 \bmod p$, tức là $p ~|~ \gcd(x_s - x_t, n)$.

Vì vậy, nếu tìm được hai chỉ số $s$ và $t$ sao cho $g = \gcd(x_s - x_t, n) > 1$, chúng ta đã tìm ra chu trình và đồng thời tìm được ước số $g$ của $n$.
Có khả năng $g = n$. Trong trường hợp này, chúng ta chưa tìm được ước số thực sự, và cần chạy lại thuật toán với các tham số khác (giá trị bắt đầu $x_0$ khác hoặc hằng số $c$ khác trong hàm đa thức $f$).

Để tìm chu trình, chúng ta có thể sử dụng bất kỳ thuật toán phát hiện chu trình thông thường nào.

### Thuật toán tìm chu trình Floyd (Floyd's cycle-finding algorithm)

Thuật toán này tìm chu trình bằng cách sử dụng hai con trỏ di chuyển trên dãy với tốc độ khác nhau (thường gọi là thuật toán Rùa và Thỏ).
Ở mỗi bước, con trỏ thứ nhất (Rùa) tiến lên 1 phần tử, còn con trỏ thứ hai (Thỏ) tiến lên 2 phần tử.
Nếu tồn tại chu trình, Thỏ chắc chắn sẽ đuổi kịp và gặp lại Rùa tại một thời điểm nào đó.
Thuật toán này còn được biết đến với tên gọi [Thuật toán Rùa và Thỏ](../others/tortoise_and_hare.md), dựa trên câu chuyện ngụ ngôn trong đó một con rùa (con trỏ chậm) và một con thỏ (con trỏ nhanh) chạy đua với nhau.
Nếu chiều dài chu trình là $\lambda$ và vị trí bắt đầu chu trình là $\mu$, thuật toán chạy trong thời gian $O(\lambda + \mu)$ và sử dụng bộ nhớ $O(1)$.

```text
function floyd(f, x0):
    tortoise = x0
    hare = f(x0)
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    return true
```

### Cài đặt

Bản cài đặt dưới đây sử dụng **thuật toán tìm chu trình Floyd**.
Thuật toán chạy trong thời gian $O(\sqrt[4]{n} \log(n))$.

```{.cpp file=pollard_rho}
long long mult(long long a, long long b, long long mod) {
    return (__int128)a * b % mod;
}

long long f(long long x, long long c, long long mod) {
    return (mult(x, x, mod) + c) % mod;
}

long long rho(long long n, long long x0=2, long long c=1) {
    long long x = x0;
    long long y = x0;
    long long g = 1;
    while (g == 1) {
        x = f(x, c, n);
        y = f(y, c, n);
        y = f(y, c, n);
        g = gcd(abs(x - y), n);
    }
    return g;
}
```

Bảng dưới đây minh họa giá trị của $x$ và $y$ trong thuật toán cho $n = 2206637$, $x_0 = 2$ và $c = 1$.

$$
\newcommand\T{\Rule{0pt}{1em}{.3em}}
\begin{array}{|l|l|l|l|l|l|}
\hline
i & x_i \bmod n & x_{2i} \bmod n & x_i \bmod 317 & x_{2i} \bmod 317 & \gcd(x_i - x_{2i}, n) \\
\hline
0   & 2       & 2       & 2       & 2       & -   \\
1   & 5       & 26      & 5       & 26      & 1   \\
2   & 26      & 458330  & 26      & 265     & 1   \\
3   & 677     & 1671573 & 43      & 32      & 1   \\
4   & 458330  & 641379  & 265     & 88      & 1   \\
5   & 1166412 & 351937  & 169     & 67      & 1   \\
6   & 1671573 & 1264682 & 32      & 169     & 1   \\
7   & 2193080 & 2088470 & 74      & 74      & 317 \\
\hline
\end{array}$$

Đoạn mã trên sử dụng hàm `mult` để nhân hai số nguyên $\le 10^{18}$ tránh tràn số bằng cách dùng kiểu dữ liệu `__int128` của GCC.
Nếu không sử dụng trình biên dịch GCC, bạn có thể triển khai hàm nhân bằng ý tưởng tương tự như [lũy thừa nhị phân](binary-exp.md).

```{.cpp file=pollard_rho_mult2}
long long mult(long long a, long long b, long long mod) {
    long long result = 0;
    while (b) {
        if (b & 1)
            result = (result + a) % mod;
        a = (a + a) % mod;
        b >>= 1;
    }
    return result;
}
```

Ngoài ra, bạn cũng có thể cài đặt [phép nhân Montgomery](montgomery_multiplication.md).

Như đã đề cập trước đó, nếu $n$ là hợp số nhưng thuật toán lại trả về ước số chính bằng $n$, bạn cần lặp lại thuật toán với các giá trị khác cho $x_0$ và $c$.
Ví dụ việc chọn $x_0 = c = 1$ sẽ không thể phân tích số $25 = 5 \cdot 5$ (thuật toán sẽ trả về $25$). Tuy nhiên, nếu chọn $x_0 = 1$, $c = 2$ thì thuật toán sẽ phân tích thành công.

### Thuật toán Brent (Brent's algorithm)

Brent đề xuất một phương pháp tìm chu trình tương tự như Floyd nhưng tối ưu hơn.
Thay vì tăng vị trí con trỏ thêm 1 và 2 đơn vị, thuật toán tăng theo các lũy thừa của 2.
Ngay khi $2^i$ lớn hơn $\lambda$ và $\mu$, chúng ta sẽ phát hiện được chu trình.

```text
function floyd(f, x0):
    tortoise = x0
    hare = f(x0)
    l = 1
    while tortoise != hare:
        tortoise = hare
        repeat l times:
            hare = f(hare)
            if tortoise == hare:
                return true
        l *= 2
    return true
```

Thuật toán Brent cũng chạy trong thời gian tuyến tính nhưng thường nhanh hơn Floyd vì nó sử dụng ít lượt tính toán hàm $f$ hơn.

### Cài đặt

Bản cài đặt thuật toán Brent dưới đây được tăng tốc bằng cách bỏ qua các số hạng $x_l - x_k$ khi $k < \frac{3 \cdot l}{2}$.
Ngoài ra, thay vì thực hiện phép tính $\gcd$ ở mỗi bước, chúng ta nhân tích dồn các số hạng lại và chỉ thực hiện $\gcd$ sau mỗi khoảng bước cố định, và quay lui nếu vượt quá.

```{.cpp file=pollard_rho_brent}
long long brent(long long n, long long x0=2, long long c=1) {
    long long x = x0;
    long long g = 1;
    long long q = 1;
    long long xs, y;

    int m = 128;
    int l = 1;
    while (g == 1) {
        y = x;
        for (int i = 1; i < l; i++)
            x = f(x, c, n);
        int k = 0;
        while (k < l && g == 1) {
            xs = x;
            for (int i = 0; i < m && i < l - k; i++) {
                x = f(x, c, n);
                q = mult(q, abs(y - x), n);
            }
            g = gcd(q, n);
            k += m;
        }
        l *= 2;
    }
    if (g == n) {
        do {
            xs = f(xs, c, n);
            g = gcd(abs(xs - y), n);
        } while (g == 1);
    }
    return g;
}
```

Sự kết hợp giữa phép chia thử cho các số nguyên tố nhỏ cùng với thuật toán Brent (biến thể của thuật toán rho của Pollard) tạo nên một công cụ phân tích thừa số cực kỳ mạnh mẽ.

## Bài tập áp dụng

- [SPOJ - FACT0](https://www.spoj.com/problems/FACT0/)
- [SPOJ - FACT1](https://www.spoj.com/problems/FACT1/)
- [SPOJ - FACT2](https://www.spoj.com/problems/FACT2/)
- [GCPC 15 - Divisions](https://codeforces.com/gym/100753)
