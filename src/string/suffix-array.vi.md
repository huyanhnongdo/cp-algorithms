---
tags:
  - Translated
e_maxx_link: suffix_array
lang: vi
---

# Mảng hậu tố (Suffix Array)

## Định nghĩa

Cho một xâu $s$ độ dài $n$. Hậu tố thứ $i$ của $s$ là xâu con $s[i \ldots n - 1]$.

Một **mảng hậu tố (suffix array)** chứa các số nguyên đại diện cho **chỉ số bắt đầu** của tất cả các hậu tố của một xâu cho trước, sau khi các hậu tố này đã được sắp xếp theo thứ tự từ điển.

Ví dụ, xét xâu $s = abaab$.
Tất cả các hậu tố của nó là:

$$\begin{array}{ll}
0. & abaab \\
1. & baab \\
2. & aab \\
3. & ab \\
4. & b
\end{array}$$

Sau khi sắp xếp các xâu này theo thứ tự từ điển:

$$\begin{array}{ll}
2. & aab \\
3. & ab \\
0. & abaab \\
4. & b \\
1. & baab
\end{array}$$

Do đó, mảng hậu tố của $s$ sẽ là $(2,~ 3,~ 0,~ 4,~ 1)$.

Là một cấu trúc dữ liệu, mảng hậu tố được sử dụng rộng rãi trong các lĩnh vực như nén dữ liệu, tin sinh học và nhìn chung trong bất kỳ lĩnh vực nào liên quan đến xử lý xâu ký tự và các bài toán khớp mẫu trên xâu (string matching).

## Xây dựng

### Cách tiếp cận $O(n^2 \log n)$ {data-toc-label="Cách tiếp cận O(n^2 log n)"}

Đây là cách tiếp cận ngây thơ nhất.
Lấy ra tất cả các hậu tố và sắp xếp chúng bằng các thuật toán như Quicksort hoặc Mergesort, đồng thời lưu lại chỉ số gốc của chúng.
Việc sắp xếp tốn $O(n \log n)$ phép so sánh, và vì việc so sánh hai xâu tốn thêm $O(n)$ thời gian, chúng ta thu được độ phức tạp cuối cùng là $O(n^2 \log n)$.

### Cách tiếp cận $O(n \log n)$ {data-toc-label="Cách tiếp cận O(n log n)"}

Nói một cách chính xác, thuật toán sau đây không trực tiếp sắp xếp các hậu tố, mà là sắp xếp các **dịch vòng (cyclic shift)** của xâu.
Tuy nhiên, chúng ta có thể dễ dàng chuyển đổi thành thuật toán sắp xếp hậu tố từ nó:
chỉ cần thêm một ký tự đặc biệt vào cuối xâu, ký tự này phải nhỏ hơn mọi ký tự khác có trong xâu.
Thông thường chúng ta sử dụng ký hiệu \$.
Khi đó, thứ tự của các dịch vòng sau khi sắp xếp tương đương với thứ tự của các hậu tố sau khi sắp xếp, như minh họa dưới đây với xâu $dabbb$:

$$\begin{array}{lll}
1. & abbb\$d & abbb \\
4. & b\$dabb & b \\
3. & bb\$dab & bb \\
2. & bbb\$da & bbb \\
0. & dabbb\$ & dabbb
\end{array}$$

Vì chúng ta sẽ sắp xếp các dịch vòng, chúng ta sẽ xem xét các **xâu con xoay vòng (cyclic substring)**.
Chúng ta sử dụng ký hiệu $s[i \dots j]$ cho xâu con của $s$ ngay cả khi $i > j$.
Trong trường hợp này, ý của chúng ta thực chất là xâu $s[i \dots n-1] + s[0 \dots j]$.
Ngoài ra, chúng ta sẽ lấy tất cả các chỉ số theo modulo độ dài của $s$, và sẽ lược bớt phép toán modulo này để cho đơn giản.

