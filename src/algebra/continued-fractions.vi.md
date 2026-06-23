---
tags:
  - Translated
---

<!--?title Continued fractions -->
# Liên phân số

**Liên phân số (Continued fraction)** là một cách biểu diễn một số thực dưới dạng một giới hạn hội tụ của một dãy các phân số (số hữu tỉ). Chúng rất hữu ích trong lập trình thi đấu vì chúng dễ tính toán và có thể được sử dụng hiệu quả để tìm xấp xỉ số hữu tỉ tốt nhất cho một số thực cho trước (trong số tất cả các phân số có mẫu số không vượt quá một giá trị nhất định).

Bên cạnh đó, liên phân số có mối quan hệ chặt chẽ với thuật toán Euclid, điều này giúp chúng trở nên hữu ích trong nhiều bài toán lý thuyết số.

## Biểu diễn liên phân số

!!! info "Định nghĩa"
    Cho $a_0, a_1, \dots, a_k \in \mathbb Z$ và $a_1, a_2, \dots, a_k \geq 1$. Khi đó biểu thức

    $$r=a_0 + \frac{1}{a_1 + \frac{1}{\dots + \frac{1}{a_k}}},$$

    được gọi là **biểu diễn liên phân số** của số hữu tỉ $r$ và được ký hiệu ngắn gọn là $r=[a_0;a_1,a_2,\dots,a_k]$.

??? example
    Cho $r = \frac{5}{3}$. Có hai cách để biểu diễn nó dưới dạng liên phân số:

    $$
    \begin{align}
    r = [1;1,1,1] &= 1+\frac{1}{1+\frac{1}{1+\frac{1}{1}}},\\
    r = [1;1,2] &= 1+\frac{1}{1+\frac{1}{2}}.
    \end{align}
    $$

Người ta có thể chứng minh rằng bất kỳ số hữu tỉ nào cũng có thể được biểu diễn dưới dạng liên phân số theo đúng $2$ cách:

$$r = [a_0;a_1,\dots,a_k,1] = [a_0;a_1,\dots,a_k+1].$$

Hơn nữa, chiều dài $k$ của liên phân số như vậy được ước tính là $k = O(\log \min(p, q))$ cho $r=\frac{p}{q}$.

Lý do đằng sau điều này sẽ rõ ràng khi chúng ta đi sâu vào chi tiết cách dựng liên phân số.

!!! info "Định nghĩa"
    Cho $a_0,a_1,a_2, \dots$ là một dãy số nguyên sao cho $a_1, a_2, \dots \geq 1$. Gọi $r_k = [a_0; a_1, \dots, a_k]$. Khi đó biểu thức

    $$r = a_0 + \frac{1}{a_1 + \frac{1}{a_2+\dots}} = \lim\limits_{k \to \infty} r_k.$$

    được gọi là **biểu diễn liên phân số** của số vô tỉ $r$ và được ký hiệu ngắn gọn là $r = [a_0;a_1,a_2,\dots]$.

Lưu ý rằng đối với $r=[a_0;a_1,\dots]$ và số nguyên $k$, ta luôn có $r+k = [a_0+k; a_1, \dots]$.

Một quan sát quan trọng khác là $\frac{1}{r}=[0;a_0, a_1, \dots]$ khi $a_0 > 0$ và $\frac{1}{r} = [a_1; a_2, \dots]$ khi $a_0 = 0$.

!!! info "Định nghĩa"
    Trong định nghĩa trên, các số hữu tỉ $r_0, r_1, r_2, \dots$ được gọi là **phân số hội tụ (convergents)** của $r$.

    Tương ứng, giá trị $r_k = [a_0; a_1, \dots, a_k] = \frac{p_k}{q_k}$ được gọi là phân số hội tụ thứ $k$ của $r$.

??? example
    Xét $r = [1; 1, 1, 1, \dots]$. Bằng phương pháp quy nạp toán học, ta có thể chứng minh rằng $r_k = \frac{F_{k+2}}{F_{k+1}}$, trong đó $F_k$ là dãy số Fibonacci được định nghĩa là $F_0 = 0$, $F_1 = 1$ và $F_{k} = F_{k-1} + F_{k-2}$. Từ công thức Binet, ta đã biết:

    $$r_k = \frac{\phi^{k+2} - \psi^{k+2}}{\phi^{k+1} - \psi^{k+1}},$$

    trong đó $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$ là tỷ lệ vàng và $\psi = \frac{1-\sqrt{5}}{2} = -\frac{1}{\phi} \approx -0.618$. Do đó,

    $$r = 1+\frac{1}{1+\frac{1}{1+\dots}}=\lim\limits_{k \to \infty} r_k = \phi = \frac{1+\sqrt{5}}{2}.$$

    Lưu ý rằng trong trường hợp cụ thể này, một cách khác để tìm $r$ là giải phương trình:

    $$r = 1+\frac{1}{r} \implies r^2 = r + 1. $$

!!! info "Định nghĩa"
    Cho $r_k = [a_0; a_1, \dots, a_{k-1}, a_k]$. Các số $[a_0; a_1, \dots, a_{k-1}, t]$ với $1 \leq t \leq a_k$ được gọi là **phân số bán hội tụ (semiconvergents)**.

    Chúng ta thường gọi các phân số (bán) hội tụ lớn hơn $r$ là phân số (bán) hội tụ **trên** (upper) và các phân số nhỏ hơn $r$ là phân số (bán) hội tụ **dưới** (lower).

!!! info "Định nghĩa"
    Bên cạnh các phân số hội tụ, chúng ta định nghĩa **[thương đầy đủ (complete quotients)](https://en.wikipedia.org/wiki/Complete_quotient)** là $s_k = [a_k; a_{k+1}, a_{k+2}, \dots]$.

    Tương ứng, chúng ta sẽ gọi một phần tử $s_k$ cụ thể là thương đầy đủ thứ $k$ của $r$.

Từ các định nghĩa trên, ta có thể kết luận rằng $s_k \geq 1$ với mọi $k \geq 1$.

Coi $[a_0; a_1, \dots, a_k]$ như một biểu thức đại số hình thức và cho phép các số thực bất kỳ thay thế cho các $a_i$, ta thu được:

$$r = [a_0; a_1, \dots, a_{k-1}, s_k].$$

Đặc biệt, $r = [s_0] = s_0$. Mặt khác, chúng ta có thể biểu diễn $s_k$ dưới dạng:

$$s_k = [a_k; s_{k+1}] = a_k + \frac{1}{s_{k+1}},$$

nghĩa là chúng ta có thể tính $a_k = \lfloor s_k \rfloor$ và $s_{k+1} = (s_k - a_k)^{-1}$ từ $s_k$.

Dãy $a_0, a_1, \dots$ được định nghĩa rõ ràng trừ khi $s_k=a_k$, điều này chỉ xảy ra khi $r$ là một số hữu tỉ.

Vì vậy, biểu diễn liên phân số được định nghĩa duy nhất cho bất kỳ số vô tỉ $r$ nào.

### Cài đặt

Trong các đoạn mã dưới đây, chúng ta chủ yếu giả định các liên phân số là hữu hạn.

Từ $s_k$, bước chuyển sang $s_{k+1}$ có dạng:

$$s_k =\left\lfloor s_k \right\rfloor + \frac{1}{s_{k+1}}.$$

Từ biểu thức này, thương đầy đủ tiếp theo $s_{k+1}$ được tính là:

$$s_{k+1} = \left(s_k-\left\lfloor s_k\right\rfloor\right)^{-1}.$$

Đối với $s_k=\frac{p}{q}$, điều đó có nghĩa là:

$$
s_{k+1} = \left(\frac{p}{q}-\left\lfloor \frac{p}{q} \right\rfloor\right)^{-1} = \frac{q}{p-q\cdot \lfloor \frac{p}{q} \rfloor} = \frac{q}{p \bmod q}.
$$

Do đó, việc tính toán biểu diễn liên phân số cho $r=\frac{p}{q}$ tuân theo các bước của thuật toán Euclid cho $p$ và $q$.

Từ đây cũng suy ra $\gcd(p_k, q_k) = 1$ cho $\frac{p_k}{q_k} = [a_0; a_1, \dots, a_k]$. Vì vậy, các phân số hội tụ luôn là các phân số tối giản.

=== "C++"
    ```cpp
    auto fraction(int p, int q) {
        vector<int> a;
        while(q) {
            a.push_back(p / q);
            tie(p, q) = make_pair(q, p % q);
        }
        return a;
    }
    ```
=== "Python"
    ```py
    def fraction(p, q):
        a = []
        while q:
            a.append(p // q)
            p, q = q, p % q
        return a
    ```

## Các kết quả chính

Để tạo động lực cho việc nghiên cứu sâu hơn về liên phân số, chúng tôi đưa ra một số tính chất chính dưới đây.

??? note "Công thức truy hồi"
    Đối với các phân số hội tụ $r_k = \frac{p_k}{q_k}$, công thức truy hồi sau đây cho phép tính toán nhanh chúng:
    
    $$\frac{p_k}{q_k}=\frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}},$$
    
    trong đó $\frac{p_{-1}}{q_{-1}}=\frac{1}{0}$ và $\frac{p_{-2}}{q_{-2}}=\frac{0}{1}$.

