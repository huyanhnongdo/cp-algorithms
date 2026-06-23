---
tags:
  - Translated
e_maxx_link: stern_brocot_farey
lang: vi
---
# Cây Stern-Brocot và dãy Farey

## Cây Stern-Brocot

Cây Stern-Brocot là một cấu trúc tinh tế dùng để biểu diễn tập hợp tất cả các phân số dương. Nó được phát hiện độc lập bởi nhà toán học người Đức Moritz Stern vào năm 1858 và thợ làm đồng hồ người Pháp Achille Brocot vào năm 1861. Tuy nhiên, một số nguồn tư liệu cho rằng người phát hiện ra nó là nhà toán học Hy Lạp cổ đại Eratosthenes.

Việc xây dựng bắt đầu ở bước lặp thứ không với hai phân số

$$
    \frac{0}{1}, \frac{1}{0}
$$

cần lưu ý rằng giá trị thứ hai không hẳn là một phân số, nhưng nó có thể được hiểu là một phân số tối giản biểu diễn cho vô cực.

Tại mỗi bước lặp kế tiếp, xét tất cả các cặp phân số kề nhau $\frac{a}{b}$ và $\frac{c}{d}$, sau đó chèn [trung bình cộng phân số](https://en.wikipedia.org/wiki/Mediant_(mathematics)) (mediant) $\frac{a+c}{b+d}$ của chúng vào giữa.

Một vài bước lặp đầu tiên trông như sau:

$$
    \begin{array}{c}
    \dfrac{0}{1}, \dfrac{1}{1}, \dfrac{1}{0} \\
    \dfrac{0}{1}, \dfrac{1}{2}, \dfrac{1}{1}, \dfrac{2}{1}, \dfrac{1}{0} \\
    \dfrac{0}{1}, \dfrac{1}{3}, \dfrac{1}{2}, \dfrac{2}{3}, \dfrac{1}{1}, \dfrac{3}{2}, \dfrac{2}{1}, \dfrac{3}{1}, \dfrac{1}{0}
    \end{array}
$$

Tiếp tục quá trình này đến vô hạn, ta sẽ thu được *tất cả* các phân số dương. Ngoài ra, tất cả các phân số sẽ là *duy nhất* và *tối giản*. Cuối cùng, các phân số cũng sẽ xuất hiện theo thứ tự tăng dần.

Trước khi chứng minh các tính chất này, hãy cùng xem một hình ảnh trực quan về cây Stern-Brocot thay vì danh sách liệt kê. Mỗi phân số trong cây có hai nút con. Mỗi nút con là trung bình cộng phân số của tổ tiên gần nhất bên trái và tổ tiên gần nhất bên phải.

<div style="text-align: center;" markdown="1">

![Cây Stern-Brocot](https://upload.wikimedia.org/wikipedia/commons/3/37/SternBrocotTree.svg)

</div>

## Các chứng minh

**Thứ tự.** Việc chứng minh thứ tự rất đơn giản. Ta lưu ý rằng trung bình cộng phân số của hai phân số luôn nằm giữa hai phân số đó

$$
    \frac{a}{b} \le \frac{a+c}{b+d} \le \frac{c}{d}
$$

với điều kiện là

$$
    \frac{a}{b} \le \frac{c}{d}.
$$

Hai bất đẳng thức này có thể dễ dàng được chứng minh bằng cách quy đồng mẫu số của các phân số.

Vì thứ tự là tăng dần ở bước lặp thứ không, nên nó sẽ được duy trì ở mọi bước lặp kế tiếp.

**Tính tối giản.** Để chứng minh điều này, ta sẽ chỉ ra rằng với mọi cặp phân số kề nhau $\frac{a}{b}$ và $\frac{c}{d}$, ta luôn có

$$
    bc - ad = 1.
$$

Hãy nhớ lại rằng một phương trình Diophantine hai biến $ax+by=c$ có nghiệm khi và chỉ khi $c$ là bội số của $\gcd(a,b)$. Trong trường hợp của chúng ta, điều này ngụ ý $\gcd(a,b) = \gcd(c,d) = 1$, đây chính là điều cần chứng minh.

Rõ ràng ở bước lặp thứ không $bc - ad = 1$. Điều cần chứng minh tiếp theo là các trung bình cộng phân số vẫn giữ được tính chất này.

Giả sử hai phân số kề nhau của ta thỏa mãn $bc - ad = 1$, sau khi trung bình cộng phân số được thêm vào danh sách

$$
    \frac{a}{b}, \frac{a+c}{b+d}, \frac{c}{d}
$$

các biểu thức mới trở thành

$$\begin{align}
    b(a+c) - a(b+d) &= 1 \\
    c(b+d) - d(a+c) &= 1
\end{align}$$

Sử dụng $bc-ad=1$, ta có thể dễ dàng chứng minh điều này là đúng.

Từ đây, ta thấy rằng tính chất luôn được duy trì và do đó tất cả các phân số đều tối giản.

**Sự hiện diện của tất cả các phân số.** Chứng minh này liên quan mật thiết đến việc tìm vị trí của một phân số trong cây Stern-Brocot. Từ tính chất thứ tự, ta thấy cây con bên trái của một phân số chỉ chứa các phân số nhỏ hơn phân số cha, và cây con bên phải chỉ chứa các phân số lớn hơn phân số cha. Điều này có nghĩa là ta có thể tìm một phân số bằng cách duyệt cây từ gốc, đi sang trái nếu mục tiêu nhỏ hơn phân số hiện tại và đi sang phải nếu lớn hơn.

Chọn một phân số mục tiêu dương tùy ý $\frac{x}{y}$. Rõ ràng nó nằm giữa $\frac{0}{1}$ và $\frac{1}{0}$, vì vậy cách duy nhất để phân số này không nằm trong cây là nếu cần vô số bước để đạt tới nó.

Nếu trường hợp đó xảy ra, tại mọi bước lặp ta sẽ có

$$
    \frac{a}{b} \lt \frac{x}{y} \lt \frac{c}{d}
$$

điều này (sử dụng thực tế rằng số nguyên $z \gt 0 \iff z \ge 1$) có thể viết lại thành

$$
\begin{align}
    bx - ay &\ge 1 \\
    cy - dx &\ge 1.
\end{align}
$$

Bây giờ nhân bất đẳng thức thứ nhất với $c+d$ và thứ hai với [LATEX_INLINE_17}, rồi cộng lại ta được

$$
    (c+d)(bx - ay) + (a+b)(cy - dx) \ge a+b+c+d.
$$

Khai triển và sử dụng tính chất đã chứng minh trước đó $bc-ad=1$, ta được

$$
    x+y \ge a+b+c+d.
$$

Và vì tại mỗi bước lặp, ít nhất một trong các giá trị $a,b,c,d$ sẽ tăng lên, quá trình tìm kiếm phân số sẽ không quá $x+y$ bước lặp. Điều này mâu thuẫn với giả định rằng đường đi tới $\frac{x}{y}$ là vô hạn, do đó $\frac{x}{y}$ phải thuộc về cây.

## Thuật toán xây dựng cây

Để xây dựng bất kỳ cây con nào của cây Stern-Brocot, chỉ cần biết tổ tiên trái và phải. Ở mức đầu tiên, các tổ tiên trái và phải lần lượt là $\frac{0}{1}$ và $\frac{1}{0}$. Sử dụng chúng, ta tính trung bình cộng phân số và đi sâu hơn một mức, với trung bình cộng phân số thay thế tổ tiên phải trong cây con trái, và ngược lại.

Đoạn mã giả này cố gắng xây dựng toàn bộ cây vô hạn:

```cpp
void build(int a = 0, int b = 1, int c = 1, int d = 0, int level = 1) {
    int x = a + c, y = b + d;

    ... output the current fraction x/y at the current level in the tree
    
    build(a, b, x, y, level + 1);
    build(x, y, c, d, level + 1);
}
```

## Thuật toán tìm kiếm phân số

Thuật toán tìm kiếm đã được mô tả trong phần chứng minh rằng tất cả các phân số đều xuất hiện trong cây, nhưng chúng ta sẽ nhắc lại ở đây. Thuật toán này là một thuật toán Tìm kiếm nhị phân (Binary Search). Ban đầu, ta đứng ở gốc cây và so sánh mục tiêu với phân số hiện tại. Nếu chúng bằng nhau, ta hoàn thành và dừng quá trình. Nếu mục tiêu nhỏ hơn, ta đi đến nút con bên trái, ngược lại ta đi đến nút con bên phải.

### Tìm kiếm ngây thơ (Naive search)

Dưới đây là cài đặt trả về đường đi tới một phân số $\frac{p}{q}$ cho trước dưới dạng một chuỗi ký tự `'L'` và `'R'`, tương ứng với việc đi sang trái và phải. Chuỗi ký tự này xác định duy nhất mọi phân số dương và được gọi là hệ thống số Stern-Brocot.

```cpp
string find(int p, int q) {
    int pL = 0, qL = 1;
    int pR = 1, qR = 0;
    int pM = 1, qM = 1;
    string res;
    while(pM != p || qM != q) {
        if(p * qM < pM * q) {
            res += 'L';
            tie(pR, qR) = {pM, qM};
        } else {
            res += 'R';
            tie(pL, qL) = {pM, qM};
        }
        tie(pM, qM) = pair{pL + pR, qL + qR};
    }
    return res;
}
```

Các số vô tỷ trong hệ thống số Stern-Brocot tương ứng với các chuỗi ký tự vô hạn. Dọc theo con đường vô tận tới số vô tỷ, thuật toán sẽ tìm thấy các phân số tối giản với mẫu số tăng dần, cung cấp các xấp xỉ ngày càng tốt hơn cho số vô tỷ đó. Vì vậy, bằng cách lấy tiền tố của chuỗi vô hạn, ta có thể đạt được độ chính xác mong muốn. Ứng dụng này rất quan trọng trong chế tạo đồng hồ, điều này giải thích tại sao cây này lại được phát hiện trong lĩnh vực đó.

Lưu ý rằng với một phân số $\frac{p}{q}$, độ dài của chuỗi kết quả có thể lớn tới $O(p+q)$, ví dụ khi phân số có dạng $\frac{p}{1}$. Điều này có nghĩa là thuật toán trên **không nên được sử dụng trừ khi độ phức tạp này có thể chấp nhận được**!

### Tìm kiếm Logarithmic

Rất may, có thể cải tiến thuật toán trên để đảm bảo độ phức tạp $O(\log (p+q))$. Để làm điều này, ta lưu ý rằng nếu các phân số biên hiện tại là $\frac{p_L}{q_L}$ và $\frac{p_R}{q_R}$, thì bằng cách thực hiện $a$ bước sang phải, ta di chuyển đến phân số $\frac{p_L + a p_R}{q_L + a q_R}$, và bằng cách thực hiện $a$ bước sang trái, ta di chuyển đến phân số $\frac{a p_L + p_R}{a q_L + q_R}$.

Do đó, thay vì thực hiện từng bước `L` hoặc `R` một, ta có thể thực hiện $k$ bước theo cùng một hướng cùng lúc, sau đó đổi sang hướng khác, v.v. Bằng cách này, ta có thể tìm đường tới phân số $\frac{p}{q}$ dưới dạng mã hóa độ dài chuỗi (run-length encoding).

Khi các hướng thay đổi theo cách này, ta sẽ luôn biết nên chọn hướng nào. Vì vậy, để thuận tiện, ta có thể biểu diễn đường đi tới một phân số $\frac{p}{q}$ như một dãy các phân số

$$
\frac{p_0}{q_0}, \frac{p_1}{q_1}, \frac{p_2}{q_2}, \dots, \frac{p_n}{q_n}, \frac{p_{n+1}}{q_{n+1}} = \frac{p}{q}
$$

sao cho $\frac{p_{k-1}}{q_{k-1}}$ và $\frac{p_k}{q_k}$ là các biên của khoảng tìm kiếm tại bước $k$, bắt đầu với $\frac{p_0}{q_0} = \frac{0}{1}$ và $\frac{p_1}{q_1} = \frac{1}{0}$. Sau đó, sau bước $k$, ta di chuyển tới phân số

$$
\frac{p_{k+1}}{q_{k+1}} = \frac{p_{k-1} + a_k p_k}{q_{k-1} + a_k q_k},
$$

với $a_k$ là một số nguyên dương. Nếu bạn quen thuộc với [phân số liên tục](../algebra/continued-fractions.md) (continued fractions), bạn sẽ nhận ra dãy $\frac{p_i}{q_i}$ chính là các phân số hội tụ của $\frac{p}{q}$ và dãy $[a_1; a_2, \dots, a_{n}, 1]$ biểu diễn phân số liên tục của $\frac{p}{q}$.

Điều này cho phép tìm mã hóa run-length của đường đi tới $\frac{p}{q}$ theo thuật toán tính biểu diễn phân số liên tục của phân số $\frac{p}{q}$:

```cpp
auto find(int p, int q) {
    bool right = true;
    vector<pair<int, char>> res;
    while(q) {
        res.emplace_back(p / q, right ? 'R' : 'L');
        tie(p, q) = pair{q, p % q};
        right ^= 1;
    }
    res.back().first--;
    return res;
}
```

Tuy nhiên, cách tiếp cận này chỉ hiệu quả nếu ta đã biết $\frac{p}{q}$ và muốn tìm vị trí của nó trong cây Stern-Brocot.

Trong thực tế, thường thì $\frac{p}{q}$ không được biết trước, nhưng ta có thể kiểm tra cho một $\frac{x}{y}$ cụ thể xem $\frac{x}{y} < \frac{p}{q}$ hay không.

Biết được điều này, ta có thể mô phỏng tìm kiếm trên cây Stern-Brocot bằng cách duy trì các biên hiện tại $\frac{p_{k-1}}{q_{k-1}}$ và $\frac{p_k}{q_k}$, và tìm mỗi $a_k$ thông qua tìm kiếm nhị phân. Thuật toán khi đó sẽ kỹ thuật hơn một chút và có khả năng đạt độ phức tạp $O(\log^2(x+y))$, trừ khi bài toán cho phép tìm $a_k$ nhanh hơn (ví dụ: sử dụng `floor` của một biểu thức đã biết).

## Dãy Farey

Dãy Farey bậc $n$ là dãy đã sắp xếp các phân số giữa $0$ và $1$ mà mẫu số của chúng không vượt quá $n$.

Dãy này được đặt theo tên nhà địa chất người Anh John Farey, người vào năm 1816 đã dự đoán rằng bất kỳ phân số nào trong dãy Farey cũng là trung bình cộng phân số của hai láng giềng của nó. Điều này đã được chứng minh một thời gian sau đó bởi Cauchy, nhưng độc lập với cả hai, nhà toán học Haros đã đi đến kết luận gần như tương tự vào năm 1802.

Các dãy Farey tự thân chúng có nhiều tính chất thú vị, nhưng kết nối với cây Stern-Brocot là rõ ràng nhất. Thực tế, các dãy Farey có thể thu được bằng cách cắt tỉa các nhánh từ cây Stern-Brocot.

Từ thuật toán xây dựng cây Stern-Brocot, ta có thuật toán cho dãy Farey. Bắt đầu với danh sách các phân số $\frac{0}{1}, \frac{1}{0}$. Tại mỗi bước lặp kế tiếp, chỉ chèn trung bình cộng phân số nếu mẫu số không vượt quá $n$. Đến một lúc nào đó, danh sách sẽ không thay đổi nữa và dãy Farey mong muốn sẽ được tìm thấy.

### Độ dài của dãy Farey

Dãy Farey bậc $n$ chứa tất cả các phần tử của dãy Farey bậc $n-1$ cũng như tất cả các phân số tối giản có mẫu số là $n$, nhưng cái sau chính là hàm phi Euler $\varphi(n)$. Vì vậy, độ dài $L_n$ của dãy Farey bậc $n$ là

$$
    L_n = L_{n-1} + \varphi(n)
$$

hoặc tương đương, bằng cách khai triển đệ quy, ta có

$$
    L_n = 1 + \sum_{k=1}^n \varphi(k).
$$