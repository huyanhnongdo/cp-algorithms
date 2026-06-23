---
tags:
    - Translated
lang: vi
---

# Kiểm tra tính nguyên tố (Primality tests)

Bài viết này mô tả nhiều thuật toán khác nhau nhằm xác định xem một số có phải là số nguyên tố hay không.

## Phép chia thử (Trial division)

Theo định nghĩa, một số nguyên tố không có bất kỳ ước số nào ngoài $1$ và chính nó.
Một hợp số có ít nhất một ước số khác, gọi ước số này là $d$.
Rõ ràng $\frac{n}{d}$ cũng là một ước của $n$.
Dễ thấy rằng, hoặc $d \le \sqrt{n}$ hoặc $\frac{n}{d} \le \sqrt{n}$, do đó một trong hai ước $d$ và $\frac{n}{d}$ phải $\le \sqrt{n}$.
Chúng ta có thể tận dụng thông tin này để kiểm tra tính nguyên tố.

Chúng ta cố gắng tìm một ước số thực sự (khác 1 và n) bằng cách kiểm tra xem có bất kỳ số nào trong khoảng từ $2$ đến $\sqrt{n}$ là ước của $n$ hay không.
Nếu tìm được ước số, n chắc chắn là hợp số, ngược lại $n$ là số nguyên tố.

```cpp
bool isPrime(int x) {
    for (int d = 2; d * d <= x; d++) {
        if (x % d == 0)
            return false;
    }
    return x >= 2;
}
```

Đây là dạng đơn giản nhất của phép kiểm tra số nguyên tố.
Bạn có thể tối ưu hóa hàm này thêm khá nhiều, ví dụ chỉ cần kiểm tra các số lẻ trong vòng lặp vì số nguyên tố chẵn duy nhất là 2.
Nhiều tối ưu hóa tương tự được mô tả chi tiết trong bài viết về [phân tích thừa số nguyên tố](factorization.md).

## Phép kiểm tra tính nguyên tố Fermat (Fermat primality test)

Đây là một phép kiểm tra xác suất.

Định lý nhỏ Fermat (xem thêm tại bài viết [Phi hàm Euler](phi-function.md)) phát biểu rằng, với mọi số nguyên tố $p$ và số nguyên $a$ nguyên tố cùng nhau với p, phương trình sau luôn đúng:

$$a^{p-1} \equiv 1 \bmod p$$

Nhìn chung, định lý này không đúng đối với hợp số.

Tính chất này có thể được dùng để xây dựng thuật toán kiểm tra số nguyên tố.
Chúng ta chọn một số nguyên $2 \le a \le p - 2$, và kiểm tra xem phương trình trên có thỏa mãn hay không.
Nếu phương trình không thỏa mãn, tức là $a^{p-1} \not\equiv 1 \bmod p$, chúng ta biết chắc chắn rằng $p$ không thể là số nguyên tố.
Trong trường hợp này, cơ số $a$ được gọi là một *chứng nhân Fermat (Fermat witness)* cho việc p là hợp số.

Tuy nhiên, phương trình trên cũng có thể thỏa mãn đối với một hợp số.
Do đó, nếu phương trình thỏa mãn, chúng ta vẫn chưa có bằng chứng chắc chắn về tính nguyên tố của $p$.
Chúng ta chỉ có thể kết luận rằng $p$ *có khả năng là số nguyên tố (probably prime)*.
Nếu sau đó xác định được số này thực tế là hợp số, cơ số $a$ được gọi là một *kẻ nói dối Fermat (Fermat liar)*.

Bằng cách chạy kiểm tra cho tất cả các cơ số $a$ khả dĩ, chúng ta thực sự có thể chứng minh một số là số nguyên tố.
Tuy nhiên, điều này không được thực hiện trong thực tế vì nó đòi hỏi nhiều công sức hơn cả *phép chia thử*.
Thay vào đó, phép kiểm tra sẽ được lặp lại nhiều lần với các cơ số $a$ được chọn ngẫu nhiên.
Nếu không tìm thấy chứng nhân hợp số nào sau nhiều lượt thử, khả năng cực kỳ cao là số đó là số nguyên tố.

