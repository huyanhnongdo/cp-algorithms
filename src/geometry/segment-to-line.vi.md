---
tags:
  - Translated
e_maxx_link: segment_to_line
lang: vi
---
# Tìm phương trình đường thẳng cho một đoạn thẳng

Nhiệm vụ là: cho trước tọa độ các điểm mút của một đoạn thẳng, xây dựng một đường thẳng đi qua đoạn thẳng đó.

Chúng ta giả sử rằng đoạn thẳng là không suy biến, tức là có độ dài lớn hơn không (nếu không, tất nhiên là có vô số đường thẳng khác nhau đi qua nó).

### Trường hợp hai chiều

Cho đoạn thẳng đã cho là $PQ$ tức là tọa độ đã biết của các điểm mút của nó $P_x , P_y , Q_x , Q_y$ .

Cần phải xây dựng **phương trình của một đường thẳng trong mặt phẳng** đi qua đoạn thẳng này, tức là tìm các hệ số $A , B , C$ trong phương trình của đường thẳng:

$$A x + B y + C = 0.$$

Lưu ý rằng đối với các bộ ba cần thiết $(A, B, C)$ có **vô số** nghiệm mô tả đoạn thẳng đã cho: bạn có thể nhân cả ba hệ số với một số khác không tùy ý và nhận được cùng một đường thẳng. Do đó, nhiệm vụ của chúng ta là tìm một trong các bộ ba này.

Dễ dàng kiểm chứng (bằng cách thay thế các biểu thức này và tọa độ các điểm $P$ và $Q$ vào phương trình của đường thẳng) rằng bộ hệ số sau đây là phù hợp:

$$\begin{align}
A &= P_y - Q_y, \\
B &= Q_x - P_x, \\
C &= - A P_x - B P_y.
\end{align}$$

### Trường hợp số nguyên

Một ưu điểm quan trọng của phương pháp xây dựng đường thẳng này là nếu tọa độ các điểm mút là số nguyên, thì các hệ số thu được cũng sẽ là **số nguyên**. Trong một số trường hợp, điều này cho phép thực hiện các phép toán hình học mà không cần dùng đến số thực.

Tuy nhiên, có một nhược điểm nhỏ: đối với cùng một đường thẳng, có thể thu được các bộ ba hệ số khác nhau. Để tránh điều này, nhưng vẫn giữ các hệ số nguyên, bạn có thể áp dụng kỹ thuật sau, thường được gọi là **chuẩn hóa** (rationing). Tìm [GCD (Ước chung lớn nhất)](../algebra/euclid-algorithm.md) của các số $| A | , | B | , | C |$ , chúng ta chia cả ba hệ số cho nó, và sau đó chúng ta thực hiện chuẩn hóa dấu: nếu $A <0$ hoặc $A = 0, B <0$ thì nhân cả ba hệ số với $-1$ . Kết quả là, chúng ta sẽ đi đến kết luận rằng đối với các đường thẳng trùng nhau, sẽ thu được các bộ ba hệ số giống hệt nhau, điều này giúp dễ dàng kiểm tra sự bằng nhau của các đường thẳng.

### Trường hợp số thực

Khi làm việc với số thực, bạn nên luôn nhận thức về các sai số.

Các hệ số $A$ và $B$ sẽ có cùng bậc với tọa độ gốc, hệ số $C$ có bậc là bình phương của chúng. Điều này có thể tạo ra các số khá lớn, và, ví dụ, khi chúng ta [giao cắt các đường thẳng](lines-intersection.md), chúng sẽ trở nên lớn hơn nữa, điều này có thể dẫn đến sai số làm tròn lớn ngay cả khi tọa độ các điểm mút có bậc $10^3$.

Do đó, khi làm việc với số thực, nên thực hiện cái gọi là **chuẩn hóa** (normalization), điều này rất đơn giản: đó là làm cho các hệ số sao cho $A ^ 2 + B ^ 2 = 1$ . Để làm điều này, tính toán số $Z$ :

$$Z = \sqrt{A ^ 2 + B ^ 2},$$

và chia cả ba hệ số $A , B , C$ cho nó.

Như vậy, bậc của các hệ số $A$ và $B$ sẽ không phụ thuộc vào bậc của các tọa độ đầu vào, và hệ số $C$ sẽ có cùng bậc với tọa độ đầu vào. Trong thực tế, điều này dẫn đến cải thiện đáng kể độ chính xác của các phép tính.

Cuối cùng, chúng ta đề cập đến việc **so sánh** các đường thẳng - trên thực tế, sau khi chuẩn hóa như vậy, đối với cùng một đường thẳng, chỉ có thể thu được hai bộ ba hệ số: sai khác một phép nhân với $-1$. Theo đó, nếu chúng ta thực hiện chuẩn hóa bổ sung có tính đến dấu (nếu $A < -\varepsilon$ hoặc $| A | < \varepsilon$, $B <- \varepsilon$ thì nhân với $-1$ ), các hệ số thu được sẽ là duy nhất.

### Trường hợp ba chiều và đa chiều

Ngay cả trong trường hợp ba chiều cũng không có **phương trình đơn giản** nào mô tả một đường thẳng (nó có thể được định nghĩa là giao của hai mặt phẳng, tức là một hệ hai phương trình, nhưng đây là một phương pháp bất tiện).

Do đó, trong các trường hợp ba chiều và đa chiều, chúng ta phải sử dụng **phương pháp tham số để định nghĩa một đường thẳng** (parametric method of defining a straight line), tức là dưới dạng một điểm $p$ và một vector $v$ :

$$p + v t, ~~~ t \in \mathbb{R}.$$

Tức là một đường thẳng là tất cả các điểm có thể thu được từ một điểm $p$ bằng cách cộng một vector $v$ với một hệ số tùy ý.

Việc **xây dựng** một đường thẳng dưới dạng tham số theo tọa độ các điểm mút của một đoạn thẳng là đơn giản, chúng ta chỉ cần lấy một điểm mút của đoạn thẳng làm điểm $p$, và vector từ điểm mút thứ nhất đến điểm mút thứ hai làm vector $v$.