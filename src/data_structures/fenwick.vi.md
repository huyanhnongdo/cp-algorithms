---
tags:
  - Translated
e_maxx_link: fenwick_tree
lang: vi
---
# Cây Fenwick

Giả sử $f$ là một phép toán nhóm (một hàm kết hợp nhị phân trên một tập hợp có phần tử đơn vị và các phần tử nghịch đảo) và $A$ là một mảng (Array) số nguyên có độ dài $N$.
Ký hiệu trung tố (infix notation) của $f$ là $*$; tức là, $f(x,y) = x*y$ cho các số nguyên tùy ý $x,y$.
(Vì phép toán này có tính kết hợp, chúng ta sẽ bỏ qua dấu ngoặc đơn cho thứ tự áp dụng của $f$ khi sử dụng ký hiệu trung tố.)

Cây Fenwick (Fenwick Tree) là một cấu trúc dữ liệu (Data Structure) có các khả năng sau:

* Tính toán giá trị của hàm $f$ trong đoạn (Range) $[l, r]$ đã cho (tức là $A_l * A_{l+1} * \dots * A_r$) trong thời gian $O(\log N)$.
* Cập nhật (Update) giá trị của một phần tử (Element) của $A$ trong thời gian $O(\log N)$.
* Yêu cầu $O(N)$ bộ nhớ (Space Complexity) (tương đương lượng bộ nhớ cần thiết cho $A$).
* Dễ sử dụng và cài đặt (Implementation), đặc biệt trong trường hợp mảng đa chiều.

Ứng dụng phổ biến nhất của cây Fenwick là _tính tổng của một đoạn_.
Ví dụ, sử dụng phép cộng trên tập hợp số nguyên làm phép toán nhóm, tức là $f(x,y) = x + y$: phép toán nhị phân $*$ trong trường hợp này là $+$, vì vậy $A_l * A_{l+1} * \dots * A_r = A_l + A_{l+1} + \dots + A_{r}$.

Cây Fenwick còn được gọi là **Cây chỉ mục nhị phân** (Binary Indexed Tree) (BIT).
Nó lần đầu tiên được mô tả trong một bài báo có tiêu đề "A new data structure for cumulative frequency tables" (Peter M. Fenwick, 1994).

## Mô tả

### Tổng quan

Để đơn giản hóa, chúng ta sẽ giả định rằng hàm $f$ được định nghĩa là $f(x,y) = x + y$ trên các số nguyên.

Giả sử chúng ta được cho một mảng số nguyên, $A[0 \dots N-1]$.
(Lưu ý rằng chúng ta đang sử dụng đánh chỉ số từ 0 (zero-based indexing).)
Cây Fenwick chỉ là một mảng, $T[0 \dots N-1]$, trong đó mỗi phần tử bằng tổng các phần tử của $A$ trong một đoạn nào đó, $[g(i), i]$:

$$T_i = \sum_{j = g(i)}^{i}{A_j}$$

trong đó $g$ là một hàm nào đó thỏa mãn $0 \le g(i) \le i$.
Chúng ta sẽ định nghĩa $g$ trong một vài đoạn văn tiếp theo.

Cấu trúc dữ liệu này được gọi là cây (Tree) vì có một biểu diễn đẹp của nó dưới dạng cây, mặc dù chúng ta không cần mô hình hóa một cây thực sự với các đỉnh (Node) và cạnh (Edge).
Chúng ta chỉ cần duy trì mảng $T$ để xử lý tất cả các truy vấn (Query).

**Lưu ý:** Cây Fenwick được trình bày ở đây sử dụng đánh chỉ số từ 0.
Nhiều người sử dụng một phiên bản cây Fenwick dùng đánh chỉ số từ 1.
Do đó, bạn cũng sẽ tìm thấy một cài đặt thay thế sử dụng đánh chỉ số từ 1 trong phần cài đặt.
Cả hai phiên bản đều tương đương về độ phức tạp thời gian (Time Complexity) và độ phức tạp bộ nhớ.

