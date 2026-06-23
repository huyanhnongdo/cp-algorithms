---
title: Manacher's Algorithm - Finding all sub-palindromes in O(N)
tags:
  - Translated
e_maxx_link: palindromes_count
lang: vi
---
# Thuật toán Manacher - Tìm tất cả các xâu con đối xứng trong $O(N)$

## Phát biểu bài toán

Cho xâu $s$ có độ dài $n$. Hãy tìm tất cả các cặp $(i, j)$ sao cho xâu con $s[i\dots j]$ là một xâu đối xứng (palindrome). Xâu $t$ là một xâu đối xứng khi $t = t_{rev}$ (trong đó $t_{rev}$ là xâu đảo ngược của $t$).

## Phát biểu chi tiết hơn

Trong trường hợp xấu nhất, một xâu có thể có tới $O(n^2)$ xâu con đối xứng, và thoạt nhìn thì có vẻ như không có thuật toán tuyến tính nào cho bài toán này.

Tuy nhiên, thông tin về các xâu đối xứng có thể được lưu trữ một cách **gọn gàng**: tại mỗi vị trí $i$, chúng ta sẽ tìm số lượng xâu đối xứng không rỗng có tâm tại vị trí đó.

Các xâu đối xứng có chung một tâm tạo thành một chuỗi liên tiếp, nghĩa là nếu ta có một xâu đối xứng độ dài $l$ với tâm tại $i$, thì ta cũng có các xâu đối xứng độ dài $l-2$, $l-4$, v.v., cũng có tâm tại $i$. Do đó, chúng ta sẽ thu thập thông tin về tất cả các xâu con đối xứng theo cách này.

Các xâu đối xứng có độ dài lẻ và chẵn được tính riêng biệt lần lượt là $d_{odd}[i]$ và $d_{even}[i]$. Đối với các xâu đối xứng độ dài chẵn, chúng ta giả định tâm của chúng nằm tại vị trí $i$ nếu hai ký tự trung tâm là $s[i]$ và $s[i-1]$.

Ví dụ, xâu $s = abababc$ có ba xâu đối xứng độ dài lẻ với tâm tại vị trí $s[3] = b$, cụ thể là $d_{odd}[3] = 3$:

$$a\ \overbrace{b\ a\ \underbrace{b}_{s_3}\ a\ b}^{d_{odd}[3]=3} c$$

Và xâu $s = cbaabd$ có hai xâu đối xứng độ dài chẵn với tâm tại vị trí $s[3] = a$, cụ thể là $d_{even}[3] = 2$:

$$c\ \overbrace{b\ a\ \underbrace{a}_{s_3}\ b}^{d_{even}[3]=2} d$$

Một sự thật đáng ngạc nhiên là tồn tại một thuật toán khá đơn giản để tính các "mảng đối xứng" $d_{odd}[]$ và $d_{even}[]$ trong thời gian tuyến tính. Thuật toán này được mô tả trong bài viết dưới đây.

## Lời giải

Nhìn chung, bài toán này có nhiều cách giải: bằng [Băm xâu (String Hashing)](string-hashing.md) có thể giải trong $O(n\cdot \log n)$, hoặc với [Cây hậu tố (Suffix Tree)](suffix-tree-ukkonen.md) và truy vấn LCA nhanh, bài toán có thể giải trong $O(n)$.

Tuy nhiên, phương pháp được mô tả ở đây **đơn giản hơn đáng kể** và có hằng số ẩn nhỏ hơn trong độ phức tạp thời gian và bộ nhớ. Thuật toán này được khám phá bởi **Glenn K. Manacher** vào năm 1975.

Một cách hiện đại khác để giải bài toán này và xử lý các xâu đối xứng nói chung là thông qua cái gọi là cây đối xứng (palindromic tree), hay còn gọi là eertree.

## Thuật toán Vét cạn (Brute Force)

Để tránh nhầm lẫn trong các mô tả tiếp theo, chúng ta định nghĩa thế nào là "thuật toán vét cạn".

