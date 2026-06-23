---
tags:
  - Translated
e_maxx_link: kirchhoff_theorem
---

# Định lý Kirchhoff. Tìm số lượng cây khung

Bài toán: Cho một đồ thị vô hướng liên thông (có thể có đa cạnh) được biểu diễn bằng ma trận kề. Tìm số lượng cây khung khác nhau của đồ thị này.

Công thức dưới đây đã được chứng minh bởi Kirchhoff vào năm 1847.

## Định lý ma trận cây Kirchhoff

Gọi $A$ là ma trận kề của đồ thị: $A_{u,v}$ là số lượng cạnh nối giữa $u$ và $v$.
Gọi $D$ là ma trận bậc của đồ thị: một ma trận đường chéo với $D_{u,u}$ là bậc của đỉnh $u$ (tính cả đa cạnh và khuyên - các cạnh nối đỉnh $u$ với chính nó).

Ma trận Laplacian của đồ thị được định nghĩa là $L = D - A$.
Theo định lý Kirchhoff, tất cả các phần bù đại số (cofactor) của ma trận này đều bằng nhau, và chúng bằng số lượng cây khung của đồ thị.
Phần bù đại số $(i,j)$ của một ma trận là tích của $(-1)^{i + j}$ với định thức của ma trận thu được sau khi xóa hàng thứ $i$ và cột thứ $j$.
Vì vậy, ví dụ bạn có thể xóa hàng cuối cùng và cột cuối cùng của ma trận $L$, định thức (trị tuyệt đối) của ma trận kết quả thu được sẽ cho bạn biết số lượng cây khung.

Định thức của ma trận có thể được tìm trong $O(N^3)$ bằng cách sử dụng [phương pháp Gauss](../linear_algebra/determinant-gauss.md).

Chứng minh của định lý này khá phức tạp và không được trình bày ở đây; để xem sơ lược chứng minh cũng như các biến thể của định lý cho đồ thị không có đa cạnh và cho đồ thị có hướng, bạn có thể tham khảo [Wikipedia](https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem).

## Mối liên hệ với các định luật mạch điện Kirchhoff

Định lý ma trận cây Kirchhoff và các định luật Kirchhoff cho mạch điện có một mối liên hệ tuyệt đẹp. Ta có thể chứng minh được (sử dụng định luật Ohm và định luật Kirchhoff thứ nhất) rằng điện trở $R_{ij}$ giữa hai điểm $i$ và $j$ của mạch điện là:

$$R_{ij} = \frac{ \left| L^{(i,j)} \right| }{ | L^j | }.$$

Ở đây, ma trận $L$ được thu từ ma trận nghịch đảo điện trở $A$ ($A_{i,j}$ là nghịch đảo điện trở của dây dẫn giữa hai điểm $i$ và $j$) bằng cách sử dụng quy trình được mô tả trong định lý ma trận cây Kirchhoff.
$T^j$ là ma trận được loại bỏ hàng và cột $j$, $T^{(i,j)}$ là ma trận được loại bỏ hai hàng và hai cột $i$ và $j$.

Định lý Kirchhoff đem lại ý nghĩa hình học cho công thức này.

## Bài tập luyện tập
 - [CODECHEF: Roads in Stars](https://www.codechef.com/problems/STARROAD)
 - [SPOJ: Maze](http://www.spoj.com/problems/KPMAZE/)
 - [CODECHEF: Complement Spanning Trees](https://www.codechef.com/problems/CSTREE)