Bây giờ chúng ta có thể viết một số mã giả (pseudo-code) cho hai phép toán đã đề cập ở trên.
Dưới đây, chúng ta sẽ lấy tổng các phần tử của $A$ trong đoạn $[0, r]$ và cập nhật (tăng) một phần tử $A_i$:

```python
def sum(int r):
    res = 0
    while (r >= 0):
        res += t[r]
        r = g(r) - 1
    return res

def increase(int i, int delta):
    for all j with g(j) <= i <= j:
        t[j] += delta
```

Hàm `sum` hoạt động như sau:

1. Đầu tiên, nó cộng tổng của đoạn $[g(r), r]$ (tức là $T[r]$) vào `result`.
2. Sau đó, nó "nhảy" đến đoạn $[g(g(r)-1), g(r)-1]$ và cộng tổng của đoạn này vào `result`.
3. Điều này tiếp tục cho đến khi nó "nhảy" từ $[0, g(g( \dots g(r)-1 \dots -1)-1)]$ đến $[g(-1), -1]$; đây là nơi hàm `sum` ngừng nhảy.

Hàm `increase` hoạt động tương tự, nhưng nó "nhảy" theo hướng các chỉ số (Index) tăng dần:

1. Tổng cho mỗi đoạn có dạng $[g(j), j]$ thỏa mãn điều kiện $g(j) \le i \le j$ được tăng thêm `delta`; tức là, `t[j] += delta`.
Do đó, nó cập nhật tất cả các phần tử trong $T$ tương ứng với các đoạn mà $A_i$ nằm trong đó.

Độ phức tạp của cả `sum` và `increase` phụ thuộc vào hàm $g$.
Có nhiều cách để chọn hàm $g$ sao cho $0 \le g(i) \le i$ với mọi $i$.
Ví dụ, hàm $g(i) = i$ hoạt động được, nó mang lại $T = A$ (trong trường hợp này, các truy vấn tổng sẽ chậm).
Chúng ta cũng có thể chọn hàm $g(i) = 0$.
Điều này sẽ tương ứng với mảng tổng tiền tố (Prefix Sum Arrays) (trong trường hợp này, việc tìm tổng của đoạn $[0, i]$ sẽ chỉ mất thời gian hằng số; tuy nhiên, các cập nhật sẽ chậm).
Phần thông minh của thuật toán (Algorithm) cây Fenwick là cách nó sử dụng một định nghĩa đặc biệt của hàm $g$ có thể xử lý cả hai phép toán trong thời gian $O(\log N)$.

### Định nghĩa của $g(i)$ { data-toc-label='Định nghĩa của <script type="math/tex">g(i)</script>' }

Việc tính toán $g(i)$ được định nghĩa bằng cách sử dụng phép toán đơn giản sau:
chúng ta thay thế tất cả các bit $1$ cuối cùng (trailing $1$ bits) trong biểu diễn nhị phân của $i$ bằng các bit $0$.

Nói cách khác, nếu chữ số có ý nghĩa nhỏ nhất của $i$ trong hệ nhị phân là $0$, thì $g(i) = i$.
Và ngược lại, chữ số có ý nghĩa nhỏ nhất là một $1$, và chúng ta lấy $1$ này cùng với tất cả các $1$s cuối cùng khác và đảo ngược chúng.

Ví dụ chúng ta có:

$$\begin{align}
g(11) = g(1011_2) = 1000_2 &= 8 \\\\
g(12) = g(1100_2) = 1100_2 &= 12 \\\\
g(13) = g(1101_2) = 1100_2 &= 12 \\\\
g(14) = g(1110_2) = 1110_2 &= 14 \\\\
g(15) = g(1111_2) = 0000_2 &= 0 \\\\
\end{align}$$