??? note "Đánh giá sai số"
    Sai số của $r_k = \frac{p_k}{q_k}$ so với $r$ nói chung có thể được ước tính như sau:
    
    $$\left|\frac{p_k}{q_k}-r\right| \leq \frac{1}{q_k q_{k+1}} \leq \frac{1}{q_k^2}.$$
    
    Nhân cả hai vế với $q_k$, ta thu được đánh giá thay thế:
    
    $$|p_k - q_k r| \leq \frac{1}{q_{k+1}}.$$

    Từ công thức truy hồi ở trên, suy ra $q_k$ tăng trưởng nhanh ít nhất bằng dãy số Fibonacci.

    Trên hình dưới đây, bạn có thể thấy trực quan hóa cách các phân số hội tụ $r_k$ tiến tới giá trị $r=\frac{1+\sqrt 5}{2}$:

    ![](https://upload.wikimedia.org/wikipedia/commons/b/b4/Golden_ration_convergents.svg)

    $r=\frac{1+\sqrt 5}{2}$ được mô tả bằng đường đứt nét màu xanh dương. Các phân số hội tụ lẻ tiến tới nó từ phía trên và các phân số hội tụ chẵn tiến tới nó từ phía dưới.

??? note "Bao lồi lưới điểm"
    Xét bao lồi của các điểm nguyên nằm phía trên và phía dưới đường thẳng $y=rx$.
    
    Các phân số hội tụ lẻ $(q_k;p_k)$ là đỉnh của bao lồi phía trên, trong khi các phân số hội tụ chẵn $(q_k;p_k)$ là đỉnh của bao lồi phía dưới.
    
    Tất cả các đỉnh nguyên trên các bao lồi này được biểu diễn dưới dạng $(q;p)$ sao cho:
    
    $$\frac{p}{q} = \frac{tp_{k-1} + p_{k-2}}{tq_{k-1} + q_{k-2}}$$
    
    với số nguyên $0 \leq t \leq a_k$. Nói cách khác, tập hợp các điểm nguyên trên bao lồi chính là tập hợp các phân số bán hội tụ.

    Trong hình dưới đây, bạn có thể thấy các phân số hội tụ và bán hội tụ (các điểm màu xám trung gian) của $r=\frac{9}{7}$.

    ![](https://upload.wikimedia.org/wikipedia/commons/9/92/Continued_convergents_geometry.svg)

??? note "Xấp xỉ tốt nhất"
    Gọi $\frac{p}{q}$ là phân số cực tiểu hóa $\left|r-\frac{p}{q}\right|$ thỏa mãn điều kiện $q \leq x$ với một giá trị $x$ cho trước.
    
    Khi đó $\frac{p}{q}$ chính là một phân số bán hội tụ của $r$.

Tính chất cuối cùng cho phép chúng ta tìm các xấp xỉ hữu tỉ tốt nhất của $r$ bằng cách kiểm tra các phân số bán hội tụ của nó.

Dưới đây là các giải thích chi tiết hơn và trực quan hóa cho các tính chất này.

## Phân số hội tụ (Convergents)

Hãy cùng xem xét kỹ hơn các phân số hội tụ đã được định nghĩa ở trên. Đối với số $r=[a_0, a_1, a_2, \dots]$, các phân số hội tụ của nó là:

\begin{gather}
r_0=[a_0],\\r_1=[a_0, a_1],\\ \dots,\\ r_k=[a_0, a_1, \dots, a_k].
\end{gather}

Các phân số hội tụ là khái niệm cốt lõi của liên phân số, do đó việc nghiên cứu các tính chất của chúng là vô cùng quan trọng.

Đối với số $r$, phân số hội tụ thứ $k$ của nó $r_k = \frac{p_k}{q_k}$ có thể được tính như sau:

$$r_k = \frac{P_k(a_0,a_1,\dots,a_k)}{P_{k-1}(a_1,\dots,a_k)} = \frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}},$$

