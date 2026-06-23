---
tags:
  - Translated
e_maxx_link: circle_line_intersection
lang: vi
---
# Giao điểm giữa đường tròn và đường thẳng

Cho tọa độ tâm của một đường tròn (Circle) và bán kính của nó, cùng với phương trình của một đường thẳng (Line), bạn được yêu cầu tìm các điểm giao (Intersection).

## Lời giải

Thay vì giải hệ hai phương trình, chúng ta sẽ tiếp cận bài toán theo hình học. Bằng cách này, chúng ta sẽ có được một lời giải chính xác hơn về mặt độ ổn định số học (numerical stability).

Chúng ta giả sử không mất tính tổng quát rằng đường tròn có tâm tại gốc tọa độ. Nếu không, chúng ta tịnh tiến nó đến đó và điều chỉnh hằng số $C$ trong phương trình đường thẳng. Như vậy, chúng ta có một đường tròn tâm tại $(0,0)$ với bán kính $r$ và một đường thẳng có phương trình $Ax+By+C=0$.

Hãy bắt đầu bằng cách tìm điểm trên đường thẳng gần gốc tọa độ nhất $(x_0, y_0)$. Thứ nhất, nó phải nằm ở một khoảng cách

$$ d_0 = \frac{|C|}{\sqrt{A^2+B^2}} $$

Thứ hai, vì vector $(A, B)$ vuông góc với đường thẳng, tọa độ của điểm phải tỉ lệ với tọa độ của vector này. Vì chúng ta biết khoảng cách từ điểm đến gốc tọa độ, chúng ta chỉ cần tỉ lệ (scale) vector $(A, B)$ đến độ dài này, và chúng ta sẽ có:

$$\begin{align}
x_0 &= - \frac{AC}{A^2 + B^2} \\
y_0 &= - \frac{BC}{A^2 + B^2} 
\end{align}$$

Các dấu trừ không hiển nhiên, nhưng chúng có thể dễ dàng kiểm chứng bằng cách thay thế $x_0$ và $y_0$ vào phương trình của đường thẳng.

Ở giai đoạn này, chúng ta có thể xác định số điểm giao, và thậm chí tìm lời giải khi có một hoặc không có điểm nào. Thật vậy, nếu khoảng cách từ $(x_0, y_0)$ đến gốc tọa độ $d_0$ lớn hơn bán kính $r$, kết quả là **không điểm**. Nếu $d_0=r$, kết quả là **một điểm** $(x_0, y_0)$. Nếu $d_0<r$, có hai điểm giao, và bây giờ chúng ta phải tìm tọa độ của chúng.

Vậy, chúng ta biết rằng điểm $(x_0, y_0)$ nằm bên trong đường tròn. Hai điểm giao, $(a_x, a_y)$ và $(b_x, b_y)$, phải thuộc đường thẳng $Ax+By+C=0$ và phải cách $(x_0, y_0)$ cùng một khoảng cách $d$, và khoảng cách này rất dễ tìm:

$$ d = \sqrt{r^2 - \frac{C^2}{A^2 + B^2}} $$

Lưu ý rằng vector $(-B, A)$ cùng phương với đường thẳng, và do đó chúng ta có thể tìm các điểm được đề cập bằng cách cộng và trừ vector $(-B,A)$, đã được tỉ lệ đến độ dài $d$, vào điểm $(x_0, y_0)$.

Cuối cùng, tọa độ của hai điểm giao là:

$$\begin{align}
m &= \sqrt{\frac{d^2}{A^2 + B^2}} \\
a_x &= x_0 + B \cdot m, a_y = y_0 - A \cdot m \\
b_x &= x_0 - B \cdot m, b_y = y_0 + A \cdot m
\end{align}$$

Nếu chúng ta giải hệ phương trình ban đầu bằng các phương pháp đại số, chúng ta có khả năng nhận được kết quả dưới dạng khác với sai số lớn hơn. Phương pháp hình học được mô tả ở đây trực quan và chính xác hơn.

## Cài đặt

Như đã chỉ ra lúc đầu, chúng ta giả sử rằng đường tròn có tâm tại gốc tọa độ, và do đó đầu vào (Input) của chương trình là bán kính `r` $r$ của đường tròn và các tham số `a`, `b` $A$, $B$ và `c` $C$ của phương trình đường thẳng.

```cpp
double r, a, b, c; // given as input
double x0 = -a*c/(a*a+b*b), y0 = -b*c/(a*a+b*b);
if (c*c > r*r*(a*a+b*b)+EPS)
    puts ("no points");
else if (abs (c*c - r*r*(a*a+b*b)) < EPS) {
    puts ("1 point");
    cout << x0 << ' ' << y0 << '\n';
}
else {
    double d = r*r - c*c/(a*a+b*b);
    double mult = sqrt (d / (a*a+b*b));
    double ax, ay, bx, by;
    ax = x0 + b * mult;
    bx = x0 - b * mult;
    ay = y0 - a * mult;
    by = y0 + a * mult;
    puts ("2 points");
    cout << ax << ' ' << ay << '\n' << bx << ' ' << by << '\n';
}
```

## Bài toán thực hành

- [CODECHEF: ANDOOR](https://www.codechef.com/problems/ANDOOR)