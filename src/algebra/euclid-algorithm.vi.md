---
tags:
  - Translated
e_maxx_link: euclid_algorithm
lang: vi
---

# Thuật toán Euclid tìm ước chung lớn nhất (greatest common divisor)

Cho hai số nguyên không âm $a$ và $b$, chúng ta cần tìm **ước chung lớn nhất (greatest common divisor - GCD)** của chúng, tức là số lớn nhất là ước của cả $a$ và $b$.
Thông thường nó được ký hiệu là $\gcd(a, b)$. Về mặt toán học, nó được định nghĩa như sau:

$$\gcd(a, b) = \max \{k > 0 : (k \mid a) \text{ and } (k \mid b) \}$$

(ở đây ký hiệu "$\mid$" biểu thị tính chia hết, tức là "$k \mid a$" nghĩa là "$a$ chia hết cho $k$")

Khi một trong hai số bằng không và số còn lại khác không, ước chung lớn nhất của chúng, theo định nghĩa, là số thứ hai. Khi cả hai số đều bằng không, ước chung lớn nhất của chúng không được xác định (nó có thể là bất kỳ số lớn tùy ý nào), nhưng để thuận tiện, chúng ta cũng định nghĩa nó bằng không để bảo toàn tính kết hợp của phép toán $\gcd$. Quy tắc đơn giản là: nếu một trong hai số bằng 0, ước chung lớn nhất là số còn lại.

Thuật toán Euclid, được thảo luận dưới đây, cho phép tìm ước chung lớn nhất của hai số $a$ và $b$ trong thời gian $O(\log \min(a, b))$. Vì hàm này có tính **kết hợp**, để tìm GCD của **nhiều hơn hai số**, chúng ta có thể thực hiện $\gcd(a, b, c) = \gcd(a, \gcd(b, c))$ và tương tự như vậy cho nhiều số hơn.

Thuật toán này lần đầu tiên được mô tả trong cuốn sách "Elements" của Euclid (khoảng năm 300 trước Công nguyên), nhưng có khả năng thuật toán này còn có nguồn gốc sớm hơn thế.

## Thuật toán

Ban đầu, thuật toán Euclid được phát biểu như sau: trừ số nhỏ hơn từ số lớn hơn cho đến khi một trong hai số bằng không. Thực vậy, nếu $g$ chia hết cả $a$ và $b$, thì nó cũng chia hết $a-b$. Ngược lại, nếu $g$ chia hết $a-b$ và $b$, thì nó cũng chia hết $a = b + (a-b)$, điều này có nghĩa là tập hợp các ước chung của $\{a, b\}$ và $\{b, a-b\}$ là trùng nhau.

Lưu ý rằng số $a$ vẫn là số lớn hơn cho đến khi ta trừ $b$ khỏi nó ít nhất $\left\lfloor\frac{a}{b}\right\rfloor$ lần. Do đó, để tăng tốc thuật toán, ta thay thế phép trừ liên tiếp $a-b$ bằng phép chia lấy dư $a-\left\lfloor\frac{a}{b}\right\rfloor b = a \bmod b$. Khi đó, thuật toán được phát biểu một cách cực kỳ đơn giản:

$$\gcd(a, b) = \begin{cases}a,&\text{if }b = 0 \\ \gcd(b, a \bmod b),&\text{otherwise.}\end{cases}$$

## Cài đặt {: #implementation}

```cpp
int gcd (int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd (b, a % b);
}
```

Sử dụng toán tử ba ngôi trong C++, chúng ta có thể viết mã nguồn ngắn gọn trên một dòng:

```cpp
int gcd (int a, int b) {
    return b ? gcd (b, a % b) : a;
}
```

Và cuối cùng, đây là phiên bản cài đặt không sử dụng đệ quy (vòng lặp):

```cpp
int gcd (int a, int b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}
```