trong đó $P_k(a_0,\dots,a_k)$ là [continuant](https://en.wikipedia.org/wiki/Continuant_(mathematics)), một đa thức nhiều biến được định nghĩa dưới dạng định thức ma trận:

$$P_k(x_0,x_1,\dots,x_k) = \det \begin{bmatrix}
x_k & 1 & 0 & \dots & 0 \\
-1 & x_{k-1} & 1 & \dots & 0 \\
0 & -1 & x_2 & . & \vdots \\
\vdots & \vdots & . & \ddots & 1 \\
0 & 0 & \dots & -1 & x_0
\end{bmatrix}_{\textstyle .}$$

Do đó, $r_k$ là một trung số có trọng số (weighted [mediant](https://en.wikipedia.org/wiki/Mediant_(mathematics))) của $r_{k-1}$ và $r_{k-2}$.

Để đảm bảo tính nhất quán, người ta định nghĩa hai phân số hội tụ ảo ban đầu là $r_{-1} = \frac{1}{0}$ và $r_{-2} = \frac{0}{1}$.

??? hint "Giải thích chi tiết"

    Tử số và mẫu số của $r_k$ có thể được coi là các đa thức nhiều biến của $a_0, a_1, \dots, a_k$:

    $$r_k = \frac{P_k(a_0, a_1, \dots, a_k)}{Q_k(a_0,a_1, \dots, a_k)}.$$

    Từ định nghĩa của phân số hội tụ:

    $$r_k = a_0 + \frac{1}{[a_1;a_2,\dots, a_k]}= a_0 + \frac{Q_{k-1}(a_1, \dots, a_k)}{P_{k-1}(a_1, \dots, a_k)} = \frac{a_0 P_{k-1}(a_1, \dots, a_k) + Q_{k-1}(a_1, \dots, a_k)}{P_{k-1}(a_1, \dots, a_k)}.$$

    Từ đây suy ra $Q_k(a_0, \dots, a_k) = P_{k-1}(a_1, \dots, a_k)$. Điều này dẫn đến hệ thức:

    $$P_k(a_0, \dots, a_k) = a_0 P_{k-1}(a_1, \dots, a_k) + P_{k-2}(a_2, \dots, a_k).$$

    Ban đầu, $r_0 = \frac{a_0}{1}$ và $r_1 = \frac{a_0 a_1 + 1}{a_1}$, do đó:

    $$\begin{align}P_0(a_0)&=a_0,\\ P_1(a_0, a_1) &= a_0 a_1 + 1.\end{align}$$

    Để đảm bảo tính nhất quán, ta định nghĩa $P_{-1} = 1$ và $P_{-2}=0$, từ đó viết một cách hình thức là $r_{-1} = \frac{1}{0}$ và $r_{-2}=\frac{0}{1}$.

    Từ giải tích số, ta đã biết rằng định thức của một ma trận tam chéo (tridiagonal matrix) bất kỳ:

    $$T_k = \det \begin{bmatrix}
    a_0 & b_0 & 0 & \dots & 0 \\
    c_0 & a_1 & b_1 & \dots & 0 \\
    0 & c_1 & a_2 & . & \vdots \\
    \vdots & \vdots & . & \ddots & c_{k-1} \\
    0 & 0 & \dots & b_{k-1} & a_k
    \end{bmatrix}$$

    có thể được tính đệ quy là $T_k = a_k T_{k-1} - b_{k-1} c_{k-1} T_{k-2}$. So sánh nó với $P_k$, ta nhận được biểu thức trực tiếp:

    $$P_k = \det \begin{bmatrix}
    x_k & 1 & 0 & \dots & 0 \\
    -1 & x_{k-1} & 1 & \dots & 0 \\
    0 & -1 & x_2 & . & \vdots \\
    \vdots & \vdots & . & \ddots & 1 \\
    0 & 0 & \dots & -1 & x_0
    \end{bmatrix}_{\textstyle .}$$

    Đa thức này còn được gọi là [continuant](https://en.wikipedia.org/wiki/Continuant_(mathematics)) do mối quan hệ chặt chẽ của nó với liên phân số. Continuant sẽ không thay đổi nếu dãy trên đường chéo chính bị đảo ngược. Điều này cho ta công thức tính thay thế:

    $$P_k(a_0, \dots, a_k) = a_k P_{k-1}(a_0, \dots, a_{k-1}) + P_{k-2}(a_0, \dots, a_{k-2}).$$

### Cài đặt

Chúng ta sẽ tính toán các phân số hội tụ dưới dạng một cặp dãy số $p_{-2}, p_{-1}, p_0, p_1, \dots, p_k$ và $q_{-2}, q_{-1}, q_0, q_1, \dots, q_k$:

=== "C++"
    ```cpp
    auto convergents(vector<int> a) {
        vector<int> p = {0, 1};
        vector<int> q = {1, 0};
        for(auto it: a) {
            p.push_back(p[p.size() - 1] * it + p[p.size() - 2]);
            q.push_back(q[q.size() - 1] * it + q[q.size() - 2]);
        }
        return make_pair(p, q);
    }
    ```
=== "Python"
    ```py
    def convergents(a):
        p = [0, 1]
        q = [1, 0]
        for it in a:
            p.append(p[-1]*it + p[-2])
            q.append(q[-1]*it + q[-2])
        return p, q
    ```

## Cây liên phân số

Có hai cách chính để tổ chức tất cả các liên phân số có thể có vào các cấu trúc cây hữu ích.

### Cây Stern-Brocot

[Cây Stern-Brocot](../others/stern_brocot_tree_farey_sequences.md) là một cây tìm kiếm nhị phân chứa tất cả các số hữu tỉ dương phân biệt.

Cây nhìn chung có dạng như sau:

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/37/SternBrocotTree.svg">
<figcaption>
<a href="https://commons.wikimedia.org/wiki/File:SternBrocotTree.svg">Hình ảnh</a> của <a href="https://commons.wikimedia.org/wiki/User:Aaron_Rotenberg">Aaron Rotenberg</a> được cấp phép dưới <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA 3.0</a>
</figcaption>
</figure>

Các phân số $\frac{0}{1}$ và $\frac{1}{0}$ được giữ "ảo" lần lượt ở bên trái và bên phải của cây.

Khi đó phân số tại một nút là trung số (mediant) $\frac{a+c}{b+d}$ của hai phân số $\frac{a}{b}$ và $\frac{c}{d}$ ở phía trên nó.

Hệ thức truy hồi $\frac{p_k}{q_k}=\frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}}$ có nghĩa là biểu diễn liên phân số mã hóa đường đi đến $\frac{p_k}{q_k}$ trong cây. Để tìm $[a_0; a_1, \dots, a_{k}, 1]$, ta phải thực hiện $a_0$ bước sang phải, $a_1$ bước sang trái, $a_2$ bước sang phải, và cứ tiếp tục như vậy cho đến $a_k$.

Nút cha của $[a_0; a_1, \dots, a_k,1]$ khi đó là phân số nhận được bằng cách lùi lại một bước theo hướng cuối cùng đã đi.

Nói cách khác, đó là $[a_0; a_1, \dots, a_k-1,1]$ khi $a_k > 1$ và $[a_0; a_1, \dots, a_{k-1}, 1]$ khi $a_k = 1$.

Do đó, các con của $[a_0; a_1, \dots, a_k, 1]$ là $[a_0; a_1, \dots, a_k+1, 1]$ và $[a_0; a_1, \dots, a_k, 1, 1]$.

Hãy đánh chỉ số cho cây Stern-Brocot. Nút gốc được gán chỉ số $1$. Sau đó đối với một nút $v$, chỉ số của con bên trái được gán bằng cách thay đổi bit dẫn đầu của $v$ từ $1$ thành $10$, và đối với con bên phải, nó được gán bằng cách thay đổi bit dẫn đầu từ $1$ thành $11$:

<figure><img src="https://upload.wikimedia.org/wikipedia/commons/1/18/Stern-brocot-index.svg" width="500px"/></figure>

Trong cách đánh chỉ số này, biểu diễn liên phân số của một số hữu tỉ xác định mã hóa độ dài loạt chạy (run-length encoding) của chỉ số nhị phân của nó.

Đối với $\frac{5}{2} = [2;2] = [2;1,1]$, chỉ số của nó là $1011_2$ và mã hóa độ dài loạt chạy của nó, xét các bit theo thứ tự tăng dần, là $[2;1,1]$.

Một ví dụ khác là $\frac{2}{5} = [0;2,2]=[0;2,1,1]$, có chỉ số là $1100_2$ và mã hóa độ dài loạt chạy của nó thực chất chính là $[0;2,2]$.

Cần lưu ý rằng cây Stern-Brocot thực chất là một cấu trúc [treap](../data_structures/treap.md). Nghĩa là, nó là một cây tìm kiếm nhị phân đối với giá trị phân số $\frac{p}{q}$, nhưng đồng thời là cấu trúc heap đối với cả tử số $p$ và mẫu số $q$.

!!! example "So sánh các liên phân số"
    Bạn được cho $A=[a_0; a_1, \dots, a_n]$ và $B=[b_0; b_1, \dots, b_m]$. Phân số nào nhỏ hơn?
??? hint "Lời giải"
    Giả định tạm thời rằng $A$ và $B$ là các số vô tỉ và biểu diễn liên phân số của chúng biểu thị một đường đi xuống vô hạn trong cây Stern-Brocot.

    Như đã đề cập, trong biểu diễn này, $a_0$ biểu thị số lần rẽ phải trong quá trình đi xuống, $a_1$ biểu thị số lần rẽ trái tiếp theo, và vân vân. Do đó, khi so sánh $a_k$ và $b_k$, nếu $a_k = b_k$, chúng ta chỉ cần chuyển sang so sánh $a_{k+1}$ và $b_{k+1}$. Ngược lại, nếu chúng ta đang ở các bước rẽ phải, chúng ta cần kiểm tra xem $a_k < b_k$, và nếu ở các bước rẽ trái, chúng ta cần kiểm tra xem $a_k > b_k$ để xác định liệu $A < B$ hay không.

    Nói cách khác, đối với số vô tỉ $A$ và $B$, ta có $A < B$ khi và chỉ khi $(a_0, -a_1, a_2, -a_3, \dots) < (b_0, -b_1, b_2, -b_3, \dots)$ theo so sánh thứ tự từ điển.

    Bây giờ, bằng cách sử dụng một cách hình thức ký tự $\infty$ như một phần tử của liên phân số, chúng ta có thể mô phỏng các số vô tỉ $A-\varepsilon$ và $A+\varepsilon$, tức là các phần tử nhỏ hơn (hoặc lớn hơn) $A$, nhưng lớn hơn (hoặc nhỏ hơn) bất kỳ số thực nào khác. Cụ thể, đối với $A=[a_0; a_1, \dots, a_n]$, một trong hai phần tử này có thể được mô phỏng là $[a_0; a_1, \dots, a_n, \infty]$ và phần tử kia có thể được mô phỏng là $[a_0; a_1, \dots, a_n - 1, 1, \infty]$.

    Phần tử nào tương ứng với $A-\varepsilon$ và phần tử nào tương ứng với $A+\varepsilon$ có thể được xác định bằng tính chẵn lẻ của $n$ hoặc bằng cách so sánh chúng như các số vô tỉ.

    === "Python"
        ```py
        # check if a < b assuming that a[-1] = b[-1] = infty and a != b
        def less(a, b):
            a = [(-1)**i*a[i] for i in range(len(a))]
            b = [(-1)**i*b[i] for i in range(len(b))]
            return a < b

        # [a0; a1, ..., ak] -> [a0, a1, ..., ak-1, 1]
        def expand(a):
            if a: # empty a = inf
                a[-1] -= 1
                a.append(1)
            return a

        # return a-eps, a+eps
        def pm_eps(a):
            b = expand(a.copy())
            a.append(float('inf'))
            b.append(float('inf'))
            return (a, b) if less(a, b) else (b, a)
        ```

!!! example "Điểm nguyên nằm giữa tốt nhất"
    Bạn được cho $\frac{0}{1} \leq \frac{p_0}{q_0} < \frac{p_1}{q_1} \leq \frac{1}{0}$. Tìm số hữu tỉ $\frac{p}{q}$ sao cho cặp $(q; p)$ nhỏ nhất theo thứ tự từ điển và thỏa mãn $\frac{p_0}{q_0} < \frac{p}{q} < \frac{p_1}{q_1}$.

??? hint "Lời giải"
    Theo thuật ngữ của cây Stern-Brocot, điều này có nghĩa là chúng ta cần tìm tổ tiên chung gần nhất (LCA) của $\frac{p_0}{q_0}$ và $\frac{p_1}{q_1}$. Do mối liên hệ giữa cây Stern-Brocot và liên phân số, LCA này sẽ tương ứng với tiền tố chung lớn nhất của biểu diễn liên phân số cho $\frac{p_0}{q_0}$ và $\frac{p_1}{q_1}$.

    Do đó, nếu $\frac{p_0}{q_0} = [a_0; a_1, \dots, a_{k-1}, a_k, \dots]$ và $\frac{p_1}{q_1} = [a_0; a_1, \dots, a_{k-1}, b_k, \dots]$ là các số vô tỉ, thì LCA sẽ là $[a_0; a_1, \dots, \min(a_k, b_k)+1]$.

    Đối với các số hữu tỉ $r_0$ và $r_1$, một trong số chúng có thể chính là LCA, điều này yêu cầu chúng ta phải chia trường hợp xử lý. Để đơn giản hóa lời giải cho số hữu tỉ $r_0$ và $r_1$, chúng ta có thể sử dụng biểu diễn liên phân số của $r_0 + \varepsilon$ và $r_1 - \varepsilon$ đã được xây dựng ở bài toán trước.

    === "Python"
        ```py
        # finds lexicographically smallest (q, p)
        # such that p0/q0 < p/q < p1/q1
        def middle(p0, q0, p1, q1):
            a0 = pm_eps(fraction(p0, q0))[1]
            a1 = pm_eps(fraction(p1, q1))[0]
            a = []
            for i in range(min(len(a0), len(a1))):
                a.append(min(a0[i], a1[i]))
                if a0[i] != a1[i]:
                    break
            a[-1] += 1
            p, q = convergents(a)
            return p[-1], q[-1]
        ```

!!! example "[GCJ 2019, Round 2 - New Elements: Part 2](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146184)"
    Bạn được cho $N$ cặp số nguyên dương $(C_i, J_i)$. Bạn cần tìm một cặp số nguyên dương $(x, y)$ sao cho dãy $C_i x + J_i y$ là một dãy tăng ngặt.

    Trong số các cặp như vậy, hãy tìm cặp nhỏ nhất theo thứ tự từ điển.
??? hint "Lời giải"
    Phát biểu lại yêu cầu, $A_i x + B_i y$ phải dương với mọi $i$, trong đó $A_i = C_i - C_{i-1}$ và $B_i = J_i - J_{i-1}$.

    Trong số các bất phương trình này, chúng ta có bốn nhóm quan trọng cho điều kiện $A_i x + B_i y > 0$:

    1. $A_i, B_i > 0$ có thể bỏ qua vì chúng ta đang tìm $x, y > 0$.
    2. $A_i, B_i \leq 0$ sẽ đưa ra câu trả lời là "IMPOSSIBLE".
    3. $A_i > 0$, $B_i \leq 0$. Các ràng buộc này tương đương với $\frac{y}{x} < \frac{A_i}{-B_i}$.
    4. $A_i \leq 0$, $B_i > 0$. Các ràng buộc này tương đương với $\frac{y}{x} > \frac{-A_i}{B_i}$.

    Gọi $\frac{p_0}{q_0}$ là giá trị lớn nhất của $\frac{-A_i}{B_i}$ từ nhóm thứ tư, và $\frac{p_1}{q_1}$ là giá trị nhỏ nhất của $\frac{A_i}{-B_i}$ từ nhóm thứ ba.

    Bài toán bây giờ quy về: cho $\frac{p_0}{q_0} < \frac{p_1}{q_1}$, tìm phân số $\frac{p}{q}$ sao cho cặp $(q;p)$ nhỏ nhất theo thứ tự từ điển và thỏa mãn $\frac{p_0}{q_0} < \frac{p}{q} < \frac{p_1}{q_1}$.
    === "Python"
        ```py
            def solve():
            n = int(input())
            C = [0] * n
            J = [0] * n
            # p0/q0 < y/x < p1/q1
            p0, q0 = 0, 1
            p1, q1 = 1, 0
            fail = False
            for i in range(n):
                C[i], J[i] = map(int, input().split())
                if i > 0:
                    A = C[i] - C[i-1]
                    B = J[i] - J[i-1]
                    if A <= 0 and B <= 0:
                        fail = True
                    elif B > 0 and A < 0: # y/x > (-A)/B if B > 0
                        if (-A)*q0 > p0*B:
                            p0, q0 = -A, B
                    elif B < 0 and A > 0: # y/x < A/(-B) if B < 0
                        if A*q1 < p1*(-B):
                            p1, q1 = A, -B
            if p0*q1 >= p1*q0 or fail:
                return 'IMPOSSIBLE'

            p, q = middle(p0, q0, p1, q1)
            return str(q) + ' ' + str(p)
        ```

### Cây Calkin-Wilf

Một cách đơn giản hơn để tổ chức các liên phân số dưới dạng cây nhị phân là [Cây Calkin-Wilf](https://en.wikipedia.org/wiki/Calkin–Wilf_tree).

Cây nhìn chung có dạng như sau:

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Calkin–Wilf_tree.svg" width="500px"/>
<figcaption><a href="https://commons.wikimedia.org/wiki/File:Calkin–Wilf_tree.svg">Hình ảnh</a> bởi <a href="https://commons.wikimedia.org/wiki/User:Olli_Niemitalo">Olli Niemitalo</a>, <a href="https://commons.wikimedia.org/wiki/User:Proz">Proz</a> được cấp phép dưới dạng <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.en">CC0 1.0</a></figcaption>
</figure>

Tại nút gốc của cây, số $\frac{1}{1}$ được đặt. Sau đó, đối với nút có giá trị $\frac{p}{q}$, các con của nó là $\frac{p}{p+q}$ và $\frac{p+q}{q}$.

Khác với cây Stern-Brocot, cây Calkin-Wilf không phải là một cây *tìm kiếm* nhị phân, do đó nó không thể được sử dụng để thực hiện tìm kiếm nhị phân số hữu tỉ.

Trong cây Calkin-Wilf, nút cha trực tiếp của phân số $\frac{p}{q}$ là $\frac{p-q}{q}$ khi $p>q$ và $\frac{p}{q-p}$ trong trường hợp ngược lại.

Đối với cây Stern-Brocot, chúng ta đã sử dụng công thức truy hồi cho các phân số hội tụ. Để rút ra mối liên hệ giữa liên phân số và cây Calkin-Wilf, chúng ta nên nhớ lại công thức truy hồi cho các thương đầy đủ. Nếu $s_k = \frac{p}{q}$, thì $s_{k+1} = \frac{q}{p \mod q} = \frac{q}{p-\lfloor p/q \rfloor \cdot q}$.

Mặt khác, nếu chúng ta liên tục đi từ $s_k = \frac{p}{q}$ lên nút cha của nó trong cây Calkin-Wilf khi $p > q$, chúng ta sẽ dừng lại ở $\frac{p \mod q}{q} = \frac{1}{s_{k+1}}$. Nếu tiếp tục làm vậy, chúng ta sẽ dừng lại ở $s_{k+2}$, rồi $\frac{1}{s_{k+3}}$, vân vân. Từ đây ta có thể suy ra rằng:

1. Khi $a_0> 0$, nút cha trực tiếp của $[a_0; a_1, \dots, a_k]$ trong cây Calkin-Wilf là $\frac{p-q}{q}=[a_0 - 1; a_1, \dots, a_k]$.
2. Khi $a_0 = 0$ và $a_1 > 1$, nút cha trực tiếp của nó là $\frac{p}{q-p} = [0; a_1 - 1, a_2, \dots, a_k]$.
3. Và khi $a_0 = 0$ và $a_1 = 1$, nút cha trực tiếp của nó là $\frac{p}{q-p} = [a_2; a_3, \dots, a_k]$.

Tương ứng, các con của $\frac{p}{q} = [a_0; a_1, \dots, a_k]$ là:

1. $\frac{p+q}{q}=1+\frac{p}{q}$, chính là $[a_0+1; a_1, \dots, a_k]$,
2. $\frac{p}{p+q} = \frac{1}{1+\frac{q}{p}}$, chính là $[0, 1, a_0, a_1, \dots, a_k]$ khi $a_0 > 0$ và $[0, a_1+1, a_2, \dots, a_k]$ khi $a_0=0$.

Đáng chú ý, nếu chúng ta đánh số các nút của cây Calkin-Wilf theo thứ tự duyệt theo chiều rộng (nghĩa là nút gốc có số $1$, và các con của nút $v$ có chỉ số là $2v$ và $2v+1$ tương ứng), thì chỉ số của số hữu tỉ trong cây Calkin-Wilf sẽ trùng với chỉ số trong cây Stern-Brocot.

Do đó, các số trên cùng một tầng của cây Stern-Brocot và cây Calkin-Wilf là giống nhau, nhưng thứ tự của chúng khác nhau qua [hoán vị đảo bit (bit-reversal permutation)](https://en.wikipedia.org/wiki/Bit-reversal_permutation).

## Tính hội tụ

Đối với số $r$ và phân số hội tụ thứ $k$ của nó $r_k=\frac{p_k}{q_k}$, ta có công thức sau:

$$r_k = a_0 + \sum\limits_{i=1}^k \frac{(-1)^{i-1}}{q_i q_{i-1}}.$$

Đặc biệt, điều này có nghĩa là:

$$r_k - r_{k-1} = \frac{(-1)^{k-1}}{q_k q_{k-1}}$$

và:

$$p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}.$$

Từ đây chúng ta có thể kết luận rằng:

$$\left| r-\frac{p_k}{q_k} \right| \leq \frac{1}{q_{k+1}q_k} \leq \frac{1}{q_k^2}.$$

Bất đẳng thức sau là do thực tế là $r_k$ và $r_{k+1}$ luôn nằm ở hai phía khác nhau của $r$, do đó:

$$|r-r_k| = |r_k-r_{k+1}|-|r-r_{k+1}| \leq |r_k - r_{k+1}|.$$

??? tip "Giải thích chi tiết"

    Để đánh giá $|r-r_k|$, chúng ta bắt đầu bằng cách đánh giá hiệu giữa các phân số hội tụ kề nhau. Theo định nghĩa:

    $$\frac{p_k}{q_k} - \frac{p_{k-1}}{q_{k-1}} = \frac{p_k q_{k-1} - p_{k-1} q_k}{q_k q_{k-1}}.$$

    Thay thế $p_k$ và $q_k$ ở tử số bằng hệ thức truy hồi của chúng, ta được:

    $$\begin{align} p_k q_{k-1} - p_{k-1} q_k &= (a_k p_{k-1} + p_{k-2}) q_{k-1} - p_{k-1} (a_k q_{k-1} + q_{k-2})
    \\&= p_{k-2} q_{k-1} - p_{k-1} q_{k-2},\end{align}$$

    do đó tử số của $r_k - r_{k-1}$ luôn đối dấu với tử số của $r_{k-1} - r_{k-2}$. Nó bằng $1$ cho hiệu ban đầu:

    $$r_1 - r_0=\left(a_0+\frac{1}{a_1}\right)-a_0=\frac{1}{a_1},$$

    do đó ta thu được:

    $$r_k - r_{k-1} = \frac{(-1)^{k-1}}{q_k q_{k-1}}.$$

    Điều này cho phép biểu diễn $r_k$ dưới dạng tổng riêng của một chuỗi vô hạn:

    $$r_k = (r_k - r_{k-1}) + \dots + (r_1 - r_0) + r_0
    = a_0 + \sum\limits_{i=1}^k \frac{(-1)^{i-1}}{q_i q_{i-1}}.$$

    Từ hệ thức truy hồi suy ra $q_k$ tăng đơn điệu nhanh ít nhất bằng dãy số Fibonacci, do đó giới hạn:

    $$r = \lim\limits_{k \to \infty} r_k = a_0 + \sum\limits_{i=1}^\infty \frac{(-1)^{i-1}}{q_i q_{i-1}}$$

    luôn được xác định rõ ràng, vì chuỗi số tương ứng luôn hội tụ. Đáng chú ý, chuỗi phần dư:

    $$r-r_k = \sum\limits_{i=k+1}^\infty \frac{(-1)^{i-1}}{q_i q_{i-1}}$$

    có cùng dấu với $(-1)^k$ do tốc độ giảm nhanh của $q_i q_{i-1}$. Do đó, các phân số hội tụ có chỉ số chẵn $r_k$ tiến tới $r$ từ phía dưới, trong khi các phân số hội tụ có chỉ số lẻ $r_k$ tiến tới nó từ phía trên:

    <figure><img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Golden_ration_convergents.svg" width="600px"/>
    <figcaption>_Các phân số hội tụ của $r=\phi = \frac{1+\sqrt{5}}{2}=[1;1,1,\dots]$ và khoảng cách của chúng đến $r$._</figcaption></figure>

    Từ hình ảnh này ta thấy rằng:

    $$|r-r_k| = |r_k - r_{k+1}| - |r-r_{k+1}| \leq |r_k - r_{k+1}|,$$

    do đó khoảng cách giữa $r$ và $r_k$ không bao giờ lớn hơn khoảng cách giữa $r_k$ và $r_{k+1}$:

    $$\left|r-\frac{p_k}{q_k}\right| \leq \frac{1}{q_k q_{k+1}} \leq \frac{1}{q_k^2}.$$

!!! example "Thuật toán Euclid mở rộng?"
    Bạn được cho các số nguyên $A, B, C \in \mathbb Z$. Tìm các số nguyên $x, y \in \mathbb Z$ sao cho $Ax + By = C$.
??? hint "Lời giải"
    Mặc dù bài toán này thường được giải quyết bằng [thuật toán Euclid mở rộng](../algebra/extended-euclid-algorithm.md), nhưng có một lời giải rất đơn giản và trực quan sử dụng liên phân số.

    Gọi $\frac{A}{B}=[a_0; a_1, \dots, a_k]$. Ta đã chứng minh ở trên rằng $p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}$. Thay thế $p_k$ và $q_k$ bằng $A$ và $B$, ta được:

    $$Aq_{k-1} - Bp_{k-1} = (-1)^{k-1} g,$$

    trong đó $g = \gcd(A, B)$. Nếu $C$ chia hết cho $g$, thì nghiệm của phương trình là $x = (-1)^{k-1}\frac{C}{g} q_{k-1}$ và $y = (-1)^{k}\frac{C}{g} p_{k-1}$.
    
    === "Python"
        ```py
        # return (x, y) such that Ax+By=C
        # assumes that such (x, y) exists
        def dio(A, B, C):
            p, q = convergents(fraction(A, B))
            C //= A // p[-1] # divide by gcd(A, B)
            t = (-1) if len(p) % 2 else 1
            return t*C*q[-2], -t*C*p[-2]
        ```

## Phép biến đổi phân tuyến tính

Một khái niệm quan trọng khác đối với liên phân số là các **phép biến đổi phân tuyến tính (linear fractional transformations)**.

!!! info "Định nghĩa"
    Một **phép biến đổi phân tuyến tính** là một hàm số $f : \mathbb R \to \mathbb R$ sao cho $f(x) = \frac{ax+b}{cx+d}$ với các số thực $a,b,c,d \in \mathbb R$ nào đó.

Hợp thành $(L_0 \circ L_1)(x) = L_0(L_1(x))$ của hai phép biến đổi phân tuyến tính $L_0(x)=\frac{a_0 x + b_0}{c_0 x + d_0}$ và $L_1(x)=\frac{a_1 x + b_1}{c_1 x + d_1}$ cũng là một phép biến đổi phân tuyến tính:

$$\frac{a_0\frac{a_1 x + b_1}{c_1 x + d_1} + b_0}{c_0 \frac{a_1 x + b_1}{c_1 x + d_1} + d_0} = \frac{a_0(a_1 x + b_1) + b_0 (c_1 x + d_1)}{c_0 (a_1 x + b_1) + d_0 (c_1 x + d_1)} = \frac{(a_0 a_1 + b_0 c_1) x + (a_0 b_1 + b_0 d_1)}{(c_0 a_1 + d_0 c_1) x + (c_0 b_1 + d_0 d_1)}.$$

Hàm ngược của một phép biến đổi phân tuyến tính cũng là một phép biến đổi phân tuyến tính:

$$y = \frac{ax+b}{cx+d} \iff y(cx+d) = ax + b \iff x = -\frac{dy-b}{cy-a}.$$

!!! example "[DMOPC '19 Contest 7 P4 - Bob and Continued Fractions](https://dmoj.ca/problem/dmopc19c7p4)"
    Bạn được cho một mảng các số nguyên dương $a_1, \dots, a_n$. Bạn cần trả lời $m$ truy vấn. Mỗi truy vấn yêu cầu tính giá trị $[a_l; a_{l+1}, \dots, a_r]$.
??? hint "Lời giải"
    Chúng ta có thể giải quyết bài toán này bằng cây phân đoạn (segment tree) nếu có thể thực hiện ghép các liên phân số.

    Nói chung, ta luôn có đẳng thức $[a_0; a_1, \dots, a_k, b_0, b_1, \dots, b_k] = [a_0; a_1, \dots, a_k, [b_1; b_2, \dots, b_k]]$.

    Hãy ký hiệu $L_{k}(x) = [a_k; x] = a_k + \frac{1}{x} = \frac{a_k\cdot x+1}{1\cdot x + 0}$. Lưu ý rằng $L_k(\infty) = a_k$. Theo cách ký hiệu này, ta có:

    $$[a_0; a_1, \dots, a_k, x] = [a_0; [a_1; [\dots; [a_k; x]]]] = (L_0 \circ L_1 \circ \dots \circ L_k)(x) = \frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}.$$

    Do đó, bài toán quy về việc tính toán tích hợp thành:

    $$(L_l \circ L_{l+1} \circ \dots \circ L_r)(\infty).$$

    Phép toán hợp thành các phép biến đổi có tính kết hợp, do đó ta có thể tính toán trong mỗi nút của cây phân đoạn phép hợp thành các biến đổi trong cây con của nó.

!!! example "Biến đổi phân tuyến tính của một liên phân số"
    Cho $L(x) = \frac{ax+b}{cx+d}$. Tính biểu diễn liên phân số $[b_0; b_1, \dots, b_m]$ của $L(A)$ với $A=[a_0; a_1, \dots, a_n]$.

    _Điều này cho phép tính $A + \frac{p}{q} = \frac{qA + p}{q}$ và $A \cdot \frac{p}{q} = \frac{p A}{q}$ với phân số $\frac{p}{q}$ bất kỳ._

??? hint "Lời giải"
    Như đã lưu ý ở trên, $[a_0; a_1, \dots, a_k] = (L_{a_0} \circ L_{a_1} \circ \dots \circ L_{a_k})(\infty)$, do đó $L([a_0; a_1, \dots, a_k]) = (L \circ L_{a_0} \circ L_{a_1} \circ \dots L_{a_k})(\infty)$.

    Vì vậy, bằng cách lần lượt thêm các biến đổi $L_{a_0}$, $L_{a_1}$, vân vân, chúng ta có thể tính được:

    $$(L \circ L_{a_0} \circ \dots \circ L_{a_k})(x) = L\left(\frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}\right)=\frac{a_k x + b_k}{c_k x + d_k}.$$

    Vì $L(x)$ khả nghịch nên nó cũng đơn điệu đối với $x$. Do đó, với mọi $x \geq 0$, ta có $L(\frac{p_k x + p_{k-1}}{q_k x + q_{k-1}})$ nằm giữa $L(\frac{p_k}{q_k}) = \frac{a_k}{c_k}$ và $L(\frac{p_{k-1}}{q_{k-1}}) = \frac{b_k}{d_k}$.

    Hơn nữa, với $x=[a_{k+1}; \dots, a_n]$, nó bằng $L(A)$. Do đó, $b_0 = \lfloor L(A) \rfloor$ nằm giữa $\lfloor L(\frac{p_k}{q_k}) \rfloor$ và $\lfloor L(\frac{p_{k-1}}{q_{k-1}}) \rfloor$. Khi hai giá trị này bằng nhau, chúng cũng bằng $b_0$.

    Lưu ý rằng $L(A) = (L_{b_0} \circ L_{b_1} \circ \dots \circ L_{b_m})(\infty)$. Khi biết $b_0$, chúng ta có thể thực hiện hợp thành $L_{b_0}^{-1}$ với biến đổi hiện tại và tiếp tục thêm $L_{a_{k+1}}$, $L_{a_{k+2}}$, vân vân, để tìm các phần nguyên khớp nhau, từ đó suy ra $b_1$ và cứ tiếp tục như vậy cho đến khi khôi phục tất cả các giá trị của $[b_0; b_1, \dots, b_m]$.

