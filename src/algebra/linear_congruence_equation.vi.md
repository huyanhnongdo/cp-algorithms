---
tags:
  - Translated
e_maxx_link: diofant_1_equation
lang: vi
---

# Phương trình đồng dư tuyến tính (Linear Congruence Equation)

Phương trình này có dạng như sau:

$$a \cdot x \equiv b \pmod n,$$

trong đó $a$, $b$ và $n$ là các số nguyên cho trước và $x$ là số nguyên chưa biết.

Nhiệm vụ của chúng ta là tìm giá trị $x$ nằm trong đoạn $[0, n-1]$ (rõ ràng, trên toàn bộ trục số có thể có vô số nghiệm và chúng khác nhau một lượng là bội của $n$, tức là $n \cdot k$ với $k$ là số nguyên bất kỳ). Nếu nghiệm của phương trình không phải là duy nhất, chúng ta cũng sẽ xem xét cách tìm tất cả các nghiệm đó.

## Giải bằng cách tìm phần tử nghịch đảo

Trước tiên, hãy xét trường hợp đơn giản khi $a$ và $n$ **nguyên tố cùng nhau** ($\gcd(a, n) = 1$).
Khi đó ta có thể tìm [phần tử nghịch đảo mô-đun](module-inverse.md) của $a$. Nhân cả hai vế của phương trình với nghịch đảo đó, ta sẽ nhận được một nghiệm **duy nhất**:

$$x \equiv b \cdot a ^ {- 1} \pmod n$$

Bây giờ hãy xét trường hợp $a$ và $n$ **không nguyên tố cùng nhau** ($\gcd(a, n) \ne 1$).
Khi đó phương trình không phải lúc nào cũng có nghiệm (ví dụ $2 \cdot x \equiv 1 \pmod 4$ vô nghiệm).

Gọi $g = \gcd(a, n)$, tức là [ước chung lớn nhất](euclid-algorithm.md) của $a$ và $n$ (trong trường hợp này lớn hơn 1).

Nếu $b$ không chia hết cho $g$, phương trình sẽ vô nghiệm. Thực chất, với mọi $x$, vế trái của phương trình $a \cdot x \pmod n$ luôn chia hết cho $g$, trong khi vế phải không chia hết cho $g$, do đó suy ra phương trình không có nghiệm.

Nếu $g$ chia hết cho $b$, thì bằng cách chia cả hai vế của phương trình (tức là chia cả $a$, $b$ và $n$) cho $g$, ta thu được một phương trình mới:

$$a^\prime \cdot x \equiv b^\prime \pmod{n^\prime}$$

trong đó $a^\prime$ và $n^\prime$ đã nguyên tố cùng nhau, và chúng ta đã biết cách giải phương trình dạng này.
Gọi nghiệm tìm được của phương trình mới là $x^\prime$.

Rõ ràng $x^\prime$ này cũng sẽ là một nghiệm của phương trình ban đầu.
Tuy nhiên, đây **không phải là nghiệm duy nhất**.
Người ta chứng minh được rằng phương trình ban đầu có chính xác $g$ nghiệm, và các nghiệm đó có dạng như sau:

$$x_i \equiv (x^\prime + i\cdot n^\prime) \pmod n \quad \text{với } i = 0 \ldots g-1$$

Tóm lại, **số lượng nghiệm** của phương trình đồng dư tuyến tính bằng $g = \gcd(a, n)$ hoặc bằng 0.

## Giải bằng Thuật toán Euclid mở rộng

Chúng ta có thể viết lại phương trình đồng dư tuyến tính dưới dạng phương trình Diophantine sau:

$$a \cdot x + n \cdot k = b,$$

trong đó $x$ và $k$ là các số nguyên chưa biết.

Phương pháp giải phương trình này đã được mô tả chi tiết trong bài viết tương ứng [Phương trình Diophantine tuyến tính](linear-diophantine-equation.md) và nó sử dụng [Thuật toán Euclid mở rộng](extended-euclid-algorithm.md).

Bài viết đó cũng mô tả cách tìm tất cả các nghiệm của phương trình từ một nghiệm tìm được trước đó. Trên thực tế, nếu xem xét kỹ, phương pháp đó hoàn toàn tương đương với phương pháp được mô tả ở phần trước.
