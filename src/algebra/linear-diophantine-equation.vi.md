---
tags:
  - Translated
e_maxx_link: diofant_2_equation
---

# Phương trình Diophantine tuyến tính

Phương trình Diophantine tuyến tính (hai ẩn) là một phương trình có dạng tổng quát:

$$ax + by = c$$

trong đó $a$, $b$, $c$ là các số nguyên cho trước, và $x$, $y$ là các số nguyên chưa biết.

Trong bài viết này, chúng ta xem xét một số bài toán cổ điển liên quan đến các phương trình này:

* Tìm một nghiệm
* Tìm tất cả các nghiệm
* Tìm số lượng nghiệm và chính các nghiệm đó trong một khoảng cho trước
* Tìm nghiệm có tổng $x + y$ nhỏ nhất

## Trường hợp suy biến

Một trường hợp suy biến cần lưu ý là khi $a = b = 0$. Rõ ràng là phương trình sẽ vô nghiệm hoặc có vô số nghiệm, tùy thuộc vào việc $c = 0$ hay không. Trong phần còn lại của bài viết, chúng ta sẽ bỏ qua trường hợp này.

## Nghiệm giải tích

Khi $a \neq 0$ và $b \neq 0$, phương trình $ax+by=c$ có thể được xem xét tương đương với một trong hai phương trình đồng dư sau:

\begin{align}
ax &\equiv c \pmod b \\
by &\equiv c \pmod a
\end{align}

Không mất tính tổng quát, giả sử $b \neq 0$ và xét phương trình thứ nhất. Khi $a$ và $b$ nguyên tố cùng nhau, nghiệm của phương trình đồng dư này là:

$$x \equiv ca^{-1} \pmod b,$$

trong đó $a^{-1}$ là [nghịch đảo mô-đun (modular inverse)](module-inverse.md) của $a$ theo mô-đun $b$.

Khi $a$ và $b$ không nguyên tố cùng nhau, các giá trị của $ax$ theo mô-đun $b$ với mọi số nguyên $x$ đều chia hết cho $g=\gcd(a, b)$, do đó nghiệm chỉ tồn tại khi $c$ chia hết cho $g$. Trong trường hợp này, một nghiệm có thể được tìm thấy bằng cách giản ước phương trình cho $g$:

$$(a/g) x \equiv (c/g) \pmod{b/g}.$$

Theo định nghĩa của $g$, các số $a/g$ and $b/g$ nguyên tố cùng nhau, nên nghiệm có thể được viết rõ ràng là:

$$\begin{cases}
x \equiv (c/g)(a/g)^{-1}\pmod{b/g},\\
y = \frac{c-ax}{b}.
\end{cases}$$

## Thuật toán giải

**Bổ đề Bézout** (hay đồng nhất thức Bézout) là một kết quả hữu ích để hiểu cách giải sau:

> Gọi $g = \gcd(a,b)$. Khi đó tồn tại các số nguyên $x,y$ sao cho $ax + by = g$.
> 
> Hơn nữa, $g$ là số nguyên dương nhỏ nhất có thể biểu diễn dưới dạng $ax + by$; tất cả các số nguyên có dạng $ax + by$ đều là bội số của $g$.

Để tìm một nghiệm của phương trình Diophantine với 2 ẩn, bạn có thể sử dụng [Thuật toán Euclid mở rộng (Extended Euclidean algorithm)](extended-euclid-algorithm.md). Đầu tiên, giả định rằng $a$ and $b$ không âm. Khi áp dụng Thuật toán Euclid mở rộng cho $a$ và $b$, chúng ta có thể tìm được ước chung lớn nhất $g$ của chúng và hai số $x_g$ và $y_g$ sao cho:

$$a x_g + b y_g = g$$

Nếu $c$ chia hết cho $g = \gcd(a, b)$, thì phương trình Diophantine đã cho có nghiệm, ngược lại phương trình vô nghiệm. Việc chứng minh điều này rất trực quan: một tổ hợp tuyến tính của hai số nguyên luôn chia hết cho ước chung của hai số đó.

Bây giờ giả sử $c$ chia hết cho $g$, khi đó ta có:

$$a \cdot x_g \cdot \frac{c}{g} + b \cdot y_g \cdot \frac{c}{g} = c$$

Do đó, một nghiệm của phương trình Diophantine là:

