---
tags:
  - Translated
e_maxx_link: pick_grid_theorem
lang: vi
---
# Định lý Pick (Pick's Theorem)

Một đa giác không tự cắt được gọi là đa giác lưới (lattice polygon) nếu tất cả các đỉnh của nó đều có tọa độ nguyên trên hệ tọa độ 2D. Định lý Pick cung cấp một cách để tính diện tích của đa giác này thông qua số lượng các điểm lưới nằm trên biên và số lượng các điểm lưới nằm hoàn toàn bên trong đa giác.

## Công thức

Cho một đa giác lưới nhất định có diện tích khác không.

Ta ký hiệu diện tích của nó là $S$, số điểm có tọa độ nguyên nằm hoàn toàn bên trong đa giác là $I$ và số điểm nằm trên các cạnh của đa giác là $B$.

Khi đó, **công thức Pick** phát biểu rằng:

$$S=I+\frac{B}{2}-1$$

Đặc biệt, nếu đã biết các giá trị của $I$ và $B$ cho một đa giác, diện tích có thể được tính toán trong $O(1)$ mà không cần biết tọa độ các đỉnh.

Công thức này được nhà toán học người Áo Georg Alexander Pick khám phá và chứng minh vào năm 1899.

## Chứng minh

Việc chứng minh được thực hiện qua nhiều giai đoạn: từ các đa giác đơn giản đến các đa giác bất kỳ:

- Một hình vuông đơn vị: $S=1, I=0, B=4$, thỏa mãn công thức.

- Một hình chữ nhật không suy biến với các cạnh song song với các trục tọa độ: Giả sử $a$ và $b$ là độ dài các cạnh của hình chữ nhật. Khi đó, $S=ab, I=(a-1)(b-1), B=2(a+b)$. Khi thay thế vào, ta thấy công thức là đúng.

- Một tam giác vuông với các cạnh góc vuông song song với các trục tọa độ: Để chứng minh điều này, hãy lưu ý rằng bất kỳ tam giác nào như vậy cũng có thể thu được bằng cách cắt một hình chữ nhật bởi một đường chéo. Gọi $c$ là số điểm nguyên nằm trên đường chéo, có thể chứng minh rằng công thức Pick đúng với tam giác này bất kể $c$ là bao nhiêu.

- Một tam giác bất kỳ: Lưu ý rằng bất kỳ tam giác nào cũng có thể được biến thành một hình chữ nhật bằng cách gắn thêm các tam giác vuông có các cạnh song song với trục tọa độ (bạn sẽ không cần nhiều hơn 3 tam giác như vậy). Từ đây, ta có thể thu được công thức chính xác cho bất kỳ tam giác nào.

- Một đa giác bất kỳ: Để chứng minh điều này, hãy thực hiện tam giác hóa nó, tức là chia nó thành các tam giác với các tọa độ nguyên. Hơn nữa, có thể chứng minh rằng định lý Pick vẫn giữ nguyên tính hợp lệ khi một đa giác được cộng thêm một tam giác. Do đó, chúng ta đã chứng minh được công thức Pick cho đa giác bất kỳ.

## Tổng quát hóa cho không gian nhiều chiều

Thật không may, công thức đơn giản và đẹp đẽ này không thể được tổng quát hóa cho các không gian nhiều chiều hơn.

John Reeve đã chứng minh điều này bằng cách đề xuất một hình tứ diện (**tứ diện Reeve**) với các đỉnh sau vào năm 1957:

$$A=(0,0,0),
B=(1,0,0),
C=(0,1,0),
D=(1,1,k),$$

trong đó $k$ có thể là bất kỳ số tự nhiên nào. Khi đó với bất kỳ $k$, hình tứ diện $ABCD$ không chứa điểm nguyên nào bên trong và chỉ có $4$ điểm trên các biên của nó, $A, B, C, D$. Do đó, thể tích và diện tích bề mặt có thể thay đổi mặc dù số lượng điểm bên trong và trên biên không đổi. Vì vậy, định lý Pick không cho phép tổng quát hóa.

Tuy nhiên, các chiều cao hơn vẫn có một sự tổng quát hóa bằng cách sử dụng **đa thức Ehrhart** (Ehrhart polynomials), nhưng chúng khá phức tạp và không chỉ phụ thuộc vào các điểm bên trong mà còn phụ thuộc vào biên của đa diện (polytype).

## Tài liệu bổ sung
Một vài ví dụ đơn giản và một chứng minh đơn giản của định lý Pick có thể được tìm thấy [tại đây](http://www.geometer.org/mathcircles/pick.pdf).