---
tags:
  - Translated
e_maxx_link: heavy_light
---

# Phân rã Heavy-Light

**Phân rã Heavy-light** (Heavy-light decomposition - HLD) là một kỹ thuật khá tổng quát cho phép chúng ta giải quyết hiệu quả nhiều bài toán liên quan đến **truy vấn trên cây** (queries on a tree).

## Mô tả

Cho một cây $G$ gồm $n$ đỉnh, với một đỉnh gốc bất kỳ.

Ý tưởng cốt lõi của phép phân rã cây này là **chia cây thành nhiều đường đi** sao cho từ đỉnh $v$ bất kỳ, chúng ta có thể đi tới đỉnh gốc bằng cách đi qua tối đa $\log n$ đường đi. Thêm vào đó, không có hai đường đi nào trong số này giao nhau.

Rõ ràng, nếu chúng ta tìm được phân rã như vậy cho một cây bất kỳ, nó sẽ cho phép chúng ta quy các truy vấn đơn lẻ có dạng *"tính toán gì đó trên đường đi từ $a$ đến $b$"* về một vài truy vấn dạng *"tính toán gì đó trên đoạn $[l, r]$ của đường đi thứ $k$"*.

### Thuật toán xây dựng

Chúng ta tính toán cho mỗi đỉnh $v$ kích thước của cây con của nó, ký hiệu là $s(v)$ (tức là số lượng đỉnh thuộc cây con của đỉnh $v bao gồm cả chính nó).

Tiếp theo, xét tất cả các cạnh nối từ đỉnh $v$ tới các con của nó. Chúng ta gọi một cạnh là **heavy** (nặng) nếu nó dẫn tới đỉnh con $c$ thỏa mãn:

$$
s(c) \ge \frac{s(v)}{2} \iff \text{cạnh }(v, c)\text{ là heavy}
$$

Tất cả các cạnh khác được gọi là **light** (nhẹ).

Rõ ràng là từ một đỉnh đi xuống phía dưới có tối đa một cạnh heavy, vì nếu không đỉnh $v$ sẽ có ít nhất hai con có kích thước $\ge \frac{s(v)}{2}$, và do đó kích thước cây con của $v$ sẽ quá lớn, $s(v) \ge 1 + 2 \frac{s(v)}{2} > s(v)$, dẫn đến mâu thuẫn.

Bây giờ chúng ta sẽ phân rã cây thành các đường đi không giao nhau. Xét tất cả các đỉnh không có cạnh heavy nào đi xuống. Chúng ta sẽ đi ngược lên từ mỗi đỉnh như vậy cho đến khi gặp gốc của cây hoặc đi qua một cạnh light. Kết quả là chúng ta sẽ thu được các đường đi gồm không hoặc nhiều cạnh heavy cộng thêm một cạnh light. Đường đi kết thúc ở gốc cây là một ngoại lệ và sẽ không có cạnh light nào. Các đường đi này được gọi là các **đường đi heavy** (heavy paths) - đây chính là các đường đi cần tìm của phân rã heavy-light.

### Chứng minh tính đúng đắn

Đầu tiên, chúng ta nhận thấy rằng các đường đi heavy thu được từ thuật toán sẽ **không giao nhau**. Thật vậy, nếu hai đường đi như vậy có chung một cạnh, điều đó ngụ ý rằng có hai cạnh heavy đi ra từ cùng một đỉnh, điều này là bất khả thi.

Thứ hai, chúng ta sẽ chứng minh rằng khi đi xuống từ gốc của cây tới một đỉnh bất kỳ, chúng ta sẽ **không chuyển đổi quá $\log n$ đường đi heavy dọc đường đi**. Việc đi xuống qua một cạnh light sẽ làm giảm kích thước của cây con hiện tại đi ít nhất một nửa:

$$
s(c) < \frac{s(v)}{2} \iff \text{cạnh }(v, c)\text{ là light}
$$

Do đó, chúng ta chỉ có thể đi qua tối đa $\log n$ cạnh light trước khi kích thước cây con giảm về 1.

