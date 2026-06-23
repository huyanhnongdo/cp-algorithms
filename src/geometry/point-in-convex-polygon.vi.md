---
title: Check if point belongs to the convex polygon in O(log N)
tags:
  - Translated
e_maxx_link: pt_in_polygon
lang: vi
---
# Kiểm tra điểm nằm trong đa giác lồi trong $O(\log N)$

Xét bài toán sau: bạn được cho một đa giác lồi (convex polygon) với các đỉnh là tọa độ nguyên và rất nhiều truy vấn (query).
Mỗi truy vấn là một điểm, chúng ta cần xác định xem điểm đó có nằm bên trong hoặc nằm trên biên của đa giác hay không.
Giả sử đa giác được sắp xếp theo chiều ngược chiều kim đồng hồ. Chúng ta sẽ trả lời mỗi truy vấn trong $O(\log n)$ theo hình thức trực tuyến (online).

## Thuật toán
Hãy chọn điểm có tọa độ x nhỏ nhất. Nếu có nhiều điểm như vậy, chúng ta chọn điểm có tọa độ y nhỏ nhất. Hãy gọi điểm này là $p_0$.
Bây giờ, tất cả các điểm còn lại $p_1,\dots,p_n$ của đa giác được sắp xếp theo góc cực (polar angle) từ điểm đã chọn (vì đa giác được sắp xếp ngược chiều kim đồng hồ).

Nếu điểm cần xét nằm trong đa giác, nó sẽ nằm trong một tam giác $p_0, p_i, p_{i + 1}$ nào đó (có thể nhiều hơn một nếu nó nằm trên cạnh của các tam giác).
Xét tam giác $p_0, p_i, p_{i + 1}$ sao cho $p$ thuộc tam giác này và $i$ là giá trị lớn nhất trong tất cả các tam giác thỏa mãn điều kiện đó.

Có một trường hợp đặc biệt: $p$ nằm trên đoạn thẳng $(p_0, p_n)$. Trường hợp này chúng ta sẽ kiểm tra riêng.
Nếu không, tất cả các điểm $p_j$ với $j \le i$ sẽ nằm theo chiều ngược chiều kim đồng hồ so với $p$ với gốc là $p_0$, và tất cả các điểm còn lại thì không.
Điều này có nghĩa là chúng ta có thể áp dụng tìm kiếm nhị phân (Binary Search) để tìm điểm $p_i$, sao cho $p_i$ không nằm ngược chiều kim đồng hồ so với $p$ với gốc là $p_0$, và $i$ là lớn nhất trong tất cả các điểm như vậy.
Sau đó, chúng ta kiểm tra xem điểm này thực sự có nằm trong tam giác đã xác định hay không.

Dấu của $(a - c) \times (b - c)$ sẽ cho chúng ta biết liệu điểm $a$ nằm theo chiều kim đồng hồ hay ngược chiều kim đồng hồ so với điểm $b$ với gốc là điểm $c$.
Nếu $(a - c) \times (b - c) > 0$, thì điểm $a$ nằm bên phải vector đi từ $c$ đến $b$, nghĩa là nằm theo chiều kim đồng hồ so với $b$ với gốc là $c$.
Và nếu $(a - c) \times (b - c) < 0$, thì điểm đó nằm bên trái, hoặc ngược chiều kim đồng hồ.
Nếu bằng 0, điểm đó nằm chính xác trên đường thẳng giữa hai điểm $b$ và $c$.

Quay lại thuật toán:
Xét một điểm truy vấn $p$.
Trước tiên, chúng ta phải kiểm tra xem điểm đó có nằm giữa $p_1$ và $p_n$ hay không.
Nếu không, ta đã biết ngay nó không thể là một phần của đa giác.
Việc này có thể thực hiện bằng cách kiểm tra xem tích chéo (cross product) $(p_1 - p_0)\times(p - p_0)$ có bằng 0 hoặc cùng dấu với $(p_1 - p_0)\times(p_n - p_0)$, và $(p_n - p_0)\times(p - p_0)$ có bằng 0 hoặc cùng dấu với $(p_n - p_0)\times(p_1 - p_0)$ hay không.
Sau đó, chúng ta xử lý trường hợp đặc biệt mà $p$ nằm trên đường thẳng $(p_0, p_1)$.
Tiếp theo, ta thực hiện tìm kiếm nhị phân để tìm điểm cuối cùng từ $p_1,\dots p_n$ không nằm ngược chiều kim đồng hồ so với $p$ với gốc là $p_0$.
Với một điểm $p_i$ đơn lẻ, điều kiện này có thể được kiểm tra bằng $(p_i - p_0)\times(p - p_0) \le 0$. Sau khi tìm thấy điểm $p_i$, chúng ta phải kiểm tra xem $p$ có nằm trong tam giác $p_0, p_i, p_{i + 1}$ hay không.
Để kiểm tra xem nó có thuộc tam giác hay không, ta chỉ cần kiểm tra xem $|(p_i - p_0)\times(p_{i + 1} - p_0)| = |(p_0 - p)\times(p_i - p)| + |(p_i - p)\times(p_{i + 1} - p)| + |(p_{i + 1} - p)\times(p_0 - p)|$.
Cách này kiểm tra xem diện tích của tam giác $p_0, p_i, p_{i+1}$ có bằng chính xác tổng diện tích của tam giác $p_0, p_i, p$, tam giác $p_0, p, p_{i+1}$ và tam giác $p_i, p_{i+1}, p$ hay không.
Nếu $p$ nằm ngoài, thì tổng diện tích của ba tam giác đó sẽ lớn hơn diện tích tam giác ban đầu.
Nếu nó nằm trong, thì hai giá trị đó sẽ bằng nhau.

