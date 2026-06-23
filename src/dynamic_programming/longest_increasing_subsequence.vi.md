---
tags:
  - Translated
e_maxx_link: longest_increasing_subseq_log
lang: vi
---

# Dãy con tăng dài nhất (Longest Increasing Subsequence)

Cho một mảng gồm $n$ số: $a[0 \dots n-1]$.
Nhiệm vụ là tìm dãy con tăng ngặt dài nhất trong $a$.

Một cách hình thức, chúng ta tìm dãy các chỉ số dài nhất $i_1, \dots i_k$ sao cho

$$i_1 < i_2 < \dots < i_k,\quad
a[i_1] < a[i_2] < \dots < a[i_k]$$

Trong bài viết này, chúng ta sẽ thảo luận về nhiều thuật toán để giải quyết bài toán này.
Đồng thời, chúng ta cũng sẽ thảo luận về một số bài toán khác có thể đưa về bài toán này.

## Giải pháp trong $O(n^2)$ với quy hoạch động {data-toc-label="Giải pháp trong O(n^2) với quy hoạch động"}

Quy hoạch động (Dynamic programming) là một kỹ thuật rất tổng quát cho phép giải quyết một lớp bài toán lớn.
Ở đây chúng ta áp dụng kỹ thuật này cho bài toán cụ thể của mình.

Trước hết, chúng ta sẽ chỉ tìm **độ dài** của dãy con tăng dài nhất, và sau đó mới học cách khôi phục lại chính dãy con đó.

### Tìm độ dài

Để thực hiện công việc này, chúng ta định nghĩa một mảng $d[0 \dots n-1]$, trong đó $d[i]$ là độ dài của dãy con tăng dài nhất kết thúc ở phần tử tại chỉ số $i$.

!!! example

    $$\begin{array}{ll}
    a &= \{8, 3, 4, 6, 5, 2, 0, 7, 9, 1\} \\
    d &= \{1, 1, 2, 3, 3, 1, 1, 4, 5, 2\}
    \end{array}$$

    Dãy con tăng dài nhất kết thúc ở chỉ số 4 là $\{3, 4, 5\}$ với độ dài là 3, dãy con tăng dài nhất kết thúc ở chỉ số 8 là $\{3, 4, 5, 7, 9\}$ hoặc $\{3, 4, 6, 7, 9\}$, cả hai đều có độ dài 5, và dãy con tăng dài nhất kết thúc ở chỉ số 9 là $\{0, 1\}$ có độ dài 2.

Chúng ta sẽ tính toán mảng này một cách tuần tự: đầu tiên là $d[0]$, sau đó là $d[1]$, v.v.
Sau khi mảng này được tính xong, đáp án của bài toán sẽ là giá trị lớn nhất trong mảng $d[]$.

Giả sử chỉ số hiện tại là $i$.
Nghĩa là chúng ta muốn tính giá trị $d[i]$ và tất cả các giá trị trước đó $d[0], \dots, d[i-1]$ đều đã được biết.
Khi đó có hai trường hợp:

-   $d[i] = 1$: dãy con cần tìm chỉ gồm duy nhất phần tử $a[i]$.

-   $d[i] > 1$: Dãy con sẽ kết thúc tại $a[i]$, và ngay trước đó sẽ là một số $a[j]$ nào đó với $j < i$ và $a[j] < a[i]$.

    Dễ dàng thấy rằng, dãy con kết thúc ở $a[j]$ chính là một trong những dãy con tăng dài nhất kết thúc ở $a[j]$.
    Số $a[i]$ chỉ đơn giản là kéo dài dãy con tăng dài nhất đó thêm một phần tử.

    Do đó, chúng ta có thể duyệt qua tất cả các chỉ số $j < i$ thỏa mãn $a[j] < a[i]$, và lấy dãy dài nhất có được bằng cách thêm $a[i]$ vào dãy con tăng dài nhất kết thúc ở $a[j]$.
    Dãy con tăng dài nhất kết thúc ở $a[j]$ có độ dài $d[j]$, việc kéo dài thêm một phần tử sẽ cho độ dài $d[j] + 1$.
  
    $$d[i] = \max_{\substack{j < i \\\\ a[j] < a[i]}} \left(d[j] + 1\right)$$

