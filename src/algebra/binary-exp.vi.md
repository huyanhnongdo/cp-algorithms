---
tags:
  - Translated
e_maxx_link: binary_pow
lang: vi
---

# Lũy thừa nhị phân (Binary Exponentiation)

**Lũy thừa nhị phân (Binary Exponentiation)** (hay còn gọi là phương pháp bình phương liên tiếp) là một kỹ thuật cho phép tính $a^n$, với $n$ là một số nguyên không âm, chỉ bằng cách sử dụng $O(\log n)$ phép nhân (thay vì $O(n)$ phép nhân như cách tiếp cận ngây thơ).

Nó cũng có các ứng dụng quan trọng trong nhiều bài toán không liên quan đến số học, vì nó có thể được áp dụng cho bất kỳ phép toán nào có tính chất **kết hợp**:

$$(X \cdot Y) \cdot Z = X \cdot (Y \cdot Z)$$

Ứng dụng rõ ràng nhất là phép nhân mô-đun, phép nhân ma trận và các bài toán khác mà chúng ta sẽ thảo luận ở phần dưới.

## Thuật toán

Phép nâng $a$ lên lũy thừa $n$ một cách ngây thơ được thể hiện bằng cách nhân $a$ liên tiếp $n - 1$ lần:
$a^{n} = a \cdot a \cdot \ldots \cdot a$. Tuy nhiên, cách tiếp cận này không khả thi đối với các giá trị $a$ hoặc $n$ lớn.

Có các tính chất: $a^{b+c} = a^b \cdot a^c$ và $a^{2b} = a^b \cdot a^b = (a^b)^2$.

Ý tưởng của lũy thừa nhị phân là chúng ta phân chia phép tính bằng cách sử dụng biểu diễn nhị phân của số mũ.

Hãy viết số mũ $n$ dưới dạng cơ số 2, ví dụ:

$$3^{13} = 3^{1101_2} = 3^8 \cdot 3^4 \cdot 3^1$$

Vì số $n$ có chính xác $\lfloor \log_2 n \rfloor + 1$ chữ số trong cơ số nhị phân, nên chúng ta chỉ cần thực hiện $O(\log n)$ phép nhân, nếu chúng ta biết các lũy thừa tương ứng $a^1, a^2, a^4, a^8, \dots, a^{2^{\lfloor \log_2 n \rfloor}}$.

Do đó, chúng ta chỉ cần tìm một cách nhanh chóng để tính các lũy thừa này.
Thật may mắn, điều này rất đơn giản vì phần tử tiếp theo trong dãy chỉ đơn thuần là bình phương của phần tử trước đó.

$$\begin{align}
3^1 &= 3 \\
3^2 &= \left(3^1\right)^2 = 3^2 = 9 \\
3^4 &= \left(3^2\right)^2 = 9^2 = 81 \\
3^8 &= \left(3^4\right)^2 = 81^2 = 6561
\end{align}$$

Vì vậy, để có câu trả lời cuối cùng cho $3^{13}$, chúng ta chỉ cần nhân ba lũy thừa lại với nhau (bỏ qua $3^2$ vì bit tương ứng của nó trong biểu diễn nhị phân của $n$ không được bật):
$3^{13} = 6561 \cdot 81 \cdot 3 = 1594323$

Độ phức tạp cuối cùng của thuật toán này là $O(\log n)$: chúng ta phải tính toán $\log n$ lũy thừa của $a$, và sau đó thực hiện tối đa $\log n$ phép nhân để thu được kết quả cuối cùng từ chúng.

Công thức đệ quy dưới đây cũng thể hiện cùng một ý tưởng:

$$a^n = \begin{cases}
1 &\text{if } n == 0 \\
\left(a^{\frac{n}{2}}\right)^2 &\text{if } n > 0 \text{ and } n \text{ even}\\
\left(a^{\frac{n - 1}{2}}\right)^2 \cdot a &\text{if } n > 0 \text{ and } n \text{ odd}\\
\end{cases}$$

## Cài đặt

Đầu tiên là cách tiếp cận đệ quy, đây là một sự chuyển thể trực tiếp của công thức đệ quy ở trên:

```cpp
long long binpow(long long a, long long b) {
    if (b == 0)
        return 1;
    long long res = binpow(a, b / 2);
    if (b % 2)
        return res * res * a;
    else
        return res * res;
}
```

Cách tiếp cận thứ hai thực hiện cùng một nhiệm vụ nhưng không sử dụng đệ quy.
Nó tính toán tất cả các lũy thừa trong một vòng lặp và thực hiện phép nhân khi gặp bit tương ứng được bật trong biểu diễn nhị phân của $n$.
Mặc dù độ phức tạp của cả hai cách tiếp cận là như nhau, nhưng cách tiếp cận lặp này sẽ chạy nhanh hơn trên thực tế vì không gặp chi phí phụ (overhead) của các lời gọi đệ quy.

