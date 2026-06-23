---
tags:
  - Translated
e_maxx_link: counting_connected_graphs
lang: vi
---
# Đếm số đồ thị dán nhãn (Labeled graphs)

## Đồ thị dán nhãn

Giả sử số đỉnh trong một đồ thị là $n$.
Chúng ta cần tính số lượng $G_n$ các đồ thị dán nhãn với $n$ đỉnh (dán nhãn có nghĩa là các đỉnh được đánh dấu bằng các số từ $1$ đến $n$).
Các cạnh của đồ thị được xem là vô hướng, đồng thời cấm các khuyên (loop) và cạnh bội (multiple edges).

Chúng ta xem xét tập hợp tất cả các cạnh có thể có của đồ thị.
Với mỗi cạnh $(i, j)$, ta có thể giả định rằng $i < j$ (vì đồ thị là vô hướng và không có khuyên).
Do đó, tập hợp tất cả các cạnh có lực lượng (cardinality) là $\binom{n}{2}$, tức là $\frac{n(n-1)}{2}$.

Vì bất kỳ đồ thị dán nhãn nào cũng được xác định duy nhất bởi các cạnh của nó, số lượng đồ thị dán nhãn với $n$ đỉnh bằng:

$$G_n = 2^{\frac{n(n-1)}{2}}$$

## Đồ thị dán nhãn liên thông

Ở đây, chúng ta bổ sung thêm ràng buộc rằng đồ thị phải liên thông.

Hãy ký hiệu số lượng đồ thị liên thông cần tìm với $n$ đỉnh là $C_n$.

Trước hết, chúng ta sẽ thảo luận về số lượng đồ thị **không liên thông** tồn tại.
Khi đó, số lượng đồ thị liên thông sẽ bằng $G_n$ trừ đi số lượng đồ thị không liên thông.
Hơn nữa, chúng ta sẽ đếm số lượng **đồ thị không liên thông, có gốc**. Một đồ thị có gốc là đồ thị mà chúng ta nhấn mạnh một đỉnh bằng cách dán nhãn nó là gốc.
Rõ ràng là có $n$ khả năng để chọn gốc cho một đồ thị với $n$ đỉnh được dán nhãn, do đó cuối cùng chúng ta sẽ cần chia số lượng đồ thị không liên thông có gốc cho $n$ để có được số lượng đồ thị không liên thông.

Đỉnh gốc sẽ nằm trong một thành phần liên thông có kích thước $1, \dots n-1$.
Có $k \binom{n}{k} C_k G_{n-k}$ đồ thị sao cho đỉnh gốc nằm trong một thành phần liên thông với $k$ đỉnh (có $\binom{n}{k}$ cách để chọn $k$ đỉnh cho thành phần này, chúng được kết nối theo một trong $C_k$ cách, đỉnh gốc có thể là bất kỳ đỉnh nào trong $k$ đỉnh đó, và $n-k$ đỉnh còn lại có thể được kết nối/không kết nối theo bất kỳ cách nào, điều này tạo ra một hệ số $G_{n-k}$).
Do đó, số lượng đồ thị không liên thông với $n$ đỉnh là:

$$\frac{1}{n} \sum_{k=1}^{n-1} k \binom{n}{k} C_k G_{n-k}$$

Và cuối cùng, số lượng đồ thị liên thông là:

$$C_n = G_n - \frac{1}{n} \sum_{k=1}^{n-1} k \binom{n}{k} C_k G_{n-k}$$

## Đồ thị dán nhãn với $k$ thành phần liên thông

Dựa trên công thức từ phần trước, chúng ta sẽ tìm hiểu cách đếm số lượng đồ thị dán nhãn với $n$ đỉnh và $k$ thành phần liên thông.

Số lượng này có thể được tính bằng Quy hoạch động (DP).
Chúng ta sẽ tính $D[i][j]$ - số lượng đồ thị dán nhãn với $i$ đỉnh và $j$ thành phần - cho mỗi $i \le n$ và $j \le k$.

Hãy thảo luận về cách tính phần tử tiếp theo $D[n][k]$ nếu chúng ta đã biết các giá trị trước đó.
Chúng ta sử dụng một cách tiếp cận phổ biến: chọn đỉnh cuối cùng (chỉ số $n$).
Đỉnh này thuộc về một thành phần nào đó.
Nếu kích thước của thành phần này là $s$, thì có $\binom{n-1}{s-1}$ cách để chọn một tập hợp các đỉnh như vậy, và $C_s$ cách để kết nối chúng. Sau khi loại bỏ thành phần này khỏi đồ thị, chúng ta còn lại $n-s$ đỉnh với $k-1$ thành phần liên thông.
Do đó, ta thu được công thức truy hồi sau:

$$D[n][k] = \sum_{s=1}^{n} \binom{n-1}{s-1} C_s D[n-s][k-1]$$