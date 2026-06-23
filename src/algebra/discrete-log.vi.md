---
tags:
  - Translated
e_maxx_link: discrete_log
---

# Logarit rời rạc

Logarit rời rạc là một số nguyên $x$ thỏa mãn phương trình

$$a^x \equiv b \pmod m$$

với các số nguyên $a$, $b$ và $m$ cho trước.

Logarit rời rạc không phải lúc nào cũng tồn tại, ví dụ như không có nghiệm cho phương trình $2^x \equiv 3 \pmod 7$. Không có điều kiện đơn giản nào để xác định xem logarit rời rạc có tồn tại hay không.

Trong bài viết này, chúng tôi mô tả thuật toán **Baby-step giant-step** (thuật toán chia căn / từng bước nhỏ từng bước lớn), một thuật toán tính logarit rời rạc được đề xuất bởi Shanks vào năm 1971, có độ phức tạp thời gian là $O(\sqrt{m})$. Đây là một thuật toán **meet-in-the-middle** (thuật toán gặp nhau ở giữa) vì nó sử dụng kỹ thuật chia đôi tác vụ.

## Thuật toán

Xét phương trình:

$$a^x \equiv b \pmod m,$$

trong đó $a$ và $m$ là nguyên tố cùng nhau.

Đặt $x = np - q$, với $n$ là một hằng số được chọn trước (chúng ta sẽ mô tả cách chọn $n$ sau). $p$ được gọi là **bước lớn (giant step)**, vì việc tăng nó lên một đơn vị sẽ làm $x$ tăng thêm $n$. Tương tự, $q$ được gọi là **bước nhỏ (baby step)**.

Rõ ràng, bất kỳ số $x$ nào trong khoảng $[0; m)$ đều có thể được biểu diễn dưới dạng này, với $p \in [1; \lceil \frac{m}{n} \rceil ]$ và $q \in [0; n]$.

Khi đó, phương trình trở thành:

$$a^{np - q} \equiv b \pmod m.$$

Sử dụng tính chất $a$ và $m$ nguyên tố cùng nhau, chúng ta thu được:

$$a^{np} \equiv ba^q \pmod m$$

Phương trình mới này có thể được viết lại dưới dạng đơn giản hóa:

$$f_1(p) = f_2(q).$$

Bài toán này có thể được giải quyết bằng phương pháp meet-in-the-middle như sau:

* Tính $f_1$ cho tất cả các đối số $p$ có thể. Sắp xếp mảng gồm các cặp giá trị-đối số.
* Với tất cả các đối số $q$ có thể, tính $f_2$ và tìm $p$ tương ứng trong mảng đã sắp xếp bằng cách sử dụng tìm kiếm nhị phân.

## Độ phức tạp

Chúng ta có thể tính $f_1(p)$ trong $O(\log m)$ bằng cách sử dụng [thuật toán lũy thừa nhị phân](binary-exp.md). Tương tự cho $f_2(q)$.

Trong bước đầu tiên của thuật toán, chúng ta cần tính $f_1$ cho mọi đối số $p$ có thể và sau đó sắp xếp các giá trị. Do đó, bước này có độ phức tạp là:

$$O\left(\left\lceil \frac{m}{n} \right\rceil \left(\log m + \log \left\lceil \frac{m}{n} \right\rceil \right)\right) = O\left( \left\lceil \frac {m}{n} \right\rceil \log m\right)$$

Trong bước thứ hai của thuật toán, chúng ta cần tính $f_2(q)$ cho mọi đối số $q$ có thể và sau đó thực hiện tìm kiếm nhị phân trên mảng các giá trị của $f_1$, do đó bước này có độ phức tạp là:

$$O\left(n \left(\log m + \log \frac{m}{n} \right) \right) = O\left(n \log m\right).$$

Bây giờ, khi cộng hai độ phức tạp này lại, chúng ta thu được $\log m$ nhân với tổng của $n$ và $m/n$, tổng này đạt giá trị nhỏ nhất khi $n = m/n$, nghĩa là để đạt hiệu suất tối ưu, $n$ nên được chọn sao cho:

$$n = \sqrt{m}.$$

Khi đó, độ phức tạp của thuật toán trở thành:

$$O(\sqrt {m} \log m).$$

## Cài đặt

### Cài đặt đơn giản nhất

Trong đoạn mã sau, hàm `powmod` tính $a^b \pmod m$ và hàm `solve` tìm một nghiệm phù hợp cho bài toán.
Nó trả về $-1$ nếu không có nghiệm và trả về một trong các nghiệm có thể có nếu ngược lại.

```cpp
int powmod(int a, int b, int m) {
    int res = 1;
    while (b > 0) {
        if (b & 1) {
            res = (res * 1ll * a) % m;
        }
        a = (a * 1ll * a) % m;
        b >>= 1;
    }
    return res;
}

int solve(int a, int b, int m) {
    a %= m, b %= m;
    int n = sqrt(m) + 1;
    map<int, int> vals;
    for (int p = 1; p <= n; ++p)
        vals[powmod(a, p * n, m)] = p;
    for (int q = 0; q <= n; ++q) {
        int cur = (powmod(a, q, m) * 1ll * b) % m;
        if (vals.count(cur)) {
            int ans = vals[cur] * n - q;
            return ans;
        }
    }
    return -1;
}
```

Trong đoạn mã này, chúng ta sử dụng `map` từ thư viện tiêu chuẩn C++ để lưu trữ các giá trị của $f_1$.
Bên trong, `map` sử dụng cây đỏ-đen để lưu trữ giá trị.
Do đó, đoạn mã này chạy chậm hơn một chút so với việc sử dụng mảng và tìm kiếm nhị phân, nhưng viết dễ hơn nhiều.

Lưu ý rằng đoạn mã của chúng tôi giả định $0^0 = 1$, tức là đoạn mã sẽ tính $0$ làm nghiệm cho phương trình $0^x \equiv 1 \pmod m$ và cũng làm nghiệm cho phương trình $0^x \equiv 0 \pmod 1$.
Đây là một quy ước thường được sử dụng trong đại số, nhưng nó không được chấp nhận rộng rãi trong tất cả các lĩnh vực.
Đôi khi $0^0$ đơn giản là không xác định.
Nếu bạn không đồng ý với quy ước này, bạn cần xử lý riêng trường hợp $a=0$:

```cpp
    if (a == 0)
        return b == 0 ? 1 : -1;
```

Một điều cần lưu ý khác là nếu có nhiều đối số $p$ ánh xạ tới cùng một giá trị $f_1$, chúng ta chỉ lưu trữ một đối số như vậy.
Điều này hoạt động trong trường hợp này vì chúng ta chỉ muốn trả về một nghiệm có thể.
Nếu cần trả về tất cả các nghiệm có thể có, chúng ta cần thay đổi `map<int, int>` thành, ví dụ, `map<int, vector<int>>`.
Chúng ta cũng cần thay đổi bước thứ hai tương ứng.

## Cài đặt cải tiến

Một cải tiến khả thi là loại bỏ phép lũy thừa nhị phân.
Điều này có thể được thực hiện bằng cách duy trì một biến được nhân với $a$ mỗi khi tăng $q$ và một biến được nhân với $a^n$ mỗi khi tăng $p$.
Với thay đổi này, độ phức tạp của thuật toán vẫn như cũ, nhưng giờ đây hệ số $\log$ chỉ xuất hiện ở `map`.
Thay vì dùng `map`, chúng ta cũng có thể sử dụng bảng băm (`unordered_map` trong C++) vốn có độ phức tạp thời gian trung bình là $O(1)$ cho việc chèn và tìm kiếm.

