---
tags:
  - Translated
---

# Lũy thừa nhị phân bằng phân tích nhân tử

Xét bài toán tính $ax^y \pmod{2^d}$, cho trước các số nguyên $a$, $x$, $y$ và $d \geq 3$, trong đó $x$ là số lẻ.

Thuật toán dưới đây cho phép giải bài toán này với $O(d)$ phép cộng và phép toán nhị phân, cùng một phép nhân duy nhất với $y$.

Do cấu trúc của nhóm nhân các số nguyên modulo $2^d$, bất kỳ số $x$ nào thỏa mãn $x \equiv 1 \pmod 4$ đều có thể được biểu diễn dưới dạng:

$$
x \equiv b^{L(x)} \pmod{2^d},
$$

trong đó $b \equiv 5 \pmod 8$. Không mất tính tổng quát, chúng ta giả định rằng $x \equiv 1 \pmod 4$, vì chúng ta có thể quy đổi $x \equiv 3 \pmod 4$ về $x \equiv 1 \pmod 4$ bằng cách thế $x \mapsto -x$ và $a \mapsto (-1)^{y} a$. Với cách biểu diễn này, $ax^y$ được viết dưới dạng:

$$
a x^y \equiv a b^{yL(x)} \pmod{2^d}.
$$

Ý tưởng cốt lõi của thuật toán là đơn giản hóa việc tính toán $L(x)$ và $b^{y L(x)}$ dựa trên tính chất chúng ta đang làm việc theo mô-đun $2^d$. Vì những lý do sẽ được giải thích rõ ở phần sau, chúng ta sẽ làm việc với $4L(x)$ thay vì $L(x)$, nhưng lấy theo mô-đun $2^d$ thay vì $2^{d-2}$.

Trong bài viết này, chúng tôi sẽ đề cập đến cài đặt cho số nguyên $32$-bit. Gọi:

* `mbin_log_32(r, x)` là hàm tính $r+4L(x) \pmod{2^d}$;
* `mbin_exp_32(r, x)` là hàm tính $r b^{\frac{x}{4}} \pmod{2^d}$;
* `mbin_power_odd_32(a, x, y)` là hàm tính $ax^y \pmod{2^d}$.

Khi đó, `mbin_power_odd_32` được cài đặt như sau:

```cpp
uint32_t mbin_power_odd_32(uint32_t rem, uint32_t base, uint32_t exp) {
    if (base & 2) {
        /* divider is considered negative */
        base = -base;
        /* check if result should be negative */
        if (exp & 1) {
            rem = -rem;
        }
    }
    return (mbin_exp_32(rem, mbin_log_32(0, base) * exp));
}
```

## Tính 4L(x) từ x

Gọi $x$ là một số lẻ sao cho $x \equiv 1 \pmod 4$. Nó có thể được biểu diễn dưới dạng:

$$
x \equiv (2^{a_1}+1)\dots(2^{a_k}+1) \pmod{2^d},
$$

trong đó $1 < a_1 < \dots < a_k < d$. Ở đây $L(\cdot)$ được định nghĩa rõ ràng cho từng thừa số, vì chúng đều bằng $1$ theo mô-đun $4$. Do đó,

$$
4L(x) \equiv 4L(2^{a_1}+1)+\dots+4L(2^{a_k}+1) \pmod{2^{d}}.
$$

Vì vậy, nếu chúng ta tính trước $t_k = 4L(2^n+1)$ cho tất cả $1 < k < d$, chúng ta sẽ có thể tính được $4L(x)$ cho số $x$ bất kỳ.

Đối với số nguyên 32-bit, chúng ta có thể sử dụng bảng sau:

```cpp
const uint32_t mbin_log_32_table[32] = {
    0x00000000, 0x00000000, 0xd3cfd984, 0x9ee62e18,
    0xe83d9070, 0xb59e81e0, 0xa17407c0, 0xce601f80,
    0xf4807f00, 0xe701fe00, 0xbe07fc00, 0xfc1ff800,
    0xf87ff000, 0xf1ffe000, 0xe7ffc000, 0xdfff8000,
    0xffff0000, 0xfffe0000, 0xfffc0000, 0xfff80000,
    0xfff00000, 0xffe00000, 0xffc00000, 0xff800000,
    0xff000000, 0xfe000000, 0xfc000000, 0xf8000000,
    0xf0000000, 0xe0000000, 0xc0000000, 0x80000000,
};
```

Trong thực tế, một cách tiếp cận hơi khác so với mô tả ở trên được sử dụng. Thay vì tìm sự phân tích nhân tử trực tiếp của $x$, chúng ta sẽ lần lượt nhân $x$ với $2^n+1$ cho đến khi biến đổi nó thành $1$ theo mô-đun $2^d$. Bằng cách này, chúng ta sẽ tìm thấy biểu diễn của $x^{-1}$, tức là:

$$
x (2^{a_1}+1)\dots(2^{a_k}+1) \equiv 1 \pmod {2^d}.
$$

Để làm điều này, chúng ta duyệt qua $n$ sao cho $1 < n < d$. Nếu số $x$ hiện tại có bit thứ $n$ được bật, chúng ta nhân $x$ với $2^n+1$, việc này được thực hiện thuận tiện trong C++ dưới dạng `x = x + (x << n)`. Cách này không làm thay đổi các bit thấp hơn $n$, nhưng sẽ chuyển bit thứ $n$ thành 0 vì $x$ là số lẻ.

Với tất cả những điều trên, hàm `mbin_log_32(r, x)` được cài đặt như sau:

```cpp
uint32_t mbin_log_32(uint32_t r, uint32_t x) {
    uint8_t n;

    for (n = 2; n < 32; n++) {
        if (x & (1 << n)) {
            x = x + (x << n);
            r -= mbin_log_32_table[n];
        }
    }

    return r;
}
```

