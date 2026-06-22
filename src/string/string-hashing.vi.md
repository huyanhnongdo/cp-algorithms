---
tags:
  - Translated
e_maxx_link: string_hashes
lang: vi
---

# Băm chuỗi (String Hashing)

Các thuật toán băm (hashing) cực kỳ hữu ích trong việc giải quyết nhiều bài toán tin học.

Chúng ta muốn giải quyết bài toán so sánh các chuỗi ký tự một cách hiệu quả.
Cách tiếp cận ngây thơ (brute force) là so sánh từng ký tự của hai chuỗi, có độ phức tạp thời gian là $O(\min(n_1, n_2))$ với $n_1$ và $n_2$ là độ dài của hai chuỗi đó.
Chúng ta muốn cải tiến điều này.
Ý tưởng cốt lõi của băm chuỗi (string hashing) là: chúng ta ánh xạ mỗi chuỗi ký tự thành một số nguyên và so sánh các số nguyên này thay vì so sánh trực tiếp các chuỗi.
Điều này cho phép giảm thời gian thực thi của phép so sánh hai chuỗi xuống còn $O(1)$.

Để thực hiện phép biến đổi này, chúng ta cần một **hàm băm (hash function)**.
Mục tiêu của nó là chuyển một chuỗi ký tự thành một số nguyên, gọi là **mã băm (hash)** của chuỗi đó.
Điều kiện tiên quyết phải được thỏa mãn: nếu hai chuỗi $s$ và $t$ bằng nhau ($s = t$), thì mã băm của chúng cũng phải bằng nhau ($\text{hash}(s) = \text{hash}(t)$).
Nếu không, chúng ta sẽ không thể dùng mã băm để so sánh các chuỗi.

Lưu ý rằng chiều ngược lại không nhất thiết phải đúng.
Nếu hai mã băm bằng nhau ($\text{hash}(s) = \text{hash}(t)$), thì các chuỗi không bắt buộc phải giống nhau.
Ví dụ, một hàm băm hợp lệ (nhưng vô dụng) là luôn trả về $\text{hash}(s) = 0$ cho mọi chuỗi $s$.
Sở dĩ chiều ngược lại không cần đúng là vì số lượng chuỗi ký tự khả dĩ là vô cùng lớn (tăng theo hàm mũ).
Nếu ta muốn hàm băm phân biệt được tất cả các chuỗi chỉ gồm ký tự thường tiếng Anh có độ dài nhỏ hơn 15, thì mã băm đã vượt quá giới hạn biểu diễn của số nguyên 64-bit (ví dụ: `unsigned long long`) vì số lượng chuỗi là quá lớn.
Và hiển nhiên chúng ta cũng không muốn so sánh các số nguyên có độ dài lớn tùy ý vì độ phức tạp của nó cũng sẽ là $O(n)$.

Do đó, thông thường chúng ta muốn hàm băm ánh xạ các chuỗi thành các số nguyên nằm trong một khoảng cố định $[0, m)$. Khi đó, việc so sánh hai chuỗi quy về việc so sánh hai số nguyên có độ dài cố định.
Và hiển nhiên, ta muốn xác suất xảy ra $\text{hash}(s) \neq \text{hash}(t)$ là rất cao khi $s \neq t$.

Đây là điểm quan trọng bạn cần ghi nhớ:
Việc sử dụng phương pháp băm không thể đảm bảo tính đúng đắn một cách tuyệt đối (100% deterministic), vì hai chuỗi hoàn toàn khác nhau vẫn có thể có cùng mã băm (hiện tượng này gọi là **va chạm mã băm - hash collision**).
Tuy nhiên, trong phần lớn các bài toán, ta có thể bỏ qua rủi ro này vì xác suất va chạm của hai chuỗi khác nhau là vô cùng nhỏ.
Chúng ta cũng sẽ thảo luận một số kỹ thuật trong bài viết này để giữ cho xác suất va chạm ở mức tối thiểu.

## Công thức tính mã băm của một chuỗi

Một cách định nghĩa hàm băm chuỗi $s$ có độ dài $n$ tốt và được sử dụng rộng rãi là:

$$\begin{align}
\text{hash}(s) &= s[0] + s[1] \cdot p + s[2] \cdot p^2 + ... + s[n-1] \cdot p^{n-1} \mod m \\
&= \sum_{i=0}^{n-1} s[i] \cdot p^i \mod m,
\end{align}$$