$$x_0 = x_g \cdot \frac{c}{g},$$

$$y_0 = y_g \cdot \frac{c}{g}.$$

Ý tưởng trên vẫn hoạt động khi $a$ hoặc $b$ hoặc cả hai số là số âm. Chúng ta chỉ cần thay đổi dấu của $x_0$ và $y_0$ khi cần thiết.

Cuối cùng, chúng ta có thể cài đặt ý tưởng này như sau (lưu ý rằng đoạn mã này không xét trường hợp $a = b = 0$):

```{.cpp file=linear_diophantine_any}
int gcd(int a, int b, int& x, int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d = gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

bool find_any_solution(int a, int b, int c, int &x0, int &y0, int &g) {
    g = gcd(abs(a), abs(b), x0, y0);
    if (c % g) {
        return false;
    }

    x0 *= c / g;
    y0 *= c / g;
    if (a < 0) x0 = -x0;
    if (b < 0) y0 = -y0;
    return true;
}
```

## Tìm tất cả các nghiệm

Từ một nghiệm $(x_0, y_0)$, chúng ta có thể tìm được tất cả các nghiệm của phương trình đã cho.

Gọi $g = \gcd(a, b)$ và $x_0, y_0$ là các số nguyên thỏa mãn:

$$a \cdot x_0 + b \cdot y_0 = c$$

Bây giờ, chúng ta thấy rằng việc cộng thêm $b / g$ vào $x_0$, đồng thời trừ đi $a / g$ từ $y_0$ sẽ không làm thay đổi đẳng thức:

$$a \cdot \left(x_0 + \frac{b}{g}\right) + b \cdot \left(y_0 - \frac{a}{g}\right) = a \cdot x_0 + b \cdot y_0 + a \cdot \frac{b}{g} - b \cdot \frac{a}{g} = c$$

Rõ ràng, quá trình này có thể được lặp lại, do đó tất cả các số có dạng:

$$x = x_0 + k \cdot \frac{b}{g}$$

$$y = y_0 - k \cdot \frac{a}{g}$$

đều là nghiệm của phương trình Diophantine đã cho.

Vì phương trình là tuyến tính nên tất cả các nghiệm đều nằm trên cùng một đường thẳng, và theo định nghĩa của $g$, đây chính là tập hợp tất cả các nghiệm có thể có của phương trình Diophantine đã cho.

## Tìm số lượng nghiệm và các nghiệm trong một khoảng cho trước

Từ phần trước, rõ ràng nếu chúng ta không đặt bất kỳ giới hạn nào cho các nghiệm thì sẽ có vô số nghiệm. Do đó trong phần này, chúng ta thêm giới hạn cho khoảng của $x$ và $y$, từ đó đếm và liệt kê các nghiệm.

Giả sử có hai khoảng: $[min_x; max_x]$ và $[min_y; max_y]$ và chúng ta chỉ muốn tìm các nghiệm nằm trong hai khoảng này.

Lưu ý rằng nếu $a$ hoặc $b$ bằng $0$, bài toán chỉ có nhiều nhất một nghiệm. Chúng ta không xét trường hợp đó ở đây.

Đầu tiên, chúng ta có thể tìm một nghiệm có giá trị $x$ nhỏ nhất sao cho $x \ge min_x$. Để làm điều này, trước tiên ta tìm một nghiệm bất kỳ của phương trình Diophantine. Sau đó, ta tịnh tiến nghiệm này để có $x \ge min_x$ (sử dụng những gì đã biết về tập nghiệm ở phần trước). Việc này có thể thực hiện trong $O(1)$.
Ký hiệu giá trị $x$ nhỏ nhất này là $l_{x1}$.

Tương tự, chúng ta có thể tìm giá trị lớn nhất của $x$ thỏa mãn $x \le max_x$. Ký hiệu giá trị $x$ lớn nhất này là $r_{x1}$.

Tương tự, chúng ta có thể tìm giá trị $y$ nhỏ nhất $(y \ge min_y)$ và giá trị $y$ lớn nhất $(y \le max_y)$. Ký hiệu các giá trị $x$ tương ứng là $l_{x2}$ và $r_{x2}$.

Tập nghiệm cuối cùng là tất cả các nghiệm có $x$ nằm trong phần giao của $[l_{x1}, r_{x1}]$ và $[l_{x2}, r_{x2}]$. Hãy ký hiệu phần giao này là $[l_x, r_x]$.