Tồn tại một cài đặt đơn giản sử dụng các phép toán bitwise (bitwise operations) cho phép toán không tầm thường được mô tả ở trên:

$$g(i) = i ~\&~ (i+1),$$

trong đó $\&$ là toán tử AND bitwise. Không khó để tự mình nhận thấy rằng giải pháp này thực hiện điều tương tự như phép toán được mô tả ở trên.

Bây giờ, chúng ta chỉ cần tìm cách để lặp qua tất cả các $j$'s, sao cho $g(j) \le i \le j$.

Dễ dàng nhận thấy rằng chúng ta có thể tìm tất cả các $j$'s như vậy bằng cách bắt đầu với $i$ và đảo ngược bit 0 cuối cùng.
Chúng ta sẽ gọi phép toán này là $h(j)$.
Ví dụ, với $i = 10$ chúng ta có:

$$\begin{align}
10 &= 0001010_2 \\\\
h(10) = 11 &= 0001011_2 \\\\
h(11) = 15 &= 0001111_2 \\\\
h(15) = 31 &= 0011111_2 \\\\
h(31) = 63 &= 0111111_2 \\\\
\vdots &
\end{align}$$

Không ngạc nhiên, cũng tồn tại một cách đơn giản để thực hiện $h$ bằng cách sử dụng các phép toán bitwise:

$$h(j) = j ~|~ (j+1),$$

trong đó $|$ là toán tử OR bitwise.

Hình ảnh sau đây cho thấy một cách diễn giải có thể của cây Fenwick dưới dạng cây.
Các đỉnh của cây hiển thị các đoạn mà chúng bao phủ.

<div style="text-align: center;">
  <img src="binary_indexed_tree.png" alt="Cây chỉ mục nhị phân">
</div>

## Cài đặt

### Tìm tổng trong mảng một chiều

Ở đây chúng tôi trình bày một cài đặt của cây Fenwick cho các truy vấn tổng và các cập nhật đơn lẻ.

Cây Fenwick thông thường chỉ có thể trả lời các truy vấn tổng dạng $[0, r]$ bằng cách sử dụng `sum(int r)`, tuy nhiên chúng ta cũng có thể trả lời các truy vấn khác dạng $[l, r]$ bằng cách tính toán hai tổng $[0, r]$ và $[0, l-1]$ rồi trừ chúng đi.
Điều này được xử lý trong phương thức `sum(int l, int r)`.

Cài đặt này cũng hỗ trợ hai hàm tạo (constructor).
Bạn có thể tạo một cây Fenwick được khởi tạo bằng các số 0, hoặc bạn có thể chuyển đổi một mảng hiện có sang dạng Fenwick.

```{.cpp file=fenwick_sum}
struct FenwickTree {
    vector<int> bit;  // binary indexed tree
    int n;

    FenwickTree(int n) {
        this->n = n;
        bit.assign(n, 0);
    }

    FenwickTree(vector<int> const &a) : FenwickTree(a.size()) {
        for (size_t i = 0; i < a.size(); i++)
            add(i, a[i]);
    }

    int sum(int r) {
        int ret = 0;
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret += bit[r];
        return ret;
    }

    int sum(int l, int r) {
        return sum(r) - sum(l - 1);
    }

    void add(int idx, int delta) {
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] += delta;
    }
};
```

### Xây dựng tuyến tính

Cài đặt trên yêu cầu thời gian $O(N \log N)$.
Có thể cải thiện điều đó thành thời gian $O(N)$.

Ý tưởng là, số $a[i]$ tại chỉ số $i$ sẽ đóng góp vào đoạn được lưu trữ trong $bit[i]$, và vào tất cả các đoạn mà chỉ số $i | (i + 1)$ đóng góp vào.
Vì vậy, bằng cách thêm các số theo thứ tự, bạn chỉ cần đẩy tổng hiện tại tiếp tục đến đoạn tiếp theo, nơi nó sẽ được đẩy xa hơn đến đoạn tiếp theo, và cứ thế tiếp diễn.

