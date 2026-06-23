---
tags:
  - Translated
e_maxx_link: string_tandems
lang: vi
---
# Tìm kiếm các đoạn lặp (Repetitions)

Cho một xâu `s` có độ dài `n`.

Một **đoạn lặp** (repetition) là hai lần xuất hiện liên tiếp của một xâu.
Nói cách khác, một đoạn lặp có thể được mô tả bởi cặp chỉ số $i < j$ sao cho xâu con $s[i \dots j]$ bao gồm hai xâu giống hệt nhau viết liền nhau.

Thách thức ở đây là **tìm tất cả các đoạn lặp** trong một xâu $s$ cho trước.
Hoặc một bài toán đơn giản hơn: tìm **bất kỳ** đoạn lặp nào hoặc tìm đoạn lặp **dài nhất**.

Thuật toán được mô tả dưới đây được Main và Lorentz công bố vào năm 1982.

## Ví dụ

Xét các đoạn lặp trong ví dụ xâu sau:

$$acababaee$$

Xâu này chứa ba đoạn lặp sau:

- $s[2 \dots 5] = abab$
- $s[3 \dots 6] = baba$
- $s[7 \dots 8] = ee$

Một ví dụ khác:

$$abaaba$$

Ở đây chỉ có hai đoạn lặp:

- $s[0 \dots 5] = abaaba$
- $s[2 \dots 3] = aa$

## Số lượng các đoạn lặp

Nói chung, có thể có tối đa $O(n^2)$ đoạn lặp trong một xâu có độ dài $n$.
Một ví dụ hiển nhiên là xâu bao gồm $n$ lần cùng một ký tự, trong trường hợp này bất kỳ xâu con nào có độ dài chẵn đều là một đoạn lặp.
Nhìn chung, bất kỳ xâu tuần hoàn nào có chu kỳ ngắn đều sẽ chứa rất nhiều đoạn lặp.

Mặt khác, thực tế này không ngăn cản việc tính toán số lượng các đoạn lặp trong thời gian $O(n \log n)$, vì thuật toán có thể cung cấp các đoạn lặp dưới dạng nén, trong các nhóm gồm nhiều phần cùng một lúc.

Thậm chí còn có khái niệm mô tả các nhóm xâu con tuần hoàn bằng các bộ tứ (tuple).
Người ta đã chứng minh rằng số lượng các nhóm như vậy tối đa là tuyến tính so với độ dài xâu.

Ngoài ra, dưới đây là một số kết quả thú vị khác liên quan đến số lượng các đoạn lặp:

  - Số lượng các đoạn lặp nguyên thủy (những đoạn lặp mà các nửa của nó không phải là đoạn lặp) tối đa là $O(n \log n)$.
  - Nếu chúng ta mã hóa các đoạn lặp bằng các bộ ba số (được gọi là bộ ba Crochemore) $(i,~ p,~ r)$ (trong đó $i$ là vị trí bắt đầu, $p$ là độ dài của xâu lặp lại, và $r$ là số lần lặp lại), thì tất cả các đoạn lặp có thể được mô tả bằng $O(n \log n)$ bộ ba như vậy.
  - Các xâu Fibonacci, được định nghĩa là 
    
    \[\begin{align}
    t_0 &= a, \\\\
    t_1 &= b, \\\\
    t_i &= t_{i-1} + t_{i-2},
    \end{align}\]
    
    là các xâu "tuần hoàn mạnh".
    Số lượng các đoạn lặp trong xâu Fibonacci $f_i$, ngay cả khi đã nén với bộ ba Crochemore, là $O(f_n \log f_n)$.
    Số lượng các đoạn lặp nguyên thủy cũng là $O(f_n \log f_n)$.

## Thuật toán Main-Lorentz

Ý tưởng đằng sau thuật toán Main-Lorentz là **chia để trị (Divide and Conquer)**.