trong đó $p$ và $m$ là các số nguyên dương được lựa chọn từ trước.
Hàm này được gọi là **hàm băm đa thức cuộn (polynomial rolling hash function)**.

Ta nên chọn $p$ là một số nguyên tố xấp xỉ bằng số lượng ký tự trong bảng chữ cái đầu vào.
Ví dụ, nếu đầu vào chỉ gồm các chữ cái thường tiếng Anh, ta nên chọn $p = 31$.
Nếu đầu vào có thể gồm cả chữ hoa lẫn chữ thường, ta nên chọn $p = 53$.
Mã nguồn minh họa trong bài viết này sẽ sử dụng $p = 31$.

Rõ ràng $m$ phải là một số lớn, vì xác suất va chạm của hai chuỗi ngẫu nhiên là khoảng $\approx \frac{1}{m}$.
Đôi khi người ta chọn $m = 2^{64}$, vì khi đó hiện tượng tràn số của kiểu số nguyên 64-bit không dấu hoạt động giống hệt phép toán modulo.
Tuy nhiên, có một kỹ thuật cho phép tạo ra các chuỗi gây va chạm mã băm một cách chủ đích (hoạt động độc lập với việc chọn $p$).
Vì vậy, trên thực tế không khuyến nghị chọn $m = 2^{64}$.
Lựa chọn tốt cho $m$ là một số nguyên tố lớn.
Mã nguồn trong bài viết này sử dụng $m = 10^9+9$.
Đây là một số lớn nhưng vẫn đủ nhỏ để chúng ta có thể thực hiện phép nhân hai giá trị sử dụng kiểu số nguyên 64-bit mà không lo bị tràn số.

Dưới đây là một ví dụ tính mã băm của chuỗi $s$ chỉ gồm các chữ cái viết thường.
Chúng ta chuyển mỗi ký tự của $s$ thành một số nguyên, theo quy tắc: $a \rightarrow 1$, $b \rightarrow 2$, $\dots$, $z \rightarrow 26$.
Việc chuyển $a \rightarrow 0$ là không tốt, vì khi đó mã băm của các chuỗi $a$, $aa$, $aaa$, $\dots$ đều bằng $0$.

```{.cpp file=hashing_function}
long long compute_hash(string const& s) {
    const int p = 31;
    const int m = 1e9 + 9;
    long long hash_value = 0;
    long long p_pow = 1;
    for (char c : s) {
        hash_value = (hash_value + (c - 'a' + 1) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    }
    return hash_value;
}
```

Việc tính toán trước các lũy thừa của $p$ (precompute) có thể giúp tăng hiệu năng đáng kể.

## Các bài toán ví dụ

### Tìm các chuỗi trùng lặp trong một mảng chuỗi

Bài toán: Cho danh sách gồm $n$ chuỗi ký tự $s_i$, mỗi chuỗi có độ dài không quá $m$, hãy tìm tất cả các chuỗi bị trùng lặp và chia chúng thành các nhóm.

Nếu sử dụng thuật toán sắp xếp chuỗi thông thường, chúng ta có độ phức tạp thời gian là $O(n m \log n)$ vì việc sắp xếp cần $O(n \log n)$ phép so sánh và mỗi phép so sánh hai chuỗi mất thời gian $O(m)$.
Tuy nhiên, nếu sử dụng mã băm, ta có thể giảm thời gian so sánh xuống còn $O(1)$, mang lại một thuật toán chạy trong thời gian $O(n m + n \log n)$.

Chúng ta tính mã băm cho mỗi chuỗi, sắp xếp các mã băm kèm theo chỉ số ban đầu, rồi nhóm các chỉ số có cùng mã băm lại với nhau.

```{.cpp file=hashing_group_identical_strings}
vector<vector<int>> group_identical_strings(vector<string> const& s) {
    int n = s.size();
    vector<pair<long long, int>> hashes(n);
    for (int i = 0; i < n; i++)
        hashes[i] = {compute_hash(s[i]), i};

    sort(hashes.begin(), hashes.end());

    vector<vector<int>> groups;
    for (int i = 0; i < n; i++) {
        if (i == 0 || hashes[i].first != hashes[i-1].first)
            groups.emplace_back();
        groups.back().push_back(hashes[i].second);
    }
    return groups;
}
```

### Tính nhanh mã băm của các chuỗi con của một chuỗi cho trước

