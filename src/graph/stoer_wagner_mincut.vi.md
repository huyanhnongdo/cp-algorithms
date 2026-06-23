---
tags:
  - Translated
e_maxx_link: stoer_wagner_mincut
lang: vi
---

# Lát cắt tối thiểu - Thuật toán Stoer-Wagner

## Phát biểu bài toán

Cho một đồ thị vô hướng có trọng số $G$ gồm $n$ đỉnh và $m$ cạnh. Một lát cắt $C$ là một tập con thực sự, khác rỗng của tập đỉnh (nói một cách dễ hiểu, một lát cắt phân hoạch các đỉnh thành hai tập hợp khác rỗng: tập chứa các đỉnh thuộc $C$ và tập chứa các đỉnh còn lại). Trọng số của lát cắt là tổng trọng số của các cạnh đi qua lát cắt, tức là các cạnh có đúng một đầu mút thuộc $C$:

$$ w(C) = \sum_{\substack{(v,u) \in E \\ u \in C,\ v \not\in C}} c(v,u), $$

trong đó $E$ là tập hợp tất cả các cạnh của đồ thị $G$, và $c(v,u)$ là trọng số của cạnh $(v,u)$.

Nhiệm vụ của chúng ta là tìm một **lát cắt có trọng số nhỏ nhất** (lát cắt tối thiểu).

Đôi khi bài toán này được gọi là "lát cắt tối thiểu toàn cục" (global minimum cut) — để phân biệt với bài toán tìm lát cắt tối thiểu $C$ có đỉnh nguồn $s$ và đỉnh đích $t$ cho trước, sao cho lát cắt chứa $t$ nhưng không chứa $s$. Lát cắt tối thiểu toàn cục bằng giá trị nhỏ nhất trong số các lát cắt tối thiểu $s$-$t$ trên mọi cặp nguồn-đích $(s, t)$ khả dĩ.

Mặc dù bài toán này có thể được giải quyết bằng thuật toán luồng cực đại (bằng cách chạy nó $O(n^2)$ lần cho tất cả các cặp nguồn và đích), dưới đây chúng ta sẽ mô tả một thuật toán đơn giản và nhanh hơn nhiều, được đề xuất bởi Mechthild Stoer và Frank Wagner in 1994.

Nói chung, đồ thị có thể có khuyên (loop) và đa cạnh (multiple edges), mặc dù các khuyên rõ ràng không ảnh hưởng đến kết quả theo bất kỳ cách nào, và các đa cạnh luôn có thể được thay thế bằng một cạnh duy nhất có trọng số bằng tổng trọng số của chúng. Do đó, để đơn giản, chúng ta giả định đồ thị đầu vào không chứa khuyên hay đa cạnh.

## Mô tả thuật toán

**Ý tưởng cơ bản** của thuật toán vô cùng đơn giản. Chúng ta lặp đi lặp lại quy trình sau: tìm lát cắt tối thiểu giữa một cặp đỉnh $s$ và $t$ nào đó, rồi gộp hai đỉnh này thành một (nối các danh sách kề của chúng lại). Cuối cùng, sau $n-1$ bước lặp, đồ thị sẽ được nén lại chỉ còn đúng một đỉnh duy nhất và quy trình dừng lại. Sau đó, kết quả của bài toán chính là giá trị nhỏ nhất trong số tất cả $n-1$ lát cắt tìm được ở mỗi bước. Thật vậy, ở mỗi giai đoạn thứ $i$, lát cắt tối thiểu $C_i$ tìm được giữa hai đỉnh $s_i$ và $t_i$ hoặc chính là lát cắt tối thiểu toàn cục cần tìm, hoặc ngược lại, việc đặt $s_i$ và $t_i$ vào hai phần khác nhau của lát cắt tối thiểu toàn cục là không tối ưu, do đó chúng ta không làm mất mát nghiệm tối ưu khi gộp hai đỉnh này lại làm một.

Do đó, chúng ta đưa bài toán về bài toán con sau: với một đồ thị cho trước, tìm **lát cắt tối thiểu giữa một cặp đỉnh** s and t **tùy ý**. Để giải quyết bài toán này, quy trình lặp sau đây được đề xuất. Chúng ta khởi tạo một tập hợp đỉnh $A$, ban đầu chỉ chứa duy nhất một đỉnh tùy ý. Tại mỗi bước, chúng ta tìm đỉnh **kết nối mạnh nhất** với tập hợp $A$, tức là đỉnh $v \not\in A$ sao cho lượng dưới đây đạt cực đại:

$$ w(v,A) = \sum_{\substack{(v,u) \in E \\ u \in A}} c(v,u) $$

(tức là tổng trọng số các cạnh có một đầu mút là $v$ và đầu mút kia thuộc $A$ là lớn nhất).

