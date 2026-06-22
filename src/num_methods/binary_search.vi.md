---
tags:
    - Original
lang: vi
---

# Tìm kiếm nhị phân (Binary Search)

**Tìm kiếm nhị phân (Binary Search)** là một phương pháp cho phép tìm kiếm nhanh hơn bằng cách chia đôi khoảng tìm kiếm sau mỗi bước. Ứng dụng phổ biến nhất của nó là tìm kiếm giá trị trong mảng đã sắp xếp, tuy nhiên ý tưởng chia đôi này cũng là cốt lõi của rất nhiều bài toán điển hình khác.

## Tìm kiếm trên mảng đã sắp xếp

Bài toán điển hình nhất dẫn đến thuật toán tìm kiếm nhị phân là: Cho một mảng đã được sắp xếp $A_0 \leq A_1 \leq \dots \leq A_{n-1}$, hãy kiểm tra xem giá trị $k$ có xuất hiện trong dãy hay không. Lời giải đơn giản nhất là duyệt qua từng phần tử và so sánh nó với $k$ (được gọi là tìm kiếm tuyến tính (linear search)). Cách tiếp cận này hoạt động trong thời gian $O(n)$, nhưng chưa tận dụng được tính chất mảng đã được sắp xếp.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/83/Binary_Search_Depiction.svg" width="800px">
<br>
<i>Minh họa tìm kiếm nhị phân giá trị $7$ trong một mảng</i>.
<br>
<i>Hình ảnh trên <a href="https://commons.wikimedia.org/wiki/File:Binary_Search_Depiction.svg">image</a> bởi <a href="https://commons.wikimedia.org/wiki/User:AlwaysAngry">AlwaysAngry</a> được phân phối dưới giấy phép <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">CC BY-SA 4.0</a></i>.
</center>

Bây giờ giả sử chúng ta biết hai chỉ số $L < R$ sao cho $A_L \leq k \leq A_R$. Do mảng đã sắp xếp, ta có thể suy ra rằng nếu $k$ có tồn tại, nó chỉ có thể nằm trong đoạn từ $A_L, A_{L+1}, \dots, A_R$ hoặc không xuất hiện trong mảng. Nếu ta chọn một chỉ số $M$ bất kỳ sao cho $L < M < R$ và kiểm tra xem $k$ nhỏ hơn hay lớn hơn $A_M$, ta có hai trường hợp xảy ra:

1. $A_L \leq k \leq A_M$. Trong trường hợp này, ta thu hẹp phạm vi bài toán từ đoạn $[L, R]$ về đoạn $[L, M]$;
2. $A_M \leq k \leq A_R$. Trong trường hợp này, ta thu hẹp phạm vi bài toán từ đoạn $[L, R]$ về đoạn $[M, R]$.

Khi không thể chọn được chỉ số $M$ nữa, tức là khi $R = L + 1$, chúng ta sẽ so sánh trực tiếp $k$ với $A_L$ và $A_R$. Trong trường hợp ngược lại, chúng ta muốn chọn chỉ số $M$ sao cho nó giảm kích thước phân đoạn đang xét về 1 phần tử nhanh nhất có thể _trong trường hợp xấu nhất_.

Trong trường hợp xấu nhất, ta sẽ luôn phải thu hẹp về phân đoạn lớn hơn trong hai phân đoạn $[L, M]$ và $[M, R]$. Do đó, ở kịch bản xấu nhất, kích thước phân đoạn sẽ giảm từ $R-L$ xuống còn $\max(M-L, R-M)$. Để tối thiểu hóa giá trị này, ta nên chọn $M \approx \frac{L+R}{2}$, khi đó:

$$
M-L \approx \frac{R-L}{2} \approx R-M.
$$

Nói cách khác, dưới góc độ trường hợp xấu nhất, việc luôn chọn $M$ ở chính giữa đoạn $[L, R]$ và chia đôi nó là tối ưu nhất. Vì thế, phân đoạn đang xét sẽ giảm đi một nửa sau mỗi bước cho đến khi kích thước của nó bằng $1$. Do đó, nếu quá trình này cần $h$ bước, cuối cùng hiệu số giữa $R$ và $L$ sẽ giảm từ $R-L$ xuống $\frac{R-L}{2^h} \approx 1$, cho ta phương trình $2^h \approx R-L$.