Nếu kết hợp cả hai trường hợp này, chúng ta có công thức cuối cùng cho $d[i]$:

$$d[i] = \max\left(1, \max_{\substack{j < i \\\\ a[j] < a[i]}} \left(d[j] + 1\right)\right)$$

### Cài đặt

Dưới đây là mã nguồn cài đặt thuật toán được mô tả ở trên để tính độ dài của dãy con tăng dài nhất.

```{.cpp file=lis_n2}
int lis(vector<int> const& a) {
    int n = a.size();
    vector<int> d(n, 1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i])
                d[i] = max(d[i], d[j] + 1);
        }
    }

    int ans = d[0];
    for (int i = 1; i < n; i++) {
        ans = max(ans, d[i]);
    }
    return ans;
}
```

### Khôi phục dãy con

Cho đến nay chúng ta mới chỉ học cách tìm độ dài của dãy con, chứ chưa học cách tìm chính dãy con đó.

Để có thể khôi phục lại dãy con, chúng ta tạo thêm một mảng phụ trợ $p[0 \dots n-1]$ được tính toán song song với mảng $d[]$.
$p[i]$ sẽ là chỉ số $j$ của phần tử kề cuối trong dãy con tăng dài nhất kết thúc ở $i$.
Nói cách khác, chỉ số $p[i]$ chính là chỉ số $j$ mà tại đó giá trị lớn nhất của $d[i]$ được tìm thấy.
Mảng phụ này đóng vai trò như các liên kết trỏ tới nút cha.

Sau đó, để tìm dãy con, chúng ta chỉ cần bắt đầu từ chỉ số $i$ có giá trị $d[i]$ lớn nhất, rồi đi theo liên kết cha cho đến khi khôi phục được toàn bộ dãy con, tức là đến khi chạm tới phần tử có $d[i] = 1$.

### Cài đặt khôi phục dãy con

Chúng ta sẽ thay đổi đoạn mã từ các phần trước một chút.
Chúng ta sẽ tính toán mảng $p[]$ cùng với $d[]$, và sau đó khôi phục lại dãy con.

Để thuận tiện, ban đầu chúng ta gán các phần tử cha $p[i] = -1$.
Đối với các phần tử có $d[i] = 1$, giá trị cha của chúng sẽ giữ nguyên là $-1$, điều này giúp việc khôi phục dãy con tiện lợi hơn một chút.

```{.cpp file=lis_n2_restore}
vector<int> lis(vector<int> const& a) {
    int n = a.size();
    vector<int> d(n, 1), p(n, -1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i] && d[i] < d[j] + 1) {
                d[i] = d[j] + 1;
                p[i] = j;
            }
        }
    }

    int ans = d[0], pos = 0;
    for (int i = 1; i < n; i++) {
        if (d[i] > ans) {
            ans = d[i];
            pos = i;
        }
    }

    vector<int> subseq;
    while (pos != -1) {
        subseq.push_back(a[pos]);
        pos = p[pos];
    }
    reverse(subseq.begin(), subseq.end());
    return subseq;
}
```

### Cách khôi phục dãy con thay thế

Chúng ta cũng có thể khôi phục dãy con mà không cần mảng phụ trợ $p[]$.
Chúng ta chỉ cần tính toán lại giá trị hiện tại của $d[i]$ và xem làm thế nào để đạt được giá trị lớn nhất đó.

Phương pháp này khiến đoạn mã dài hơn một chút, nhưng bù lại chúng ta tiết kiệm được bộ nhớ.

## Giải pháp trong $O(n \log n)$ với quy hoạch động và tìm kiếm nhị phân {data-toc-label="Giải pháp trong O(n log n) với quy hoạch động và tìm kiếm nhị phân"}

