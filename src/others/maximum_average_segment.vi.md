---
tags:
  - Translated
e_maxx_link: maximum_average_segment
lang: vi
---
# Tìm mảng con có tổng lớn nhất/nhỏ nhất

Ở đây, chúng ta sẽ xem xét bài toán tìm mảng con (subarray) có tổng lớn nhất, cùng với một vài biến thể của nó (bao gồm cả thuật toán để giải bài toán này theo kiểu trực tuyến).

## Phát biểu bài toán

Cho một mảng các số $a[1 \ldots n]$. Yêu cầu tìm một mảng con $a[l \ldots r]$ có tổng lớn nhất:

$$ \max_{ 1 \le l \le r \le n } \sum_{i=l}^{r} a[i].$$

Ví dụ, nếu tất cả các số nguyên trong mảng $a[]$ đều không âm, thì câu trả lời chính là toàn bộ mảng đó.
Tuy nhiên, bài toán sẽ không còn tầm thường khi mảng chứa cả số dương và số âm.

Rõ ràng là bài toán tìm mảng con có **tổng nhỏ nhất** cũng tương tự, bạn chỉ cần đổi dấu tất cả các số trong mảng.

## Thuật toán 1

Ở đây chúng ta xem xét một thuật toán gần như hiển nhiên. (Tiếp theo, chúng ta sẽ xem xét một thuật toán khác, khó nghĩ ra hơn một chút, nhưng cài đặt lại ngắn gọn hơn).

### Mô tả thuật toán

Thuật toán rất đơn giản.

Để thuận tiện, chúng ta đặt **ký hiệu**: $s[i] = \sum_{j=1}^{i} a[j]$. Nghĩa là mảng $s[i]$ là mảng các tổng tiền tố (prefix sum) của mảng $a[]$. Ngoài ra, đặt $s[0] = 0$.

Bây giờ, hãy lặp qua chỉ số $r = 1 \ldots n$, và tìm cách xác định nhanh $l$ tối ưu cho giá trị hiện tại $r$, tại đó đạt được tổng lớn nhất trên mảng con $[l, r]$.

Về mặt hình thức, điều này có nghĩa là với $r$ hiện tại, chúng ta cần tìm một $l$ (không vượt quá $r$), sao cho giá trị $s[r] - s[l-1]$ là lớn nhất. Sau một phép biến đổi tầm thường, ta thấy rằng cần tìm giá trị nhỏ nhất trong mảng $s[]$ trên đoạn $[0, r-1]$.

Từ đó, ta có ngay lời giải: chỉ cần lưu trữ vị trí của giá trị nhỏ nhất trong mảng $s[]$. Sử dụng giá trị nhỏ nhất này, ta tìm được chỉ số tối ưu $l$ trong $O(1)$, và khi di chuyển từ chỉ số $r$ hiện tại sang chỉ số tiếp theo, ta chỉ cần cập nhật giá trị nhỏ nhất này.

Rõ ràng, thuật toán này hoạt động với độ phức tạp thời gian $O(n)$ và là tối ưu về mặt tiệm cận.

### Cài đặt

Để cài đặt, chúng ta thậm chí không cần lưu trữ mảng tổng tiền tố $s[]$ một cách tường minh — chúng ta chỉ cần phần tử hiện tại từ nó.

Phần cài đặt dưới đây sử dụng mảng đánh chỉ số từ 0, thay vì đánh chỉ số từ 1 như đã mô tả ở trên.

Đầu tiên là lời giải trả về giá trị số đơn thuần mà không tìm chỉ số của đoạn cần tìm:

```cpp
int ans = a[0], sum = 0, min_sum = 0;

for (int r = 0; r < n; ++r) {
    sum += a[r];
    ans = max(ans, sum - min_sum);
    min_sum = min(min_sum, sum);
}
```

Bây giờ là phiên bản đầy đủ, bổ sung thêm việc tìm biên của đoạn mảng cần tìm:

```cpp
int ans = a[0], ans_l = 0, ans_r = 0;
int sum = 0, min_sum = 0, min_pos = -1;

for (int r = 0; r < n; ++r) {
    sum += a[r];
    int cur = sum - min_sum;
    if (cur > ans) {
        ans = cur;
        ans_l = min_pos + 1;
        ans_r = r;
    }
    if (sum < min_sum) {
        min_sum = sum;
        min_pos = r;
    }
}
```

