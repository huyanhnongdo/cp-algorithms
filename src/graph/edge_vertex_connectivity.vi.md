---
tags:
  - Translated
e_maxx_link:
  - rib_connectivity
  - vertex_connectivity
lang: vi
---

# Độ liên thông cạnh / Độ liên thông đỉnh

## Định nghĩa

Cho một đồ thị vô hướng $G$ gồm $n$ đỉnh và $m$ cạnh.
Cả độ liên thông cạnh và độ liên thông đỉnh đều là các đặc trưng mô tả đồ thị này.

### Độ liên thông cạnh

**Độ liên thông cạnh** (edge connectivity) $\lambda$ của đồ thị $G$ là số lượng cạnh tối thiểu cần xóa bỏ để đồ thị $G$ trở nên mất liên thông.

Ví dụ, một đồ thị đã mất liên thông sẵn có độ liên thông cạnh là $0$, một đồ thị liên thông có chứa ít nhất một cầu có độ liên thông cạnh là $1$, và một đồ thị liên thông không chứa cầu nào có độ liên thông cạnh tối thiểu là $2$.

Chúng ta nói tập hợp $S$ các cạnh **phân tách** (separates) hai đỉnh $s$ và $t$ nếu sau khi xóa toàn bộ các cạnh trong $S$ khỏi đồ thị $G$, hai đỉnh $s$ và $t$ nằm ở các thành phần liên thông khác nhau.

Rõ ràng, độ liên thông cạnh của đồ thị bằng kích thước nhỏ nhất của tập hợp phân tách hai đỉnh $s$ và $t$, lấy trên tất cả các cặp đỉnh $(s, t)$ khả dĩ.

### Độ liên thông đỉnh

**Độ liên thông đỉnh** (vertex connectivity) $\kappa$ của đồ thị $G$ là số lượng đỉnh tối thiểu cần xóa bỏ để đồ thị $G$ trở nên mất liên thông.

Ví dụ, một đồ thị mất liên thông sẵn có độ liên thông đỉnh là $0$, và một đồ thị liên thông có đỉnh khớp (articulation point) có độ liên thông đỉnh là $1$.
Chúng ta quy ước đồ thị đầy đủ (complete graph) có độ liên thông đỉnh là $n-1$.
Đối với tất cả các đồ thị khác, độ liên thông đỉnh không vượt quá $n-2$, vì ta luôn có thể tìm thấy một cặp đỉnh không có cạnh nối trực tiếp giữa chúng, và xóa đi $n-2$ đỉnh còn lại.

Chúng ta nói tập hợp $T$ các đỉnh **phân tách** (separates) hai đỉnh $s$ và $t$ nếu sau khi xóa toàn bộ các đỉnh trong $T$ khỏi đồ thị $G$, hai đỉnh này nằm ở các thành phần liên thông khác nhau.

Rõ ràng, độ liên thông đỉnh của đồ thị bằng kích thước nhỏ nhất của tập hợp phân tách hai đỉnh $s$ và $t$, lấy trên tất cả các cặp đỉnh $(s, t)$ khả dĩ.

## Tính chất

### Bất đẳng thức Whitney

**Bất đẳng thức Whitney** (1932) đưa ra mối liên hệ giữa độ liên thông cạnh $\lambda$, độ liên thông đỉnh $\kappa$, và bậc nhỏ nhất của đỉnh bất kỳ trong đồ thị $\delta$:

$$\kappa \le \lambda \le \delta$$

Trực giác là nếu ta có một tập hợp cạnh kích thước $\lambda$ làm đồ thị mất liên thông, ta có thể chọn một trong các đầu mút của mỗi cạnh này để tạo thành một tập hợp đỉnh cũng làm đồ thị mất liên thông.
Và tập hợp đỉnh này có kích thước $\le \lambda$.

Và nếu chúng ta chọn đỉnh có bậc nhỏ nhất $\delta$ rồi xóa mọi cạnh nối với nó, ta cũng thu được một đồ thị mất liên thông.
Do đó bất đẳng thức thứ hai $\lambda \le \delta$ được thỏa mãn.