Nó chia xâu ban đầu thành hai nửa và tính toán số lượng các đoạn lặp nằm hoàn toàn trong mỗi nửa bằng hai lần gọi đệ quy.
Sau đó là phần khó khăn.
Thuật toán tìm tất cả các đoạn lặp bắt đầu ở nửa thứ nhất và kết thúc ở nửa thứ hai (chúng ta gọi là **các đoạn lặp bắc cầu** - crossing repetitions).
Đây là phần cốt yếu của thuật toán Main-Lorentz, và chúng ta sẽ thảo luận chi tiết về nó ở đây.

Độ phức tạp của các thuật toán chia để trị đã được nghiên cứu kỹ lưỡng.
[Định lý thạc sĩ (Master Theorem)](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)) nói rằng chúng ta sẽ thu được thuật toán $O(n \log n)$, nếu chúng ta có thể tính toán các đoạn lặp bắc cầu trong thời gian $O(n)$.

### Tìm kiếm các đoạn lặp bắc cầu

Chúng ta muốn tìm tất cả các đoạn lặp bắt đầu ở nửa đầu của xâu, gọi là $u$, và kết thúc ở nửa sau, gọi là $v$:

$$s = u + v$$

Độ dài của chúng xấp xỉ bằng độ dài của $s$ chia cho hai.

Xét một đoạn lặp bất kỳ và nhìn vào ký tự ở giữa (chính xác hơn là ký tự đầu tiên của nửa thứ hai của đoạn lặp).
Nghĩa là, nếu đoạn lặp là một xâu con $s[i \dots j]$, thì ký tự ở giữa là $(i + j + 1) / 2$.

Chúng ta gọi một đoạn lặp là **trái** hoặc **phải** tùy thuộc vào việc ký tự này nằm trong xâu nào - trong xâu $u$ hay trong xâu $v$.
Nói cách khác, một đoạn lặp được gọi là trái nếu phần lớn nó nằm trong $u$, ngược lại chúng ta gọi nó là phải.

Bây giờ chúng ta sẽ thảo luận cách tìm **tất cả các đoạn lặp trái**.
Việc tìm tất cả các đoạn lặp phải có thể được thực hiện theo cách tương tự.

Hãy ký hiệu độ dài của đoạn lặp trái là $2l$ (tức là mỗi nửa của đoạn lặp có độ dài $l$).
Xét ký tự đầu tiên của đoạn lặp rơi vào xâu $v$ (nó nằm ở vị trí $|u|$ trong xâu $s$).
Nó trùng với ký tự $l$ vị trí trước đó, hãy ký hiệu vị trí này là $cntr$.

Chúng ta sẽ cố định vị trí này $cntr$, và **tìm tất cả các đoạn lặp tại vị trí này** $cntr$.

Ví dụ:

$$c ~ \underset{cntr}{a} ~ c ~ | ~ a ~ d ~ a$$

Các đường kẻ dọc chia hai nửa.
Ở đây chúng ta cố định vị trí $cntr = 1$, và tại vị trí này chúng ta tìm thấy đoạn lặp $caca$.

Rõ ràng là nếu chúng ta cố định vị trí $cntr$, chúng ta đồng thời cố định độ dài của các đoạn lặp có thể có: $l = |u| - cntr$.
Khi biết cách tìm các đoạn lặp này, chúng ta sẽ lặp qua tất cả các giá trị có thể cho $cntr$ từ $0$ đến $|u|-1$, và tìm tất cả các đoạn lặp trái bắc cầu có độ dài $l = |u|,~ |u|-1,~ \dots, 1$.

### Tiêu chuẩn cho các đoạn lặp trái bắc cầu

Bây giờ, làm thế nào chúng ta có thể tìm tất cả các đoạn lặp như vậy cho một $cntr$ cố định?
Hãy nhớ rằng vẫn có thể có nhiều đoạn lặp như vậy.

Hãy nhìn lại một hình ảnh trực quan, lần này cho đoạn lặp $abcabc$:

$$\overbrace{a}^{l_1} ~ \overbrace{\underset{cntr}{b} ~ c}^{l_2} ~ \overbrace{a}^{l_1} ~ | ~ \overbrace{b ~ c}^{l_2}$$

