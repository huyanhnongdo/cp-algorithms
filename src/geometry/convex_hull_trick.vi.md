---
tags:
  - Original
lang: vi
---
# Kỹ thuật bao lồi (Convex Hull Trick) và cây Li Chao

Xét bài toán sau đây: Có $n$ thành phố. Bạn muốn đi từ thành phố $1$ đến thành phố $n$ bằng xe hơi. Để làm điều này, bạn cần mua xăng. Biết rằng một lít xăng có giá $cost_k$ tại thành phố $k^{th}$. Ban đầu bình xăng của bạn rỗng và bạn tiêu thụ một lít xăng cho mỗi kilômét. Các thành phố nằm trên cùng một đường thẳng theo thứ tự tăng dần với thành phố $k^{th}$ có tọa độ $x_k$. Ngoài ra, bạn phải trả $toll_k$ phí để vào thành phố $k^{th}$. Nhiệm vụ của bạn là thực hiện chuyến đi với chi phí tối thiểu có thể. Rõ ràng là lời giải có thể được tính thông qua quy hoạch động (Dynamic Programming - DP):

$$dp_i = toll_i+\min\limits_{j<i}(cost_j \cdot (x_i - x_j)+dp_j)$$

Cách tiếp cận ngây thơ (Brute Force) sẽ cho bạn độ phức tạp $O(n^2)$, có thể cải thiện thành $O(n \log n)$ hoặc $O(n \log [C \varepsilon^{-1}])$ trong đó $C$ là giá trị $|x_i|$ lớn nhất có thể và $\varepsilon$ là độ chính xác mà $x_i$ được xem xét ($\varepsilon = 1$ cho số nguyên, trường hợp thường gặp). Để làm được điều này, ta cần lưu ý rằng bài toán có thể được quy về việc thêm các hàm tuyến tính $k \cdot x + b$ vào một tập hợp và tìm giá trị nhỏ nhất của các hàm tại một điểm $x$ cụ thể. Có hai phương pháp chính mà ta có thể sử dụng ở đây.

## Kỹ thuật bao lồi (Convex Hull Trick)

Ý tưởng của phương pháp này là duy trì bao lồi dưới (lower convex hull) của các hàm tuyến tính.
Thực tế, sẽ thuận tiện hơn khi coi chúng không phải là các hàm tuyến tính, mà là các điểm $(k;b)$ trên mặt phẳng sao cho ta phải tìm điểm có tích vô hướng nhỏ nhất với một điểm cho trước $(x;1)$, nghĩa là đối với điểm này, $kx+b$ được tối thiểu hóa, cũng chính là bài toán ban đầu.
Giá trị tối thiểu này nhất thiết sẽ nằm trên bao lồi dưới của các điểm này, như có thể thấy bên dưới:

<div style="text-align: center;" markdown="1">

![bao lồi dưới](convex_hull_trick.png)

</div>

Ta cần giữ các điểm trên bao lồi và các vector pháp tuyến của các cạnh bao.
Khi có một truy vấn $(x;1)$, bạn cần tìm vector pháp tuyến gần nó nhất xét về góc giữa chúng, khi đó hàm tuyến tính tối ưu sẽ tương ứng với một trong các điểm đầu mút của cạnh đó.
Để thấy điều này, cần lưu ý rằng các điểm có tích vô hướng không đổi với $(x;1)$ nằm trên một đường thẳng vuông góc với $(x;1)$, vì vậy hàm tuyến tính tối ưu sẽ là hàm có tiếp tuyến với bao lồi cùng phương với pháp tuyến của $(x;1)$ chạm vào bao.
Điểm này là điểm mà các pháp tuyến của các cạnh nằm bên trái và bên phải nó hướng về hai phía khác nhau của $(x;1)$.

