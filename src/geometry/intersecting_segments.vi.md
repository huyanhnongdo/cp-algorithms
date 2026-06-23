---
tags:
  - Translated
e_maxx_link: intersecting_segments
lang: vi
---
# Tìm kiếm một cặp đoạn thẳng cắt nhau

Cho $n$ đoạn thẳng trên mặt phẳng. Cần kiểm tra xem có ít nhất hai đoạn thẳng nào cắt nhau hay không.
Nếu câu trả lời là có, hãy in ra cặp đoạn thẳng cắt nhau đó; chỉ cần chọn bất kỳ cặp nào trong số nhiều trường hợp có thể xảy ra.

Thuật toán vét cạn (brute force) là lặp qua tất cả các cặp đoạn thẳng trong $O(n^2)$ và kiểm tra từng cặp xem chúng có cắt nhau hay không. Bài viết này mô tả một thuật toán với độ phức tạp thời gian $O(n \log n)$, dựa trên **thuật toán quét đường (sweep line algorithm)**.

## Thuật toán

Hãy tưởng tượng một đường thẳng đứng $x = -\infty$ và bắt đầu di chuyển đường thẳng này sang bên phải.
Trong quá trình di chuyển, đường thẳng này sẽ gặp các đoạn thẳng, và tại mỗi thời điểm một đoạn thẳng cắt đường thẳng của chúng ta, nó sẽ cắt tại đúng một điểm (chúng ta giả định rằng không có đoạn thẳng đứng nào).

<div style="text-align: center;" markdown="1">

![sweep line và sự giao nhau của đoạn thẳng](sweep_line_1.png)

</div>

Như vậy, với mỗi đoạn thẳng, tại một thời điểm nào đó, điểm của nó sẽ xuất hiện trên đường quét, sau đó theo sự di chuyển của đường thẳng, điểm này sẽ di chuyển, và cuối cùng, tại một thời điểm nào đó, đoạn thẳng sẽ biến mất khỏi đường thẳng.

Chúng ta quan tâm đến **thứ tự tương đối của các đoạn thẳng** dọc theo chiều thẳng đứng.
Cụ thể, chúng ta sẽ lưu trữ một danh sách các đoạn thẳng cắt đường quét tại một thời điểm nhất định, trong đó các đoạn thẳng sẽ được sắp xếp theo tọa độ $y$ của chúng trên đường quét.

<div style="text-align: center;" markdown="1">

![thứ tự tương đối của các đoạn thẳng qua đường quét](sweep_line_2.png)

</div>

Thứ tự này rất thú vị vì các đoạn thẳng cắt nhau sẽ có cùng tọa độ $y$ tại ít nhất một thời điểm:

<div style="text-align: center;" markdown="1">

![điểm giao nhau có cùng tọa độ y](sweep_line_3.png)

</div>

Chúng ta phát biểu các khẳng định chính:

  - Để tìm một cặp cắt nhau, chỉ cần xem xét **các đoạn thẳng kề nhau** tại mỗi vị trí cố định của đường quét là đủ.
  - Chỉ cần xem xét đường quét không phải ở mọi vị trí thực $(-\infty \ldots +\infty)$, mà **chỉ tại những vị trí khi các đoạn thẳng mới xuất hiện hoặc các đoạn thẳng cũ biến mất**. Nói cách khác, chỉ cần giới hạn ở các vị trí bằng hoành độ các điểm đầu mút của các đoạn thẳng.
  - Khi một đoạn thẳng mới xuất hiện, chỉ cần **chèn** nó vào vị trí mong muốn trong danh sách thu được từ đường quét trước đó. Chúng ta chỉ cần kiểm tra sự giao nhau của **đoạn thẳng được thêm vào với các đoạn thẳng lân cận ngay phía trên và phía dưới trong danh sách**.
  - Nếu đoạn thẳng biến mất, chỉ cần **xóa** nó khỏi danh sách hiện tại. Sau đó, cần **kiểm tra sự giao nhau của các đoạn thẳng lân cận phía trên và phía dưới trong danh sách**.
  - Không tồn tại các thay đổi nào khác trong thứ tự các đoạn thẳng trong danh sách ngoài những thay đổi đã mô tả. Không cần kiểm tra giao nhau nào khác.