Ở đây chúng ta ký hiệu độ dài của hai mảnh của đoạn lặp là $l_1$ và $l_2$:
$l_1$ là độ dài của đoạn lặp tính đến vị trí $cntr-1$, và $l_2$ là độ dài của đoạn lặp từ $cntr$ đến cuối nửa của đoạn lặp.
Chúng ta có $2l = l_1 + l_2 + l_1 + l_2$ là tổng độ dài của đoạn lặp.

Hãy tạo ra các điều kiện **cần và đủ** cho một đoạn lặp như vậy tại vị trí $cntr$ với độ dài $2l = 2(l_1 + l_2) = 2(|u| - cntr)$:

- Cho $k_1$ là số lớn nhất sao cho $k_1$ ký tự đầu tiên trước vị trí $cntr$ trùng khớp với $k_1$ ký tự cuối cùng trong xâu $u$:
  
$$
u[cntr - k_1 \dots cntr - 1] = u[|u| - k_1 \dots |u| - 1]
$$
  
- Cho $k_2$ là số lớn nhất sao cho $k_2$ ký tự bắt đầu tại vị trí $cntr$ trùng khớp với $k_2$ ký tự đầu tiên trong xâu $v$:

$$  
  u[cntr \dots cntr + k_2 - 1] = v[0 \dots k_2 - 1]
$$
  
- Khi đó, chúng ta có một đoạn lặp chính xác cho bất kỳ cặp $(l_1,~ l_2)$ nào với

$$
  \begin{align}
  l_1 &\le k_1, \\\\
  l_2 &\le k_2. \\\\
  \end{align}
$$

Tóm lại:

- Chúng ta cố định một vị trí cụ thể $cntr$.
- Tất cả các đoạn lặp mà chúng ta tìm thấy bây giờ có độ dài $2l = 2(|u| - cntr)$.
  Có thể có nhiều đoạn lặp như vậy, chúng phụ thuộc vào độ dài $l_1$ và $l_2 = l - l_1$.
- Chúng ta tìm $k_1$ và $k_2$ như mô tả ở trên.
- Sau đó, tất cả các đoạn lặp phù hợp là những đoạn lặp mà độ dài của các mảnh $l_1$ và $l_2$ thỏa mãn các điều kiện:

$$
  \begin{align}
  l_1 + l_2 &= l = |u| - cntr \\\\
  l_1 &\le k_1, \\\\
  l_2 &\le k_2. \\\\
  \end{align}
$$

Do đó, phần duy nhất còn lại là cách chúng ta có thể tính toán các giá trị $k_1$ và $k_2$ một cách nhanh chóng cho mỗi vị trí $cntr$.
May mắn thay, chúng ta có thể tính chúng trong $O(1)$ bằng cách sử dụng [Hàm Z (Z-function)](../string/z-function.md):

- Để tìm giá trị $k_1$ cho mỗi vị trí bằng cách tính hàm Z cho xâu $\overline{u}$ (tức là xâu đảo ngược $u$).
  Khi đó giá trị $k_1$ cho một $cntr$ cụ thể sẽ bằng giá trị tương ứng của mảng hàm Z.
- Để tính trước tất cả các giá trị $k_2$, chúng ta tính hàm Z cho xâu $v + \# + u$ (tức là xâu $u$ nối với ký tự phân tách $\#$ và xâu $v$).
  Một lần nữa, chúng ta chỉ cần tra cứu giá trị tương ứng trong hàm Z để lấy giá trị $k_2$.

Vậy là đủ để tìm tất cả các đoạn lặp trái bắc cầu.

### Các đoạn lặp phải bắc cầu

Để tính toán các đoạn lặp phải bắc cầu, chúng ta thực hiện tương tự:
chúng ta xác định tâm $cntr$ là ký tự tương ứng với ký tự cuối cùng trong xâu $u$.

