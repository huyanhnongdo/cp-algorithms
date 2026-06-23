---
tags:
  - Translated
e_maxx_link: edmonds_karp
lang: vi
---

# Luồng cực đại - Ford-Fulkerson và Edmonds-Karp

Thuật toán Edmonds-Karp là một cài đặt cụ thể của phương pháp Ford-Fulkerson dùng để tính luồng cực đại trên một mạng luồng.

## Mạng luồng

Trước tiên, hãy định nghĩa **mạng luồng** (flow network), **luồng** (flow), và **luồng cực đại** (maximum flow) là gì.

Một **mạng** (network) là một đồ thị có hướng $G$ với tập đỉnh $V$ và tập cạnh $E$, kết hợp với một hàm $c$ gán cho mỗi cạnh $e \in E$ một giá trị nguyên không âm, gọi là **sức chứa** (capacity) của $e$.
Một mạng như vậy được gọi là **mạng luồng** (flow network) nếu chúng ta xác định thêm hai đỉnh đặc biệt: một đỉnh gọi là **nguồn** (source) và một đỉnh gọi là **đích** (sink).

Một **luồng** (flow) trên mạng luồng là một hàm $f$ gán cho mỗi cạnh $e$ một giá trị nguyên không âm.
Hàm này phải thỏa mãn hai điều kiện sau:

Luồng trên mỗi cạnh không vượt quá sức chứa của cạnh đó.

$$f(e) \le c(e)$$

Và tổng lượng luồng đi vào một đỉnh $u$ bất kỳ phải bằng tổng lượng luồng đi ra khỏi đỉnh $u$ đó, ngoại trừ ở các đỉnh nguồn và đỉnh đích.

$$\sum_{(v, u) \in E} f((v, u)) = \sum_{(u, v) \in E} f((u, v))$$

Đỉnh nguồn $s$ chỉ có luồng đi ra, và đỉnh đích $t$ chỉ có luồng đi vào.

Dễ thấy rằng phương trình sau luôn được thỏa mãn:

$$\sum_{(s, u) \in E} f((s, u)) = \sum_{(u, t) \in E} f((u, t))$$

Một hình ảnh tương tự trực quan cho mạng luồng là:
Chúng ta biểu diễn các cạnh như các ống nước, sức chứa của một cạnh là lượng nước tối đa có thể chảy qua ống đó trong một giây, và luồng của một cạnh là lượng nước thực tế đang chảy qua ống đó trong một giây.
Điều này giải thích cho điều kiện luồng thứ nhất: không thể có nhiều nước chảy qua ống hơn sức chứa của nó.
Các đỉnh đóng vai trò là các điểm nối, nơi nước chảy ra từ một số ống và được phân phối theo cách nào đó vào các ống khác.
Điều này giải thích cho điều kiện luồng thứ hai: tại mỗi điểm nối, lượng nước đi vào phải bằng lượng nước đi ra. Nước không thể tự nhiên sinh ra hay mất đi.
Đỉnh nguồn $s$ là nơi bắt đầu của tất cả lượng nước, và nước chỉ có thể thoát ra ở đỉnh đích $t$.

Hình dưới đây cho thấy một mạng luồng.
Giá trị đầu tiên của mỗi cạnh đại diện cho luồng (ban đầu bằng 0), và giá trị thứ hai đại diện cho sức chứa.
<div style="text-align: center;" markdown="1">

![Flow network](Flow1.png)

</div>

Giá trị của luồng trên một mạng là tổng lượng luồng được tạo ra tại đỉnh nguồn $s$, hoặc tương đương, bằng tổng lượng luồng đi vào đỉnh đích $t$.
Một **luồng cực đại** (maximum flow) là một luồng có giá trị lớn nhất có thể đạt được.
Tìm luồng cực đại của một mạng luồng chính là bài toán chúng ta muốn giải quyết.

Trong bài toán ống nước, câu hỏi có thể phát biểu như sau:
lượng nước tối đa có thể đẩy qua các đường ống từ nguồn đến đích là bao nhiêu?

