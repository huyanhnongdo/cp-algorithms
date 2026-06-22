---
tags:
  - Translated
e_maxx_link: prefix_function
lang: vi
---

# Hàm tiền tố. Thuật toán Knuth-Morris-Pratt

## Định nghĩa hàm tiền tố

Cho một xâu $s$ có độ dài $n$.
**Hàm tiền tố (prefix function)** của xâu này được định nghĩa là một mảng $\pi$ có độ dài $n$, trong đó $\pi[i]$ là độ dài của tiền tố thực sự (proper prefix) dài nhất của xâu con $s[0 \dots i]$ đồng thời cũng là hậu tố của xâu con này.
Tiền tố thực sự của một xâu là một tiền tố không bằng chính xâu đó.
Theo định nghĩa, $\pi[0] = 0$.

Về mặt toán học, định nghĩa của hàm tiền tố có thể được viết như sau:

$$\pi[i] = \max_ {k = 0 \dots i} \{k : s[0 \dots k-1] = s[i-(k-1) \dots i] \}$$

Ví dụ, hàm tiền tố của xâu "abcabcd" là $[0, 0, 0, 1, 2, 3, 0]$, và hàm tiền tố của xâu "aabaaab" là $[0, 1, 0, 1, 2, 2, 3]$.

## Thuật toán ngây thơ

Một thuật toán tuân theo chính xác định nghĩa của hàm tiền tố có dạng như sau:

```{.cpp file=prefix_slow}
vector<int> prefix_function(string s) {
    int n = (int)s.length();
    vector<int> pi(n);
    for (int i = 0; i < n; i++)
        for (int k = 0; k <= i; k++)
            if (s.substr(0, k) == s.substr(i-k+1, k))
                pi[i] = k;
    return pi;
}
```

Dễ thấy độ phức tạp của thuật toán này là $O(n^3)$, một kết quả hoàn toàn có thể cải thiện được.

## Thuật toán hiệu quả

Thuật toán này được đề xuất bởi Knuth và Pratt, và độc lập bởi Morris vào năm 1977.
Nó được sử dụng làm hàm cốt lõi cho một thuật toán tìm kiếm xâu con.

### Tối ưu hóa thứ nhất

Nhận xét quan trọng đầu tiên là các giá trị của hàm tiền tố chỉ có thể tăng tối đa một đơn vị giữa các bước liên tiếp.

Thật vậy, ngược lại, nếu $\pi[i + 1] \gt \pi[i] + 1$, ta có thể lấy hậu tố kết thúc tại vị trí $i + 1$ có độ dài $\pi[i + 1]$ và loại bỏ ký tự cuối cùng của nó.
Khi đó ta thu được một hậu tố kết thúc tại vị trí $i$ có độ dài $\pi[i + 1] - 1$, lớn hơn $\pi[i]$, dẫn đến mâu thuẫn.

Hình minh họa dưới đây mô tả mâu thuẫn này.
Hậu tố thực sự dài nhất tại vị trí $i$ đồng thời là tiền tố có độ dài là $2$, và tại vị trí $i+1$ là $4$.
Do đó xâu $s_0 ~ s_1 ~ s_2 ~ s_3$ bằng xâu $s_{i-2} ~ s_{i-1} ~ s_i ~ s_{i+1}$, nghĩa là các xâu $s_0 ~ s_1 ~ s_2$ và $s_{i-2} ~ s_{i-1} ~ s_i$ cũng bằng nhau, do đó $\pi[i]$ phải bằng $3$.

$$\underbrace{\overbrace{s_0 ~ s_1}^{\pi[i] = 2} ~ s_2 ~ s_3}_{\pi[i+1] = 4} ~ \dots ~ \underbrace{s_{i-2} ~ \overbrace{s_{i-1} ~ s_{i}}^{\pi[i] = 2} ~ s_{i+1}}_{\pi[i+1] = 4}$$