Một điều thú vị là bất đẳng thức Whitney không thể cải tiến thêm được nữa:
tức là với mọi bộ ba số thỏa mãn bất đẳng thức này, luôn tồn tại ít nhất một đồ thị tương ứng.
Một đồ thị như vậy có thể được dựng theo cách sau:
Đồ thị gồm $2(\delta + 1)$ đỉnh, trong đó $\delta + 1$ đỉnh đầu tiên tạo thành một đồ thị đầy đủ (clique - tất cả các cặp đỉnh được nối với nhau bởi cạnh), và $\delta + 1$ đỉnh tiếp theo tạo thành đồ thị đầy đủ thứ hai.
Ngoài ra, chúng ta nối hai đồ thị đầy đủ này bằng $\lambda$ cạnh, sao cho các cạnh này sử dụng $\lambda$ đỉnh khác nhau ở đồ thị đầy đủ thứ nhất, nhưng chỉ sử dụng $\kappa$ đỉnh ở đồ thị đầy đủ thứ hai.
Đồ thị thu được sẽ có đúng ba đặc trưng thỏa mãn yêu cầu.

### Định lý Ford-Fulkerson

**Định lý Ford-Fulkerson** chỉ ra rằng, số lượng đường đi không giao nhau về cạnh lớn nhất nối hai đỉnh bằng chính số lượng cạnh nhỏ nhất phân tách hai đỉnh này.

## Tính toán giá trị

### Độ liên thông cạnh sử dụng luồng cực đại

Phương pháp này dựa trên định lý Ford-Fulkerson.

Chúng ta duyệt qua tất cả các cặp đỉnh $(s, t)$ và với mỗi cặp, tìm số đường đi không giao nhau về cạnh lớn nhất giữa chúng.
Giá trị này có thể tìm thấy bằng thuật toán luồng cực đại:
chọn $s$ làm nguồn, $t$ làm đích, và gán cho mỗi cạnh của đồ thị một sức chứa bằng $1$.
Khi đó luồng cực đại chính là số đường đi không giao nhau về cạnh.

Độ phức tạp của thuật toán sử dụng [Edmonds-Karp](../graph/edmonds_karp.md) là $O(V^2 V E^2) = O(V^3 E^2)$.
Tuy nhiên ta nên lưu ý rằng đánh giá này chứa một hệ số ẩn, vì trên thực tế không thể tạo ra đồ thị mà thuật toán luồng cực đại chạy chậm trên mọi cặp nguồn và đích.
Đặc biệt, thuật toán sẽ chạy rất nhanh trên các đồ thị ngẫu nhiên.

### Thuật toán chuyên biệt cho độ liên thông cạnh

Nhiệm vụ tìm độ liên thông cạnh tương đương với nhiệm vụ tìm **lát cắt tối thiểu toàn cục** (global minimum cut).

Các thuật toán chuyên biệt đã được phát triển cho bài toán này.
Một trong số đó là [Thuật toán Stoer-Wagner](stoer_wagner_mincut.md), chạy trong thời gian $O(V^3)$ hoặc $O(V E + V^2 \log V)$.

### Độ liên thông đỉnh

Một lần nữa, chúng ta duyệt qua tất cả các cặp đỉnh $s$ và $t$, và với mỗi cặp, tìm số lượng đỉnh tối thiểu để phân tách $s$ và $t$.

Để làm điều này, chúng ta có thể áp dụng cùng cách tiếp cận luồng cực đại như đã mô tả ở các phần trước.

Chúng ta nhân đôi mỗi đỉnh $x$ với $x \neq s$ và $x \neq t$ thành hai đỉnh $x_1$ và $x_2$.
Chúng ta nối hai đỉnh này bằng một cạnh có hướng $(x_1, x_2)$ có sức chứa $1$, và thay thế mọi cạnh $(u, v)$ ban đầu bằng hai cạnh có hướng $(u_2, v_1)$ và $(v_2, u_1)$, cả hai đều có sức chứa là 1.
Khi đó, theo cách dựng, giá trị của luồng cực đại sẽ bằng số lượng đỉnh tối thiểu cần xóa bỏ để phân tách $s$ và $t$.

Cách tiếp cận này có cùng độ phức tạp thời gian giống như cách tiếp cận luồng cực đại để tìm độ liên thông cạnh.
