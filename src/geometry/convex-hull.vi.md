---
tags:
  - Translated
e_maxx_link: convex_hull_graham
lang: vi
---
# Xây dựng Bao lồi (Convex Hull)

Trong bài viết này, chúng ta sẽ thảo luận về bài toán xây dựng bao lồi (Convex Hull) từ một tập hợp các điểm.

Xét $N$ điểm cho trước trên một mặt phẳng, mục tiêu là tạo ra một bao lồi, nghĩa là đa giác lồi nhỏ nhất chứa tất cả các điểm đã cho.

Chúng ta sẽ tìm hiểu thuật toán **Graham's scan** được Graham công bố năm 1972 và thuật toán **Monotone chain** được Andrew công bố năm 1979. Cả hai đều có độ phức tạp thời gian $\mathcal{O}(N \log N)$ và đạt tối ưu tiệm cận (vì đã được chứng minh là không có thuật toán nào tốt hơn về mặt tiệm cận), ngoại trừ một vài trường hợp đặc biệt liên quan đến xử lý song song hoặc trực tuyến (online).

## Thuật toán Graham's scan
Thuật toán trước tiên tìm điểm thấp nhất $P_0$. Nếu có nhiều điểm cùng tọa độ Y, điểm có tọa độ X nhỏ hơn sẽ được chọn. Bước này tốn $\mathcal{O}(N)$ thời gian.

Tiếp theo, tất cả các điểm còn lại được sắp xếp theo góc cực (polar angle) theo chiều kim đồng hồ. Nếu hai hoặc nhiều điểm có cùng góc cực, thứ tự ưu tiên được quyết định bởi khoảng cách đến $P_0$ theo thứ tự tăng dần.

Sau đó, chúng ta duyệt qua từng điểm một và đảm bảo rằng điểm hiện tại cùng với hai điểm trước đó tạo thành một lượt rẽ theo chiều kim đồng hồ; nếu không, điểm trước đó sẽ bị loại bỏ vì nó sẽ tạo thành hình dạng không lồi. Việc kiểm tra tính chất cùng chiều hay ngược chiều kim đồng hồ có thể được thực hiện bằng cách kiểm tra [định hướng](oriented-triangle-area.md).

Chúng ta sử dụng một ngăn xếp (stack) để lưu trữ các điểm, và khi đã quay lại điểm ban đầu $P_0$, thuật toán hoàn tất và chúng ta trả về ngăn xếp chứa tất cả các điểm của bao lồi theo thứ tự chiều kim đồng hồ.

Nếu bạn cần bao gồm các điểm thẳng hàng khi thực hiện Graham scan, bạn cần thêm một bước sau khi sắp xếp. Bạn cần lấy các điểm có khoảng cách cực đại từ $P_0$ (các điểm này nên nằm ở cuối vector đã sắp xếp) và thẳng hàng với nhau. Các điểm trên đoạn này nên được đảo ngược thứ tự để có thể xuất ra tất cả các điểm thẳng hàng, nếu không thuật toán sẽ chỉ lấy điểm gần nhất trên đoạn đó và dừng lại. Bước này không nên bao gồm trong phiên bản không lấy các điểm thẳng hàng, nếu không bạn sẽ không thu được bao lồi nhỏ nhất.

### Cài đặt

