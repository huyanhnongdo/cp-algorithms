---
title: Point location in O(log n)
tags:
  - Original
lang: vi
---
# Xác định vị trí điểm trong $O(log n)$

Xét bài toán sau: cho một [phân hoạch phẳng](https://en.wikipedia.org/wiki/Planar_straight-line_graph) không chứa bất kỳ đỉnh bậc một hay bậc không nào, cùng với rất nhiều truy vấn.
Mỗi truy vấn là một điểm, chúng ta cần xác định mặt của phân hoạch mà điểm đó thuộc về.
Chúng ta sẽ trả lời mỗi truy vấn trong $O(\log n)$ theo cách ngoại tuyến (offline).<br>
Bài toán này có thể xuất hiện khi bạn cần định vị một số điểm trong biểu đồ Voronoi hoặc trong một đa giác đơn.

## Thuật toán

Trước tiên, với mỗi điểm truy vấn $p\ (x_0, y_0)$, chúng ta muốn tìm một cạnh sao cho nếu điểm đó nằm trên bất kỳ cạnh nào, thì điểm đó nằm trên cạnh chúng ta tìm thấy; nếu không, cạnh này phải cắt đường thẳng $x = x_0$ tại một điểm duy nhất $(x_0, y)$ sao cho $y < y_0$ và $y$ là giá trị lớn nhất trong tất cả các cạnh thỏa mãn điều kiện đó.
Hình ảnh sau đây minh họa cả hai trường hợp.

<div style="text-align: center;" markdown="1">

![Hình ảnh mục tiêu](point_location_goal.png)

</div>

Chúng ta sẽ giải quyết bài toán này ngoại tuyến bằng thuật toán quét đường (sweep line). Hãy duyệt qua các tọa độ x của các điểm truy vấn và các đầu mút của cạnh theo thứ tự tăng dần, đồng thời duy trì một tập hợp các cạnh $s$. Với mỗi tọa độ x, chúng ta sẽ thêm trước một số sự kiện.

Các sự kiện sẽ có bốn loại: _thêm_ (_add_), _xóa_ (_remove_), _dọc_ (_vertical_), _lấy_ (_get_).
Với mỗi cạnh dọc (cả hai đầu mút có cùng tọa độ x), chúng ta thêm một sự kiện _dọc_ cho tọa độ x tương ứng.
Với mọi cạnh khác, chúng ta thêm một sự kiện _thêm_ tại tọa độ x nhỏ nhất của các đầu mút và một sự kiện _xóa_ tại tọa độ x lớn nhất của các đầu mút.
Cuối cùng, với mỗi điểm truy vấn, chúng ta thêm một sự kiện _lấy_ tại tọa độ x của nó.

Với mỗi tọa độ x, chúng ta sẽ sắp xếp các sự kiện theo loại của chúng (theo thứ tự: _dọc_, _lấy_, _xóa_, _thêm_).
Hình ảnh dưới đây hiển thị tất cả các sự kiện đã được sắp xếp cho từng tọa độ x.

<div style="text-align: center;" markdown="1">

![Hình ảnh các sự kiện](point_location_events.png)

</div>

Chúng ta sẽ duy trì hai tập hợp trong quá trình quét đường.
Một tập hợp $t$ cho tất cả các cạnh không dọc, và một tập hợp $vert$ dành riêng cho các cạnh dọc.
Chúng ta sẽ xóa sạch tập hợp $vert$ khi bắt đầu xử lý mỗi tọa độ x.

Bây giờ, hãy xử lý các sự kiện cho một tọa độ x cố định.

 - Nếu nhận được sự kiện _dọc_, chúng ta chỉ cần chèn tọa độ y nhỏ nhất của đầu mút cạnh tương ứng vào $vert$.
 - Nếu nhận được sự kiện _xóa_ hoặc _thêm_, chúng ta xóa cạnh tương ứng khỏi $t$ hoặc thêm nó vào $t$.
 - Cuối cùng, với mỗi sự kiện _lấy_, chúng ta phải kiểm tra xem điểm đó có nằm trên cạnh dọc nào không bằng cách thực hiện tìm kiếm nhị phân (binary search) trong $vert$.
Nếu điểm không nằm trên cạnh dọc nào, chúng ta cần tìm câu trả lời cho truy vấn này trong $t$.
Để làm điều này, chúng ta lại thực hiện tìm kiếm nhị phân.
Để xử lý một số trường hợp suy biến (ví dụ: trong trường hợp tam giác $(0,~0)$, $(0,~2)$, $(1, 1)$ khi ta truy vấn điểm $(0,~0)$), chúng ta phải trả lời lại tất cả các sự kiện _lấy_ sau khi đã xử lý tất cả các sự kiện cho tọa độ x này và chọn kết quả tốt nhất trong hai câu trả lời.

Bây giờ hãy chọn một hàm so sánh cho tập hợp $t$.
Hàm so sánh này nên kiểm tra xem một cạnh có nằm phía trên cạnh kia với mọi tọa độ x mà cả hai đều bao phủ hay không. Giả sử ta có hai cạnh $(a, b)$ và $(c, d)$. Khi đó hàm so sánh là (giả mã):<br>

$val = sgn((b - a)\times(c - a)) + sgn((b - a)\times(d - a))$<br>
<b>if</b> $val \neq 0$<br>
<b>then return</b> $val > 0$<br>
$val = sgn((d - c)\times(a - c)) + sgn((d - c)\times(b - c))$<br>
<b>return</b> $val < 0$<br>

Bây giờ, với mỗi truy vấn, chúng ta đã có cạnh tương ứng.
Làm thế nào để tìm mặt?
Nếu không tìm được cạnh, nghĩa là điểm nằm ở mặt ngoài.
Nếu điểm thuộc cạnh vừa tìm được, mặt đó không duy nhất.
Nếu không, có hai ứng viên - các mặt được giới hạn bởi cạnh này.
Làm thế nào để kiểm tra mặt nào là câu trả lời? Lưu ý rằng cạnh đó không phải là cạnh dọc.
Khi đó, câu trả lời là mặt nằm phía trên cạnh này.
Hãy tìm mặt như vậy cho mỗi cạnh không dọc.
Xét một lượt duyệt ngược chiều kim đồng hồ của mỗi mặt.
Nếu trong quá trình duyệt này, tọa độ x tăng lên khi đi qua cạnh, thì mặt này chính là mặt cần tìm cho cạnh đó.

## Ghi chú

Trên thực tế, với các cây bền vững (persistent trees), cách tiếp cận này có thể được sử dụng để trả lời các truy vấn trực tuyến.

## Cài đặt

Đoạn mã sau được cài đặt cho số nguyên, nhưng có thể dễ dàng sửa đổi để làm việc với số thực (bằng cách thay đổi các phương thức so sánh và kiểu điểm).
Cài đặt này giả định rằng phân hoạch được lưu trữ chính xác bên trong một cấu trúc [DCEL](https://en.wikipedia.org/wiki/Doubly_connected_edge_list) và mặt ngoài được đánh số $-1$.<br>
Với mỗi truy vấn, một cặp $(1, i)$ được trả về nếu điểm nằm hoàn toàn bên trong mặt số $i$, và một cặp $(0, i)$ được trả về nếu điểm nằm trên cạnh số $i$.

```{.cpp file=point-location}
typedef long long ll;

bool ge(const ll& a, const ll& b) { return a >= b; }
bool le(const ll& a, const ll& b) { return a <= b; }
bool eq(const ll& a, const ll& b) { return a == b; }
bool gt(const ll& a, const ll& b) { return a > b; }
bool lt(const ll& a, const ll& b) { return a < b; }
int sgn(const ll& x) { return le(x, 0) ? eq(x, 0) ? 0 : -1 : 1; }

struct pt {
    ll x, y;
    pt() {}
    pt(ll _x, ll _y) : x(_x), y(_y) {}
    pt operator-(const pt& a) const { return pt(x - a.x, y - a.y); }
    ll dot(const pt& a) const { return x * a.x + y * a.y; }
    ll dot(const pt& a, const pt& b) const { return (a - *this).dot(b - *this); }
    ll cross(const pt& a) const { return x * a.y - y * a.x; }
    ll cross(const pt& a, const pt& b) const { return (a - *this).cross(b - *this); }
    bool operator==(const pt& a) const { return a.x == x && a.y == y; }
};

struct Edge {
    pt l, r;
};

bool edge_cmp(Edge* edge1, Edge* edge2)
{
    const pt a = edge1->l, b = edge1->r;
    const pt c = edge2->l, d = edge2->r;
    int val = sgn(a.cross(b, c)) + sgn(a.cross(b, d));
    if (val != 0)
        return val > 0;
    val = sgn(c.cross(d, a)) + sgn(c.cross(d, b));
    return val < 0;
}

enum EventType { DEL = 2, ADD = 3, GET = 1, VERT = 0 };

struct Event {
    EventType type;
    int pos;
    bool operator<(const Event& event) const { return type < event.type; }
};

vector<Edge*> sweepline(vector<Edge*> planar, vector<pt> queries)
{
    using pt_type = decltype(pt::x);

    // collect all x-coordinates
    auto s =
        set<pt_type, std::function<bool(const pt_type&, const pt_type&)>>(lt);
    for (pt p : queries)
        s.insert(p.x);
    for (Edge* e : planar) {
        s.insert(e->l.x);
        s.insert(e->r.x);
    }

    // map all x-coordinates to ids
    int cid = 0;
    auto id =
        map<pt_type, int, std::function<bool(const pt_type&, const pt_type&)>>(
            lt);
    for (auto x : s)
        id[x] = cid++;

    // create events
    auto t = set<Edge*, decltype(*edge_cmp)>(edge_cmp);
    auto vert_cmp = [](const pair<pt_type, int>& l,
                       const pair<pt_type, int>& r) {
        if (!eq(l.first, r.first))
            return lt(l.first, r.first);
        return l.second < r.second;
    };
    auto vert = set<pair<pt_type, int>, decltype(vert_cmp)>(vert_cmp);
    vector<vector<Event>> events(cid);
    for (int i = 0; i < (int)queries.size(); i++) {
        int x = id[queries[i].x];
        events[x].push_back(Event{GET, i});
    }
    for (int i = 0; i < (int)planar.size(); i++) {
        int lx = id[planar[i]->l.x], rx = id[planar[i]->r.x];
        if (lx > rx) {
            swap(lx, rx);
            swap(planar[i]->l, planar[i]->r);
        }
        if (lx == rx) {
            events[lx].push_back(Event{VERT, i});
        } else {
            events[lx].push_back(Event{ADD, i});
            events[rx].push_back(Event{DEL, i});
        }
    }

    // perform sweep line algorithm
    vector<Edge*> ans(queries.size(), nullptr);
    for (int x = 0; x < cid; x++) {
        sort(events[x].begin(), events[x].end());
        vert.clear();
        for (Event event : events[x]) {
            if (event.type == DEL) {
                t.erase(planar[event.pos]);
            }
            if (event.type == VERT) {
                vert.insert(make_pair(
                    min(planar[event.pos]->l.y, planar[event.pos]->r.y),
                    event.pos));
            }
            if (event.type == ADD) {
                t.insert(planar[event.pos]);
            }
            if (event.type == GET) {
                auto jt = vert.upper_bound(
                    make_pair(queries[event.pos].y, planar.size()));
                if (jt != vert.begin()) {
                    --jt;
                    int i = jt->second;
                    if (ge(max(planar[i]->l.y, planar[i]->r.y),
                           queries[event.pos].y)) {
                        ans[event.pos] = planar[i];
                        continue;
                    }
                }
                Edge* e = new Edge;
                e->l = e->r = queries[event.pos];
                auto it = t.upper_bound(e);
                if (it != t.begin())
                    ans[event.pos] = *(--it);
                delete e;
            }
        }

        for (Event event : events[x]) {
            if (event.type != GET)
                continue;
            if (ans[event.pos] != nullptr &&
                eq(ans[event.pos]->l.x, ans[event.pos]->r.x))
                continue;

            Edge* e = new Edge;
            e->l = e->r = queries[event.pos];
            auto it = t.upper_bound(e);
            delete e;
            if (it == t.begin())
                e = nullptr;
            else
                e = *(--it);
            if (ans[event.pos] == nullptr) {
                ans[event.pos] = e;
                continue;
            }
            if (e == nullptr)
                continue;
            if (e == ans[event.pos])
                continue;
            if (id[ans[event.pos]->r.x] == x) {
                if (id[e->l.x] == x) {
                    if (gt(e->l.y, ans[event.pos]->r.y))
                        ans[event.pos] = e;
                }
            } else {
                ans[event.pos] = e;
            }
        }
    }
    return ans;
}

struct DCEL {
    struct Edge {
        pt origin;
        Edge* nxt = nullptr;
        Edge* twin = nullptr;
        int face;
    };
    vector<Edge*> body;
};

vector<pair<int, int>> point_location(DCEL planar, vector<pt> queries)
{
    vector<pair<int, int>> ans(queries.size());
    vector<Edge*> planar2;
    map<intptr_t, int> pos;
    map<intptr_t, int> added_on;
    int n = planar.body.size();
    for (int i = 0; i < n; i++) {
        if (planar.body[i]->face > planar.body[i]->twin->face)
            continue;
        Edge* e = new Edge;
        e->l = planar.body[i]->origin;
        e->r = planar.body[i]->twin->origin;
        added_on[(intptr_t)e] = i;
        pos[(intptr_t)e] =
            lt(planar.body[i]->origin.x, planar.body[i]->twin->origin.x)
                ? planar.body[i]->face
                : planar.body[i]->twin->face;
        planar2.push_back(e);
    }
    auto res = sweepline(planar2, queries);
    for (int i = 0; i < (int)queries.size(); i++) {
        if (res[i] == nullptr) {
            ans[i] = make_pair(1, -1);
            continue;
        }
        pt p = queries[i];
        pt l = res[i]->l, r = res[i]->r;
        if (eq(p.cross(l, r), 0) && le(p.dot(l, r), 0)) {
            ans[i] = make_pair(0, added_on[(intptr_t)res[i]]);
            continue;
        }
        ans[i] = make_pair(1, pos[(intptr_t)res[i]]);
    }
    for (auto e : planar2)
        delete e;
    return ans;
}
```

## Bài tập
 * [TIMUS 1848 Fly Hunt](http://acm.timus.ru/problem.aspx?space=1&num=1848&locale=en)
 * [UVA 12310 Point Location](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=297&page=show_problem&problem=3732)