Lấy $\log_2$ hai vế, ta thu được $h \approx \log_2(R-L) \in O(\log n)$.

Độ phức tạp logarit vượt trội hơn rất nhiều so với tìm kiếm tuyến tính. Ví dụ, với $n \approx 2^{20} \approx 10^6$, tìm kiếm tuyến tính cần tới khoảng 1 triệu phép tính trong trường hợp xấu nhất, nhưng tìm kiếm nhị phân chỉ cần khoảng $20$ phép tính.

### Biên dưới (lower bound) và Biên trên (upper bound)

Thay vì tìm vị trí chính xác của phần tử, nhiều khi việc tìm vị trí của phần tử đầu tiên lớn hơn hoặc bằng $k$ (được gọi là biên dưới - **lower bound** của $k$) hoặc vị trí của phần tử đầu tiên lớn hơn $k$ (được gọi là biên trên - **upper bound** của $k$) sẽ thuận tiện hơn.

Cùng với nhau, biên dưới và biên trên tạo ra một nửa khoảng (có thể rỗng) chứa các phần tử trong mảng có giá trị bằng $k$. Để kiểm tra xem $k$ có xuất hiện trong mảng hay không, ta chỉ cần tìm biên dưới của nó và kiểm tra xem phần tử tại vị trí đó có bằng $k$ hay không.

### Cài đặt

Giải thích ở trên mô tả khái quát về thuật toán. Để cài đặt chi tiết, chúng ta cần phải chính xác hơn.

Chúng ta sẽ duy trì một cặp chỉ số $L < R$ sao cho $A_L \leq k < A_R$. Điều này có nghĩa là khoảng tìm kiếm hiện tại là nửa khoảng $[L, R)$. Việc sử dụng nửa khoảng thay vì đoạn đóng $[L, R]$ giúp giảm bớt các trường hợp đặc biệt ở biên.

Khi $R = L+1$, dựa vào các định nghĩa trên, ta có thể suy ra $R$ chính là biên trên (upper bound) của $k$. Việc khởi tạo $R$ với chỉ số ngay sau phần tử cuối mảng, tức là $R=n$, và khởi tạo $L$ với chỉ số ngay trước phần tử đầu mảng, tức là $L=-1$, là rất thuận tiện. Điều này hoàn toàn hợp lệ miễn là chúng ta không bao giờ truy xuất trực tiếp các phần tử $A_L$ và $A_R$ trong thuật toán, về mặt hình thức coi như $A_L = -\infty$ và $A_R = +\infty$.

Cuối cùng, giá trị cụ thể của $M$ được chọn sẽ là $M = \lfloor \frac{L+R}{2} \rfloor$.

Khi đó, mã nguồn cài đặt có thể trông như sau:

```cpp
... // a sorted array is stored as a[0], a[1], ..., a[n-1]
int l = -1, r = n;
while (r - l > 1) {
    int m = (l + r) / 2;
    if (k < a[m]) {
        r = m; // a[l] <= k < a[m] <= a[r]
    } else {
        l = m; // a[l] <= a[m] <= k < a[r]
    }
}
```

Trong suốt quá trình thực thi thuật toán, chúng ta không bao giờ truy xuất giá trị của $A_L$ hay $A_R$, do luôn có $L < M < R$. Cuối cùng, $L$ sẽ là chỉ số của phần tử cuối cùng không lớn hơn $k$ (hoặc $-1$ nếu không có phần tử nào thỏa mãn) và $R$ sẽ là chỉ số của phần tử đầu tiên lớn hơn $k$ (hoặc $n$ nếu không có phần tử nào thỏa mãn).