!!! example "Số học trên liên phân số"
    Cho $A=[a_0; a_1, \dots, a_n]$ và $B=[b_0; b_1, \dots, b_m]$. Tính biểu diễn liên phân số của $A+B$ và $A \cdot B$.
??? hint "Lời giải"
    Ý tưởng ở đây tương tự như bài toán trước, nhưng thay vì $L(x) = \frac{ax+b}{cx+d}$ bạn nên xem xét phép biến đổi phân song tuyến tính (bilinear fractional transform) $L(x, y) = \frac{axy+bx+cy+d}{exy+fx+gy+h}$.

    Thay vì $L(x) \mapsto L(L_{a_k}(x))$ bạn sẽ thay đổi biến đổi hiện tại thành $L(x, y) \mapsto L(L_{a_k}(x), y)$ hoặc $L(x, y) \mapsto L(x, L_{b_k}(y))$.

    Sau đó, bạn kiểm tra xem các giá trị $\lfloor \frac{a}{e} \rfloor = \lfloor \frac{b}{f} \rfloor = \lfloor \frac{c}{g} \rfloor = \lfloor \frac{d}{h} \rfloor$ có bằng nhau hay không. Nếu tất cả chúng bằng nhau, bạn sử dụng giá trị này làm $c_k$ trong phân số kết quả và thay đổi biến đổi hiện tại thành:

    $$L(x, y) \mapsto \frac{1}{L(x, y) - c_k}.$$

