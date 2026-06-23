---
tags:
  - Translated
e_maxx_link: preflow_push
lang: vi
---

# Luồng cực đại - Thuật toán Push-relabel

Thuật toán push-relabel (còn được gọi là thuật toán đẩy-nhãn - preflow-push) là một thuật toán dùng để tính toán luồng cực đại trên một mạng luồng.
Định nghĩa chính xác của bài toán cần giải có thể được tìm thấy trong bài viết [Luồng cực đại - Ford-Fulkerson và Edmonds-Karp](edmonds_karp.md).

Trong bài viết này chúng ta sẽ xem xét giải quyết bài toán bằng cách đẩy luồng tiền phong (preflow) qua mạng, thuật toán này sẽ chạy trong thời gian $O(V^4)$, hay chính xác hơn là $O(V^2 E)$.
Thuật toán được thiết kế bởi Andrew Goldberg và Robert Tarjan vào năm 1985.

## Định nghĩa

Trong suốt quá trình thực hiện thuật toán, chúng ta phải xử lý một **luồng tiền phong** (preflow) - tức là một hàm $f$ tương tự như hàm luồng, nhưng không nhất thiết phải thỏa mãn ràng buộc bảo toàn luồng.
Với luồng tiền phong, chỉ cần các ràng buộc sau được thỏa mãn:

$$0 \le f(e) \le c(e)$$

và

$$\sum_{(v, u) \in E} f((v, u)) \ge \sum_{(u, v) \in E} f((u, v))$$

Do đó, một đỉnh hoàn toàn có thể nhận được nhiều luồng hơn lượng luồng mà nó phân phối.
Chúng ta nói rằng đỉnh này có một lượng luồng dư, và định nghĩa lượng dư này bằng hàm **dư** (excess): $x(u) =\sum_{(v, u) \in E} f((v, u)) - \sum_{(u, v) \in E} f((u, v))$.

Tương tự như với hàm luồng, chúng ta có thể định nghĩa sức chứa thặng dư và đồ thị thặng dư đối với hàm luồng tiền phong.

Thuật toán sẽ bắt đầu với một luồng tiền phong ban đầu (một số đỉnh có phần dư), và trong quá trình thực hiện, luồng tiền phong này sẽ được xử lý và sửa đổi.
Nói qua một chút về chi tiết, thuật toán sẽ chọn một đỉnh có lượng dư và đẩy lượng dư đó sang các đỉnh lân cận.
Nó sẽ lặp lại việc này cho đến khi tất cả các đỉnh, ngoại trừ nguồn và đích, không còn lượng dư.
Dễ thấy rằng, một luồng tiền phong không có đỉnh nào dư chính là một luồng hợp lệ.
Điều này giúp thuật toán kết thúc với một luồng thực sự.

Tuy nhiên vẫn còn hai vấn đề chúng ta cần giải quyết:
Thứ nhất, làm thế nào để đảm bảo thuật toán chắc chắn kết thúc?
Và thứ hai, làm thế nào để đảm bảo luồng thu được thực sự là luồng cực đại, chứ không phải là một luồng ngẫu nhiên bất kỳ?

Để giải quyết những vấn đề này, chúng ta cần sự trợ giúp của một hàm khác, đó là hàm **nhãn** (labeling) $h$, thường được gọi là hàm **chiều cao** (height), gán cho mỗi đỉnh một số nguyên.
Chúng ta gọi một nhãn là hợp lệ nếu $h(s) = |V|$, $h(t) = 0$, và $h(u) \le h(v) + 1$ nếu có cạnh $(u, v)$ trong đồ thị thặng dư - tức là cạnh $(u, v)$ có sức chứa thặng dư dương.
Nói cách khác, nếu có thể tăng luồng từ $u$ sang $v$, thì chiều cao của $v$ chỉ có thể nhỏ hơn chiều cao của $u$ tối đa là 1, hoặc có thể bằng hoặc thậm chí cao hơn.