Vì chúng ta chỉ có thể chuyển từ đường đi heavy này sang đường đi heavy khác thông qua một cạnh light (mỗi đường đi heavy, trừ đường đi chứa gốc cây, đều có một cạnh light ở đầu phía trên), chúng ta không thể chuyển đổi đường đi heavy quá $\log n$ lần trên đường đi từ gốc tới đỉnh bất kỳ, thỏa mãn yêu cầu chứng minh.

Hình ảnh dưới đây minh họa phân rã của một cây ví dụ. Các cạnh heavy được vẽ dày hơn các cạnh light. Các đường đi heavy được đánh dấu bằng các khung nét đứt.

<div style="text-align: center;" markdown="1">

![Minh họa HLD](hld.png)

</div>

## Các bài toán ví dụ

Khi giải quyết các bài toán, đôi khi việc coi phân rã heavy-light là một tập hợp các đường đi **không giao đỉnh** (vertex disjoint paths) sẽ thuận tiện hơn (thay vì không giao cạnh). Để làm việc này, ta chỉ cần loại bỏ cạnh cuối cùng khỏi mỗi đường đi heavy nếu nó là một cạnh light. Khi đó không có tính chất nào bị vi phạm, và mỗi đỉnh sẽ thuộc về chính xác một đường đi heavy.

Dưới đây chúng ta sẽ xem xét một số bài toán điển hình có thể được giải quyết bằng phân rã heavy-light.

Một bài toán riêng biệt đáng chú ý là **tổng các số trên đường đi**, vì đây là ví dụ điển hình cho bài toán có thể được giải quyết bằng các kỹ thuật đơn giản hơn.

### Giá trị lớn nhất trên đường đi giữa hai đỉnh

Cho một cây, mỗi đỉnh được gán một giá trị. Có các truy vấn dạng $(a, b)$, với $a$ và $b$ là hai đỉnh trên cây, yêu cầu tìm giá trị lớn nhất trên đường đi giữa hai đỉnh $a$ và $b$.

Chúng ta xây dựng trước phân rã heavy-light của cây. Trên mỗi đường đi heavy, chúng ta dựng một [cây phân đoạn (segment tree)](../data_structures/segment_tree.md), cho phép chúng ta tìm kiếm đỉnh có giá trị lớn nhất trên đoạn chỉ định của đường đi heavy đó trong $\mathcal{O}(\log n)$. Mặc dù số lượng đường đi heavy trong phân rã heavy-light có thể đạt tới $n - 1$, tổng kích thước của tất cả các đường đi bị giới hạn bởi $\mathcal{O}(n)$, do đó tổng kích thước của các cây phân đoạn cũng là tuyến tính.