!!! info "Định nghĩa"
    Một liên phân số $x = [a_0; a_1, \dots]$ được gọi là **tuần hoàn (periodic)** nếu $x = [a_0; a_1, \dots, a_k, x]$ với một số nguyên $k$ nào đó.

    Một liên phân số $x = [a_0; a_1, \dots]$ được gọi là **tuần hoàn kể từ lúc nào đó (eventually periodic)** nếu $x = [a_0; a_1, \dots, a_k, y]$, trong đó $y$ là một liên phân số tuần hoàn.

Đối với $x = [1; 1, 1, \dots]$, ta có $x = 1 + \frac{1}{x}$, do đó $x^2 = x + 1$. Có một mối liên hệ tổng quát giữa các liên phân số tuần hoàn và phương trình bậc hai. Xét phương trình sau:

$$ x = [a_0; a_1, \dots, a_k, x].$$

Một mặt, phương trình này có nghĩa là biểu diễn liên phân số của $x$ là tuần hoàn với chu kỳ $k+1$.

Mặt khác, sử dụng công thức tính phân số hội tụ, phương trình này có nghĩa là:

$$x = \frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}.$$

Nghĩa là, $x$ là một phép biến đổi phân tuyến tính của chính nó. Từ phương trình này, suy ra $x$ là nghiệm của một phương trình bậc hai:

$$q_k x^2 + (q_{k-1}-p_k)x - p_{k-1} = 0.$$

Lập luận tương tự cũng áp dụng cho các liên phân số tuần hoàn kể từ lúc nào đó, tức là $x = [a_0; a_1, \dots, a_k, y]$ với $y=[b_0; b_1, \dots, b_k, y]$. Thật vậy, từ phương trình thứ nhất ta rút ra $x = L_0(y)$ và từ phương trình thứ hai ta có $y = L_1(y)$, trong đó $L_0$ và $L_1$ là các phép biến đổi phân tuyến tính. Do đó:

$$x = (L_0 \circ L_1)(y) = (L_0 \circ L_1 \circ L_0^{-1})(x).$$

Người ta có thể chứng minh thêm (và điều này lần đầu tiên được thực hiện bởi Lagrange) rằng đối với phương trình bậc hai bất kỳ $ax^2+bx+c=0$ với các hệ số nguyên, nghiệm $x$ của nó luôn có biểu diễn liên phân số tuần hoàn kể từ lúc nào đó.

!!! example "Vô tỉ bậc hai (Quadratic irrationality)"
    Tìm liên phân số của số vô tỉ bậc hai $\alpha = \frac{x+y\sqrt{n}}{z}$ trong đó $x, y, z, n \in \mathbb Z$ và $n > 0$ không phải là một số chính phương.
??? hint "Lời giải"
    Đối với thương đầy đủ thứ $k$ là $s_k$ của số đó, ta luôn có:

    $$\alpha = [a_0; a_1, \dots, a_{k-1}, s_k] = \frac{s_k p_{k-1} + p_{k-2}}{s_k q_{k-1} + q_{k-2}}.$$

    Do đó:

    $$s_k = -\frac{\alpha q_{k-1} - p_{k-1}}{\alpha q_k - p_k} = -\frac{q_{k-1} y \sqrt n + (x q_{k-1} - z p_{k-1})}{q_k y \sqrt n + (xq_k-zp_k)}.$$

    Nhân cả tử và mẫu với $(xq_k - zp_k) - q_k y \sqrt n$, chúng ta sẽ loại bỏ được $\sqrt n$ ở mẫu số, do đó các thương đầy đủ có dạng:

    $$s_k = \frac{x_k + y_k \sqrt n}{z_k}.$$

    Hãy tìm $s_{k+1}$, giả sử $s_k$ đã biết.

    Trước hết, $a_k = \lfloor s_k \rfloor = \left\lfloor \frac{x_k + y_k \lfloor \sqrt n \rfloor}{z_k} \right\rfloor$. Khi đó:

    $$s_{k+1} = \frac{1}{s_k-a_k} = \frac{z_k}{(x_k - z_k a_k) + y_k \sqrt n} = \frac{z_k (x_k - y_k a_k) - y_k z_k \sqrt n}{(x_k - y_k a_k)^2 - y_k^2 n}.$$

    Do đó, nếu ký hiệu $t_k = x_k - y_k a_k$, ta có hệ thức:

    \begin{align}x_{k+1} &=& z_k t_k, \\ y_{k+1} &=& -y_k z_k, \\ z_{k+1} &=& t_k^2 - y_k^2 n.\end{align}

    Điều tuyệt vời về biểu diễn này là nếu chúng ta giản ước $x_{k+1}, y_{k+1}, z_{k+1}$ cho ước chung lớn nhất của chúng, kết quả thu được sẽ là duy nhất. Do đó, chúng ta có thể sử dụng nó để kiểm tra xem trạng thái hiện tại đã từng xuất hiện trước đó hay chưa, và chỉ số trước đó có trạng thái này là chỉ số nào.

    Dưới đây là đoạn mã tính toán biểu diễn liên phân số cho $\alpha = \sqrt n$:

    === "Python"
        ```py
        # compute the continued fraction of sqrt(n)
        def sqrt(n):
            n0 = math.floor(math.sqrt(n))
            x, y, z = 1, 0, 1
            a = []
            def step(x, y, z):
                a.append((x * n0 + y) // z)
                t = y - a[-1]*z
                x, y, z = -z*x, z*t, t**2 - n*x**2
                g = math.gcd(x, math.gcd(y, z))
                return x // g, y // g, z // g

            used = dict()
            for i in range(n):
                used[x, y, z] = i
                x, y, z = step(x, y, z)
                if (x, y, z) in used:
                    return a
        ```

    Sử dụng cùng hàm `step` này nhưng với các giá trị khởi tạo $x$, $y$ và $z$ khác nhau, chúng ta có thể tính toán liên phân số cho số $\frac{x+y \sqrt{n}}{z}$ bất kỳ.