Đó là thuật toán thực hiện như sau: tại mỗi vị trí tâm $i$, nó cố gắng tăng câu trả lời lên một đơn vị chừng nào còn có thể, bằng cách so sánh cặp ký tự tương ứng mỗi lần.

Thuật toán này chậm, nó chỉ có thể tính kết quả trong $O(n^2)$.

Cài đặt của thuật toán vét cạn như sau:

```cpp
vector<int> manacher_odd_trivial(string s) {
    int n = s.size();
    s = "$" + s + "^";
    vector<int> p(n + 2);
    for(int i = 1; i <= n; i++) {
        while(s[i - p[i]] == s[i + p[i]]) {
            p[i]++;
        }
    }
    return vector<int>(begin(p) + 1, end(p) - 1);
}
```

Các ký tự đặc biệt `$` và `^` được sử dụng để tránh phải xử lý riêng các biên của xâu.

## Thuật toán Manacher

Chúng ta mô tả thuật toán tìm tất cả các xâu con đối xứng độ dài lẻ, tức là tính $d_{odd}[]$.

Để tính toán nhanh, chúng ta sẽ duy trì **biên độc quyền $(l, r)$** của xâu đối xứng (con) nằm xa nhất về bên phải (tức là xâu đối xứng con nằm xa nhất hiện tại là $s[l+1] s[l+2] \dots s[r-1]$). Ban đầu ta đặt $l = 0, r = 1$, tương ứng với xâu rỗng.

Vì vậy, chúng ta muốn tính $d_{odd}[i]$ cho vị trí tiếp theo $i$, và tất cả các giá trị trước đó trong $d_{odd}[]$ đã được tính xong. Chúng ta thực hiện như sau:

* Nếu $i$ nằm ngoài xâu đối xứng hiện tại, tức là $i \geq r$, chúng ta sẽ chạy thuật toán vét cạn.
    
    Chúng ta sẽ tăng $d_{odd}[i]$ liên tiếp và kiểm tra xem xâu con nằm xa nhất hiện tại $[i - d_{odd}[i]\dots i + d_{odd}[i]]$ có là xâu đối xứng hay không. Khi gặp cặp ký tự không khớp đầu tiên hoặc chạm tới biên của $s$, ta dừng lại. Lúc này, ta đã tính xong $d_{odd}[i]$. Sau đó, ta cập nhật $(l, r)$. $r$ cần được cập nhật sao cho nó đại diện cho chỉ số cuối cùng của xâu đối xứng nằm xa nhất về bên phải hiện tại.