Một điểm quan trọng cần lưu ý là nếu tồn tại một hàm nhãn hợp lệ, thì sẽ không tồn tại đường tăng luồng từ $s$ đến $t$ trong đồ thị thặng dư.
Bởi vì một đường đi như vậy sẽ có độ dài tối đa là $|V| - 1$ cạnh, và mỗi cạnh chỉ có thể làm giảm chiều cao đi tối đa là 1, điều này là bất khả thi nếu chiều cao đầu tiên là $h(s) = |V|$ và chiều cao cuối cùng là $h(t) = 0$.

Sử dụng hàm nhãn này, chúng ta có thể phát biểu chiến lược của thuật toán push-relabel như sau:
Chúng ta bắt đầu với một luồng tiền phong hợp lệ và một hàm nhãn hợp lệ.
Tại mỗi bước, chúng ta đẩy một lượng dư giữa các đỉnh và cập nhật nhãn của các đỉnh.
Chúng ta phải đảm bảo rằng sau mỗi bước, luồng tiền phong và nhãn vẫn hợp lệ.
Khi thuật toán kết thúc, luồng tiền phong sẽ trở thành một luồng hợp lệ.
Và vì chúng ta luôn duy trì một nhãn hợp lệ, nên không tồn tại đường đi giữa $s$ và $t$ trong đồ thị thặng dư, điều này có nghĩa là luồng thu được chính là luồng cực đại.

Nếu so sánh thuật toán Ford-Fulkerson với thuật toán push-relabel, có vẻ như hai thuật toán này là đối ngẫu của nhau.
Thuật toán Ford-Fulkerson luôn duy trì một luồng hợp lệ tại mọi thời điểm và cải thiện nó cho đến khi không còn đường tăng luồng nào, trong khi thuật toán push-relabel luôn đảm bảo không có đường tăng luồng tại mọi thời điểm, và chúng ta cải thiện luồng tiền phong cho đến khi nó trở thành một luồng hợp lệ.

## Thuật toán

Trước tiên chúng ta phải khởi tạo đồ thị với một luồng tiền phong và hàm nhãn hợp lệ.

Sử dụng luồng rỗng - như cách làm trong thuật toán Ford-Fulkerson - là không thể, vì khi đó sẽ tồn tại một đường tăng luồng và điều này ngụ ý rằng không tồn tại nhãn hợp lệ.
Do đó, chúng ta sẽ khởi tạo mỗi cạnh đi ra từ $s$ bằng sức chứa tối đa của nó: $f((s, u)) = c((s, u))$.
Và tất cả các cạnh khác bằng 0.
Trong trường hợp này, tồn tại một nhãn hợp lệ, cụ thể là $h(s) = |V|$ cho đỉnh nguồn và $h(u) = 0$ cho tất cả các đỉnh khác.

Bây giờ hãy mô tả hai thao tác chi tiết hơn.

Với thao tác đẩy luồng (`push`), chúng ta cố gắng đẩy nhiều nhất có thể lượng luồng dư từ một đỉnh $u$ sang đỉnh lân cận $v$.
Chúng ta có một quy tắc: chỉ được phép đẩy luồng từ $u$ sang $v$ nếu $h(u) = h(v) + 1$.
Nói một cách nôm na, luồng dư phải chảy xuống phía dưới, nhưng không được quá dốc.
Tất nhiên, chúng ta chỉ có thể đẩy tối đa một lượng luồng là $\min(x(u), c((u, v)) - f((u, v)))$.

Nếu một đỉnh có lượng dư nhưng không thể đẩy lượng dư này sang bất kỳ đỉnh kề nào, thì chúng ta cần phải tăng chiều cao của đỉnh này.
Chúng ta gọi thao tác này là áp nhãn (`relabel`).
Chúng ta sẽ tăng chiều cao của nó nhiều nhất có thể, miễn là vẫn duy trì tính hợp lệ của nhãn.

