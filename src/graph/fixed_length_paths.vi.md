---
tags:
  - Translated
e_maxx_link: fixed_length_paths
lang: vi
---

# Số lượng đường đi có độ dài cố định / Đường đi ngắn nhất có độ dài cố định

Bài viết dưới đây mô tả giải pháp cho hai bài toán này dựa trên cùng một ý tưởng:
đưa bài toán về việc dựng ma trận và tính toán kết quả bằng phép nhân ma trận thông thường hoặc phép nhân ma trận được sửa đổi.

## Số lượng đường đi có độ dài cố định

Cho một đồ thị có hướng, không trọng số $G$ gồm $n$ đỉnh và một số nguyên $k$.
Nhiệm vụ là:
với mỗi cặp đỉnh $(i, j)$, chúng ta phải tìm số lượng đường đi có độ dài đúng bằng $k$ giữa hai đỉnh này.
Đường đi không nhất thiết phải là đường đi đơn, tức là các đỉnh và cạnh có thể được ghé thăm nhiều lần trên cùng một đường đi.

Chúng ta giả định rằng đồ thị được biểu diễn bằng ma trận kề, tức là ma trận $G[][]$ kích thước $n \times n$, trong đó mỗi phần tử $G[i][j]$ bằng $1$ nếu đỉnh $i$ có cạnh nối đến $j$, và bằng $0$ nếu ngược lại.
Thuật toán dưới đây cũng hoạt động trong trường hợp đồ thị có đa cạnh:
nếu một cặp đỉnh $(i, j)$ được nối bởi $m$ cạnh, chúng ta có thể ghi nhận điều này trong ma trận kề bằng cách đặt $G[i][j] = m$.
Thuật toán cũng hoạt động nếu đồ thị chứa các khuyên (loop - cạnh nối một đỉnh với chính nó).

Rõ ràng, ma trận kề được dựng chính là câu trả lời cho bài toán trong trường hợp $k = 1$.
Nó chứa số lượng đường đi có độ dài $1$ giữa mỗi cặp đỉnh.

Chúng ta sẽ xây dựng lời giải một cách lặp đi lặp lại:
Giả sử chúng ta đã biết câu trả lời cho một giá trị $k$ nào đó.
Dưới đây mô tả phương pháp để dựng câu trả lời cho $k + 1$.
Ký hiệu $C_k$ là ma trận ứng với trường hợp $k$, và $C_{k+1}$ là ma trận chúng ta muốn dựng.
Với công thức dưới đây, chúng ta có thể tính toán từng phần tử của $C_{k+1}$:

$$C_{k+1}[i][j] = \sum_{p = 1}^{n} C_k[i][p] \cdot G[p][j]$$

Dễ thấy rằng công thức này không tính toán gì khác ngoài tích của hai ma trận $C_k$ và $G$:

$$C_{k+1} = C_k \cdot G$$

Do đó, lời giải của bài toán có thể được biểu diễn như sau:

$$C_k = \underbrace{G \cdot G \cdots G}_{k \text{ lần}} = G^k$$

Công việc còn lại là nhận xét rằng lũy thừa ma trận có thể được tính toán hiệu quả trong thời gian nhanh bằng [Lũy thừa nhị phân](../algebra/binary-exp.md).
Điều này mang lại một giải pháp với độ phức tạp $O(n^3 \log k)$.

## Đường đi ngắn nhất có độ dài cố định

Cho một đồ thị có hướng, có trọng số $G$ gồm $n$ đỉnh và một số nguyên $k$.
Với mỗi cặp đỉnh $(i, j)$, chúng ta phải tìm độ dài của đường đi ngắn nhất giữa $i$ và $j$ gồm chính xác $k$ cạnh.

Chúng ta giả định rằng đồ thị được biểu diễn bằng ma trận kề, tức là qua ma trận $G[][]$ kích thước $n \times n$, trong đó mỗi phần tử $G[i][j]$ chứa độ dài của cạnh đi từ đỉnh $i$ đến đỉnh $j$.
Nếu không có cạnh nối giữa hai đỉnh, phần tử tương ứng của ma trận sẽ được gán giá trị vô cùng $\infty$.

