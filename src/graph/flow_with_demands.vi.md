---
tags:
  - Translated
e_maxx_link: flow_with_limits
lang: vi
---

# Luồng với yêu cầu biên dưới

Trong một mạng luồng thông thường, luồng trên mỗi cạnh chỉ bị chặn trên bởi sức chứa $c(e)$ và chặn dưới bởi 0.
Trong bài viết này, chúng ta sẽ thảo luận về mạng luồng trong đó yêu cầu bổ sung là luồng trên mỗi cạnh phải đạt một lượng nhất định, nghĩa là chúng ta chặn dưới luồng của mỗi cạnh bởi một hàm **yêu cầu biên dưới** (demand) $d(e)$:

$$ d(e) \le f(e) \le c(e)$$

Như vậy, mỗi cạnh có một giá trị luồng tối thiểu mà chúng ta bắt buộc phải truyền qua cạnh đó.

Đây là một bài toán tổng quát hóa của bài toán luồng thông thường, vì nếu đặt $d(e) = 0$ cho tất cả các cạnh $e$, ta sẽ thu được một mạng luồng thông thường.
Lưu ý rằng trong mạng luồng thông thường, việc tìm một luồng hợp lệ là vô cùng đơn giản: chỉ cần đặt $f(e) = 0$ là đã có một luồng hợp lệ.
Tuy nhiên, nếu luồng trên mỗi cạnh phải thỏa mãn yêu cầu biên dưới, thì việc tìm một luồng hợp lệ đã trở nên khá phức tạp.

Chúng ta sẽ xem xét hai bài toán:

1. Tìm một luồng hợp lệ bất kỳ thỏa mãn tất cả các ràng buộc.
2. Tìm một luồng nhỏ nhất (cực tiểu) thỏa mãn tất cả các ràng buộc.

## Tìm một luồng hợp lệ bất kỳ

Chúng ta thực hiện các thay đổi sau trên mạng luồng.
Chúng ta thêm một nguồn mới $s'$ và một đích mới $t'$, một cạnh mới đi từ nguồn mới $s'$ đến mọi đỉnh khác, một cạnh mới đi từ mọi đỉnh đến đích mới $t'$, và một cạnh đi từ đích cũ $t$ đến nguồn cũ $s$.
Ngoài ra, chúng ta định nghĩa hàm sức chứa mới $c'$ như sau:

- $c'((s', v)) = \sum_{u \in V} d((u, v))$ cho mỗi cạnh $(s', v)$.
- $c'((v, t')) = \sum_{w \in V} d((v, w))$ cho mỗi cạnh $(v, t')$.
- $c'((u, v)) = c((u, v)) - d((u, v))$ cho mỗi cạnh $(u, v)$ trong mạng cũ.
- $c'((t, s)) = \infty$

Nếu mạng mới có một luồng bão hòa (một luồng mà mỗi cạnh đi ra từ $s'$ đều được lấp đầy hoàn toàn, tương đương với mọi cạnh đi vào $t'$ đều được lấp đầy hoàn toàn), thì mạng với yêu cầu biên dưới ban đầu có một luồng hợp lệ, và luồng thực tế có thể dễ dàng được dựng lại từ mạng mới này.
Ngược lại, nếu không, thì không tồn tại luồng nào thỏa mãn tất cả các điều kiện.
Vì luồng bão hòa phải là luồng cực đại, nó có thể được tìm thấy bằng bất kỳ thuật toán luồng cực đại nào, chẳng hạn như [Thuật toán Edmonds-Karp](edmonds_karp.md) hoặc [Thuật toán Push-relabel](push-relabel.md).

Tính đúng đắn của những phép biến đổi này khó hiểu hơn một chút.
Chúng ta có thể suy nghĩ theo cách sau:
Mỗi cạnh $e = (u, v)$ có $d(e) > 0$ ban đầu được thay thế bằng hai cạnh: một cạnh có sức chứa $d(e)$, và cạnh kia có sức chứa $c(e) - d(e)$.
Chúng ta muốn tìm một luồng làm bão hòa cạnh thứ nhất (nghĩa là luồng trên cạnh này phải bằng sức chứa của nó).
Cạnh thứ hai ít quan trọng hơn - luồng trên nó có thể là bất kỳ giá trị nào, miễn là không vượt quá sức chứa.
Xét mỗi cạnh cần được làm bão hòa, chúng ta thực hiện thao tác sau:
vẽ cạnh đi từ nguồn mới $s'$ đến điểm cuối $v$ của nó, vẽ cạnh đi từ điểm đầu $u$ của nó đến đích mới $t'$, loại bỏ chính cạnh đó, và vẽ một cạnh có sức chứa vô hạn từ đích cũ $t$ đến nguồn cũ $s$.
Bằng các hành động này, chúng ta mô phỏng việc cạnh này bị bão hòa - từ $v$ sẽ có thêm một lượng luồng $d(e)$ đi ra (chúng ta mô phỏng nó bằng một nguồn mới cung cấp đúng lượng luồng này cho $v$), và $u$ cũng sẽ đẩy thêm một lượng luồng $d(e)$ (nhưng thay vì đi dọc theo cạnh cũ, lượng luồng này sẽ đi trực tiếp đến đích mới $t'$).
Một luồng có giá trị $d(e)$, vốn chảy dọc theo đường đi cũ $s - \dots - u - v - \dots - t$, nay có thể đi theo đường đi mới $s' - v - \dots - t - s - \dots - u - t'$.
Điều duy nhất được đơn giản hóa trong định nghĩa của mạng mới là nếu quy trình trên tạo ra nhiều cạnh giữa cùng một cặp đỉnh, chúng sẽ được gộp lại thành một cạnh duy nhất với sức chứa bằng tổng sức chứa của chúng.

## Luồng cực tiểu

Lưu ý rằng dọc theo cạnh $(t, s)$ (từ đích cũ đến nguồn cũ) với sức chứa $\infty$ sẽ truyền toàn bộ lượng luồng của mạng cũ tương ứng.
Nghĩa là sức chứa của cạnh này ảnh hưởng đến giá trị luồng của mạng cũ.
Bằng cách gán cho cạnh này một sức chứa đủ lớn (tức là $\infty$), luồng của mạng cũ là không giới hạn.
Bằng cách giới hạn cạnh này bằng các sức chứa nhỏ hơn, giá trị luồng thu được sẽ giảm đi.
Tuy nhiên, nếu chúng ta giới hạn cạnh này bởi một giá trị quá nhỏ, thì mạng mới sẽ không có lời giải bão hòa, nghĩa là lời giải tương ứng cho mạng ban đầu sẽ không thỏa mãn yêu cầu biên dưới của các cạnh.
Rõ ràng, ở đây chúng ta có thể sử dụng tìm kiếm nhị phân (binary search) để tìm ra giá trị nhỏ nhất mà tại đó tất cả các ràng buộc vẫn được thỏa mãn.
Điều này mang lại luồng cực tiểu của mạng ban đầu.