Hình dưới đây cho thấy luồng cực đại trong mạng luồng.
<div style="text-align: center;" markdown="1">

![Maximal flow](Flow9.png)

</div>

## Phương pháp Ford-Fulkerson

Hãy định nghĩa thêm một khái niệm nữa.
**Sức chứa thặng dư** (residual capacity) của một cạnh có hướng là sức chứa trừ đi luồng hiện tại trên cạnh đó.
Cần lưu ý rằng nếu có một luồng chảy dọc theo cạnh có hướng $(u, v)$, thì cạnh ngược $(v, u)$ có sức chứa bằng 0 và chúng ta có thể định nghĩa luồng của nó là $f((v, u)) = -f((u, v))$.
Điều này cũng giúp định nghĩa sức chứa thặng dư cho tất cả các cạnh ngược.
Chúng ta có thể tạo ra một **mạng thặng dư** (residual network) từ tất cả các cạnh này. Đây là mạng có cùng tập đỉnh và tập cạnh, nhưng sử dụng sức chứa thặng dư làm sức chứa của các cạnh.

Phương pháp Ford-Fulkerson hoạt động như sau:
Đầu tiên, ta đặt luồng của tất cả các cạnh bằng 0.
Sau đó, ta tìm một **đường tăng luồng** (augmenting path) từ $s$ đến $t$.
Đường tăng luồng là một đường đi đơn trên đồ thị thặng dư sao cho tất cả các cạnh dọc theo đường đi đó đều có sức chứa thặng dư dương.
Nếu tìm thấy một đường đi như vậy, chúng ta có thể tăng luồng dọc theo các cạnh này.
Chúng ta tiếp tục tìm kiếm các đường tăng luồng và tăng luồng.
Khi không còn tồn tại đường tăng luồng nào nữa, luồng hiện tại là luồng cực đại.

Hãy làm rõ hơn việc tăng luồng dọc theo một đường tăng luồng có nghĩa là gì.
Gọi $C$ là sức chứa thặng dư nhỏ nhất của các cạnh trên đường đi.
Khi đó chúng ta tăng luồng như sau:
chúng ta cập nhật $f((u, v)) ~\text{+=}~ C$ và $f((v, u)) ~\text{-=}~ C$ cho mỗi cạnh $(u, v)$ trên đường đi.

Dưới đây là một ví dụ minh họa phương pháp này.
Chúng ta sử dụng mạng luồng tương tự như trên.
Ban đầu chúng ta bắt đầu với luồng bằng 0.
<div style="text-align: center;" markdown="1">

![Flow network](Flow1.png)

</div>

Chúng ta có thể tìm thấy đường đi $s - A - B - t$ với sức chứa thặng dư lần lượt là 7, 5, và 8.
Giá trị nhỏ nhất của chúng là 5, do đó chúng ta có thể tăng luồng dọc theo đường đi này thêm 5.
Mạng luồng hiện tại có giá trị luồng là 5.
<div style="text-align: center;" markdown="1">

![First path](Flow2.png)
![Network after first path](Flow3.png)

</div>

Tiếp tục tìm đường tăng luồng, lần này ta tìm thấy $s - D - A - C - t$ với các sức chứa thặng dư là 4, 3, 3, và 5.
Do đó, chúng ta có thể tăng luồng thêm 3, tổng luồng của mạng tăng lên thành 8.
<div style="text-align: center;" markdown="1">

![Second path](Flow4.png)
![Network after second path](Flow5.png)

</div>

Lần này chúng ta tìm thấy đường đi $s - D - C - B - t$ với các sức chứa thặng dư là 1, 2, 3, và 3, do đó ta tăng luồng thêm 1.
<div style="text-align: center;" markdown="1">

![Third path](Flow6.png)
![Network after third path](Flow7.png)

</div>

