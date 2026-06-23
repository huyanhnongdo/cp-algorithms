---
tags:
  - Translated
e_maxx_link: mst_kruskal
lang: vi
---

# Cây khung nhỏ nhất - Thuật toán Kruskal

Cho một đồ thị vô hướng có trọng số.
Chúng ta muốn tìm một cây con của đồ thị này kết nối tất cả các đỉnh (tức là một cây khung) và có tổng trọng số nhỏ nhất (tức là tổng trọng số của tất cả các cạnh trong cây là nhỏ nhất) trong số tất cả các cây khung có thể có.
Cây khung này được gọi là cây khung nhỏ nhất (Minimum Spanning Tree - MST).

Trong hình bên trái, bạn có thể thấy một đồ thị vô hướng có trọng số, và trong hình bên phải là cây khung nhỏ nhất tương ứng của nó.

![Đồ thị ngẫu nhiên](MST_before.png) ![MST của đồ thị](MST_after.png)

Bài viết này sẽ thảo luận về một vài tính chất quan trọng liên quan đến cây khung nhỏ nhất, sau đó sẽ đưa ra cài đặt đơn giản nhất của thuật toán Kruskal để tìm cây khung nhỏ nhất.

## Tính chất của cây khung nhỏ nhất

* Cây khung nhỏ nhất của một đồ thị là duy nhất nếu trọng số của tất cả các cạnh đều đôi một phân biệt. Ngược lại, có thể tồn tại nhiều cây khung nhỏ nhất khác nhau.
  (Các thuật toán cụ thể thường in ra một trong số các cây khung nhỏ nhất có thể).
* Cây khung nhỏ nhất cũng là cây có tích trọng số các cạnh là nhỏ nhất.
  (Điều này có thể dễ dàng chứng minh bằng cách thay thế trọng số của tất cả các cạnh bằng logarit của chúng).
* Trong một cây khung nhỏ nhất của đồ thị, trọng số lớn nhất của một cạnh trong cây là nhỏ nhất có thể trong số tất cả các cây khung có thể của đồ thị đó.
  (Điều này được suy ra trực tiếp từ tính đúng đắn của thuật toán Kruskal).
* Cây khung lớn nhất (cây khung có tổng trọng số các cạnh lớn nhất) của một đồ thị có thể tìm được tương tự như cây khung nhỏ nhất, bằng cách đổi dấu trọng số của tất cả các cạnh thành số đối và áp dụng bất kỳ thuật toán tìm cây khung nhỏ nhất nào.

## Thuật toán Kruskal

Thuật toán này được mô tả bởi Joseph Bernard Kruskal, Jr. vào năm 1956.

Thuật toán Kruskal ban đầu coi tất cả các đỉnh của đồ thị gốc đứng độc lập với nhau, tạo thành một rừng gồm các cây chỉ có một nút duy nhất, và sau đó gộp dần các cây này lại với nhau, kết hợp tại mỗi bước bất kỳ hai cây nào bằng một cạnh của đồ thị gốc. Trước khi thực hiện thuật toán, tất cả các cạnh được sắp xếp theo trọng số (theo thứ tự không giảm). Sau đó bắt đầu quá trình hợp nhất: duyệt qua tất cả các cạnh từ đầu đến cuối (theo thứ tự đã sắp xếp), và nếu hai đầu của cạnh hiện tại thuộc về hai cây con khác nhau, hai cây con này sẽ được gộp lại làm một, và cạnh đó được thêm vào kết quả. Sau khi duyệt qua tất cả các cạnh, tất cả các đỉnh sẽ thuộc về cùng một cây con duy nhất, và chúng ta thu được kết quả cuối cùng.

## Cài đặt đơn giản nhất

Đoạn mã dưới đây cài đặt trực tiếp thuật toán đã mô tả ở trên, có độ phức tạp thời gian là $O(M \log M + N^2)$.
Sắp xếp các cạnh yêu cầu $O(M \log N)$ phép toán (tương đương với $O(M \log M)$).
Thông tin về việc một đỉnh thuộc về cây con nào được duy trì với sự trợ giúp của một mảng `tree_id[]` - đối với mỗi đỉnh `v`, `tree_id[v]` lưu trữ mã số của cây chứa đỉnh `v`.
Đối với mỗi cạnh, việc kiểm tra xem hai đầu của nó có thuộc các cây khác nhau hay không có thể thực hiện trong $O(1)$.
Cuối cùng, việc hợp nhất hai cây được thực hiện trong $O(N)$ bằng cách duyệt qua mảng `tree_id[]` để cập nhật lại mã số cây.
Vì tổng số thao tác hợp nhất tối đa là $N-1$, chúng ta thu được độ phức tạp tiệm cận là $O(M \log N + N^2)$.

```cpp
struct Edge {
    int u, v, weight;
    bool operator<(Edge const& other) {
        return weight < other.weight;
    }
};

int n;
vector<Edge> edges;

int cost = 0;
vector<int> tree_id(n);
vector<Edge> result;
for (int i = 0; i < n; i++)
    tree_id[i] = i;

sort(edges.begin(), edges.end());
   
for (Edge e : edges) {
    if (tree_id[e.u] != tree_id[e.v]) {
        cost += e.weight;
        result.push_back(e);

        int old_id = tree_id[e.u], new_id = tree_id[e.v];
        for (int i = 0; i < n; i++) {
            if (tree_id[i] == old_id)
                tree_id[i] = new_id;
        }
    }
}
```

## Chứng minh tính đúng đắn

