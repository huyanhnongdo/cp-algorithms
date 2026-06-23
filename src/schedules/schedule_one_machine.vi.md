---
tags:
  - Translated
e_maxx_link: johnson_problem_1
lang: vi
---
# Lập lịch công việc trên một máy

Bài toán này nói về việc tìm một lịch trình tối ưu cho $n$ công việc trên một máy duy nhất, nếu công việc $i$ có thể được xử lý trong thời gian $t_i$, nhưng với $t$ giây chờ đợi trước khi xử lý công việc đó, ta phải chịu một mức phạt là $f_i(t)$.

Do đó, bài toán yêu cầu tìm một hoán vị của các công việc sao cho tổng mức phạt là tối thiểu.
Nếu ta ký hiệu $\pi$ là hoán vị của các công việc ($\pi_1$ là phần tử được xử lý đầu tiên, $\pi_2$ là phần tử thứ hai, v.v.), thì tổng mức phạt bằng:

$$F(\pi) = f_{\pi_1}(0) + f_{\pi_2}(t_{\pi_1}) + f_{\pi_3}(t_{\pi_1} + t_{\pi_2}) + \dots + f_{\pi_n}\left(\sum_{i=1}^{n-1} t_{\pi_i}\right)$$

## Các lời giải cho trường hợp đặc biệt

### Hàm phạt tuyến tính

Đầu tiên, chúng ta sẽ giải bài toán trong trường hợp tất cả các hàm phạt $f_i(t)$ đều là tuyến tính, nghĩa là chúng có dạng $f_i(t) = c_i \cdot t$, trong đó $c_i$ là một số không âm.
Lưu ý rằng các hàm này không có hằng số cộng thêm.
Nếu có, chúng ta có thể cộng tất cả các hằng số đó lại và giải quyết bài toán mà không cần xét đến chúng.

Giả sử ta cố định một hoán vị $\pi$ và chọn một chỉ số $i = 1 \dots n-1$.
Gọi hoán vị $\pi'$ bằng với hoán vị $\pi$ nhưng đã hoán đổi hai phần tử $i$ và $i+1$.
Hãy xem mức phạt đã thay đổi như thế nào.

$$F(\pi') - F(\pi) =$$

Dễ thấy rằng các thay đổi chỉ xảy ra ở số hạng thứ $i$ và thứ $(i+1)$:

$$\begin{align}
&= c_{\pi_i'} \cdot \sum_{k = 1}^{i-1} t_{\pi_k'} + c_{\pi_{i+1}'} \cdot \sum_{k = 1}^i t_{\pi_k'} - c_{\pi_i} \cdot \sum_{k = 1}^{i-1} t_{\pi_k} - c_{\pi_{i+1}} \cdot \sum_{k = 1}^i t_{\pi_k} \\
&= c_{\pi_{i+1}} \cdot \sum_{k = 1}^{i-1} t_{\pi_k'} + c_{\pi_i} \cdot \sum_{k = 1}^i t_{\pi_k'} - c_{\pi_i} \cdot \sum_{k = 1}^{i-1} t_{\pi_k} - c_{\pi_{i+1}} \cdot \sum_{k = 1}^i t_{\pi_k} \\
&= c_{\pi_i} \cdot t_{\pi_{i+1}} - c_{\pi_{i+1}} \cdot t_{\pi_i}
\end{align}$$

Dễ thấy rằng, nếu lịch trình $\pi$ là tối ưu, thì bất kỳ thay đổi nào trong đó cũng dẫn đến mức phạt tăng lên (hoặc mức phạt không đổi), do đó đối với lịch trình tối ưu, ta có thể viết ra điều kiện sau:

$$c_{\pi_{i}} \cdot t_{\pi_{i+1}} - c_{\pi_{i+1}} \cdot t_{\pi_i} \ge 0 \quad \forall i = 1 \dots n-1$$

Và sau khi sắp xếp lại, ta được:

$$\frac{c_{\pi_i}}{t_{\pi_i}} \ge \frac{c_{\pi_{i+1}}}{t_{\pi_{i+1}}} \quad \forall i = 1 \dots n-1$$

Như vậy, ta có được **lịch trình tối ưu** bằng cách đơn giản là **sắp xếp** các công việc theo phân số $\frac{c_i}{t_i}$ theo thứ tự không tăng.

Cần lưu ý rằng chúng ta đã xây dựng thuật toán này bằng cái gọi là **phương pháp hoán vị**:
chúng ta thử hoán đổi hai phần tử kề nhau, tính toán xem mức phạt thay đổi bao nhiêu, và sau đó suy ra thuật toán để tìm phương pháp tối ưu.

### Hàm phạt mũ

Giả sử hàm phạt có dạng:

$$f_i(t) = c_i \cdot e^{\alpha \cdot t},$$

trong đó tất cả các số $c_i$ đều không âm và hằng số $\alpha$ là số dương.

Bằng cách áp dụng phương pháp hoán vị, dễ dàng xác định được rằng các công việc phải được sắp xếp theo thứ tự không tăng của giá trị:

$$v_i = \frac{1 - e^{\alpha \cdot t_i}}{c_i}$$

### Hàm phạt đơn điệu đồng nhất

Trong trường hợp này, chúng ta xét trường hợp tất cả các $f_i(t)$ đều bằng nhau và hàm này là hàm đơn điệu tăng.

Rõ ràng là trong trường hợp này, hoán vị tối ưu là sắp xếp các công việc theo thời gian xử lý $t_i$ không giảm.

## Định lý Livshits-Kladov

Định lý Livshits-Kladov xác lập rằng phương pháp hoán vị chỉ áp dụng được cho ba trường hợp nêu trên, cụ thể là:

- Trường hợp tuyến tính: $f_i(t) = c_i(t) + d_i$, trong đó $c_i$ là các hằng số không âm,
- Trường hợp mũ: $f_i(t) = c_i \cdot e_{\alpha \cdot t} + d_i$, trong đó $c_i$ và $\alpha$ là các hằng số dương,
- Trường hợp đồng nhất: $f_i(t) = \phi(t)$, trong đó $\phi$ là một hàm đơn điệu tăng.

Trong tất cả các trường hợp khác, phương pháp này không thể áp dụng được.

Định lý được chứng minh dựa trên giả định rằng các hàm phạt đủ trơn (tồn tại đạo hàm bậc ba).

Trong cả ba trường hợp, chúng ta áp dụng phương pháp hoán vị, qua đó lịch trình tối ưu mong muốn có thể được tìm thấy bằng cách sắp xếp, do đó có độ phức tạp thời gian là $O(n \log n)$.