```cpp
bool probablyPrimeFermat(int n, int iter=5) {
    if (n < 4)
        return n == 2 || n == 3;

    for (int i = 0; i < iter; i++) {
        int a = 2 + rand() % (n - 3);
        if (binpower(a, n - 1, n) != 1)
            return false;
    }
    return true;
}
```

Chúng ta sử dụng thuật toán [Lũy thừa nhị phân](binary-exp.md) để tính toán lũy thừa $a^{p-1}$ một cách hiệu quả.

Tuy nhiên, có một tin xấu:
Tồn tại một số hợp số mà phương trình $a^{n-1} \equiv 1 \bmod n$ thỏa mãn với mọi $a$ nguyên tố cùng nhau với $n$, ví dụ như số $561 = 3 \cdot 11 \cdot 17$.
Những số như vậy được gọi là *số Carmichael*.
Phép kiểm tra tính nguyên tố Fermat chỉ có thể phát hiện các số này nếu chúng ta cực kỳ may mắn chọn được cơ số $a$ mà $\gcd(a, n) \ne 1$.

Mặc dù vậy, phép kiểm tra Fermat vẫn được sử dụng trong thực tế vì tốc độ rất nhanh và số Carmichael cực kỳ hiếm.
Ví dụ, chỉ có 646 số Carmichael nhỏ hơn $10^9$.

## Phép kiểm tra tính nguyên tố Miller-Rabin (Miller-Rabin primality test)

Phép kiểm tra Miller-Rabin mở rộng ý tưởng của phép kiểm tra Fermat.

Với một số lẻ $n$, số $n-1$ là số chẵn nên chúng ta có thể tách tất cả các lũy thừa của 2 ra ngoài.
Chúng ta có thể viết:

$$n - 1 = 2^s \cdot d,~\text{với}~d~\text{là số lẻ}.$$

Điều này cho phép chúng ta phân tích phương trình của định lý nhỏ Fermat thành các nhân tử:

$$\begin{array}{rl}
a^{n-1} \equiv 1 \bmod n &\Longleftrightarrow a^{2^s d} - 1 \equiv 0 \bmod n \\\\
&\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-1} d} - 1) \equiv 0 \bmod n \\\\
&\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-2} d} + 1) (a^{2^{s-2} d} - 1) \equiv 0 \bmod n \\\\
&\quad\vdots \\\\
&\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-2} d} + 1) \cdots (a^{d} + 1) (a^{d} - 1) \equiv 0 \bmod n \\\\
\end{array}$$

Nếu $n$ là số nguyên tố, thì $n$ phải chia hết một trong các nhân tử này.
Trong phép kiểm tra tính nguyên tố Miller-Rabin, chúng ta kiểm tra chính xác mệnh đề đó, đây là một phiên bản chặt chẽ hơn nhiều so với phép kiểm tra Fermat.
Với một cơ số $2 \le a \le n-2$, chúng ta kiểm tra xem có phải:

$$a^d \equiv 1 \bmod n$$

thỏa mãn hoặc

$$a^{2^r d} \equiv -1 \bmod n$$

thỏa mãn với một giá trị $0 \le r \le s - 1$ nào đó.

Nếu tìm được một cơ số $a$ không thỏa mãn bất kỳ đẳng thức nào ở trên, chúng ta đã tìm thấy một *chứng nhân (witness)* chứng tỏ $n$ là hợp số.
Trong trường hợp này, chúng ta đã chứng minh được $n$ không phải là số nguyên tố.

Tương tự như phép kiểm tra Fermat, hệ phương trình trên cũng có thể thỏa mãn đối với một hợp số.
Khi đó, cơ số $a$ được gọi là một *kẻ nói dối mạnh (strong liar)*.
Nếu một cơ số $a$ thỏa mãn một trong các phương trình, $n$ chỉ được gọi là *số nguyên tố xác suất mạnh (strong probable prime)*.
Tuy nhiên, không có các số đặc biệt giống như số Carmichael khiến tất cả các cơ số phi hữu tỉ đều bị lừa.
Thực tế, người ta đã chứng minh được rằng có tối đa $\frac{1}{4}$ số cơ số có thể là kẻ nói dối mạnh.
Nếu $n$ là hợp số, xác suất để một cơ số ngẫu nhiên chỉ ra nó là hợp số là $\ge 75\%$.
Bằng cách lặp lại nhiều lần với các cơ số ngẫu nhiên khác nhau, chúng ta có thể kết luận với xác suất cực kỳ cao liệu số đó là số nguyên tố thực sự hay là hợp số.