Dưới đây là đoạn mã cài đặt ý tưởng này.
Lưu ý rằng chúng ta chia $a$ và $b$ cho $g$ ở ngay đầu hàm.
Vì phương trình $a x + b y = c$ tương đương với phương trình $\frac{a}{g} x + \frac{b}{g} y = \frac{c}{g}$, chúng ta có thể sử dụng phương trình rút gọn này với $\gcd(\frac{a}{g}, \frac{b}{g}) = 1$ để đơn giản hóa các công thức.

```{.cpp file=linear_diophantine_all}
void shift_solution(int & x, int & y, int a, int b, int cnt) {
    x += cnt * b;
    y -= cnt * a;
}

int find_all_solutions(int a, int b, int c, int minx, int maxx, int miny, int maxy) {
    int x, y, g;
    if (!find_any_solution(a, b, c, x, y, g))
        return 0;
    a /= g;
    b /= g;

    int sign_a = a > 0 ? +1 : -1;
    int sign_b = b > 0 ? +1 : -1;

    shift_solution(x, y, a, b, (minx - x) / b);
    if (x < minx)
        shift_solution(x, y, a, b, sign_b);
    if (x > maxx)
        return 0;
    int lx1 = x;

    shift_solution(x, y, a, b, (maxx - x) / b);
    if (x > maxx)
        shift_solution(x, y, a, b, -sign_b);
    int rx1 = x;

    shift_solution(x, y, a, b, -(miny - y) / a);
    if (y < miny)
        shift_solution(x, y, a, b, -sign_a);
    if (y > maxy)
        return 0;
    int lx2 = x;

    shift_solution(x, y, a, b, -(maxy - y) / a);
    if (y > maxy)
        shift_solution(x, y, a, b, sign_a);
    int rx2 = x;

    if (lx2 > rx2)
        swap(lx2, rx2);
    int lx = max(lx1, lx2);
    int rx = min(rx1, rx2);

    if (lx > rx)
        return 0;
    return (rx - lx) / abs(b) + 1;
}
```

Sau khi có $l_x$ và $r_x$, việc liệt kê tất cả các nghiệm là rất đơn giản. Ta chỉ cần duyệt qua $x = l_x + k \cdot \frac{b}{g}$ với mọi $k \ge 0$ cho đến khi $x = r_x$, và tìm các giá trị $y$ tương ứng bằng cách sử dụng phương trình $a x + b y = c$.

## Tìm nghiệm có tổng $x + y$ nhỏ nhất { data-toc-label='Tìm nghiệm có tổng x + y nhỏ nhất' }

Ở đây, $x$ và $y$ cũng cần được giới hạn khoảng giá trị, nếu không kết quả có thể tiến tới âm vô cùng.

Ý tưởng tương tự như phần trước: Chúng ta tìm một nghiệm bất kỳ của phương trình Diophantine, sau đó tịnh tiến nghiệm để thỏa mãn một số điều kiện.

Cuối cùng, sử dụng tính chất của tập nghiệm để tìm giá trị nhỏ nhất:

$$x' = x + k \cdot \frac{b}{g},$$

$$y' = y - k \cdot \frac{a}{g}.$$

Lưu ý rằng $x + y$ thay đổi như sau:

$$x' + y' = x + y + k \cdot \left(\frac{b}{g} - \frac{a}{g}\right) = x + y + k \cdot \frac{b-a}{g}$$

Nếu $a < b$, chúng ta cần chọn giá trị $k$ nhỏ nhất có thể. Nếu $a > b$, chúng ta cần chọn giá trị $k$ lớn nhất có thể. Nếu $a = b$, tất cả các nghiệm đều có cùng tổng $x + y$.

## Bài tập luyện tập

* [Spoj - Crucial Equation](http://www.spoj.com/problems/CEQU/)
* [SGU 106](http://codeforces.com/problemsets/acmsguru/problem/99999/106)
* [Codeforces - Ebony and Ivory](http://codeforces.com/contest/633/problem/A)
* [Codechef - Get AC in one go](https://www.codechef.com/problems/COPR16G)
* [LightOj - Solutions to an equation](http://www.lightoj.com/volume_showproblem.php?problem=1306)
* [Atcoder - F - S = 1](https://atcoder.jp/contests/abc340/tasks/abc340_f)
