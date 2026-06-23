---
tags:
  - Translated
e_maxx_link: duval_algorithm
lang: vi
---
# Phân tích Lyndon (Lyndon factorization)

## Phân tích Lyndon

Trước hết, hãy định nghĩa khái niệm về phân tích Lyndon.

Một xâu được gọi là **đơn giản** (hay từ Lyndon), nếu nó thực sự **nhỏ hơn** bất kỳ **hậu tố** không tầm thường nào của chính nó.
Ví dụ về các xâu đơn giản là: $a$, $b$, $ab$, $aab$, $abb$, $ababb$, $abcd$.
Có thể chứng minh rằng một xâu là đơn giản khi và chỉ khi nó thực sự **nhỏ hơn** tất cả các **dịch chuyển vòng quanh** không tầm thường của nó.

Tiếp theo, giả sử có một xâu $s$ cho trước.
**Phân tích Lyndon** của xâu $s$ là một cách phân tích $s = w_1 w_2 \dots w_k$, trong đó tất cả các xâu $w_i$ đều là các xâu đơn giản, và chúng được sắp xếp theo thứ tự không tăng $w_1 \ge w_2 \ge \dots \ge w_k$.

Có thể chứng minh rằng với bất kỳ xâu nào, cách phân tích như vậy luôn tồn tại và là duy nhất.

## Thuật toán Duval

Thuật toán Duval xây dựng phân tích Lyndon trong thời gian $O(n)$ với bộ nhớ bổ sung là $O(1)$.

Trước hết, hãy giới thiệu một khái niệm khác:
một xâu $t$ được gọi là **tiền đơn giản** (pre-simple), nếu nó có dạng $t = w w \dots w \overline{w}$, trong đó $w$ là một xâu đơn giản và $\overline{w}$ là một tiền tố của $w$ (có thể rỗng).
Một xâu đơn giản cũng được coi là tiền đơn giản.

Thuật toán Duval là một thuật toán tham lam (Greedy).
Tại bất kỳ thời điểm nào trong quá trình thực thi, xâu $s$ sẽ được chia thành ba phần $s = s_1 s_2 s_3$, trong đó phân tích Lyndon cho $s_1$ đã được tìm thấy và cố định, xâu $s_2$ là tiền đơn giản (và ta đã biết độ dài của xâu đơn giản bên trong nó), và $s_3$ là phần chưa được xử lý.
Trong mỗi lần lặp, thuật toán Duval lấy ký tự đầu tiên của xâu $s_3$ và cố gắng thêm nó vào xâu $s_2$.
Nếu $s_2$ không còn là tiền đơn giản nữa, thì phân tích Lyndon cho một phần của $s_2$ đã được xác định, và phần này được chuyển sang $s_1$.

Hãy mô tả chi tiết thuật toán hơn.
Con trỏ $i$ sẽ luôn chỉ vào đầu của xâu $s_2$.
Vòng lặp ngoài sẽ được thực thi chừng nào $i < n$.
Bên trong vòng lặp, chúng ta sử dụng hai con trỏ bổ sung: $j$ chỉ vào phần bắt đầu của $s_3$, và $k$ chỉ vào ký tự hiện tại mà chúng ta đang so sánh.
Chúng ta muốn thêm ký tự $s[j]$ vào xâu $s_2$, đòi hỏi phải so sánh với ký tự $s[k]$.
Có ba trường hợp xảy ra:

- $s[j] = s[k]$: Nếu trường hợp này xảy ra, việc thêm ký tự $s[j]$ vào $s_2$ không làm mất tính tiền đơn giản của nó. Vì vậy, chúng ta chỉ cần tăng các con trỏ $j$ và $k$.
- $s[j] > s[k]$: Ở đây, xâu $s_2 + s[j]$ trở thành xâu đơn giản. Chúng ta có thể tăng $j$ và đặt lại $k$ về đầu của $s_2$, để ký tự tiếp theo có thể được so sánh với phần đầu của từ đơn giản.
- $s[j] < s[k]$: Xâu $s_2 + s[j]$ không còn là tiền đơn giản nữa. Do đó, chúng ta sẽ tách xâu tiền đơn giản $s_2$ thành các xâu đơn giản và phần dư (có thể rỗng). Xâu đơn giản sẽ có độ dài $j - k$. Trong lần lặp tiếp theo, chúng ta bắt đầu lại với phần còn lại $s_2$.