Tại sao thuật toán Kruskal lại cho chúng ta kết quả chính xác?

Nếu đồ thị gốc liên thông, đồ thị kết quả cũng sẽ liên thông.
Vì nếu ngược lại, sẽ tồn tại hai thành phần có thể được kết nối bởi ít nhất một cạnh. Tuy nhiên điều này là không thể, vì Kruskal chắc chắn đã chọn một trong số các cạnh đó, do ID của hai thành phần là khác nhau.
Đồng thời đồ thị kết quả không chứa chu trình, vì chúng ta đã ngăn chặn điều này một cách tường minh trong thuật toán.
Do đó thuật toán tạo ra một cây khung.

Vậy tại sao cây khung này lại là nhỏ nhất?

Chúng ta có thể chứng minh khẳng định sau bằng quy nạp: "nếu $F$ là tập các cạnh được chọn bởi thuật toán tại bất kỳ thời điểm nào của quá trình chạy, thì luôn tồn tại một cây khung nhỏ nhất (MST) chứa tất cả các cạnh của $F$".

Khẳng định này hiển nhiên đúng ở bước khởi đầu, tập rỗng là tập con của mọi MST.

Bây giờ giả sử $F$ là tập cạnh tại một thời điểm của thuật toán, $T$ là một MST chứa $F$ và $e$ là cạnh mới tiếp theo mà chúng ta muốn thêm vào bằng thuật toán Kruskal.

Nếu $e$ tạo ra một chu trình, chúng ta không thêm nó vào, và khẳng định hiển nhiên vẫn đúng sau bước này.

Trong trường hợp $T$ đã chứa cạnh $e$, khẳng định cũng tiếp tục đúng sau bước này.

Trong trường hợp $T$ không chứa cạnh $e$, thì đồ thị $T + e$ sẽ chứa một chu trình $C$.
Chu trình này chứa ít nhất một cạnh $f$ không thuộc $F$.
Tập các cạnh $T - f + e$ cũng tạo thành một cây khung.
Lưu ý rằng trọng số của $f$ không thể nhỏ hơn trọng số của $e$, vì nếu không Kruskal đã chọn $f$ từ trước.
Nó cũng không thể có trọng số lớn hơn, vì điều đó sẽ làm cho tổng trọng số của $T - f + e$ nhỏ hơn tổng trọng số của $T$, điều này vô lý vì $T$ đã là một MST.
Điều này có nghĩa là trọng số của $e$ phải bằng trọng số của $f$.
Do đó, $T - f + e$ cũng là một MST và nó chứa tất cả các cạnh thuộc $F + e$.
Khẳng định vẫn tiếp tục được thỏa mãn sau bước này.

Như vậy khẳng định đã được chứng minh.
Điều này có nghĩa là sau khi duyệt qua tất cả các cạnh, tập cạnh thu được sẽ liên thông và là tập con của một MST, có nghĩa nó chính là một MST.

## Cải tiến cài đặt

Chúng ta có thể sử dụng cấu trúc dữ liệu [**Hợp nhất các tập hợp rời nhau (Disjoint Set Union - DSU)**](../data_structures/disjoint_set_union.md) để cài đặt thuật toán Kruskal nhanh hơn với độ phức tạp khoảng $O(M \log N)$. [Bài viết này](mst_kruskal_with_dsu.md) trình bày chi tiết về cách tiếp cận đó.

## Bài tập áp dụng

* [SPOJ - Koicost](http://www.spoj.com/problems/KOICOST/)
* [SPOJ - MaryBMW](http://www.spoj.com/problems/MARYBMW/)
* [Codechef - Fullmetal Alchemist](https://www.codechef.com/ICL2016/problems/ICL16A)
* [Codeforces - Edges in MST](http://codeforces.com/contest/160/problem/D)
* [UVA 12176 - Bring Your Own Horse](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3328)
* [UVA 10600 - ACM Contest and Blackout](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1541)
* [UVA 10724 - Road Construction](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1665)
* [Hackerrank - Roads in HackerLand](https://www.hackerrank.com/contests/june-world-codesprint/challenges/johnland/problem)
* [UVA 11710 - Expensive subway](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2757)
* [Codechef - Chefland and Electricity](https://www.codechef.com/problems/CHEFELEC)
* [UVA 10307 - Killing Aliens in Borg Maze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1248)
* [Codeforces - Flea](http://codeforces.com/problemset/problem/32/C)
* [Codeforces - Igon in Museum](http://codeforces.com/problemset/problem/598/D)
* [Codeforces - Hongcow Builds a Nation](http://codeforces.com/problemset/problem/744/A)
* [UVA - 908 - Re-connecting Computer Sites](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=849)
* [UVA 1208 - Oreon](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3649)
* [UVA 1235 - Anti Brute Force Lock](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3676)
* [UVA 10034 - Freckles](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=975)
* [UVA 11228 - Transportation system](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2169)
* [UVA 11631 - Dark roads](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2678)
* [UVA 11733 - Airports](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2833)
* [UVA 11747 - Heavy Cycle Edges](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2847)
* [SPOJ - Blinet](http://www.spoj.com/problems/BLINNET/)
* [SPOJ - Help the Old King](http://www.spoj.com/problems/IITKWPCG/)
* [Codeforces - Hierarchy](http://codeforces.com/contest/17/problem/B)
* [SPOJ - Modems](https://www.spoj.com/problems/EC_MODE/)
* [CSES - Road Reparation](https://cses.fi/problemset/task/1675)
* [CSES - Road Construction](https://cses.fi/problemset/task/1676)