Thuật toán của chúng ta sẽ thực hiện $\lceil \log n \rceil + 1$ bước lặp.
Ở bước lặp thứ $k$ ($k = 0 \dots \lceil \log n \rceil$), chúng ta sắp xếp $n$ xâu con xoay vòng của $s$ có độ dài $2^k$.
Sau bước lặp thứ $\lceil \log n \rceil$, các xâu con độ dài $2^{\lceil \log n \rceil} \ge n$ sẽ được sắp xếp, việc này tương đương với việc sắp xếp toàn bộ các dịch vòng.

Trong mỗi bước lặp của thuật toán, bên cạnh hoán vị $p[0 \dots n-1]$ (trong đó $p[i]$ là chỉ số của xâu con thứ $i$ (bắt đầu tại $i$ và có độ dài $2^k$) trong thứ tự đã sắp xếp), chúng ta cũng duy trì một mảng $c[0 \dots n-1]$, trong đó $c[i]$ tương ứng với **lớp tương đương (equivalence class)** mà xâu con đó thuộc về.
Bởi vì một số xâu con sẽ giống nhau, và thuật toán cần xử lý chúng như nhau.
Để thuận tiện, các lớp tương đương sẽ được đánh số từ không.
Đồng thời, các số lớp $c[i]$ được gán sao cho chúng bảo toàn thông tin về thứ tự từ điển:
nếu một xâu con nhỏ hơn xâu con khác, nó cũng phải có nhãn lớp tương đương nhỏ hơn.
Số lượng lớp tương đương sẽ được lưu trong biến $\text{classes}$.

Hãy xem một ví dụ.
Xét xâu $s = aaba$.
Các xâu con xoay vòng cùng các mảng $p[]$ và $c[]$ tương ứng qua mỗi bước lặp được thể hiện như sau:

$$\begin{array}{cccc}
0: & (a,~ a,~ b,~ a) & p = (0,~ 1,~ 3,~ 2) & c = (0,~ 0,~ 1,~ 0)\\
1: & (aa,~ ab,~ ba,~ aa) & p = (0,~ 3,~ 1,~ 2) & c = (0,~ 1,~ 2,~ 0)\\
2: & (aaba,~ abaa,~ baaa,~ aaab) & p = (3,~ 0,~ 1,~ 2) & c = (1,~ 2,~ 3,~ 0)\\
\end{array}$$

Lưu ý rằng các giá trị trong mảng $p[]$ có thể khác nhau tùy cách cài đặt.
Ví dụ ở bước lặp $0$, mảng p[] cũng có thể là $p = (3,~ 1,~ 0,~ 2)$ hoặc $p = (3,~ 0,~ 1,~ 2)$.
Tất cả các hoán vị này đều đưa các xâu con về thứ tự đã sắp xếp, nên chúng đều hợp lệ.
Tuy nhiên, mảng $c[]$ là duy nhất và cố định.

Bây giờ chúng ta sẽ đi sâu vào việc cài đặt thuật toán.
Chúng ta viết một hàm nhận vào xâu $s$ và trả về hoán vị của các dịch vòng đã được sắp xếp.

```{.cpp file=suffix_array_sort_cyclic1}
vector<int> sort_cyclic_shifts(string const& s) {
    int n = s.size();
    const int alphabet = 256;
```

Tại thời điểm bắt đầu (ở **bước lặp $0$**), chúng ta cần sắp xếp các xâu con xoay vòng độ dài $1$, tức là sắp xếp toàn bộ ký tự của xâu ban đầu và chia chúng vào các lớp tương đương (các ký tự giống nhau thuộc cùng một lớp).
Việc này có thể thực hiện đơn giản bằng **sắp xếp đếm (Counting Sort)**.
Với mỗi ký tự, chúng ta đếm số lần xuất hiện của nó trong xâu, rồi dùng thông tin này để tạo mảng $p[]$.
Sau đó, duyệt qua mảng $p[]$ để dựng mảng $c[]$ bằng cách so sánh các ký tự kề nhau.

```{.cpp file=suffix_array_sort_cyclic2}
    vector<int> p(n), c(n), cnt(max(alphabet, n), 0);
    for (int i = 0; i < n; i++)
        cnt[s[i]]++;
    for (int i = 1; i < alphabet; i++)
        cnt[i] += cnt[i-1];
    for (int i = 0; i < n; i++)
        p[--cnt[s[i]]] = i;
    c[p[0]] = 0;
    int classes = 1;
    for (int i = 1; i < n; i++) {
        if (s[p[i]] != s[p[i-1]])
            classes++;
        c[p[i]] = classes - 1;
    }
```