```{.cpp file=graham_scan}
struct pt {
    double x, y;
    bool operator == (pt const& t) const {
        return x == t.x && y == t.y;
    }
};

int orientation(pt a, pt b, pt c) {
    double v = a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y);
    if (v < 0) return -1; // clockwise
    if (v > 0) return +1; // counter-clockwise
    return 0;
}

bool cw(pt a, pt b, pt c, bool include_collinear) {
    int o = orientation(a, b, c);
    return o < 0 || (include_collinear && o == 0);
}
bool collinear(pt a, pt b, pt c) { return orientation(a, b, c) == 0; }

void convex_hull(vector<pt>& a, bool include_collinear = false) {
    pt p0 = *min_element(a.begin(), a.end(), [](pt a, pt b) {
        return make_pair(a.y, a.x) < make_pair(b.y, b.x);
    });
    sort(a.begin(), a.end(), [&p0](const pt& a, const pt& b) {
        int o = orientation(p0, a, b);
        if (o == 0)
            return (p0.x-a.x)*(p0.x-a.x) + (p0.y-a.y)*(p0.y-a.y)
                < (p0.x-b.x)*(p0.x-b.x) + (p0.y-b.y)*(p0.y-b.y);
        return o < 0;
    });
    if (include_collinear) {
        int i = (int)a.size()-1;
        while (i >= 0 && collinear(p0, a[i], a.back())) i--;
        reverse(a.begin()+i+1, a.end());
    }

    vector<pt> st;
    for (int i = 0; i < (int)a.size(); i++) {
        while (st.size() > 1 && !cw(st[st.size()-2], st.back(), a[i], include_collinear))
            st.pop_back();
        st.push_back(a[i]);
    }

    if (include_collinear == false && st.size() == 2 && st[0] == st[1])
        st.pop_back();

    a = st;
}
```

## Thuật toán Monotone chain
Thuật toán trước tiên tìm điểm xa nhất về bên trái (A) và bên phải (B). Trong trường hợp có nhiều điểm như vậy, điểm thấp nhất trong số các điểm bên trái (tọa độ Y nhỏ nhất) được chọn làm A, và điểm cao nhất trong số các điểm bên phải (tọa độ Y lớn nhất) được chọn làm B. Rõ ràng, cả A và B đều phải thuộc về bao lồi vì chúng là các điểm xa nhất và không thể bị chứa bởi bất kỳ đường thẳng nào được tạo bởi một cặp điểm trong số các điểm đã cho.

Bây giờ, vẽ một đường thẳng đi qua AB. Đường thẳng này chia tất cả các điểm còn lại thành hai tập hợp, S1 và S2, trong đó S1 chứa tất cả các điểm nằm trên đường thẳng nối A và B, và S2 chứa tất cả các điểm nằm dưới đường thẳng nối A và B. Các điểm nằm trên đường thẳng nối A và B có thể thuộc về bất kỳ tập hợp nào. Điểm A và B thuộc về cả hai tập hợp. Bây giờ thuật toán xây dựng tập hợp phía trên S1 và tập hợp phía dưới S2, sau đó kết hợp chúng để thu được kết quả.

Để thu được tập hợp phía trên, chúng ta sắp xếp tất cả các điểm theo tọa độ x. Với mỗi điểm, chúng ta kiểm tra xem: nếu điểm hiện tại là điểm cuối cùng (được định nghĩa là B), hoặc nếu hướng giữa đường thẳng nối A với điểm hiện tại và đường thẳng nối điểm hiện tại với B là cùng chiều kim đồng hồ. Trong những trường hợp đó, điểm hiện tại thuộc về tập hợp phía trên S1. Việc kiểm tra định hướng có thể thực hiện thông qua [định hướng](oriented-triangle-area.md).

Nếu điểm đã cho thuộc về tập hợp phía trên, chúng ta kiểm tra góc tạo bởi đường thẳng nối điểm gần cuối và điểm cuối trong bao lồi phía trên với đường thẳng nối điểm cuối trong bao lồi phía trên và điểm hiện tại. Nếu góc đó không phải chiều kim đồng hồ, chúng ta loại bỏ điểm mới thêm vào gần nhất vì điểm hiện tại có thể bao chứa điểm trước đó sau khi được thêm vào bao lồi.

Logic tương tự áp dụng cho tập hợp phía dưới S2. Nếu điểm hiện tại là B, hoặc định hướng của các đường thẳng được tạo bởi A và điểm hiện tại, cũng như giữa điểm hiện tại và B là ngược chiều kim đồng hồ, thì nó thuộc về S2.