Bây giờ, chúng ta tìm thấy đường tăng luồng $s - A - D - C - t$ với các sức chứa thặng dư là 2, 3, 1, và 2.
Chúng ta có thể tăng luồng thêm 1.
Đường đi này rất thú vị vì nó bao gồm cạnh ngược $(A, D)$.
Trong mạng luồng ban đầu, chúng ta không được phép truyền bất kỳ luồng nào từ $A$ đến $D$.
Nhưng vì chúng ta đã có luồng là 3 từ $D$ đến $A$, việc này là hoàn toàn có thể.
Ý nghĩa thực tế của việc này như sau:
Thay vì truyền luồng 3 từ $D$ đến $A$, chúng ta chỉ truyền 2 và bù lại bằng cách truyền thêm 1 từ $s$ đến $A$, điều này cho phép chúng ta truyền thêm 1 dọc theo đường đi $D - C - t$.
<div style="text-align: center;" markdown="1">

![Fourth path](Flow8.png)
![Network after fourth path](Flow9.png)

</div>

Hiện tại, không thể tìm thấy bất kỳ đường tăng luồng nào giữa $s$ và $t$, do đó luồng có giá trị $10$ chính là luồng cực đại có thể đạt được.
Chúng ta đã tìm thấy luồng cực đại.