Để hiểu tính đúng đắn của các khẳng định này, các ghi chú sau là đủ:

  - Hai đoạn thẳng không giao nhau không bao giờ thay đổi **thứ tự tương đối** của chúng.<br>
    Thực tế, nếu một đoạn thẳng ban đầu nằm cao hơn đoạn kia, rồi sau đó lại thấp hơn, thì giữa hai thời điểm đó đã có sự giao nhau của hai đoạn thẳng này.
  - Hai đoạn thẳng không cắt nhau cũng không thể có cùng tọa độ $y$.
  - Từ đó suy ra tại thời điểm đoạn thẳng xuất hiện, chúng ta có thể tìm vị trí cho đoạn thẳng này trong hàng đợi, và chúng ta sẽ không phải sắp xếp lại đoạn thẳng này trong hàng đợi nữa: **thứ tự của nó so với các đoạn thẳng khác trong hàng đợi sẽ không thay đổi**.
  - Hai đoạn thẳng cắt nhau tại thời điểm giao điểm của chúng sẽ là lân cận của nhau trong hàng đợi.
  - Do đó, để tìm các cặp đoạn thẳng cắt nhau, chỉ cần kiểm tra sự giao nhau của tất cả và chỉ những cặp đoạn thẳng mà tại một thời điểm nào đó trong quá trình di chuyển của đường quét, ít nhất một lần là lân cận của nhau.<br>
    Dễ thấy rằng chỉ cần kiểm tra đoạn thẳng được thêm vào với các lân cận trên và dưới của nó, cũng như khi xóa đoạn thẳng — các lân cận trên và dưới của nó (mà sau khi xóa sẽ trở thành lân cận của nhau).<br>
  - Cần lưu ý rằng tại một vị trí cố định của đường quét, chúng ta phải **thêm tất cả các đoạn thẳng** bắt đầu tại hoành độ này trước, và chỉ sau đó mới **xóa tất cả các đoạn thẳng** kết thúc tại đó.<br>
    Nhờ vậy, chúng ta không bỏ lỡ sự giao nhau của các đoạn thẳng tại đỉnh: tức là các trường hợp khi hai đoạn thẳng có chung một đỉnh.
  - Lưu ý rằng **các đoạn thẳng đứng** thực sự không ảnh hưởng đến tính đúng đắn của thuật toán.<br>
    Các đoạn thẳng này được phân biệt bởi thực tế là chúng xuất hiện và biến mất cùng một lúc. Tuy nhiên, nhờ ghi chú trước, chúng ta biết rằng tất cả các đoạn thẳng sẽ được thêm vào hàng đợi trước, và chỉ sau đó chúng mới bị xóa. Do đó, nếu đoạn thẳng đứng cắt một đoạn thẳng khác được mở tại thời điểm đó (bao gồm cả chính nó), nó sẽ được phát hiện.<br>
    **Đặt các đoạn thẳng đứng ở đâu trong hàng đợi?** Xét cho cùng, một đoạn thẳng đứng không có một tọa độ $y$ cụ thể, nó trải dài trên một đoạn dọc theo tọa độ $y$. Tuy nhiên, dễ hiểu rằng bất kỳ tọa độ nào từ đoạn này đều có thể được coi là tọa độ $y$.

Như vậy, toàn bộ thuật toán sẽ thực hiện không quá $2n$ lần kiểm tra sự giao nhau của một cặp đoạn thẳng, và thực hiện $O(n)$ thao tác với hàng đợi các đoạn thẳng ($O(1)$ thao tác tại thời điểm xuất hiện và biến mất của mỗi đoạn thẳng).

**Hành vi tiệm cận của thuật toán** do đó là $O(n \log n)$.

## Cài đặt

Chúng tôi trình bày cài đặt đầy đủ của thuật toán đã mô tả:

```cpp
const double EPS = 1E-9;

struct pt {
    double x, y;
};

struct seg {
    pt p, q;
    int id;

    double get_y(double x) const {
        if (abs(p.x - q.x) < EPS)
            return p.y;
        return p.y + (q.y - p.y) * (x - p.x) / (q.x - p.x);
    }
};

bool intersect1d(double l1, double r1, double l2, double r2) {
    if (l1 > r1)
        swap(l1, r1);
    if (l2 > r2)
        swap(l2, r2);
    return max(l1, l2) <= min(r1, r2) + EPS;
}

int vec(const pt& a, const pt& b, const pt& c) {
    double s = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
    return abs(s) < EPS ? 0 : s > 0 ? +1 : -1;
}

bool intersect(const seg& a, const seg& b)
{
    return intersect1d(a.p.x, a.q.x, b.p.x, b.q.x) &&
           intersect1d(a.p.y, a.q.y, b.p.y, b.q.y) &&
           vec(a.p, a.q, b.p) * vec(a.p, a.q, b.q) <= 0 &&
           vec(b.p, b.q, a.p) * vec(b.p, b.q, a.q) <= 0;
}

bool operator<(const seg& a, const seg& b)
{
    double x = max(min(a.p.x, a.q.x), min(b.p.x, b.q.x));
    return a.get_y(x) < b.get_y(x) - EPS;
}

struct event {
    double x;
    int tp, id;

    event() {}
    event(double x, int tp, int id) : x(x), tp(tp), id(id) {}

    bool operator<(const event& e) const {
        if (abs(x - e.x) > EPS)
            return x < e.x;
        return tp > e.tp;
    }
};

set<seg> s;
vector<set<seg>::iterator> where;

set<seg>::iterator prev(set<seg>::iterator it) {
    return it == s.begin() ? s.end() : --it;
}

set<seg>::iterator next(set<seg>::iterator it) {
    return ++it;
}

pair<int, int> solve(const vector<seg>& a) {
    int n = (int)a.size();
    vector<event> e;
    for (int i = 0; i < n; ++i) {
        e.push_back(event(min(a[i].p.x, a[i].q.x), +1, i));
        e.push_back(event(max(a[i].p.x, a[i].q.x), -1, i));
    }
    sort(e.begin(), e.end());

    s.clear();
    where.resize(a.size());
    for (size_t i = 0; i < e.size(); ++i) {
        int id = e[i].id;
        if (e[i].tp == +1) {
            set<seg>::iterator nxt = s.lower_bound(a[id]), prv = prev(nxt);
            if (nxt != s.end() && intersect(*nxt, a[id]))
                return make_pair(nxt->id, id);
            if (prv != s.end() && intersect(*prv, a[id]))
                return make_pair(prv->id, id);
            where[id] = s.insert(nxt, a[id]);
        } else {
            set<seg>::iterator nxt = next(where[id]), prv = prev(where[id]);
            if (nxt != s.end() && prv != s.end() && intersect(*nxt, *prv))
                return make_pair(prv->id, nxt->id);
            s.erase(where[id]);
        }
    }

    return make_pair(-1, -1);
}
```

Hàm chính ở đây là `solve()`, trả về các đoạn thẳng cắt nhau nếu tồn tại, hoặc $(-1, -1)$ nếu không có sự giao nhau nào.

Việc kiểm tra sự giao nhau của hai đoạn thẳng được thực hiện bởi hàm `intersect()`, sử dụng **thuật toán dựa trên diện tích có hướng của tam giác**.

Hàng đợi các đoạn thẳng là biến toàn cục `s`, một `set<event>`. Các bộ lặp (iterator) xác định vị trí của mỗi đoạn thẳng trong hàng đợi (để thuận tiện cho việc xóa đoạn thẳng khỏi hàng đợi) được lưu trữ trong mảng toàn cục `where`.

Hai hàm bổ trợ `prev()` và `next()` cũng được giới thiệu, trả về các bộ lặp tới các phần tử trước và sau (hoặc `end()`, nếu không tồn tại).

Hằng số `EPS` biểu thị sai số của việc so sánh hai số thực (nó chủ yếu được sử dụng khi kiểm tra hai đoạn thẳng có cắt nhau hay không).

## Bài tập
 * [TIMUS 1469 No Smoking!](https://acm.timus.ru/problem.aspx?space=1&num=1469)