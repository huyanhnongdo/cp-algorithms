---
title: Finding faces of a planar graph
tags:
  - Translated
e_maxx_link: facets
lang: vi
---
# Tìm các mặt của một đồ thị phẳng (Planar Graph)

Xét một đồ thị $G$ với $n$ đỉnh và $m$ cạnh, có thể được vẽ trên một mặt phẳng sao cho hai cạnh chỉ cắt nhau tại một đỉnh chung (nếu có).
Các đồ thị như vậy được gọi là **đồ thị phẳng** (planar graph). Giả sử chúng ta có một đồ thị phẳng cùng với cách nhúng đoạn thẳng của nó, nghĩa là với mỗi đỉnh $v$, ta có một điểm tương ứng $(x, y)$ và tất cả các cạnh được vẽ dưới dạng các đoạn thẳng nối giữa các điểm này mà không cắt nhau (cách nhúng như vậy luôn tồn tại). Các đoạn thẳng này chia mặt phẳng thành nhiều vùng, được gọi là các mặt (face). Có đúng một mặt là không bị chặn (unbounded). Mặt này được gọi là **mặt ngoài** (outer face), trong khi các mặt còn lại được gọi là **mặt trong** (inner face).

Trong bài viết này, chúng ta sẽ đề cập đến việc tìm cả mặt trong và mặt ngoài của một đồ thị phẳng. Chúng ta sẽ giả định rằng đồ thị là liên thông.

## Một vài sự thật về đồ thị phẳng