Các bài toán thường yêu cầu tìm giá trị $x$ nhỏ nhất thỏa mãn phương trình.
Chúng ta có thể tìm tất cả các nghiệm rồi lấy giá trị nhỏ nhất, hoặc rút gọn nghiệm đầu tiên tìm được bằng cách sử dụng [định lý Euler](phi-function.md#application), nhưng chúng ta cũng có thể khôn ngoan điều chỉnh thứ tự tính toán các giá trị để đảm bảo nghiệm đầu tiên tìm được là nghiệm nhỏ nhất.

```{.cpp file=discrete_log}
// Returns minimum x for which a ^ x % m = b % m, a and m are coprime.
int solve(int a, int b, int m) {
    a %= m, b %= m;
    int n = sqrt(m) + 1;

    int an = 1;
    for (int i = 0; i < n; ++i)
        an = (an * 1ll * a) % m;

    unordered_map<int, int> vals;
    for (int q = 0, cur = b; q <= n; ++q) {
        vals[cur] = q;
        cur = (cur * 1ll * a) % m;
    }

    for (int p = 1, cur = 1; p <= n; ++p) {
        cur = (cur * 1ll * an) % m;
        if (vals.count(cur)) {
            int ans = n * p - vals[cur];
            return ans;
        }
    }
    return -1;
}
```

Độ phức tạp là $O(\sqrt{m})$ khi sử dụng `unordered_map`.

## Khi $a$ và $m$ không nguyên tố cùng nhau { data-toc-label='Khi a và m không nguyên tố cùng nhau' }
Gọi $g = \gcd(a, m)$, và $g > 1$. Rõ ràng $a^x \bmod m$ với mọi $x \ge 1$ sẽ chia hết cho $g$.

Nếu $g \nmid b$, không có nghiệm cho $x$.

Nếu $g \mid b$, đặt $a = g \alpha, b = g \beta, m = g \nu$.

$$
\begin{aligned}
a^x & \equiv b \mod m \\\
(g \alpha) a^{x - 1} & \equiv g \beta \mod g \nu \\\
\alpha a^{x-1} & \equiv \beta \mod \nu
\end{aligned}
$$

Thuật toán baby-step giant-step có thể dễ dàng mở rộng để giải phương trình $ka^{x} \equiv b \pmod m$ tìm $x$.

```{.cpp file=discrete_log_extended}
// Returns minimum x for which a ^ x % m = b % m.
int solve(int a, int b, int m) {
    a %= m, b %= m;
    int k = 1, add = 0, g;
    while ((g = gcd(a, m)) > 1) {
        if (b == k)
            return add;
        if (b % g)
            return -1;
        b /= g, m /= g, ++add;
        k = (k * 1ll * a / g) % m;
    }

    int n = sqrt(m) + 1;
    int an = 1;
    for (int i = 0; i < n; ++i)
        an = (an * 1ll * a) % m;

    unordered_map<int, int> vals;
    for (int q = 0, cur = b; q <= n; ++q) {
        vals[cur] = q;
        cur = (cur * 1ll * a) % m;
    }

    for (int p = 1, cur = k; p <= n; ++p) {
        cur = (cur * 1ll * an) % m;
        if (vals.count(cur)) {
            int ans = n * p - vals[cur] + add;
            return ans;
        }
    }
    return -1;
}
```

Độ phức tạp thời gian vẫn là $O(\sqrt{m})$ như trước vì bước rút gọn ban đầu để đưa về $a$ và $m$ nguyên tố cùng nhau được thực hiện trong $O(\log^2 m)$.

## Bài tập luyện tập
* [Spoj - Power Modulo Inverted](http://www.spoj.com/problems/MOD/)
* [Topcoder - SplittingFoxes3](https://community.topcoder.com/stat?c=problem_statement&pm=14386&rd=16801)
* [CodeChef - Inverse of a Function](https://www.codechef.com/problems/INVXOR/)
* [Hard Equation](https://codeforces.com/gym/101853/problem/G) (giả định rằng $0^0$ không xác định)
* [CodeChef - Chef and Modular Sequence](https://www.codechef.com/problems/CHEFMOD)

## Tài liệu tham khảo
* [Wikipedia - Baby-step giant-step](https://en.wikipedia.org/wiki/Baby-step_giant-step)
* [Câu trả lời của Zander trên Mathematics StackExchange](https://math.stackexchange.com/a/133054)