Bây giờ chúng ta thảo luận về bước chuyển tiếp giữa các vòng lặp.
Giả sử chúng ta đã thực hiện xong bước lặp $k-1$ và tính được các mảng $p[]$, $c[]$ cho bước đó.
Chúng ta muốn tính các giá trị cho bước lặp $k$ trong thời gian $O(n)$.
Vì chúng ta thực hiện bước lặp này $O(\log n)$ lần, toàn bộ thuật toán sẽ có độ phức tạp thời gian là $O(n \log n)$.

Để thực hiện điều này, nhận thấy rằng mỗi xâu con xoay vòng độ dài $2^k$ gồm hai xâu con xoay vòng độ dài $2^{k-1}$ ghép lại. Chúng ta có thể so sánh chúng với nhau trong $O(1)$ bằng cách sử dụng thông tin của bước trước đó — chính là các lớp tương đương trong mảng $c[]$.
Cụ thể, đối với hai xâu con độ dài $2^k$ bắt đầu tại vị trí $i$ và $j$, mọi thông tin cần thiết để so sánh chúng được chứa trong các cặp tương đương $(c[i],~ c[i + 2^{k-1}])$ và $(c[j],~ c[j + 2^{k-1}])$.

$$\dots
\overbrace{
\underbrace{s_i \dots s_{i+2^{k-1}-1}}_{\text{độ dài} = 2^{k-1},~ \text{lớp} = c[i]}
\quad
\underbrace{s_{i+2^{k-1}} \dots s_{i+2^k-1}}_{\text{độ dài} = 2^{k-1},~ \text{lớp} = c[i + 2^{k-1}]}
}^{\text{độ dài} = 2^k}
\dots
\overbrace{
\underbrace{s_j \dots s_{j+2^{k-1}-1}}_{\text{độ dài} = 2^{k-1},~ \text{lớp} = c[j]}
\quad
\underbrace{s_{j+2^{k-1}} \dots s_{j+2^k-1}}_{\text{độ dài} = 2^{k-1},~ \text{lớp} = c[j + 2^{k-1}]}
}^{\text{độ dài} = 2^k}
\dots
$$

Điều này cho chúng ta một giải pháp rất đơn giản:
**sắp xếp** các xâu con độ dài $2^k$ **theo các cặp số này**.
Từ đó thu được hoán vị $p[]$ mong muốn.
Tuy nhiên, một thuật toán sắp xếp thông thường sẽ chạy trong $O(n \log n)$, dẫn đến tổng độ phức tạp thuật toán dựng mảng hậu tố là $O(n \log^2 n)$, mức độ phức tạp chưa tối ưu.

Làm thế nào để sắp xếp các cặp số này một cách nhanh chóng?
Vì các phần tử của cặp số đều không vượt quá $n$, chúng ta có thể sử dụng sắp xếp đếm (Counting Sort) một lần nữa.
Tuy nhiên, việc sắp xếp các cặp số trực tiếp bằng sắp xếp đếm không phải là cách tối ưu nhất.
Để có hằng số ẩn tốt hơn, chúng ta sử dụng một kỹ thuật khác.

Chúng ta áp dụng nguyên lý của **sắp xếp cơ số (Radix Sort)**: để sắp xếp các cặp số, trước hết ta sắp xếp chúng theo phần tử thứ hai, sau đó sắp xếp theo phần tử thứ nhất (bằng một thuật toán sắp xếp ổn định - stable sort, tức là sắp xếp giữ nguyên thứ tự tương đối của các phần tử bằng nhau).
Nhận thấy rằng, phần tử thứ hai của các cặp đã được sắp xếp từ bước lặp trước đó.
Do đó, để sắp xếp các cặp theo phần tử thứ hai, chúng ta chỉ cần trừ đi $2^{k-1}$ từ các chỉ số trong mảng $p[]$ (ví dụ: nếu xâu con nhỏ nhất độ dài $2^{k-1}$ bắt đầu tại vị trí $i$, thì xâu con độ dài $2^k$ có nửa sau nhỏ nhất sẽ bắt đầu tại $i - 2^{k-1}$).