* Bây giờ xét trường hợp $i \le r$. Chúng ta sẽ cố gắng trích xuất thông tin từ các giá trị đã tính trong $d_{odd}[]$. Tìm vị trí "đối xứng" của $i$ trong xâu đối xứng $(l, r)$, tức là vị trí $j = l + (r - i)$, và kiểm tra giá trị $d_{odd}[j]$. Vì $j$ là vị trí đối xứng với $i$ qua $(l+r)/2$, chúng ta **gần như luôn luôn** có thể gán $d_{odd}[i] = d_{odd}[j]$. Hình minh họa (xâu đối xứng quanh $j$ thực tế được "sao chép" vào xâu đối xứng quanh $i$):
    
    $$
    \ldots\ 
    \overbrace{
        s_{l+1}\ \ldots\ 
        \underbrace{
            s_{j-d_{odd}[j]+1}\ \ldots\ s_j\ \ldots\ s_{j+d_{odd}[j]-1}\ 
        }_\text{palindrome}\ 
        \ldots\ 
        \underbrace{
            s_{i-d_{odd}[j]+1}\ \ldots\ s_i\ \ldots\ s_{i+d_{odd}[j]-1}\ 
        }_\text{palindrome}\ 
        \ldots\ s_{r-1}\ 
    }^\text{palindrome}\ 
    \ldots
    $$
    
    Tuy nhiên, có một **trường hợp đặc biệt** cần xử lý đúng: khi xâu đối xứng "bên trong" chạm tới biên của xâu đối xứng "bên ngoài", tức là $j - d_{odd}[j] \le l$ (hoặc $i + d_{odd}[j] \ge r$). Vì tính đối xứng bên ngoài xâu "bên ngoài" không được đảm bảo, việc chỉ gán $d_{odd}[i] = d_{odd}[j]$ sẽ không chính xác: ta không có đủ dữ liệu để khẳng định xâu đối xứng tại vị trí $i$ có cùng độ dài.
    
    Thực tế, ta nên giới hạn độ dài của xâu đối xứng tại thời điểm này, tức là gán $d_{odd}[i] = r - i$ để xử lý tình huống đó một cách chính xác. Sau đó, ta sẽ chạy thuật toán vét cạn để cố gắng tăng $d_{odd}[i]$ nếu có thể.
    
    Hình minh họa trường hợp này (xâu đối xứng với tâm $j$ bị giới hạn để nằm trọn trong xâu "bên ngoài"):
    
    $$
    \ldots\ 
    \overbrace{
        \underbrace{
            s_{l+1}\ \ldots\ s_j\ \ldots\ s_{j+(j-l)-1}\ 
        }_\text{palindrome}\ 
        \ldots\ 
        \underbrace{
            s_{i-(r-i)+1}\ \ldots\ s_i\ \ldots\ s_{r-1}
        }_\text{palindrome}\ 
    }^\text{palindrome}\ 
    \underbrace{
        \ldots \ldots \ldots \ldots \ldots
    }_\text{try moving here}
    $$
    
    Hình minh họa cho thấy xâu đối xứng với tâm $j$ có thể lớn hơn và vượt ra ngoài xâu "bên ngoài", nhưng với $i$ là tâm, ta chỉ có thể sử dụng phần nằm trọn vẹn bên trong xâu "bên ngoài". Tuy nhiên, kết quả cho vị trí $i$ ($d_{odd}[i]$) có thể lớn hơn phần này, vì vậy tiếp theo ta sẽ chạy thuật toán vét cạn để thử mở rộng nó ra ngoài xâu "bên ngoài", tức là vùng "thử di chuyển đến đây".

Một lần nữa, đừng quên cập nhật giá trị $(l, r)$ sau khi tính mỗi $d_{odd}[i]$.

## Độ phức tạp của thuật toán Manacher

Thoạt nhìn, không rõ thuật toán này có độ phức tạp thời gian tuyến tính hay không, vì ta thường xuyên chạy thuật toán vét cạn khi tìm đáp án cho một vị trí cụ thể.

Tuy nhiên, phân tích kỹ hơn cho thấy thuật toán có độ phức tạp tuyến tính. Thực tế, [thuật toán xây dựng Hàm Z](z-function.md), vốn trông khá tương tự, cũng hoạt động trong thời gian tuyến tính.

Ta có thể nhận thấy rằng mỗi bước lặp của thuật toán vét cạn sẽ làm tăng $r$ lên một. Đồng thời, $r$ không bao giờ giảm trong suốt thuật toán. Do đó, thuật toán vét cạn chỉ thực hiện tổng cộng $O(n)$ lần lặp.

Các phần khác của thuật toán Manacher hiển nhiên hoạt động trong thời gian tuyến tính. Do đó, ta có độ phức tạp thời gian $O(n)$.

## Cài đặt thuật toán Manacher

Để tính $d_{odd}[]$, ta có mã nguồn sau. Các điểm cần lưu ý:

 - $i$ là chỉ số của ký tự tâm của xâu đối xứng hiện tại.
 - Nếu $i$ vượt quá $r$, $d_{odd}[i]$ được khởi tạo bằng 0.
 - Nếu $i$ không vượt quá $r$, $d_{odd}[i]$ được khởi tạo bằng $d_{odd}[j]$, trong đó $j$ là vị trí đối xứng của $i$ trong $(l,r)$, hoặc $d_{odd}[i]$ bị giới hạn bởi kích thước của xâu "bên ngoài".
 - Vòng lặp `while` biểu thị thuật toán vét cạn. Chúng ta chạy nó bất kể giá trị của $k$.
 - Nếu kích thước của xâu đối xứng tâm $i$ là $x$, thì $d_{odd}[i]$ lưu $\frac{x+1}{2}$.

