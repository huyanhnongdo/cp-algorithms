---
tags:
  - Translated
e_maxx_link: bracket_sequences
lang: vi
---
# Các dãy ngoặc cân bằng

Một **dãy ngoặc cân bằng** (balanced bracket sequence) là một chuỗi chỉ bao gồm các dấu ngoặc, sao cho khi chèn vào đó một số lượng các số và phép toán toán học, ta thu được một biểu thức toán học hợp lệ.
Về mặt hình thức, bạn có thể định nghĩa dãy ngoặc cân bằng như sau:

- $e$ (chuỗi rỗng) là một dãy ngoặc cân bằng.
- Nếu $s$ là một dãy ngoặc cân bằng, thì $(s)$ cũng là một dãy ngoặc cân bằng.
- Nếu $s$ và $t$ là các dãy ngoặc cân bằng, thì $s t$ cũng là một dãy ngoặc cân bằng.

Ví dụ, $(())()$ là một dãy ngoặc cân bằng, nhưng $())($ thì không.

Tất nhiên, bạn cũng có thể định nghĩa các loại dãy ngoặc khác với nhiều loại dấu ngoặc theo cách tương tự.

Trong bài viết này, chúng ta sẽ thảo luận về một số bài toán kinh điển liên quan đến các dãy ngoặc cân bằng (gọi tắt là các dãy): kiểm tra tính hợp lệ, đếm số lượng dãy, tìm dãy tiếp theo theo thứ tự từ điển, tạo tất cả các dãy có kích thước nhất định, tìm chỉ số của một dãy, và tạo dãy thứ $k$.
Chúng ta cũng sẽ thảo luận về hai biến thể của bài toán: phiên bản đơn giản hơn khi chỉ cho phép một loại dấu ngoặc, và trường hợp khó hơn khi có nhiều loại dấu ngoặc.

## Kiểm tra tính cân bằng

Chúng ta muốn kiểm tra xem một chuỗi cho trước có cân bằng hay không.

Trước hết, giả sử chỉ có một loại dấu ngoặc.
Với trường hợp này, tồn tại một thuật toán rất đơn giản.
Gọi $\text{depth}$ là số lượng dấu mở ngoặc hiện tại.
Ban đầu $\text{depth} = 0$.
Chúng ta duyệt qua tất cả các ký tự của chuỗi, nếu ký tự ngoặc hiện tại là dấu mở, ta tăng $\text{depth}$, ngược lại ta giảm nó.
Nếu tại bất kỳ thời điểm nào biến $\text{depth}$ trở nên âm, hoặc cuối cùng nó khác $0$, thì chuỗi không phải là một dãy cân bằng.
Ngược lại, chuỗi đó là cân bằng.

Nếu có nhiều loại dấu ngoặc, thuật toán cần được thay đổi.
Thay vì dùng biến đếm $\text{depth}$, ta sử dụng một ngăn xếp (Stack), nơi ta sẽ lưu trữ tất cả các dấu mở ngoặc gặp phải.
Nếu ký tự ngoặc hiện tại là dấu mở, ta đẩy nó vào ngăn xếp.
Nếu là dấu đóng, ta kiểm tra xem ngăn xếp có khác rỗng hay không, và liệu phần tử trên cùng của ngăn xếp có cùng loại với dấu đóng hiện tại hay không.
Nếu cả hai điều kiện đều thỏa mãn, ta loại bỏ dấu mở ngoặc khỏi ngăn xếp.
Nếu tại bất kỳ thời điểm nào một trong các điều kiện không được thỏa mãn, hoặc cuối cùng ngăn xếp không rỗng, thì chuỗi không cân bằng.
Ngược lại, nó là cân bằng.

## Số lượng các dãy cân bằng

### Công thức

Số lượng các dãy ngoặc cân bằng với chỉ một loại dấu ngoặc có thể được tính bằng cách sử dụng [số Catalan](catalan-numbers.md).
Số lượng các dãy ngoặc cân bằng có độ dài $2n$ ($n$ cặp ngoặc) là:

$$\frac{1}{n+1} \binom{2n}{n}$$

Nếu cho phép $k$ loại dấu ngoặc, thì mỗi cặp có thể thuộc bất kỳ loại nào trong $k$ loại đó (độc lập với các cặp khác), do đó số lượng dãy ngoặc cân bằng là:

$$\frac{1}{n+1} \binom{2n}{n} k^n$$

### Quy hoạch động

Mặt khác, các số này có thể được tính bằng **Quy hoạch động (DP)**.
Gọi $d[n]$ là số lượng các dãy ngoặc chuẩn với $n$ cặp ngoặc.
Lưu ý rằng ở vị trí đầu tiên luôn luôn là một dấu mở ngoặc.
Và ở đâu đó sau đó là dấu đóng ngoặc tương ứng của cặp này.
Rõ ràng là bên trong cặp này là một dãy ngoặc cân bằng, và tương tự, sau cặp này cũng là một dãy ngoặc cân bằng.
Vì vậy, để tính $d[n]$, ta sẽ xem xét có bao nhiêu dãy cân bằng với $i$ cặp ngoặc nằm trong cặp ngoặc đầu tiên đó, và bao nhiêu dãy cân bằng với $n-1-i$ cặp ngoặc nằm sau cặp đó.
Kết quả là công thức có dạng:

$$d[n] = \sum_{i=0}^{n-1} d[i] \cdot d[n-1-i]$$

Giá trị khởi đầu cho công thức truy hồi này là $d[0] = 1$.

## Tìm dãy cân bằng kế tiếp theo thứ tự từ điển

Ở đây chúng ta chỉ xem xét trường hợp có một loại dấu ngoặc hợp lệ.

Cho trước một dãy cân bằng, ta phải tìm dãy tiếp theo (theo thứ tự từ điển).

Rõ ràng là ta cần tìm dấu mở ngoặc nằm xa nhất về bên phải mà ta có thể thay thế bằng một dấu đóng ngoặc mà không làm vi phạm điều kiện "số dấu đóng không được vượt quá số dấu mở tại mọi vị trí".
Sau khi thay thế vị trí này, ta có thể lấp đầy phần còn lại của chuỗi theo cách nhỏ nhất có thể về thứ tự từ điển: nghĩa là trước tiên đặt càng nhiều dấu mở ngoặc càng tốt, sau đó lấp đầy các vị trí còn lại bằng các dấu đóng ngoặc.
Nói cách khác, ta cố gắng giữ tiền tố dài nhất có thể, và hậu tố sẽ được thay thế bằng chuỗi nhỏ nhất về thứ tự từ điển.

Để tìm vị trí này, ta có thể duyệt các ký tự từ phải sang trái và duy trì sự cân bằng $\text{depth}$ giữa các dấu mở và dấu đóng.
Khi gặp dấu mở ngoặc, ta giảm $\text{depth}$, và khi gặp dấu đóng ngoặc, ta tăng nó lên.
Nếu tại một điểm nào đó ta gặp một dấu mở ngoặc và số dư sau khi xử lý ký tự đó là dương, thì ta đã tìm thấy vị trí xa nhất về bên phải mà ta có thể thay đổi.
Ta thay đổi ký tự đó, tính toán số lượng dấu mở và đóng cần thêm vào phía bên phải, và sắp xếp chúng theo cách nhỏ nhất về thứ tự từ điển.

Nếu không tìm thấy vị trí thích hợp, thì dãy này đã là dãy lớn nhất có thể, và không có đáp án.

```{.cpp file=next_balanced_brackets_sequence}
bool next_balanced_sequence(string & s) {
    int n = s.size();
    int depth = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '(')
            depth--;
        else
            depth++;

        if (s[i] == '(' && depth > 0) {
            depth--;
            int open = (n - i - 1 - depth) / 2;
            int close = n - i - 1 - open;
            string next = s.substr(0, i) + ')' + string(open, '(') + string(close, ')');
            s.swap(next);
            return true;
        }
    }
    return false;
}
```

Hàm này tính toán dãy ngoặc cân bằng tiếp theo trong thời gian $O(n)$, và trả về `false` nếu không có dãy tiếp theo.

## Tìm tất cả các dãy cân bằng

Đôi khi ta cần tìm và xuất ra tất cả các dãy ngoặc cân bằng có độ dài cụ thể $n$.

Để tạo chúng, ta có thể bắt đầu với dãy nhỏ nhất về thứ tự từ điển là $((\dots(())\dots))$, sau đó tiếp tục tìm các dãy tiếp theo bằng thuật toán được mô tả ở phần trước.

Tuy nhiên, nếu độ dài của dãy không quá lớn (ví dụ $n$ nhỏ hơn $12$), thì ta cũng có thể tạo tất cả các hoán vị một cách thuận tiện bằng hàm `next_permutation` của C++ STL và kiểm tra tính cân bằng của từng hoán vị.

Các dãy này cũng có thể được tạo ra bằng ý tưởng sử dụng quy hoạch động. Chúng ta sẽ thảo luận về ý tưởng này trong hai phần tiếp theo.

## Chỉ số của dãy

Cho một dãy ngoặc cân bằng với $n$ cặp ngoặc.
Ta cần tìm chỉ số của nó trong danh sách đã sắp xếp theo thứ tự từ điển của tất cả các dãy cân bằng có $n$ cặp ngoặc.

Hãy định nghĩa một mảng phụ $d[i][j]$, trong đó $i$ là độ dài của dãy ngoặc (bán cân bằng, mỗi dấu đóng có một dấu mở tương ứng, nhưng không phải mọi dấu mở đều nhất thiết có dấu đóng tương ứng), và $j$ là sự cân bằng hiện tại (hiệu số giữa dấu mở và dấu đóng).
$d[i][j]$ là số lượng các dãy thỏa mãn các tham số đó.
Chúng ta sẽ tính toán các con số này với chỉ một loại dấu ngoặc.

Với giá trị khởi đầu $i = 0$, câu trả lời hiển nhiên là: $d[0][0] = 1$, và $d[0][j] = 0$ cho $j > 0$.
Bây giờ giả sử $i > 0$, và ta xem xét ký tự cuối cùng trong dãy.
Nếu ký tự cuối là dấu mở $($, thì trạng thái trước đó là $(i-1, j-1)$, nếu là dấu đóng $)$, thì trạng thái trước đó là $(i-1, j+1)$.
Như vậy ta có công thức truy hồi:

$$d[i][j] = d[i-1][j-1] + d[i-1][j+1]$$

$d[i][j] = 0$ rõ ràng đúng với $j$ âm.
Do đó, ta có thể tính mảng này trong $O(n^2)$.

Bây giờ hãy tạo chỉ số cho một dãy cho trước.

Trước hết, giả sử chỉ có một loại dấu ngoặc.
Ta sẽ sử dụng biến đếm $\text{depth}$ để theo dõi mức độ lồng nhau hiện tại và duyệt qua các ký tự của dãy.
Nếu ký tự hiện tại $s[i]$ bằng $($, thì ta tăng $\text{depth}$.
Nếu ký tự hiện tại $s[i]$ bằng $)$, thì ta phải cộng $d[2n-i-1][\text{depth}+1]$ vào kết quả, tính đến tất cả các kết thúc có thể bắt đầu bằng một $($ (đây là những dãy nhỏ hơn về thứ tự từ điển), và sau đó giảm $\text{depth}$.

Bây giờ giả sử có $k$ loại dấu ngoặc khác nhau.

Vì vậy, khi xem xét ký tự hiện tại $s[i]$ trước khi tính toán lại $\text{depth}$, ta phải đi qua tất cả các loại dấu ngoặc nhỏ hơn ký tự hiện tại, thử đặt dấu ngoặc đó vào vị trí hiện tại (thu được sự cân bằng mới $\text{ndepth} = \text{depth} \pm 1$), và cộng số cách để hoàn thành dãy (độ dài $2n-i-1$, cân bằng $ndepth$) vào kết quả:

$$d[2n - i - 1][\text{ndepth}] \cdot k^{\frac{2n - i - 1 - ndepth}{2}}$$

Công thức này có thể được suy ra như sau:
Trước tiên, hãy "quên" đi rằng có nhiều loại dấu ngoặc và chỉ lấy kết quả $d[2n - i - 1][\text{ndepth}]$.
Bây giờ ta xem xét kết quả thay đổi như thế nào nếu có $k$ loại dấu ngoặc.
Ta có $2n - i - 1$ vị trí chưa xác định, trong đó $\text{ndepth}$ vị trí đã được xác định do các dấu mở ngoặc.
Nhưng tất cả các dấu ngoặc còn lại ($(2n - i - 1 - \text{ndepth})/2$ cặp) có thể thuộc bất kỳ loại nào, vì vậy ta nhân số lượng đó với lũy thừa tương ứng của $k$.

## Tìm dãy thứ $k$ {data-toc-label="Finding the k-th sequence"}

Gọi $n$ là số cặp ngoặc trong dãy.
Ta cần tìm dãy cân bằng thứ $k$ trong danh sách đã sắp xếp theo thứ tự từ điển của tất cả các dãy cân bằng cho trước $k$.

Như ở phần trước, ta tính mảng phụ $d[i][j]$, là số lượng các dãy ngoặc bán cân bằng có độ dài $i$ với độ cân bằng $j$.

Trước tiên, bắt đầu với chỉ một loại dấu ngoặc.

Ta sẽ duyệt qua các ký tự trong chuỗi muốn tạo.
Như trong bài toán trước, ta lưu biến đếm $\text{depth}$ - độ sâu lồng nhau hiện tại.
Tại mỗi vị trí, ta phải quyết định đặt dấu mở hay dấu đóng. Để đặt một dấu mở, điều kiện $d[2n - i - 1][\text{depth}+1] \ge k$ phải đúng.
Nếu đúng, ta tăng biến đếm $\text{depth}$ và chuyển sang ký tự tiếp theo.
Nếu không, ta giảm $k$ đi $d[2n - i - 1][\text{depth}+1]$, đặt một dấu đóng và tiếp tục.

```{.cpp file=kth_balances_bracket}
string kth_balanced(int n, int k) {
    vector<vector<int>> d(2*n+1, vector<int>(n+1, 0));
    d[0][0] = 1;
    for (int i = 1; i <= 2*n; i++) {
        d[i][0] = d[i-1][1];
        for (int j = 1; j < n; j++)
            d[i][j] = d[i-1][j-1] + d[i-1][j+1];
        d[i][n] = d[i-1][n-1];
    }

    string ans;
    int depth = 0;
    for (int i = 0; i < 2*n; i++) {
        if (depth + 1 <= n && d[2*n-i-1][depth+1] >= k) {
            ans += '(';
            depth++;
        } else {
            ans += ')';
            if (depth + 1 <= n)
                k -= d[2*n-i-1][depth+1];
            depth--;
        }
    }
    return ans;
}
```

Bây giờ giả sử có $k$ loại dấu ngoặc.
Giải pháp chỉ khác biệt một chút ở chỗ ta phải nhân giá trị $d[2n-i-1][\text{ndepth}]$ với $k^{(2n-i-1-\text{ndepth})/2}$ và lưu ý rằng có thể có các loại dấu ngoặc khác nhau cho ký tự tiếp theo.

Dưới đây là cài đặt sử dụng hai loại dấu ngoặc: ngoặc tròn và ngoặc vuông:

```{.cpp file=kth_balances_bracket_multiple}
string kth_balanced2(int n, int k) {
    vector<vector<int>> d(2*n+1, vector<int>(n+1, 0));
    d[0][0] = 1;
    for (int i = 1; i <= 2*n; i++) {
        d[i][0] = d[i-1][1];
        for (int j = 1; j < n; j++)
            d[i][j] = d[i-1][j-1] + d[i-1][j+1];
        d[i][n] = d[i-1][n-1];
    }

    string ans;
    int shift, depth = 0;

    stack<char> st;
    for (int i = 0; i < 2*n; i++) {

        // '('
        shift = ((2*n-i-1-depth-1) / 2);
        if (shift >= 0 && depth + 1 <= n) {
            int cnt = d[2*n-i-1][depth+1] << shift;
            if (cnt >= k) {
                ans += '(';
                st.push('(');
                depth++;
                continue;
            }
            k -= cnt;
        }

        // ')'
        shift = ((2*n-i-1-depth+1) / 2);
        if (shift >= 0 && depth && st.top() == '(') {
            int cnt = d[2*n-i-1][depth-1] << shift;
            if (cnt >= k) {
                ans += ')';
                st.pop();
                depth--;
                continue;
            }
            k -= cnt;
        }
            
        // '['
        shift = ((2*n-i-1-depth-1) / 2);
        if (shift >= 0 && depth + 1 <= n) {
            int cnt = d[2*n-i-1][depth+1] << shift;
            if (cnt >= k) {
                ans += '[';
                st.push('[');
                depth++;
                continue;
            }
            k -= cnt;
        }

        // ']'
        ans += ']';
        st.pop();
        depth--;
    }
    return ans;
}
```