Nếu điểm đã cho thuộc về tập hợp phía dưới, chúng ta thực hiện tương tự như với tập hợp phía trên, ngoại trừ việc kiểm tra định hướng ngược chiều kim đồng hồ thay vì cùng chiều kim đồng hồ. Do đó, nếu góc tạo bởi đường thẳng nối điểm gần cuối và điểm cuối trong bao lồi phía dưới với đường thẳng nối điểm cuối trong bao lồi phía dưới và điểm hiện tại không phải ngược chiều kim đồng hồ, chúng ta loại bỏ điểm mới nhất đã thêm vào bao lồi phía dưới.

Bao lồi cuối cùng thu được từ hợp của bao lồi phía trên và phía dưới, tạo thành một bao lồi theo chiều kim đồng hồ, và cài đặt như sau.

Nếu bạn cần các điểm thẳng hàng, bạn chỉ cần kiểm tra chúng trong các quy trình kiểm tra chiều kim đồng hồ/ngược chiều kim đồng hồ. Tuy nhiên, điều này có thể dẫn đến trường hợp suy biến khi tất cả các điểm đầu vào thẳng hàng trên một đường thẳng, và thuật toán sẽ xuất ra các điểm bị lặp lại. Để giải quyết vấn đề này, chúng ta kiểm tra xem bao lồi phía trên có chứa tất cả các điểm hay không, nếu có, chúng ta chỉ cần trả về các điểm theo thứ tự ngược lại, vì đó là những gì cài đặt của Graham sẽ trả về trong trường hợp này.

### Cài đặt

```{.cpp file=monotone_chain}
struct pt {
    double x, y;
};

int orientation(pt a, pt b, pt c) {
    double v = a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y);
    if (v < 0) return -1; // clockwise
    if (v > 0) return +1; // counter-clockwise
    return 0;
}

bool cw(pt a, pt b, pt c, bool include_collinear) {
    int o = orientation(a, b, c);
    return o < 0 || (include_collinear && o == 0);
}
bool ccw(pt a, pt b, pt c, bool include_collinear) {
    int o = orientation(a, b, c);
    return o > 0 || (include_collinear && o == 0);
}

void convex_hull(vector<pt>& a, bool include_collinear = false) {
    if (a.size() == 1)
        return;

    sort(a.begin(), a.end(), [](pt a, pt b) {
        return make_pair(a.x, a.y) < make_pair(b.x, b.y);
    });
    pt p1 = a[0], p2 = a.back();
    vector<pt> up, down;
    up.push_back(p1);
    down.push_back(p1);
    for (int i = 1; i < (int)a.size(); i++) {
        if (i == a.size() - 1 || cw(p1, a[i], p2, include_collinear)) {
            while (up.size() >= 2 && !cw(up[up.size()-2], up[up.size()-1], a[i], include_collinear))
                up.pop_back();
            up.push_back(a[i]);
        }
        if (i == a.size() - 1 || ccw(p1, a[i], p2, include_collinear)) {
            while (down.size() >= 2 && !ccw(down[down.size()-2], down[down.size()-1], a[i], include_collinear))
                down.pop_back();
            down.push_back(a[i]);
        }
    }

    if (include_collinear && up.size() == a.size()) {
        reverse(a.begin(), a.end());
        return;
    }
    a.clear();
    for (int i = 0; i < (int)up.size(); i++)
        a.push_back(up[i]);
    for (int i = down.size() - 2; i > 0; i--)
        a.push_back(down[i]);
}
```

## Bài tập thực hành

* [Kattis - Convex Hull](https://open.kattis.com/problems/convexhull)
* [Kattis - Keep the Parade Safe](https://open.kattis.com/problems/parade)
* [Codeforces - I. Birthday](https://codeforces.com/contest/2172/problem/I)
* [Latin American Regionals 2006 - Onion Layers](https://matcomgrader.com/problem/9413/onion-layers/)
* [Timus 1185: Wall](http://acm.timus.ru/problem.aspx?space=1&num=1185)
* [Usaco 2014 January Contest, Gold - Cow Curling](http://usaco.org/index.php?page=viewproblem2&cpid=382)