Như vậy, chỉ bằng các phép trừ đơn giản, chúng ta đã có thể sắp xếp các phần tử thứ hai của các cặp trong $p[]$.
Bây giờ chúng ta cần thực hiện một phép sắp xếp ổn định theo phần tử thứ nhất.
Như đã đề cập, việc này được thực hiện bằng sắp xếp đếm.

Bước còn lại là cập nhật các lớp tương đương $c[]$. Việc này tương tự như trước, chỉ cần duyệt qua hoán vị đã sắp xếp $p[]$ và so sánh các cặp lân cận.

Dưới đây là phần cài đặt còn lại của thuật toán.
Chúng ta sử dụng các mảng tạm thời $pn[]$ và $cn[]$ để lưu hoán vị theo phần tử thứ hai và nhãn lớp tương đương mới.

```{.cpp file=suffix_array_sort_cyclic3}
    vector<int> pn(n), cn(n);
    for (int h = 0; (1 << h) < n; ++h) {
        for (int i = 0; i < n; i++) {
            pn[i] = p[i] - (1 << h);
            if (pn[i] < 0)
                pn[i] += n;
        }
        fill(cnt.begin(), cnt.begin() + classes, 0);
        for (int i = 0; i < n; i++)
            cnt[c[pn[i]]]++;
        for (int i = 1; i < classes; i++)
            cnt[i] += cnt[i-1];
        for (int i = n-1; i >= 0; i--)
            p[--cnt[c[pn[i]]]] = pn[i];
        cn[p[0]] = 0;
        classes = 1;
        for (int i = 1; i < n; i++) {
            pair<int, int> cur = {c[p[i]], c[(p[i] + (1 << h)) % n]};
            pair<int, int> prev = {c[p[i-1]], c[(p[i-1] + (1 << h)) % n]};
            if (cur != prev)
                ++classes;
            cn[p[i]] = classes - 1;
        }
        c.swap(cn);
    }
    return p;
}
```

Thuật toán yêu cầu thời gian $O(n \log n)$ và bộ nhớ $O(n)$. Để cho đơn giản, chúng ta sử dụng bảng mã ASCII làm bảng chữ cái.

Nếu biết trước xâu chỉ chứa một tập hợp ký tự thu nhỏ (ví dụ chỉ gồm các chữ cái viết thường), mã nguồn có thể được tối ưu thêm, tuy nhiên mức độ tối ưu thường không đáng kể vì kích thước bảng chữ cái chỉ ảnh hưởng đến bước lặp đầu tiên. Tất cả các bước lặp sau đều phụ thuộc vào số lượng lớp tương đương, vốn nhanh chóng đạt tới $O(n)$ ngay cả khi xâu ban đầu chỉ được xây dựng trên bảng chữ cái kích thước $2$.

Cần lưu ý rằng thuật toán này chỉ sắp xếp các dịch vòng của xâu.
Như đã đề cập ở đầu phần này, chúng ta có thể tạo mảng hậu tố đã sắp xếp của xâu bằng cách thêm một ký tự nhỏ hơn tất cả các ký tự khác vào cuối xâu, rồi chạy thuật toán sắp xếp dịch vòng cho xâu mới này, ví dụ sắp xếp dịch vòng của $s + \$$.
Kết quả nhận được chính là mảng hậu tố của $s$ sau khi loại bỏ phần tử đầu tiên (có độ dài $|s|$).

```{.cpp file=suffix_array_construction}
vector<int> suffix_array_construction(string s) {
    s += "$";
    vector<int> sorted_shifts = sort_cyclic_shifts(s);
    sorted_shifts.erase(sorted_shifts.begin());
    return sorted_shifts;
}
```

## Ứng dụng

### Tìm dịch vòng nhỏ nhất

Thuật toán trên sắp xếp tất cả các dịch vòng (không cần thêm ký tự đặc biệt vào cuối xâu), do đó $p[0]$ chính là vị trí bắt đầu của dịch vòng nhỏ nhất theo thứ tự từ điển.

### Tìm kiếm xâu con trong một văn bản