**Ghi chú.** Phép tính `m = (r + l) / 2` có thể dẫn đến tràn số (overflow) nếu `l` và `r` là hai số nguyên dương lớn, lỗi này đã tồn tại khoảng 9 năm trong thư viện JDK như được mô tả trong [bài viết này](https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html). Một số cách giải quyết thay thế bao gồm viết `m = l + (r - l) / 2` - cách này luôn hoạt động đúng với `l` và `r` nguyên dương nhưng vẫn có thể tràn số nếu `l` là một số âm. Nếu bạn sử dụng C++20, thư viện chuẩn cung cấp một giải pháp thay thế là `m = std::midpoint(l, r)` luôn đảm bảo tính toán chính xác.

## Tìm kiếm trên vị từ bất kỳ

Gọi $f : \{0,1,\dots, n-1\} \to \{0, 1\}$ là một hàm boolean (vị từ) được định nghĩa trên tập $0,1,\dots,n-1$ sao cho nó là một hàm đơn điệu tăng, nghĩa là:

$$
f(0) \leq f(1) \leq \dots \leq f(n-1).
$$

Tìm kiếm nhị phân như được mô tả ở trên thực chất là tìm điểm phân chia của mảng bằng vị từ (predicate) $f(M)$, mang giá trị chân trị của biểu thức $k < A_M$.
Chúng ta hoàn toàn có thể sử dụng một vị từ đơn điệu bất kỳ thay vì biểu thức $k < A_M$. Điều này đặc biệt hữu ích khi việc tính toán trực tiếp $f(k)$ cho mọi giá trị có thể có là quá tốn thời gian.
Nói cách khác, tìm kiếm nhị phân sẽ tìm ra chỉ số duy nhất $L$ sao cho $f(L) = 0$ và $f(R)=f(L+1)=1$ nếu tồn tại _điểm chuyển tiếp_ (transition point) như vậy, hoặc trả về $L = n-1$ nếu $f(0) = \dots = f(n-1) = 0$, hoặc $L = -1$ nếu $f(0) = \dots = f(n-1) = 1$.

Chứng minh tính đúng đắn giả sử tồn tại một điểm chuyển tiếp, nghĩa là $f(0)=0$ và $f(n-1)=1$: Cài đặt này duy trì một bất biến vòng lặp (loop invariant) $f(l)=0, f(r)=1$. Khi $r - l > 1$, việc chọn $m$ đảm bảo hiệu $r-l$ luôn giảm dần. Vòng lặp kết thúc khi $r - l = 1$, cho ta điểm chuyển tiếp cần tìm.

```cpp
... // f(i) is a boolean function such that f(0) <= ... <= f(n-1)
int l = -1, r = n;
while (r - l > 1) {
    int m = (l + r) / 2;
    if (f(m)) {
        r = m; // 0 = f(l) < f(m) = 1
    } else {
        l = m; // 0 = f(m) < f(r) = 1
    }
}
```

### Tìm kiếm nhị phân trên tập kết quả (Binary search on the answer)

Tình huống này thường xảy ra khi chúng ta cần tính toán một giá trị nào đó, nhưng chỉ có khả năng kiểm tra xem giá trị đó có đạt tối thiểu là $i$ hay không. Ví dụ, cho một mảng $a_1,\dots,a_n$, bạn cần tìm giá trị trung bình cộng lớn nhất phần nguyên dưới (floored average sum):

$$
\left \lfloor \frac{a_l + a_{l+1} + \dots + a_r}{r-l+1} \right\rfloor
$$

giữa mọi cặp $l, r$ khả dĩ sao cho $r-l \geq x$. Một trong những cách đơn giản để giải bài toán này là kiểm tra xem đáp án có đạt tối thiểu $\lambda$ hay không, tức là kiểm tra xem có tồn tại cặp $l, r$ sao cho:

$$
\frac{a_l + a_{l+1} + \dots + a_r}{r-l+1} \geq \lambda.
$$

Biến đổi tương đương, ta thu được:

$$
(a_l - \lambda) + (a_{l+1} - \lambda) + \dots + (a_r - \lambda) \geq 0,
$$

và bây giờ bài toán quy về việc kiểm tra xem trong mảng mới $a_i - \lambda$ có tồn tại mảng con độ dài tối thiểu $x+1$ có tổng không âm hay không, điều này có thể giải quyết dễ dàng bằng kỹ thuật mảng cộng dồn tiền tố (prefix sum).

## Tìm kiếm liên tục

