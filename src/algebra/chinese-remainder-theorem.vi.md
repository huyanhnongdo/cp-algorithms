---
tags:
  - Translated
e_maxx_link: chinese_theorem
lang: vi
---

# Định lý thặng dư Trung Hoa (Chinese Remainder Theorem)

Định lý thặng dư Trung Hoa (trong phần còn lại của bài viết sẽ được viết tắt là CRT) được phát hiện bởi nhà toán học Trung Quốc Tôn Tử.

## Phát biểu định lý

Gọi $m = m_1 \cdot m_2 \cdots m_k$, trong đó các số $m_i$ nguyên tố cùng nhau đôi một. Ngoài các số $m_i$, chúng ta cũng được cho một hệ phương trình đồng dư:

$$\left\{\begin{array}{rcl}
    a & \equiv & a_1 \pmod{m_1} \\
    a & \equiv & a_2 \pmod{m_2} \\
      & \vdots & \\
    a & \equiv & a_k \pmod{m_k}
\end{array}\right.$$

với $a_i$ là các hằng số cho trước. Định lý thặng dư Trung Hoa phát biểu rằng hệ phương trình đồng dư trên luôn có *một và chỉ một* nghiệm duy nhất theo mô-đun $m$.

Ví dụ, hệ phương trình đồng dư:

$$\left\{\begin{array}{rcl}
    a & \equiv & 2 \pmod{3} \\
    a & \equiv & 3 \pmod{5} \\
    a & \equiv & 2 \pmod{7}
\end{array}\right.$$

có nghiệm là $23$ theo mô-đun $105$, bởi vì $23 \bmod{3} = 2$, $23 \bmod{5} = 3$ và $23 \bmod{7} = 2$.
Chúng ta có thể biểu diễn tất cả các nghiệm dưới dạng $23 + 105\cdot k$ với $k \in \mathbb{Z}$.

### Hệ quả

Một hệ quả trực tiếp của CRT là phương trình:

$$x \equiv a \pmod{m}$$

tương đương với hệ phương trình:

$$\left\{\begin{array}{rcl}
    x & \equiv & a_1 \pmod{m_1} \\
      & \vdots & \\
    x & \equiv & a_k \pmod{m_k}
\end{array}\right.$$

(Trong đó, giả sử rằng $m = m_1 m_2 \cdots m_k$ và các số $m_i$ nguyên tố cùng nhau đôi một).

## Giải quyết cho trường hợp hai mô-đun

Xét hệ gồm hai phương trình với $m_1, m_2$ nguyên tố cùng nhau:

$$
\left\{\begin{align}
    a &\equiv a_1 \pmod{m_1} \\
    a &\equiv a_2 \pmod{m_2} \\
\end{align}\right.
$$

Chúng ta muốn tìm nghiệm $a \pmod{m_1 m_2}$. Sử dụng [Thuật toán Euclid mở rộng](extended-euclid-algorithm.md), chúng ta có thể tìm các hệ số Bézout $n_1, n_2$ thỏa mãn:

$$n_1 m_1 + n_2 m_2 = 1.$$

Thực tế, $n_1$ và $n_2$ chính là các [nghịch đảo mô-đun](module-inverse.md) của $m_1$ và $m_2$ tương ứng theo mô-đun $m_2$ và $m_1$.
Ta có $n_1 m_1 \equiv 1 \pmod{m_2}$ nên $n_1 \equiv m_1^{-1} \pmod{m_2}$, và ngược lại $n_2 \equiv m_2^{-1} \pmod{m_1}$.

Với hai hệ số này, chúng ta có thể xác định công thức nghiệm:

$$a = a_1 n_2 m_2 + a_2 n_1 m_1 \bmod{m_1 m_2}$$

Dễ dàng kiểm tra đây thực sự là nghiệm bằng cách tính $a \bmod{m_1}$ và $a \bmod{m_2}$:

$$
\begin{array}{rcll}
a & \equiv & a_1 n_2 m_2 + a_2 n_1 m_1 & \pmod{m_1}\\
  & \equiv & a_1 (1 - n_1 m_1) + a_2 n_1 m_1 & \pmod{m_1}\\
  & \equiv & a_1 - a_1 n_1 m_1 + a_2 n_1 m_1 & \pmod{m_1}\\
  & \equiv & a_1 & \pmod{m_1}
\end{array}
$$

Chú ý rằng Định lý thặng dư Trung Hoa cũng đảm bảo chỉ có duy nhất 1 nghiệm tồn tại theo mô-đun $m_1 m_2$. Điều này rất dễ chứng minh.

Giả sử chúng ta có hai nghiệm khác nhau là $x$ và $y$.
Vì $x \equiv a_i \pmod{m_i}$ và $y \equiv a_i \pmod{m_i}$, suy ra $x − y \equiv 0 \pmod{m_i}$ với mọi $i$. Do đó $x − y \equiv 0 \pmod{m_1 m_2}$, hay tương đương $x \equiv y \pmod{m_1 m_2}$.
Vì vậy $x$ và $y$ thực chất là cùng một nghiệm.

## Giải quyết cho trường hợp tổng quát

### Giải bằng quy nạp

Vì $m_1 m_2$ nguyên tố cùng nhau với $m_3$, chúng ta có thể áp dụng lặp đi lặp lại một cách quy nạp thuật toán cho hai mô-đun để giải quyết hệ nhiều mô-đun.
Đầu tiên bạn tính $b_2 := a \pmod{m_1 m_2}$ sử dụng hai phương trình đồng dư đầu tiên. Sau đó, bạn tính tiếp $b_3 := a \pmod{m_1 m_2 m_3}$ từ hai phương trình $a \equiv b_2 \pmod{m_1 m_2}$ và $a \equiv a_3 \pmod {m_3}$, v.v.

### Xây dựng trực tiếp

Chúng ta cũng có thể xây dựng nghiệm trực tiếp tương tự như công thức nội suy Lagrange.

Đặt $M_i := \prod_{i \neq j} m_j$ là tích của tất cả các mô-đun ngoại trừ $m_i$, và $N_i$ là nghịch đảo mô-đun $N_i := M_i^{-1} \bmod{m_i}$.
Khi đó, nghiệm của hệ phương trình đồng dư là:

$$a \equiv \sum_{i=1}^k a_i M_i N_i \pmod{m_1 m_2 \cdots m_k}$$

Chúng ta có thể kiểm chứng đây là nghiệm đúng bằng cách tính $a \bmod{m_i}$ với mỗi $i$. Do $M_j$ chia hết cho $m_i$ với mọi $i \neq j$, ta có:

$$\begin{array}{rcll}
a & \equiv & \sum_{j=1}^k a_j M_j N_j & \pmod{m_i} \\
  & \equiv & a_i M_i N_i              & \pmod{m_i} \\
  & \equiv & a_i M_i M_i^{-1}         & \pmod{m_i} \\
  & \equiv & a_i                      & \pmod{m_i}
\end{array}$$

### Cài đặt

```{.cpp file=chinese_remainder_theorem}
struct Congruence {
    long long a, m;
};

long long chinese_remainder_theorem(vector<Congruence> const& congruences) {
    long long M = 1;
    for (auto const& congruence : congruences) {
        M *= congruence.m;
    }

    long long solution = 0;
    for (auto const& congruence : congruences) {
        long long a_i = congruence.a;
        long long M_i = M / congruence.m;
        long long N_i = mod_inv(M_i, congruence.m);
        solution = (solution + a_i * M_i % M * N_i) % M;
    }
    return solution;
}
```

## Giải quyết cho trường hợp các mô-đun không nguyên tố cùng nhau

Như đã đề cập, thuật toán trên chỉ hoạt động khi các mô-đun $m_1, m_2, \dots m_k$ nguyên tố cùng nhau đôi một.

Trong trường hợp chúng không nguyên tố cùng nhau, một hệ phương trình đồng dư có thể có đúng một nghiệm theo mô-đun $\text{lcm}(m_1, m_2, \dots, m_k)$, hoặc hoàn toàn vô nghiệm.

Ví dụ, trong hệ phương trình dưới đây, phương trình đầu tiên yêu cầu nghiệm phải là số lẻ, còn phương trình thứ hai yêu cầu nghiệm phải là số chẵn. Một số không thể vừa lẻ vừa chẵn, do đó hệ phương trình rõ ràng vô nghiệm.

$$\left\{\begin{align}
    a & \equiv 1 \pmod{4} \\
    a & \equiv 2 \pmod{6}
\end{align}\right.$$

Việc xác định xem một hệ phương trình có nghiệm hay không khá đơn giản. Và nếu hệ có nghiệm, chúng ta có thể biến đổi hệ ban đầu để áp dụng thuật toán chuẩn.

Một phương trình đồng dư $a \equiv a_i \pmod{m_i}$ tương đương với hệ gồm nhiều phương trình đồng dư dạng $a \equiv a_i \pmod{p_j^{n_j}}$, trong đó $p_1^{n_1} p_2^{n_2}\cdots p_k^{n_k}$ là phân tích thừa số nguyên tố của $m_i$.

Dựa vào tính chất này, chúng ta có thể phân tách hệ phương trình ban đầu thành một hệ mới chỉ chứa các mô-đun là lũy thừa số nguyên tố.
Ví dụ hệ phương trình trên tương đương với:

$$\left\{\begin{array//t}
    a \equiv 1          & \pmod{4} \\
    a \equiv 2 \equiv 0 & \pmod{2} \\
    a \equiv 2          & \pmod{3}
\end{array}\right.$$

Do ban đầu một số mô-đun có chung ước số, chúng ta sẽ nhận được một vài phương trình đồng dư có chung cơ số số nguyên tố, tuy nhiên có thể khác nhau về số mũ (lũy thừa).

Dễ thấy rằng, phương trình đồng dư với mô-đun là lũy thừa số nguyên tố cao nhất sẽ là phương trình chặt chẽ nhất trong số các phương trình có cùng cơ số nguyên tố đó.
Nó sẽ mâu thuẫn với các phương trình còn lại, hoặc nó sẽ bao hàm tất cả các phương trình còn lại.

Trong ví dụ của chúng ta, phương trình thứ nhất $a \equiv 1 \pmod{4}$ kéo theo $a \equiv 1 \pmod{2}$, và điều này trực tiếp mâu thuẫn với phương trình thứ hai $a \equiv 0 \pmod{2}$. Do đó hệ phương trình này vô nghiệm.

Nếu không có bất kỳ mâu thuẫn nào xảy ra, hệ phương trình sẽ có nghiệm. Chúng ta chỉ cần giữ lại các phương trình đồng dư ứng với lũy thừa số nguyên tố cao nhất của mỗi số nguyên tố và bỏ qua các phương trình còn lại. Các mô-đun giữ lại này đôi một nguyên tố cùng nhau, và chúng ta có thể giải hệ mới bằng thuật toán thông thường đã mô tả ở trên.

Ví dụ, hệ phương trình dưới đây có nghiệm theo mô-đun $\text{lcm}(10, 12) = 60$:

$$\left\{\begin{align}
    a & \equiv 3 \pmod{10} \\
    a & \equiv 5 \pmod{12}
\end{align}\right.$$

Hệ trên tương đương với hệ các phương trình đồng dư sau:

$$\left\{\begin{align}
    a & \equiv 3 \equiv 1 \pmod{2} \\
    a & \equiv 3 \equiv 3 \pmod{5} \\
    a & \equiv 5 \equiv 1 \pmod{4} \\
    a & \equiv 5 \equiv 2 \pmod{3}
\end{align}\right.$$

Các phương trình có chung cơ số nguyên tố là $a \equiv 1 \pmod{4}$ và $a \equiv 1 \pmod{2}$.
Phương trình thứ nhất đã bao hàm phương trình thứ hai, nên chúng ta có thể bỏ qua phương trình thứ hai. Hệ rút gọn với các mô-đun nguyên tố cùng nhau là:

$$\left\{\begin{align}
    a & \equiv 3 \equiv 3 \pmod{5} \\
    a & \equiv 5 \equiv 1 \pmod{4} \\
    a & \equiv 5 \equiv 2 \pmod{3}
\end{align}\right.$$

Hệ này có nghiệm là $53 \pmod{60}$, và thực sự ta có $53 \bmod{10} = 3$ và $53 \bmod{12} = 5$.

## Thuật toán Garner (Garner's Algorithm)

Một ứng dụng khác của CRT là chúng ta có thể biểu diễn các số lớn bằng một mảng gồm các số nguyên nhỏ.

Thay vì thực hiện các phép toán phức tạp trên các số cực kỳ lớn (chẳng hạn như chia các số có 1000 chữ số), bạn có thể chọn một bộ các mô-đun nguyên tố cùng nhau đôi một, biểu diễn số lớn dưới dạng một hệ phương trình đồng dư, và thực hiện mọi phép toán trên hệ phương trình này.
Bất kỳ số $a$ nào nhỏ hơn $m_1 m_2 \cdots m_k$ đều có thể được đại diện bằng một mảng $a_1, \ldots, a_k$, trong đó $a \equiv a_i \pmod{m_i}$.

Bằng cách sử dụng thuật toán ở trên, bạn có thể tái dựng lại số lớn ban đầu bất cứ khi nào cần thiết.

Ngoài ra, bạn cũng có thể biểu diễn số đó dưới dạng **hệ cơ số hỗn hợp (mixed radix)**:

$$a = x_1 + x_2 m_1 + x_3 m_1 m_2 + \ldots + x_k m_1 \cdots m_{k-1} \text{ với } x_i \in [0, m_i)$$

Thuật toán Garner, được mô tả chi tiết trong bài viết riêng [Thuật toán Garner](garners-algorithm.md), tính toán các hệ số $x_i$ này. Dựa vào các hệ số đó, bạn có thể khôi phục lại hoàn chỉnh số ban đầu.

## Bài tập áp dụng:

* [Google Code Jam - Golf Gophers](https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/round_1a/golf_gophers/statement.pdf)
* [Hackerrank - Number of sequences](https://www.hackerrank.com/contests/w22/challenges/number-of-sequences)
* [Codeforces - Remainders Game](http://codeforces.com/problemset/problem/687/B)
