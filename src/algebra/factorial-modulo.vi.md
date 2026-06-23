---
title: Giai thừa mô-đun p
tags:
  - Translated
e_maxx_link: modular_factorial
---

# Giai thừa mô-đun $p$

Trong một số trường hợp, chúng ta cần tính các công thức phức tạp theo mô-đun của một số nguyên tố $p$ nào đó, có chứa giai thừa ở cả tử số và mẫu số, giống như công thức tính Hệ số nhị thức.
Chúng ta xét trường hợp khi $p$ tương đối nhỏ.
Bài toán này chỉ có ý nghĩa khi các giai thừa xuất hiện ở cả tử số và mẫu số của phân số.
Nếu không, $p!$ và các số hạng tiếp theo sẽ bằng 0 theo mô-đun $p$.
Nhưng trong phân số, các thừa số $p$ có thể triệt tiêu lẫn nhau, và biểu thức kết quả sẽ khác không theo mô-đun $p$.

Do đó, phát biểu bài toán một cách hình thức là: Bạn muốn tính $n! \bmod p$ mà không tính đến tất cả các thừa số $p$ xuất hiện trong giai thừa.
Hãy tưởng tượng bạn viết phân tích thừa số nguyên tố của $n!$, loại bỏ tất cả các thừa số $p$, và tính tích các số còn lại theo mô-đun $p$.
Chúng ta sẽ ký hiệu giai thừa *đã biến đổi* này là $n!_{\%p}$.
Ví dụ: $7!_{\%p} \equiv 1 \cdot 2 \cdot \underbrace{1}_{3} \cdot 4 \cdot 5 \underbrace{2}_{6} \cdot 7 \equiv 2 \bmod 3$.

Việc biết cách tính hiệu quả giai thừa đã biến đổi này cho phép chúng ta nhanh chóng tính toán giá trị của các công thức tổ hợp khác nhau (ví dụ: [Hệ số nhị thức (Binomial coefficients)](../combinatorics/binomial-coefficients.md)).

## Thuật toán
Hãy viết giai thừa đã biến đổi này một cách rõ ràng:

$$\begin{eqnarray}
n!_{\%p} &=& 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot (p+1) \cdot (p+2) \cdot \ldots \cdot (2p-1) \cdot \underbrace{2}_{2p} \\\
 & &\quad \cdot (2p+1) \cdot \ldots \cdot (p^2-1) \cdot \underbrace{1}_{p^2} \cdot (p^2 +1) \cdot \ldots \cdot n \pmod{p} \\\\
&=& 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot 1 \cdot 2 \cdot \ldots \cdot (p-1) \cdot \underbrace{2}_{2p} \cdot 1 \cdot 2 \\\
& &\quad \cdot \ldots \cdot (p-1) \cdot \underbrace{1}_{p^2} \cdot 1 \cdot 2 \cdot \ldots \cdot (n \bmod p) \pmod{p}
\end{eqnarray}$$

Có thể thấy rõ rằng giai thừa được chia thành nhiều khối có cùng độ dài ngoại trừ khối cuối cùng.

$$\begin{eqnarray}
n!_{\%p}&=& \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{1\text{st}} \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 2}_{2\text{nd}} \cdot \ldots \\\\
& & \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{p\text{th}} \cdot \ldots \cdot \quad \underbrace{1 \cdot 2 \cdot \cdot \ldots \cdot (n \bmod p)}_{\text{tail}} \pmod{p}.
\end{eqnarray}$$

Phần chính của các khối này rất dễ tính — nó chỉ là $(p-1)!\ \mathrm{mod}\ p$.
Chúng ta có thể tính toán điều đó bằng lập trình hoặc chỉ cần áp dụng định lý Wilson, định lý này phát biểu rằng $(p-1)! \bmod p = -1$ với mọi số nguyên tố $p$.

Chúng ta có chính xác $\lfloor \frac{n}{p} \rfloor$ khối như vậy, vì vậy chúng ta cần lũy thừa $-1$ với số mũ $\lfloor \frac{n}{p} \rfloor$.
Điều này có thể được thực hiện trong thời gian logarit bằng cách sử dụng [Lũy thừa nhị phân (Binary Exponentiation)](binary-exp.md); tuy nhiên bạn cũng có thể nhận thấy rằng kết quả sẽ luân phiên giữa $-1$ và $1$, vì vậy chúng ta chỉ cần xem xét tính chẵn lẻ của số mũ và nhân với $-1$ nếu số mũ là lẻ.
Và thay vì phép nhân, chúng ta cũng có thể chỉ cần lấy $p$ trừ đi kết quả hiện tại.