Bài toán yêu cầu tìm kiếm một xâu $s$ bên trong một văn bản $t$ cho trước trực tuyến (online) — văn bản $t$ được biết trước, còn xâu truy vấn $s$ chỉ được đưa vào sau đó.
Chúng ta có thể dựng mảng hậu tố cho văn bản $t$ trong thời gian $O(|t| \log |t|)$.
Bây giờ chúng ta tìm xâu $s$ như sau:
mỗi lần xuất hiện của $s$ trong văn bản phải là tiền tố của một hậu tố nào đó của $t$.
Vì chúng ta đã sắp xếp các hậu tố theo thứ tự từ điển, chúng ta có thể thực hiện tìm kiếm nhị phân cho $s$ trên mảng hậu tố $p$.
Việc so sánh xâu con $s$ với hậu tố hiện tại trong mỗi bước tìm kiếm nhị phân tốn $O(|s|)$, do đó tổng độ phức tạp để tìm kiếm xâu con là $O(|s| \log |t|)$.
Ngoài ra, nếu xâu con xuất hiện nhiều lần trong $t$, tất cả các lần xuất hiện này sẽ nằm kề nhau trên mảng hậu tố $p$.
Vì vậy, số lượng lần xuất hiện có thể được tìm thấy bằng phép tìm kiếm nhị phân thứ hai, và tất cả các vị trí xuất hiện có thể được liệt kê một cách dễ dàng.

### So sánh hai xâu con của một xâu

Chúng ta muốn so sánh hai xâu con có cùng độ dài của một xâu $s$ cho trước trong thời gian $O(1)$, tức là kiểm tra xem xâu con thứ nhất có nhỏ hơn xâu con thứ hai theo thứ tự từ điển hay không.

Để làm việc này, chúng ta dựng mảng hậu tố trong thời gian $O(|s| \log |s|)$ và lưu lại tất cả các kết quả trung gian của mảng lớp tương đương $c[]$ qua mỗi bước lặp.

Sử dụng thông tin này, chúng ta có thể so sánh hai xâu con bất kỳ có độ dài là lũy thừa của 2 trong O(1):
chỉ cần so sánh trực tiếp các lớp tương đương của hai xâu con đó.
Bây giờ chúng ta tổng quát hóa phương pháp này cho các xâu con có độ dài bất kỳ.

Giả sử cần so sánh hai xâu con độ dài $l$ bắt đầu tại chỉ số $i$ và $j$.
Chúng ta tìm độ dài khối lớn nhất là lũy thừa của 2 nằm vừa vặn trong xâu con này: tức là số $k$ lớn nhất sao cho $2^k \le l$.
Khi đó việc so sánh hai xâu con độ dài $l$ có thể quy về việc so sánh hai khối chồng lên nhau độ dài $2^k$:
đầu tiên so sánh hai khối bắt đầu tại $i$ và $j$, và nếu chúng bằng nhau, ta tiếp tục so sánh hai khối kết thúc tại $i + l - 1$ và $j + l - 1$:

$$\dots
\overbrace{\underbrace{s_i \dots s_{i+l-2^k} \dots s_{i+2^k-1}}_{2^k} \dots s_{i+l-1}}^{\text{thứ nhất}}
\dots
\overbrace{\underbrace{s_j \dots s_{j+l-2^k} \dots s_{j+2^k-1}}_{2^k} \dots s_{j+l-1}}^{\text{thứ hai}}
\dots$$

$$\dots
\overbrace{s_i \dots \underbrace{s_{i+l-2^k} \dots s_{i+2^k-1} \dots s_{i+l-1}}_{2^k}}^{\text{thứ nhất}}
\dots
\overbrace{s_j \dots \underbrace{s_{j+l-2^k} \dots s_{j+2^k-1} \dots s_{j+l-1}}_{2^k}}^{\text{thứ hai}}
\dots$$

Dưới đây là cài đặt hàm so sánh.
Lưu ý rằng hàm giả định biến $k$ đã được tính toán từ trước.
Chúng ta có thể tính $k$ với $\lfloor \log l \rfloor$, nhưng sẽ hiệu quả hơn nếu tiền xử lý và lưu trước giá trị $k$ cho mọi độ dài $l$.
Xem thêm bài viết về [Bảng thưa (Sparse Table)](../data_structures/sparse-table.md), cấu trúc này sử dụng ý tưởng tương tự và tiền xử lý toàn bộ các giá trị $\log$.