Gọi $f : \mathbb R \to \mathbb R$ là một hàm số thực liên tục trên đoạn $[L, R]$.

Không mất tính tổng quát, giả định rằng $f(L) \leq f(R)$. Từ [định lý giá trị trung gian](https://en.wikipedia.org/wiki/Intermediate_value_theorem), ta suy ra với mọi $y \in [f(L), f(R)]$ luôn tồn tại $x \in [L, R]$ sao cho $f(x) = y$. Lưu ý rằng, khác với các phần trước, ở đây hàm số _không_ nhất thiết phải là hàm đơn điệu.

Giá trị $x$ có thể được xấp xỉ trong phạm vi sai số $\pm\delta$ với độ phức tạp thời gian $O\left(\log \frac{R-L}{\delta}\right)$ cho bất kỳ sai số $\delta$ nào mong muốn. Ý tưởng hoàn toàn tương tự, nếu ta lấy điểm $M \in (L, R)$, ta có thể thu hẹp khoảng tìm kiếm về $[L, M]$ hoặc $[M, R]$ tùy thuộc vào việc $f(M)$ lớn hơn hay nhỏ hơn $y$. Một ví dụ phổ biến cho phương pháp này là tìm nghiệm của các đa thức bậc lẻ.

Ví dụ, xét hàm số $f(x)=x^3 + ax^2 + bx + c$. Ta thấy $f(L) \to -\infty$ và $f(R) \to +\infty$ khi $L \to -\infty$ và $R \to +\infty$. Điều này có nghĩa là luôn có thể tìm được giá trị $L$ đủ nhỏ và $R$ đủ lớn sao cho $f(L) < 0$ and $f(R) > 0$. Khi đó, ta có thể sử dụng tìm kiếm nhị phân để tìm ra một khoảng nhỏ tùy ý chứa giá trị $x$ thỏa mãn $f(x)=0$.

## Tìm kiếm bằng lũy thừa của 2

Một cách đáng lưu ý khác để thực hiện tìm kiếm nhị phân là thay vì duy trì phân đoạn tìm kiếm, chúng ta duy trì con trỏ hiện tại $i$ và số mũ hiện tại $k$. Con trỏ bắt đầu tại $i=L$, và ở mỗi bước lặp ta kiểm tra vị từ tại điểm $i+2^k$. Nếu vị từ vẫn bằng $0$, ta dịch chuyển con trỏ từ $i$ sang $i+2^k$, ngược lại ta giữ nguyên vị trí con trỏ, sau đó giảm số mũ $k$ đi $1$.

Kỹ thuật này được áp dụng cực kỳ rộng rãi trong các bài toán trên cây, ví dụ như tìm tổ tiên chung gần nhất (LCA) của hai đỉnh hoặc tìm tổ tiên ở một độ cao cụ thể của một đỉnh. Nó cũng có thể được điều chỉnh để tìm phần tử khác không thứ $k$ trên cây Fenwick.

## Bài tập thực hành

* [LeetCode -  Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
* [LeetCode -  Search Insert Position](https://leetcode.com/problems/search-insert-position/)
* [LeetCode -  First Bad Version](https://leetcode.com/problems/first-bad-version/)
* [LeetCode -  Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
* [LeetCode -  Find Peak Element](https://leetcode.com/problems/find-peak-element/)
* [LeetCode -  Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-rotated-sorted-array/)
* [LeetCode -  Find Right Interval](https://leetcode.com/problems/find-right-interval/)
* [Codeforces - Interesting Drink](https://codeforces.com/problemset/problem/706/B/)
* [Codeforces - Magic Powder - 1](https://codeforces.com/problemset/problem/670/D1)
* [Codeforces - Another Problem on Strings](https://codeforces.com/problemset/problem/165/C)
* [Codeforces - Frodo and pillows](https://codeforces.com/problemset/problem/760/B)
* [Codeforces - GukiZ hates Boxes](https://codeforces.com/problemset/problem/551/C)
* [Codeforces - Enduring Exodus](https://codeforces.com/problemset/problem/645/C)
* [Codeforces - Chip 'n Dale Rescue Rangers](https://codeforces.com/problemset/problem/590/B)