Để có được lời giải nhanh hơn cho bài toán này, trước tiên chúng ta xây dựng một giải pháp quy hoạch động khác chạy trong $O(n^2)$, và sau đó cải tiến nó thành $O(n \log n)$.

Chúng ta sẽ sử dụng mảng quy hoạch động $d[0 \dots n]$.
Lần này $d[l]$ không tương ứng với phần tử $a[i]$ hay tiền tố của mảng nữa. 
Thay vào đó, $d[l]$ sẽ là phần tử nhỏ nhất mà một dãy con tăng độ dài $l$ kết thúc tại đó.

Ban đầu chúng ta giả định $d[0] = -\infty$ và đối với tất cả các độ dài khác $d[l] = \infty$.

Chúng ta lại xử lý tuần tự các số, đầu tiên là $a[0]$, sau đó là $a[1]$, v.v., và ở mỗi bước duy trì mảng $d[]$ luôn được cập nhật.

!!! example

    Cho mảng $a = \{8, 3, 4, 6, 5, 2, 0, 7, 9, 1\}$, dưới đây là tất cả các tiền tố và mảng quy hoạch động tương ứng của chúng.
    Lưu ý rằng các giá trị của mảng không phải lúc nào cũng chỉ thay đổi ở vị trí cuối cùng.

    $$
    \begin{array}{ll}
    \text{tiền tố} = \{\} &\quad d = \{-\infty, \infty, \dots\}\\
    \text{tiền tố} = \{8\} &\quad d = \{-\infty, 8, \infty, \dots\}\\
    \text{tiền tố} = \{8, 3\} &\quad d = \{-\infty, 3, \infty, \dots\}\\
    \text{tiền tố} = \{8, 3, 4\} &\quad d = \{-\infty, 3, 4, \infty, \dots\}\\
    \text{tiền tố} = \{8, 3, 4, 6\} &\quad d = \{-\infty, 3, 4, 6, \infty, \dots\}\\
    \text{tiền tố} = \{8, 3, 4, 6, 5\} &\quad d = \{-\infty, 3, 4, 5, \infty, \dots\}\\
    \text{tiền tố} = \{8, 3, 4, 6, 5, 2\} &\quad d = \{-\infty, 2, 4, 5, \infty, \dots \}\\
    \text{tiền tố} = \{8, 3, 4, 6, 5, 2, 0\} &\quad d = \{-\infty, 0, 4, 5, \infty, \dots \}\\
    \text{tiền tố} = \{8, 3, 4, 6, 5, 2, 0, 7\} &\quad d = \{-\infty, 0, 4, 5, 7, \infty, \dots \}\\
    \text{tiền tố} = \{8, 3, 4, 6, 5, 2, 0, 7, 9\} &\quad d = \{-\infty, 0, 4, 5, 7, 9, \infty, \dots \}\\
    \text{tiền tố} = \{8, 3, 4, 6, 5, 2, 0, 7, 9, 1\} &\quad d = \{-\infty, 0, 1, 5, 7, 9, \infty, \dots \}\\
    \end{array}
    $$

Khi xử lý $a[i]$, chúng ta có thể tự hỏi:
Điều kiện là gì để chúng ta ghi số hiện tại $a[i]$ vào mảng $d[0 \dots n]$?

Chúng ta gán $d[l] = a[i]$, nếu tồn tại một dãy con tăng dài nhất độ dài $l$ kết thúc tại $a[i]$, và không có dãy con tăng dài nhất độ dài $l$ nào khác kết thúc ở một số nhỏ hơn.
Tương tự như cách tiếp cận trước, nếu loại bỏ số $a[i]$ khỏi dãy con tăng độ dài $l$, chúng ta sẽ thu được một dãy con tăng khác có độ dài $l - 1$.
Do đó, chúng ta muốn mở rộng một dãy con tăng độ dài $l - 1$ bằng số $a[i]$, và rõ ràng dãy con tăng độ dài $l - 1$ kết thúc bởi phần tử nhỏ nhất sẽ là lựa chọn tối ưu nhất, nói cách khác chính là dãy con kết thúc ở phần tử $d[l-1]$.

