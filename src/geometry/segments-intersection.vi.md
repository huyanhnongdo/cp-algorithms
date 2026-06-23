---
tags:
  - Translated
e_maxx_link: segments_intersection
lang: vi
---
# Tìm giao điểm của hai đoạn thẳng

Bạn được cho hai đoạn thẳng AB và CD, được mô tả bởi cặp điểm đầu mút của chúng. Mỗi đoạn thẳng có thể là một điểm duy nhất nếu hai đầu mút của nó trùng nhau.
Bạn cần tìm giao điểm của hai đoạn thẳng này; kết quả có thể là rỗng (nếu các đoạn thẳng không giao nhau), một điểm duy nhất, hoặc một đoạn thẳng (nếu các đoạn thẳng chồng lấp lên nhau).

## Lời giải

Chúng ta có thể tìm giao điểm của các đoạn thẳng theo cách tương tự như [giao điểm của hai đường thẳng](lines-intersection.md):
xây dựng phương trình đường thẳng từ các đầu mút của đoạn thẳng và kiểm tra xem chúng có song song hay không.

Nếu các đường thẳng không song song, chúng ta cần tìm giao điểm của chúng và kiểm tra xem điểm đó có thuộc về cả hai đoạn thẳng hay không
(để làm điều này, chỉ cần xác minh rằng giao điểm thuộc về mỗi đoạn thẳng khi chiếu lên trục X và trục Y).
Trong trường hợp này, kết quả sẽ là "không giao nhau" hoặc là một điểm duy nhất tại giao điểm của hai đường thẳng.

Trường hợp các đường thẳng song song thì phức tạp hơn một chút (trường hợp một hoặc cả hai đoạn thẳng là một điểm duy nhất cũng thuộc nhóm này).
Trong trường hợp này, chúng ta cần kiểm tra xem cả hai đoạn thẳng có cùng nằm trên một đường thẳng hay không.
Nếu không, kết quả là "không giao nhau".
Nếu có, kết quả là phần giao của các đoạn thẳng cùng nằm trên một đường thẳng đó, thu được bằng cách
sắp xếp các đầu mút của cả hai đoạn thẳng theo thứ tự tăng dần của một tọa độ nào đó, sau đó lấy giá trị lớn nhất trong các đầu mút bên trái và giá trị nhỏ nhất trong các đầu mút bên phải.

Nếu cả hai đoạn thẳng đều là các điểm đơn lẻ, các điểm này phải trùng nhau, và việc thực hiện kiểm tra riêng cho trường hợp này là cần thiết.

Ở phần đầu của thuật toán, hãy thêm bước kiểm tra hộp bao (bounding box) - điều này cần thiết cho trường hợp các đoạn thẳng cùng nằm trên một đường thẳng,
và (là một bước kiểm tra nhẹ nhàng) nó cho phép thuật toán chạy nhanh hơn trung bình trên các bộ test ngẫu nhiên.

## Cài đặt

Dưới đây là phần cài đặt, bao gồm tất cả các hàm hỗ trợ để xử lý đường thẳng và đoạn thẳng.

Hàm chính `intersect` trả về `true` nếu hai đoạn thẳng có giao điểm khác rỗng,
và lưu các đầu mút của đoạn giao vào các tham số `left` và `right`.
Nếu kết quả là một điểm duy nhất, các giá trị được ghi vào `left` và `right` sẽ giống nhau.

```{.cpp file=segment_intersection}
const double EPS = 1E-9;

struct pt {
    double x, y;

    bool operator<(const pt& p) const
    {
        return x < p.x - EPS || (abs(x - p.x) < EPS && y < p.y - EPS);
    }
};

struct line {
    double a, b, c;

    line() {}
    line(pt p, pt q)
    {
        a = p.y - q.y;
        b = q.x - p.x;
        c = -a * p.x - b * p.y;
        norm();
    }

    void norm()
    {
        double z = sqrt(a * a + b * b);
        if (abs(z) > EPS)
            a /= z, b /= z, c /= z;
    }

    double dist(pt p) const { return a * p.x + b * p.y + c; }
};

double det(double a, double b, double c, double d)
{
    return a * d - b * c;
}

inline bool betw(double l, double r, double x)
{
    return min(l, r) <= x + EPS && x <= max(l, r) + EPS;
}

inline bool intersect_1d(double a, double b, double c, double d)
{
    if (a > b)
        swap(a, b);
    if (c > d)
        swap(c, d);
    return max(a, c) <= min(b, d) + EPS;
}

bool intersect(pt a, pt b, pt c, pt d, pt& left, pt& right)
{
    if (!intersect_1d(a.x, b.x, c.x, d.x) || !intersect_1d(a.y, b.y, c.y, d.y))
        return false;
    line m(a, b);
    line n(c, d);
    double zn = det(m.a, m.b, n.a, n.b);
    if (abs(zn) < EPS) {
        if (abs(m.dist(c)) > EPS || abs(n.dist(a)) > EPS)
            return false;
        if (b < a)
            swap(a, b);
        if (d < c)
            swap(c, d);
        left = max(a, c);
        right = min(b, d);
        return true;
    } else {
        left.x = right.x = -det(m.c, m.b, n.c, n.b) / zn;
        left.y = right.y = -det(m.a, m.c, n.a, n.c) / zn;
        return betw(a.x, b.x, left.x) && betw(a.y, b.y, left.y) &&
               betw(c.x, d.x, left.x) && betw(c.y, d.y, left.y);
    }
}
```