### Cài đặt

Dưới đây là cài đặt của thuật toán Duval, trả về phân tích Lyndon mong muốn cho xâu $s$ cho trước.

```{.cpp file=duval_algorithm}
vector<string> duval(string const& s) {
    int n = s.size();
    int i = 0;
    vector<string> factorization;
    while (i < n) {
        int j = i + 1, k = i;
        while (j < n && s[k] <= s[j]) {
            if (s[k] < s[j])
                k = i;
            else
                k++;
            j++;
        }
        while (i <= k) {
            factorization.push_back(s.substr(i, j - k));
            i += j - k;
        }
    }
    return factorization;
}
```

### Độ phức tạp

Hãy ước tính thời gian chạy của thuật toán này.

**Vòng lặp while ngoài** không vượt quá $n$ lần lặp, vì sau mỗi lần lặp $i$ đều tăng lên. Ngoài ra, vòng lặp while thứ hai bên trong chạy trong $O(n)$, vì nó chỉ đơn giản là xuất ra phân tích cuối cùng.

Vì vậy, chúng ta chỉ quan tâm đến **vòng lặp while thứ nhất bên trong**. Nó thực hiện bao nhiêu lần lặp trong trường hợp xấu nhất? Dễ thấy rằng các từ đơn giản mà chúng ta xác định được trong mỗi lần lặp của vòng ngoài đều dài hơn phần dư mà chúng ta đã so sánh thêm. Do đó, tổng các phần dư sẽ nhỏ hơn $n$, nghĩa là chúng ta chỉ thực hiện tối đa $O(n)$ lần lặp cho vòng while thứ nhất. Trên thực tế, tổng số lần so sánh ký tự sẽ không vượt quá $4n - 3$.

## Tìm dịch chuyển vòng quanh nhỏ nhất

Giả sử có một xâu $s$.
Chúng ta xây dựng phân tích Lyndon cho xâu $s + s$ (trong thời gian $O(n)$).
Chúng ta sẽ tìm kiếm một xâu đơn giản trong phân tích này mà bắt đầu tại một vị trí nhỏ hơn $n$ (tức là nó bắt đầu trong lần xuất hiện thứ nhất của $s$) và kết thúc ở một vị trí lớn hơn hoặc bằng $n$ (tức là trong lần xuất hiện thứ hai của $s$).
Người ta khẳng định rằng vị trí bắt đầu của xâu đơn giản này sẽ là điểm bắt đầu của dịch chuyển vòng quanh nhỏ nhất cần tìm. Điều này có thể dễ dàng kiểm chứng bằng định nghĩa của phân tích Lyndon.

Điểm bắt đầu của khối đơn giản có thể được tìm thấy dễ dàng - chỉ cần ghi nhớ con trỏ $i$ tại đầu mỗi lần lặp của vòng lặp ngoài, nó biểu thị điểm bắt đầu của xâu tiền đơn giản hiện tại.

Như vậy, ta có cài đặt sau:

```{.cpp file=smallest_cyclic_string}
string min_cyclic_string(string s) {
    s += s;
    int n = s.size();
    int i = 0, ans = 0;
    while (i < n / 2) {
        ans = i;
        int j = i + 1, k = i;
        while (j < n && s[k] <= s[j]) {
            if (s[k] < s[j])
                k = i;
            else
                k++;
            j++;
        }
        while (i <= k)
            i += j - k;
    }
    return s.substr(ans, n / 2);
}
```

## Các bài toán

- [UVA #719 - Glass Beads](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=660)