```cpp
FenwickTree(vector<int> const &a) : FenwickTree(a.size()){
    for (int i = 0; i < n; i++) {
        bit[i] += a[i];
        int r = i | (i + 1);
        if (r < n) bit[r] += bit[i];
    }
}
```

### Tìm giá trị nhỏ nhất của $[0, r]$ trong mảng một chiều { data-toc-label='Tìm giá trị nhỏ nhất của <script type="math/tex">[0, r]</script> trong mảng một chiều' }

Rõ ràng là không có cách dễ dàng nào để tìm giá trị nhỏ nhất của đoạn $[l, r]$ bằng cách sử dụng cây Fenwick, vì cây Fenwick chỉ có thể trả lời các truy vấn dạng $[0, r]$.
Ngoài ra, mỗi khi một giá trị được `update`, giá trị mới phải nhỏ hơn giá trị hiện tại.
Cả hai hạn chế đáng kể này là do phép toán $min$ cùng với tập hợp số nguyên không tạo thành một nhóm, vì không có phần tử nghịch đảo.

```{.cpp file=fenwick_min}
struct FenwickTreeMin {
    vector<int> bit;
    int n;
    const int INF = (int)1e9;

    FenwickTreeMin(int n) {
        this->n = n;
        bit.assign(n, INF);
    }

    FenwickTreeMin(vector<int> a) : FenwickTreeMin(a.size()) {
        for (size_t i = 0; i < a.size(); i++)
            update(i, a[i]);
    }

    int getmin(int r) {
        int ret = INF;
        for (; r >= 0; r = (r & (r + 1)) - 1)
            ret = min(ret, bit[r]);
        return ret;
    }

    void update(int idx, int val) {
        for (; idx < n; idx = idx | (idx + 1))
            bit[idx] = min(bit[idx], val);
    }
};
```

