---
tags:
  - Original
lang: vi
---
# Phương pháp ngăn và bi (Stars and bars)

Phương pháp ngăn và bi (Stars and bars) là một kỹ thuật toán học dùng để giải các bài toán tổ hợp nhất định.
Nó xuất hiện bất cứ khi nào bạn muốn đếm số cách nhóm các đối tượng giống hệt nhau.

## Định lý

Số cách đặt $n$ đối tượng giống hệt nhau vào $k$ chiếc hộp có nhãn là

$$\binom{n + k - 1}{n}.$$

Chứng minh liên quan đến việc biến các đối tượng thành các ngôi sao và tách các hộp bằng các thanh (do đó có tên gọi này).
Ví dụ: ta có thể biểu diễn bằng $\bigstar | \bigstar \bigstar |~| \bigstar \bigstar$ tình huống sau:
trong hộp thứ nhất có một đối tượng, trong hộp thứ hai có hai đối tượng, hộp thứ ba trống và hộp cuối cùng có hai đối tượng.
Đây là một cách chia 5 đối tượng vào 4 hộp.

Có thể thấy khá rõ ràng rằng mọi cách phân chia đều có thể được biểu diễn bằng $n$ ngôi sao và $k - 1$ thanh, và mọi hoán vị ngăn-và-bi sử dụng $n$ ngôi sao và $k - 1$ thanh đều biểu diễn một cách phân chia.
Do đó, số cách chia $n$ đối tượng giống hệt nhau vào $k$ hộp có nhãn cũng bằng số hoán vị của $n$ ngôi sao và $k - 1$ thanh.
[Hệ số nhị thức (Binomial Coefficient)](binomial-coefficients.md) cho chúng ta công thức mong muốn.

## Số lượng nghiệm nguyên không âm của phương trình

Bài toán này là một ứng dụng trực tiếp của định lý.

Bạn muốn đếm số lượng nghiệm của phương trình

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge 0$.

Một lần nữa, chúng ta có thể biểu diễn một nghiệm bằng phương pháp ngăn và bi.
Ví dụ: nghiệm $1 + 3 + 0 = 4$ cho $n = 4$, $k = 3$ có thể được biểu diễn bằng $\bigstar | \bigstar \bigstar \bigstar |$.

Dễ thấy rằng đây chính xác là định lý ngăn và bi.
Do đó, kết quả là $\binom{n + k - 1}{n}$.

## Số lượng nghiệm nguyên dương của phương trình

Định lý thứ hai cung cấp một cách diễn giải hay cho các số nguyên dương. Xét các nghiệm của

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge 1$.

Chúng ta có thể xét $n$ ngôi sao, nhưng lần này ta có thể đặt tối đa *một thanh* giữa các ngôi sao, vì hai thanh giữa các ngôi sao sẽ biểu diễn $x_i=0$, tức là một hộp trống.
Có $n-1$ khoảng trống giữa các ngôi sao để đặt $k-1$ thanh, vì vậy kết quả là $\binom{n-1}{k-1}$.

## Số lượng nghiệm nguyên với chặn dưới

Kỹ thuật này có thể dễ dàng mở rộng cho các bài toán tổng với các chặn dưới khác nhau.
Tức là, chúng ta muốn đếm số lượng nghiệm cho phương trình

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge a_i$.

Sau khi thay thế $x_i' := x_i - a_i$, ta nhận được phương trình đã sửa đổi

$$(x_1' + a_i) + (x_2' + a_i) + \dots + (x_k' + a_k) = n$$

$$\Leftrightarrow ~ ~ x_1' + x_2' + \dots + x_k' = n - a_1 - a_2 - \dots - a_k$$

với $x_i' \ge 0$.
Vì vậy, chúng ta đã đưa bài toán về trường hợp đơn giản hơn với $x_i' \ge 0$ và có thể áp dụng lại định lý ngăn và bi.

## Số lượng nghiệm nguyên với chặn trên

Với sự trợ giúp của [Nguyên lý bù trừ (Inclusion-Exclusion Principle)](./inclusion-exclusion.md), bạn cũng có thể giới hạn các số nguyên bằng các chặn trên.
Xem phần [Số lượng nghiệm nguyên với chặn trên](./inclusion-exclusion.md#number-of-upper-bound-integer-sums) trong bài viết tương ứng.

## Bài tập thực hành

* [Codeforces - Array](https://codeforces.com/contest/57/problem/C)
* [Codeforces - Kyoya and Coloured Balls](https://codeforces.com/problemset/problem/553/A)
* [Codeforces - Colorful Bricks](https://codeforces.com/contest/1081/problem/C)
* [Codeforces - Two Arrays](https://codeforces.com/problemset/problem/1288/C)
* [Codeforces - One-Dimensional Puzzle](https://codeforces.com/contest/1931/problem/G)