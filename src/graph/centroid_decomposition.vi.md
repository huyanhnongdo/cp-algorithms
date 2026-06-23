---
tags:
  - Original
lang: vi
---

# Phân rã trọng tâm

Kiến thức tiên quyết: [DFS (Tìm kiếm theo chiều sâu)](./depth-first-search.md), [Chia để trị (Divide and Conquer)](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm), [Cây (Tree)](<https://en.wikipedia.org/wiki/Tree_(graph_theory)>).

## Giới thiệu

**Phân rã trọng tâm** (Centroid Decomposition) là một kỹ thuật chia để trị trên cây. Nó được sử dụng để giải quyết các bài toán khác nhau liên quan đến các đường đi trên cây, chẳng hạn như đếm số đường đi có tính chất nhất định, tìm khoảng cách, hoặc trả lời các truy vấn trên các đường đi của cây.

Ý tưởng chính là phân rã đệ quy một cây bằng cách tìm **trọng tâm** (centroid) của nó. Đỉnh đặc biệt này khi bị loại bỏ sẽ chia cây thành các thành phần liên thông, mỗi thành phần chứa tối đa một nửa số đỉnh của cây ban đầu. Điều này đảm bảo chiều sâu đệ quy là hàm logarit, giúp thuật toán hoạt động hiệu quả.

## Tính chất và định nghĩa của Trọng tâm

Trước tiên hãy hiểu thế nào là trọng tâm. Một **trọng tâm** (centroid) của cây là một đỉnh mà khi loại bỏ nó, không có cây con nào có nhiều hơn $\frac{N}{2}$ đỉnh, trong đó $N$ là tổng số đỉnh của cây.

<div style="text-align: center;" markdown="1">

![Centroid Tree](centroid-definition.png)

</div>

Đối với bất kỳ cây nào có $N$ đỉnh, luôn tồn tại một hoặc hai trọng tâm. Nếu có hai trọng tâm, chúng bắt buộc phải kề nhau.

### Sự tồn tại và tính duy nhất

**Định lý**: Mọi cây luôn có ít nhất một trọng tâm và tối đa hai trọng tâm. Nếu có hai trọng tâm, chúng bắt buộc phải kề nhau.

??? note "Chứng minh"

    _Sự tồn tại_: Bắt đầu từ một đỉnh bất kỳ và liên tục di chuyển đến nút con có cây con lớn nhất. Dừng lại khi không có nút con nào có cây con chứa nhiều hơn $\frac{N}{2}$ đỉnh. Tại thời điểm này, đỉnh hiện tại $v$ là một trọng tâm vì (1) không có cây con của nút con nào chứa nhiều hơn $\frac{N}{2}$ đỉnh (theo điều kiện dừng) (2) phần cây còn lại (tất cả các đỉnh ngoài cây con của $v$) chứa tối đa $\frac{N}{2}$ đỉnh (nếu không, chúng ta đã di chuyển từ nút cha sang $v$).

    Dễ thấy rằng quá trình này luôn kết thúc, chứng minh luôn tồn tại ít nhất một trọng tâm.

    _Tính duy nhất_: Giả sử có hai trọng tâm $u$ và $v$. Xét đường đi giữa chúng. Khi loại bỏ $u$, đỉnh $v$ phải nằm trong một thành phần có tối đa $\frac{N}{2}$ đỉnh. Tương tự, khi loại bỏ $v$, đỉnh $u$ phải nằm trong một thành phần có tối đa $\frac{N}{2}$ đỉnh. Điều này chỉ khả thi nếu $u$ và $v$ kề nhau; nếu không, việc loại bỏ một trong hai đỉnh sẽ đặt đỉnh kia vào một thành phần có nhiều hơn $\frac{N}{2}$ đỉnh. Điều này mâu thuẫn với giả thiết ban đầu là cả hai trọng tâm đều nằm trong một thành phần có tối đa $\frac{N}{2}$ đỉnh. Hơn nữa, nếu có hai trọng tâm, chúng phải chia cây thành hai thành phần có chính xác $\frac{N}{2}$ đỉnh mỗi bên, điều này chỉ có thể xảy ra khi $N$ là số chẵn.

## Tính chất và định nghĩa của Phân rã trọng tâm

"Phân rã" cây về cơ bản có nghĩa là tìm trọng tâm một cách đệ quy và chia cây thành các cây con dựa trên các thành phần liên thông sau khi loại bỏ trọng tâm. Việc phân rã đệ quy cây thành các thành phần này tạo ra một tập hợp các tính chất độc đáo:

1. **Chiều sâu phân rã**: Chiều sâu phân rã là $O(\log N)$ vì mỗi cấp độ phân rã sẽ giảm kích thước thành phần đi ít nhất một nửa.
2. **Độ bao phủ đường đi**: Mọi đường đi trên cây đều đi qua trọng tâm của một thành phần nào đó trong quá trình phân rã.

### Chiều sâu phân rã

**Định lý**: Chiều sâu, hay số bước phân rã, khi sử dụng phân rã trọng tâm trên một cây bất kỳ là $O(\log N)$.

??? note "Chứng minh"

    Xét một đỉnh $v$ bất kỳ trong cây ban đầu. Chúng ta theo dõi số lần $v$ có thể là một phần của một thành phần trong quá trình phân rã.

    Ở cấp độ đầu tiên, $v$ nằm trong thành phần có kích thước $N$. Khi chúng ta loại bỏ trọng tâm của thành phần này, $v$ sẽ thuộc về một thành phần có kích thước tối đa là $\frac{N}{2}$ (theo tính chất cân bằng của trọng tâm).

    Ở cấp độ thứ hai, $v$ nằm trong thành phần có kích thước tối đa là $\frac{N}{2}$. Loại bỏ trọng tâm của thành phần này sẽ đưa $v$ vào một thành phần có kích thước tối đa là $\frac{N}{4}$.

    Tiếp tục quá trình này, ở cấp độ thứ $k$, $v$ sẽ nằm trong một thành phần có kích thước tối đa là $\frac{N}{2^{k-1}}$.

    Quá trình phân rã dừng lại khi kích thước thành phần đạt đến 1. Điều này xảy ra khi $\frac{N}{2^{k-1}} \leq 1$, tức là $k \leq \log_2 N + 1$.

    Do đó, chiều sâu tối đa của cây phân rã trọng tâm là $O(\log N)$.

**Hệ quả**: Vì mỗi đỉnh tham gia vào tối đa $O(\log N)$ cấp độ phân rã, và chúng ta xử lý mỗi đỉnh một lần ở mỗi cấp độ, các thuật toán sử dụng phân rã trọng tâm thường có độ phức tạp thời gian là $O(\log N)$ nhân với lượng công việc thực hiện trên mỗi đỉnh ở mỗi cấp độ.

### Độ bao phủ đường đi

**Định lý**: Mọi đường đi trong cây ban đầu đều đi qua trọng tâm của một thành phần nào đó trong quá trình phân rã.

??? note "Chứng minh"

    Xét một đường đi $P$ bất kỳ từ đỉnh $u$ đến đỉnh $v$ trên cây ban đầu. Chúng ta cần chỉ ra rằng đường đi này đi qua ít nhất một trọng tâm được chọn trong quá trình phân rã.

    Chúng ta chứng minh điều này bằng phương pháp quy nạp theo quá trình phân rã.

    _Trường hợp cơ sở_: Ở cấp độ đầu tiên của phân rã, chúng ta chọn trọng tâm $c_1$ của toàn bộ cây. Nếu đường đi $P$ đi qua $c_1$, ta hoàn thành chứng minh.

    _Trường hợp quy nạp_: Giả sử đường đi $P$ không đi qua $c_1$. Khi loại bỏ $c_1$, cây phân rã thành nhiều thành phần liên thông. Vì $P$ là một đường đi liên thông, cả $u$ và $v$ phải nằm trong cùng một thành phần $C$ sau khi loại bỏ $c_1$ (nếu không, $P$ buộc phải đi qua $c_1$ để kết nối chúng, mâu thuẫn với giả thiết).

    Bây giờ chúng ta phân rã đệ quy thành phần $C$. Theo giả thiết quy nạp áp dụng cho thành phần $C$, đường đi $P$ (nằm hoàn toàn trong $C$) phải đi qua trọng tâm của một thành phần nào đó trong quá trình phân rã $C$.

    Quá trình này tiếp tục cho đến khi tìm thấy trọng tâm mà $P$ đi qua. Quá trình chắc chắn phải dừng lại vì ở mỗi cấp độ, thành phần chứa $P$ sẽ nhỏ đi rõ rệt (theo tính chất cân bằng) và cuối cùng chỉ còn lại một cạnh hoặc một đỉnh duy nhất.

**Hệ quả**: Tính chất này là nền tảng cho tính đúng đắn của các thuật toán phân rã trọng tâm. Nó đảm bảo rằng khi chúng ta xử lý tất cả các đường đi đi qua mỗi trọng tâm, chúng ta sẽ bao phủ tất cả các đường đi có thể có trong cây chính xác một lần ở một cấp độ phân rã nào đó. Đây là lý do tại sao phân rã trọng tâm có thể giải quyết các bài toán liên quan đến đường đi một cách hiệu quả: mọi đường đi đều được xem xét chính xác một lần, tại cấp độ mà nó lần đầu tiên gặp một trọng tâm.

## Tìm trọng tâm

Để tìm trọng tâm của cây một cách hiệu quả:

1. Tính kích thước cây con của tất cả các đỉnh bằng cách sử dụng DFS.
2. Bắt đầu từ một đỉnh bất kỳ.
3. Tìm một nút con $v$ có cây con chứa nhiều hơn $\frac{N}{2}$ đỉnh.
4. Di chuyển đến $v$ và lặp lại bước 3.
5. Nếu không có nút con nào như vậy, đỉnh hiện tại chính là trọng tâm.

Độ phức tạp thời gian: $O(N)$.

Độ phức tạp bộ nhớ: $O(N)$.

## Mô tả thuật toán

Khi sử dụng phân rã trọng tâm, luồng hoạt động chung như sau:

1. **Tìm trọng tâm** của cây/thành phần hiện tại.
2. **Xử lý** tất cả các đường đi đi qua trọng tâm này và thực hiện các tính toán mong muốn.
3. **Loại bỏ** trọng tâm (đánh dấu là đã sử dụng).
4. **Phân rã đệ quy** từng cây con kết quả.

Quá trình này tạo ra một **cây trọng tâm** (centroid tree). Mỗi nút trong cây này đại diện cho một trọng tâm ở một giai đoạn phân rã nhất định. Điều này có nghĩa là cha của một trọng tâm (của một nút bất kỳ) là trọng tâm được tìm thấy ở thành phần lớn hơn chứa nó. Chiều cao của cây này là $O(\log N)$ như đã được chứng minh ở trên.

<div style="text-align: center;" markdown="1">

![Centroid Tree](CentroidTree.png)

</div>

Ví dụ, trong hình trên, chúng ta có một cây trọng tâm. Mỗi nút ở mỗi cấp độ của cây là trọng tâm của thành phần đó (ví dụ: gốc là trọng tâm của toàn bộ cây, nút con ngoài cùng bên trái của gốc là trọng tâm của cây con ngoài cùng bên trái của gốc, v.v.).

## Cài đặt

Dưới đây là một cài đặt của phân rã trọng tâm giải quyết bài toán cụ thể: **đếm số đường đi trong cây có độ dài chính xác là $K$**.

Trong bài toán này, chúng ta được cho một cây với $N$ đỉnh và cần đếm xem có bao nhiêu đường đi có đúng $K$ cạnh. Một đường đi được xác định bởi hai đỉnh phân biệt.

```{.cpp file=centroid_decomposition}
const int MAXN = 1e5;
vector<int> adj[MAXN];
bool removed[MAXN];
int subtree_size[MAXN];
int K;  // Target path length
long long answer = 0;  // Count of paths with length K

int get_subtree_size(int v, int p = -1) {
    subtree_size[v] = 1;
    for (int u : adj[v]) {
        if (u == p || removed[u]) continue;
        subtree_size[v] += get_subtree_size(u, v);
    }
    return subtree_size[v];
}

int get_centroid(int v, int tree_size, int p = -1) {
    for (int u : adj[v]) {
        if (u == p || removed[u]) continue;
        if (subtree_size[u] * 2 > tree_size)
            return get_centroid(u, tree_size, v);
    }
    return v;
}

void get_distances(int v, int p, int dist, vector<int>& distances) {
    if (dist > K) return;
    distances.push_back(dist);
    for (int u : adj[v]) {
        if (u == p || removed[u]) continue;
        get_distances(u, v, dist + 1, distances);
    }
}

void process_centroid(int centroid) {
    unordered_map<int, int> all_distances;
    all_distances[0] = 1;

    for (int u : adj[centroid]) {
        if (removed[u])
            continue;

        vector<int> current_distances;
        get_distances(u, centroid, 1, current_distances);

        for (int d : current_distances) {
            if (K - d >= 0) {
                answer += (all_distances[K - d] ? all_distances[K - d] : 0);
            }
        }

        for (int d : current_distances) {
            if (all_distances.find(d) == all_distances.end())
                all_distances[d] = 0;
            all_distances[d]++;
        }
    }
}

void decompose(int v) {
    int tree_size = get_subtree_size(v);
    int centroid = get_centroid(v, tree_size);

    process_centroid(centroid);

    removed[centroid] = true;

    for (int u : adj[centroid]) {
        if (!removed[u]) {
            decompose(u);
        }
    }
}
```

Mẫu này có thể được tùy biến để giải quyết các bài toán khác nhau sử dụng phân rã trọng tâm. Trong trường hợp cụ thể này, nó giải quyết bài toán đếm số đường đi có độ dài $K$. Chiến lược là: đối với mỗi trọng tâm, đếm các đường đi đi qua nó bằng cách tìm cặp đỉnh ở các cây con khác nhau có khoảng cách $d_1$ và $d_2$ có tổng bằng $K$ (tức là một đường đi đi qua trọng tâm bao gồm một đỉnh ở một cây con có khoảng cách $d_1$ đến trọng tâm và một đỉnh ở cây con khác có khoảng cách $d_2$ với $d_1 + d_2 = K$). Với mỗi khoảng cách $d$ trong cây con hiện tại, mã nguồn sẽ đếm xem có bao nhiêu đỉnh có khoảng cách $K - d$ trong các cây con đã duyệt trước đó. Việc tối ưu hóa sẽ bỏ qua các khoảng cách vượt quá $K$ để tránh đệ quy không cần thiết.

### Xây dựng Cây trọng tâm

Nếu bạn cần xây dựng một cấu trúc cây trọng tâm tường minh (hữu ích cho việc trả lời các truy vấn):

```cpp
int centroid_parent[MAXN];

int decompose(int v, int p = -1) {
    int tree_size = get_subtree_size(v);
    int centroid = get_centroid(v, tree_size);

    centroid_parent[centroid] = p;
    removed[centroid] = true;

    for (int u : adj[centroid]) {
        if (!removed[u]) {
            decompose(u, centroid);
        }
    }

    return centroid;
}
```

## Bài tập thực hành

- [CSES - Finding a Centroid](https://cses.fi/problemset/task/2079) [độ khó: dễ]
- [CSES - Fixed-Length Paths II](https://cses.fi/problemset/task/2081) [độ khó: dễ]
- [Codeforces - Xenia and Tree](http://codeforces.com/problemset/problem/342/E) [độ khó: trung bình]
- [Codeforces - Digit Tree](http://codeforces.com/contest/716/problem/E) [độ khó: trung bình]
- [OJ - Race](https://oj.uz/problem/view/IOI11_race) [độ khó: trung bình]
- [SPOJ - QTREE5](http://www.spoj.com/problems/QTREE5/) [độ khó: khó]