!!! example "[Tavrida NU Akai Contest - Continued Fraction](https://timus.online/problem.aspx?space=1&num=1814)"
    Bạn được cho $x$ và $k$, với $x$ không phải số chính phương. Gọi $\sqrt x = [a_0; a_1, \dots]$, hãy tìm phân số $\frac{p_k}{q_k}=[a_0; a_1, \dots, a_k]$ với $0 \leq k \leq 10^9$.
??? hint "Lời giải"
    Sau khi tính toán chu kỳ của $\sqrt x$, ta có thể tính $a_k$ bằng cách sử dụng lũy thừa nhị phân trên phép biến đổi phân tuyến tính được tạo bởi biểu diễn liên phân số. Để tìm biến đổi kết quả, bạn nén chu kỳ có kích thước $T$ thành một biến đổi duy nhất và lặp lại nó $\lfloor \frac{k-1}{T}\rfloor$ lần, sau đó kết hợp thủ công với các biến đổi còn lại.

    === "Python"
        ```py
        x, k = map(int, input().split())

        mod = 10**9+7
        
        # compose (A[0]*x + A[1]) / (A[2]*x + A[3]) and (B[0]*x + B[1]) / (B[2]*x + B[3])
        def combine(A, B):
            return [t % mod for t in [A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3]]]

        A = [1, 0, 0, 1] # (x + 0) / (0*x + 1) = x

        a = sqrt(x)

        T = len(a) - 1 # period of a

        # apply ak + 1/x = (ak*x+1)/(1x+0) to (Ax + B) / (Cx + D)
        for i in reversed(range(1, len(a))):
            A = combine([a[i], 1, 1, 0], A)

        def bpow(A, n):
            return [1, 0, 0, 1] if not n else combine(A, bpow(A, n-1)) if n % 2 else bpow(combine(A, A), n // 2)


        C = (0, 1, 0, 0) # = 1 / 0
        while k % T:
            i = k % T
            C = combine([a[i], 1, 1, 0], C)
            k -= 1

        C = combine(bpow(A, k // T), C)
        C = combine([a[0], 1, 1, 0], C)
        print(str(C[1]) + '/' + str(C[3]))
        ```

## Ý nghĩa hình học

Gọi $\vec r_k = (q_k;p_k)$ là vector tương ứng với phân số hội tụ $r_k = \frac{p_k}{q_k}$. Khi đó, hệ thức truy hồi sau đây được thỏa mãn:

$$\vec r_k = a_k \vec r_{k-1} + \vec r_{k-2}.$$

Gọi $\vec r = (1;r)$. Khi đó, mỗi vector $(x;y)$ tương ứng với một số bằng hệ số góc (độ dốc) $\frac{y}{x}$ của nó.

Sử dụng định nghĩa của [tích vô hướng chéo (cross product)](../geometry/basic-geometry.md) $(x_1;y_1) \times (x_2;y_2) = x_1 y_2 - x_2 y_1$, ta có thể chứng minh được rằng (xem phần giải thích bên dưới):

$$s_k = -\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r} = \left|\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r}\right|.$$

Phương trình cuối cùng là do thực tế là $r_{k-1}$ và $r_{k-2}$ nằm ở hai phía khác nhau của $r$, do đó các tích vô hướng chéo của $\vec r_{k-1}$ và $\vec r_{k-2}$ với $\vec r$ có dấu trái ngược nhau. Với $a_k = \lfloor s_k \rfloor$, công thức cho $\vec r_k$ bây giờ có dạng:

$$\vec r_k = \vec r_{k-2} + \left\lfloor \left| \frac{\vec r \times \vec r_{k-2}}{\vec r \times \vec r_{k-1}}\right|\right\rfloor \vec r_{k-1}.$$

Lưu ý rằng $\vec r_k \times r = (q;p) \times (1;r) = qr - p$, do đó:

$$a_k = \left\lfloor \left| \frac{q_{k-1}r-p_{k-1}}{q_{k-2}r-p_{k-2}} \right| \right\rfloor.$$

??? hint "Giải thích"
    Như chúng ta đã biết, $a_k = \lfloor s_k \rfloor$, với $s_k = [a_k; a_{k+1}, a_{k+2}, \dots]$. Mặt khác, từ công thức truy hồi của các phân số hội tụ, ta có:

    $$r = [a_0; a_1, \dots, a_{k-1}, s_k] = \frac{s_k p_{k-1} + p_{k-2}}{s_k q_{k-1} + q_{k-2}}.$$

    Dưới dạng vector, nó được viết lại thành:

    $$\vec r \parallel s_k \vec r_{k-1} + \vec r_{k-2},$$

    nghĩa là $\vec r$ và $s_k \vec r_{k-1} + \vec r_{k-2}$ là hai vector cùng phương (tức là có cùng hệ số góc). Thực hiện tích chéo cả hai vế với $\vec r$, ta thu được:

    $$0 = s_k (\vec r_{k-1} \times \vec r) + (\vec r_{k-2} \times \vec r),$$

    cho ta công thức cuối cùng:

    $$s_k = -\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r}.$$

!!! example "Thuật toán kéo mũi (Nose stretching)"
    Mỗi khi bạn cộng thêm $\vec r_{k-1}$ vào vector $\vec p$, giá trị của tích $\vec p \times \vec r$ tăng thêm một lượng là $\vec r_{k-1} \times \vec r$.

    Do đó, $a_k=\lfloor s_k \rfloor$ là số nguyên lớn nhất các vector $\vec r_{k-1}$ có thể cộng vào $\vec r_{k-2}$ mà không làm thay đổi dấu của tích chéo với $\vec r$.

    Nói cách khác, $a_k$ là số lần nguyên tối đa bạn có thể cộng $\vec r_{k-1}$ vào $\vec r_{k-2}$ mà không vượt qua đường thẳng xác định bởi $\vec r$:

    <figure><img src="https://upload.wikimedia.org/wikipedia/commons/9/92/Continued_convergents_geometry.svg" width="700px"/>
    <figcaption>_Các phân số hội tụ của $r=\frac{7}{9}=[0;1,3,2]$. Các phân số bán hội tụ tương ứng với các điểm trung gian giữa các mũi tên màu xám._</figcaption></figure>

    Trong hình trên, $\vec r_2 = (4;3)$ thu được bằng cách cộng liên tiếp $\vec r_1 = (1;1)$ vào $\vec r_0 = (1;0)$.

    Khi không thể cộng thêm $\vec r_1$ vào $\vec r_0$ nữa mà không vượt qua đường $y=rx$, chúng ta chuyển sang phía bên kia và cộng liên tiếp $\vec r_2$ vào $\vec r_1$ để thu được $\vec r_3 = (9;7)$.

    Quy trình này tạo ra các vector dài hơn theo hàm mũ, tiệm cận gần sát đường thẳng.

    Vì tính chất này, quy trình tạo các vector hội tụ liên tiếp được Boris Delaunay gọi là **thuật toán kéo mũi (nose stretching algorithm)**.

Nếu chúng ta xét tam giác được tạo bởi các điểm $\vec r_{k-2}$, $\vec r_{k}$ và $\vec 0$, chúng ta sẽ thấy rằng diện tích gấp đôi của nó là:

$$|\vec r_{k-2} \times \vec r_k| = |\vec r_{k-2} \times (\vec r_{k-2} + a_k \vec r_{k-1})| = a_k |\vec r_{k-2} \times \vec r_{k-1}| = a_k.$$

Kết hợp với [Định lý Pick](../geometry/picks-theorem.md), điều này có nghĩa là không có điểm nguyên nào nằm hoàn toàn bên trong tam giác và các điểm nguyên duy nhất trên biên của nó là $\vec 0$ và $\vec r_{k-2} + t \cdot \vec r_{k-1}$ với mọi số nguyên $t$ thỏa mãn $0 \leq t \leq a_k$. Khi kết hợp lại cho tất cả các giá trị $k$, điều này có nghĩa là không có điểm nguyên nào nằm trong khoảng trống giữa các đa giác tạo bởi các vector hội tụ chỉ số chẵn và chỉ số lẻ.

Điều này có nghĩa là các vector $\vec r_k$ với chỉ số lẻ tạo thành bao lồi của các điểm nguyên có $x \geq 0$ nằm phía trên đường thẳng $y=rx$, trong khi các vector $\vec r_k$ với chỉ số chẵn tạo thành bao lồi của các điểm nguyên có $x > 0$ nằm phía dưới đường thẳng $y=rx$.

!!! info "Định nghĩa"
    Các đa giác này được gọi là **đa giác Klein (Klein polygons)**, đặt theo tên của Felix Klein, người đầu tiên đề xuất cách giải thích hình học này cho liên phân số.

## Các ví dụ bài toán

Bây giờ các khái niệm và tính chất quan trọng nhất đã được giới thiệu, đã đến lúc đi sâu vào các ví dụ bài toán cụ thể.

!!! example "Bao lồi dưới đường thẳng"
    Tìm bao lồi của các điểm nguyên $(x;y)$ sao cho $0 \leq x \leq N$ và $0 \leq y \leq rx$ với $r=[a_0;a_1,\dots,a_k]=\frac{p_k}{q_k}$.