Như vậy, khi chuyển sang vị trí tiếp theo, giá trị của hàm tiền tố chỉ có thể tăng thêm một, giữ nguyên, hoặc giảm đi một lượng nào đó.
Thực tế này cho phép chúng ta giảm độ phức tạp của thuật toán xuống $O(n^2)$, vì ở mỗi bước hàm tiền tố tăng tối đa một đơn vị.
Tổng cộng, hàm số có thể tăng tối đa $n$ bước, và do đó cũng chỉ có thể giảm tổng cộng $n$ bước.
Điều này có nghĩa là chúng ta chỉ cần thực hiện tổng cộng $O(n)$ phép so sánh xâu, đạt độ phức tạp $O(n^2)$.

### Tối ưu hóa thứ hai

Chúng ta muốn loại bỏ hoàn toàn các phép so sánh xâu.
Để làm được điều này, chúng ta cần tận dụng mọi thông tin đã được tính toán ở các bước trước đó.

Giả sử chúng ta đang tính giá trị của hàm tiền tố $\pi$ cho vị trí $i + 1$.
Nếu $s[i+1] = s[\pi[i]]$, ta có thể khẳng định chắc chắn rằng $\pi[i+1] = \pi[i] + 1$, vì chúng ta đã biết hậu tố tại vị trí $i$ có độ dài $\pi[i]$ bằng với tiền tố có độ dài $\pi[i]$.
Hình dưới đây minh họa cho trường hợp này:

$$\underbrace{\overbrace{s_0 ~ s_1 ~ s_2}^{\pi[i]} ~ \overbrace{s_3}^{s_3 = s_{i+1}}}_{\pi[i+1] = \pi[i] + 1} ~ \dots ~ \underbrace{\overbrace{s_{i-2} ~ s_{i-1} ~ s_{i}}^{\pi[i]} ~ \overbrace{s_{i+1}}^{s_3 = s_{i + 1}}}_{\pi[i+1] = \pi[i] + 1}$$

Nếu điều này không xảy ra, tức là $s[i+1] \neq s[\pi[i]]$, chúng ta cần phải thử với một xâu ngắn hơn.
Để tăng tốc, chúng ta muốn nhảy ngay lập tức đến độ dài lớn nhất $j \lt \pi[i]$ thỏa mãn tính chất tiền tố tại vị trí $i$, tức là $s[0 \dots j-1] = s[i-j+1 \dots i]$:

$$\overbrace{\underbrace{s_0 ~ s_1}_j ~ s_2 ~ s_3}^{\pi[i]} ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_j}^{\pi[i]} ~ s_{i+1}$$

Thực tế, nếu tìm được độ dài $j$ như vậy, chúng ta lại chỉ cần so sánh hai ký tự $s[i+1]$ và $s[j]$.
Nếu chúng bằng nhau, ta có thể gán $\pi[i+1] = j + 1$.
Ngược lại, chúng ta tiếp tục tìm giá trị lớn nhất nhỏ hơn $j$ thỏa mãn tính chất tiền tố, và cứ tiếp tục như thế.
Quá trình này có thể lặp lại cho đến khi $j = 0$.
Nếu khi đó $s[i+1] = s[0]$, ta gán $\pi[i+1] = 1$, ngược lại gán $\pi[i+1] = 0$.

Như vậy chúng ta đã có lược đồ tổng quát của thuật toán.
Câu hỏi duy nhất còn lại là làm thế nào để tìm các độ dài $j$ một cách hiệu quả.
Hãy xem lại:
với độ dài $j$ hiện tại tại vị trí $i$ thỏa mãn tính chất tiền tố, tức là $s[0 \dots j-1] = s[i-j+1 \dots i]$, chúng ta muốn tìm giá trị $k \lt j$ lớn nhất cũng thỏa mãn tính chất tiền tố.

$$\overbrace{\underbrace{s_0 ~ s_1}_k ~ s_2 ~ s_3}^j ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_k}^j ~s_{i+1}$$

Hình minh họa cho thấy giá trị này chính là $\pi[j-1]$ mà chúng ta đã tính toán từ trước.

