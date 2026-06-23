---
tags:
  - Original
lang: vi
---
# Đường tròn bao nhỏ nhất (Minimum Enclosing Circle)

Xét bài toán sau:

!!! example "[Library Checker - Minimum Enclosing Circle](https://judge.yosupo.jp/problem/minimum_enclosing_circle)"

    Cho $n \leq 10^5$ điểm $p_i=(x_i, y_i)$.

    Với mỗi $p_i$, hãy xác định xem nó có nằm trên đường tròn bao nhỏ nhất (Minimum Enclosing Circle - MEC) của $\{p_1,\dots,p_n\}$ hay không.

Ở đây, đường tròn bao nhỏ nhất (MEC) là đường tròn có bán kính nhỏ nhất chứa tất cả $n$ điểm, hoặc nằm bên trong hoặc nằm trên biên của đường tròn. Bài toán này có một lời giải ngẫu nhiên (randomized) đơn giản, thoạt nhìn có vẻ sẽ chạy trong $O(n^3)$, nhưng thực tế có độ phức tạp thời gian kỳ vọng là $O(n)$.

Để hiểu rõ hơn về lập luận dưới đây, chúng ta cần lưu ý ngay rằng nghiệm của bài toán này là duy nhất:

??? question "Tại sao MEC lại duy nhất?"

    Xét thiết lập sau: Giả sử $r$ là bán kính của MEC. Ta vẽ một đường tròn bán kính $r$ quanh mỗi điểm trong $p_1,\dots,p_n$. Về mặt hình học, tâm của các đường tròn có bán kính $r$ bao phủ tất cả các điểm $p_1,\dots,p_n$ chính là giao điểm của tất cả $n$ đường tròn này.

    Nếu giao điểm chỉ là một điểm duy nhất, điều đó chứng minh tính duy nhất. Ngược lại, nếu giao điểm là một hình có diện tích khác không, ta có thể giảm $r$ một chút và vẫn có giao điểm khác rỗng, điều này mâu thuẫn với giả thiết $r$ là bán kính nhỏ nhất có thể.

    Với logic tương tự, ta cũng có thể chứng minh tính duy nhất của MEC nếu thêm điều kiện đường tròn phải đi qua một điểm cụ thể $p_i$ hoặc hai điểm $p_i$ và $p_j$ (nó duy nhất vì bán kính xác định nó một cách duy nhất).

    Cách khác, giả sử có hai MEC khác nhau, ta có thể thấy rằng giao điểm của chúng (đã chứa các điểm $p_1,\dots,p_n$) phải có đường kính nhỏ hơn các đường tròn ban đầu, do đó có thể được bao phủ bởi một đường tròn nhỏ hơn.

## Thuật toán Welzl

Để ngắn gọn, gọi $\operatorname{mec}(p_1,\dots,p_n)$ là MEC của $\{p_1,\dots,p_n\}$, và đặt $P_i = \{p_1,\dots,p_i\}$.