Tóm lại, thuật toán có thể được tóm tắt như sau:
Chúng ta khởi tạo luồng tiền phong và hàm nhãn hợp lệ.
Chừng nào còn có thể thực hiện thao tác đẩy luồng (`push`) hoặc áp nhãn (`relabel`), chúng ta thực hiện chúng.
Sau đó, luồng tiền phong thực sự trở thành một luồng hợp lệ và chúng ta trả về nó.

## Độ phức tạp

Dễ dàng chứng minh được rằng nhãn lớn nhất của một đỉnh là $2|V| - 1$.
Tại thời điểm này, tất cả lượng dư còn lại có thể và sẽ được đẩy ngược trở lại nguồn.
Điều này dẫn đến tối đa $O(V^2)$ thao tác áp nhãn.

Người ta cũng chứng minh được rằng sẽ có tối đa $O(V E)$ lần đẩy bão hòa (lần đẩy sử dụng hết sức chứa thặng dư của cạnh) và tối đa $O(V^2 E)$ lần đẩy không bão hòa (lần đẩy không sử dụng hết sức chứa thặng dư của cạnh).
Nếu chọn một cấu trúc dữ liệu cho phép tìm đỉnh tiếp theo có lượng dư trong $O(1)$, tổng độ phức tạp của thuật toán sẽ là $O(V^2 E)$.

## Cài đặt

```{.cpp file=push_relabel}
const int inf = 1000000000;

int n;
vector<vector<int>> capacity, flow;
vector<int> height, excess, seen;
queue<int> excess_vertices;

void push(int u, int v) {
    int d = min(excess[u], capacity[u][v] - flow[u][v]);
    flow[u][v] += d;
    flow[v][u] -= d;
    excess[u] -= d;
    excess[v] += d;
    if (d && excess[v] == d)
        excess_vertices.push(v);
}

void relabel(int u) {
    int d = inf;
    for (int i = 0; i < n; i++) {
        if (capacity[u][i] - flow[u][i] > 0)
            d = min(d, height[i]);
    }
    if (d < inf)
        height[u] = d + 1;
}

void discharge(int u) {
    while (excess[u] > 0) {
        if (seen[u] < n) {
            int v = seen[u];
            if (capacity[u][v] - flow[u][v] > 0 && height[u] > height[v])
                push(u, v);
            else 
                seen[u]++;
        } else {
            relabel(u);
            seen[u] = 0;
        }
    }
}

int max_flow(int s, int t) {
    height.assign(n, 0);
    height[s] = n;
    flow.assign(n, vector<int>(n, 0));
    excess.assign(n, 0);
    excess[s] = inf;
    for (int i = 0; i < n; i++) {
    	if (i != s)
	        push(s, i);
    }
    seen.assign(n, 0);

    while (!excess_vertices.empty()) {
        int u = excess_vertices.front();
        excess_vertices.pop();
        if (u != s && u != t)
            discharge(u);
    }

    int max_flow = 0;
    for (int i = 0; i < n; i++)
        max_flow += flow[i][t];
    return max_flow;
}
```

Ở đây chúng ta sử dụng hàng đợi `excess_vertices` để lưu trữ tất cả các đỉnh hiện đang có lượng dư.
Bằng cách đó, chúng ta có thể chọn đỉnh tiếp theo để thực hiện thao tác đẩy luồng hoặc áp nhãn trong thời gian hằng số.

Và để đảm bảo không mất quá nhiều thời gian tìm đỉnh kề có thể đẩy luồng sang, chúng ta sử dụng cấu trúc dữ liệu gọi là **cung hiện tại** (current-arc).
Về cơ bản, chúng ta sẽ duyệt qua các cạnh theo vòng tròn và luôn lưu lại cạnh cuối cùng được sử dụng.
Bằng cách này, ứng với một giá trị nhãn cụ thể, chúng ta chỉ thay đổi cạnh hiện tại $O(n)$ lần.
Và vì thao tác áp nhãn đã mất $O(n)$ thời gian, điều này không làm độ phức tạp thuật toán tệ hơn.