Phương pháp này hữu ích khi các truy vấn thêm hàm tuyến tính có tính đơn điệu về $k$ hoặc nếu chúng ta xử lý ngoại tuyến (offline), tức là ta có thể thêm tất cả các hàm tuyến tính trước rồi mới trả lời các truy vấn sau.
Vì vậy, chúng ta không thể giải bài toán thành phố/xăng dầu bằng cách này.
Điều đó đòi hỏi phải xử lý các truy vấn trực tuyến (online).
Tuy nhiên, khi xử lý các truy vấn trực tuyến, mọi thứ trở nên khó khăn và người ta sẽ phải sử dụng một cấu trúc dữ liệu kiểu tập hợp nào đó để cài đặt bao lồi đúng cách.
Dẫu vậy, phương pháp trực tuyến sẽ không được đề cập trong bài viết này do độ khó của nó và vì phương pháp thứ hai (cây Li Chao) cho phép giải bài toán đơn giản hơn nhiều.
Cũng cần lưu ý rằng ta vẫn có thể sử dụng phương pháp này cho bài toán trực tuyến mà không gặp khó khăn bằng kỹ thuật chia căn (Sqrt Decomposition).
Nghĩa là, xây dựng lại bao lồi từ đầu sau mỗi $\sqrt n$ đường thẳng mới.

Để cài đặt phương pháp này, ta nên bắt đầu với một số hàm hình học tiện ích; ở đây chúng tôi đề xuất sử dụng kiểu số phức (complex) của C++.

```cpp
typedef int ftype;
typedef complex<ftype> point;
#define x real
#define y imag
 
ftype dot(point a, point b) {
	return (conj(a) * b).x();
}
 
ftype cross(point a, point b) {
	return (conj(a) * b).y();
}
```

Ở đây chúng ta giả định rằng khi các hàm tuyến tính được thêm vào, $k$ của chúng chỉ tăng dần và ta muốn tìm giá trị nhỏ nhất.
Ta sẽ lưu các điểm vào vector $hull$ và các vector pháp tuyến vào vector $vecs$.
Khi thêm một điểm mới, ta phải nhìn vào góc tạo bởi cạnh cuối cùng trong bao lồi và vector từ điểm cuối cùng trong bao lồi đến điểm mới.
Góc này phải được định hướng ngược chiều kim đồng hồ, nghĩa là tích vô hướng của vector pháp tuyến cuối cùng trong bao (hướng vào trong bao) và vector từ điểm cuối đến điểm mới phải không âm.
Chừng nào điều này không đúng, ta nên xóa điểm cuối cùng trong bao lồi cùng với cạnh tương ứng.

```cpp
vector<point> hull, vecs;
 
void add_line(ftype k, ftype b) {
    point nw = {k, b};
    while(!vecs.empty() && dot(vecs.back(), nw - hull.back()) < 0) {
        hull.pop_back();
        vecs.pop_back();
    }
    if(!hull.empty()) {
        vecs.push_back(1i * (nw - hull.back()));
    }
    hull.push_back(nw);
}
 
```
Bây giờ, để lấy giá trị nhỏ nhất tại một điểm, ta sẽ tìm vector pháp tuyến đầu tiên trong bao lồi hướng ngược chiều kim đồng hồ so với $(x;1)$. Điểm đầu mút bên trái của cạnh đó sẽ là câu trả lời. Để kiểm tra xem vector $a$ có không hướng ngược chiều kim đồng hồ so với vector $b$ hay không, ta nên kiểm tra xem tích chéo (cross product) $[a,b]$ của chúng có dương hay không.
```cpp
int get(ftype x) {
    point query = {x, 1};
    auto it = lower_bound(vecs.begin(), vecs.end(), query, [](point a, point b) {
        return cross(a, b) > 0;
    });
    return dot(query, hull[it - vecs.begin()]);
}
```

## Cây Li Chao

Giả sử bạn có một tập hợp các hàm sao cho mỗi hai hàm có thể cắt nhau tối đa một lần. Hãy giữ trong mỗi đỉnh của một cây phân đoạn (Segment Tree) một hàm theo cách mà nếu ta đi từ gốc đến lá, đảm bảo rằng một trong các hàm ta gặp trên đường đi sẽ là hàm cho giá trị nhỏ nhất tại lá đó. Hãy xem cách xây dựng nó.