### Thuật toán hoàn chỉnh

Cuối cùng, chúng ta có thể xây dựng một thuật toán không thực hiện bất kỳ phép so sánh xâu nào và chỉ thực hiện $O(n)$ thao tác.

Dưới đây là quy trình hoàn chỉnh:

- Chúng ta tính các giá trị tiền tố $\pi[i]$ trong một vòng lặp duyệt từ $i = 1$ đến $i = n-1$ ($\pi[0]$ được gán mặc định bằng $0$).
- Để tính giá trị $\pi[i]$ hiện tại, chúng ta đặt biến $j$ là độ dài của hậu tố tốt nhất cho vị trí $i-1$. Ban đầu, $j = \pi[i-1]$.
- Kiểm tra xem hậu tố có độ dài $j+1$ có phải là một tiền tố hay không bằng cách so sánh $s[j]$ và $s[i]$.
  Nếu chúng bằng nhau, ta gán $\pi[i] = j + 1$. Ngược lại, ta giảm $j$ xuống $\pi[j-1]$ và lặp lại bước này.
- Nếu đạt đến độ dài $j = 0$ và vẫn không khớp, ta gán $\pi[i] = 0$ và chuyển sang chỉ số tiếp theo $i + 1$.

### Cài đặt

Mã nguồn cài đặt cực kỳ ngắn gọn và rõ ràng:

```{.cpp file=prefix_fast}
vector<int> prefix_function(string s) {
    int n = (int)s.length();
    vector<int> pi(n);
    for (int i = 1; i < n; i++) {
        int j = pi[i-1];
        while (j > 0 && s[i] != s[j])
            j = pi[j-1];
        if (s[i] == s[j])
            j++;
        pi[i] = j;
    }
    return pi;
}
```

Đây là một thuật toán **trực tuyến (online)**, tức là nó xử lý dữ liệu ngay khi nhận được - ví dụ, bạn có thể đọc từng ký tự của xâu và xử lý ngay lập tức, tìm giá trị của hàm tiền tố cho mỗi ký tự tiếp theo.
Thuật toán vẫn yêu cầu lưu trữ bản thân xâu đó và các giá trị hàm tiền tố đã tính trước đó, nhưng nếu chúng ta biết trước giá trị cực đại $M$ mà hàm tiền tố có thể đạt được trên xâu, chúng ta chỉ cần lưu trữ $M+1$ ký tự đầu tiên của xâu và một số lượng tương đương các giá trị hàm tiền tố.

## Ứng dụng

### Tìm kiếm xâu con trong một xâu. Thuật toán Knuth-Morris-Pratt

Đây là ứng dụng cổ điển nhất của hàm tiền tố.

Cho một văn bản $t$ và một xâu $s$, chúng ta muốn tìm và hiển thị tất cả các vị trí xuất hiện của xâu $s$ trong văn bản $t$.

Để thuận tiện, ký hiệu $n$ là độ dài của xâu $s$ và $m$ là độ dài của văn bản $t$.

Chúng ta tạo ra một xâu mới $s + \# + t$, trong đó $\#$ là một ký tự phân tách (separator) không xuất hiện trong cả $s$ và $t$.
Tính hàm tiền tố cho xâu mới này.
Bây giờ, hãy suy nghĩ về ý nghĩa của các giá trị hàm tiền tố, ngoại trừ $n + 1$ phần tử đầu tiên (thuộc về xâu $s$ và ký tự phân tách).
Theo định nghĩa, giá trị $\pi[i]$ biểu thị độ dài lớn nhất của xâu con kết thúc tại vị trí $i$ trùng với tiền tố.
Nhưng trong trường hợp của chúng ta, đây chính là khối lớn nhất trùng với $s$ và kết thúc tại vị trí $i$.
Độ dài này không thể lớn hơn $n$ do có sự xuất hiện của ký tự phân tách.
Tuy nhiên, nếu đạt được đẳng thức $\pi[i] = n$, điều đó có nghĩa là xâu $s$ xuất hiện hoàn chỉnh tại vị trí này, tức là nó kết thúc tại vị trí $i$.
Chỉ cần lưu ý rằng các vị trí đang được đánh chỉ số trên xâu chung $s + \# + t$.