Lưu ý rằng $4L(x) = -4L(x^{-1})$, do đó thay vì cộng thêm $4L(2^n+1)$, chúng ta trừ nó đi từ $r$, giá trị ban đầu của $r$ là $0$.

## Tính x từ 4L(x)

Lưu ý rằng với $k \geq 1$, ta luôn có:

$$
(a 2^{k}+1)^2 = a^2 2^{2k} +a 2^{k+1}+1 = b2^{k+1}+1,
$$

từ đó (bằng cách bình phương liên tiếp) chúng ta có thể suy ra rằng:

$$
(2^a+1)^{2^b} \equiv 1 \pmod{2^{a+b}}.
$$

Áp dụng kết quả này với $a=2^n+1$ and $b=d-k$, ta suy ra cấp (order) nhân tính của $2^n+1$ là một ước của $2^{d-n}$.

Điều này có nghĩa là $L(2^n+1)$ phải chia hết cho $2^{n}$, vì cấp của $b$ là $2^{d-2}$ và cấp của $b^y$ là $2^{d-2-v}$, với $2^v$ là lũy thừa cao nhất của $2$ chia hết cho $y$, nên chúng ta cần:

$$
2^{d-k} \equiv 0 \pmod{2^{d-2-v}},
$$

do đó $v$ phải lớn hơn hoặc bằng $k-2$. Điều này hơi phức tạp và để giảm bớt sự phức tạp này, chúng tôi đã nói ở phần đầu rằng chúng ta nhân $L(x)$ với $4$. Bây giờ, nếu chúng ta biết $4L(x)$, chúng ta có thể phân tích duy nhất nó thành tổng của các $4L(2^n+1)$ bằng cách lần lượt kiểm tra các bit trong $4L(x)$. Nếu bit thứ $n$ được đặt thành $1$, chúng ta sẽ nhân kết quả với $2^n+1$ và giảm bớt giá trị $4L(x)$ hiện tại đi một lượng là $4L(2^n+1)$.

Do đó, `mbin_exp_32` được cài đặt như sau:

```cpp
uint32_t mbin_exp_32(uint32_t r, uint32_t x) {
    uint8_t n;

    for (n = 2; n < 32; n++) {
        if (x & (1 << n)) {
            r = r + (r << n);
            x -= mbin_log_32_table[n];
        }
    }

    return r;
}
```

## Các tối ưu hóa thêm

Chúng ta có thể giảm một nửa số lần lặp nếu nhận thấy rằng $4L(2^{d-1}+1)=2^{d-1}$ và với $2k \geq d$, ta luôn có:

$$
(2^n+1)^2 \equiv 2^{2n} + 2^{n+1}+1 \equiv 2^{n+1}+1 \pmod{2^d},
$$

điều này cho phép ta suy ra rằng $4L(2^n+1)=2^n$ với $2n \geq d$. Do đó, bạn có thể đơn giản hóa thuật toán bằng cách chỉ duyệt lên đến $\frac{d}{2}$ và sau đó sử dụng tính chất trên để tính phần còn lại bằng các phép toán thao tác bit:

```cpp
uint32_t mbin_log_32(uint32_t r, uint32_t x) {
    uint8_t n;

    for (n = 2; n != 16; n++) {
        if (x & (1 << n)) {
            x = x + (x << n);
            r -= mbin_log_32_table[n];
        }
    }

    r -= (x & 0xFFFF0000);

    return r;
}

uint32_t mbin_exp_32(uint32_t r, uint32_t x) {
    uint8_t n;

    for (n = 2; n != 16; n++) {
        if (x & (1 << n)) {
            r = r + (r << n);
            x -= mbin_log_32_table[n];
        }
    }

    r *= 1 - (x & 0xFFFF0000);

    return r;
}
```

## Tính bảng logarit

Để tính bảng logarit (log-table), người ta có thể sửa đổi [thuật toán Pohlig–Hellman](https://en.wikipedia.org/wiki/Pohlig–Hellman_algorithm) cho trường hợp mô-đun là một lũy thừa của $2$.

Nhiệm vụ chính của chúng ta ở đây là tính $x$ sao cho $g^x \equiv y \pmod{2^d}$, trong đó $g=5$ và $y$ là một số có dạng $2^n+1$.

Bình phương cả hai vế $k$ lần, chúng ta đi đến:

$$
g^{2^k x} \equiv y^{2^k} \pmod{2^d}.
$$

Lưu ý rằng cấp của $g$ không lớn hơn $2^{d}$ (trên thực tế là không lớn hơn $2^{d-2}$, nhưng chúng ta sẽ chọn $2^d$ cho thuận tiện), do đó sử dụng $k=d-1$ chúng ta sẽ có $g^1$ hoặc $g^0$ ở vế trái, cho phép xác định bit nhỏ nhất của $x$ bằng cách so sánh $y^{2^k}$ với $g$. Bây giờ giả sử $x=x_0 + 2^k x_1$, trong đó $x_0$ là phần đã biết và $x_1$ là phần chưa biết. Khi đó:

$$
g^{x_0+2^k x_1} \equiv y \pmod{2^d}.
$$

Nhân cả hai vế với $g^{-x_0}$, ta có:

$$
g^{2^k x_1} \equiv (g^{-x_0} y) \pmod{2^d}.
$$

Bây giờ, bình phương cả hai vế $d-k-1$ lần, chúng ta có thể thu được bit tiếp theo của $x$, và cuối cùng khôi phục được tất cả các bit của nó.

## Tài liệu tham khảo

* [M30, Hans Petter Selasky, 2009](https://ia601602.us.archive.org/29/items/B-001-001-251/B-001-001-251.pdf#page=640)