Rõ ràng dưới dạng này, ma trận kề chính là câu trả lời cho bài toán với $k = 1$.
Nó chứa độ dài của các đường đi ngắn nhất gồm đúng một cạnh giữa mỗi cặp đỉnh, hoặc $\infty$ nếu không tồn tại cạnh nối nào giữa chúng.

Một lần nữa, chúng ta có thể xây dựng lời giải một cách lặp đi lặp lại:
Giả sử chúng ta đã biết câu trả lời cho một giá trị $k$ nào đó.
Chúng ta chỉ ra cách tính toán câu trả lời cho $k+1$.
Ký hiệu $L_k$ là ma trận ứng với $k$ và $L_{k+1}$ là ma trận chúng ta muốn dựng.
Khi đó, công thức sau sẽ tính toán từng phần tử của $L_{k+1}$:

$$L_{k+1}[i][j] = \min_{p = 1 \ldots n} \left(L_k[i][p] + G[p][j]\right)$$

Khi nhìn kỹ hơn vào công thức này, chúng ta có thể rút ra một sự tương đồng với phép nhân ma trận:
thực tế ma trận $L_k$ được nhân với ma trận $G$, điểm khác biệt duy nhất là thay vì phép toán nhân ta dùng phép toán cộng, và thay vì phép toán cộng ở vòng ngoài ta lấy giá trị nhỏ nhất làm phép toán tổng hợp.

$$L_{k+1} = L_k \odot G,$$

trong đó phép toán $\odot$ được định nghĩa như sau:

$$A \odot B = C~~\Longleftrightarrow~~C_{i j} = \min_{p = 1 \ldots n}\left(A_{i p} + B_{p j}\right)$$

Do đó, lời giải của bài toán có thể được biểu diễn bằng phép nhân được sửa đổi này:

$$L_k = \underbrace{G \odot \ldots \odot G}_{k~\text{lần}} = G^{\odot k}$$

Công việc còn lại là nhận xét rằng phép tính lũy thừa này cũng có thể được tính toán hiệu quả bằng [Lũy thừa nhị phân](../algebra/binary-exp.md), bởi vì phép nhân sửa đổi này rõ ràng có tính kết hợp (associative).
Vì vậy, giải pháp này cũng có độ phức tạp là $O(n^3 \log k)$.

## Tổng quát hóa bài toán cho các đường đi có độ dài tối đa $k$ {data-toc-label="Tổng quát hóa bài toán cho các đường đi có độ dài tối đa k"}

Các giải pháp trên giải quyết bài toán với một giá trị $k$ cố định.
Tuy nhiên, chúng ta có thể điều chỉnh để giải quyết bài toán cho các đường đi chứa tối đa $k$ cạnh.

Điều này có thể thực hiện bằng cách sửa đổi nhẹ đồ thị đầu vào.

Chúng ta nhân đôi mỗi đỉnh:
với mỗi đỉnh $v$, chúng ta tạo thêm một đỉnh $v'$ và thêm cạnh $(v, v')$ cùng một khuyên $(v', v')$.
Số lượng đường đi giữa $i$ và $j$ chứa tối đa $k$ cạnh bằng chính số lượng đường đi giữa $i$ và $j'$ chứa chính xác $k + 1$ cạnh, bởi vì tồn tại một song ánh ánh xạ mỗi đường đi $[p_0 = i,~p_1,~\dots,~p_{m-1},~p_m = j]$ có độ dài $m \le k$ sang đường đi $[p_0 = i,~p_1,~\dots,~p_{m-1},~p_m = j, j', \dots, j']$ có độ dài đúng bằng $k + 1$.

Mẹo tương tự cũng có thể được áp dụng để tính các đường đi ngắn nhất chứa tối đa $k$ cạnh.
Chúng ta lại nhân đôi mỗi đỉnh và thêm hai cạnh nêu trên với trọng số $0$.