Do đó, nếu tại một vị trí $i$ nào đó ta có $\pi[i] = n$, thì tại vị trí $i - (n + 1) - n + 1 = i - 2n$ trong văn bản $t$, xâu $s$ xuất hiện.

Như đã đề cập trong phần mô tả tính toán hàm tiền tố, nếu biết trước các giá trị tiền tố không bao giờ vượt quá một giới hạn nhất định, chúng ta không cần lưu trữ toàn bộ xâu và toàn bộ hàm số, mà chỉ cần lưu phần đầu của nó.
Trong trường hợp này, điều đó có nghĩa là chúng ta chỉ cần lưu trữ xâu $s + \#$ và các giá trị hàm tiền tố tương ứng.
Chúng ta có thể đọc từng ký tự của văn bản $t$ và tính toán giá trị hiện tại của hàm tiền tố.

Như vậy, thuật toán Knuth-Morris-Pratt giải quyết bài toán trong thời gian $O(n + m)$ và sử dụng $O(n)$ bộ nhớ.

### Đếm số lần xuất hiện của mỗi tiền tố

Ở đây chúng ta thảo luận đồng thời hai bài toán.
Cho một xâu $s$ có độ dài $n$.
Trong biến thể thứ nhất, chúng ta muốn đếm số lần xuất hiện của mỗi tiền tố $s[0 \dots i]$ trong chính xâu đó.
Trong biến thể thứ hai, một xâu $t$ khác được cho trước và chúng ta muốn đếm số lần xuất hiện của mỗi tiền tố $s[0 \dots i]$ trong $t$.

Đầu tiên chúng ta giải bài toán thứ nhất.
Xét giá trị của hàm tiền tố $\pi[i]$ tại vị trí $i$.
Theo định nghĩa, điều này có nghĩa là tiền tố có độ dài $\pi[i]$ của xâu $s$ xuất hiện và kết thúc tại vị trí $i$, và không có tiền tố nào dài hơn thỏa mãn định nghĩa này.
Đồng thời, các tiền tố ngắn hơn cũng có thể kết thúc tại vị trí này.
Không khó để nhận thấy rằng chúng ta gặp lại câu hỏi đã trả lời khi tính toán chính hàm tiền tố:
Cho một tiền tố độ dài $j$ là hậu tố kết thúc tại vị trí $i$, tiền tố nhỏ hơn tiếp theo $\lt j$ cũng là hậu tố kết thúc tại vị trí $i$ là gì.
Do đó, tại vị trí $i$ kết thúc tiền tố có độ dài $\pi[i]$, tiền tố có độ dài $\pi[\pi[i] - 1]$, tiền tố $\pi[\pi[\pi[i] - 1] - 1]$, và cứ tiếp tục như vậy cho đến khi chỉ số trở thành 0.
Vì vậy, chúng ta có thể tính toán câu trả lời bằng cách sau:

```{.cpp file=prefix_count_each_prefix}
vector<int> ans(n + 1);
for (int i = 0; i < n; i++)
    ans[pi[i]]++;
for (int i = n-1; i > 0; i--)
    ans[pi[i-1]] += ans[i];
for (int i = 0; i <= n; i++)
    ans[i]++;
```

Ở đây, đối với mỗi giá trị của hàm tiền tố, đầu tiên chúng ta đếm số lần nó xuất hiện trong mảng $\pi$, và sau đó tính toán câu trả lời cuối cùng:
nếu biết tiền tố độ dài $i$ xuất hiện đúng $\text{ans}[i]$ lần, thì số lượng này phải được cộng vào số lần xuất hiện của hậu tố dài nhất của nó mà cũng là tiền tố.
Cuối cùng, chúng ta cần cộng thêm $1$ vào mỗi kết quả, vì chúng ta cũng cần đếm cả các tiền tố ban đầu.