Thuật toán, được Welzl [đề xuất](https://doi.org/10.1007/BFb0038202) lần đầu vào năm 1991, hoạt động như sau:

1. Áp dụng hoán vị ngẫu nhiên cho dãy điểm đầu vào.
2. Duy trì ứng viên hiện tại cho MEC là $C$, bắt đầu với $C = \operatorname{mec}(p_1, p_2)$.
3. Lặp qua $i=3..n$ và kiểm tra nếu $p_i \in C$.
    1. Nếu $p_i \in C$, nghĩa là $C$ là MEC của $P_i$.
    2. Ngược lại, gán $C = \operatorname{mec}(p_i, p_1)$ và lặp qua $j=2..i$ để kiểm tra nếu $p_j \in C$.
        1. Nếu $p_j \in C$, thì $C$ là MEC của $P_j$ trong số các đường tròn đi qua $p_i$.
        2. Ngược lại, gán $C=\operatorname{mec}(p_i, p_j)$ và lặp qua $k=1..j$ để kiểm tra nếu $p_k \in C$.
            1. Nếu $p_k \in C$, thì $C$ là MEC của $P_k$ trong số các đường tròn đi qua $p_i$ và $p_j$.
            2. Ngược lại, $C=\operatorname{mec}(p_i,p_j,p_k)$ là MEC của $P_k$ trong số các đường tròn đi qua $p_i$ và $p_j$.

Ta thấy rằng mỗi tầng lồng nhau ở đây đều duy trì một bất biến (rằng $C$ là MEC trong số các đường tròn đi qua các điểm $0$, $1$ hoặc $2$ bổ sung), và mỗi khi vòng lặp trong kết thúc, bất biến của nó trở nên tương đương với bất biến của vòng lặp cha. Điều này đảm bảo tính *đúng đắn* của toàn bộ thuật toán.

Bỏ qua một vài chi tiết kỹ thuật, toàn bộ thuật toán có thể cài đặt bằng C++ như sau:

```cpp
struct point {...};

// Is represented by 2 or 3 points on its circumference
struct mec {...};

bool inside(mec const& C, point p) {
    return ...;
}

// Choose some good generator of randomness for the shuffle
mt19937_64 gen(...);
mec enclosing_circle(vector<point> &p) {
    int n = p.size();
    ranges::shuffle(p, gen);
    auto C = mec{p[0], p[1]};
    for(int i = 0; i < n; i++) {
        if(!inside(C, p[i])) {
            C = mec{p[i], p[0]};
            for(int j = 0; j < i; j++) {
                if(!inside(C, p[j])) {
                    C = mec{p[i], p[j]};
                    for(int k = 0; k < j; k++) {
                        if(!inside(C, p[k])) {
                            C = mec{p[i], p[j], p[k]};
                        }
                    }
                }
            }
        }
    }
    return C;
}
```

Việc kiểm tra xem một điểm $p_i$ có nằm trong MEC của $2$ hoặc $3$ điểm có thể thực hiện trong $O(1)$. Nhưng ngay cả như vậy, thuật toán trên trông có vẻ sẽ mất $O(n^3)$ trong trường hợp xấu nhất do các vòng lặp lồng nhau. Tại sao chúng ta lại khẳng định nó có thời gian chạy kỳ vọng tuyến tính? Hãy cùng tìm hiểu!

### Phân tích độ phức tạp

Với vòng lặp trong cùng (qua $k$), rõ ràng thời gian chạy kỳ vọng là $O(j)$. Còn vòng lặp qua $j$ thì sao?

Nó chỉ kích hoạt vòng lặp tiếp theo nếu $p_j$ nằm trên biên của MEC của $P_j$ mà cũng đi qua điểm $i$, *và việc loại bỏ $p_j$ sẽ làm đường tròn thu nhỏ lại*. Trong tất cả các điểm của $P_j$, chỉ có tối đa $2$ điểm có tính chất này, vì nếu có nhiều hơn $2$ điểm từ $P_j$ nằm trên biên, nghĩa là sau khi loại bỏ bất kỳ điểm nào trong số đó, vẫn còn ít nhất $3$ điểm trên biên, đủ để xác định duy nhất đường tròn.

Nói cách khác, sau khi xáo trộn ngẫu nhiên, xác suất để chọn phải một trong hai điểm "xui xẻo" đó làm $p_j$ là tối đa $\frac{2}{j}$. Tổng hợp lại qua tất cả $j$ từ $1$ đến $i$, ta nhận được thời gian chạy kỳ vọng là:

$$
\sum\limits_{j=1}^i \frac{2}{j} \cdot O(j) = O(i).
$$

Tương tự, ta cũng có thể chứng minh vòng lặp ngoài cùng có thời gian chạy kỳ vọng là $O(n)$.

### Kiểm tra một điểm nằm trong MEC của 2 hoặc 3 điểm

Hãy xác định chi tiết cài đặt của `point` và `mec`. Trong bài toán này, sử dụng [std::complex](https://codeforces.com/blog/entry/22175) làm lớp cho điểm là cực kỳ hữu ích:

```cpp
using ftype = int64_t;
using point = complex<ftype>;
```

Nhắc lại, một số phức là số có kiểu $x+yi$, trong đó $i^2=-1$ và $x, y \in \mathbb R$. Trong C++, số phức được biểu diễn bởi một điểm 2 chiều $(x, y)$. Số phức đã hỗ trợ sẵn các phép toán tuyến tính theo thành phần (cộng, nhân với số thực), nhưng phép nhân và chia số phức còn mang ý nghĩa hình học.

Tính chất quan trọng nhất cho tác vụ này là: Nhân hai số phức làm cộng các góc cực của chúng (tính từ $Ox$ ngược chiều kim đồng hồ), và lấy liên hợp (thay $z=x+yi$ bằng $\overline{z} = x-yi$) làm đổi dấu góc cực đó. Điều này cho phép ta xây dựng các tiêu chí đơn giản để kiểm tra xem một điểm $z$ có nằm trong MEC của $2$ hoặc $3$ điểm hay không.

#### MEC của 2 điểm

Với $2$ điểm $a$ và $b$, MEC của chúng đơn giản là đường tròn có tâm tại $\frac{a+b}{2}$ với bán kính $\frac{|a-b|}{2}$, hay nói cách khác là đường tròn nhận $ab$ làm đường kính. Để kiểm tra $z$ có nằm trong đường tròn này không, ta chỉ cần kiểm tra góc giữa $za$ và $zb$ không phải là góc nhọn.

<center>
![](https://upload.wikimedia.org/wikipedia/commons/8/8e/Diameter_angles.svg)
<br>
<i>Các góc trong là góc tù, các góc ngoài là góc nhọn và các góc trên cung tròn là góc vuông</i>
</center>

Tương đương, ta cần kiểm tra:

$$
I_0=(b-z)\overline{(a-z)}
$$

không có tọa độ thực dương (tương ứng với các điểm có góc cực nằm giữa $-90^\circ$ và $90^\circ$).

#### MEC của 3 điểm

Việc thêm $z$ vào tam giác $abc$ sẽ tạo thành một tứ giác. Xét biểu thức sau:

$$
\angle azb + \angle bca
$$

Trong một [tứ giác nội tiếp](https://en.wikipedia.org/wiki/Cyclic_quadrilateral), nếu $c$ và $z$ nằm cùng phía so với $ab$, các góc sẽ bằng nhau và tổng lại thành $0^\circ$ khi xét dấu (dương nếu ngược chiều kim đồng hồ, âm nếu cùng chiều). Tương tự, nếu $c$ và $z$ nằm ở hai phía đối diện, các góc sẽ cộng lại thành $180^\circ$.

<center>
![](https://upload.wikimedia.org/wikipedia/commons/3/30/Opposing_inscribed_angles.svg)
<br>
<i>Các góc nội tiếp kề nhau thì bằng nhau, các góc đối diện bù nhau 180 độ</i>
</center>

Dưới dạng số phức, ta lưu ý rằng $\angle azb$ là góc cực của $(b-z)\overline{(a-z)}$ và $\angle bca$ là góc cực của $(a-c)\overline{(b-c)}$. Do đó, $\angle azb + \angle bca$ chính là góc cực của:

$$
I_1 = (b-z) \overline{(a-z)} (a-c) \overline{(b-c)}
$$

Nếu góc là $0^\circ$ hoặc $180^\circ$, nghĩa là phần ảo của $I_1$ bằng $0$. Nếu không, ta có thể suy ra liệu $z$ nằm trong hay ngoài đường tròn bao của $abc$ bằng cách kiểm tra dấu của phần ảo của $I_1$. Phần ảo dương tương ứng với góc dương, phần ảo âm tương ứng với góc âm.

Như đã nhận thấy, việc $z$ nằm trong đường tròn thường làm tăng độ lớn của $\angle azb$, trong khi nằm ngoài sẽ làm giảm nó. Chúng ta có 4 trường hợp:

1. $\angle bca > 0^\circ$, $c$ cùng phía $ab$ với $z$. Khi đó, $\angle azb < 0^\circ$, và $\angle azb + \angle bca < 0^\circ$ cho các điểm nằm trong đường tròn.
3. $\angle bca < 0^\circ$, $c$ cùng phía $ab$ với $z$. Khi đó, $\angle azb > 0^\circ$, và $\angle azb + \angle bca > 0^\circ$ cho các điểm nằm trong đường tròn.
2. $\angle bca > 0^\circ$, $c$ khác phía $ab$ so với $z$. Khi đó, $\angle azb > 0^\circ$ và $\angle azb + \angle bca > 180^\circ$ cho các điểm nằm trong đường tròn.
4. $\angle bca < 0^\circ$, $c$ khác phía $ab$ so với $z$. Khi đó, $\angle azb < 0^\circ$ và $\angle azb + \angle bca < 180^\circ$ cho các điểm nằm trong đường tròn.

Nói cách khác, nếu $\angle bca$ dương, các điểm bên trong đường tròn sẽ có $\angle azb + \angle bca < 0^\circ$, ngược lại sẽ có $\angle azb + \angle bca > 0^\circ$ (giả sử chuẩn hóa góc trong khoảng $-180^\circ$ và $180^\circ$). Điều này có thể kiểm tra qua dấu phần ảo của $I_2=(a-c)\overline{(b-c)}$ và $I_1 = I_0 I_2$.

**Lưu ý**: Khi nhân bốn số phức để có $I_1$, các hệ số trung gian có thể lớn tới $O(A^4)$, với $A$ là độ lớn tọa độ lớn nhất trong đầu vào. Nếu đầu vào là số nguyên, các phép kiểm tra trên có thể thực hiện hoàn toàn bằng số nguyên.

#### Cài đặt

Để cài đặt, ta quyết định cách biểu diễn MEC. Vì tiêu chí hoạt động trực tiếp trên các điểm, cách tự nhiên nhất là đại diện MEC bằng cặp hoặc bộ ba điểm xác định nó:

```cpp
using mec = variant<
    array<point, 2>,
    array<point, 3>
>;
```

Sử dụng `std::visit` để xử lý hiệu quả cả hai trường hợp theo tiêu chí trên:

```cpp
/* I < 0 if z inside C,
   I > 0 if z outside C,
   I = 0 if z on the circumference of C */
ftype indicator(mec const& C, point z) {
    return visit([&](auto &&C) {
        point a = C[0], b = C[1];
        point I0 = (b - z) * conj(a - z);
        if constexpr (size(C) == 2) {
            return real(I0);
        } else {
            point c = C[2];
            point I2 = (a - c) * conj(b - c);
            point I1 = I0 * I2;
            return imag(I2) < 0 ? -imag(I1) : imag(I1);
        }
    }, C);
}

bool inside(mec const& C, point p) {
    return indicator(C, p) <= 0;
}

```

Cuối cùng, ta có thể đảm bảo mọi thứ hoạt động bằng cách nộp bài lên Library Checker: [#308668](https://judge.yosupo.jp/submission/308668).

## Bài tập thực hành

- [Library Checker - Minimum Enclosing Circle](https://judge.yosupo.jp/problem/minimum_enclosing_circle)
- [BOI 2002 - Aliens](https://www.spoj.com/problems/ALIENS)