Cần lưu ý rằng phương pháp Ford-Fulkerson không chỉ định thuật toán cụ thể nào để tìm đường tăng luồng.
Các phương pháp phổ biến là sử dụng [DFS](depth-first-search.md) hoặc [BFS](breadth-first-search.md), cả hai đều chạy trong $O(E)$.
Nếu tất cả sức chứa của mạng là các số nguyên, thì mỗi đường tăng luồng sẽ làm giá trị luồng của mạng tăng lên ít nhất 1 (xem thêm chi tiết tại [Định lý luồng nguyên](#integral-theorem)).
Do đó, độ phức tạp của Ford-Fulkerson là $O(E F)$, trong đó $F$ là giá trị luồng cực đại của mạng.
Trong trường hợp sức chứa là số hữu tỉ, thuật toán vẫn sẽ kết thúc nhưng độ phức tạp không bị chặn trên.
Trong trường hợp sức chứa là số vô tỉ, thuật toán có thể không bao giờ kết thúc, và thậm chí có thể không hội tụ về luồng cực đại.

## Thuật toán Edmonds-Karp

Thuật toán Edmonds-Karp đơn giản là một cài đặt của phương pháp Ford-Fulkerson sử dụng [BFS](breadth-first-search.md) để tìm các đường tăng luồng.
Thuật toán được công bố đầu tiên bởi Yefim Dinitz vào năm 1970, và sau đó được công bố độc lập bởi Jack Edmonds và Richard Karp vào năm 1972.

Độ phức tạp của thuật toán có thể được biểu diễn độc lập với luồng cực đại.
Thuật toán chạy trong thời gian $O(V E^2)$, ngay cả đối với sức chứa vô tỉ.
Ý tưởng là, mỗi lần chúng ta tìm thấy một đường tăng luồng, một trong các cạnh sẽ trở nên bão hòa (đạt sức chứa tối đa), và khoảng cách từ cạnh đó đến $s$ sẽ dài hơn nếu nó xuất hiện lại ở một đường tăng luồng sau đó.
Độ dài của đường đi đơn bị chặn bởi $V$.

### Cài đặt

Ma trận `capacity` lưu trữ sức chứa cho mỗi cặp đỉnh.
`adj` là danh sách kề của **đồ thị vô hướng**, vì chúng ta cũng cần sử dụng các cạnh ngược khi tìm kiếm các đường tăng luồng.

Hàm `maxflow` sẽ trả về giá trị của luồng cực đại.
Trong quá trình thực hiện thuật toán, ma trận `capacity` sẽ thực sự lưu trữ sức chứa thặng dư của mạng.
Giá trị luồng trên mỗi cạnh sẽ không được lưu trữ trực tiếp, nhưng có thể dễ dàng mở rộng cài đặt này - bằng cách sử dụng một ma trận bổ sung - để lưu trữ luồng và trả về nó.

```{.cpp file=edmondskarp}
int n;
vector<vector<int>> capacity;
vector<vector<int>> adj;

int bfs(int s, int t, vector<int>& parent) {
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2;
    queue<pair<int, int>> q;
    q.push({s, INF});

    while (!q.empty()) {
        int cur = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int next : adj[cur]) {
            if (parent[next] == -1 && capacity[cur][next]) {
                parent[next] = cur;
                int new_flow = min(flow, capacity[cur][next]);
                if (next == t)
                    return new_flow;
                q.push({next, new_flow});
            }
        }
    }

    return 0;
}

int maxflow(int s, int t) {
    int flow = 0;
    vector<int> parent(n);
    int new_flow;

    while (new_flow = bfs(s, t, parent)) {
        flow += new_flow;
        int cur = t;
        while (cur != s) {
            int prev = parent[cur];
            capacity[prev][cur] -= new_flow;
            capacity[cur][prev] += new_flow;
            cur = prev;
        }
    }

    return flow;
}
```

## Định lý luồng nguyên ## { #integral-theorem}

Định lý phát biểu rằng nếu mọi sức chứa trong mạng là số nguyên, thì giá trị của luồng cực đại cũng là số nguyên, và tồn tại một luồng cực đại sao cho luồng trên mỗi cạnh cũng là số nguyên. Đặc biệt, phương pháp Ford-Fulkerson luôn tìm ra một luồng như vậy.

## Định lý luồng cực đại lát cắt cực tiểu

Một **lát cắt $s$-$t$** là một cách phân hoạch các đỉnh của mạng luồng thành hai tập hợp sao cho một tập hợp chứa nguồn $s$ và tập hợp còn lại chứa đích $t$.
Sức chứa của lát cắt $s$-$t$ được định nghĩa bằng tổng sức chứa của các cạnh đi từ phía tập chứa nguồn sang tập chứa đích.

Rõ ràng, chúng ta không thể truyền một luồng từ $s$ đến $t$ lớn hơn sức chứa của bất kỳ lát cắt $s$-$t$ nào.
Do đó, luồng cực đại bị chặn trên bởi sức chứa của lát cắt nhỏ nhất (minimum cut).

Định lý luồng cực đại lát cắt cực tiểu còn chỉ ra nhiều hơn thế:
Nó phát biểu rằng giá trị của luồng cực đại bằng chính sức chứa của lát cắt nhỏ nhất.

Trong hình dưới đây, bạn có thể thấy lát cắt nhỏ nhất của mạng luồng mà chúng ta đã sử dụng trước đó.
Nó cho thấy sức chứa của lát cắt giữa $\{s, A, D\}$ và $\{B, C, t\}$ là $5 + 3 + 2 = 10$, bằng chính luồng cực đại chúng ta đã tìm thấy.
Các lát cắt khác sẽ có sức chứa lớn hơn, chẳng hạn sức chứa giữa $\{s, A\}$ và $\{B, C, D, t\}$ là $4 + 3 + 5 = 12$.
<div style="text-align: center;" markdown="1">

![Minimum cut](Cut.png)

</div>

Lát cắt nhỏ nhất có thể được tìm thấy sau khi thực hiện tính toán luồng cực đại bằng phương pháp Ford-Fulkerson.
Một lát cắt nhỏ nhất có thể được xác định như sau:
tập hợp tất cả các đỉnh có thể đến được từ $s$ trong đồ thị thặng dư (sử dụng các cạnh có sức chứa thặng dư dương), và tập hợp tất cả các đỉnh còn lại.
Phân hoạch này có thể được tìm thấy dễ dàng bằng cách sử dụng [DFS](depth-first-search.md) bắt đầu từ $s$.

## Bài tập thực hành
- [Codeforces - Array and Operations](https://codeforces.com/contest/498/problem/c)
- [Codeforces - Red-Blue Graph](https://codeforces.com/contest/1288/problem/f)
- [CSES - Download Speed](https://cses.fi/problemset/task/1694)
- [CSES - Police Chase](https://cses.fi/problemset/task/1695)
- [CSES - School Dance](https://cses.fi/problemset/task/1696)
- [CSES - Distinct Routes](https://cses.fi/problemset/task/1711)