??? hint "Lời giải"
    Nếu chúng ta xem xét tập hợp không giới hạn $0 \leq x$, bao lồi phía trên sẽ chính là đường thẳng $y=rx$.

    Tuy nhiên, với ràng buộc bổ sung $x \leq N$ chúng ta sẽ phải lệch khỏi đường thẳng tại một thời điểm nào đó để duy trì bao lồi hợp lệ.

    Gọi $t = \lfloor \frac{N}{q_k}\rfloor$, khi đó $t$ điểm nguyên đầu tiên trên bao lồi sau điểm $(0;0)$ là $\alpha \cdot (q_k; p_k)$ với số nguyên $1 \leq \alpha \leq t$.

    Tuy nhiên, $(t+1)(q_k; p_k)$ không thể là điểm nguyên tiếp theo vì $(t+1)q_k$ lớn hơn $N$.

    Để tìm các điểm nguyên tiếp theo trên bao lồi, chúng ta phải đi đến điểm nguyên $(x;y)$ lệch khỏi đường thẳng $y=rx$ với khoảng cách nhỏ nhất, đồng thời vẫn phải thỏa mãn $x \leq N$.

    <figure><img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Lattice-hull.svg" width="500px"/>
    <figcaption>Bao lồi của các điểm nguyên dưới đường thẳng $y=\frac{4}{7}x$ với $0 \leq x \leq 19$ gồm các điểm $(0;0), (7;4), (14;8), (16;9), (18;10), (19;10)$.</figcaption></figure>

    Gọi $(x; y)$ là điểm hiện tại cuối cùng trên bao lồi. Khi đó điểm tiếp theo $(x'; y')$ phải thỏa mãn $x' \leq N$ và hiệu $(x'; y') - (x; y) = (\Delta x; \Delta y)$ nằm sát đường thẳng $y=rx$ nhất có thể. Nói cách khác, hiệu $(\Delta x; \Delta y)$ cực đại hóa biểu thức $r \Delta x - \Delta y$ thỏa mãn $\Delta x \leq N - x$ và $\Delta y \leq r \Delta x$.

    Các điểm như vậy nằm trên bao lồi của các điểm nguyên phía dưới đường thẳng $y=rx$. Nói cách khác, $(\Delta x; \Delta y)$ phải là một phân số bán hội tụ dưới của $r$.

    Do đó, $(\Delta x; \Delta y)$ có dạng $(q_{i-1}; p_{i-1}) + t \cdot (q_i; p_i)$ với chỉ số lẻ $i$ nào đó và $0 \leq t < a_i$.

    Để tìm $i$ như vậy, chúng ta có thể duyệt qua tất cả các giá trị $i$ khả dĩ bắt đầu từ giá trị lớn nhất và chọn $t = \lfloor \frac{N-x-q_{i-1}}{q_i} \rfloor$ cho chỉ số $i$ thỏa mãn $N-x-q_{i-1} \geq 0$.

    Với $(\Delta x; \Delta y) = (q_{i-1}; p_{i-1}) + t \cdot (q_i; p_i)$, điều kiện $\Delta y \leq r \Delta x$ sẽ được bảo toàn nhờ các tính chất của phân số bán hội tụ.

    Và điều kiện $t < a_i$ sẽ được thỏa mãn vì chúng ta đã vét hết các phân số bán hội tụ thu được từ $i+2$, do đó $x + q_{i-1} + a_i q_i = x+q_{i+1}$ chắc chắn lớn hơn $N$.

    Bây giờ chúng ta có thể cộng $(\Delta x; \Delta y)$ vào $(x;y)$ tổng cộng $k = \lfloor \frac{N-x}{\Delta x} \rfloor$ lần trước khi nó vượt quá $N$, sau đó chúng ta tiếp tục thử với phân số bán hội tụ tiếp theo.

    === "C++"
        ```cpp
        // returns [ah, ph, qh] such that points r[i]=(ph[i], qh[i]) constitute upper convex hull
        // of lattice points on 0 <= x <= N and 0 <= y <= r * x, where r = [a0; a1, a2, ...]
        // and there are ah[i]-1 integer points on the segment between r[i] and r[i+1]
        auto hull(auto a, int N) {
            auto [p, q] = convergents(a);
            int t = N / q.back();
            vector ah = {t};
            vector ph = {0, t*p.back()};
            vector qh = {0, t*q.back()};

            for(int i = q.size() - 1; i >= 0; i--) {
                if(i % 2) {
                    while(qh.back() + q[i - 1] <= N) {
                        t = (N - qh.back() - q[i - 1]) / q[i];
                        int dp = p[i - 1] + t * p[i];
                        int dq = q[i - 1] + t * q[i];
                        int k = (N - qh.back()) / dq;
                        ah.push_back(k);
                        ph.push_back(ph.back() + k * dp);
                        qh.push_back(qh.back() + k * dq);
                    }
                }
            }
            return make_tuple(ah, ph, qh);
        }
        ```
    === "Python"
        ```py
        # returns [ah, ph, qh] such that points r[i]=(ph[i], qh[i]) constitute upper convex hull
        # of lattice points on 0 <= x <= N and 0 <= y <= r * x, where r = [a0; a1, a2, ...]
        # and there are ah[i]-1 integer points on the segment between r[i] and r[i+1]
        def hull(a, N):
            p, q = convergents(a)
            t = N // q[-1]
            ah = [t]
            ph = [0, t*p[-1]]
            qh = [0, t*q[-1]]
            for i in reversed(range(len(q))):
                if i % 2 == 1:
                    while qh[-1] + q[i-1] <= N:
                        t = (N - qh[-1] - q[i-1]) // q[i]
                        dp = p[i-1] + t*p[i]
                        dq = q[i-1] + t*q[i]
                        k = (N - qh[-1]) // dq
                        ah.append(k)
                        ph.append(ph[-1] + k * dp)
                        qh.append(qh[-1] + k * dq)
            return ah, ph, qh
        ```

!!! example "[Timus - Crime and Punishment](https://timus.online/problem.aspx?space=1&num=1430)"
    Bạn được cho các số nguyên $A$, $B$ và $N$. Tìm $x \geq 0$ và $y \geq 0$ sao cho $Ax + By \leq N$ và tổng $Ax + By$ đạt giá trị lớn nhất có thể.

??? hint "Lời giải"
    Trong bài toán này, ta có ràng buộc $1 \leq A, B, N \leq 2 \cdot 10^9$, do đó nó có thể được giải quyết trong thời gian $O(\sqrt N)$. Tuy nhiên, có một lời giải tốt hơn chạy trong thời gian $O(\log N)$ sử dụng liên phân số.

    Để thuận tiện, chúng ta sẽ đảo ngược chiều của $x$ bằng phép thế $x \mapsto \lfloor \frac{N}{A}\rfloor - x$, sao cho bây giờ chúng ta cần tìm điểm $(x; y)$ thỏa mãn $0 \leq x \leq \lfloor \frac{N}{A} \rfloor$, $By - Ax \leq N \;\bmod\; A$ và hiệu $By - Ax$ đạt giá trị lớn nhất có thể. Giá trị $y$ tối ưu cho mỗi $x$ sẽ bằng $\lfloor \frac{Ax + (N \bmod A)}{B} \rfloor$.

    Để giải quyết bài toán một cách tổng quát hơn, chúng ta sẽ viết một hàm tìm điểm tốt nhất trong khoảng $0 \leq x \leq N$ và $y = \lfloor \frac{Ax+B}{C} \rfloor$.

    Ý tưởng giải chính của bài toán này về cơ bản lặp lại bài toán trước, nhưng thay vì sử dụng các phân số bán hội tụ dưới để lệch khỏi đường thẳng, bạn sử dụng các phân số bán hội tụ trên để tiến sát đường thẳng nhất có thể mà không vượt qua nó và không vi phạm điều kiện $x \leq N$. Không giống như bài toán trước, bạn cần đảm bảo không vượt qua đường thẳng $y=\frac{Ax+B}{C}$ khi tiến lại gần nó, do đó bạn cần lưu ý điều này khi tính toán hệ số $t$ của phân số bán hội tụ.

    === "Python"
        ```py
        # (x, y) such that y = (A*x+B) // C,
        # Cy - Ax is max and 0 <= x <= N.
        def closest(A, B, C, N):
            # y <= (A*x + B)/C <=> diff(x, y) <= B
            def diff(x, y):
                return C*y-A*x
            a = fraction(A, C)
            p, q = convergents(a)
            ph = [B // C]
            qh = [0]
            for i in range(2, len(q) - 1):
                if i % 2 == 0:
                    while diff(qh[-1] + q[i+1], ph[-1] + p[i+1]) <= B:
                        t = 1 + (diff(qh[-1] + q[i-1], ph[-1] + p[i-1]) - B - 1) // abs(diff(q[i], p[i]))
                        dp = p[i-1] + t*p[i]
                        dq = q[i-1] + t*q[i]
                        k = (N - qh[-1]) // dq
                        if k == 0:
                            return qh[-1], ph[-1]
                        if diff(dq, dp) != 0:
                            k = min(k, (B - diff(qh[-1], ph[-1])) // diff(dq, dp))
                        qh.append(qh[-1] + k*dq)
                        ph.append(ph[-1] + k*dp)
            return qh[-1], ph[-1]

        def solve(A, B, N):
            x, y = closest(A, N % A, B, N // A)
            return N // A - x, y
        ```

!!! example "[June Challenge 2017 - Euler Sum](https://www.codechef.com/problems/ES)"
    Tính tổng $\sum\limits_{x=1}^N \lfloor ex \rfloor$, trong đó $e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, \dots, 1, 2n, 1, \dots]$ là hằng số Euler và $N \leq 10^{4000}$.

