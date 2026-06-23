---
tags:
  - Translated
---

# Phép nhân Montgomery

Nhiều thuật toán trong lý thuyết số, như [kiểm tra số nguyên tố](primality_tests.md) hoặc [phân tích thừa số nguyên tố](factorization.md), và trong mật mã học, như RSA, yêu cầu rất nhiều phép toán mô-đun với một số lớn.
Phép nhân như $x y \bmod{n}$ khá chậm để tính toán bằng các thuật toán thông thường, vì nó yêu cầu phép chia để biết được số lần $n$ cần phải trừ đi từ tích.
Và phép chia là một phép toán rất tốn kém, đặc biệt là với các số lớn.

**Phép nhân (mô-đun) Montgomery** là một phương pháp cho phép tính toán các phép nhân như vậy nhanh hơn.
Thay vì chia tích và trừ $n$ nhiều lần, nó cộng thêm các bội số của $n$ để triệt tiêu các bit thấp hơn và sau đó chỉ cần loại bỏ các bit thấp này đi.

## Biểu diễn Montgomery

Tuy nhiên, phép nhân Montgomery không phải là không có chi phí.
Thuật toán này chỉ hoạt động trong **không gian Montgomery (Montgomery space)**.
Và chúng ta cần chuyển các số của mình vào không gian đó trước khi bắt đầu thực hiện phép nhân.

Đối với không gian này, chúng ta cần một số nguyên dương $r \ge n$ nguyên tố cùng nhau với $n$, tức là $\gcd(n, r) = 1$.
Trong thực tế, chúng ta luôn chọn $r$ là $2^m$ với $m$ là số nguyên dương, vì khi đó phép nhân, phép chia và phép toán mô-đun $r$ có thể được thực hiện hiệu quả bằng các phép dịch bit và các phép toán bit khác.
Trong hầu hết mọi ứng dụng, $n$ sẽ là một số lẻ, vì việc phân tích một số chẵn thành thừa số là không khó.
Do đó, mọi lũy thừa của $2$ đều nguyên tố cùng nhau với $n$.

Số đại diện $\bar{x}$ của một số $x$ trong không gian Montgomery được định nghĩa là:

$$\bar{x} := x \cdot r \bmod n$$

Lưu ý rằng bản thân phép biến đổi này chính là phép nhân mà chúng ta muốn tối ưu hóa.
Vì vậy, đây vẫn là một phép toán tốn kém.
Tuy nhiên, bạn chỉ cần chuyển đổi một số vào không gian này một lần duy nhất.
Ngay sau khi bạn ở trong không gian Montgomery, bạn có thể thực hiện bao nhiêu phép toán tùy ý một cách hiệu quả.
Và cuối cùng, bạn biến đổi kết quả cuối cùng trở lại không gian thường.
Vì vậy, miễn là bạn thực hiện nhiều phép toán theo mô-đun $n$, việc chuyển đổi này sẽ không phải là vấn đề lớn.

Trong không gian Montgomery, bạn vẫn có thể thực hiện hầu hết các phép toán như bình thường.
Bạn có thể cộng hai phần tử ($x \cdot r + y \cdot r \equiv (x + y) \cdot r \bmod n$), trừ, kiểm tra tính bằng nhau, và thậm chí tính ước chung lớn nhất của một số với $n$ (vì $\gcd(n, r) = 1$).
Tất cả đều sử dụng các thuật toán thông thường.

Tuy nhiên, điều này không đúng đối với phép nhân.

Chúng ta mong muốn kết quả sẽ là:

$$\bar{x} * \bar{y} = \overline{x \cdot y} = (x \cdot y) \cdot r \bmod n.$$

Nhưng phép nhân thông thường sẽ cho chúng ta:

$$\bar{x} \cdot \bar{y} = (x \cdot y) \cdot r \cdot r \bmod n.$$

Do đó, phép nhân trong không gian Montgomery được định nghĩa là:

$$\bar{x} * \bar{y} := \bar{x} \cdot \bar{y} \cdot r^{-1} \bmod n.$$

## Phép khử Montgomery