```cpp
long long binpow(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}
```

## Ứng dụng

### Tính lũy thừa lớn theo mô-đun một cách hiệu quả

**Bài toán:**
Tính $x^n \bmod m$.
Đây là một thao tác cực kỳ phổ biến. Ví dụ, nó được sử dụng để tính [nghịch đảo nhân mô-đun](module-inverse.md).

**Lời giải:**
Vì ta biết rằng phép toán lấy dư mô-đun không ảnh hưởng đến phép nhân ($a \cdot b \equiv (a \bmod m) \cdot (b \bmod m) \pmod m$), chúng ta có thể sử dụng trực tiếp đoạn mã nguồn trên và thay thế mọi phép nhân bằng phép nhân mô-đun tương ứng:

```cpp
long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
```

**Ghi chú:**
Chúng ta có thể tăng tốc thuật toán này đối với trường hợp $b >> m$.
Nếu $m$ là số nguyên dương và $\gcd(x, m) = 1$, ta có $x^n \equiv x^{n \bmod (m-1)} \pmod{m}$ đối với $m$ nguyên tố, và $x^n \equiv x^{n \bmod{\phi(m)}} \pmod{m}$ đối với $m$ là hợp số.
Điều này được suy ra trực tiếp từ định lý nhỏ Fermat và định lý Euler, xem bài viết về [Nghịch đảo mô-đun](module-inverse.md#fermat-euler) để biết thêm chi tiết.

### Tính số Fibonacci một cách hiệu quả

**Bài toán:** Tính số Fibonacci thứ $n$ là $F_n$.

**Lời giải:** Xem chi tiết tại [Bài viết về Số Fibonacci](fibonacci-numbers.md).
Ở đây chúng ta chỉ điểm qua sơ lược về thuật toán.
Để tính số Fibonacci tiếp theo, chúng ta chỉ cần hai số liền trước nó, do có hệ thức $F_n = F_{n-1} + F_{n-2}$.
Ta có thể xây dựng một ma trận kích thước $2 \times 2$ biểu diễn phép biến đổi này:
phép chuyển từ cặp $F_i$ và $F_{i+1}$ sang cặp $F_{i+1}$ và $F_{i+2}$.
Ví dụ, áp dụng phép biến đổi này cho cặp $F_0$ và $F_1$ sẽ đổi nó thành cặp $F_1$ và $F_2$.
Vì vậy, ta có thể nâng ma trận biến đổi này lên lũy thừa bậc $n$ để tìm số Fibonacci $F_n$ với độ phức tạp thời gian $O(\log n)$.

### Áp dụng hoán vị $k$ lần { data-toc-label='Áp dụng hoán vị <script type="math/tex">k</script> lần' }

**Bài toán:** Cho một dãy độ dài $n$. Áp dụng một hoán vị cho trước lên dãy đó $k$ lần.

**Lời giải:** Đơn giản là nâng hoán vị đó lên lũy thừa bậc $k$ sử dụng thuật toán lũy thừa nhị phân, sau đó áp dụng hoán vị kết quả lên dãy ban đầu. Cách này cho độ phức tạp thời gian là $O(n \log k)$.

```cpp
vector<int> applyPermutation(vector<int> sequence, vector<int> permutation) {
    vector<int> newSequence(sequence.size());
    for(int i = 0; i < sequence.size(); i++) {
        newSequence[i] = sequence[permutation[i]];
    }
    return newSequence;
}

vector<int> permute(vector<int> sequence, vector<int> permutation, long long k) {
    while (k > 0) {
        if (k & 1) {
            sequence = applyPermutation(sequence, permutation);
        }
        permutation = applyPermutation(permutation, permutation);
        k >>= 1;
    }
    return sequence;
}
```

**Ghi chú:** Bài toán này có thể được giải hiệu quả hơn trong thời gian tuyến tính bằng cách dựng đồ thị hoán vị và xét độc lập từng chu trình. Sau đó bạn có thể lấy $k$ chia lấy dư cho kích thước của chu trình để tìm ra vị trí cuối cùng cho mỗi số thuộc chu trình đó.

### Áp dụng nhanh một tập các phép biến đổi hình học cho một tập điểm

**Bài toán:** Cho $n$ điểm $p_i$, áp dụng $m$ phép biến đổi lên mỗi điểm này. Mỗi phép biến đổi có thể là tịnh tiến (dịch chuyển), co giãn hoặc quay quanh một trục cho trước một góc cho trước. Ngoài ra còn có một phép toán "vòng lặp" cho phép áp dụng danh sách các phép biến đổi cho trước $k$ lần (phòng lặp có thể lồng nhau). Bạn cần áp dụng tất cả các phép biến đổi này nhanh hơn thời gian $O(n \cdot length)$, với $length$ là tổng số phép biến đổi cần áp dụng (sau khi đã khai triển các vòng lặp).

**Lời giải:** Hãy xem cách các loại phép biến đổi khác nhau thay đổi tọa độ điểm:

* Phép tịnh tiến: cộng một hằng số khác nhau vào mỗi tọa độ.
* Phép co giãn: nhân mỗi tọa độ với một hằng số khác nhau.
* Phép quay: phép biến đổi phức tạp hơn một chút (chúng ta sẽ không đi sâu vào chi tiết ở đây), nhưng mỗi tọa độ mới vẫn có thể được biểu diễn dưới dạng tổ hợp tuyến tính của các tọa độ cũ.

Như bạn thấy, mỗi phép biến đổi đều có thể biểu diễn dưới dạng phép toán tuyến tính trên tọa độ điểm. Do đó, một phép biến đổi có thể viết dưới dạng ma trận kích thước $4 \times 4$ như sau:

$$\begin{pmatrix}
a_{11} & a_ {12} & a_ {13} & a_ {14} \\
a_{21} & a_ {22} & a_ {23} & a_ {24} \\
a_{31} & a_ {32} & a_ {33} & a_ {34} \\
a_{41} & a_ {42} & a_ {43} & a_ {44}
\end{pmatrix}$$

mà khi nhân với vector chứa các tọa độ cũ và một số đơn vị (fictitious coordinate), ta nhận được vector chứa các tọa độ mới và số đơn vị:

$$\begin{pmatrix} x & y & z & 1 \end{pmatrix} \cdot
\begin{pmatrix}
a_{11} & a_ {12} & a_ {13} & a_ {14} \\
a_{21} & a_ {22} & a_ {23} & a_ {24} \\
a_{31} & a_ {32} & a_ {33} & a_ {34} \\
a_{41} & a_ {42} & a_ {43} & a_ {44}
\end{pmatrix}
 = \begin{pmatrix} x' & y' & z' & 1 \end{pmatrix}$$

(Bạn có thể hỏi tại sao lại đưa thêm tọa độ thứ tư giả định này vào? Đó chính là vẻ đẹp của [tọa độ đồng nhất (homogeneous coordinates)](https://en.wikipedia.org/wiki/Homogeneous_coordinates), vốn được ứng dụng rộng rãi trong đồ họa máy tính. Không có nó, chúng ta không thể thực hiện các phép biến đổi affine như tịnh tiến dưới dạng một phép nhân ma trận đơn lẻ, vì nó yêu cầu chúng ta phải _cộng_ một hằng số vào các tọa độ. Phép biến đổi affine nhờ vậy trở thành một phép biến đổi tuyến tính trong không gian số chiều cao hơn!)

Dưới đây là một số ví dụ về cách biểu diễn các phép biến đổi dưới dạng ma trận:

* Phép tịnh tiến: dịch tọa độ $x$ đi $5$, tọa độ $y$ đi $7$ và tọa độ $z$ đi $9$.

$$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
5 & 7 & 9 & 1
\end{pmatrix}$$

* Phép co giãn: nhân tọa độ $x$ với $10$ và hai tọa độ còn lại với $5$.

$$\begin{pmatrix}
10 & 0 & 0 & 0 \\
0 & 5 & 0 & 0 \\
0 & 0 & 5 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

* Phép quay: quay một góc $\theta$ độ quanh trục $x$ theo quy tắc bàn tay phải (ngược chiều kim đồng hồ).

$$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \cos \theta & -\sin \theta & 0 \\
0 & \sin \theta & \cos \theta & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

Bây giờ, khi mỗi phép biến đổi được mô tả dưới dạng một ma trận, chuỗi các phép biến đổi có thể biểu diễn dưới dạng tích của các ma trận này, và một "vòng lặp" lặp lại $k$ lần có thể biểu diễn bằng ma trận nâng lên lũy thừa bậc $k$ (có thể tính bằng lũy thừa nhị phân trong thời gian $O(\log{k})$). Theo cách này, ma trận đại diện cho tất cả phép biến đổi có thể tính trước trong thời gian $O(m \log{k})$, và sau đó áp dụng cho mỗi điểm trong số $n$ điểm trong thời gian $O(n)$ với tổng độ phức tạp là $O(n + m \log{k})$.

### Số lượng đường đi độ dài $k$ trong đồ thị { data-toc-label='Số lượng đường đi độ dài <script type="math/tex">k</script> trong đồ thị' }

**Bài toán:** Cho một đồ thị có hướng không trọng số gồm $n$ đỉnh, hãy tìm số lượng đường đi độ dài $k$ từ đỉnh $u$ bất kỳ đến đỉnh $v$ bất kỳ.

**Lời giải:** Bài toán này được trình bày chi tiết hơn trong [một bài viết riêng](../graph/fixed_length_paths.md). Thuật toán bao gồm việc nâng ma trận kề $M$ của đồ thị (ma trận có $m_{ij} = 1$ nếu có cạnh nối từ $i$ đến $j$, ngược lại bằng $0$) lên lũy thừa bậc $k$. Khi đó, phần tử $m_{ij}$ chính là số lượng đường đi độ dài $k$ từ $i$ đến $j$. Độ phức tạp thời gian của giải pháp này là $O(n^3 \log k)$.

**Ghi chú:** Trong cùng bài viết đó, một biến thể khác của bài toán cũng được xem xét: khi các cạnh có trọng số và bài toán yêu cầu tìm đường đi có tổng trọng số nhỏ nhất chứa đúng $k$ cạnh. Bài toán này cũng được giải quyết bằng lũy thừa ma trận kề, trong đó ma trận kề chứa trọng số của cạnh nối từ $i$ đến $j$, hoặc bằng $\infty$ nếu không có cạnh nối.
Tuy nhiên, thay vì phép toán nhân ma trận thông thường, chúng ta sử dụng phép toán biến đổi:
thay vì nhân hai số, ta cộng chúng lại; và thay vì cộng dồn, ta lấy giá trị nhỏ nhất (phép toán cộng-tối thiểu).
Tức là: $result_{ij} = \min\limits_{1\ \leq\ k\ \leq\ n}(a_{ik} + b_{kj})$.

### Biến thể của lũy thừa nhị phân: nhân hai số theo mô-đun $m$ { data-toc-label='Biến thể của lũy thừa nhị phân: nhân hai số theo mô-đun <script type="math/tex">m</script>' }

**Bài toán:** Nhân hai số $a$ và $b$ theo mô-đun $m$. $a$ và $b$ có thể biểu diễn được bằng các kiểu dữ liệu số nguyên có sẵn, nhưng tích của chúng lại quá lớn để lưu trữ bằng kiểu số nguyên 64-bit. Ý tưởng là tính $a \cdot b \pmod m$ mà không cần sử dụng các cấu trúc số lớn (bignum arithmetic).

**Lời giải:** Chúng ta chỉ cần áp dụng thuật toán nhị phân tương tự như trên, nhưng thực hiện các phép cộng thay vì phép nhân. Nói cách khác, chúng ta đã "phân rã" phép nhân hai số thành $O (\log m)$ phép toán cộng và phép nhân hai (thực chất cũng là phép cộng).

$$a \cdot b = \begin{cases}
0 &\text{if }a = 0 \\
2 \cdot \frac{a}{2} \cdot b &\text{if }a > 0 \text{ and }a \text{ even} \\
2 \cdot \frac{a-1}{2} \cdot b + b &\text{if }a > 0 \text{ and }a \text{ odd}
\end{cases}$$

**Ghi chú:** Bạn có thể giải quyết bài toán này theo một cách khác sử dụng số thực dấu phẩy động. Đầu tiên tính toán biểu thức $\frac{a \cdot b}{m}$ dùng kiểu số thực và ép kiểu kết quả về số nguyên không dấu $q$. Trừ $q \cdot m$ khỏi tích $a \cdot b$ sử dụng số học nguyên không dấu và lấy dư mô-đun $m$ để có đáp án. Giải pháp này trông có vẻ kém tin cậy hơn, nhưng lại cực kỳ nhanh và dễ cài đặt. Xem chi tiết tại [Modular Multiplication](https://cs.stackexchange.com/questions/77016/modular-multiplication).

## Bài tập thực hành

* [UVa 1230 - MODEX](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
* [UVa 374 - Big Mod](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
* [UVa 11029 - Leading and Trailing](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
* [Codeforces - Parking Lot](http://codeforces.com/problemset/problem/630/I)
* [leetcode - Count good numbers](https://leetcode.com/problems/count-good-numbers/)
* [Codechef - Chef and Riffles](https://www.codechef.com/JAN221B/problems/RIFFLES)
* [Codeforces - Decoding Genome](https://codeforces.com/contest/222/problem/E)
* [Codeforces - Neural Network Country](https://codeforces.com/contest/852/problem/B)
* [Codeforces - Magic Gems](https://codeforces.com/problemset/problem/1117/D)
* [SPOJ - The last digit](http://www.spoj.com/problems/LASTDIG/)
* [SPOJ - Locker](http://www.spoj.com/problems/LOCKER/)
* [LA - 3722 Jewel-eating Monsters](https://vjudge.net/problem/UVALive-3722)
* [SPOJ - Just add it](http://www.spoj.com/problems/ZSUM/)
* [Codeforces - Stairs and Lines](https://codeforces.com/contest/498/problem/E)