## Thuật toán 2

Ở đây chúng ta xem xét một thuật toán khác. Nó khó hiểu hơn một chút, nhưng thanh thoát hơn thuật toán trên và cách cài đặt cũng ngắn gọn hơn. Thuật toán này được Jay Kadane đề xuất vào năm 1984.

### Mô tả thuật toán

Thuật toán như sau: Hãy duyệt qua mảng và tích lũy tổng tiền tố hiện tại vào một biến $s$. Nếu tại một thời điểm $s$ trở thành số âm, chúng ta gán $s=0$. Người ta chứng minh rằng giá trị lớn nhất mà biến $s$ nhận được trong quá trình chạy thuật toán chính là đáp án của bài toán.

**Chứng minh:**

Xét chỉ số đầu tiên mà tổng của $s$ trở nên âm. Điều này có nghĩa là bắt đầu với tổng tiền tố bằng 0, cuối cùng chúng ta thu được một tổng tiền tố âm — vì vậy toàn bộ tiền tố này, cũng như bất kỳ hậu tố nào của nó, đều có tổng âm. Do đó, mảng con này không bao giờ đóng góp vào tổng tiền tố của bất kỳ mảng con nào mà nó là tiền tố, và có thể đơn giản là bỏ qua nó.

Tuy nhiên, điều này vẫn chưa đủ để chứng minh thuật toán. Trong thuật toán, chúng ta thực sự chỉ giới hạn việc tìm kiếm đáp án ở các đoạn bắt đầu ngay sau các vị trí xảy ra $s<0$.

Trên thực tế, xét một đoạn bất kỳ $[l, r]$, và giả sử $l$ không nằm ở vị trí "tới hạn" (tức là $l > p+1$, với $p$ là vị trí tới hạn cuối cùng mà $s<0$). Vì vị trí tới hạn cuối cùng nằm hoàn toàn trước $l-1$, nên tổng của $a[p+1 \ldots l-1]$ không âm. Điều này có nghĩa là bằng cách di chuyển $l$ đến vị trí $p+1$, chúng ta sẽ tăng đáp án hoặc trong trường hợp xấu nhất là không làm thay đổi nó.

Dù thế nào đi nữa, kết quả là khi tìm kiếm đáp án, bạn chỉ cần giới hạn ở các đoạn bắt đầu ngay sau các vị trí xuất hiện $s<0$. Điều này chứng minh thuật toán là đúng.

### Cài đặt

Như ở thuật toán 1, chúng ta đưa ra cách cài đặt rút gọn chỉ tìm giá trị số:

```cpp
int ans = a[0], sum = 0;

for (int r = 0; r < n; ++r) {
    sum += a[r];
    ans = max(ans, sum);
    sum = max(sum, 0);
}
```

Lời giải đầy đủ, duy trì chỉ số biên của đoạn mảng tương ứng:

```cpp
int ans = a[0], ans_l = 0, ans_r = 0;
int sum = 0, minus_pos = -1;

for (int r = 0; r < n; ++r) {
    sum += a[r];
    if (sum > ans) {
        ans = sum;
        ans_l = minus_pos + 1;
        ans_r = r;
    }
    if (sum < 0) {
        sum = 0;
        minus_pos = r;
    }
}
```

## Các bài toán liên quan

### Tìm mảng con cực đại/cực tiểu với ràng buộc

Nếu điều kiện bài toán đặt ra thêm các hạn chế cho đoạn cần tìm $[l, r]$ (ví dụ: độ dài $r-l+1$ của đoạn phải nằm trong giới hạn cho trước), thì thuật toán đã mô tả vẫn dễ dàng được tổng quát hóa — dù sao đi nữa, bài toán vẫn quy về tìm giá trị nhỏ nhất trong mảng $s[]$ với các ràng buộc bổ sung cho trước.

### Bài toán hai chiều: tìm ma trận con có tổng lớn nhất/nhỏ nhất

Bài toán mô tả trong bài này được tổng quát hóa một cách tự nhiên lên không gian nhiều chiều. Ví dụ, trong trường hợp hai chiều, nó trở thành bài toán tìm ma trận con $[l_1 \ldots r_1, l_2 \ldots r_2]$ của một ma trận cho trước có tổng các phần tử lớn nhất.