Phép nhân hai số trong không gian Montgomery yêu cầu tính toán hiệu quả $x \cdot r^{-1} \bmod n$.
Phép toán này được gọi là **phép khử Montgomery (Montgomery reduction)**, và còn được gọi là thuật toán **REDC**.

Vì $\gcd(n, r) = 1$, chúng ta biết rằng có hai số $r^{-1}$ và $n^{\prime}$ với $0 < r^{-1}, n^{\prime} < n$ thỏa mãn

$$r \cdot r^{-1} + n \cdot n^{\prime} = 1.$$

Cả $r^{-1}$ và $n^{\prime}$ đều có thể được tính bằng [Thuật toán Euclid mở rộng (Extended Euclidean algorithm)](extended-euclid-algorithm.md).

Sử dụng đồng nhất thức này, chúng ta có thể viết $x \cdot r^{-1}$ dưới dạng:

$$\begin{aligned}
x \cdot r^{-1} &= x \cdot r \cdot r^{-1} / r = x \cdot (-n \cdot n^{\prime} + 1) / r \\
&= (-x \cdot n \cdot n^{\prime} + x) / r \equiv (-x \cdot n \cdot n^{\prime} + l \cdot r \cdot n + x) / r \bmod n\\
&\equiv ((-x \cdot n^{\prime} + l \cdot r) \cdot n + x) / r \bmod n
\end{aligned}$$

Các phép đồng dư trên giữ nguyên với số nguyên $l$ bất kỳ.
Điều này có nghĩa là chúng ta có thể cộng hoặc trừ một bội số bất kỳ của $r$ vào $x \cdot n^{\prime}$, hay nói cách khác, chúng ta có thể tính $q := x \cdot n^{\prime}$ theo mô-đun $r$.

Điều này cho chúng ta thuật toán sau để tính $x \cdot r^{-1} \bmod n$:

```text
function reduce(x):
    q = (x mod r) * n' mod r
    a = (x - q * n) / r
    if a < 0:
        a += n
    return a
```

Vì $x < n \cdot n < r \cdot n$ (ngay cả khi $x$ là tích của một phép nhân) và $q \cdot n < r \cdot n$, chúng ta biết rằng $-n < (x - q \cdot n) / r < n$.
Do đó, phép toán lấy mô-đun cuối cùng được cài đặt chỉ bằng một phép kiểm tra đơn giản và một phép cộng.

Như có thể thấy, chúng ta có thể thực hiện phép khử Montgomery mà không cần bất kỳ phép toán lấy mô-đun phức tạp nào.
Nếu chọn $r$ là một lũy thừa của $2$, các phép toán lấy mô-đun và phép chia trong thuật toán có thể được tính toán bằng cách sử dụng phép toán thao tác bit và phép dịch bit.

Ứng dụng thứ hai của phép khử Montgomery là chuyển một số từ không gian Montgomery ngược trở lại không gian thông thường.

## Mẹo tính nghịch đảo nhanh

Để tính nghịch đảo $n^{\prime} := n^{-1} \bmod r$ một cách hiệu quả, chúng ta có thể sử dụng mẹo sau (lấy cảm hứng từ phương pháp Newton):

$$a \cdot x \equiv 1 \bmod 2^k \Longrightarrow a \cdot x \cdot (2 - a \cdot x) \equiv 1 \bmod 2^{2k}$$

Điều này có thể được chứng minh dễ dàng.
Nếu ta có $a \cdot x = 1 + m \cdot 2^k$, thì ta có:

$$\begin{aligned}
a \cdot x \cdot (2 - a \cdot x) &= 2 \cdot a \cdot x - (a \cdot x)^2 \\
&= 2 \cdot (1 + m \cdot 2^k) - (1 + m \cdot 2^k)^2 \\
&= 2 + 2 \cdot m \cdot 2^k - 1 - 2 \cdot m \cdot 2^k - m^2 \cdot 2^{2k} \\
&= 1 - m^2 \cdot 2^{2k} \\
&\equiv 1 \bmod 2^{2k}.
\end{aligned}$$