## Cài đặt

Hàm `prepare` sẽ đảm bảo điểm có thứ tự từ điển nhỏ nhất (giá trị x nhỏ nhất, nếu bằng nhau thì y nhỏ nhất) sẽ là $p_0$, và tính toán các vector $p_i - p_0$.
Sau đó, hàm `pointInConvexPolygon` tính toán kết quả của một truy vấn.
Chúng ta lưu lại điểm $p_0$ và tịnh tiến tất cả các điểm truy vấn theo nó để tính khoảng cách chính xác, vì các vector không có điểm gốc cố định.
Bằng cách tịnh tiến các điểm truy vấn, ta có thể giả định rằng tất cả các vector đều bắt đầu tại gốc tọa độ $(0, 0)$, từ đó đơn giản hóa việc tính toán khoảng cách và độ dài.

```{.cpp file=points_in_convex_polygon}
struct pt {
    long long x, y;
    pt() {}
    pt(long long _x, long long _y) : x(_x), y(_y) {}
    pt operator+(const pt &p) const { return pt(x + p.x, y + p.y); }
    pt operator-(const pt &p) const { return pt(x - p.x, y - p.y); }
    long long cross(const pt &p) const { return x * p.y - y * p.x; }
    long long dot(const pt &p) const { return x * p.x + y * p.y; }
    long long cross(const pt &a, const pt &b) const { return (a - *this).cross(b - *this); }
    long long dot(const pt &a, const pt &b) const { return (a - *this).dot(b - *this); }
    long long sqrLen() const { return this->dot(*this); }
};

bool lexComp(const pt &l, const pt &r) {
    return l.x < r.x || (l.x == r.x && l.y < r.y);
}

int sgn(long long val) { return val > 0 ? 1 : (val == 0 ? 0 : -1); }

vector<pt> seq;
pt translation;
int n;

bool pointInTriangle(pt a, pt b, pt c, pt point) {
    long long s1 = abs(a.cross(b, c));
    long long s2 = abs(point.cross(a, b)) + abs(point.cross(b, c)) + abs(point.cross(c, a));
    return s1 == s2;
}

void prepare(vector<pt> &points) {
    n = points.size();
    int pos = 0;
    for (int i = 1; i < n; i++) {
        if (lexComp(points[i], points[pos]))
            pos = i;
    }
    rotate(points.begin(), points.begin() + pos, points.end());

    n--;
    seq.resize(n);
    for (int i = 0; i < n; i++)
        seq[i] = points[i + 1] - points[0];
    translation = points[0];
}

bool pointInConvexPolygon(pt point) {
    point = point - translation;
    if (seq[0].cross(point) != 0 &&
            sgn(seq[0].cross(point)) != sgn(seq[0].cross(seq[n - 1])))
        return false;
    if (seq[n - 1].cross(point) != 0 &&
            sgn(seq[n - 1].cross(point)) != sgn(seq[n - 1].cross(seq[0])))
        return false;

    if (seq[0].cross(point) == 0)
        return seq[0].sqrLen() >= point.sqrLen();

    int l = 0, r = n - 1;
    while (r - l > 1) {
        int mid = (l + r) / 2;
        int pos = mid;
        if (seq[pos].cross(point) >= 0)
            l = mid;
        else
            r = mid;
    }
    int pos = l;
    return pointInTriangle(seq[pos], seq[pos + 1], pt(0, 0), point);
}
```

## Các bài tập
* [SGU253 Theodore Roosevelt](https://codeforces.com/problemsets/acmsguru/problem/99999/253)
* [Codeforces 55E Very simple problem](https://codeforces.com/contest/55/problem/E)
* [Codeforces 166B Polygons](https://codeforces.com/problemset/problem/166/B)