Bây giờ hãy xem xét bài toán thứ hai.
Chúng ta áp dụng thủ thuật từ thuật toán Knuth-Morris-Pratt:
tạo xâu $s + \# + t$ và tính hàm tiền tố của nó.
Sự khác biệt duy nhất so với bài toán thứ nhất là chúng ta chỉ quan tâm đến các giá trị tiền tố liên quan đến xâu $t$, tức là các giá trị $\pi[i]$ với $i \ge n + 1$.
Với các giá trị này, chúng ta có thể thực hiện các phép tính hoàn toàn tương tự như trong bài toán thứ nhất.

### Số lượng xâu con khác nhau trong một xâu

Cho một xâu $s$ có độ dài $n$.
Chúng ta muốn tính số lượng xâu con khác nhau xuất hiện trong nó.

Chúng ta sẽ giải bài toán này một cách lặp đi lặp lại.
Cụ thể, giả sử đã biết số lượng xâu con khác nhau hiện tại, chúng ta sẽ học cách cập nhật số lượng này khi thêm một ký tự vào cuối xâu.

Gọi $k$ là số lượng xâu con khác nhau hiện tại trong $s$, và chúng ta thêm ký tự $c$ vào cuối $s$.
Rõ ràng là sẽ có một số xâu con mới kết thúc bằng $c$ xuất hiện.
Chúng ta muốn đếm các xâu con mới này (các xâu con chưa từng xuất hiện trước đó).

Chúng ta lấy xâu $t = s + c$ và đảo ngược nó.
Bây giờ, bài toán chuyển thành tính toán xem có bao nhiêu tiền tố của xâu đảo ngược không xuất hiện ở bất kỳ nơi nào khác.
Nếu chúng ta tính giá trị lớn nhất của hàm tiền tố $\pi_{\text{max}}$ của xâu đảo ngược $t$, thì tiền tố dài nhất xuất hiện trong $s$ sẽ có độ dài là $\pi_{\text{max}}$.
Rõ ràng, tất cả các tiền tố có độ dài nhỏ hơn cũng sẽ xuất hiện trong đó.

Do đó, số lượng xâu con mới xuất hiện khi thêm ký tự $c$ là $|s| + 1 - \pi_{\text{max}}$.

Như vậy, với mỗi ký tự được thêm vào, chúng ta có thể tính số lượng xâu con mới trong thời gian $O(n)$, dẫn đến tổng độ phức tạp thời gian là $O(n^2)$.

Cần lưu ý rằng chúng ta cũng có thể tính số lượng xâu con khác nhau bằng cách thêm các ký tự vào đầu xâu, hoặc xóa các ký tự ở đầu hoặc cuối xâu.

### Nén một xâu

Cho một xâu $s$ có độ dài $n$.
Chúng ta muốn tìm biểu diễn "nén" ngắn nhất của xâu này, tức là tìm một xâu $t$ có độ dài nhỏ nhất sao cho $s$ có thể được biểu diễn dưới dạng ghép của một hoặc nhiều bản sao của xâu $t$.

Rõ ràng chúng ta chỉ cần tìm độ dài của $t$. Biết được độ dài này, câu trả lời của bài toán sẽ là tiền tố của $s$ có độ dài tương ứng.

Hãy tính hàm tiền tố cho $s$.
Sử dụng giá trị cuối cùng của nó để định nghĩa $k = n - \pi[n - 1]$.
Chúng ta sẽ chứng minh rằng nếu $k$ chia hết cho $n$, thì $k$ sẽ là câu trả lời, ngược lại không có phép nén hiệu quả nào và câu trả lời là $n$.

Giả sử $n$ chia hết cho $k$.
Khi đó xâu có thể được chia thành các khối độ dài $k$.
Theo định nghĩa của hàm tiền tố, tiền tố có độ dài $n - k$ sẽ bằng hậu tố của nó.
Nhưng điều này có nghĩa là khối cuối cùng bằng khối liền trước nó.
Và khối liền trước nó phải bằng khối liền trước nó nữa.
Và cứ tiếp tục như vậy.
Kết quả là tất cả các khối đều bằng nhau, do đó chúng ta có thể nén xâu $s$ về độ dài $k$.