Tồn tại một dãy con tăng độ dài $l - 1$ có thể mở rộng bằng số $a[i]$, khi và chỉ khi $d[l-1] < a[i]$.
Vì vậy, chúng ta có thể duyệt qua từng độ dài $l$ và kiểm tra xem có thể mở rộng dãy con tăng độ dài $l - 1$ hay không dựa trên tiêu chí này.

Ngoài ra chúng ta cũng cần kiểm tra xem liệu đã tìm được một dãy con tăng độ dài $l$ có số kết thúc nhỏ hơn hay chưa.
Nên chúng ta chỉ cập nhật nếu $a[i] < d[l]$.

Sau khi xử lý tất cả các phần tử của $a[]$, độ dài của dãy con mong muốn là giá trị $l$ lớn nhất thỏa mãn $d[l] < \infty$.

```{.cpp file=lis_method2_n2}
int lis(vector<int> const& a) {
    int n = a.size();
    const int INF = 1e9;
    vector<int> d(n+1, INF);
    d[0] = -INF;

    for (int i = 0; i < n; i++) {
        for (int l = 1; l <= n; l++) {
            if (d[l-1] < a[i] && a[i] < d[l])
                d[l] = a[i];
        }
    }

    int ans = 0;
    for (int l = 0; l <= n; l++) {
        if (d[l] < INF)
            ans = l;
    }
    return ans;
}
```

Bây giờ chúng ta đưa ra hai nhận xét quan trọng:

1.  Mảng $d$ luôn được sắp xếp tăng dần: 
    $d[l-1] < d[l]$ với mọi $i = 1 \dots n$.

    Điều này hiển nhiên đúng, vì bạn chỉ cần loại bỏ phần tử cuối cùng khỏi dãy con tăng độ dài $l$, bạn sẽ thu được một dãy con tăng độ dài $l-1$ kết thúc bởi một số nhỏ hơn.

2.  Phần tử $a[i]$ sẽ chỉ cập nhật tối đa một giá trị $d[l]$.

    Điều này suy ra trực tiếp từ cách cài đặt ở trên.
    Chỉ có thể có duy nhất một vị trí trong mảng thỏa mãn $d[l-1] < a[i] < d[l]$.

Do đó, chúng ta có thể tìm phần tử này trong mảng $d[]$ bằng cách sử dụng [tìm kiếm nhị phân (Binary Search)](../num_methods/binary_search.md) trong $O(\log n)$.
Thực tế, chúng ta chỉ cần tìm kiếm trong mảng $d[]$ số đầu tiên lớn hơn ngặt $a[i]$, và thử cập nhật phần tử này tương tự như thuật toán ở trên.

### Cài đặt

Từ đó ta thu được cài đặt cải tiến chạy trong $O(n \log n)$:

```{.cpp file=lis_method2_nlogn}
int lis(vector<int> const& a) {
    int n = a.size();
    const int INF = 1e9;
    vector<int> d(n+1, INF);
    d[0] = -INF;

    for (int i = 0; i < n; i++) {
        int l = upper_bound(d.begin(), d.end(), a[i]) - d.begin();
        if (d[l-1] < a[i] && a[i] < d[l])
            d[l] = a[i];
    }

    int ans = 0;
    for (int l = 0; l <= n; l++) {
        if (d[l] < INF)
            ans = l;
    }
    return ans;
}
```

### Khôi phục dãy con

Chúng ta hoàn toàn có thể khôi phục lại dãy con bằng cách tiếp cận này.
Lần này chúng ta cần duy trì hai mảng phụ trợ.
Một mảng cho biết chỉ số thực tế của các phần tử trong $d[]$.
Và một mảng "cha" $p[i]$ như trước.
$p[i]$ sẽ là chỉ số của phần tử đứng trước nó trong dãy con tối ưu kết thúc tại phần tử thứ $i$.