??? hint "Lời giải"
    Tổng này chính bằng số lượng điểm nguyên $(x;y)$ thỏa mãn $1 \leq x \leq N$ và $1 \leq y \leq ex$.    

    Sau khi xây dựng bao lồi cho các điểm nằm phía dưới đường thẳng $y=ex$, số lượng này có thể được tính bằng cách sử dụng [Định lý Pick](../geometry/picks-theorem.md):

    === "C++"
        ```cpp
        // sum floor(k * x) for k in [1, N] and x = [a0; a1, a2, ...]
        int sum_floor(auto a, int N) {
            N++;
            auto [ah, ph, qh] = hull(a, N);

            // The number of lattice points within a vertical right trapezoid
            // on points (0; 0) - (0; y1) - (dx; y2) - (dx; 0) that has
            // a+1 integer points on the segment (0; y1) - (dx; y2).
            auto picks = [](int y1, int y2, int dx, int a) {
                int b = y1 + y2 + a + dx;
                int A = (y1 + y2) * dx;
                return (A - b + 2) / 2 + b - (y2 + 1);
            };

            int ans = 0;
            for(size_t i = 1; i < qh.size(); i++) {
                ans += picks(ph[i - 1], ph[i], qh[i] - qh[i - 1], ah[i - 1]);
            }
            return ans - N;
        }
        ```
    === "Python"
        ```py
        # sum floor(k * x) for k in [1, N] and x = [a0; a1, a2, ...]
        def sum_floor(a, N):
            N += 1
            ah, ph, qh = hull(a, N)

            # The number of lattice points within a vertical right trapezoid
            # on points (0; 0) - (0; y1) - (dx; y2) - (dx; 0) that has
            # a+1 integer points on the segment (0; y1) - (dx; y2).
            def picks(y1, y2, dx, a):
                b = y1 + y2 + a + dx
                A = (y1 + y2) * dx
                return (A - b + 2) // 2 + b - (y2 + 1)

            ans = 0
            for i in range(1, len(qh)):
                ans += picks(ph[i-1], ph[i], qh[i]-qh[i-1], ah[i-1])
            return ans - N
        ```

!!! example "[NAIPC 2019 - It's a Mod, Mod, Mod, Mod World](https://open.kattis.com/problems/itsamodmodmodmodworld)"
    Cho các số $p$, $q$ và $n$, tính giá trị $\sum\limits_{i=1}^n [p \cdot i \bmod q]$.

??? hint "Lời giải"
    Bài toán này quy về bài toán trước nếu bạn nhận thấy rằng $a \bmod b = a - \lfloor \frac{a}{b} \rfloor b$. Từ thực tế này, tổng rút gọn thành:

    $$\sum\limits_{i=1}^n \left(p \cdot i - \left\lfloor \frac{p \cdot i}{q} \right\rfloor q\right) = \frac{pn(n+1)}{2}-q\sum\limits_{i=1}^n \left\lfloor \frac{p \cdot i}{q}\right\rfloor.$$

    Tuy nhiên, việc tính tổng $\lfloor rx \rfloor$ với $x$ chạy từ $1$ đến $N$ là điều chúng ta hoàn toàn có thể giải quyết được từ bài toán trước.

    === "C++"
        ```cpp
        void solve(int p, int q, int N) {
            cout << p * N * (N + 1) / 2 - q * sum_floor(fraction(p, q), N) << "\n";
        }
        ```
    === "Python"
        ```py
        def solve(p, q, N):
            return p * N * (N + 1) // 2 - q * sum_floor(fraction(p, q), N)
        ```

!!! example "[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)"
    Cho các số $N$, $M$, $A$ và $B$, tính giá trị $\sum\limits_{i=0}^{N-1} \lfloor \frac{A \cdot i + B}{M} \rfloor$.

??? hint "Lời giải"
    Đây là bài toán phức tạp nhất về mặt kỹ thuật từ đầu đến giờ.

    Chúng ta có thể sử dụng cùng một cách tiếp cận và xây dựng đầy đủ bao lồi của các điểm nằm phía dưới đường thẳng $y = \frac{Ax+B}{M}$.

    Chúng ta đã biết cách giải bài toán này với $B = 0$. Hơn nữa, chúng ta đã biết cách dựng bao lồi này lên đến điểm nguyên gần đường thẳng nhất trên đoạn $[0, N-1]$ (điều này được thực hiện trong bài toán "Crime and Punishment" ở trên).

    Bây giờ chúng ta cần lưu ý rằng khi đã đạt đến điểm gần đường thẳng nhất, chúng ta có thể giả định rằng đường thẳng đó thực sự đi qua điểm gần nhất này, vì không có điểm nguyên nào khác trên đoạn $[0, N-1]$ nằm giữa đường thẳng thực tế và đường thẳng dịch chuyển nhẹ xuống dưới để đi qua điểm gần nhất.

    Vì vậy, để dựng đầy đủ bao lồi phía dưới đường thẳng $y=\frac{Ax+B}{M}$ trên đoạn $[0, N-1]$, chúng ta có thể dựng nó lên đến điểm gần đường thẳng nhất trên đoạn $[0, N-1]$ rồi tiếp tục dựng như thể đường thẳng đi qua điểm này, tái sử dụng thuật toán dựng bao lồi với $B=0$:

    === "Python"
        ```py
        # hull of lattice (x, y) such that C*y <= A*x+B
        def hull(A, B, C, N):
            def diff(x, y):
                return C*y-A*x
            a = fraction(A, C)
            p, q = convergents(a)
            ah = []
            ph = [B // C]
            qh = [0]

            def insert(dq, dp):
                k = (N - qh[-1]) // dq
                if diff(dq, dp) > 0:
                    k = min(k, (B - diff(qh[-1], ph[-1])) // diff(dq, dp))
                ah.append(k)
                qh.append(qh[-1] + k*dq)
                ph.append(ph[-1] + k*dp)

            for i in range(1, len(q) - 1):
                if i % 2 == 0:
                    while diff(qh[-1] + q[i+1], ph[-1] + p[i+1]) <= B:
                        t = (B - diff(qh[-1] + q[i+1], ph[-1] + p[i+1])) // abs(diff(q[i], p[i]))
                        dp = p[i+1] - t*p[i]
                        dq = q[i+1] - t*q[i]
                        if dq < 0 or qh[-1] + dq > N:
                            break
                        insert(dq, dp)

            insert(q[-1], p[-1])

            for i in reversed(range(len(q))):
                if i % 2 == 1:
                    while qh[-1] + q[i-1] <= N:
                        t = (N - qh[-1] - q[i-1]) // q[i]
                        dp = p[i-1] + t*p[i]
                        dq = q[i-1] + t*q[i]
                        insert(dq, dp)
            return ah, ph, qh
        ```

!!! example "[OKC 2 - From Modular to Rational](https://codeforces.com/gym/102354/problem/I)"
    Có một số hữu tỉ $\frac{p}{q}$ sao cho $1 \leq p, q \leq 10^9$. Bạn có thể hỏi giá trị của $p q^{-1}$ theo mô-đun $m \sim 10^9$ cho một vài số nguyên tố $m$. Hãy khôi phục lại phân số $\frac{p}{q}$.

    _Phát biểu tương đương:_ Tìm $x$ mang lại giá trị nhỏ nhất cho biểu thức $Ax \;\bmod\; M$ với $1 \leq x \leq N$.

??? hint "Lời giải"
    Theo định lý thặng dư Trung Hoa, việc hỏi kết quả theo mô-đun của một số số nguyên tố cũng giống như việc hỏi theo mô-đun tích của chúng. Do đó, không mất tính tổng quát, chúng ta có thể giả định rằng chúng ta biết số dư theo mô-đun của một số $m$ đủ lớn.

    Có thể có một số nghiệm $(p, q)$ thỏa mãn $p \equiv qr \pmod m$ cho một số dư $r$ cho trước. Tuy nhiên, nếu $(p_1, q_1)$ và $(p_2, q_2)$ đều là nghiệm thì ta cũng có $p_1 q_2 \equiv p_2 q_1 \pmod m$. Giả định rằng $\frac{p_1}{q_1} \neq \frac{p_2}{q_2}$, điều này có nghĩa là $|p_1 q_2 - p_2 q_1|$ ít nhất phải bằng $m$.

    Trong phát biểu đề bài, ta có ràng buộc $1 \leq p, q \leq 10^9$, do đó nếu cả hai cặp $p_1, q_1$ và $p_2, q_2$ đều tối đa là $10^9$, thì hiệu số tối đa là $10^{18}$. Với $m > 10^{18}$, điều này có nghĩa là nghiệm $\frac{p}{q}$ với $1 \leq p, q \leq 10^9$ là duy nhất dưới dạng một số hữu tỉ.

    Do đó, bài toán quy về: cho trước $r$ theo mô-đun $m$, tìm bất kỳ giá trị $q$ nào sao cho $1 \leq q \leq 10^9$ và $qr \;\bmod\; m \leq 10^9$.

    Điều này tương đương với việc tìm $q$ mang lại giá trị nhỏ nhất cho biểu thức $qr \bmod m$ với $1 \leq q \leq 10^9$.

    Đặt $qr = km + b$, điều này có nghĩa là chúng ta cần tìm một cặp $(q, m)$ sao cho $1 \leq q \leq 10^9$ và hiệu $qr - km \geq 0$ đạt giá trị nhỏ nhất có thể.

    Vì $m$ là hằng số, chúng ta có thể chia cho nó và phát biểu lại là tìm $q$ sao cho $1 \leq q \leq 10^9$ và hiệu $\frac{r}{m} q - k \geq 0$ đạt giá trị nhỏ nhất có thể.

    Theo thuật ngữ của liên phân số, điều này có nghĩa là $\frac{k}{q}$ là xấp xỉ Diophantine tốt nhất cho $\frac{r}{m}$ và chúng ta chỉ cần kiểm tra các phân số bán hội tụ dưới của $\frac{r}{m}$.

    === "Python"
        ```py
        # find Q that minimizes Q*r mod m for 1 <= k <= n < m 
        def mod_min(r, n, m):
            a = fraction(r, m)
            p, q = convergents(a)
            for i in range(2, len(q)):
                if i % 2 == 1 and (i + 1 == len(q) or q[i+1] > n):
                    t = (n - q[i-1]) // q[i]
                    return q[i-1] + t*q[i]
        ```

## Bài tập luyện tập

* [UVa OJ - Continued Fractions](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=775)
* [ProjectEuler+ #64: Odd period square roots](https://www.hackerrank.com/contests/projecteuler/challenges/euler064/problem)
* [Codeforces Round #184 (Div. 2) - Continued Fractions](https://codeforces.com/contest/305/problem/B)
* [Codeforces Round #201 (Div. 1) - Doodle Jump](https://codeforces.com/contest/346/problem/E)
* [Codeforces Round #325 (Div. 1) - Alice, Bob, Oranges and Apples](https://codeforces.com/contest/585/problem/C)
* [POJ Founder Monthly Contest 2008.03.16 - A Modular Arithmetic Challenge](http://poj.org/problem?id=3530)
* [2019 Multi-University Training Contest 5 - fraction](http://acm.hdu.edu.cn/showproblem.php?pid=6624)
* [SnackDown 2019 Elimination Round - Election Bait](https://www.codechef.com/SNCKEL19/problems/EBAIT)
* [Code Jam 2019 round 2 - Continued Fraction](https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/round_2/new_elements_part_2/statement.pdf)