Giả sử ta đang ở một đỉnh tương ứng với đoạn $[l,r)$ và hàm $f_{old}$ đang được giữ ở đó, và ta thêm hàm $f_{new}$. Khi đó điểm giao nhau sẽ nằm ở $[l;m)$ hoặc $[m;r)$ với $m=\left\lfloor\tfrac{l+r}{2}\right\rfloor$. Ta có thể tìm ra điều đó một cách hiệu quả bằng cách so sánh giá trị của các hàm tại điểm $l$ và $m$. Nếu hàm chiếm ưu thế thay đổi, thì giao điểm nằm ở $[l;m)$, ngược lại nó nằm ở $[m;r)$. Bây giờ, đối với nửa đoạn không có giao điểm, ta sẽ chọn hàm có giá trị nhỏ hơn và ghi nó vào đỉnh hiện tại. Bạn có thể thấy rằng đó luôn là hàm nhỏ hơn tại điểm $m$. Sau đó, ta đệ quy sang nửa còn lại của đoạn với hàm là hàm lớn hơn. Như bạn thấy, điều này sẽ giữ tính đúng đắn trên nửa đầu của đoạn và ở nửa còn lại, tính đúng đắn sẽ được duy trì trong quá trình gọi đệ quy. Do đó, ta có thể thêm các hàm và kiểm tra giá trị nhỏ nhất tại điểm trong $O(\log [C\varepsilon^{-1}])$.

Dưới đây là minh họa những gì xảy ra trong đỉnh khi ta thêm hàm mới:

<div style="text-align: center;" markdown="1">

![Đỉnh cây Li Chao](li_chao_vertex.png)

</div>

Hãy chuyển sang phần cài đặt. Một lần nữa, ta sẽ sử dụng số phức để lưu các hàm tuyến tính.

```{.cpp file=lichaotree_line_definition}
typedef long long ftype;
typedef complex<ftype> point;
#define x real
#define y imag
 
ftype dot(point a, point b) {
    return (conj(a) * b).x();
}
 
ftype f(point a,  ftype x) {
    return dot(a, {x, 1});
}
```
Ta sẽ lưu các hàm trong mảng $line$ và sử dụng chỉ số nhị phân của cây phân đoạn. Nếu bạn muốn sử dụng nó với số lớn hoặc kiểu `double`, bạn nên sử dụng cây phân đoạn động (dynamic segment tree). 
Cây phân đoạn nên được khởi tạo với các giá trị mặc định, ví dụ như các đường thẳng $0x + \infty$.

```{.cpp file=lichaotree_addline}
const int maxn = 2e5;
 
point line[4 * maxn];
 
void add_line(point nw, int v = 1, int l = 0, int r = maxn) {
    int m = (l + r) / 2;
    bool lef = f(nw, l) < f(line[v], l);
    bool mid = f(nw, m) < f(line[v], m);
    if(mid) {
        swap(line[v], nw);
    }
    if(r - l == 1) {
        return;
    } else if(lef != mid) {
        add_line(nw, 2 * v, l, m);
    } else {
        add_line(nw, 2 * v + 1, m, r);
    }
}
```
Bây giờ để lấy giá trị nhỏ nhất tại một điểm $x$, ta chỉ cần chọn giá trị nhỏ nhất dọc theo đường đi đến điểm đó.
```{.cpp file=lichaotree_getminimum}
ftype get(int x, int v = 1, int l = 0, int r = maxn) {
    int m = (l + r) / 2;
    if(r - l == 1) {
        return f(line[v], x);
    } else if(x < m) {
        return min(f(line[v], x), get(x, 2 * v, l, m));
    } else {
        return min(f(line[v], x), get(x, 2 * v + 1, m, r));
    }
}
```

## Các bài tập

* [Codebreaker - TROUBLES](https://codeforces.com/gym/103536/problem/B) (ứng dụng đơn giản của Kỹ thuật bao lồi sau một vài quan sát)
* [CS Academy - Squared Ends](https://csacademy.com/contest/archive/task/squared-ends)
* [Codeforces - Escape Through Leaf](http://codeforces.com/contest/932/problem/F)
* [CodeChef - Polynomials](https://www.codechef.com/NOV17/problems/POLY)
* [Codeforces - Kalila and Dimna in the Logging Industry](https://codeforces.com/problemset/problem/319/C)
* [Codeforces - Product Sum](https://codeforces.com/problemset/problem/631/E)
* [Codeforces - Bear and Bowling 4](https://codeforces.com/problemset/problem/660/F)
* [APIO 2010 - Commando](https://dmoj.ca/problem/apio10p1)