Giá trị của khối cuối cùng (phần dư) có thể được tính riêng trong $O(p)$.

Điều này chỉ còn lại phần tử cuối cùng của mỗi khối.
Nếu chúng ta ẩn đi các phần tử đã được xử lý, chúng ta có thể thấy quy luật sau:

$$n!_{\%p} = \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 2} \cdot \ldots \cdot \underbrace{ \ldots \cdot (p-1)} \cdot \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 1} \cdot \underbrace{ \ldots \cdot 2} \cdots$$

Đây lại là một giai thừa *đã biến đổi*, chỉ với kích thước nhỏ hơn nhiều.
Đó là $\lfloor n / p \rfloor !_{\%p}$.

Như vậy, trong quá trình tính giai thừa *đã biến đổi* $n!_{\%p}$, chúng ta đã thực hiện $O(p)$ phép toán và còn lại việc tính $\lfloor n / p \rfloor !_{\%p}$.
Chúng ta có một công thức đệ quy.
Độ sâu đệ quy là $O(\log_p n)$, và do đó độ phức tạp tiệm cận hoàn chỉnh của thuật toán là $O(p \log_p n)$.

Lưu ý rằng nếu bạn tính trước các giai thừa $0!,~ 1!,~ 2!,~ \dots,~ (p-1)!$ theo mô-đun $p$, thì độ phức tạp sẽ chỉ là $O(\log_p n)$.

## Cài đặt

Chúng ta không cần đệ quy vì đây là trường hợp đệ quy đuôi (tail recursion) và do đó có thể dễ dàng cài đặt bằng vòng lặp.
Trong cài đặt sau, chúng ta tính trước các giai thừa $0!,~ 1!,~ \dots,~ (p-1)!$, và do đó có thời gian chạy là $O(p + \log_p n)$.
Nếu bạn cần gọi hàm này nhiều lần, bạn có thể thực hiện việc tính trước bên ngoài hàm và thực hiện tính toán $n!_{\%p}$ trong thời gian $O(\log_p n)$.

```cpp
int factmod(int n, int p) {
    vector<int> f(p);
    f[0] = 1;
    for (int i = 1; i < p; i++)
        f[i] = f[i-1] * i % p;

    int res = 1;
    while (n > 1) {
        if ((n/p) % 2)
            res = p - res;
        res = res * f[n%p] % p;
        n /= p;
    }
    return res;
}
```

Ngoài ra, nếu bạn bị giới hạn bộ nhớ và không thể lưu trữ toàn bộ các giai thừa, bạn cũng có thể chỉ nhớ các giai thừa cần thiết, sắp xếp chúng, rồi tính chúng trong một lượt bằng cách tính các giai thừa $0!,~ 1!,~ 2!,~ \dots,~ (p-1)!$ trong một vòng lặp mà không cần lưu trữ chúng một cách tường minh.

## Bậc lũy thừa của $p$

Nếu chúng ta muốn tính Hệ số nhị thức (Binomial coefficient) theo mô-đun $p$, thì chúng ta cần thêm bậc lũy thừa của $p$ trong $n!$, tức là số lần $p$ xuất hiện trong phân tích thừa số nguyên tố của $n!$, hay số lần chúng ta đã loại bỏ $p$ trong quá trình tính giai thừa *đã biến đổi*.

[Công thức Legendre (Legendre's formula)](https://en.wikipedia.org/wiki/Legendre%27s_formula) cung cấp cho chúng ta một cách để tính toán điều này trong thời gian $O(\log_p n)$.
Công thức cho số mũ $\nu_p$ như sau:

$$\nu_p(n!) = \sum_{i=1}^{\infty} \left\lfloor \frac{n}{p^i} \right\rfloor$$

Do đó, chúng ta có cài đặt:

```cpp
int multiplicity_factorial(int n, int p) {
    int count = 0;
    do {
        n /= p;
        count += n;
    } while (n);
    return count;
}
```

Công thức này có thể được chứng minh rất dễ dàng bằng cách sử dụng cùng các ý tưởng mà chúng ta đã làm ở các phần trước.
Loại bỏ tất cả các phần tử không chứa thừa số $p$.
Điều này để lại $\lfloor n/p \rfloor$ phần tử còn lại.
Nếu chúng ta loại bỏ thừa số $p$ từ mỗi phần tử đó, chúng ta sẽ được tích $1 \cdot 2 \cdots \lfloor n/p \rfloor = \lfloor n/p \rfloor !$, và một lần nữa chúng ta lại có đệ quy.