Lưu ý: có thể cài đặt một cây Fenwick có thể xử lý các truy vấn giá trị nhỏ nhất trên đoạn tùy ý và các cập nhật tùy ý.
Bài báo [Efficient Range Minimum Queries using Binary Indexed Trees](http://ioinformatics.org/oi/pdf/v9_2015_39_44.pdf) mô tả một cách tiếp cận như vậy.
Tuy nhiên với cách tiếp cận đó, bạn cần duy trì một cây chỉ mục nhị phân thứ hai trên dữ liệu, với một cấu trúc hơi khác, vì một cây không đủ để lưu trữ giá trị của tất cả các phần tử trong mảng.
Cài đặt này cũng khó hơn nhiều so với cài đặt thông thường cho tổng.

### Tìm tổng trong mảng hai chiều

Như đã tuyên bố trước đây, việc triển khai cây Fenwick cho mảng đa chiều là rất dễ dàng.

```cpp
struct FenwickTree2D {
    vector<vector<int>> bit;
    int n, m;

    // init(...) { ... }

    int sum(int x, int y) {
        int ret = 0;
        for (int i = x; i >= 0; i = (i & (i + 1)) - 1)
            for (int j = y; j >= 0; j = (j & (j + 1)) - 1)
                ret += bit[i][j];
        return ret;
    }

    void add(int x, int y, int delta) {
        for (int i = x; i < n; i = i | (i + 1))
            for (int j = y; j < m; j = j | (j + 1))
                bit[i][j] += delta;
    }
};
```

### Cách tiếp cận đánh chỉ số từ 1

Đối với cách tiếp cận này, chúng ta thay đổi một chút các yêu cầu và định nghĩa cho $T[]$ và $g()$.
Chúng ta muốn $T[i]$ lưu trữ tổng của $[g(i)+1; i]$.
Điều này thay đổi cài đặt một chút, và cho phép một định nghĩa đẹp tương tự cho $g(i)$:

```python
def sum(int r):
    res = 0
    while (r > 0):
        res += t[r]
        r = g(r)
    return res

def increase(int i, int delta):
    for all j with g(j) < i <= j:
        t[j] += delta
```

Việc tính toán $g(i)$ được định nghĩa là:
đảo ngược bit $1$ cuối cùng (last set $1$ bit) trong biểu diễn nhị phân của $i$.

$$\begin{align}
g(7) = g(111_2) = 110_2 &= 6 \\\\
g(6) = g(110_2) = 100_2 &= 4 \\\\
g(4) = g(100_2) = 000_2 &= 0 \\\\
\end{align}$$

Bit 1 cuối cùng có thể được trích xuất bằng cách sử dụng $i ~\&~ (-i)$, vì vậy phép toán có thể được biểu diễn là:

$$g(i) = i - (i ~\&~ (-i)).$$

Và không khó để thấy rằng bạn cần thay đổi tất cả các giá trị $T[j]$ trong dãy $i,~ h(i),~ h(h(i)),~ \dots$ khi bạn muốn cập nhật $A[j]$, trong đó $h(i)$ được định nghĩa là:

$$h(i) = i + (i ~\&~ (-i)).$$

Như bạn có thể thấy, lợi ích chính của cách tiếp cận này là các phép toán nhị phân bổ sung cho nhau rất đẹp.

Cài đặt sau đây có thể được sử dụng như các cài đặt khác, tuy nhiên nó sử dụng đánh chỉ số từ 1 nội bộ.

```{.cpp file=fenwick_sum_onebased}
struct FenwickTreeOneBasedIndexing {
    vector<int> bit;  // binary indexed tree
    int n;

    FenwickTreeOneBasedIndexing(int n) {
        this->n = n + 1;
        bit.assign(n + 1, 0);
    }

    FenwickTreeOneBasedIndexing(vector<int> a)
        : FenwickTreeOneBasedIndexing(a.size()) {
        for (size_t i = 0; i < a.size(); i++)
            add(i, a[i]);
    }

    int sum(int idx) {
        int ret = 0;
        for (++idx; idx > 0; idx -= idx & -idx)
            ret += bit[idx];
        return ret;
    }

    int sum(int l, int r) {
        return sum(r) - sum(l - 1);
    }

    void add(int idx, int delta) {
        for (++idx; idx < n; idx += idx & -idx)
            bit[idx] += delta;
    }
};
```

## Các phép toán trên đoạn

Một cây Fenwick có thể hỗ trợ các phép toán trên đoạn sau:

1. Cập nhật điểm (Point Update) và Truy vấn đoạn (Range Query)
2. Cập nhật đoạn (Range Update) và Truy vấn điểm (Point Query)
3. Cập nhật đoạn và Truy vấn đoạn

### 1. Cập nhật điểm và Truy vấn đoạn

Đây chỉ là cây Fenwick thông thường như đã giải thích ở trên.

### 2. Cập nhật đoạn và Truy vấn điểm

Sử dụng các thủ thuật đơn giản, chúng ta cũng có thể thực hiện các phép toán ngược lại: tăng các đoạn và truy vấn cho các giá trị đơn lẻ.

Giả sử cây Fenwick được khởi tạo bằng các số 0.
Giả sử chúng ta muốn tăng khoảng (Interval) $[l, r]$ thêm $x$.
Chúng ta thực hiện hai phép toán cập nhật điểm trên cây Fenwick là `add(l, x)` và `add(r+1, -x)`.

Nếu chúng ta muốn lấy giá trị của $A[i]$, chúng ta chỉ cần lấy tổng tiền tố (Prefix Sum) bằng cách sử dụng phương pháp tổng đoạn thông thường.
Để thấy lý do tại sao điều này đúng, chúng ta có thể tập trung lại vào phép toán tăng trước đó.
Nếu $i < l$, thì hai phép toán cập nhật không có tác dụng đối với truy vấn và chúng ta nhận được tổng $0$.
Nếu $i \in [l, r]$, thì chúng ta nhận được kết quả $x$ vì phép toán cập nhật đầu tiên.
Và nếu $i > r$, thì phép toán cập nhật thứ hai sẽ triệt tiêu tác dụng của phép toán đầu tiên.

Cài đặt sau đây sử dụng đánh chỉ số từ 1.

```cpp
void add(int idx, int val) {
    for (++idx; idx < n; idx += idx & -idx)
        bit[idx] += val;
}

void range_add(int l, int r, int val) {
    add(l, val);
    add(r + 1, -val);
}

int point_query(int idx) {
    int ret = 0;
    for (++idx; idx > 0; idx -= idx & -idx)
        ret += bit[idx];
    return ret;
}
```

Lưu ý: tất nhiên cũng có thể tăng một điểm đơn lẻ $A[i]$ bằng `range_add(i, i, val)`.

### 3. Cập nhật đoạn và Truy vấn đoạn

Để hỗ trợ cả cập nhật đoạn và truy vấn đoạn, chúng ta sẽ sử dụng hai cây BIT cụ thể là $B_1[]$ và $B_2[]$, được khởi tạo bằng các số 0.

Giả sử chúng ta muốn tăng khoảng $[l, r]$ thêm giá trị $x$.
Tương tự như trong phương pháp trước, chúng ta thực hiện hai cập nhật điểm trên $B_1$: `add(B1, l, x)` và `add(B1, r+1, -x)`.
Và chúng ta cũng cập nhật $B_2$. Chi tiết sẽ được giải thích sau.

```python
def range_add(l, r, x):
    add(B1, l, x)
    add(B1, r+1, -x)
    add(B2, l, x*(l-1))
    add(B2, r+1, -x*r))
```
Sau khi cập nhật đoạn $(l, r, x)$, truy vấn tổng đoạn nên trả về các giá trị sau:

$$
sum[0, i]=
\begin{cases}
0 & i < l \\\\
x \cdot (i-(l-1)) & l \le i \le r \\\\
x \cdot (r-l+1) & i > r \\\\
\end{cases}
$$

Chúng ta có thể viết tổng đoạn dưới dạng hiệu của hai số hạng (term), trong đó chúng ta sử dụng $B_1$ cho số hạng đầu tiên và $B_2$ cho số hạng thứ hai.
Sự khác biệt của các truy vấn sẽ cho chúng ta tổng tiền tố trên $[0, i]$.

$$\begin{align}
sum[0, i] &= sum(B_1, i) \cdot i - sum(B_2, i) \\\\
&= \begin{cases}
0 \cdot i - 0 & i < l\\\\
x \cdot i - x \cdot (l-1) & l \le i \le r \\\\
0 \cdot i - (x \cdot (l-1) - x \cdot r) & i > r \\\\
\end{cases}
\end{align}
$$

Biểu thức cuối cùng chính xác bằng các số hạng cần thiết.
Do đó, chúng ta có thể sử dụng $B_2$ để loại bỏ các số hạng thừa khi chúng ta nhân $B_1[i]\times i$.

Chúng ta có thể tìm các tổng đoạn tùy ý bằng cách tính tổng tiền tố cho $l-1$ và $r$ và lấy hiệu của chúng một lần nữa.

```python
def add(b, idx, x):
    while idx <= N:
        b[idx] += x
        idx += idx & -idx

def range_add(l,r,x):
    add(B1, l, x)
    add(B1, r+1, -x)
    add(B2, l, x*(l-1))
    add(B2, r+1, -x*r)

def sum(b, idx):
    total = 0
    while idx > 0:
        total += b[idx]
        idx -= idx & -idx
    return total

def prefix_sum(idx):
    return sum(B1, idx)*idx -  sum(B2, idx)

def range_sum(l, r):
    return prefix_sum(r) - prefix_sum(l-1)
```

## Bài tập thực hành

* [UVA 12086 - Potentiometers](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3238)
* [LOJ 1112 - Curious Robin Hood](http://www.lightoj.com/volume_showproblem.php?problem=1112)
* [LOJ 1266 - Điểm trong Hình chữ nhật](http://www.lightoj.com/volume_showproblem.php?problem=1266 "2D Fenwick Tree")
* [Codechef - SPREAD](http://www.codechef.com/problems/SPREAD)
* [SPOJ - CTRICK](http://www.spoj.com/problems/CTRICK/)
* [SPOJ - MATSUM](http://www.spoj.com/problems/MATSUM/)
* [SPOJ - DQUERY](http://www.spoj.com/problems/DQUERY/)
* [SPOJ - NKTEAM](http://www.spoj.com/problems/NKTEAM/)
* [SPOJ - YODANESS](http://www.spoj.com/problems/YODANESS/)
* [SRM 310 - FloatingMedian](https://community.topcoder.com/stat?c=problem_statement&pm=6551&rd=9990)
* [SPOJ - Ada and Behives](http://www.spoj.com/problems/ADABEHIVE/)
* [Hackerearth - Counting in Byteland](https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/counting-in-byteland/)
* [DevSkill - Shan and String (đã lưu trữ)](http://web.archive.org/web/20210322010617/https://devskill.com/CodingProblems/ViewProblem/300)
* [Codeforces - Little Artem and Time Machine](http://codeforces.com/contest/669/problem/E)
* [Codeforces - Hanoi Factory](http://codeforces.com/contest/777/problem/E)
* [SPOJ - Tulip and Numbers](http://www.spoj.com/problems/TULIPNUM/)
* [SPOJ - SUMSUM](http://www.spoj.com/problems/SUMSUM/)
* [SPOJ - Sabir and Gifts](http://www.spoj.com/problems/SGIFT/)
* [SPOJ - The Permutation Game Again](http://www.spoj.com/problems/TPGA/)
* [SPOJ - Zig when you Zag](http://www.spoj.com/problems/ZIGZAG2/)
* [SPOJ - Cryon](http://www.spoj.com/problems/CRAYON/)
* [SPOJ - Weird Points](http://www.spoj.com/problems/DCEPC705/)
* [SPOJ - Its a Murder](http://www.spoj.com/problems/DCEPC206/)
* [SPOJ - Bored of Suffixes and Prefixes](http://www.spoj.com/problems/KOPC12G/)
* [SPOJ - Mega Inversions](http://www.spoj.com/problems/TRIPINV/)
* [Codeforces - Subsequences](http://codeforces.com/contest/597/problem/C)
* [Codeforces - Ball](http://codeforces.com/contest/12/problem/D)
* [GYM - The Kamphaeng Phet's Chedis](http://codeforces.com/gym/101047/problem/J)
* [Codeforces - Garlands](http://codeforces.com/contest/707/problem/E)
* [Codeforces - Inversions after Shuffle](http://codeforces.com/contest/749/problem/E)
* [GYM - Cairo Market](http://codeforces.com/problemset/gymProblem/101055/D)
* [Codeforces - Goodbye Souvenir](http://codeforces.com/contest/849/problem/E)
* [SPOJ - Ada and Species](http://www.spoj.com/problems/ADACABAA/)
* [Codeforces - Thor](https://codeforces.com/problemset/problem/704/A)
* [CSES - Forest Queries II](https://cses.fi/problemset/task/1739/)
* [Latin American Regionals 2017 - Fundraising](http://matcomgrader.com/problem/9346/fundraising/)

## Các nguồn khác

* [Cây Fenwick trên Wikipedia](http://en.wikipedia.org/wiki/Fenwick_tree)
* [Hướng dẫn về cây chỉ mục nhị phân trên TopCoder](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/)
* [Cập nhật và truy vấn đoạn](https://programmingcontests.quora.com/Tutorial-Range-Updates-in-Fenwick-Tree)