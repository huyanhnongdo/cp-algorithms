---
tags:
  - Translated
lang: vi
---

# Bài toán cái túi (Knapsack Problem)

Kiến thức chuẩn bị: [Giới thiệu về Quy hoạch động](https://cp-algorithms.com/dynamic_programming/intro-to-dp.html)

## Giới thiệu

Hãy xem xét ví dụ sau đây:

### [[USACO07 Dec] Charm Bracelet](https://www.acmicpc.net/problem/6144)
Có $n$ vật phẩm phân biệt và một cái túi có sức chứa tối đa là $W$. Mỗi vật phẩm $i$ có 2 thuộc tính là trọng lượng ($w_{i}$) và giá trị ($v_{i}$).
Bạn cần chọn một tập hợp con các vật phẩm để cho vào túi sao cho tổng trọng lượng của chúng không vượt quá sức chứa $W$ và tổng giá trị thu được là lớn nhất.

Trong ví dụ trên, mỗi vật phẩm chỉ có hai trạng thái có thể xảy ra (được chọn hoặc không được chọn), tương ứng với các giá trị nhị phân 0 và 1. Do đó, loại bài toán này được gọi là "bài toán cái túi 0-1" (0-1 knapsack problem).

## Bài toán cái túi 0-1 (0-1 Knapsack)

### Giải thích

Trong ví dụ trên, đầu vào của bài toán bao gồm: trọng lượng của vật phẩm thứ $i$ là $w_{i}$, giá trị của vật phẩm thứ $i$ là $v_{i}$, và tổng sức chứa của cái túi là $W$.

Gọi $f_{i, j}$ là trạng thái quy hoạch động biểu thị tổng giá trị lớn nhất mà cái túi có thể chứa với sức chứa tối đa là $j$, khi chúng ta chỉ xem xét chọn lựa trong số $i$ vật phẩm đầu tiên.

Giả sử tất cả các trạng thái của $i-1$ vật phẩm đầu tiên đã được xử lý xong, chúng ta có các lựa chọn nào cho vật phẩm thứ i?

- Khi không cho vật phẩm thứ i vào túi, sức chứa còn lại của túi không đổi và tổng giá trị không đổi. Do đó, giá trị tối đa thu được trong trường hợp này là $f_{i-1, j}$.
- Khi cho vật phẩm thứ i vào túi, sức chứa còn lại của túi giảm đi $w_{i}$ và tổng giá trị tăng thêm $v_{i}$, do đó giá trị tối đa thu được trong trường hợp này là $f_{i-1, j-w_i} + v_i$.

Từ đây, chúng ta rút ra được công thức chuyển trạng thái quy hoạch động:

$$f_{i, j} = \max(f_{i-1, j}, f_{i-1, j-w_i} + v_i)$$

Hơn nữa, nhận thấy rằng hàng trạng thái $f_{i}$ chỉ phụ thuộc trực tiếp vào hàng trạng thái trước đó $f_{i-1}$, do đó chúng ta có thể loại bỏ chiều thứ nhất để tiết kiệm không gian bộ nhớ. Khi đó, quy tắc chuyển trạng thái trở thành:

$$f_j \gets \max(f_j, f_{j-w_i}+v_i)$$

và quy tắc này cần được thực hiện theo thứ tự **giảm dần** của $j$ (để giá trị $f_{j-w_i}$ tương ứng với trạng thái ở bước i-1 là $f_{i-1, j-w_i}$ chứ không phải trạng thái ở bước hiện tại $f_{i, j-w_i}$).

**Hiểu rõ quy tắc chuyển trạng thái này là vô cùng quan trọng, bởi hầu hết các công thức chuyển trạng thái cho các biến thể của bài toán cái túi đều được suy ra theo cách tương tự.**

### Cài đặt

Thuật toán đã mô tả có thể được cài đặt với độ phức tạp thời gian $O(nW)$ như sau:

```.c++
for (int i = 1; i <= n; i++)
  for (int j = W; j >= w[i]; j--)
    f[j] = max(f[j], f[j - w[i]] + v[i]);
```

Một lần nữa, hãy chú ý đến thứ tự thực hiện vòng lặp của biến `j`. Thứ tự này cần được tuân thủ nghiêm ngặt để đảm bảo tính chất sau: Ngay trước khi trạng thái $(i, j)$ được xử lý, phần tử $f_k$ tương ứng với $f_{i,k}$ đối với mọi $k > j$, nhưng tương ứng với $f_{i-1,k}$ đối với mọi $k < j$. Điều này đảm bảo rằng giá trị $f_{j-w_i}$ luôn được lấy từ bước thứ $(i-1)$ chứ không phải từ bước thứ $i$ hiện tại.

## Bài toán cái túi không giới hạn số lượng (Complete Knapsack)

Mô hình bài toán cái túi không giới hạn số lượng (Complete Knapsack) tương tự như bài toán cái túi 0-1, điểm khác biệt duy nhất là mỗi vật phẩm có thể được chọn với số lượng không giới hạn thay vì chỉ tối đa một lần.

Chúng ta có thể tham khảo ý tưởng của bài toán cái túi 0-1 để định nghĩa trạng thái: $f_{i, j}$ là giá trị lớn nhất mà cái túi có thể đạt được khi chọn trong số $i$ vật phẩm đầu tiên với sức chứa tối đa là $j$.

Mặc dù định nghĩa trạng thái tương tự như bài toán cái túi 0-1, nhưng quy tắc chuyển trạng thái của nó sẽ có sự khác biệt.

### Giải thích

Cách tiếp cận ngây thơ là đối với mỗi vật phẩm thứ $i$, chúng ta duyệt qua tất cả số lần có thể chọn vật phẩm đó. Độ phức tạp thời gian của cách này là $O(n^2W)$.

Công thức chuyển trạng thái tương ứng là:

$$f_{i, j} = \max\limits_{k=0}^{\infty}(f_{i-1, j-k\cdot w_i} + k\cdot v_i)$$

Tuy nhiên, công thức trên có thể được rút gọn thành một phương trình chuyển trạng thái phẳng và trực tiếp hơn:

$$f_{i, j} = \max(f_{i-1, j}, f_{i, j-w_i} + v_i)$$

Lý do công thức này hoạt động chính xác là vì trạng thái $f_{i, j-w_i}$ đã được cập nhật từ trước bởi trạng thái $f_{i, j-2\cdot w_i}$, v.v.

Tương tự như bài toán cái túi 0-1, chúng ta có thể loại bỏ chiều thứ nhất để tối ưu hóa không gian bộ nhớ. Công thức chuyển trạng thái thu được giống hệt bài toán cái túi 0-1:

$$f_j \gets \max(f_j, f_{j-w_i}+v_i)$$

### Cài đặt

Thuật toán có thể được cài đặt trong thời gian $O(nW)$ như sau:

```.c++
for (int i = 1; i <= n; i++)
  for (int j = w[i]; j <= W; j++)
    f[j] = max(f[j], f[j - w[i]] + v[i]);
```

Mặc dù có chung quy tắc chuyển trạng thái dạng thu gọn, nhưng đoạn mã ở trên sẽ chạy sai đối với bài toán cái túi 0-1.

Quan sát kỹ đoạn mã, chúng ta thấy rằng đối với vật phẩm $i$ đang xử lý và trạng thái hiện tại $f_{i, j}$, khi $j \ge w_i$, giá trị $f_{i, j}$ sẽ bị ảnh hưởng bởi giá trị $f_{i, j-w_i}$ (vốn đã được cập nhật ở bước hiện tại). Điều này tương đương với việc cho phép vật phẩm i được bỏ vào túi nhiều lần, hoàn toàn khớp với yêu cầu của bài toán cái túi không giới hạn số lượng và không đúng với bài toán cái túi 0-1.

## Bài toán cái túi giới hạn số lượng (Multiple Knapsack)

Bài toán cái túi giới hạn số lượng (Multiple Knapsack) cũng là một biến thể của bài toán cái túi 0-1. Điểm khác biệt chính là mỗi vật phẩm thứ $i$ có số lượng giới hạn là $k_i$ chiếc thay vì chỉ có đúng $1$ chiếc.

### Giải thích

Một ý tưởng rất đơn giản là: "chọn vật phẩm i tối đa $k_i$ lần" tương đương với việc "coi $k_i$ vật phẩm giống nhau này là các vật phẩm riêng biệt và chọn lần lượt từng chiếc". Từ đó chúng ta đưa bài toán về mô hình cái túi 0-1 thông thường, mô tả bởi công thức chuyển trạng thái:

$$f_{i, j} = \max_{k=0}^{k_i}(f_{i-1,j-k\cdot w_i} + k\cdot v_i)$$

Độ phức tạp thời gian của quá trình này là $O(W\sum\limits_{i=1}^{n}k_i)$.

### Tối ưu hóa bằng phân tách nhị phân (Binary Grouping Optimization)

Chúng ta tiếp tục xem xét việc chuyển đổi bài toán cái túi giới hạn số lượng thành bài toán cái túi 0-1 để tìm cách tối ưu. Độ phức tạp thời gian theo sức chứa $O(Wn)$ không thể tối ưu thêm bằng cách tiếp cận ở trên, vì vậy chúng ta tập trung tối ưu hóa thành phần $O(\sum k_i)$.

Gọi $A_{i, j}$ là vật phẩm thứ j được phân tách ra từ vật phẩm thứ i. Trong cách tiếp cận ngây thơ ở trên, $A_{i, j}$ đại diện cho cùng một vật phẩm với mọi $j \le k_i$. Lý do chính khiến hiệu năng thấp là vì chúng ta thực hiện rất nhiều công việc lặp đi lặp lại. Ví dụ, việc chọn tập hợp $\{A_{i, 1}, A_{i, 2}\}$ và chọn tập hợp $\{A_{i, 2}, A_{i, 3}\}$ là hoàn toàn tương đương nhau về mặt giá trị và trọng lượng. Do đó, việc tối ưu hóa cách phân tách vật phẩm sẽ giúp giảm đáng kể độ phức tạp thời gian.

Việc gom nhóm vật phẩm có thể thực hiện hiệu quả bằng cách sử dụng phân tách nhị phân.

Cụ thể, nhóm $A_{i, j}$ sẽ chứa lượng vật phẩm bằng $2^j$ lần vật phẩm gốc ($j\in[0,\lfloor \log_2(k_i+1)\rfloor-1]$). Nếu $k_i + 1$ không phải là một lũy thừa nguyên của $2$, một nhóm cuối cùng có kích thước bằng $k_i-(2^{\lfloor \log_2(k_i+1)\rfloor}-1)$ sẽ được thêm vào để bù cho đủ số lượng $k_i$.

Thông qua cách phân tách trên, chúng ta có thể tạo ra bất kỳ số lượng vật phẩm nào $\le k_i$ bằng cách chọn một số nhóm thích hợp trong số các nhóm $A_{i, j}$. Sau khi phân tách tất cả các vật phẩm theo cách này, chúng ta chỉ cần áp dụng thuật toán cái túi 0-1 thông thường để giải quyết bài toán mới.

Tối ưu hóa này mang lại độ phức tạp thời gian là $O(W\sum\limits_{i=1}^{n}\log k_i)$.

### Cài đặt

```c++
index = 0;
for (int i = 1; i <= n; i++) {
  int c = 1, p, h, k;
  cin >> p >> h >> k;
  while (k > c) {
    k -= c;
    list[++index].w = c * p;
    list[index].v = c * h;
    c *= 2;
  }
  list[++index].w = p * k;
  list[index].v = h * k;
}
```

### Tối ưu hóa bằng hàng đợi đơn điệu (Monotone Queue Optimization)

Trong tối ưu hóa này, mục tiêu của chúng ta là đưa bài toán cái túi về bài toán [hàng đợi cực đại](https://cp-algorithms.com/data_structures/stack_queue_modification.html).

Để thuận tiện cho việc mô tả, đặt $g_{x, y} = f_{i, x \cdot w_i + y} ,\space g'_{x, y} = f_{i-1, x \cdot w_i + y}$. Khi đó, quy tắc chuyển trạng thái có thể viết dưới dạng:

$$g_{x, y} = \max_{k=0}^{k_i}(g'_{x-k, y} + v_i \cdot k)$$

Tiếp tục đặt $G_{x, y} = g'_{x, y} - v_i \cdot x$. Quy tắc chuyển trạng thái có thể biểu diễn lại thành:

$$g_{x, y} \gets \max_{k=0}^{k_i}(G_{x-k, y}) + v_i \cdot x$$

Biểu thức này đã chuyển về dạng tối ưu hóa bằng hàng đợi đơn điệu kinh điển. Giá trị $G_{x, y}$ có thể tính được trong thời gian $O(1)$, vì vậy với mỗi giá trị $y$ cố định, chúng ta có thể tính toán $g_{x, y}$ trong thời gian $O(\lfloor \frac{W}{w_i} \rfloor)$.
Do đó, độ phức tạp để tìm tất cả các giá trị $g_{x, y}$ là $O(\lfloor \frac{W}{w_i} \rfloor) \times O(w_i) = O(W)$.
Nhờ phương pháp này, tổng độ phức tạp của thuật toán giảm xuống chỉ còn $O(nW)$.

## Bài toán cái túi hỗn hợp (Mixed Knapsack)

Bài toán cái túi hỗn hợp (Mixed Knapsack) là sự kết hợp của cả ba bài toán đã mô tả ở trên. Nghĩa là, một số vật phẩm chỉ có thể chọn đúng một lần (0-1 knapsack), một số có thể chọn không giới hạn số lượng (complete knapsack), và một số chỉ có thể chọn tối đa $k$ lần (multiple knapsack).

Bài toán nhìn có vẻ phức tạp, nhưng chỉ cần bạn hiểu rõ ý tưởng cốt lõi của các bài toán cái túi trước đó và kết hợp mã nguồn của chúng lại với nhau là có thể giải quyết được. Đoạn mã giả cho giải pháp như sau:

```c++
for (each item) {
  if (0-1 knapsack)
    Apply 0-1 knapsack code;
  else if (complete knapsack)
    Apply complete knapsack code;
  else if (multiple knapsack)
    Apply multiple knapsack code;
}
```

## Bài tập áp dụng

- [Atcoder: Knapsack-1](https://atcoder.jp/contests/dp/tasks/dp_d)
- [Atcoder: Knapsack-2](https://atcoder.jp/contests/dp/tasks/dp_e)
- [LeetCode - 494. Target Sum](https://leetcode.com/problems/target-sum)
- [LeetCode - 416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)
- [CSES: Book Shop II](https://cses.fi/problemset/task/1159)
- [DMOJ: Knapsack-3](https://dmoj.ca/problem/knapsack)
- [DMOJ: Knapsack-4](https://dmoj.ca/problem/knapsack4)