Khi đó độ dài $k_1$ sẽ được xác định là số ký tự lớn nhất trước vị trí $cntr$ (bao gồm cả vị trí đó) trùng khớp với các ký tự cuối của xâu $u$.
Và độ dài $k_2$ sẽ được xác định là số ký tự lớn nhất bắt đầu tại $cntr + 1$ trùng khớp với các ký tự của xâu $v$.

Như vậy, chúng ta có thể tìm các giá trị $k_1$ và $k_2$ bằng cách tính hàm Z cho các xâu $\overline{u} + \# + \overline{v}$ và $v$.

Sau đó, chúng ta có thể tìm các đoạn lặp bằng cách nhìn vào tất cả các vị trí $cntr$, và sử dụng tiêu chuẩn tương tự như đối với các đoạn lặp trái bắc cầu.

### Cài đặt

Việc cài đặt thuật toán Main-Lorentz tìm tất cả các đoạn lặp dưới dạng các bộ tứ đặc biệt $(cntr,~ l,~ k_1,~ k_2)$ trong thời gian $O(n \log n)$.
Nếu bạn chỉ muốn tìm số lượng các đoạn lặp trong một xâu, hoặc chỉ muốn tìm đoạn lặp dài nhất, thông tin này là đủ và thời gian chạy vẫn sẽ là $O(n \log n)$.

Lưu ý rằng nếu bạn muốn mở rộng các bộ tứ này để lấy vị trí bắt đầu và kết thúc của mỗi đoạn lặp, thì thời gian chạy sẽ là $O(n^2)$ (hãy nhớ rằng có thể có $O(n^2)$ đoạn lặp).
Trong cài đặt này, chúng ta sẽ thực hiện việc đó và lưu trữ tất cả các đoạn lặp được tìm thấy vào một vector chứa các cặp chỉ số bắt đầu và kết thúc.

```{.cpp file=main_lorentz}
vector<int> z_function(string const& s) {
    int n = s.size();
    vector<int> z(n);
    for (int i = 1, l = 0, r = 0; i < n; i++) {
        if (i <= r)
            z[i] = min(r-i+1, z[i-l]);
        while (i + z[i] < n && s[z[i]] == s[i+z[i]])
            z[i]++;
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}

int get_z(vector<int> const& z, int i) {
    if (0 <= i && i < (int)z.size())
        return z[i];
    else
        return 0;
}

vector<pair<int, int>> repetitions;

void convert_to_repetitions(int shift, bool left, int cntr, int l, int k1, int k2) {
    for (int l1 = max(1, l - k2); l1 <= min(l, k1); l1++) {
        if (left && l1 == l) break;
        int l2 = l - l1;
        int pos = shift + (left ? cntr - l1 : cntr - l - l1 + 1);
        repetitions.emplace_back(pos, pos + 2*l - 1);
    }
}

void find_repetitions(string s, int shift = 0) {
    int n = s.size();
    if (n == 1)
        return;

    int nu = n / 2;
    int nv = n - nu;
    string u = s.substr(0, nu);
    string v = s.substr(nu);
    string ru(u.rbegin(), u.rend());
    string rv(v.rbegin(), v.rend());

    find_repetitions(u, shift);
    find_repetitions(v, shift + nu);

    vector<int> z1 = z_function(ru);
    vector<int> z2 = z_function(v + '#' + u);
    vector<int> z3 = z_function(ru + '#' + rv);
    vector<int> z4 = z_function(v);

    for (int cntr = 0; cntr < n; cntr++) {
        int l, k1, k2;
        if (cntr < nu) {
            l = nu - cntr;
            k1 = get_z(z1, nu - cntr);
            k2 = get_z(z2, nv + 1 + cntr);
        } else {
            l = cntr - nu + 1;
            k1 = get_z(z3, nu + 1 + nv - 1 - (cntr - nu));
            k2 = get_z(z4, (cntr - nu) + 1);
        }
        if (k1 + k2 >= l)
            convert_to_repetitions(shift, cntr < nu, cntr, l, k1, k2);
    }
}
```