```cpp
int compare(int i, int j, int l, int k) {
    pair<int, int> a = {c[k][i], c[k][(i+l-(1 << k))%n]};
    pair<int, int> b = {c[k][j], c[k][(j+l-(1 << k))%n]};
    return a == b ? 0 : a < b ? -1 : 1;
}
```

### Tiền tố chung dài nhất của hai xâu con sử dụng thêm bộ nhớ

Với một xâu $s$ cho trước, chúng ta muốn tính tiền tố chung dài nhất (**LCP - Longest Common Prefix**) của hai hậu tố bắt đầu tại vị trí $i$ và $j$.

Phương pháp mô tả ở phần này sử dụng thêm $O(|s| \log |s|)$ bộ nhớ phụ trợ.
Một phương pháp khác chỉ sử dụng lượng bộ nhớ tuyến tính sẽ được trình bày ở phần tiếp theo.

Chúng ta dựng mảng hậu tố trong thời gian $O(|s| \log |s|)$, và lưu lại các mảng lớp tương đương $c[]$ ở mỗi bước lặp.

Để tính LCP của hai hậu tố bắt đầu tại $i$ và $j$:
chúng ta có thể so sánh hai xâu con bất kỳ có độ dài là lũy thừa của 2 trong $O(1)$.
Dựa vào đó, chúng ta so sánh các xâu con theo các lũy thừa của 2 (từ lớn đến nhỏ). Nếu các xâu con có độ dài này trùng nhau, chúng ta cộng độ dài này vào kết quả LCP và tiếp tục kiểm tra phần xâu con còn lại ở bên phải phần trùng khớp (tức là dịch chuyển $i$ và $j$ sang phải một khoảng bằng lũy thừa của 2 hiện tại).

```cpp
int lcp(int i, int j) {
    int ans = 0;
    for (int k = log_n; k >= 0; k--) {
        if (c[k][i % n] == c[k][j % n]) {
            ans += 1 << k;
            i += 1 << k;
            j += 1 << k;
        }
    }
    return ans;
}
```

Ở đây `log_n` đại diện cho một hằng số bằng phần nguyên của logarit của $n$ cơ số $2$.

### Tiền tố chung dài nhất của hai xâu con không cần thêm bộ nhớ phụ trợ

Chúng ta giải quyết cùng bài toán như phần trước:
tính tiền tố chung dài nhất (**LCP**) của hai hậu tố bất kỳ của xâu $s$.

Khác với phương pháp trên, thuật toán này chỉ sử dụng $O(|s|)$ bộ nhớ.
Kết quả của quá trình tiền xử lý là một mảng phụ (đây là một nguồn thông tin rất quan trọng về cấu trúc của xâu ký tự, do đó nó cũng được dùng để giải quyết nhiều bài toán khác).
Các truy vấn LCP sau đó có thể được trả lời bằng các truy vấn RMQ (Range Minimum Query - truy vấn giá trị nhỏ nhất trên đoạn) trên mảng này, nhờ đó có thể đạt được thời gian truy vấn là thời gian logarit hoặc thậm chí là hằng số tùy thuộc vào cách cài đặt RMQ.

Cơ sở của thuật toán dựa trên ý tưởng sau:
chúng ta sẽ tính tiền tố chung dài nhất cho mỗi **cặp hậu tố kề nhau trong mảng hậu tố đã sắp xếp**.
Nói cách khác, chúng ta dựng mảng $\text{lcp}[0 \dots n-2]$, trong đó $\text{lcp}[i]$ bằng độ dài tiền tố chung dài nhất của hai hậu tố bắt đầu tại $p[i]$ và $p[i+1]$.
Mảng này cho phép trả lời LCP của hai hậu tố kề nhau bất kỳ.
Từ đó, câu trả lời cho hai hậu tố bất kỳ (không nhất thiết kề nhau) có thể suy ra từ mảng này.
Cụ thể, LCP của hai hậu tố $p[i]$ và $p[j]$ chính bằng giá trị nhỏ nhất trên đoạn $\min(lcp[i],~ lcp[i+1],~ \dots,~ lcp[j-1])$.

