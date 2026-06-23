---
tags:
  - Translated
e_maxx_link: nearest_points
lang: vi
---
# Tìm cặp điểm gần nhất

## Phát biểu bài toán

Cho $n$ điểm trên mặt phẳng. Mỗi điểm $p_i$ được xác định bởi tọa độ $(x_i,y_i)$. Cần tìm trong số đó hai điểm sao cho khoảng cách giữa chúng là nhỏ nhất:

$$ \min_{\scriptstyle i, j=0 \ldots n-1,\atop \scriptstyle i \neq j } \rho (p_i, p_j). $$

Chúng ta sử dụng khoảng cách Euclid thông thường:

$$ \rho (p_i,p_j) = \sqrt{(x_i-x_j)^2 + (y_i-y_j)^2} .$$

Thuật toán vét cạn (brute force) - duyệt qua tất cả các cặp và tính khoảng cách cho từng cặp — hoạt động với độ phức tạp thời gian $O(n^2)$.

Thuật toán có thời gian chạy $O(n \log n)$ được mô tả dưới đây. Thuật toán này được Shamos và Hoey đề xuất vào năm 1975. (Nguồn: Chương 5 trong _Algorithm Design_ của Kleinberg & Tardos, xem thêm [tại đây](https://ieeexplore.ieee.org/abstract/document/4567872)). Preparata và Shamos cũng đã chứng minh rằng thuật toán này là tối ưu trong mô hình cây quyết định.

## Thuật toán
Chúng ta xây dựng thuật toán theo sơ đồ chung của các thuật toán **chia để trị** (divide-and-conquer): thuật toán được thiết kế như một hàm đệ quy, trong đó ta truyền vào một tập hợp các điểm; hàm đệ quy này chia tập hợp thành hai nửa, gọi đệ quy trên từng nửa, và sau đó thực hiện một số thao tác để kết hợp các kết quả. Thao tác kết hợp bao gồm việc phát hiện các trường hợp khi một điểm của cặp tối ưu nằm ở nửa này, và điểm còn lại nằm ở nửa kia (trong trường hợp này, các lời gọi đệ quy riêng lẻ trên từng nửa không thể phát hiện ra cặp này). Khó khăn chính, như thường lệ đối với các thuật toán chia để trị, nằm ở việc cài đặt giai đoạn gộp (merge stage) hiệu quả. Nếu một tập hợp gồm $n$ điểm được truyền vào hàm đệ quy, thì giai đoạn gộp nên thực hiện không quá $O(n)$, khi đó độ phức tạp tiệm cận của toàn bộ thuật toán $T(n)$ sẽ được tìm ra từ phương trình:

$$T(n) = 2T(n/2) + O(n).$$

Nghiệm của phương trình này, như đã biết, là $T(n) = O(n \log n).$

Vì vậy, chúng ta tiến hành xây dựng thuật toán. Để đạt được cách cài đặt giai đoạn gộp hiệu quả trong tương lai, chúng ta sẽ chia tập hợp các điểm thành hai tập con dựa trên tọa độ $x$: Thực tế, ta kẻ một đường thẳng đứng chia tập hợp điểm thành hai tập con có kích thước xấp xỉ nhau. Cách phân chia thuận tiện như sau: Sắp xếp các điểm theo cách chuẩn là cặp số, tức là:

$$p_i < p_j \Longleftrightarrow (x_i < x_j) \lor \Big(\left(x_i = x_j\right) \wedge \left(y_i < y_j \right) \Big) $$

Sau đó lấy điểm ở giữa sau khi sắp xếp $p_m (m = \lfloor n/2 \rfloor)$, tất cả các điểm đứng trước nó và chính $p_m$ được gán vào nửa thứ nhất, và tất cả các điểm sau nó - vào nửa thứ hai:

$$A_1 = \{p_i \ | \ i = 0 \ldots m \}$$

$$A_2 = \{p_i \ | \ i = m + 1 \ldots n-1 \}.$$

Bây giờ, gọi đệ quy trên từng tập hợp $A_1$ và $A_2$, chúng ta sẽ tìm được các câu trả lời $h_1$ và $h_2$ cho từng nửa. Và chọn giá trị tốt nhất trong số đó: $h = \min(h_1, h_2)$.

Bây giờ chúng ta cần thực hiện **giai đoạn gộp**, tức là cố gắng tìm các cặp điểm mà khoảng cách giữa chúng nhỏ hơn $h$, trong đó một điểm nằm trong $A_1$ và điểm kia nằm trong $A_2$. Rõ ràng là chỉ cần xem xét những điểm cách đường thẳng đứng một khoảng nhỏ hơn $h$, tức là tập hợp $B$ các điểm được xem xét ở giai đoạn này bằng:

$$B = \{ p_i\ | \ | x_i - x_m\ | < h \}.$$

Với mỗi điểm trong tập hợp $B$, chúng ta cố gắng tìm các điểm gần nó hơn $h$. Ví dụ, chỉ cần xem xét những điểm có tọa độ $y$ chênh lệch không quá $h$. Hơn nữa, không có ý nghĩa gì khi xem xét những điểm có tọa độ $y$ lớn hơn tọa độ $y$ của điểm hiện tại. Do đó, với mỗi điểm $p_i$, chúng ta xác định tập hợp các điểm được xem xét $C(p_i)$ như sau:

$$C(p_i) = \{ p_j\ |\ p_j \in B,\ \ y_i - h < y_j \le y_i \}.$$

Nếu chúng ta sắp xếp các điểm của tập hợp $B$ theo tọa độ $y$, sẽ rất dễ dàng để tìm $C(p_i)$: đó là một vài điểm liên tiếp đứng trước điểm $p_i$.

Vậy, theo ký hiệu mới, **giai đoạn gộp** trông như sau: xây dựng tập hợp $B$, sắp xếp các điểm trong đó theo tọa độ $y$, sau đó với mỗi điểm $p_i \in B$, xét tất cả các điểm $p_j \in C(p_i)$, và với mỗi cặp $(p_i,p_j)$, tính khoảng cách rồi so sánh với khoảng cách tốt nhất hiện tại.

Thoạt nhìn, đây vẫn là thuật toán chưa tối ưu: có vẻ như kích thước của các tập hợp $C(p_i)$ sẽ ở bậc $n$, và độ phức tạp tiệm cận mong muốn sẽ không đạt được. Tuy nhiên, đáng ngạc nhiên là ta có thể chứng minh rằng kích thước của mỗi tập hợp $C(p_i)$ là một đại lượng $O(1)$, tức là nó không vượt quá một hằng số nhỏ bất kể các điểm là gì. Chứng minh của thực tế này được đưa ra trong phần tiếp theo.

Cuối cùng, chúng ta chú ý đến việc sắp xếp trong thuật toán trên: trước hết là sắp xếp theo cặp $(x, y)$, và sau đó là sắp xếp các phần tử của tập hợp $B$ theo $y$. Thực tế, cả hai phép sắp xếp này bên trong hàm đệ quy đều có thể loại bỏ (nếu không, chúng ta sẽ không đạt được ước lượng $O(n)$ cho **giai đoạn gộp**, và độ phức tạp tiệm cận chung của thuật toán sẽ là $O(n \log^2 n)$). Dễ dàng loại bỏ phép sắp xếp thứ nhất - chỉ cần thực hiện sắp xếp này trước khi bắt đầu đệ quy: vì các phần tử không thay đổi bên trong đệ quy, nên không cần sắp xếp lại. Với phép sắp xếp thứ hai thì khó thực hiện hơn, việc thực hiện nó từ trước sẽ không hiệu quả. Nhưng, nhớ lại thuật toán sắp xếp trộn (Merge Sort), cũng hoạt động dựa trên nguyên lý chia để trị, chúng ta có thể đơn giản nhúng phép sắp xếp này vào đệ quy. Hãy để hàm đệ quy, nhận vào một tập hợp điểm (đã được sắp xếp theo cặp $(x, y)$), trả về chính tập hợp đó nhưng được sắp xếp theo tọa độ $y$. Để làm điều này, chỉ cần trộn (trong $O(n)$) hai kết quả trả về từ các lời gọi đệ quy. Điều này sẽ tạo ra một tập hợp được sắp xếp theo tọa độ $y$.

## Đánh giá độ phức tạp tiệm cận

Để chứng minh rằng thuật toán trên thực sự chạy trong thời gian $O(n \log n)$, chúng ta cần chứng minh thực tế sau: $|C(p_i)| = O(1)$.

Xét một điểm $p_i$; hãy nhớ rằng tập hợp $C(p_i)$ là tập hợp các điểm có tọa độ $y$ nằm trong đoạn $[y_i-h; y_i]$, và hơn nữa, dọc theo tọa độ $x$, điểm $p_i$ và tất cả các điểm của tập hợp $C(p_i)$ nằm trong một dải có độ rộng $2h$. Nói cách khác, các điểm chúng ta đang xem xét $p_i$ và $C(p_i)$ nằm trong một hình chữ nhật có kích thước $2h \times h$.

Nhiệm vụ của chúng ta là ước lượng số lượng điểm tối đa có thể nằm trong hình chữ nhật này $2h \times h$; qua đó, chúng ta ước lượng kích thước tối đa của tập hợp $C(p_i)$. Đồng thời, khi đánh giá, chúng ta không được quên rằng có thể có các điểm trùng lặp.

Nhớ lại rằng $h$ thu được từ kết quả của hai lời gọi đệ quy — trên các tập hợp $A_1$ và $A_2$, trong đó $A_1$ chứa các điểm bên trái đường phân chia và một phần trên đường đó, $A_2$ chứa các điểm còn lại trên đường phân chia và các điểm bên phải nó. Với bất kỳ cặp điểm nào từ $A_1$, cũng như từ $A_2$, khoảng cách không thể nhỏ hơn $h$ — nếu không, nó có nghĩa là hàm đệ quy hoạt động không chính xác.

Để ước lượng số điểm tối đa trong hình chữ nhật $2h \times h$, chúng ta chia nó thành hai hình vuông $h \times h$, hình vuông thứ nhất bao gồm tất cả các điểm $C(p_i) \cap A_1$, và hình thứ hai chứa tất cả các điểm còn lại, tức là $C(p_i) \cap A_2$. Từ các xem xét trên, suy ra trong mỗi hình vuông này, khoảng cách giữa hai điểm bất kỳ đều ít nhất là $h$.

Chúng ta chỉ ra rằng có tối đa bốn điểm trong mỗi hình vuông. Ví dụ, điều này có thể thực hiện như sau: chia hình vuông thành $4$ hình vuông con với các cạnh là $h/2$. Khi đó, không thể có quá một điểm trong mỗi hình vuông con này (vì ngay cả đường chéo cũng bằng $h / \sqrt{2}$, nhỏ hơn $h$). Do đó, không thể có quá $4$ điểm trong toàn bộ hình vuông.

Như vậy, chúng ta đã chứng minh rằng trong hình chữ nhật $2h \times h$ không thể có quá $4 \cdot 2 = 8$ điểm, và do đó, kích thước của tập hợp $C(p_i)$ không thể vượt quá $7$, như yêu cầu.

## Cài đặt

Chúng ta giới thiệu một cấu trúc dữ liệu để lưu trữ một điểm (tọa độ và chỉ số của nó) cùng các toán tử so sánh cần thiết cho hai kiểu sắp xếp:

```{.cpp file=nearest_pair_def}
struct pt {
    int x, y, id;
};

struct cmp_x {
    bool operator()(const pt & a, const pt & b) const {
        return a.x < b.x || (a.x == b.x && a.y < b.y);
    }
};
 
struct cmp_y {
    bool operator()(const pt & a, const pt & b) const {
        return a.y < b.y;
    }
};
 
int n;
vector<pt> a;
```

Để thuận tiện cho việc cài đặt đệ quy, chúng ta đưa vào một hàm phụ `upd_ans()`, sẽ tính khoảng cách giữa hai điểm và kiểm tra xem nó có tốt hơn câu trả lời hiện tại hay không:

```{.cpp file=nearest_pair_update}
double mindist;
pair<int, int> best_pair;
 
void upd_ans(const pt & a, const pt & b) {
    double dist = sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y));
    if (dist < mindist) {
        mindist = dist;
        best_pair = {a.id, b.id};
    }
}
```

Cuối cùng, phần cài đặt đệ quy. Giả định rằng trước khi gọi đệ quy, mảng $a[]$ đã được sắp xếp theo tọa độ $x$. Trong đệ quy, ta truyền vào hai con trỏ $l, r$, chỉ ra rằng cần tìm câu trả lời cho $a[l \ldots r)$. Nếu khoảng cách giữa $r$ và $l$ quá nhỏ, đệ quy phải dừng lại, thực hiện thuật toán vét cạn để tìm cặp gần nhất, sau đó sắp xếp mảng con theo tọa độ $y$.

Để gộp hai tập hợp điểm nhận được từ các lời gọi đệ quy thành một (được sắp xếp theo tọa độ $y$), chúng ta sử dụng hàm chuẩn $merge()$ của STL và tạo một bộ đệm phụ $t[]$ (một bộ đệm dùng chung cho tất cả các lời gọi đệ quy). (Sử dụng `inplace_merge()` là không thực tế vì nó thường không hoạt động trong thời gian tuyến tính).

Cuối cùng, tập hợp $B$ được lưu trữ trong cùng mảng $t$.

```{.cpp file=nearest_pair_rec}
vector<pt> t;

void rec(int l, int r) {
    if (r - l <= 3) {
        for (int i = l; i < r; ++i) {
            for (int j = i + 1; j < r; ++j) {
                upd_ans(a[i], a[j]);
            }
        }
        sort(a.begin() + l, a.begin() + r, cmp_y());
        return;
    }

    int m = (l + r) >> 1;
    int midx = a[m].x;
    rec(l, m);
    rec(m, r);

    merge(a.begin() + l, a.begin() + m, a.begin() + m, a.begin() + r, t.begin(), cmp_y());
    copy(t.begin(), t.begin() + r - l, a.begin() + l);

    int tsz = 0;
    for (int i = l; i < r; ++i) {
        if (abs(a[i].x - midx) < mindist) {
            for (int j = tsz - 1; j >= 0 && a[i].y - t[j].y < mindist; --j)
                upd_ans(a[i], t[j]);
            t[tsz++] = a[i];
        }
    }
}
```

Nhân tiện, nếu tất cả các tọa độ là số nguyên, thì tại thời điểm đệ quy bạn không cần chuyển sang giá trị phân số, và có thể lưu bình phương của khoảng cách nhỏ nhất vào $mindist$.

Trong chương trình chính, đệ quy nên được gọi như sau:

```{.cpp file=nearest_pair_main}
t.resize(n);
sort(a.begin(), a.end(), cmp_x());
mindist = 1E20;
rec(0, n);
```

## Các thuật toán ngẫu nhiên thời gian tuyến tính

### Một thuật toán ngẫu nhiên với thời gian kỳ vọng tuyến tính

Một phương pháp thay thế, ban đầu được Rabin đề xuất vào năm 1976, xuất phát từ một ý tưởng rất đơn giản để cải thiện thời gian chạy theo hướng heuristic: Chúng ta có thể chia mặt phẳng thành một lưới các hình vuông $d \times d$, sau đó chỉ cần kiểm tra khoảng cách giữa các điểm trong cùng một ô hoặc các ô lân cận (trừ khi tất cả các ô không liên thông với nhau, nhưng chúng ta sẽ tránh điều này bằng cách thiết kế), vì bất kỳ cặp điểm nào khác đều có khoảng cách lớn hơn hai điểm trong cùng một ô.

<div style="text-align: center;" markdown="1">

![Ví dụ về chiến lược chia ô vuông](nearest_points_blocks_example.png)

</div>

Chúng ta sẽ chỉ xem xét các ô vuông có chứa ít nhất một điểm. Ký hiệu $n_1, n_2, \dots, n_k$ là số lượng điểm trong mỗi ô vuông $k$ còn lại. Giả sử có ít nhất hai điểm nằm trong cùng một ô hoặc các ô lân cận, và không có điểm trùng lặp, độ phức tạp thời gian là $\Theta\!\left(\sum\limits_{i=1}^k n_i^2\right)$. Chúng ta có thể tìm các điểm trùng lặp trong thời gian kỳ vọng tuyến tính bằng cách sử dụng bảng băm (hash table), và nếu có, câu trả lời chính là cặp đó.

??? info "Chứng minh"
	Đối với ô vuông thứ $i$ chứa $n_i$ điểm, số lượng cặp bên trong là $\Theta(n_i^2)$. Nếu ô vuông thứ $i$ kề với ô vuông thứ $j$, thì chúng ta cũng thực hiện $n_i n_j \le \max(n_i, n_j)^2 \le n_i^2 + n_j^2$ phép so sánh khoảng cách. Lưu ý rằng mỗi ô vuông có tối đa $8$ ô vuông lân cận, vì vậy chúng ta có thể chặn tổng tất cả các phép so sánh bằng $\Theta(\sum_{i=1}^{k} n_i^2)$. $\quad \blacksquare$

Bây giờ chúng ta cần quyết định cách đặt $d$ sao cho nó tối thiểu hóa $\Theta\!\left(\sum\limits_{i=1}^k n_i^2\right)$.

#### Chọn d

Chúng ta cần $d$ là một xấp xỉ của khoảng cách tối thiểu $d$. Richard Lipton đề xuất lấy mẫu ngẫu nhiên $n$ khoảng cách và chọn $d$ là giá trị nhỏ nhất trong số đó làm xấp xỉ cho $d$. Chúng ta sẽ chứng minh rằng thời gian chạy kỳ vọng của thuật toán là tuyến tính.

??? info "Chứng minh"
	Hãy tưởng tượng sự sắp xếp các điểm trong các ô vuông với một lựa chọn cụ thể của $d$, giả sử là $x$. Xét $d$ là một biến ngẫu nhiên, kết quả từ việc lấy mẫu các khoảng cách của chúng ta. Hãy định nghĩa $C(x) := \sum_{i=1}^{k(x)} n_i(x)^2$ là ước lượng chi phí cho một sự sắp xếp cụ thể khi ta chọn $d=x$. Bây giờ, hãy định nghĩa $\lambda(x)$ sao cho $C(x) = \lambda(x) \, n$. Xác suất để lựa chọn $x$ như vậy tồn tại sau khi lấy mẫu $n$ khoảng cách độc lập là bao nhiêu? Nếu một cặp duy nhất trong số các cặp được lấy mẫu có khoảng cách nhỏ hơn $x$, thì sự sắp xếp này sẽ bị thay thế bởi $d$ nhỏ hơn. Bên trong một ô vuông, khoảng $1/16$ các cặp sẽ tạo ra một khoảng cách nhỏ hơn (hãy tưởng tượng bốn hình vuông con trong mỗi hình vuông; theo nguyên lý Dirichlet, ít nhất một hình vuông con có $n_i/4$ điểm), vì vậy chúng ta có khoảng $\sum_{i=1}^{k} {n_i/4 \choose 2} \approx \sum_{i=1}^{k} \frac{1}{16} {n_i \choose 2}$ các cặp mang lại một $d$ cuối cùng nhỏ hơn. Đây là, xấp xỉ, $\frac{1}{32} \sum_{i=1}^{k} n_i^2 = \frac{1}{32} \lambda(x) n$. Mặt khác, có khoảng $\frac{1}{2} n^2$ cặp có thể được lấy mẫu. Xác suất lấy mẫu một cặp có khoảng cách nhỏ hơn $x$ là ít nhất (xấp xỉ)
	
	$$\frac{\lambda(x) \, n / 32}{n^2 / 2} = \frac{\lambda(x)/16}{n}$$
	
	vì vậy xác suất ít nhất một cặp như vậy được chọn trong $n$ vòng (và do đó tìm thấy $d$ nhỏ hơn) là
	
	$$1 - \left(1 - \frac{\lambda(x)/16}{n}\right)^n \ge 1 - e^{-\lambda(x)/16}$$
	
	(chúng ta đã sử dụng bất đẳng thức $(1 + x)^n \le e^{xn}$ cho bất kỳ số thực $x$, xem [bất đẳng thức Bernoulli](https://en.wikipedia.org/wiki/Bernoulli%27s_inequality#Related_inequalities)). <br> Lưu ý rằng điều này tiến tới $1$ theo hàm mũ khi $\lambda(x)$ tăng. Điều này gợi ý rằng $\lambda$ sẽ nhỏ đối với một $d$ được chọn tồi.
	
	
	Chúng ta đã chỉ ra rằng $\Pr(d \le x) \ge 1 - e^{-\lambda(x)/16}$, hay tương đương, $\Pr(d \ge x) \le e^{-\lambda(x)/16}$. Chúng ta cần biết $\Pr(\lambda(d) \ge \text{something})$ để có thể ước lượng giá trị kỳ vọng của nó. Ta nhận thấy rằng $\lambda(d) \ge \lambda(x) \iff d \ge x$. Điều này là do việc làm cho các ô vuông nhỏ hơn chỉ làm giảm số lượng điểm trong mỗi ô (chia các điểm vào các ô khác), và điều này giữ cho tổng các bình phương giảm xuống. Do đó,
	
	$$\Pr(\lambda(d) \ge \lambda(x)) = \Pr(d \ge x) \le e^{-\lambda(x)/16} \implies \Pr(\lambda(d) \ge t) \le e^{-t/16} \implies \mathbb{E}[\lambda(d)] \le \int_{0}^{+\infty} e^{-t/16} \, \mathrm{d}t = 16$$
	
	(chúng ta đã sử dụng $E[X] = \int_0^{+\infty} \Pr(X \ge x) \, \mathrm{d}x$, xem [chứng minh trên Stackexchange](https://math.stackexchange.com/a/1690829)).
	
	Cuối cùng, $\mathbb{E}[C(d)] = \mathbb{E}[\lambda(d) \, n] \le 16n$, và thời gian chạy kỳ vọng là $O(n)$, với một hệ số hằng số hợp lý. $\quad \blacksquare$

#### Cài đặt thuật toán

Ưu điểm của thuật toán này là rất dễ cài đặt, nhưng vẫn có hiệu suất tốt trong thực tế. Đầu tiên, chúng ta lấy mẫu $n$ khoảng cách và đặt $d$ là giá trị nhỏ nhất trong số đó. Sau đó, chúng ta chèn các điểm vào các "ô" bằng cách sử dụng bảng băm ánh xạ từ tọa độ 2D sang một vector chứa các điểm. Cuối cùng, chỉ cần tính khoảng cách giữa các cặp điểm trong cùng ô và các cặp điểm ở ô lân cận. Các thao tác trên bảng băm có chi phí thời gian kỳ vọng là $O(1)$, do đó thuật toán của chúng ta giữ nguyên chi phí thời gian kỳ vọng $O(n)$ với một hằng số lớn hơn một chút.

Xem [bài nộp này](https://judge.yosupo.jp/submission/309605) trên Library Checker.

```{.cpp file=nearest_pair_randomized}
#include <bits/stdc++.h>
using namespace std;


using ll = long long;
using ld = long double;


struct pt {
	ll x, y;
	pt() {}
	pt(ll x_, ll y_) : x(x_), y(y_) {}
	void read() {
		cin >> x >> y;
	}
};

bool operator==(const pt& a, const pt& b) {
    return a.x == b.x and a.y == b.y;
}


struct CustomHashPoint {
	size_t operator()(const pt& p) const {
		static const uint64_t C = chrono::steady_clock::now().time_since_epoch().count();
		return C ^ ((p.x << 32) ^ p.y);
	}
};


ll dist2(pt a, pt b) {
	ll dx = a.x - b.x;
	ll dy = a.y - b.y;
	return dx*dx + dy*dy;
}


pair<int,int> closest_pair_of_points(vector<pt> P) {
    int n = int(P.size());
    assert(n >= 2);

    // if there is a duplicated point, we have the solution
    unordered_map<pt,int,CustomHashPoint> previous;
    for (int i = 0; i < int(P.size()); ++i) {
        auto it = previous.find(P[i]);
        if (it != previous.end()) {
            return {it->second, i};
        }
        previous[P[i]] = i;
    }

	unordered_map<pt,vector<int>,CustomHashPoint> grid;
	grid.reserve(n);

	mt19937 rd(chrono::system_clock::now().time_since_epoch().count());
	uniform_int_distribution<int> dis(0, n-1);

	ll d2 = dist2(P[0], P[1]);
	pair<int,int> closest = {0, 1};

	auto candidate_closest = [&](int i, int j) -> void {
		ll ab2 = dist2(P[i], P[j]);
		if (ab2 < d2) {
			d2 = ab2;
			closest = {i, j};
		}
	};

	for (int i = 0; i < n; ++i) {
		int j = dis(rd);
		int k = dis(rd);
		while (j == k) k = dis(rd);
		candidate_closest(j, k);
	}

	ll d = ll( sqrt(ld(d2)) + 1 );

	for (int i = 0; i < n; ++i) {
		grid[{P[i].x/d, P[i].y/d}].push_back(i);
	}

	// same block
	for (const auto& it : grid) {
		int k = int(it.second.size());
		for (int i = 0; i < k; ++i) {
			for (int j = i+1; j < k; ++j) {
				candidate_closest(it.second[i], it.second[j]);
			}
		}
	}
 
	// adjacent blocks
	for (const auto& it : grid) {
		auto coord = it.first;
		for (int dx = 0; dx <= 1; ++dx) {
			for (int dy = -1; dy <= 1; ++dy) {
				if (dx == 0 and dy == 0) continue;
				pt neighbour = pt(
					coord.x  + dx, 
					coord.y + dy
                );
				for (int i : it.second) {
					if (not grid.count(neighbour)) continue;
					for (int j : grid.at(neighbour)) {
						candidate_closest(i, j);
					}
				}
			}
		}
	}

	return closest;
}
```

### Một thuật toán ngẫu nhiên thay thế với thời gian kỳ vọng tuyến tính

Bây giờ chúng ta giới thiệu một thuật toán ngẫu nhiên khác ít thực dụng hơn nhưng rất dễ chứng minh rằng nó chạy trong thời gian kỳ vọng tuyến tính.

- Hoán vị ngẫu nhiên $n$ điểm
- Lấy $\delta := \operatorname{dist}(p_1, p_2)$
- Phân chia mặt phẳng thành các ô vuông cạnh $\delta/2$
- Với $i = 1,2,\dots,n$:
	- Lấy ô vuông tương ứng với $p_i$
	- Lặp qua các ô vuông $25$ trong phạm vi hai bước xung quanh ô của chúng ta trong lưới phân chia mặt phẳng
	- Nếu một $p_j$ nào đó trong các ô đó có $\operatorname{dist}(p_j, p_i) < \delta$, thì
		- Tính toán lại phân chia và các ô vuông với $\delta := \operatorname{dist}(p_j, p_i)$
		- Lưu trữ các điểm $p_1, \dots, p_i$ vào các ô tương ứng
	- Nếu không, lưu $p_i$ vào ô tương ứng
- đầu ra $\delta$

Tính đúng đắn đến từ việc tại bất kỳ thời điểm nào chúng ta đã có một cặp có khoảng cách $\delta$, vì vậy chúng ta chỉ cố gắng tìm các cặp mới có khoảng cách nhỏ hơn $\delta$. Vì mỗi ô vuông có cạnh $\delta/2$, một cặp ứng viên có thể cách nhau tối đa $2$ ô, nên với một điểm cho trước, chúng ta kiểm tra các ứng viên trong các ô xung quanh $25$. Bất kỳ điểm nào trong ô xa hơn sẽ luôn cho khoảng cách lớn hơn $\delta$.

Mặc dù thuật toán này có vẻ chậm vì phải tính toán lại mọi thứ nhiều lần, ta có thể chứng minh tổng chi phí kỳ vọng là tuyến tính.

??? info "Chứng minh"
	Gọi $X_i$ là biến ngẫu nhiên nhận giá trị $1$ khi điểm $p_i$ gây ra sự thay đổi $\delta$ và tính toán lại các cấu trúc dữ liệu, và $0$ nếu không. Dễ dàng chỉ ra rằng chi phí là $O(n + \sum_{i=1}^{n} i X_i)$, vì ở bước $i$ chúng ta chỉ xét $i$ điểm đầu tiên. Tuy nhiên, hóa ra $\Pr(X_i = 1) \le \frac{2}{i}$. Điều này là do ở bước $i$, $\delta$ là khoảng cách của cặp gần nhất trong $\{p_1,\dots,p_i\}$, và $\Pr(X_i = 1)$ là xác suất để $p_i$ thuộc về cặp gần nhất, điều này chỉ xảy ra trong $2(i-1)$ cặp trong tổng số $i(i-1)$ cặp có thể (giả sử tất cả các khoảng cách đều khác nhau), vì vậy xác suất tối đa là $\frac{2(i-1)}{i(i-1)} = \frac{2}{i}$, vì trước đó chúng ta đã hoán vị các điểm một cách đồng nhất.
	
	Vì vậy, chúng ta có thể thấy chi phí kỳ vọng là
	
	$$O\!\left(n + \sum_{i=1}^{n} i \Pr(X_i = 1)\right) \le O\!\left(n + \sum_{i=1}^{n} i \frac{2}{i}\right) = O(3n) = O(n) \quad \quad \blacksquare$$

## Tổng quát hóa: tìm tam giác có chu vi nhỏ nhất

Thuật toán mô tả ở trên được mở rộng thú vị cho bài toán này: trong một tập hợp điểm đã cho, chọn ba điểm khác nhau sao cho tổng khoảng cách giữa các cặp điểm đó là nhỏ nhất.

Thực tế, để giải bài toán này, thuật toán vẫn như cũ: chúng ta chia mặt phẳng thành hai nửa bởi đường thẳng đứng, gọi đệ quy lời giải trên cả hai nửa, chọn giá trị $minper$ tối thiểu từ các chu vi tìm được, xây dựng một dải có độ dày $minper / 2$, và lặp qua tất cả các tam giác có thể cải thiện câu trả lời. (Lưu ý rằng tam giác có chu vi $\le minper$ có cạnh dài nhất là $\le minper / 2$.)

## Các bài tập thực hành

* [UVA 10245 "The Closest Pair Problem" [độ khó: thấp]](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1186)
* [SPOJ #8725 CLOPPAIR "Closest Point Pair" [độ khó: thấp]](https://www.spoj.com/problems/CLOPPAIR/)
* [CODEFORCES Team Olympiad Saratov - 2011 "Minimum amount" [độ khó: trung bình]](http://codeforces.com/contest/120/problem/J)
* [Google CodeJam 2009 Final "Min Perimeter" [độ khó: trung bình]](https://github.com/google/coding-competitions-archive/blob/main/codejam/2009/world_finals/min_perimeter/statement.pdf)
* [SPOJ #7029 CLOSEST "Closest Triple" [độ khó: trung bình]](https://www.spoj.com/problems/CLOSEST/)
* [TIMUS 1514 National Park [độ khó: trung bình]](https://acm.timus.ru/problem.aspx?space=1&num=1514)