Sử dụng lời giải cho trường hợp một chiều, ta dễ dàng thu được lời giải với độ phức tạp $O(n^3)$ cho trường hợp hai chiều: chúng ta lặp qua mọi cặp giá trị $l_1$ và $r_1$, và tính tổng từ $l_1$ đến $r_1$ cho từng hàng của ma trận. Bây giờ chúng ta có bài toán một chiều về việc tìm chỉ số $l_2$ và $r_2$ trong mảng này, vốn đã có thể giải quyết trong thời gian tuyến tính.

Có nhiều thuật toán **nhanh hơn** để giải bài toán này, nhưng chúng không nhanh hơn đáng kể so với $O(n^3)$ và rất phức tạp (phức tạp đến mức nhiều thuật toán trong số đó còn chậm hơn thuật toán tầm thường do hằng số ẩn lớn đối với mọi ràng buộc hợp lý). Hiện tại, thuật toán tốt nhất được biết đến hoạt động trong $O\left(n^3 \frac{ \log^3 \log n }{ \log^2 n} \right)$ (T. Chan 2007 "More algorithms for all-pairs shortest paths in weighted graphs").

Thuật toán của Chan, cũng như nhiều kết quả khác trong lĩnh vực này, thực sự mô tả **phép nhân ma trận nhanh** (trong đó phép nhân ma trận được hiểu là phép nhân biến đổi: sử dụng phép lấy min thay cho phép cộng, và phép cộng thay cho phép nhân). Bài toán tìm ma trận con có tổng lớn nhất có thể quy về bài toán tìm đường đi ngắn nhất giữa tất cả các cặp đỉnh, và bài toán này, đến lượt nó, lại có thể quy về phép nhân ma trận dạng trên.

### Tìm mảng con có trung bình cộng lớn nhất/nhỏ nhất

Bài toán này nằm ở việc tìm đoạn $a[l, r]$ sao cho giá trị trung bình là lớn nhất:

$$ \max_{l \le r} \frac{ 1 }{ r-l+1 } \sum_{i=l}^{r} a[i].$$

Tất nhiên, nếu không có điều kiện nào khác được đặt ra cho đoạn cần tìm $[l, r]$, thì lời giải luôn là một đoạn có độ dài $1$ tại phần tử lớn nhất của mảng. Bài toán chỉ có ý nghĩa khi có thêm các ràng buộc bổ sung (ví dụ: độ dài của đoạn cần tìm bị chặn dưới).

Trong trường hợp này, chúng ta áp dụng **kỹ thuật tiêu chuẩn** khi làm việc với các bài toán về giá trị trung bình: chọn giá trị trung bình lớn nhất cần tìm bằng **tìm kiếm nhị phân (Binary Search)**.

Để làm điều này, chúng ta cần học cách giải bài toán con sau: cho số $x$, cần kiểm tra xem có mảng con nào của mảng $a[]$ (thỏa mãn các ràng buộc bổ sung của bài toán) mà giá trị trung bình lớn hơn $x$ hay không.

Để giải bài toán con này, hãy trừ $x$ từ mỗi phần tử của mảng $a[]$. Khi đó, bài toán con thực sự trở thành: liệu có tồn tại mảng con có tổng dương trong mảng này hay không. Và chúng ta đã biết cách giải bài toán này.

Như vậy, chúng ta thu được lời giải với độ phức tạp tiệm cận $O(T(n) \log W)$, trong đó $W$ là độ chính xác yêu cầu, $T(n)$ là thời gian giải bài toán con cho một mảng có độ dài $n$ (có thể thay đổi tùy thuộc vào các ràng buộc bổ sung cụ thể).

### Giải bài toán trực tuyến (Online)

Điều kiện bài toán như sau: cho một mảng gồm $n$ số và một số $L$. Có các truy vấn dạng $(l,r)$, và để trả lời mỗi truy vấn, cần tìm một mảng con trong đoạn $[l, r]$ có độ dài không nhỏ hơn $L$ với giá trị trung bình cộng lớn nhất có thể.

Thuật toán để giải bài toán này khá phức tạp. KADR (Yaroslav Tverdokhleb) đã mô tả thuật toán của mình trên [diễn đàn tiếng Nga](http://e-maxx.ru/forum/viewtopic.php?id=410).