Như vậy, nếu có mảng $\text{lcp}$, bài toán được quy về [RMQ](../sequences/rmq.md), vốn có nhiều thuật toán giải quyết hiệu quả với các độ phức tạp khác nhau.

Do đó, nhiệm vụ chính là **xây dựng** mảng $\text{lcp}$ này.
Chúng ta sẽ sử dụng **thuật toán Kasai**, thuật toán cho phép tính mảng này trong thời gian $O(n)$.

Xét hai hậu tố kề nhau trong mảng hậu tố đã sắp xếp.
Giả sử vị trí bắt đầu của chúng lần lượt là $i$ và $j$, và độ dài tiền tố chung dài nhất $\text{lcp}$ của chúng bằng $k > 0$.
Nếu ta bỏ đi ký tự đầu tiên của cả hai hậu tố — tức là xét hai hậu tố tại chỉ số $i+1$ và $j+1$ — rõ ràng $\text{lcp}$ của hai hậu tố mới này sẽ là $k - 1$.
Tuy nhiên, chúng ta không thể điền ngay giá trị này vào mảng $\text{lcp}$ cho vị trí tương ứng, bởi vì hai hậu tố này có thể không nằm kề nhau trong mảng hậu tố đã sắp xếp.
Hậu tố $i+1$ chắc chắn sẽ nhỏ hơn hậu tố $j+1$, nhưng có thể có các hậu tố khác nằm xen giữa chúng.
Mặc dù vậy, vì LCP giữa hai hậu tố bất kỳ bằng giá trị nhỏ nhất của các đoạn LCP kề nhau giữa chúng, chúng ta biết chắc chắn rằng LCP giữa bất kỳ cặp hậu tố nào trong đoạn đó phải đạt tối thiểu là $k-1$, đặc biệt là LCP giữa hậu tố $i+1$ và hậu tố đứng ngay sau nó.
Và giá trị LCP thực tế hoàn toàn có thể lớn hơn.

Từ ý tưởng này, chúng ta cài đặt thuật toán như sau:
chúng ta duyệt qua các hậu tố theo thứ tự độ dài giảm dần của chúng (tức là duyệt theo chỉ số bắt đầu từ 0 đến n-1). Cách này giúp chúng ta tái sử dụng giá trị $k$ từ bước trước, vì việc chuyển từ hậu tố $i$ sang hậu tố $i+1$ tương đương với việc bỏ đi ký tự đầu tiên của hậu tố đó.
Chúng ta cần một mảng phụ $\text{rank}$ lưu vị trí của hậu tố trong mảng hậu tố đã được sắp xếp.

```{.cpp file=suffix_array_lcp_construction}
vector<int> lcp_construction(string const& s, vector<int> const& p) {
    int n = s.size();
    vector<int> rank(n, 0);
    for (int i = 0; i < n; i++)
        rank[p[i]] = i;

    int k = 0;
    vector<int> lcp(n-1, 0);
    for (int i = 0; i < n; i++) {
        if (rank[i] == n - 1) {
            k = 0;
            continue;
        }
        int j = p[rank[i] + 1];
        while (i + k < n && j + k < n && s[i+k] == s[j+k])
            k++;
        lcp[rank[i]] = k;
        if (k)
            k--;
    }
    return lcp;
}
```

Dễ thấy rằng, chúng ta giảm $k$ tối đa $O(n)$ lần (mỗi bước lặp giảm tối đa một lần, trừ trường hợp $\text{rank}[i] == n-1$ nơi chúng ta trực tiếp đặt lại về $0$). Vì LCP của hai xâu tối đa là $n-1$, chúng ta cũng chỉ tăng $k$ tối đa $O(n)$ lần.
Do đó thuật toán chạy trong thời gian $O(n)$.

### Số lượng xâu con phân biệt

Chúng ta tiền xử lý xâu $s$ bằng cách tính mảng hậu tố và mảng LCP.
Sử dụng các thông tin này, chúng ta có thể tính được tổng số lượng xâu con phân biệt của xâu.