Để trả lời truy vấn $(a, b)$, chúng ta tìm [tổ tiên chung gần nhất (LCA)](https://en.wikipedia.org/wiki/Lowest_common_ancestor) của $a$ và $b$ là $l$, bằng bất kỳ phương pháp nào. Bây giờ bài toán được quy về hai truy vấn $(a, l)$ và $(b, l)$, với mỗi truy vấn chúng ta làm như sau: tìm đường đi heavy chứa đỉnh nằm dưới, thực hiện truy vấn trên đường đi này, di chuyển lên đầu đường đi này, tiếp tục xác định đường đi heavy tiếp theo và thực hiện truy vấn trên đó, v.v., cho đến khi gặp đường đi chứa $l$.

Cần cẩn thiện với trường hợp ví dụ như $a$ và $l$ nằm trên cùng một đường đi heavy - khi đó truy vấn lớn nhất trên đường đi này không được thực hiện trên bất kỳ tiền tố nào, mà trên đoạn nội bộ nằm giữa $a$ và $l$.

Trả lời các truy vấn con $(a, l)$ và $(b, l)$ đòi hỏi phải đi qua $\mathcal{O}(\log n)$ đường đi heavy và với mỗi đường đi, một truy vấn giá trị lớn nhất được thực hiện trên một đoạn của nó, mất tiếp $\mathcal{O}(\log n)$ phép toán trên cây phân đoạn.
Do đó, một truy vấn $(a, b)$ tốn $\mathcal{O}(\log^2 n)$ thời gian.

Nếu bạn tính toán trước và lưu trữ giá trị lớn nhất trên tất cả các tiền tố của mỗi đường đi heavy, thì bạn sẽ thu được lời giải $\mathcal{O}(\log n)$ vì tất cả các truy vấn giá trị lớn nhất đều nằm trên các tiền tố, ngoại trừ tối đa một lần khi chúng ta chạm tới đỉnh tổ tiên $l$.

### Tổng các số trên đường đi giữa hai đỉnh

Cho một cây, mỗi đỉnh được gán một giá trị. Có các truy vấn dạng $(a, b)$, với $a$ và $b$ là hai đỉnh trên cây, yêu cầu tìm tổng các giá trị trên đường đi giữa hai đỉnh $a$ và $b$. Một biến thể của bài toán này cho phép thực hiện thêm các thao tác cập nhật thay đổi giá trị được gán cho một hoặc nhiều đỉnh.

Bài toán này có thể giải quyết tương tự như bài toán tìm giá trị lớn nhất ở trên bằng phân rã heavy-light và xây dựng các cây phân đoạn trên các đường đi heavy. Nếu không có thao tác cập nhật, ta có thể sử dụng tổng tiền tố để thay thế. Tuy nhiên, bài toán này cũng có thể giải quyết bằng các kỹ thuật đơn giản hơn.

Nếu không có cập nhật giá trị, ta có thể tìm tổng trên đường đi giữa hai đỉnh song song với việc tìm LCA của chúng bằng phương pháp [nhảy nhị phân](lca_binary_lifting.md) — khi đó, cùng với tổ tiên thứ $2^k$ của mỗi đỉnh, chúng ta cũng lưu lại tổng trên đường đi lên tổ tiên đó trong quá trình tiền xử lý.

Có một hướng tiếp cận khác hoàn toàn cho bài toán này - coi cây như một [Euler tour](https://en.wikipedia.org/wiki/Euler_tour_technique) (chu trình Euler trên cây), và dựng cây phân đoạn trên chu trình đó. Thuật toán này được xem xét trong [bài viết về một bài toán tương tự](tree_painting.md). Một lần nữa, nếu không có cập nhật, việc lưu trữ tổng tiền tố là đủ và không cần đến cây phân đoạn.

Cả hai phương pháp trên đều cung cấp lời giải tương đối đơn giản với độ phức tạp $\mathcal{O}(\log n)$ cho mỗi truy vấn.

### Tô lại màu các cạnh trên đường đi giữa hai đỉnh

Cho một cây, ban đầu mỗi cạnh được tô màu trắng. Có các thao tác cập nhật dạng $(a, b, c)$, với $a$ và $b$ là hai đỉnh và $c$ là một màu sắc, yêu cầu tô lại tất cả các cạnh trên đường đi từ $a$ đến $b$ bằng màu $c$. Sau khi thực hiện tất cả các thao tác tô màu, yêu cầu đưa ra số lượng cạnh của mỗi màu.

Tương tự như các bài toán trên, lời giải đơn giản là áp dụng phân rã heavy-light và xây dựng một [cây phân đoạn (segment tree)](../data_structures/segment_tree.md) trên mỗi đường đi heavy.

Mỗi thao tác tô màu trên đường đi $(a, b)$ sẽ được chuyển thành hai cập nhật $(a, l)$ và $(b, l)$, với $l$ là tổ tiên chung gần nhất của $a$ và $b$.
Độ phức tạp $\mathcal{O}(\log n)$ cho mỗi đường đi trên $\mathcal{O}(\log n)$ đường đi dẫn đến độ phức tạp $\mathcal{O}(\log^2 n)$ cho mỗi thao tác cập nhật.

## Cài đặt

Một số phần trong hướng tiếp cận thảo luận ở trên có thể được sửa đổi để giúp việc cài đặt dễ dàng hơn mà không làm giảm hiệu năng:

* Định nghĩa về **cạnh heavy** có thể được đổi thành **cạnh dẫn tới đỉnh con có kích thước cây con lớn nhất**, nếu có nhiều đỉnh con có cùng kích thước lớn nhất thì chọn ngẫu nhiên một trong số chúng. Điều này có thể khiến một số cạnh light biến thành cạnh heavy, nghĩa là một số đường đi heavy sẽ gộp lại thành một đường đi dài hơn, nhưng các đường đi heavy vẫn sẽ không giao nhau. Tính chất đi xuống qua một cạnh light làm giảm kích thước cây con đi ít nhất một nửa vẫn được đảm bảo.
* Thay vì xây dựng một cây phân đoạn trên mỗi đường đi heavy, chúng ta có thể sử dụng một cây phân đoạn duy nhất trên tất cả các đỉnh của cây, với các đoạn không giao nhau được phân bổ cho từng đường đi heavy.
* Trong phần mô tả thuật toán, việc trả lời truy vấn yêu cầu tính toán LCA. Mặc dù LCA có thể được tính riêng lẻ, chúng ta cũng có thể tích hợp việc tính LCA trực tiếp trong quá trình trả lời truy vấn.

Để thực hiện phân rã heavy-light:

```cpp
vector<int> parent, depth, heavy, head, pos;
int cur_pos;

int dfs(int v, vector<vector<int>> const& adj) {
    int size = 1;
    int max_c_size = 0;
    for (int c : adj[v]) {
        if (c != parent[v]) {
            parent[c] = v, depth[c] = depth[v] + 1;
            int c_size = dfs(c, adj);
            size += c_size;
            if (c_size > max_c_size)
                max_c_size = c_size, heavy[v] = c;
        }
    }
    return size;
}

void decompose(int v, int h, vector<vector<int>> const& adj) {
    head[v] = h, pos[v] = cur_pos++;
    if (heavy[v] != -1)
        decompose(heavy[v], h, adj);
    for (int c : adj[v]) {
        if (c != parent[v] && c != heavy[v])
            decompose(c, c, adj);
    }
}

void init(vector<vector<int>> const& adj) {
    int n = adj.size();
    parent = vector<int>(n);
    depth = vector<int>(n);
    heavy = vector<int>(n, -1);
    head = vector<int>(n);
    pos = vector<int>(n);
    cur_pos = 0;

    dfs(0, adj);
    decompose(0, 0, adj);
}
```

Danh sách kề của cây phải được truyền vào hàm `init`, và phân rã được thực hiện với giả định đỉnh `0` là gốc của cây.

Hàm `dfs` được sử dụng để tính `heavy[v]`, đỉnh con ở đầu kia của cạnh heavy đi ra từ `v`, cho mỗi đỉnh `v`. Ngoài ra, `dfs` cũng lưu lại đỉnh cha và độ sâu của mỗi đỉnh để sử dụng sau này khi thực hiện truy vấn.

Hàm `decompose` gán cho mỗi đỉnh `v` các giá trị `head[v]` và `pos[v]`, tương ứng là đỉnh đầu của đường đi heavy chứa `v` và vị trí của `v` trên cây phân đoạn duy nhất bao phủ tất cả các đỉnh của cây.

Để trả lời các truy vấn trên đường đi, ví dụ như truy vấn giá trị lớn nhất đã thảo luận, chúng ta có thể làm như sau:

```cpp
int query(int a, int b) {
    int res = 0;
    for (; head[a] != head[b]; b = parent[head[b]]) {
        if (depth[head[a]] > depth[head[b]])
            swap(a, b);
        int cur_heavy_path_max = segment_tree_query(pos[head[b]], pos[b]);
        res = max(res, cur_heavy_path_max);
    }
    if (depth[a] > depth[b])
        swap(a, b);
    int last_heavy_path_max = segment_tree_query(pos[a], pos[b]);
    res = max(res, last_heavy_path_max);
    return res;
}
```

## Bài tập luyện tập

- [SPOJ - QTREE - Query on a tree](https://www.spoj.com/problems/QTREE/)
- [CSES - Path Queries II](https://cses.fi/problemset/task/2134)
- [Codeforces - Subway Lines](https://codeforces.com/gym/101908/problem/L)
- [Codeforces - Tree Queries](https://codeforces.com/contest/1254/problem/D)
- [Codeforces - Tree or not Tree](https://codeforces.com/contest/117/problem/E)
- [Codeforces - The Tree](https://codeforces.com/contest/1017/problem/G)
- [Balkan OI 2018 - Min-max tree](https://oj.uz/problem/view/BOI18_minmaxtree)
