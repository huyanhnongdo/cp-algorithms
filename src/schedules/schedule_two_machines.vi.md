---
tags:
  - Translated
e_maxx_link: johnson_problem_2
lang: vi
---
# Lập lịch công việc trên hai máy

Bài toán này nói về việc tìm một lịch trình tối ưu cho $n$ công việc trên hai máy.
Mỗi công việc trước tiên phải được xử lý trên máy thứ nhất, và sau đó là trên máy thứ hai.
Công việc thứ $i$ tốn $a_i$ thời gian trên máy thứ nhất, và $b_i$ thời gian trên máy thứ hai.
Mỗi máy chỉ có thể xử lý một công việc tại một thời điểm.

Chúng ta muốn tìm thứ tự tối ưu của các công việc sao cho tổng thời gian xử lý hoàn tất là nhỏ nhất có thể.

Lời giải được thảo luận ở đây được gọi là quy tắc Johnson (đặt theo tên của S. M. Johnson).

Cần lưu ý rằng bài toán trở nên NP-đầy đủ (NP-complete) nếu chúng ta có nhiều hơn hai máy.

## Xây dựng thuật toán

Trước hết, hãy lưu ý rằng chúng ta có thể giả định thứ tự các công việc trên máy thứ nhất và máy thứ hai phải trùng khớp nhau.
Thực tế, vì các công việc trên máy thứ hai chỉ sẵn sàng sau khi đã xử lý xong ở máy thứ nhất, và nếu có nhiều công việc sẵn sàng cho máy thứ hai, thì tổng thời gian xử lý vẫn sẽ bằng tổng $b_i$ của chúng, bất kể thứ tự của chúng là gì.
Do đó, chỉ có lợi khi gửi các công việc đến máy thứ hai theo cùng thứ tự mà chúng ta gửi đến máy thứ nhất.

Xét thứ tự các công việc trùng với thứ tự đầu vào $1, 2, \dots, n$.

Chúng ta ký hiệu $x_i$ là **thời gian nhàn rỗi** của máy thứ hai ngay trước khi xử lý công việc $i$.
Mục tiêu của chúng ta là **giảm thiểu tổng thời gian nhàn rỗi**:

$$F(x) = \sum x_i ~ \rightarrow \min$$

Với công việc đầu tiên, ta có $x_1 = a_1$.
Với công việc thứ hai, vì nó được gửi đến máy vào thời điểm $a_1 + a_2$, và máy thứ hai rảnh vào thời điểm $x_1 + b_1$, ta có $x_2 = \max\left((a_1 + a_2) - (x_1 + b_1), 0\right)$.
Tổng quát hơn, ta có phương trình:

$$x_k = \max\left(\sum_{i=1}^k a_i - \sum_{i=1}^{k-1} b_i - \sum_{i=1}^{k-1} x_i, 0 \right)$$

Bây giờ ta có thể tính **tổng thời gian nhàn rỗi** $F(x)$.
Có khẳng định rằng nó có dạng:

$$F(x) = \max_{k=1 \dots n} K_i,$$

trong đó:

$$K_i = \sum_{i=1}^k a_i - \sum_{i=1}^{k-1} b_i.$$

Điều này có thể dễ dàng kiểm chứng bằng phương pháp quy nạp.

Bây giờ chúng ta sử dụng **phương pháp hoán vị**:
chúng ta sẽ tráo đổi hai công việc kề nhau $j$ và $j+1$ và xem xét sự thay đổi của tổng thời gian nhàn rỗi.

Dựa trên dạng biểu thức của $K_i$, rõ ràng là chỉ có $K_j$ và $K_{j+1}$ thay đổi, ta ký hiệu các giá trị mới của chúng là $K_j'$ và $K_{j+1}'$.

Nếu sự thay đổi thứ tự của các công việc $j$ và $j+1$ làm tăng tổng thời gian nhàn rỗi, thì điều kiện sau phải xảy ra:

$$\max(K_j, K_{j+1}) \le \max(K_j', K_{j+1}')$$

(Việc tráo đổi hai công việc cũng có thể không gây ra ảnh hưởng gì. Điều kiện trên chỉ là điều kiện đủ, chứ không phải điều kiện cần.)

Sau khi lược bỏ $\sum_{i=1}^{j+1} a_i - \sum_{i=1}^{j-1} b_i$ từ cả hai vế của bất đẳng thức, ta nhận được:

$$\max(-a_{j+1}, -b_j) \le \max(-b_{j+1}, -a_j)$$

Và sau khi loại bỏ các dấu âm:

$$\min(a_j, b_{j+1}) \le \min(b_j, a_{j+1})$$

Như vậy, chúng ta đã có được một **bộ so sánh (comparator)**:
bằng cách sắp xếp các công việc dựa trên nó, chúng ta thu được thứ tự tối ưu của các công việc mà tại đó không có hai công việc nào có thể tráo đổi để cải thiện thời gian hoàn tất.

Tuy nhiên, bạn có thể **đơn giản hóa** việc sắp xếp hơn nữa nếu nhìn bộ so sánh từ một góc độ khác.
Bộ so sánh có thể được hiểu theo cách sau:
Nếu ta có bốn khoảng thời gian $(a_j, a_{j+1}, b_j, b_{j+1})$, và giá trị nhỏ nhất trong số đó là thời gian tương ứng với máy thứ nhất, thì công việc tương ứng nên được thực hiện trước.
Nếu thời gian nhỏ nhất là thời gian từ máy thứ hai, thì nó nên được thực hiện sau.
Như vậy, chúng ta có thể sắp xếp các công việc bằng $\min(a_i, b_i)$, và nếu thời gian xử lý của công việc hiện tại trên máy thứ nhất nhỏ hơn thời gian xử lý trên máy thứ hai, thì công việc này phải được thực hiện trước tất cả các công việc còn lại, ngược lại thì thực hiện sau tất cả các công việc còn lại.

Dù thế nào đi nữa, hóa ra là với quy tắc Johnson, chúng ta có thể giải bài toán bằng cách sắp xếp các công việc, từ đó đạt được độ phức tạp thời gian là $O(n \log n)$.

## Cài đặt

Tại đây chúng ta cài đặt biến thể thứ hai của thuật toán đã mô tả.

```{.cpp file=johnsons_rule}
struct Job {
    int a, b, idx;

    bool operator<(Job o) const {
        return min(a, b) < min(o.a, o.b);
    }
};

vector<Job> johnsons_rule(vector<Job> jobs) {
    sort(jobs.begin(), jobs.end());
    vector<Job> a, b;
    for (Job j : jobs) {
        if (j.a < j.b)
            a.push_back(j);
        else
            b.push_back(j);
    }
    a.insert(a.end(), b.rbegin(), b.rend());
    return a;
}

pair<int, int> finish_times(vector<Job> const& jobs) {
    int t1 = 0, t2 = 0;
    for (Job j : jobs) {
        t1 += j.a;
        t2 = max(t2, t1) + j.b;
    }
    return make_pair(t1, t2);
}
```

Tất cả thông tin về mỗi công việc được lưu trữ trong một `struct`.
Hàm đầu tiên sắp xếp tất cả các công việc và tính toán lịch trình tối ưu.
Hàm thứ hai tính toán thời gian hoàn tất của cả hai máy khi đã có một lịch trình cụ thể.