Dưới đây là một bản cài đặt cho số nguyên 64-bit.

```cpp
using u64 = uint64_t;
using u128 = __uint128_t;

u64 binpower(u64 base, u64 e, u64 mod) {
    u64 result = 1;
    base %= mod;
    while (e) {
        if (e & 1)
            result = (u128)result * base % mod;
        base = (u128)base * base % mod;
        e >>= 1;
    }
    return result;
}

bool check_composite(u64 n, u64 a, u64 d, int s) {
    u64 x = binpower(a, d, n);
    if (x == 1 || x == n - 1)
        return false;
    for (int r = 1; r < s; r++) {
        x = (u128)x * x % n;
        if (x == n - 1)
            return false;
    }
    return true;
};

bool MillerRabin(u64 n, int iter=5) { // returns true if n is probably prime, else returns false.
    if (n < 4)
        return n == 2 || n == 3;

    int s = 0;
    u64 d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        s++;
    }

    for (int i = 0; i < iter; i++) {
        int a = 2 + rand() % (n - 3);
        if (check_composite(n, a, d, s))
            return false;
    }
    return true;
}
```

Trước khi thực hiện kiểm tra Miller-Rabin, bạn có thể kiểm tra xem số đó có chia hết cho một vài số nguyên tố nhỏ đầu tiên hay không.
Việc này có thể giúp tăng tốc thuật toán đáng kể, vì hầu hết các hợp số đều có các ước nguyên tố rất nhỏ.
Ví dụ: $88\%$ các số đều có một ước nguyên tố nhỏ hơn $100$.

### Phiên bản tất định (Deterministic version)

Miller đã chỉ ra rằng có thể biến đổi thuật toán này thành thuật toán tất định bằng cách chỉ kiểm tra tất cả các cơ số $\le O((\ln n)^2)$.
Sau đó, Bach đã đưa ra một giới hạn cụ thể, theo đó chỉ cần kiểm tra tất cả các cơ số $a \le 2 \ln(n)^2$.

Tuy nhiên số lượng cơ số cần kiểm tra này vẫn khá lớn.
Do đó, nhiều người đã đầu tư năng lực tính toán để tìm ra các giới hạn thấp hơn.
Kết quả cho thấy, để kiểm tra một số nguyên 32-bit, chúng ta chỉ cần kiểm tra 4 cơ số nguyên tố đầu tiên: 2, 3, 5 và 7.
Hợp số nhỏ nhất không vượt qua được phép thử này là $3,215,031,751 = 151 \cdot 751 \cdot 28351$.
Đối với số nguyên 64-bit, chỉ cần kiểm tra 12 cơ số nguyên tố đầu tiên: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, và 37.

Điều này dẫn đến bản cài đặt tất định sau:

```cpp
bool MillerRabin(u64 n) { // returns true if n is prime, else returns false.
    if (n < 2)
        return false;

    int r = 0;
    u64 d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        r++;
    }

    for (int a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        if (n == a)
            return true;
        if (check_composite(n, a, d, r))
            return false;
    }
    return true;
}
```

Chúng ta cũng có thể thực hiện kiểm tra chỉ với 7 cơ số: 2, 325, 9375, 28178, 450775, 9780504 và 1795265022.
Tuy nhiên, vì các số này (trừ 2) không phải là số nguyên tố, bạn cần kiểm tra thêm xem số cần thử có bằng bất kỳ ước nguyên tố nào của các cơ số đó hay không: 2, 3, 5, 13, 19, 73, 193, 407521, 299210837.

## Bài tập áp dụng

- [SPOJ - Prime or Not](https://www.spoj.com/problems/PON/)
- [Project Euler - Investigating a Prime Pattern](https://projecteuler.net/problem=146)