Việc duy trì hai mảng này song song với quá trình tính toán mảng $d[]$ khi duyệt qua mảng $a[]$ là khá đơn giản.
Và cuối cùng việc khôi phục dãy con từ các mảng này cũng không hề phức tạp.

## Giải pháp trong $O(n \log n)$ với cấu trúc dữ liệu {data-toc-label="Giải pháp trong O(n log n) với cấu trúc dữ liệu"}

Thay vì phương pháp trên, chúng ta cũng có thể tính dãy con tăng dài nhất trong $O(n \log n)$ bằng một cách khác: sử dụng một số cấu trúc dữ liệu cơ bản.

Hãy quay lại phương pháp đầu tiên.
Nhớ rằng $d[i]$ bằng giá trị $d[j] + 1$ với $j < i$ và $a[j] < a[i]$.

Do đó, nếu ta định nghĩa thêm một mảng $t[]$ sao cho:

$$t[a[i]] = d[i],$$

thì bài toán tính giá trị $d[i]$ tương đương với việc tìm **giá trị lớn nhất trên tiền tố** của mảng $t[]$:

$$d[i] = \max\left(t[0 \dots a[i] - 1] + 1\right)$$

Bài toán tìm giá trị lớn nhất trên tiền tố của một mảng có sự thay đổi là một bài toán kinh điển có thể giải quyết bằng nhiều cấu trúc dữ liệu khác nhau. 
Ví dụ, chúng ta có thể sử dụng [Cây phân đoạn (Segment Tree)](../data_structures/segment_tree.md) hoặc [Cây Fenwick (BIT)](../data_structures/fenwick.md).

Phương pháp này rõ ràng có một số **nhược điểm**:
về mặt độ dài dòng mã và độ phức tạp cài đặt, cách tiếp cận này sẽ phức tạp hơn phương pháp tìm kiếm nhị phân.
Hơn nữa, nếu các số đầu vào $a[i]$ có giá trị quá lớn, chúng ta cần áp dụng một số kỹ thuật bổ sung như nén số (đánh số lại các phần tử từ $0$ đến $n-1$), hoặc sử dụng cây phân đoạn động (chỉ khởi tạo các nhánh cây thực sự cần thiết).
Nếu không, lượng bộ nhớ tiêu thụ sẽ là cực kỳ lớn.

Bù lại, phương pháp này cũng có những **ưu điểm**:
với cách này, bạn không cần phải suy nghĩ về bất kỳ tính chất đặc biệt nào trong lời giải quy hoạch động.
Và hướng đi này cũng giúp tổng quát hóa bài toán một cách rất dễ dàng (xem bên dưới).

## Các bài toán liên quan

Dưới đây là một số bài toán có liên quan chặt chẽ đến bài toán tìm dãy con tăng dài nhất.

### Dãy con không giảm dài nhất

Đây thực chất gần như là cùng một bài toán.
Chỉ khác là các phần tử bằng nhau được phép xuất hiện trong dãy con.

Lời giải về cơ bản cũng tương tự.
Chúng ta chỉ cần thay đổi dấu so sánh và điều chỉnh lại một chút trong tìm kiếm nhị phân.

### Số lượng dãy con tăng dài nhất

Chúng ta có thể sử dụng phương pháp đầu tiên được thảo luận, hoặc phiên bản $O(n^2)$ hoặc phiên bản sử dụng cấu trúc dữ liệu.
Chúng ta chỉ cần lưu trữ thêm số cách để đạt được dãy con tăng dài nhất kết thúc tại giá trị $d[i]$.

Số cách để tạo thành dãy con tăng dài nhất kết thúc tại $a[i]$ là tổng số cách của tất cả các dãy con tăng dài nhất kết thúc tại $j$ thỏa mãn $d[j]$ đạt cực đại.
Có thể có nhiều vị trí $j$ như vậy, nên chúng ta cần lấy tổng của tất cả chúng.