```{.cpp file=manacher_odd}
vector<int> manacher_odd(string s) {
    int n = s.size();
    s = "$" + s + "^";
    vector<int> p(n + 2);
    int l = 0, r = 1;
    for(int i = 1; i <= n; i++) {
        if(i <= r) {
            p[i] = min(r - i, p[l + (r - i)]);
        }
        while(s[i - p[i]] == s[i + p[i]]) {
            p[i]++;
        }
        if(i + p[i] > r) {
            l = i - p[i], r = i + p[i];
        }
    }
    return vector<int>(begin(p) + 1, end(p) - 1);
}
```

## Xử lý tính chẵn lẻ

Mặc dù có thể cài đặt thuật toán Manacher cho độ dài lẻ và chẵn riêng biệt, việc cài đặt phiên bản cho độ dài chẵn thường được coi là khó hơn vì nó ít tự nhiên và dễ dẫn đến các lỗi sai lệch chỉ số (off-by-one errors).

Để giảm thiểu điều này, ta có thể quy bài toán về trường hợp chỉ xử lý các xâu đối xứng độ dài lẻ. Để làm điều này, ta chèn thêm ký tự `#` vào giữa mỗi chữ cái trong xâu, cũng như ở đầu và cuối xâu:

$$abcbcba \to \#a\#b\#c\#b\#c\#b\#a\#,$$

$$d = [1,2,1,2,1,4,1,8,1,4,1,2,1,2,1].$$

Như bạn thấy, $d[2i]=2 d_{even}[i]+1$ và $d[2i+1]=2 d_{odd}[i]$, trong đó $d$ biểu thị mảng Manacher cho các xâu đối xứng độ dài lẻ trong xâu đã chèn `#`, trong khi $d_{odd}$ và $d_{even}$ tương ứng với các mảng đã định nghĩa ở trên trong xâu ban đầu.

Thật vậy, các ký tự `#` không ảnh hưởng đến các xâu đối xứng độ dài lẻ (vẫn có tâm tại các ký tự của xâu ban đầu), nhưng các xâu đối xứng độ dài chẵn của xâu ban đầu nay trở thành các xâu đối xứng độ dài lẻ của xâu mới với tâm nằm tại các ký tự `#`.

Lưu ý rằng $d[2i]$ và $d[2i+1]$ về cơ bản là độ dài (đã cộng thêm $1$) của các xâu đối xứng độ dài lẻ và chẵn lớn nhất tương ứng với tâm tại $i$.

Việc quy đổi được cài đặt như sau:

```cpp
vector<int> manacher(string s) {
    string t;
    for(auto c: s) {
        t += string("#") + c;
    }
    auto res = manacher_odd(t + "#");
    return vector<int>(begin(res) + 1, end(res) - 1);
}
```

Để đơn giản, việc tách mảng thành $d_{odd}$ và $d_{even}$ cũng như tính toán tường minh của chúng đã được lược bỏ.

## Các bài toán liên quan

- [Library Checker - Enumerate Palindromes](https://judge.yosupo.jp/problem/enumerate_palindromes)
- [Longest Palindrome](https://cses.fi/problemset/task/1111)
- [UVA 11475 - Extend to Palindrome](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=26&page=show_problem&problem=2470)
- [GYM - (Q) QueryreuQ](https://codeforces.com/gym/101806/problem/Q)
- [CF - Prefix-Suffix Palindrome](https://codeforces.com/contest/1326/problem/D2)
- [SPOJ - Number of Palindromes](https://www.spoj.com/problems/NUMOFPAL/)
- [Kattis - Palindromes](https://open.kattis.com/problems/palindromes)