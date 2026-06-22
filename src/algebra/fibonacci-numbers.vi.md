---
tags:
  - Translated
e_maxx_link: fibonacci_numbers
lang: vi
---

# Số Fibonacci

Dãy Fibonacci được định nghĩa như sau:

$$F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}$$

Các phần tử đầu tiên của dãy ([OEIS A000045](http://oeis.org/A000045)) là:

$$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$$

## Tính chất

Số Fibonacci sở hữu rất nhiều tính chất thú vị. Dưới đây là một vài tính chất trong số đó:

* Đồng nhất thức Cassini (Cassini's identity):
  
$$F_{n-1} F_{n+1} - F_n^2 = (-1)^n$$

>Tính chất này có thể được chứng minh bằng quy nạp. Một chứng minh ngắn gọn của Knuth được đưa ra bằng cách tính định thức của dạng ma trận 2x2 ở phần dưới.

* Quy tắc cộng (addition rule):
  
$$F_{n+k} = F_k F_{n+1} + F_{k-1} F_n$$

* Áp dụng đồng nhất thức trên cho trường hợp $k = n$, ta được:
  
$$F_{2n} = F_n (F_{n+1} + F_{n-1})$$

* Từ đây chúng ta có thể chứng minh bằng quy nạp rằng với mọi số nguyên dương $k$ bất kỳ, $F_{nk}$ luôn là bội số của $F_n$.

* Điều ngược lại cũng đúng: nếu $F_m$ là bội số của $F_n$, thì $m$ cũng là bội số của $n$.

* Đồng nhất thức GCD:
  
$$GCD(F_m, F_n) = F_{GCD(m, n)}$$

* Số Fibonacci là bộ dữ liệu đầu vào tệ nhất cho thuật toán Euclid (xem Định lý Lame trong bài viết về [Thuật toán Euclid](euclid-algorithm.md)).

## Mã hóa Fibonacci

Chúng ta có thể sử dụng dãy Fibonacci để mã hóa các số nguyên dương thành các từ mã nhị phân. Theo Định lý Zeckendorf (Zeckendorf's theorem), mọi số tự nhiên $n$ đều có thể được biểu diễn duy nhất dưới dạng tổng của các số Fibonacci:

$$N = F_{k_1} + F_{k_2} + \ldots + F_{k_r}$$

sao cho $k_1 \ge k_2 + 2,\ k_2 \ge k_3 + 2,\  \ldots,\  k_r \ge 2$ (tức là: biểu diễn không sử dụng hai số Fibonacci liên tiếp).

Hệ quả là mọi số đều có thể được mã hóa duy nhất theo mã hóa Fibonacci (Fibonacci coding).
Chúng ta có thể mô tả biểu diễn này bằng các mã nhị phân $d_0 d_1 d_2 \dots d_s 1$, trong đó $d_i$ là $1$ nếu $F_{i+2}$ được sử dụng trong biểu diễn.
Từ mã sẽ được thêm vào số $1$ ở cuối để đánh dấu sự kết thúc của từ mã.
Lưu ý rằng đây là trường hợp duy nhất mà hai bit 1 liên tiếp xuất hiện.

$$\begin{eqnarray}
1 &=& 1 &=& F_2 &=& (11)_F \\
2 &=& 2 &=& F_3 &=& (011)_F \\
6 &=& 5 + 1 &=& F_5 + F_2 &=& (10011)_F \\
8 &=& 8 &=& F_6 &=& (000011)_F \\
9 &=& 8 + 1 &=& F_6 + F_2 &=& (100011)_F \\
19 &=& 13 + 5 + 1 &=& F_7 + F_5 + F_2 &=& (1001011)_F
\end{eqnarray}$$

Việc mã hóa một số nguyên $n$ có thể được thực hiện bằng một thuật toán tham lam (greedy algorithm) đơn giản:

1. Duyệt qua các số Fibonacci từ lớn đến nhỏ cho đến khi tìm thấy một số nhỏ hơn hoặc bằng $n$.

2. Giả sử số này là $F_i$. Trừ $F_i$ khỏi $n$ và đặt giá trị $1$ tại vị trí $i-2$ của từ mã (đánh chỉ số từ 0 từ bit ngoài cùng bên trái sang bit ngoài cùng bên phải).

3. Lặp lại cho đến khi không còn phần dư.

4. Thêm một số $1$ vào cuối từ mã để đánh dấu sự kết thúc.

Để giải mã một từ mã, đầu tiên ta loại bỏ số $1$ ở cuối. Sau đó, nếu bit thứ $i$ được đặt (đánh chỉ số từ 0 từ bit ngoài cùng bên trái sang bit ngoài cùng bên phải), ta cộng $F_{i+2}$ vào kết quả.

## Công thức tính số Fibonacci thứ $n$ { data-toc-label="Formulas for the <script type='math/tex'>n</script>-th Fibonacci number" }

### Biểu thức dạng đóng (Closed-form expression)

Có một công thức được gọi là "Công thức Binet" (Binet's formula), mặc dù nó đã được Moivre tìm ra từ trước:

$$F_n = \frac{\left(\frac{1 + \sqrt{5}}{2}\right)^n - \left(\frac{1 - \sqrt{5}}{2}\right)^n}{\sqrt{5}}$$

Công thức này rất dễ chứng minh bằng quy nạp, ngoài ra nó có thể được suy ra bằng cách sử dụng khái niệm hàm sinh hoặc giải một phương trình hàm số.

Bạn có thể nhận thấy ngay rằng giá trị tuyệt đối của số hạng thứ hai luôn nhỏ hơn $1$, và nó cũng giảm rất nhanh (theo hàm mũ). Do đó, chỉ riêng giá trị của số hạng đầu tiên đã "gần như" là $F_n$. Công thức này có thể được viết một cách chặt chẽ là:

$$F_n = \left[\frac{\left(\frac{1 + \sqrt{5}}{2}\right)^n}{\sqrt{5}}\right]$$

trong đó dấu ngoặc vuông biểu thị phép làm tròn đến số nguyên gần nhất.

Vì hai công thức này yêu cầu độ chính xác rất cao khi làm việc với các số thập phân, chúng ít khi được sử dụng trong các phép tính toán thực tế.

### Số Fibonacci trong thời gian tuyến tính

Số Fibonacci thứ $n$ có thể dễ dàng tìm thấy trong thời gian $O(n)$ bằng cách tính toán lần lượt từng số cho đến $n$. Tuy nhiên, có những phương pháp nhanh hơn, như chúng ta sẽ thấy sau đây.

Chúng ta có thể bắt đầu bằng cách tiếp cận vòng lặp, tận dụng công thức $F_n = F_{n-1} + F_{n-2}$, đơn giản là tính trước các giá trị đó vào một mảng, lưu ý các trường hợp cơ sở của $F_0$ và $F_1$.

```{.cpp file=fibonacci_linear}
int fib(int n) {
    int a = 0;
    int b = 1;
    for (int i = 0; i < n; i++) {
        int tmp = a + b;
        a = b;
        b = tmp;
    }
    return a;
}
```

Bằng cách này, chúng ta thu được một lời giải tuyến tính, thời gian chạy $O(n)$, lưu trữ tất cả các giá trị trước $n$ trong dãy.

### Dạng ma trận (Matrix form)

Để đi từ $(F_n, F_{n-1})$ sang $(F_{n+1}, F_n)$, chúng ta có thể biểu diễn hệ thức truy hồi tuyến tính dưới dạng một phép nhân ma trận 2x2:

$$
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
F_n \\
F_{n-1}
\end{pmatrix}
=
\begin{pmatrix}
F_n + F_{n-1}  \\
F_{n}
\end{pmatrix}
=
\begin{pmatrix}
F_{n+1}  \\
F_{n}
\end{pmatrix}
$$

Điều này cho phép chúng ta xử lý các bước lặp của hệ thức truy hồi dưới dạng các phép nhân ma trận lặp lại, một phép toán có nhiều tính chất rất tốt. Cụ thể là:

$$
\begin{pmatrix}
1 & 1 \\
1 & 0
\end{pmatrix}^n
\begin{pmatrix}
F_1 \\
F_0
\end{pmatrix}
=
\begin{pmatrix}
F_{n+1}  \\
F_{n}
\end{pmatrix}
$$

trong đó $F_1 = 1, F_0 = 0$.
Thực tế, vì:

$$
\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}
= \begin{pmatrix} F_2 & F_1 \\ F_1 & F_0 \end{pmatrix}
$$

chúng ta có thể sử dụng ma trận trực tiếp:

$$
\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n
= \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}
$$

Do đó, để tìm $F_n$ trong thời gian $O(\log n)$, chúng ta chỉ cần lũy thừa ma trận lên bậc n. (Xem bài viết [Lũy thừa nhị phân](binary-exp.md)).

```{.cpp file=fibonacci_matrix}
struct matrix {
    long long mat[2][2];
    matrix friend operator *(const matrix &a, const matrix &b){
        matrix c;
        for (int i = 0; i < 2; i++) {
          for (int j = 0; j < 2; j++) {
              c.mat[i][j] = 0;
              for (int k = 0; k < 2; k++) {
                  c.mat[i][j] += a.mat[i][k] * b.mat[k][j];
              }
          }
        }
        return c;
    }
};

matrix matpow(matrix base, long long n) {
    matrix ans{ {
      {1, 0},
      {0, 1}
    } };
    while (n) {
        if(n&1)
            ans = ans*base;
        base = base*base;
        n >>= 1;
    }
    return ans;
}

long long fib(int n) {
    matrix base{ {
      {1, 1},
      {1, 0}
    } };
    return matpow(base, n).mat[0][1];
}
```

### Phương pháp nhân đôi nhanh (Fast Doubling Method)

Bằng cách khai triển biểu thức ma trận ở trên cho trường hợp $n = 2\cdot k$:

$$
\begin{pmatrix}
F_{2k+1} & F_{2k}\\
F_{2k} & F_{2k-1}
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix}^{2k}
=
\begin{pmatrix}
F_{k+1} & F_{k}\\
F_{k} & F_{k-1}
\end{pmatrix}
^2
$$

chúng ta thu được các phương trình đơn giản hơn sau:

$$ \begin{align}
F_{2k+1} &= F_{k+1}^2 + F_{k}^2 \\
F_{2k} &= F_k(F_{k+1}+F_{k-1}) = F_k (2F_{k+1} - F_{k})\\
\end{align}.$$

Do đó, sử dụng hai phương trình trên, số Fibonacci có thể được tính toán một cách dễ dàng bằng đoạn mã sau:

```{.cpp file=fibonacci_doubling}
pair<int, int> fib (int n) {
    if (n == 0)
        return {0, 1};

    auto p = fib(n >> 1);
    int c = p.first * (2 * p.second - p.first);
    int d = p.first * p.first + p.second * p.second;
    if (n & 1)
        return {d, c + d};
    else
        return {c, d};
}
```

Đoạn mã trên trả về cặp giá trị $F_n$ và $F_{n+1}$.

## Tính chu kỳ theo modulo p (Periodicity modulo p)

Xét dãy Fibonacci modulo $p$. Chúng ta sẽ chứng minh dãy số này có tính chất tuần hoàn (periodic).

Hãy chứng minh điều này bằng phương pháp phản chứng. Xét $p^2 + 1$ cặp số Fibonacci đầu tiên theo modulo $p$:

$$(F_0,\ F_1),\ (F_1,\ F_2),\ \ldots,\ (F_{p^2},\ F_{p^2 + 1})$$

Chỉ có thể có tối đa $p$ số dư khác nhau theo modulo $p$, và tối đa $p^2$ cặp số dư khác nhau, do đó tồn tại ít nhất hai cặp số dư trùng nhau trong số chúng. Điều này là đủ để chứng minh dãy số tuần hoàn, vì một số Fibonacci chỉ được xác định bởi hai số liền trước nó. Do đó, nếu hai cặp số liên tiếp lặp lại, điều này có nghĩa là các số phía sau cặp đó cũng sẽ lặp lại theo cùng một cách thức.

Bây giờ, chúng ta chọn hai cặp số dư trùng nhau có chỉ số nhỏ nhất trong dãy số. Gọi các cặp này là $(F_a,\ F_{a + 1})$ và $(F_b,\ F_{b + 1})$. Chúng ta sẽ chứng minh rằng $a = 0$. Nếu điều này là sai, sẽ tồn tại hai cặp số liền trước đó là $(F_{a-1},\ F_a)$ and $(F_{b-1},\ F_b)$, theo tính chất của số Fibonacci, chúng cũng phải bằng nhau. Tuy nhiên, điều này mâu thuẫn với việc chúng ta đã chọn các cặp có chỉ số nhỏ nhất, hoàn tất chứng minh rằng không có tiền chu kỳ (pre-period) (tức là dãy số tuần hoàn ngay từ $F_0$).

## Bài tập thực hành

* [SPOJ - Euclid Algorithm Revisited](http://www.spoj.com/problems/MAIN74/)
* [SPOJ - Fibonacci Sum](http://www.spoj.com/problems/FIBOSUM/)
* [HackerRank - Is Fibo](https://www.hackerrank.com/challenges/is-fibo/problem)
* [Project Euler - Even Fibonacci numbers](https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem)
* [DMOJ - Fibonacci Sequence](https://dmoj.ca/problem/fibonacci)
* [DMOJ - Fibonacci Sequence (Harder)](https://dmoj.ca/problem/fibonacci2)
* [DMOJ UCLV - Numbered sequence of pencils](https://dmoj.uclv.edu.cu/problem/secnum)
* [DMOJ UCLV - Fibonacci 2D](https://dmoj.uclv.edu.cu/problem/fibonacci)
* [DMOJ UCLV - fibonacci calculation](https://dmoj.uclv.edu.cu/problem/fibonaccicalculatio)
* [LightOJ -  Number Sequence](https://lightoj.com/problem/number-sequence)
* [Codeforces - C. Fibonacci](https://codeforces.com/problemset/gymProblem/102644/C)
* [Codeforces - A. Hexadecimal's theorem](https://codeforces.com/problemset/problem/199/A)
* [Codeforces - B. Blackboard Fibonacci](https://codeforces.com/problemset/problem/217/B)
* [Codeforces - E. Fibonacci Number](https://codeforces.com/problemset/problem/193/E)
