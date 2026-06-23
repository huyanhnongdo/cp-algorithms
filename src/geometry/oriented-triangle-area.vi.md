---
tags:
  - Translated
e_maxx_link: oriented_area
lang: vi
---
# Diện tích có hướng của một tam giác

Cho ba điểm $p_1$, $p_2$ và $p_3$, hãy tính diện tích có hướng (Oriented Area) (có dấu) của tam giác được tạo bởi chúng. Dấu của diện tích được xác định như sau: hãy tưởng tượng bạn đang đứng trong mặt phẳng tại điểm $p_1$ và hướng mặt về phía $p_2$. Bạn đi đến $p_2$ và nếu $p_3$ nằm bên phải bạn (khi đó chúng ta nói ba vector quay "thuận chiều kim đồng hồ"), dấu của diện tích là âm; ngược lại thì là dương. Nếu ba điểm thẳng hàng, diện tích bằng không.

Sử dụng diện tích có dấu này, chúng ta có thể vừa có được diện tích thông thường không dấu (bằng giá trị tuyệt đối của diện tích có dấu) vừa xác định xem các điểm có nằm theo chiều kim đồng hồ hay ngược chiều kim đồng hồ theo thứ tự đã chỉ định của chúng (điều này hữu ích, ví dụ, trong các thuật toán bao lồi (Convex Hull)).

## Tính toán
Chúng ta có thể sử dụng thực tế rằng định thức (Determinant) của một ma trận (Matrix) $2\times 2$ bằng với diện tích có dấu của một hình bình hành được tạo bởi các vector cột (hoặc hàng) của ma trận.
Điều này tương tự như định nghĩa của tích có hướng (Cross Product) trong không gian 2D (xem [Hình học cơ bản](basic-geometry.md)).
Bằng cách chia diện tích này cho hai, chúng ta sẽ có được diện tích của tam giác mà chúng ta quan tâm.
Chúng ta sẽ sử dụng $\vec{p_1p_2}$ và $\vec{p_2p_3}$ làm các vector cột và tính định thức $2\times 2$:

$$2S=\left|\begin{matrix}x_2-x_1 & x_3-x_2\\y_2-y_1 & y_3-y_2\end{matrix}\right|=(x_2-x_1)(y_3-y_2)-(x_3-x_2)(y_2-y_1)$$

## Cài đặt

```cpp
int signed_area_parallelogram(point2d p1, point2d p2, point2d p3) {
    return cross(p2 - p1, p3 - p2);
}

double triangle_area(point2d p1, point2d p2, point2d p3) {
    return abs(signed_area_parallelogram(p1, p2, p3)) / 2.0;
}

bool clockwise(point2d p1, point2d p2, point2d p3) {
    return signed_area_parallelogram(p1, p2, p3) < 0;
}

bool counter_clockwise(point2d p1, point2d p2, point2d p3) {
    return signed_area_parallelogram(p1, p2, p3) > 0;
}
```

## Bài tập luyện tập
* [Codechef - Chef và Đa giác](https://www.codechef.com/problems/CHEFPOLY)