Quy trình này cũng kết thúc sau $n-1$ bước lặp, khi tất cả các đỉnh đều đã được đưa vào tập hợp $A$ (quy trình này cực kỳ giống với [Thuật toán Prim](mst_prim.md)). Khi đó, theo **định lý Stoer-Wagner** phát biểu, nếu ký hiệu s and t là hai đỉnh cuối cùng được thêm vào $A$, thì lát cắt tối thiểu giữa các đỉnh s and t chính là lát cắt phân tách đỉnh đơn $t$ ra khỏi phần còn lại của đồ thị. Chứng minh của định lý này sẽ được trình bày ở phần tiếp theo (tuy nhiên, việc chứng minh này không đóng góp nhiều vào việc hiểu thuật toán).

Do đó, **lược đồ tổng thể của thuật toán Stoer-Wagner** như sau: Thuật toán gồm $n-1$ pha. Ở mỗi pha, tập hợp $A$ ban đầu được đặt chứa một đỉnh nào đó, và tính toán các trọng số bắt đầu $w(v,A)$ của các đỉnh. Sau đó là $n-1$ bước lặp, trong mỗi bước đỉnh u với giá trị $w(v,A)$ lớn nhất được chọn và đưa vào tập hợp $A$, rồi cập nhật lại các giá trị $w$ của các đỉnh còn lại (để làm việc này, ta chỉ cần duyệt qua tất cả các cạnh trong danh sách kề của đỉnh u vừa chọn). Sau khi thực hiện xong tất cả các bước lặp, ta ghi nhận ở s and t hai đỉnh được thêm vào cuối cùng, và giá trị $w(t,A \setminus t)$ chính là chi phí của lát cắt tối thiểu s and t tìm được. Chúng ta so sánh lát cắt tối thiểu này với kết quả hiện tại, nếu nó nhỏ hơn thì cập nhật lại kết quả, và chuyển sang pha tiếp theo.

Nếu không sử dụng bất kỳ cấu trúc dữ liệu phức tạp nào, phần quan trọng nhất là tìm đỉnh có giá trị $w$ lớn nhất. Nếu chúng ta tìm kiếm mất $O(n)$, thì vì có $n-1$ pha, mỗi pha có $n-1$ bước lặp, **độ phức tạp thời gian** tổng thể của thuật toán là $O(n^3)$.

Nếu sử dụng **Heap Fibonacci** để tìm đỉnh có giá trị $w$ lớn nhất (cho phép tăng giá trị khóa trong thời gian phân bổ $O(1)$ và lấy ra phần tử lớn nhất trong thời gian phân bổ $O(\log n)$), thì tất cả các thao tác liên quan đến tập hợp $A$ trong một pha được thực hiện trong thời gian $O(m + n \log n)$. Độ phức tạp của thuật toán trong trường hợp này là $O(n m + n^2 \log n)$.

## Chứng minh định lý Stoer-Wagner

Hãy nhắc lại phát biểu của định lý: Nếu chúng ta thêm lần lượt từng đỉnh vào tập $A$, mỗi lần chọn đỉnh kết nối mạnh nhất với tập này, và gọi đỉnh kề cuối được thêm vào là $s$ và đỉnh cuối cùng là $t$. Khi đó lát cắt tối thiểu $s$-$t$ chính là lát cắt phân tách đỉnh đơn $t$ ra khỏi phần còn lại của đồ thị.

Để chứng minh, xét một lát cắt $s$-$t$ bất kỳ $C$ và chỉ ra rằng trọng số của nó không thể nhỏ hơn trọng số của lát cắt phân tách duy nhất đỉnh $t$:

$$ w(\{t\}) \le w(C). $$

Để làm việc này, chúng ta chứng minh bổ đề sau. Gọi $A_v$ là trạng thái của tập hợp $A$ ngay trước khi thêm đỉnh $v$. Gọi $C_v$ là lát cắt của tập hợp $A_v \cup \{v\}$ được cảm sinh bởi lát cắt $C$ (nói một cách đơn giản, $C_v$ bằng giao của hai tập hợp đỉnh này). Tiếp theo, một đỉnh $v$ được gọi là hoạt động (active - đối với lát cắt $C$) nếu đỉnh $v$ và đỉnh được thêm ngay trước nó thuộc hai phần khác nhau của lát cắt $C$. Khi đó, ta khẳng định rằng với mọi đỉnh hoạt động $v$, bất đẳng thức sau luôn được thỏa mãn:

$$ w(v,A_v) \le w(C_v). $$

Đặc biệt, $t$ chắc chắn là một đỉnh hoạt động (vì đỉnh được thêm ngay trước nó là $s$ nằm ở phía bên kia lát cắt $C$ so với $t$), và với $v = t$, bất đẳng thức này trở thành phát biểu của định lý:

$$ w(t,A_t) = w(\{t\}) \le w(C_t) = w(C). $$

Chúng ta sẽ chứng minh bất đẳng thức này bằng phương pháp quy nạp toán học.

Với đỉnh hoạt động đầu tiên $v$, bất đẳng thức hiển nhiên đúng (thậm chí trở thành đẳng thức) — vì tất cả các đỉnh thuộc $A_v$ đều thuộc cùng một phần của lát cắt, và $v$ thuộc phần còn lại.

Giả sử bất đẳng thức đã đúng cho tất cả các đỉnh hoạt động trước $u$. Ta chứng minh bất đẳng thức cũng đúng cho đỉnh hoạt động tiếp theo $u$. Biến đổi vế trái:

$$ w(u,A_u) \equiv w(u,A_v) + w(u,A_u \setminus A_v). $$

Trước tiên, lưu ý rằng:

$$ w(u,A_v) \le w(v,A_v), $$

điều này suy ra từ việc khi tập hợp $A$ bằng $A_v$, đỉnh được chọn thêm vào tập hợp là $v$ chứ không phải $u$, nghĩa là $v$ có giá trị $w$ lớn hơn.

Tiếp theo, vì $w(v,A_v) \le w(C_v)$ theo giả thiết quy nạp, ta có:

$$ w(u,A_v) \le w(C_v), $$

suy ra:

$$ w(u,A_u) \le w(C_v) + w(u,A_u \setminus A_v). $$

Lưu ý rằng đỉnh $u$ và tất cả các đỉnh thuộc $A_u \setminus A_v$ nằm ở hai phần khác nhau của lát cắt $C$, do đó lượng $w(u,A_u \setminus A_v)$ đại diện cho tổng trọng số các cạnh được tính trong $w(C_u)$ nhưng chưa được tính trong $w(C_v)$. Từ đó ta có:

$$ w(u,A_u) \le w(C_v) + w(u,A_u \setminus A_v) \le w(C_u), $$

đây chính là điều phải chứng minh.

Chúng ta đã chứng minh được hệ thức $w(v,A_v) \le w(C_v)$, và định lý được chứng minh hoàn toàn.

## Cài đặt

Với cài đặt đơn giản nhất (độ phức tạp $O(n^3)$), đồ thị được biểu diễn bằng ma trận kề. Kết quả được lưu trong các biến `best_cost` và `best_cut` (trọng số của lát cắt tối thiểu và các đỉnh thuộc lát cắt đó).

Với mỗi đỉnh, mảng `exist` lưu thông tin xem nó có còn tồn tại trên đồ thị hay không, hay nó đã được gộp vào đỉnh khác. Danh sách `v[i]` với mỗi đỉnh đã gộp $i$ lưu chỉ số của các đỉnh ban đầu đã được gộp vào đỉnh $i$ này.

Thuật toán gồm $n-1$ pha (vòng lặp theo biến `ph`). Ở mỗi pha, tất cả các đỉnh ban đầu nằm ngoài tập hợp $A$, mảng `in_a` được điền các giá trị `false`, và kết nối $w$ của tất cả các đỉnh bằng 0. Trong mỗi bước lặp thứ $n-\mathrm{ph}$, đỉnh `sel` có giá trị $w$ lớn nhất được tìm ra. Nếu đây là bước lặp cuối cùng, kết quả được cập nhật nếu cần thiết, và gộp hai đỉnh được chọn cuối cùng `sel` và kề cuối `prev` lại làm một. Nếu không phải bước lặp cuối, đỉnh `sel` được thêm vào tập hợp $A$, sau đó cập nhật lại trọng số của các đỉnh còn lại.

Lưu ý rằng thuật toán sẽ làm thay đổi ma trận kề `g` trong quá trình chạy, nên nếu bạn cần sử dụng lại đồ thị sau đó, hãy sao lưu một bản trước khi gọi hàm.

```{.cpp file=stoer_wagner_mincut}
const int MAXN = 500;
int n;
long long g[MAXN][MAXN];
long long best_cost = (1LL << 62);
vector<int> best_cut;

void mincut() {
    vector<int> v[MAXN];
    for (int i = 0; i < n; ++i)
        v[i].assign(1, i);
    long long w[MAXN];
    bool exist[MAXN], in_a[MAXN];
    memset(exist, true, sizeof exist);
    for (int ph = 0; ph < n - 1; ++ph) {
        memset(in_a, false, sizeof in_a);
        memset(w, 0, sizeof w);
        for (int it = 0, prev; it < n - ph; ++it) {
            int sel = -1;
            for (int i = 0; i < n; ++i)
                if (exist[i] && !in_a[i] && (sel == -1 || w[i] > w[sel]))
                    sel = i;
            if (it == n - ph - 1) {
                if (w[sel] < best_cost) {
                    best_cost = w[sel];
                    best_cut = v[sel];
                }
                v[prev].insert(v[prev].end(), v[sel].begin(), v[sel].end());
                for (int i = 0; i < n; ++i)
                    g[prev][i] = g[i][prev] += g[sel][i];
                exist[sel] = false;
            } else {
                in_a[sel] = true;
                for (int i = 0; i < n; ++i)
                    w[i] += g[sel][i];
                prev = sel;
            }
        }
    }
}
```

## Tài liệu tham khảo

- [Mechthild Stoer, Frank Wagner. A Simple Min-Cut Algorithm. Journal of the ACM, 44(4):585-591, 1997](https://dl.acm.org/doi/10.1145/263867.263872)
- [Kurt Mehlhorn, Christian Uhrig. The minimum cut algorithm of Stoer and Wagner [1995]](https://www.researchgate.net/publication/2483703_The_minimum_cut_algorithm_of_Stoer_and_Wagner)