Để làm được điều này, chúng ta tính xem có bao nhiêu xâu con **mới** bắt đầu tại vị trí $p[0]$, sau đó tại $p[1]$, v.v.
Nói cách khác, chúng ta xét các hậu tố theo thứ tự đã sắp xếp và xem các tiền tố nào của hậu tố hiện tại tạo ra các xâu con mới chưa từng xuất hiện.
Cách tiếp cận này đảm bảo không bỏ sót bất kỳ xâu con nào.

Vì các hậu tố đã được sắp xếp, rõ ràng hậu tố hiện tại $p[i]$ sẽ tạo ra các xâu con mới từ tất cả các tiền tố của nó, ngoại trừ các tiền tố trùng khớp với tiền tố của hậu tố $p[i-1]$ đứng trước.
Các tiền tố trùng khớp này chính là $\text{lcp}[i-1]$ tiền tố đầu tiên.
Vì độ dài của hậu tố hiện tại là $n - p[i]$, sẽ có $n - p[i] - \text{lcp}[i-1]$ tiền tố mới bắt đầu tại $p[i]$.
Lấy tổng trên tất cả các hậu tố, ta được đáp án cuối cùng:

$$\sum_{i=0}^{n-1} (n - p[i]) - \sum_{i=0}^{n-2} \text{lcp}[i] = \frac{n^2 + n}{2} - \sum_{i=0}^{n-2} \text{lcp}[i]$$

## Bài tập thực hành

* [Uva 760 - DNA Sequencing](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=701)
* [Uva 1223 - Editor](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3664)
* [Codechef - Tandem](https://www.codechef.com/problems/TANDEM)
* [Codechef - Substrings and Repetitions](https://www.codechef.com/problems/ANUSAR)
* [Codechef - Entangled Strings](https://www.codechef.com/problems/TANGLED)
* [Codeforces - Martian Strings](http://codeforces.com/problemset/problem/149/E)
* [Codeforces - Little Elephant and Strings](http://codeforces.com/problemset/problem/204/E)
* [SPOJ - Ada and Terramorphing](http://www.spoj.com/problems/ADAPHOTO/)
* [SPOJ - Ada and Substring](http://www.spoj.com/problems/ADASTRNG/)
* [UVA - 1227 - The longest constant gene](https://onlinejudge.org/external/127/12747.pdf)
* [SPOJ - Longest Common Substring](http://www.spoj.com/problems/LCS/en/)
* [UVA 11512 - GATTACA](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2507)
* [LA 7502 - Suffixes and Palindromes](https://vjudge.net/problem/UVALive-7502)
* [GYM - Por Costel and the Censorship Committee](http://codeforces.com/gym/100923/problem/D)
* [UVA 1254 - Top 10](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3695)
* [UVA 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
* [UVA 12206 - Stammering Aliens](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3358)
* [Codechef - Jarvis and LCP](https://www.codechef.com/problems/INSQ16F)
* [LA 3943 - Liking's Letter](https://vjudge.net/problem/UVALive-3943)
* [UVA 11107 - Life Forms](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2048)
* [UVA 12974 - Exquisite Strings](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4853)
* [UVA 10526 - Intellectual Property](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1467)
* [UVA 12338 - Anti-Rhyme Pairs](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3760)
* [UVA 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
* [SPOJ - Suffix Array](http://www.spoj.com/problems/SARRAY/)
* [LA 4513 - Stammering Aliens](https://vjudge.net/problem/UVALive-4513)
* [SPOJ - LCS2](http://www.spoj.com/problems/LCS2/)
* [Codeforces - Fake News (hard)](http://codeforces.com/contest/802/problem/I)
* [SPOJ - Longest Commong Substring](http://www.spoj.com/problems/LONGCS/)
* [SPOJ - Lexicographical Substring Search](http://www.spoj.com/problems/SUBLEX/)
* [Codeforces - Forbidden Indices](http://codeforces.com/contest/873/problem/F)
* [Codeforces - Tricky and Clever Password](http://codeforces.com/contest/30/problem/E)
* [LA 6856 - Circle of digits](https://vjudge.net/problem/UVALive-6856)