Tất nhiên chúng ta vẫn cần chứng minh rằng đây thực sự là kết quả tối ưu.
Thật vậy, nếu có một phép nén nhỏ hơn $k$, thì hàm tiền tố ở cuối xâu sẽ lớn hơn $n - k$.
Do đó $k$ thực sự là đáp án tối ưu.

Bây giờ giả sử $n$ không chia hết cho $k$.
Chúng ta sẽ chỉ ra rằng điều này dẫn đến độ dài của đáp án là $n$.
Chúng ta chứng minh bằng phản chứng.
Giả định tồn tại một đáp án, và phép nén có độ dài $p$ ($p$ chia hết cho $n$).
Khi đó giá trị cuối cùng của hàm tiền tố phải lớn hơn $n - p$, tức là hậu tố sẽ bao phủ một phần của khối đầu tiên.
Bây giờ hãy xem xét khối thứ hai của xâu.
Vì tiền tố bằng hậu tố, và cả tiền tố lẫn hậu tố đều bao phủ khối này và khoảng dịch của chúng đối với nhau $k$ không chia hết cho độ dài khối $p$ (ngược lại $k$ sẽ chia hết cho $n$), nên tất cả các ký tự của khối phải giống hệt nhau.
Nhưng khi đó xâu chỉ gồm một ký tự lặp đi lặp lại nhiều lần, do đó chúng ta có thể nén nó về xâu kích thước $1$, dẫn đến $k = 1$, và $k$ chia hết cho $n$.
Mâu thuẫn.

$$\overbrace{s_0 ~ s_1 ~ s_2 ~ s_3}^p ~ \overbrace{s_4 ~ s_5 ~ s_6 ~ s_7}^p$$

$$s_0 ~ s_1 ~ s_2 ~ \underbrace{\overbrace{s_3 ~ s_4 ~ s_5 ~ s_6}^p ~ s_7}_{\pi[7] = 5}$$

$$s_4 = s_3, ~ s_5 = s_4, ~ s_6 = s_5, ~ s_7 = s_6 ~ \Rightarrow ~ s_0 = s_1 = s_2 = s_3$$

### Xây dựng automat theo hàm tiền tố

Hãy quay lại việc ghép hai xâu qua ký tự phân tách, tức là đối với hai xâu $s$ và $t$, chúng ta tính hàm tiền tố cho xâu $s + \# + t$.
Rõ ràng, vì $\#$ là ký tự phân tách, giá trị của hàm tiền tố sẽ không bao giờ vượt quá $|s|$.
Do đó, chỉ cần lưu trữ xâu $s + \#$ và các giá trị hàm tiền tố cho nó là đủ, và chúng ta có thể tính toán hàm tiền tố cho mọi ký tự tiếp theo trực tiếp:

$$\underbrace{s_0 ~ s_1 ~ \dots ~ s_{n-1} ~ \#}_{\text{cần lưu trữ}} ~ \underbrace{t_0 ~ t_1 ~ \dots ~ t_{m-1}}_{\text{không cần lưu trữ}}$$

Thật vậy, trong tình huống như vậy, biết ký tự tiếp theo $c \in t$ và giá trị của hàm tiền tố ở vị trí trước đó là đủ thông tin để tính giá trị tiếp theo của hàm tiền tố, mà không cần sử dụng bất kỳ ký tự nào trước đó của xâu $t$ hay các giá trị hàm tiền tố tương ứng của chúng.

Nói cách khác, chúng ta có thể xây dựng một **automat (automat / finite state machine)**: trạng thái trong đó là giá trị hiện tại của hàm tiền tố, và việc chuyển từ trạng thái này sang trạng thái khác sẽ được thực hiện thông qua ký tự tiếp theo.

Như vậy, ngay cả khi không có xâu $t$, chúng ta vẫn có thể xây dựng một bảng chuyển trạng thái $(\text{old}_\pi, c) \rightarrow \text{new}_\pi$ bằng cách sử dụng chính thuật toán tính toán bảng chuyển đổi:

```{.cpp file=prefix_automaton_slow}
void compute_automaton(string s, vector<vector<int>>& aut) {
    s += '#';
    int n = s.size();
    vector<int> pi = prefix_function(s);
    aut.assign(n, vector<int>(26));
    for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
            int j = i;
            while (j > 0 && 'a' + c != s[j])
                j = pi[j-1];
            if ('a' + c == s[j])
                j++;
            aut[i][c] = j;
        }
    }
}
```

Tuy nhiên, ở dạng này, thuật toán chạy trong thời gian $O(n^2 \cdot 26)$ đối với bảng chữ cái gồm các chữ cái viết thường.
Lưu ý rằng chúng ta có thể áp dụng quy hoạch động (dynamic programming) và sử dụng các phần đã được tính toán của bảng chuyển trạng thái.
Bất cứ khi nào đi từ giá trị $j$ đến giá trị $\pi[j-1]$, thực chất chúng ta ngụ ý rằng bước chuyển $(j, c)$ dẫn đến cùng một trạng thái như bước chuyển $(\pi[j-1], c)$, và kết quả này đã được tính toán chính xác từ trước.

```{.cpp file=prefix_automaton_fast}
void compute_automaton(string s, vector<vector<int>>& aut) {
    s += '#';
    int n = s.size();
    vector<int> pi = prefix_function(s);
    aut.assign(n, vector<int>(26));
    for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
            if (i > 0 && 'a' + c != s[i])
                aut[i][c] = aut[pi[i-1]][c];
            else
                aut[i][c] = i + ('a' + c == s[i]);
        }
    }
}
```

Kết quả là chúng ta xây dựng được automat trong thời gian $O(26 n)$.

Khi nào thì một automat như vậy hữu ích?
Đầu tiên, hãy nhớ rằng chúng ta sử dụng hàm tiền tố cho xâu $s + \# + t$ và các giá trị của nó hầu như chỉ cho một mục đích duy nhất: tìm tất cả các lần xuất hiện của xâu $s$ trong xâu $t$.

Do đó, lợi ích rõ ràng nhất của automat này là **tăng tốc việc tính toán hàm tiền tố** cho xâu $s + \# + t$.
Bằng cách xây dựng automat cho xâu $s + \#$, chúng ta không còn cần phải lưu trữ xâu $s$ hay các giá trị hàm tiền tố tương ứng nữa.
Tất cả các chuyển trạng thái đều đã được tính toán sẵn trong bảng.

Nhưng còn có một ứng dụng thứ hai, ít hiển nhiên hơn.
Chúng ta có thể sử dụng automat khi xâu $t$ là một **xâu khổng lồ được xây dựng theo một số quy tắc**.
Ví dụ như các xâu Gray, hoặc một xâu được tạo thành bằng cách kết hợp đệ quy của một số xâu ngắn từ đầu vào.

Để hoàn thiện, chúng ta sẽ giải quyết bài toán sau:
cho số $k \le 10^5$ và một xâu $s$ có độ dài $\le 10^5$.
Chúng ta phải tính số lần xuất hiện của $s$ trong xâu Gray thứ $k$.
Nhớ lại rằng các xâu Gray được định nghĩa theo cách sau:

$$\begin{align}
g_1 &= \text{"a"}\\
g_2 &= \text{"aba"}\\
g_3 &= \text{"abacaba"}\\
g_4 &= \text{"abacabadabacaba"}
\end{align}$$

Trong những trường hợp như vậy, ngay cả việc xây dựng xâu $t$ cũng là bất khả thi vì độ dài thiên văn của nó.
Xâu Gray thứ $k$ có độ dài $2^k-1$ ký tự.
Tuy nhiên, chúng ta có thể tính toán giá trị của hàm tiền tố tại cuối xâu một cách hiệu quả, bằng cách chỉ cần biết giá trị của hàm tiền tố ở đầu xâu.

Bên cạnh bản thân automat, chúng ta cũng tính toán các giá trị $G[i][j]$ - giá trị của automat sau khi xử lý xâu $g_i$ bắt đầu với trạng thái $j$.
Và chúng ta cũng tính toán thêm các giá trị $K[i][j]$ - số lần xuất hiện của $s$ trong $g_i$, trong quá trình xử lý xâu $g_i$ bắt đầu từ trạng thái $j$.
Thực chất, $K[i][j]$ là số lần hàm tiền tố nhận giá trị $|s|$ trong quá trình thực hiện các phép toán.
Đáp án của bài toán khi đó sẽ là $K[k][0]$.

Làm thế nào để tính các giá trị này?
Đầu tiên, các giá trị cơ sở là $G[0][j] = j$ và $K[0][j] = 0$.
Và tất cả các giá trị tiếp theo có thể được tính toán từ các giá trị trước đó và sử dụng automat.
Để tính toán giá trị cho một số $i$ nào đó, hãy nhớ rằng xâu $g_i$ gồm có $g_{i-1}$, ký tự thứ $i$ của bảng chữ cái, và $g_{i-1}$.
Do đó automat sẽ chuyển sang trạng thái:

$$\text{mid} = \text{aut}[G[i-1][j]][i]$$

$$G[i][j] = G[i-1][\text{mid}]$$

Các giá trị của $K[i][j]$ cũng có thể được tính toán dễ dàng:

$$K[i][j] = K[i-1][j] + (\text{mid} == |s|) + K[i-1][\text{mid}]$$

Như vậy chúng ta có thể giải bài toán cho các xâu Gray, và tương tự cho một lượng lớn các bài toán tương tự khác.
Ví dụ, phương pháp hoàn toàn tương tự cũng giải quyết bài toán sau:
chúng ta được cho một xâu $s$ và một số mẫu $t_i$, mỗi mẫu được xác định như sau:
nó là một xâu gồm các ký tự thông thường, và có thể có một số phép chèn đệ quy của các xâu trước đó dưới dạng $t_k^{\text{cnt}}$, có nghĩa là tại vị trí này chúng ta phải chèn xâu $t_k$ đúng $\text{cnt}$ lần.
Một ví dụ về các mẫu như vậy:

$$\begin{align}
t_1 &= \text{"abdeca"}\\
t_2 &= \text{"abc"} + t_1^{30} + \text{"abd"}\\
t_3 &= t_2^{50} + t_1^{100}\\
t_4 &= t_2^{10} + t_3^{100}
\end{align}$$

Các phép thế đệ quy làm cho xâu bùng nổ kích thước, sao cho độ dài của chúng có thể đạt tới bậc $100^{100}$.

Chúng ta phải tìm số lần xâu $s$ xuất hiện trong mỗi xâu.

Bài toán có thể được giải quyết bằng cách tương tự: xây dựng automat của hàm tiền tố, và sau đó tính toán các bước chuyển trạng thái cho mỗi mẫu bằng cách sử dụng các kết quả trước đó.

## Bài tập thực hành

* [UVA # 455 "Periodic Strings"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
* [UVA # 11022 "String Factoring"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
* [UVA # 11452 "Dancing the Cheeky-Cheeky"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2447)
* [UVA 12604 - Caesar Cipher](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4282)
* [UVA 12467 - Secret Word](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3911)
* [UVA 11019 - Matrix Matcher](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1960)
* [SPOJ - Pattern Find](http://www.spoj.com/problems/NAJPF/)
* [SPOJ - A Needle in the Haystack](https://www.spoj.com/problems/NHAY/)
* [Codeforces - Anthem of Berland](http://codeforces.com/contest/808/problem/G)
* [Codeforces - MUH and Cube Walls](http://codeforces.com/problemset/problem/471/D)
* [Codeforces - Prefixes and Suffixes](https://codeforces.com/contest/432/problem/D)