Trong phần này, chúng ta trình bày một số sự thật về đồ thị phẳng mà không có chứng minh. Những độc giả quan tâm đến chứng minh có thể tham khảo [Lý thuyết đồ thị của R. Diestel](https://www.math.uni-hamburg.de/home/diestel/books/graph.theory/preview/Ch4.pdf) (xem thêm [các bài giảng video về tính phẳng](https://www.youtube.com/@DiestelGraphTheory) dựa trên cuốn sách này) hoặc một số cuốn sách khác.

### Định lý Euler
Định lý Euler phát biểu rằng bất kỳ cách nhúng đúng đắn nào của một đồ thị phẳng liên thông với $n$ đỉnh, $m$ cạnh và $f$ mặt đều thỏa mãn:

$$n - m + f = 2$$

Tổng quát hơn, mọi đồ thị phẳng với $k$ thành phần liên thông đều thỏa mãn:

$$n - m + f = 1 + k$$

### Số cạnh của đồ thị phẳng.
Nếu $n \ge 3$ thì số cạnh tối đa của một đồ thị phẳng với $n$ đỉnh là $3n - 6$. Con số này đạt được bởi bất kỳ đồ thị phẳng liên thông nào mà mỗi mặt đều được bao quanh bởi một tam giác. Về mặt độ phức tạp, thực tế này có nghĩa là $m = O(n)$ cho bất kỳ đồ thị phẳng nào.

### Số mặt của đồ thị phẳng.
Là hệ quả trực tiếp từ thực tế trên, nếu $n \ge 3$ thì số mặt tối đa của một đồ thị phẳng với $n$ đỉnh là $2n - 4$.

### Bậc đỉnh nhỏ nhất trong đồ thị phẳng.
Mỗi đồ thị phẳng đều có ít nhất một đỉnh với bậc bằng 5 hoặc nhỏ hơn.

## Thuật toán

Trước tiên, hãy sắp xếp các cạnh kề cho mỗi đỉnh theo góc cực (polar angle).
Bây giờ, hãy duyệt đồ thị theo cách sau: Giả sử chúng ta đi vào đỉnh $u$ thông qua cạnh $(v, u)$ và $(u, w)$ là cạnh tiếp theo sau $(v, u)$ trong danh sách kề đã sắp xếp của $u$. Khi đó, đỉnh tiếp theo sẽ là $w$. Hóa ra nếu bắt đầu quá trình duyệt này tại một cạnh $(v, u)$, chúng ta sẽ duyệt đúng một trong các mặt kề với $(v, u)$, mặt cụ thể tùy thuộc vào việc bước đầu tiên của chúng ta là từ $u$ đến $v$ hay từ $v$ đến $u$.

Thuật toán hiện tại đã khá rõ ràng. Chúng ta phải lặp qua tất cả các cạnh của đồ thị và bắt đầu duyệt cho mỗi cạnh chưa được ghé thăm bởi một trong các lần duyệt trước đó. Bằng cách này, chúng ta sẽ tìm thấy mỗi mặt đúng một lần, và mỗi cạnh sẽ được duyệt hai lần (mỗi lần theo một hướng).

### Tìm cạnh tiếp theo
Trong quá trình duyệt, chúng ta phải tìm cạnh tiếp theo theo thứ tự ngược chiều kim đồng hồ. Cách rõ ràng nhất để tìm cạnh tiếp theo là tìm kiếm nhị phân (binary search) theo góc. Tuy nhiên, với thứ tự ngược chiều kim đồng hồ của các cạnh kề cho mỗi đỉnh, chúng ta có thể tiền xử lý các cạnh tiếp theo và lưu chúng trong một bảng băm (hash table). Nếu các cạnh đã được sắp xếp theo góc, độ phức tạp của việc tìm tất cả các mặt trong trường hợp này sẽ trở thành tuyến tính.

### Tìm mặt ngoài
Không khó để nhận thấy rằng thuật toán duyệt mỗi mặt trong theo chiều kim đồng hồ và mặt ngoài theo chiều ngược chiều kim đồng hồ, vì vậy mặt ngoài có thể được tìm thấy bằng cách kiểm tra thứ tự của mỗi mặt.

### Độ phức tạp
Rõ ràng là độ phức tạp của thuật toán là $O(m \log m)$ do việc sắp xếp, và vì $m = O(n)$, nên thực tế nó là $O(n \log n)$. Như đã đề cập trước đó, nếu không sắp xếp thì độ phức tạp sẽ trở thành $O(n)$.

## Điều gì xảy ra nếu đồ thị không liên thông?

Thoạt nhìn, có vẻ như việc tìm các mặt của một đồ thị không liên thông không khó hơn bao nhiêu vì chúng ta có thể chạy cùng một thuật toán cho mỗi thành phần liên thông. Tuy nhiên, các thành phần có thể được vẽ lồng vào nhau, tạo thành các **lỗ hổng** (xem hình bên dưới). Trong trường hợp này, mặt trong của một thành phần trở thành mặt ngoài của một số thành phần khác và có biên giới phức tạp không liên thông. Việc xử lý các trường hợp như vậy khá khó khăn, một cách tiếp cận khả thi là xác định các thành phần lồng nhau bằng thuật toán [định vị điểm](point-location.md) (point location).

<div style="text-align: center;" markdown="1">

![Đồ thị phẳng có lỗ hổng](planar_hole.png)

</div>

## Cài đặt
Đoạn mã dưới đây trả về một vector chứa các đỉnh cho mỗi mặt, mặt ngoài được đưa ra đầu tiên.
Các mặt trong được trả về theo thứ tự ngược chiều kim đồng hồ và mặt ngoài được trả về theo chiều kim đồng hồ.

Để đơn giản, chúng ta tìm cạnh tiếp theo bằng cách tìm kiếm nhị phân theo góc.
```{.cpp file=planar}
struct Point {
    int64_t x, y;

    Point(int64_t x_, int64_t y_): x(x_), y(y_) {}

    Point operator - (const Point & p) const {
        return Point(x - p.x, y - p.y);
    }

    int64_t cross (const Point & p) const {
        return x * p.y - y * p.x;
    }

    int64_t cross (const Point & p, const Point & q) const {
        return (p - *this).cross(q - *this);
    }

    int half () const {
        return int(y < 0 || (y == 0 && x < 0));
    }
};

std::vector<std::vector<size_t>> find_faces(std::vector<Point> vertices, std::vector<std::vector<size_t>> adj) {
    size_t n = vertices.size();
    std::vector<std::vector<char>> used(n);
    for (size_t i = 0; i < n; i++) {
        used[i].resize(adj[i].size());
        used[i].assign(adj[i].size(), 0);
        auto compare = [&](size_t l, size_t r) {
            Point pl = vertices[l] - vertices[i];
            Point pr = vertices[r] - vertices[i];
            if (pl.half() != pr.half())
                return pl.half() < pr.half();
            return pl.cross(pr) > 0;
        };
        std::sort(adj[i].begin(), adj[i].end(), compare);
    }
    std::vector<std::vector<size_t>> faces;
    for (size_t i = 0; i < n; i++) {
        for (size_t edge_id = 0; edge_id < adj[i].size(); edge_id++) {
            if (used[i][edge_id]) {
                continue;
            }
            std::vector<size_t> face;
            size_t v = i;
            size_t e = edge_id;
            while (!used[v][e]) {
                used[v][e] = true;
                face.push_back(v);
                size_t u = adj[v][e];
                size_t e1 = std::lower_bound(adj[u].begin(), adj[u].end(), v, [&](size_t l, size_t r) {
                    Point pl = vertices[l] - vertices[u];
                    Point pr = vertices[r] - vertices[u];
                    if (pl.half() != pr.half())
                        return pl.half() < pr.half();
                    return pl.cross(pr) > 0;
                }) - adj[u].begin() + 1;
                if (e1 == adj[u].size()) {
                    e1 = 0;
                }
                v = u;
                e = e1;
            }
            std::reverse(face.begin(), face.end());
            Point p1 = vertices[face[0]];
            __int128 sum = 0;
            for (int j = 0; j < face.size(); ++j) {
                Point p2 = vertices[face[j]];
                Point p3 = vertices[face[(j + 1) % face.size()]];
                sum += (p2 - p1).cross(p3 - p2);
            }
            if (sum <= 0) {
                faces.insert(faces.begin(), face);
            } else {
                faces.emplace_back(face);
            }
        }
    }
    return faces;
}
```

## Xây dựng đồ thị phẳng từ các đoạn thẳng

Đôi khi bạn không được cho một đồ thị một cách tường minh, mà thay vào đó là một tập hợp các đoạn thẳng trên mặt phẳng, và đồ thị thực tế được hình thành bởi các giao điểm của các đoạn thẳng đó, như trong hình dưới đây. Trong trường hợp này, bạn phải tự xây dựng đồ thị theo cách thủ công. Cách dễ nhất để làm điều đó như sau: Cố định một đoạn thẳng và cho nó cắt với tất cả các đoạn thẳng khác. Sau đó sắp xếp tất cả các điểm giao cắt cùng với hai điểm cuối của đoạn thẳng theo thứ tự từ điển và thêm chúng vào đồ thị dưới dạng các đỉnh. Ngoài ra, hãy nối mỗi hai đỉnh kề nhau theo thứ tự từ điển bằng một cạnh. Sau khi thực hiện quy trình này cho tất cả các cạnh, chúng ta sẽ thu được đồ thị. Tất nhiên, chúng ta nên đảm bảo rằng hai điểm giao cắt bằng nhau sẽ luôn tương ứng với cùng một đỉnh. Cách dễ nhất để làm điều này là lưu các điểm vào một map theo tọa độ của chúng, coi các điểm có tọa độ chênh lệch nhau một khoảng nhỏ (ví dụ: nhỏ hơn $10^{-9}$) là bằng nhau. Thuật toán này hoạt động trong $O(n^2 \log n)$.

<div style="text-align: center;" markdown="1">

![Đồ thị xác định ẩn](planar_implicit.png)

</div>

## Cài đặt
```{.cpp file=planar_implicit}
using dbl = long double;

const dbl eps = 1e-9;

struct Point {
    dbl x, y;

    Point(){}
    Point(dbl x_, dbl y_): x(x_), y(y_) {}

    Point operator * (dbl d) const {
        return Point(x * d, y * d);
    }

    Point operator + (const Point & p) const {
        return Point(x + p.x, y + p.y);
    }

    Point operator - (const Point & p) const {
        return Point(x - p.x, y - p.y);
    }

    dbl cross (const Point & p) const {
        return x * p.y - y * p.x;
    }

    dbl cross (const Point & p, const Point & q) const {
        return (p - *this).cross(q - *this);
    }

    dbl dot (const Point & p) const {
        return x * p.x + y * p.y;
    }

    dbl dot (const Point & p, const Point & q) const {
        return (p - *this).dot(q - *this);
    }

    bool operator < (const Point & p) const {
        if (fabs(x - p.x) < eps) {
            if (fabs(y - p.y) < eps) {
                return false;
            } else {
                return y < p.y;
            }
        } else {
            return x < p.x;
        }
    }

    bool operator == (const Point & p) const {
        return fabs(x - p.x) < eps && fabs(y - p.y) < eps;
    }

    bool operator >= (const Point & p) const {
        return !(*this < p);
    }
};

struct Line{
	Point p[2];

	Line(Point l, Point r){p[0] = l; p[1] = r;}
	Point& operator [](const int & i){return p[i];}
	const Point& operator[](const int & i)const{return p[i];}
	Line(const Line & l){
		p[0] = l.p[0]; p[1] = l.p[1];
	}
	Point getOrth()const{
		return Point(p[1].y - p[0].y, p[0].x - p[1].x);
	}
	bool hasPointLine(const Point & t)const{
		return std::fabs(p[0].cross(p[1], t)) < eps;
	}
	bool hasPointSeg(const Point & t)const{
		return hasPointLine(t) && t.dot(p[0], p[1]) < eps;
	}
};

std::vector<Point> interLineLine(Line l1, Line l2){
	if(std::fabs(l1.getOrth().cross(l2.getOrth())) < eps){
		if(l1.hasPointLine(l2[0]))return {l1[0], l1[1]};
		else return {};
	}
	Point u = l2[1] - l2[0];
	Point v = l1[1] - l1[0];
	dbl s = u.cross(l2[0] - l1[0])/u.cross(v);
	return {Point(l1[0] + v * s)};
}

std::vector<Point> interSegSeg(Line l1, Line l2){
	if (l1[0] == l1[1]) {
		if (l2[0] == l2[1]) {
			if (l1[0] == l2[0])
                return {l1[0]};
			else 
                return {};
		} else {
			if (l2.hasPointSeg(l1[0]))
                return {l1[0]};
			else
                return {};
		}
	}
	if (l2[0] == l2[1]) {
		if (l1.hasPointSeg(l2[0]))
            return {l2[0]};
		else 
            return {};
	}
	auto li = interLineLine(l1, l2);
	if (li.empty())
        return li;
	if (li.size() == 2) {
		if (l1[0] >= l1[1])
            std::swap(l1[0], l1[1]);
		if (l2[0] >= l2[1])
            std::swap(l2[0], l2[1]);
        std::vector<Point> res(2);
		if (l1[0] < l2[0])
            res[0] = l2[0];
        else
            res[0] = l1[0];
		if (l1[1] < l2[1])
            res[1] = l1[1];
        else
            res[1] = l2[1];
		if (res[0] == res[1])
            res.pop_back();
		if (res.size() == 2u && res[1] < res[0])
            return {};
		else 
            return res;
	}
	Point cand = li[0];
	if (l1.hasPointSeg(cand) && l2.hasPointSeg(cand))
        return {cand};
	else 
        return {};
}

std::pair<std::vector<Point>, std::vector<std::vector<size_t>>> build_graph(std::vector<Line> segments) {
    std::vector<Point> p;
    std::vector<std::vector<size_t>> adj;
    std::map<std::pair<int64_t, int64_t>, size_t> point_id;
    auto get_point_id = [&](Point pt) {
        auto repr = std::make_pair(
            int64_t(std::round(pt.x * 1000000000) + 1e-6),
            int64_t(std::round(pt.y * 1000000000) + 1e-6)
        );
        if (!point_id.count(repr)) {
            adj.emplace_back();
            size_t id = point_id.size();
            point_id[repr] = id;
            p.push_back(pt);
            return id;
        } else {
            return point_id[repr];
        }
    };
    for (size_t i = 0; i < segments.size(); i++) {
        std::vector<size_t> curr = {
            get_point_id(segments[i][0]),
            get_point_id(segments[i][1])
        };
        for (size_t j = 0; j < segments.size(); j++) {
            if (i == j)
                continue;
            auto inter = interSegSeg(segments[i], segments[j]);
            for (auto pt: inter) {
                curr.push_back(get_point_id(pt));
            }
        }
        std::sort(curr.begin(), curr.end(), [&](size_t l, size_t r) { return p[l] < p[r]; });
        curr.erase(std::unique(curr.begin(), curr.end()), curr.end());
        for (size_t j = 0; j + 1 < curr.size(); j++) {
            adj[curr[j]].push_back(curr[j + 1]);
            adj[curr[j + 1]].push_back(curr[j]);
        }
    }
    for (size_t i = 0; i < adj.size(); i++) {
        std::sort(adj[i].begin(), adj[i].end());
        // removing edges that were added multiple times
        adj[i].erase(std::unique(adj[i].begin(), adj[i].end()), adj[i].end());
    }
    return {p, adj};
}
```

## Các bài toán
 * [TIMUS 1664 Pipeline Transportation](https://acm.timus.ru/problem.aspx?space=1&num=1664)
 * [TIMUS 1681 Brother Bear's Garden](https://acm.timus.ru/problem.aspx?space=1&num=1681)