Lưu ý rằng kể từ phiên bản C++17, hàm `gcd` đã được cài đặt như một [hàm chuẩn](https://en.cppreference.com/w/cpp/numeric/gcd) của ngôn ngữ C++ trong thư viện `<numeric>`.

## Độ phức tạp thời gian

Thời gian chạy của thuật toán được ước lượng thông qua định lý Lamé, định lý này thiết lập một mối liên hệ đáng ngạc nhiên giữa thuật toán Euclid và dãy số Fibonacci:

Nếu $a > b \geq 1$ và $b < F_n$ với một số nguyên $n$ nào đó, thuật toán Euclid sẽ thực hiện tối đa $n-2$ lời gọi đệ quy.

Hơn nữa, người ta cũng chỉ ra rằng cận trên của định lý này là tối ưu. Khi $a = F_n$ và $b = F_{n-1}$, hàm $gcd(a, b)$ sẽ thực hiện chính xác $n-2$ lời gọi đệ quy. Nói cách khác, hai số Fibonacci liên tiếp chính là bộ dữ liệu đầu vào xấu nhất cho thuật toán Euclid.

Do các số Fibonacci tăng trưởng theo hàm mũ, chúng ta có độ phức tạp thời gian của thuật toán Euclid là $O(\log \min(a, b))$.

Một cách khác để ước lượng độ phức tạp là nhận xét rằng phép toán $a \bmod b$ cho trường hợp $a \geq b$ sẽ cho kết quả nhỏ hơn ít nhất $2$ lần so với $a$, vì thế số lớn hơn sẽ giảm đi ít nhất một nửa sau mỗi vòng lặp của thuật toán. Áp dụng lập luận này cho trường hợp tìm GCD của một tập hợp các số $a_1,\dots,a_n \leq C$, ta cũng có thể ước lượng tổng thời gian chạy là $O(n + \log C)$ thay vì $O(n \log C)$, vì mỗi bước lặp không suy biến của thuật toán sẽ làm giảm ứng viên GCD hiện tại đi ít nhất $2$ lần.

## Bội chung nhỏ nhất (least common multiple)

Tính bội chung nhỏ nhất (thường được ký hiệu là **LCM**) có thể được quy về việc tính GCD thông qua công thức đơn giản sau:

$$\text{lcm}(a, b) = \frac{a \cdot b}{\gcd(a, b)}$$

Vì vậy, LCM có thể được tính toán bằng cách sử dụng thuật toán Euclid với cùng độ phức tạp thời gian.

Dưới đây là một cách cài đặt thông minh giúp tránh tràn số (integer overflow) bằng cách chia $a$ cho ước chung lớn nhất trước khi thực hiện phép nhân với $b$:

```cpp
int lcm (int a, int b) {
    return a / gcd(a, b) * b;
}
```

## Thuật toán GCD nhị phân (Binary GCD)

Thuật toán GCD nhị phân (Binary GCD) là một cải tiến tối ưu cho thuật toán Euclid thông thường.

Phần chạy chậm nhất trong thuật toán thông thường là phép chia lấy dư (phép toán modulo). Phép toán modulo mặc dù có độ phức tạp lý thuyết là $O(1)$ nhưng chạy chậm hơn rất nhiều so với các phép toán cơ bản như cộng, trừ hay các phép toán bitwise. Do đó, việc tránh sử dụng phép toán modulo là rất hữu ích.

Hóa ra, chúng ta có thể thiết kế một thuật toán tìm GCD nhanh mà không cần sử dụng phép chia lấy dư, dựa trên một số tính chất sau:

  - Nếu cả hai số đều chẵn, ta có thể đưa thừa số 2 ra ngoài và tính GCD của hai số còn lại: $\gcd(2a, 2b) = 2 \gcd(a, b)$.
  - Nếu một số chẵn và số kia lẻ, ta có thể bỏ đi thừa số 2 của số chẵn: $\gcd(2a, b) = \gcd(a, b)$ nếu $b$ lẻ.
  - Nếu cả hai số đều lẻ, hiệu của hai số sẽ có ước chung lớn nhất không đổi: $\gcd(a, b) = \gcd(b, a-b)$.

Chỉ sử dụng các tính chất này và một số hàm xử lý bit nhanh từ trình biên dịch GCC, chúng ta có thể cài đặt phiên bản tối ưu như sau:

```cpp
int gcd(int a, int b) {
    if (!a || !b)
        return a | b;
    unsigned shift = __builtin_ctz(a | b);
    a >>= __builtin_ctz(a);
    do {
        b >>= __builtin_ctz(b);
        if (a > b)
            swap(a, b);
        b -= a;
    } while (b);
    return a << shift;
}
```

Cần lưu ý rằng tối ưu hóa này thường không thực sự cần thiết, và hầu hết các ngôn ngữ lập trình hiện đại đều đã tích hợp sẵn hàm tính GCD tối ưu trong thư viện chuẩn của chúng.
Ví dụ: C++17 cung cấp hàm `std::gcd` trong thư viện `<numeric>`.

## Bài tập thực hành

- [CSAcademy - Greatest Common Divisor](https://csacademy.com/contest/archive/task/gcd/)
- [Codeforces 1916B - Two Divisors](https://codeforces.com/contest/1916/problem/B)