Bài toán: Cho chuỗi $s$ và hai chỉ số $i$ và $j$, hãy tìm mã băm của chuỗi con $s[i \dots j]$.

Theo định nghĩa, ta có:

$$\text{hash}(s[i \dots j]) = \sum_{k = i}^j s[k] \cdot p^{k-i} \mod m$$

Nhân cả hai vế với $p^i$:

$$\begin{align}
\text{hash}(s[i \dots j]) \cdot p^i &= \sum_{k = i}^j s[k] \cdot p^k \mod m \\
&= \text{hash}(s[0 \dots j]) - \text{hash}(s[0 \dots i-1]) \mod m
\end{align}$$

Vì vậy, bằng cách biết trước mã băm của tất cả tiền tố của chuỗi $s$, chúng ta có thể tính được mã băm của bất kỳ chuỗi con nào trực tiếp bằng công thức này.
Khó khăn duy nhất là ta phải thực hiện phép chia $\text{hash}(s[0 \dots j]) - \text{hash}(s[0 \dots i-1])$ cho $p^i$.
Do đó, chúng ta cần tìm [nghịch đảo nhân mô-đun](../algebra/module-inverse.md) của $p^i$ rồi thực hiện phép nhân với nghịch đảo này.
Ta có thể tính toán trước nghịch đảo của mọi giá trị $p^i$, giúp tính mã băm của bất kỳ chuỗi con nào của $s$ trong thời gian $O(1)$.

Tuy nhiên, có một cách đơn giản hơn.
Trong hầu hết các trường hợp, thay vì tính chính xác mã băm của chuỗi con, ta chỉ cần tính mã băm nhân với một lũy thừa nào đó của $p$.
Giả sử ta có hai mã băm của hai chuỗi con, một mã băm được nhân với $p^i$ và mã băm kia được nhân với $p^j$.
Nếu $i < j$, ta nhân mã băm thứ nhất với $p^{j-i}$, ngược lại ta nhân mã băm thứ hai với $p^{i-j}$.
Bằng cách này, ta thu được cả hai mã băm đều được nhân với cùng một lũy thừa của $p$ (là giá trị lớn nhất của $i$ và $j$) và giờ đây ta có thể so sánh chúng dễ dàng mà không cần thực hiện phép chia nào.

## Ứng dụng của băm chuỗi

Dưới đây là một số ứng dụng điển hình của băm chuỗi:

* [Thuật toán Rabin-Karp](rabin-karp.md) so khớp mẫu trong xâu trong thời gian $O(n)$.
* Tính số lượng chuỗi con phân biệt của một chuỗi trong thời gian $O(n^2)$ (xem phần dưới).
* Tính số lượng chuỗi con đối xứng (palindromic substrings) trong một chuỗi.

### Xác định số lượng chuỗi con phân biệt trong một chuỗi

Bài toán: Cho chuỗi $s$ độ dài $n$ chỉ gồm các chữ cái viết thường tiếng Anh, hãy tìm số lượng chuỗi con phân biệt trong chuỗi này.

Để giải quyết bài toán này, ta duyệt qua tất cả các độ dài chuỗi con $l = 1 \dots n$.
Với mỗi độ dài $l$, ta dựng một mảng chứa mã băm của tất cả các chuỗi con độ dài $l$ đã được nhân với cùng một lũy thừa của $p$.
Số lượng phần tử phân biệt trong mảng này chính là số lượng chuỗi con phân biệt có độ dài $l$.
Số lượng này sẽ được cộng dồn vào kết quả cuối cùng.

Để thuận tiện, ta gọi $h[i]$ là mã băm của tiền tố gồm $i$ ký tự, và định nghĩa $h[0] = 0$.

```{.cpp file=hashing_count_unique_substrings}
int count_unique_substrings(string const& s) {
    int n = s.size();
    
    const int p = 31;
    const int m = 1e9 + 9;
    vector<long long> p_pow(n);
    p_pow[0] = 1;
    for (int i = 1; i < n; i++)
        p_pow[i] = (p_pow[i-1] * p) % m;

    vector<long long> h(n + 1, 0);
    for (int i = 0; i < n; i++)
        h[i+1] = (h[i] + (s[i] - 'a' + 1) * p_pow[i]) % m;

    int cnt = 0;
    for (int l = 1; l <= n; l++) {
        unordered_set<long long> hs;
        for (int i = 0; i <= n - l; i++) {
            long long cur_h = (h[i + l] + m - h[i]) % m;
            cur_h = (cur_h * p_pow[n-i-1]) % m;
            hs.insert(cur_h);
        }
        cnt += hs.size();
    }
    return cnt;
}
```