Điều này có nghĩa là chúng ta có thể bắt đầu với $x = 1$ là nghịch đảo của $a$ theo mô-đun $2^1$, áp dụng mẹo này một vài lần và sau mỗi lần lặp, chúng ta sẽ nhân đôi số lượng bit chính xác của $x$.

## Cài đặt

Sử dụng trình biên dịch GCC, chúng ta vẫn có thể tính $x \cdot y \bmod n$ một cách hiệu quả khi cả ba số đều là số nguyên 64-bit, vì trình biên dịch hỗ trợ số nguyên 128-bit với các kiểu dữ liệu `__int128` và `__uint128`.

```cpp
long long result = (__int128)x * y % n;
```

Tuy nhiên, không có kiểu dữ liệu nào cho số nguyên 256-bit.
Do đó, dưới đây chúng tôi sẽ trình bày một cài đặt cho phép nhân 128-bit.

```cpp
using u64 = uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;

struct u256 {
    u128 high, low;

    static u256 mult(u128 x, u128 y) {
        u64 a = x >> 64, b = x;
        u64 c = y >> 64, d = y;
        // (a*2^64 + b) * (c*2^64 + d) =
        // (a*c) * 2^128 + (a*d + b*c)*2^64 + (b*d)
        u128 ac = (u128)a * c;
        u128 ad = (u128)a * d;
        u128 bc = (u128)b * c;
        u128 bd = (u128)b * d;
        u128 carry = (u128)(u64)ad + (u128)(u64)bc + (bd >> 64u);
        u128 high = ac + (ad >> 64u) + (bc >> 64u) + (carry >> 64u);
        u128 low = (ad << 64u) + (bc << 64u) + bd;
        return {high, low};
    }
};

struct Montgomery {
    Montgomery(u128 n) : mod(n), inv(1) {
        for (int i = 0; i < 7; i++)
            inv *= 2 - n * inv;
    }

    u128 init(u128 x) {
        x %= mod;
        for (int i = 0; i < 128; i++) {
            x <<= 1;
            if (x >= mod)
                x -= mod;
        }
        return x;
    }

    u128 reduce(u256 x) {
        u128 q = x.low * inv;
        i128 a = x.high - u256::mult(q, mod).high;
        if (a < 0)
            a += mod;
        return a;
    }

    u128 mult(u128 a, u128 b) {
        return reduce(u256::mult(a, b));
    }

    u128 mod, inv;
};
```

## Biến đổi nhanh

Phương pháp hiện tại để chuyển đổi một số vào không gian Montgomery khá chậm.
Có những cách nhanh hơn.

Bạn có thể nhận thấy mối liên hệ sau:

$$\bar{x} := x \cdot r \bmod n = x \cdot r^2 / r = x * r^2$$

Việc chuyển đổi một số vào không gian này thực chất chỉ là một phép nhân bên trong không gian của số đó với $r^2$.
Do đó, chúng ta có thể tính trước $r^2 \bmod n$ và chỉ cần thực hiện một phép nhân thay vì dịch số đó 128 lần.

Trong đoạn mã dưới đây, chúng ta khởi tạo `r2` với `-n % n` (tương đương với $r - n \equiv r \bmod n$), dịch nó 4 lần để được $r \cdot 2^4 \bmod n$.
Số này có thể được hiểu là $2^4$ trong không gian Montgomery.
Nếu bình phương nó lên $5$ lần, chúng ta sẽ nhận được $(2^4)^{2^5} = (2^4)^{32} = 2^{128} = r$ trong không gian Montgomery, chính xác là $r^2 \bmod n$.

```
struct Montgomery {
    Montgomery(u128 n) : mod(n), inv(1), r2(-n % n) {
        for (int i = 0; i < 7; i++)
            inv *= 2 - n * inv;

        for (int i = 0; i < 4; i++) {
            r2 <<= 1;
            if (r2 >= mod)
                r2 -= mod;
        }
        for (int i = 0; i < 5; i++)
            r2 = mul(r2, r2);
    }

    u128 init(u128 x) {
        return mult(x, r2);
    }

    u128 mod, inv, r2;
};
```
