---
title: Finding area of simple polygon in O(N)
tags:
  - Translated
e_maxx_link: polygon_area
lang: vi
---
# Tìm diện tích đa giác đơn trong $O(N)$

Cho một đa giác đơn (tức là không tự giao nhau, không nhất thiết phải lồi). Cần tính diện tích của nó khi biết các đỉnh.

## Phương pháp 1

Điều này dễ thực hiện nếu ta duyệt qua tất cả các cạnh và cộng các diện tích hình thang được giới hạn bởi mỗi cạnh và trục x. Diện tích cần được tính có dấu để phần diện tích thừa sẽ được trừ đi. Do đó, công thức như sau:

$$A = \sum_{(p,q)\in \text{edges}} \frac{(p_x - q_x) \cdot (p_y + q_y)}{2}$$

Mã nguồn:

```cpp
double area(const vector<point>& fig) {
    double res = 0;
    for (unsigned i = 0; i < fig.size(); i++) {
        point p = i ? fig[i - 1] : fig.back();
        point q = fig[i];
        res += (p.x - q.x) * (p.y + q.y);
    }
    return fabs(res) / 2;
}
```

## Phương pháp 2
Ta có thể chọn một điểm $O$ tùy ý, duyệt qua tất cả các cạnh, cộng diện tích có hướng của tam giác được tạo bởi cạnh và điểm $O$. Một lần nữa, nhờ dấu của diện tích, phần diện tích thừa sẽ được trừ đi.

Phương pháp này tốt hơn vì nó có thể được tổng quát hóa cho các trường hợp phức tạp hơn (chẳng hạn như khi một số cạnh là cung tròn thay vì đường thẳng).