Lưu ý rằng $O(n^2)$ không phải là độ phức tạp tốt nhất cho bài toán này.
Một giải pháp với độ phức tạp $O(n \log n)$ được mô tả cụ thể trong bài viết về [Mảng hậu tố (Suffix Array)](suffix-array.md), và thậm chí ta có thể tính toán trong thời gian $O(n)$ sử dụng [Cây hậu tố (Suffix Tree)](./suffix-tree-ukkonen.md) hoặc [Automat hậu tố (Suffix Automaton)](./suffix-automaton.md).

## Cải thiện xác suất không xảy ra va chạm

Thông thường, hàm băm đa thức nêu trên đã đủ tốt và không có va chạm nào xảy ra trong quá trình chấm điểm.
Hãy nhớ rằng xác suất xảy ra va chạm chỉ là khoảng $\approx \frac{1}{m}$.
Với $m = 10^9 + 9$, xác suất này là khoảng $\approx 10^{-9}$ (rất thấp).
Nhưng lưu ý rằng đó là khi ta chỉ thực hiện duy nhất một phép so sánh.
Điều gì xảy ra nếu ta so sánh một chuỗi $s$ với $10^6$ chuỗi khác nhau?
Xác suất xảy ra ít nhất một va chạm lúc này tăng lên thành $\approx 10^{-3}$.
Và nếu chúng ta muốn so sánh $10^6$ chuỗi khác nhau với nhau (ví dụ: đếm xem có bao nhiêu chuỗi phân biệt), thì xác suất xảy ra ít nhất một va chạm gần như bằng $\approx 1$.
Khi đó, chương trình gần như chắc chắn sẽ gặp lỗi va chạm mã băm và cho ra kết quả sai.

Có một mẹo cực kỳ đơn giản để tăng độ chính xác:
Chúng ta tính toán hai mã băm khác nhau cho mỗi chuỗi (bằng cách chọn hai giá trị $p$ khác nhau, và/hoặc hai giá trị $m$ khác nhau) và so sánh cặp mã băm này thay vì chỉ một mã băm duy nhất.
Nếu chọn $m \approx 10^9$ cho mỗi hàm băm thì điều này tương đương với việc sử dụng một hàm băm duy nhất có $m \approx 10^{18}$.
Khi so sánh $10^6$ chuỗi với nhau, xác suất xảy ra ít nhất một va chạm lúc này giảm xuống chỉ còn $\approx 10^{-6}$.

## Bài tập thực hành
* [Good Substrings - Codeforces](https://codeforces.com/contest/271/problem/D)
* [A Needle in the Haystack - SPOJ](http://www.spoj.com/problems/NHAY/)
* [String Hashing - Kattis](https://open.kattis.com/problems/hashing)
* [Double Profiles - Codeforces](http://codeforces.com/problemset/problem/154/C)
* [Password - Codeforces](http://codeforces.com/problemset/problem/126/B)
* [SUB_PROB - SPOJ](http://www.spoj.com/problems/SUB_PROB/)
* [INSQ15_A](https://www.codechef.com/problems/INSQ15_A)
* [SPOJ - Ada and Spring Cleaning](http://www.spoj.com/problems/ADACLEAN/)
* [GYM - Text Editor](http://codeforces.com/gym/101466/problem/E)
* [12012 - Detection of Extraterrestrial](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3163)
* [Codeforces - Games on a CD](http://codeforces.com/contest/727/problem/E)
* [UVA 11855 - Buzzwords](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2955)
* [Codeforces - Santa Claus and a Palindrome](http://codeforces.com/contest/752/problem/D)
* [Codeforces - String Compression](http://codeforces.com/contest/825/problem/F)
* [Codeforces - Palindromic Characteristics](http://codeforces.com/contest/835/problem/D)
* [SPOJ - Test](http://www.spoj.com/problems/CF25E/)
* [Codeforces - Palindrome Degree](http://codeforces.com/contest/7/problem/D)
* [Codeforces - Deletion of Repeats](http://codeforces.com/contest/19/problem/C)
* [HackerRank - Gift Boxes](https://www.hackerrank.com/contests/womens-codesprint-5/challenges/gift-boxes)