Sử dụng cây phân đoạn, cách tiếp cận này cũng có thể cài đặt trong $O(n \log n)$.

Chúng ta không thể áp dụng phương pháp tìm kiếm nhị phân cho bài toán này.

### Số lượng dãy con không tăng ít nhất để phủ một dãy số

Cho một mảng có $n$ số $a[0 \dots n - 1]$, chúng ta phải tô màu các số này bằng ít màu nhất sao cho mỗi nhóm màu tạo thành một dãy con không tăng.

Để giải quyết vấn đề này, chúng ta nhận thấy rằng số lượng màu tối thiểu cần thiết bằng đúng độ dài của dãy con tăng dài nhất.

**Chứng minh**:
Chúng ta cần chứng minh **tính đối ngẫu** (duality) của hai bài toán này.

Gọi $x$ là độ dài của dãy con tăng dài nhất và $y$ là số lượng ít nhất các dãy con không tăng dùng để phủ dãy số ban đầu.
Chúng ta cần chứng minh $x = y$.

Rõ ràng trường hợp $y < x$ là không thể xảy ra, vì nếu có $x$ phần tử tăng ngặt, không thể có bất kỳ hai phần tử nào thuộc cùng một dãy con không tăng.
Vì vậy, ta luôn có $y \ge x$.

Bây giờ chúng ta chứng minh $y > x$ là không thể xảy ra bằng phản chứng.
Giả sử $y > x$.
Xét một tập hợp tối ưu gồm $y$ dãy con không tăng.
Chúng ta biến đổi tập hợp này như sau:
nếu tồn tại hai dãy con sao cho dãy thứ nhất bắt đầu trước dãy thứ hai, và phần tử bắt đầu của dãy thứ nhất lớn hơn hoặc bằng phần tử bắt đầu của dãy thứ hai, thì ta chuyển phần tử bắt đầu này sang vị trí bắt đầu của dãy thứ hai.
Sau một số hữu hạn bước, chúng ta sẽ có $y$ dãy con và các phần tử bắt đầu của chúng sẽ tạo thành một dãy con tăng có độ dài $y$.
Vì chúng ta giả sử $y > x$, điều này dẫn đến mâu thuẫn với định nghĩa dãy con tăng dài nhất có độ dài $x$.

Do đó, $y = x$.

**Khôi phục các dãy con**:
Phép phân chia dãy số ban đầu thành các dãy con có thể được thực hiện một cách tham lam (greedy).
Tức là duyệt từ trái qua phải và xếp số hiện tại vào dãy con đang kết thúc bằng phần tử nhỏ nhất thỏa mãn lớn hơn hoặc bằng số hiện tại.

## Bài tập thực hành

- [ACMSGURU - "North-East"](http://codeforces.com/problemsets/acmsguru/problem/99999/521)
- [Codeforces - LCIS](http://codeforces.com/problemset/problem/10/D)
- [Codeforces - Tourist](http://codeforces.com/contest/76/problem/F)
- [SPOJ - DOSA](https://www.spoj.com/problems/DOSA/)
- [SPOJ - HMLIS](https://www.spoj.com/problems/HMLIS/)
- [SPOJ - ONEXLIS](https://www.spoj.com/problems/ONEXLIS/)
- [SPOJ - SUPPER](http://www.spoj.com/problems/SUPPER/)
- [Topcoder - AutoMarket](https://community.topcoder.com/stat?c=problem_statement&pm=3937&rd=6532)
- [Topcoder - BridgeArrangement](https://community.topcoder.com/stat?c=problem_statement&pm=2967&rd=5881)
- [Topcoder - IntegerSequence](https://community.topcoder.com/stat?c=problem_statement&pm=5922&rd=8075)
- [UVA - Back To Edit Distance](https://onlinejudge.org/external/127/12747.pdf)
- [UVA - Happy Birthday](https://onlinejudge.org/external/120/12002.pdf)
- [UVA - Tiling Up Blocks](https://onlinejudge.org/external/11/1196.pdf)
