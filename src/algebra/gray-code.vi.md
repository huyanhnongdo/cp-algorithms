---
tags:
  - Translated
e_maxx_link: gray_code
lang: vi
---

# Mã Gray (Gray code)

Mã Gray là một hệ đếm nhị phân trong đó hai giá trị liên tiếp chỉ khác nhau ở đúng một bit.

Ký hiệu $G(n)$ là biểu diễn của số $n$ bằng mã Gray. Dãy mã Gray cho các số 3-bit là: 000, 001, 011, 010, 110, 111, 101, 100, do đó ta có $G(4) = (110)_2 = 6$.
Ví dụ, $G(3) = (010)_2$ và $G(4) = (110)_2$ chỉ khác nhau ở đúng một bit (bit bên trái nhất). Tương tự, $G(4) = 110$ và $G(5) = (111)_2$ chỉ khác nhau ở đúng một bit (bit bên phải nhất). Điều này luôn đúng với mọi cặp số liên tiếp.

Mã này được phát minh bởi Frank Gray vào năm 1953.

## Tìm mã Gray của một số

Chúng ta hãy xem xét các bit của số $n$ và các bit của số $G(n)$. Nhận thấy rằng bit thứ $i$ của $G(n)$ bằng 1 khi và chỉ khi bit thứ $i$ của $n$ bằng 1 và bit thứ $i + 1$ bằng 0, hoặc ngược lại (bit thứ $i$ bằng 0 và bit thứ $i + 1$ bằng 1). Do đó, ta có công thức chuyển đổi $G(n) = n \oplus (n >> 1)$:

```cpp
int g (int n) {
    return n ^ (n >> 1);
}
```

## Chuyển đổi ngược mã Gray

Cho trước mã Gray $g$, khôi phục lại số ban đầu $n$.

Chúng ta sẽ duyệt từ các bit có ý nghĩa lớn nhất đến các bit có ý nghĩa nhỏ nhất (bit nhỏ nhất có chỉ số 1 và bit lớn nhất có chỉ số $k$). Mối liên hệ giữa các bit $n_i$ của số $n$ và các bit $g_i$ của số $g$ như sau:

$$\begin{align}
  n_k &= g_k, \\
  n_{k-1} &= g_{k-1} \oplus n_k = g_k \oplus g_{k-1}, \\
  n_{k-2} &= g_{k-2} \oplus n_{k-1} = g_k \oplus g_{k-1} \oplus g_{k-2}, \\
  n_{k-3} &= g_{k-3} \oplus n_{k-2} = g_k \oplus g_{k-1} \oplus g_{k-2} \oplus g_{k-3},
  \vdots
\end{align}$$

Cách đơn giản nhất để biểu diễn thuật toán này bằng mã nguồn là:

```cpp
int rev_g (int g) {
  int n = 0;
  for (; g; g >>= 1)
    n ^= g;
  return n;
}
```

## Ứng dụng thực tế

Mã Gray có một số ứng dụng rất hữu ích, đôi khi khá bất ngờ:

*   Mã Gray của $n$ bit tạo thành một chu trình Hamilton trên một khối lập phương đa chiều (hypercube) $n$ chiều, trong đó mỗi bit tương ứng với một chiều không gian.

*   Mã Gray được sử dụng để giảm thiểu sai số trong quá trình chuyển đổi tín hiệu số sang tương tự (DAC) (ví dụ trong các cảm biến vị trí dạng quay).

*   Mã Gray có thể được sử dụng để giải bài toán Tháp Hà Nội.
    Gọi $n$ là số đĩa. Bắt đầu với mã Gray độ dài $n$ gồm toàn số 0 ($G(0)$) và chuyển đổi liên tiếp giữa các mã Gray (từ $G(i)$ sang $G(i+1)$).
    Coi bit thứ $i$ của mã Gray hiện tại đại diện cho đĩa thứ $n$
    (bit có ý nghĩa nhỏ nhất tương ứng với đĩa nhỏ nhất và bit có ý nghĩa lớn nhất tương ứng với đĩa lớn nhất).
    Vì chỉ có đúng một bit thay đổi ở mỗi bước, chúng ta coi việc thay đổi bit thứ $i$ tương đương với việc di chuyển đĩa thứ $i$.
    Chú ý rằng có đúng một phương án di chuyển đĩa hợp lệ cho mỗi đĩa (ngoại trừ đĩa nhỏ nhất) tại mỗi bước (ngoại trừ vị trí xuất phát và đích).
    Luôn có hai phương án di chuyển cho đĩa nhỏ nhất, nhưng ta có một chiến thuật di chuyển luôn dẫn đến đáp án đúng:
    nếu $n$ là số lẻ, chuỗi di chuyển của đĩa nhỏ nhất sẽ tuân theo quy luật $f \to t \to r \to f \to t \to r \to ...$
    (với $f$ là cọc xuất phát, $t$ là cọc đích và $r$ là cọc trung gian còn lại), và
    nếu $n$ là số chẵn: $f \to r \to t \to f \to r \to t \to ...$.

*   Mã Gray cũng được sử dụng trong lý thuyết của các thuật toán di truyền (genetic algorithms).

## Bài tập áp dụng

*   <a href="https://cses.fi/problemset/task/2205">Gray Code &nbsp;&nbsp;&nbsp;&nbsp; [Độ khó: dễ]</a>
*   <a href="http://codeforces.com/problemsets/acmsguru/problem/99999/249">SGU #249 <b>"Matrix"</b> &nbsp;&nbsp;&nbsp;&nbsp; [Độ khó: trung bình]</a>
