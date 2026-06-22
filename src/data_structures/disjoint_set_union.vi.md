---
tags:
  - Translated
e_maxx_link: dsu
lang: vi
---

# Cấu trúc các tập hợp rời nhau (Disjoint Set Union - DSU)

Bài viết này thảo luận về cấu trúc dữ liệu **Cấu trúc các tập hợp rời nhau (Disjoint Set Union)** hay viết tắt là **DSU**.
Nó cũng thường được gọi là **Union Find** dựa trên hai thao tác chính của mình.

Cấu trúc dữ liệu này cung cấp các khả năng sau.
Cho một số phần tử, ban đầu mỗi phần tử thuộc một tập hợp riêng biệt.
DSU sẽ có thao tác để gộp bất kỳ hai tập hợp nào lại với nhau, và có thể xác định được một phần tử cụ thể đang nằm trong tập hợp nào.
Phiên bản cổ điển cũng giới thiệu thêm thao tác thứ ba: tạo một tập hợp mới từ một phần tử mới.

Do đó, giao diện cơ bản của cấu trúc dữ liệu này chỉ bao gồm ba thao tác chính:

- `make_set(v)` - tạo một tập hợp mới gồm một phần tử duy nhất `v`.
- `union_sets(a, b)` - gộp hai tập hợp chứa `a` và chứa `b` lại với nhau.
- `find_set(v)` - trả về phần tử đại diện (còn gọi là leader) của tập hợp chứa phần tử `v`.
Phần tử đại diện này là một phần tử nằm trong tập hợp đó. Nó được tự cấu trúc dữ liệu lựa chọn trong mỗi tập hợp (và có thể thay đổi theo thời gian, cụ thể là sau các lời gọi `union_sets`).
Chúng ta có thể dùng phần tử đại diện này để kiểm tra xem hai phần tử có thuộc cùng một tập hợp hay không.
`a` và `b` thuộc cùng một tập hợp khi và chỉ khi `find_set(a) == find_set(b)`.
Ngược lại, chúng nằm ở các tập hợp khác nhau.

Như sẽ được mô tả chi tiết ở phần dưới, cấu trúc dữ liệu này cho phép thực hiện mỗi thao tác trên với thời gian trung bình xấp xỉ $O(1)$.

Ngoài ra, ở một trong các phần sau, chúng tôi cũng giải thích cấu trúc DSU thay thế giúp đạt độ phức tạp trung bình chậm hơn là $O(\log n)$, nhưng có thể mạnh mẽ hơn cấu trúc DSU thông thường.

## Xây dựng cấu trúc dữ liệu hiệu quả

Chúng ta sẽ lưu trữ các tập hợp dưới dạng các **cây (tree)**: mỗi cây sẽ tương ứng với một tập hợp.
Và gốc của cây sẽ đóng vai trò là phần tử đại diện/leader của tập hợp đó.

Trong hình dưới đây, bạn có thể thấy minh họa của các cây này.

![Ví dụ minh họa biểu diễn tập hợp bằng cây](DSU_example.png)

Ban đầu, mỗi phần tử là một tập hợp riêng lẻ, do đó mỗi đỉnh là cây của chính nó.
Sau đó, ta gộp tập hợp chứa phần tử 1 và tập hợp chứa phần tử 2.
Tiếp theo, ta gộp tập hợp chứa phần tử 3 và tập hợp chứa phần tử 4.
Và ở bước cuối cùng, ta gộp tập hợp chứa phần tử 1 và tập hợp chứa phần tử 3.

Đối với việc cài đặt, điều này có nghĩa là chúng ta cần duy trì một mảng `parent` lưu trữ liên kết tới nút cha trực tiếp của nó trong cây.

### Cài đặt ngây thơ

Chúng ta đã có thể viết phiên bản cài đặt đầu tiên của cấu trúc dữ liệu DSU.
Ban đầu nó sẽ khá kém hiệu quả, nhưng sau đó chúng ta sẽ cải tiến nó bằng hai kỹ thuật tối ưu hóa để mỗi lời gọi hàm chỉ mất thời gian gần như hằng số.

Như đã nói, mọi thông tin về cha của các phần tử sẽ được lưu trong mảng `parent`.

Để tạo một tập hợp mới (thao tác `make_set(v)`), chúng ta chỉ cần tạo một cây có gốc là đỉnh `v`, nghĩa là cha của nó chính là chính nó.

Để gộp hai tập hợp (thao tác `union_sets(a, b)`), đầu tiên ta tìm phần tử đại diện của tập chứa `a` và đại diện của tập chứa `b`.
Nếu hai đại diện giống nhau thì ta không cần làm gì cả, các tập hợp đã được gộp từ trước.
Ngược lại, ta chỉ cần gán đại diện này làm cha của đại diện kia - từ đó gộp hai cây lại thành một.

Cuối cùng là cài đặt cho hàm tìm đại diện (thao tác `find_set(v)`):
ta chỉ cần đi ngược lên các nút cha của đỉnh `v` cho đến khi gặp gốc cây, tức là đỉnh có nút cha trỏ vào chính nó.
Thao tác này dễ dàng cài đặt bằng đệ quy.

```cpp
void make_set(int v) {
    parent[v] = v;
}

int find_set(int v) {
    if (v == parent[v])
        return v;
    return find_set(parent[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b)
        parent[b] = a;
}
```

Tuy nhiên, cách cài đặt này rất kém hiệu quả.
Chúng ta dễ dàng xây dựng một ví dụ khiến cây bị suy biến thành một chuỗi dài đơn điệu.
Khi đó, mỗi lời gọi `find_set(v)` có thể mất thời gian $O(n)$.

Điều này còn rất xa so với độ phức tạp mong muốn (gần như hằng số).
Do đó, chúng ta sẽ xem xét hai kỹ thuật tối ưu hóa giúp tăng tốc đáng kể thuật toán.

### Tối ưu hóa nén đường đi (Path compression)

Tối ưu hóa này được thiết kế để đẩy nhanh tốc độ của thao tác `find_set`.

Nếu chúng ta gọi `find_set(v)` cho một đỉnh `v` nào đó, thực chất chúng ta sẽ tìm được đại diện `p` cho tất cả các đỉnh nằm trên đường đi từ `v` tới gốc `p`.
Ý tưởng là làm cho đường đi của tất cả các nút này ngắn lại bằng cách gán trực tiếp cha của mỗi nút được ghé thăm thành `p`.

Bạn có thể thấy thao tác này trong hình ảnh minh họa dưới đây.
Bên trái là cây ban đầu, bên phải là cây đã được nén sau khi gọi `find_set(7)`, đường đi của các nút 7, 5, 3 và 2 đã được rút ngắn trực tiếp tới gốc.

![Nén đường đi khi gọi find_set(7)](DSU_path_compression.png)

Cài đặt mới cho `find_set` như sau:

```cpp
int find_set(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}
```

Đoạn mã đơn giản này hoạt động chính xác như mong đợi:
đầu tiên tìm đại diện của tập hợp (đỉnh gốc), và sau đó trong quá trình lùi đệ quy (stack unwinding), các nút đã đi qua sẽ được gán cha trực tiếp tới đỉnh đại diện này.

Chỉ với thay đổi đơn giản này, độ phức tạp thời gian trung bình của mỗi lời gọi đã đạt tới $O(\log n)$ (ở đây không trình bày chứng minh).
Có một cải tiến thứ hai sẽ giúp nó chạy nhanh hơn nữa.

### Gộp theo kích thước hoặc thứ hạng (Union by size / rank)

Trong tối ưu hóa này, chúng ta sẽ thay đổi thao tác `union_sets`.
Cụ thể, chúng ta sẽ quyết định cây nào sẽ được đính vào cây nào.
Trong cài đặt ngây thơ, cây thứ hai luôn được đính vào cây thứ nhất.
Trên thực tế, điều đó có thể tạo ra các cây dạng chuỗi có độ dài $O(n)$.
Với tối ưu hóa này, chúng ta sẽ tránh được điều đó bằng cách chọn lựa kỹ càng cây được đính vào.

Có nhiều cách tiếp cận heuristic khác nhau.
Hai cách tiếp cận phổ biến nhất là:
Trong cách tiếp cận đầu tiên, ta sử dụng kích thước (số nút) của cây làm thứ hạng (rank). Trong cách thứ hai, ta sử dụng chiều cao của cây (chính xác hơn là biên trên của chiều cao cây, vì chiều cao sẽ nhỏ đi sau khi áp dụng nén đường đi).

Trong cả hai cách, bản chất của tối ưu hóa là giống nhau: chúng ta đính cây có thứ hạng thấp hơn vào cây có thứ hạng cao hơn.

Dưới đây là cài đặt gộp theo kích thước (union by size):

```cpp
void make_set(int v) {
    parent[v] = v;
    size[v] = 1;
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (size[a] < size[b])
            swap(a, b);
        parent[b] = a;
        size[a] += size[b];
    }
}
```

Và dưới đây là cài đặt gộp theo thứ hạng dựa trên chiều cao cây (union by rank):

```cpp
void make_set(int v) {
    parent[v] = v;
    rank[v] = 0;
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (rank[a] < rank[b])
            swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b])
            rank[a]++;
    }
}
```

Cả hai cách tối ưu hóa này đều tương đương nhau về mặt độ phức tạp thời gian và không gian bộ nhớ. Vì vậy, trên thực tế bạn có thể chọn bất kỳ cách nào.

### Độ phức tạp thời gian

Như đã đề cập trước đó, nếu chúng ta kết hợp cả hai tối ưu hóa - nén đường đi cùng gộp theo kích thước/thứ hạng - chúng ta sẽ đạt được thời gian truy vấn gần như hằng số.
Độ phức tạp thời gian phân bổ (amortized time complexity) cuối cùng sẽ là $O(\alpha(n))$, trong đó $\alpha(n)$ là hàm Ackermann đảo, một hàm tăng trưởng cực kỳ chậm.
Trên thực tế, nó tăng chậm đến mức không bao giờ vượt quá $4$ cho tất cả các giá trị $n$ thực tế (khoảng $n < 10^{600}$).

Độ phức tạp phân bổ là tổng thời gian của mỗi thao tác được tính trung bình trên một chuỗi gồm nhiều thao tác.
Ý tưởng là đảm bảo tổng thời gian của cả chuỗi thao tác luôn nhỏ, trong khi cho phép một vài thao tác đơn lẻ có thể chậm hơn nhiều so với thời gian phân bổ.
Ví dụ, trong trường hợp của chúng ta, một lời gọi đơn lẻ có thể mất $O(\log n)$ trong trường hợp xấu nhất, nhưng nếu chúng ta thực hiện liên tiếp $m$ lời gọi như vậy, thời gian trung bình cho mỗi cuộc gọi sẽ chỉ là $O(\alpha(n))$.

Chúng tôi cũng sẽ không trình bày chứng minh cho độ phức tạp thời gian này vì nó khá dài và phức tạp.

Ngoài ra, cần lưu ý rằng DSU sử dụng gộp theo kích thước/thứ hạng nhưng không có nén đường đi sẽ hoạt động trong thời gian $O(\log n)$ cho mỗi truy vấn.

### Gộp theo chỉ số ngẫu nhiên (Linking by index / coin-flip linking)

Cả hai phương pháp gộp theo thứ hạng và kích thước đều yêu cầu bạn phải lưu trữ thêm dữ liệu cho mỗi tập hợp và cập nhật các giá trị này trong mỗi thao tác gộp.
Có một thuật toán ngẫu nhiên hóa giúp đơn giản hóa thao tác gộp một chút: gộp theo chỉ số.

Chúng ta gán cho mỗi tập hợp một giá trị ngẫu nhiên gọi là chỉ số (index), và đính tập hợp có chỉ số nhỏ hơn vào tập hợp có chỉ số lớn hơn.
Nhiều khả năng tập hợp lớn hơn sẽ có chỉ số lớn hơn tập hợp nhỏ hơn, vì thế thao tác này liên quan chặt chẽ tới gộp theo kích thước.
Thực tế đã chứng minh rằng thao tác này có cùng độ phức tạp thời gian với gộp theo kích thước.
Tuy nhiên, trên thực tế nó chạy chậm hơn một chút so với gộp theo kích thước.

Bạn có thể tìm thấy chứng minh chi tiết và nhiều kỹ thuật gộp khác tại [tài liệu này](http://www.cis.upenn.edu/~sanjeev/papers/soda14_disjoint_set_union.pdf).

```cpp
void make_set(int v) {
    parent[v] = v;
    index[v] = rand();
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (index[a] < index[b])
            swap(a, b);
        parent[b] = a;
    }
}
```

Có một hiểu lầm phổ biến cho rằng việc tung đồng xu (coin-flip) ngẫu nhiên để quyết định cây nào đính vào cây nào cũng cho độ phức tạp tương tự.
Tuy nhiên điều đó không đúng.
Tài liệu liên kết ở trên phỏng đoán rằng việc gộp bằng tung đồng xu kết hợp nén đường đi có độ phức tạp là $\Omega\left(n \frac{\log n}{\log \log n}\right)$.
Và trong các thử nghiệm hiệu năng (benchmarks), nó hoạt động kém hơn nhiều so với gộp theo kích thước/thứ hạng hay gộp theo chỉ số ngẫu nhiên.

```cpp
void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (rand() % 2)
            swap(a, b);
        parent[b] = a;
    }
}
```

## Ứng dụng và các cải tiến khác nhau

Trong phần này, chúng ta sẽ xem xét một số ứng dụng của cấu trúc dữ liệu này, từ những ứng dụng thông thường cho đến các cải tiến cấu trúc nâng cao.

### Tìm các thành phần liên thông của đồ thị

Đây là một trong những ứng dụng rõ ràng nhất của DSU.

Bài toán được phát biểu như sau:
Ban đầu ta có một đồ thị rỗng. Ta cần thêm các đỉnh và các cạnh vô hướng vào đồ thị, và trả lời các truy vấn dạng $(a, b)$ - "đỉnh $a$ và đỉnh $b$ có thuộc cùng một thành phần liên thông của đồ thị hay không?"

Ở đây chúng ta có thể áp dụng trực tiếp DSU, giúp xử lý việc thêm đỉnh, thêm cạnh và trả lời truy vấn trong thời gian trung bình gần như hằng số.

Ứng dụng này rất quan trọng, vì bài toán tương tự xuất hiện trong [Thuật toán Kruskal tìm cây khung nhỏ nhất](../graph/mst_kruskal.md).
Sử dụng DSU, chúng ta có thể [cải tiến](../graph/mst_kruskal_with_dsu.md) độ phức tạp từ $O(m \log n + n^2)$ thành $O(m \log n)$.

### Tìm các thành phần liên thông trên ảnh

Một ứng dụng của DSU là bài toán sau:
Có một bức ảnh kích thước $n \times m$ pixel.
Ban đầu tất cả các pixel đều có màu trắng, sau đó một số pixel màu đen được vẽ lên.
Bạn cần xác định kích thước của mỗi thành phần liên thông màu trắng trong bức ảnh cuối cùng.

Để giải quyết bài toán này, chúng ta chỉ cần duyệt qua tất cả các pixel trắng trên ảnh, với mỗi pixel xét 4 ô lân cận của nó, nếu ô lân cận cũng có màu trắng thì ta gọi `union_sets`.
Do đó, chúng ta sẽ có một DSU gồm $n m$ nút tương ứng với các pixel ảnh.
Các cây kết quả trong DSU chính là các thành phần liên thông cần tìm.

Bài toán cũng có thể được giải bằng [DFS](../graph/depth-first-search.md) hoặc [BFS](../graph/breadth-first-search.md), nhưng phương pháp dùng DSU ở đây có một ưu điểm:
nó có thể xử lý ma trận theo từng dòng (tức là để xử lý một dòng ta chỉ cần dòng trước đó và dòng hiện tại, và chỉ cần DSU xây dựng cho các phần tử của một dòng duy nhất) với bộ nhớ chỉ cần $O(\min(n, m))$.

### Lưu trữ thông tin bổ sung cho mỗi tập hợp

DSU cho phép bạn dễ dàng lưu trữ thông tin bổ sung trong mỗi tập hợp.

Một ví dụ đơn giản là kích thước của tập hợp:
việc lưu trữ kích thước đã được mô tả trong phần Gộp theo kích thước (thông tin này được lưu trữ bởi phần tử đại diện hiện tại của tập hợp).

Tương tự như vậy - bằng cách lưu trữ tại các nút đại diện - bạn cũng có thể lưu trữ bất kỳ thông tin nào khác về các tập hợp.

### Nén các bước nhảy dọc theo đoạn / Tô màu đoạn con ngoại tuyến (offline)

Một ứng dụng phổ biến của DSU là:
Có một tập các đỉnh, mỗi đỉnh có một cạnh đi ra hướng tới một đỉnh khác.
Với DSU, bạn có thể tìm điểm kết thúc mà chúng ta sẽ tới sau khi đi theo tất cả các cạnh xuất phát từ một điểm cho trước, trong thời gian gần như hằng số.

Một ví dụ tiêu biểu cho ứng dụng này là **bài toán tô màu đoạn con**.
Chúng ta có một đoạn độ dài $L$, mỗi ô ban đầu có màu 0.
Chúng ta cần tô lại màu cho đoạn con $[l, r]$ bằng màu $c$ cho mỗi truy vấn $(l, r, c)$.
Cuối cùng, chúng ta cần tìm màu sắc sau cùng của mỗi ô.
Chúng ta giả định rằng tất cả các truy vấn đều đã được biết trước (tức là bài toán ngoại tuyến - offline).

Để giải quyết bài toán này, chúng ta có thể dựng một DSU mà mỗi ô sẽ lưu trữ một liên kết tới ô chưa tô màu tiếp theo.
Do đó ban đầu mỗi ô trỏ tới chính nó.
Sau khi tô màu một đoạn được yêu cầu, tất cả các ô trong đoạn đó sẽ trỏ tới ô nằm ngay sau đoạn đó.

Bây giờ để giải bài toán này, chúng ta sẽ xét các truy vấn **theo thứ tự ngược lại**: từ truy vấn cuối cùng đến truy vấn đầu tiên.
Bằng cách này, khi thực hiện một truy vấn, chúng ta chỉ cần tô màu chính xác các ô chưa được tô màu trong đoạn con $[l, r]$.
Tất cả các ô khác đã chứa màu sắc cuối cùng của chúng.
Để duyệt nhanh qua các ô chưa tô màu, chúng ta sử dụng DSU.
Chúng ta tìm ô chưa tô màu ngoài cùng bên trái trong đoạn, tô màu nó, và di chuyển con trỏ tới ô trống tiếp theo bên phải.

Ở đây chúng ta có thể sử dụng DSU kết hợp nén đường đi, nhưng không thể sử dụng gộp theo thứ hạng/kích thước (vì thứ tự gộp - nút nào trở thành cha sau khi gộp - là rất quan trọng để đảm bảo tính liên tục của bước nhảy).
Do đó độ phức tạp sẽ là $O(\log n)$ cho mỗi phép gộp (vẫn rất nhanh).

Cài đặt chi tiết:

```cpp
for (int i = 0; i <= L; i++) {
    make_set(i);
}

for (int i = m-1; i >= 0; i--) {
    int l = query[i].l;
    int r = query[i].r;
    int c = query[i].c;
    for (int v = find_set(l); v <= r; v = find_set(v)) {
        answer[v] = c;
        parent[v] = v + 1;
    }
}
```

Có một cách tối ưu hóa khác:
Chúng ta có thể sử dụng gộp theo thứ hạng/kích thước nếu chúng ta lưu trữ ô chưa tô màu tiếp theo trong một mảng bổ sung `end[]`.
Khi đó chúng ta có thể gộp hai tập hợp lại theo cơ chế heuristic thông thường và nhận được giải pháp trong thời gian $O(\alpha(n))$.

### Hỗ trợ khoảng cách tới phần tử đại diện

Đôi khi trong các ứng dụng cụ thể của DSU, bạn cần duy trì khoảng cách từ một đỉnh tới đại diện của tập hợp chứa nó (tức là độ dài đường đi trong cây từ nút hiện tại đến gốc của cây).

Nếu chúng ta không sử dụng nén đường đi, khoảng cách đơn giản là số lượng lời gọi đệ quy.
Nhưng cách này rất kém hiệu quả.

Tuy nhiên, chúng ta vẫn có thể áp dụng nén đường đi nếu lưu trữ thêm thông tin **khoảng cách đến nút cha** cho mỗi nút.

Khi cài đặt, ta nên sử dụng một mảng lưu trữ các cặp (pair) cho `parent[]`, và hàm `find_set` giờ đây sẽ trả về hai số: đại diện của tập hợp và khoảng cách tới nó.

```cpp
void make_set(int v) {
    parent[v] = make_pair(v, 0);
    rank[v] = 0;
}

pair<int, int> find_set(int v) {
    if (v != parent[v].first) {
        int len = parent[v].second;
        parent[v] = find_set(parent[v].first);
        parent[v].second += len;
    }
    return parent[v];
}

void union_sets(int a, int b) {
    a = find_set(a).first;
    b = find_set(b).first;
    if (a != b) {
        if (rank[a] < rank[b])
            swap(a, b);
        parent[b] = make_pair(a, 1);
        if (rank[a] == rank[b])
            rank[a]++;
    }
}
```

### Hỗ trợ tính chẵn lẻ của độ dài đường đi / Kiểm tra đồ thị hai phía trực tuyến (online)

Tương tự như tính khoảng cách đường đi tới nút gốc, chúng ta có thể duy trì tính chẵn lẻ của độ dài đường đi.
Tại sao ứng dụng này lại được trình bày ở một mục riêng?

Yêu cầu lưu trữ tính chẵn lẻ của đường đi xuất hiện trong bài toán sau:
Ban đầu cho một đồ thị rỗng, ta có thể thêm các cạnh vào đồ thị, và cần trả lời các truy vấn dạng "thành phần liên thông chứa đỉnh này có phải là **đồ thị hai phía (bipartite)** không?".

Để giải quyết bài toán này, chúng ta sử dụng DSU để lưu trữ các thành phần và lưu tính chẵn lẻ của đường đi tới đại diện cho mỗi đỉnh.
Như vậy ta có thể kiểm tra nhanh xem việc thêm một cạnh có làm vi phạm tính chất đồ thị hai phía hay không:
cụ thể nếu hai đầu của cạnh nằm trong cùng một thành phần liên thông và có cùng tính chẵn lẻ của khoảng cách tới đỉnh đại diện, thì việc thêm cạnh này sẽ tạo ra một chu trình có độ dài lẻ, và thành phần liên thông đó sẽ mất đi tính chất đồ thị hai phía.

Khó khăn duy nhất chúng ta gặp phải là tính toán lại tính chẵn lẻ trong phương thức `union_sets`.

Nếu chúng ta thêm một cạnh $(a, b)$ kết nối hai thành phần liên thông lại với nhau, khi đính một cây vào cây kia ta cần điều chỉnh lại tính chẵn lẻ.

Hãy thiết lập công thức tính toán tính chẵn lẻ cần gán cho đại diện của tập hợp sẽ được đính vào tập hợp kia.
Gọi $x$ là tính chẵn lẻ của độ dài đường đi từ đỉnh $a$ tới đại diện $A$ của nó, $y$ là tính chẵn lẻ của độ dài đường đi từ đỉnh $b$ tới đại diện $B$ của nó, và $t$ là tính chẵn lẻ cần tìm để gán cho $B$ sau khi gộp.
Đường đi mới sẽ gồm ba phần:
từ $B$ tới $b$, từ $b$ tới $a$ (được nối bởi một cạnh nên có tính chẵn lẻ là $1$), và từ $a$ tới $A$.
Do đó ta thu được công thức (với ký hiệu $\oplus$ là phép toán XOR):

$$t = x \oplus y \oplus 1$$

Như vậy, bất kể chúng ta thực hiện bao nhiêu phép gộp, tính chẵn lẻ của các cạnh vẫn được truyền một cách chính xác từ đại diện này sang đại diện khác.

Dưới đây là mã nguồn cài đặt DSU hỗ trợ kiểm tra tính chẵn lẻ. Tương tự như phần trước, chúng ta dùng một cặp dữ liệu để lưu trữ nút cha và tính chẵn lẻ. Ngoài ra, với mỗi tập hợp ta lưu trữ trong mảng `bipartite[]` trạng thái tập hợp đó có còn là đồ thị hai phía hay không.

```cpp
void make_set(int v) {
    parent[v] = make_pair(v, 0);
    rank[v] = 0;
    bipartite[v] = true;
}

pair<int, int> find_set(int v) {
    if (v != parent[v].first) {
        int parity = parent[v].second;
        parent[v] = find_set(parent[v].first);
        parent[v].second ^= parity;
    }
    return parent[v];
}

void add_edge(int a, int b) {
    pair<int, int> pa = find_set(a);
    a = pa.first;
    int x = pa.second;

    pair<int, int> pb = find_set(b);
    b = pb.first;
    int y = pb.second;

    if (a == b) {
        if (x == y)
            bipartite[a] = false;
    } else {
        if (rank[a] < rank[b])
            swap (a, b);
        parent[b] = make_pair(a, x^y^1);
        bipartite[a] &= bipartite[b];
        if (rank[a] == rank[b])
            ++rank[a];
    }
}

bool is_bipartite(int v) {
    return bipartite[find_set(v).first];
}
```

### RMQ ngoại tuyến (offline range minimum query) trong thời gian trung bình $O(\alpha(n))$ / Kỹ thuật của Arpa { #arpa data-toc-label="RMQ ngoại tuyến / Kỹ thuật của Arpa"}

Cho một mảng `a[]`, chúng ta cần tính giá trị nhỏ nhất trên các đoạn con cho trước của mảng.

Ý tưởng giải bài toán này bằng DSU như sau:
Chúng ta sẽ duyệt qua mảng và khi đang ở phần tử thứ `i`, chúng ta sẽ trả lời tất cả các truy vấn `(L, R)` có `R == i`.
Để thực hiện việc này một cách hiệu quả, chúng ta sẽ duy trì một DSU trên `i` phần tử đầu tiên với cấu trúc: cha của một phần tử là phần tử nhỏ hơn tiếp theo nằm ở bên phải của nó.
Khi đó, đáp án cho truy vấn sẽ là `a[find_set(L)]`, số nhỏ nhất ở bên phải của `L`.

Cách tiếp cận này hiển nhiên chỉ hoạt động ngoại tuyến (offline), tức là nếu chúng ta đã biết trước tất cả các truy vấn.

Chúng ta có thể áp dụng nén đường đi dễ dàng.
Và chúng ta cũng có thể sử dụng gộp theo thứ hạng nếu lưu trữ đại diện thực tế trong một mảng riêng biệt.

```cpp
struct Query {
    int L, R, idx;
};

vector<int> answer;
vector<vector<Query>> container;
```

Trong đó `container[i]` lưu trữ tất cả các truy vấn có `R == i`.

```cpp
stack<int> s;
for (int i = 0; i < n; i++) {
    while (!s.empty() && a[s.top()] > a[i]) {
        parent[s.top()] = i;
        s.pop();
    }
    s.push(i);
    for (Query q : container[i]) {
        answer[q.idx] = a[find_set(q.L)];
    }
}
```

Ngày nay, thuật toán này được biết đến với tên gọi **Kỹ thuật của Arpa (Arpa's trick)**.
Nó được đặt theo tên của AmirReza Poorakhavan, người đã độc lập phát hiện và phổ biến rộng rãi kỹ thuật này, mặc dù thuật toán đã tồn tại từ trước đó.

### LCA ngoại tuyến (lowest common ancestor) trên cây trong thời gian trung bình $O(\alpha(n))$ {data-toc-label="LCA ngoại tuyến"}

Thuật toán tìm tổ tiên chung gần nhất (LCA) ngoại tuyến được trình bày chi tiết trong bài viết [Lowest Common Ancestor - Thuật toán ngoại tuyến của Tarjan](../graph/lca_tarjan.md).
Thuật toán này nổi bật hơn các thuật toán tìm LCA khác nhờ tính đơn giản của nó (đặc biệt là khi so sánh với một thuật toán tối ưu như thuật toán của [Farach-Colton và Bender](../graph/lca_farachcoltonbender.md)).

### Lưu trữ DSU rõ ràng dưới dạng danh sách tập hợp / Ứng dụng khi gộp các cấu trúc dữ liệu khác nhau

Một trong những cách thay thế để lưu trữ DSU là bảo toàn mỗi tập hợp dưới dạng một **danh sách được lưu trữ rõ ràng chứa các phần tử của nó**.
Đồng thời, mỗi phần tử cũng lưu trữ một liên kết trực tiếp tới đại diện của tập hợp đó.

Thoạt nhìn, đây có vẻ là một cấu trúc dữ liệu kém hiệu quả:
khi gộp hai tập hợp, chúng ta sẽ phải thêm một danh sách vào cuối danh sách kia và cập nhật lại liên kết đại diện cho tất cả các phần tử của một trong hai danh sách.

Tuy nhiên, việc áp dụng **hệ thống heuristic trọng số** (tương tự như Gộp theo kích thước) có thể giảm đáng kể độ phức tạp tiệm cận:
chỉ mất $O(m + n \log n)$ để thực hiện $m$ truy vấn trên $n$ phần tử.

Nguyên lý heuristic trọng số ở đây nghĩa là chúng ta sẽ luôn **thêm tập hợp có kích thước nhỏ hơn vào tập hợp có kích thước lớn hơn**.
Việc thêm một tập hợp vào tập hợp khác rất dễ cài đặt trong hàm `union_sets` và sẽ mất thời gian tỷ lệ thuận với kích thước của tập hợp được thêm vào.
Và việc tìm kiếm đại diện trong hàm `find_set` sẽ chỉ mất thời gian $O(1)$.

Hãy cùng chứng minh **độ phức tạp thời gian** $O(m + n \log n)$ cho việc thực hiện $m$ truy vấn.
Chúng ta xét một phần tử bất kỳ $x$ và đếm số lần nó bị tác động trong thao tác gộp `union_sets`.
Khi phần tử $x$ bị tác động lần đầu tiên, kích thước của tập hợp mới chứa nó sẽ ít nhất là $2$.
Khi bị tác động lần thứ hai, tập hợp kết quả sẽ có kích thước ít nhất là $4$, vì tập hợp nhỏ hơn luôn được thêm vào tập hợp lớn hơn.
Và cứ tiếp tục như thế.
Điều này có nghĩa là phần tử $x$ chỉ có thể bị di chuyển trong tối đa $\log n$ thao tác gộp.
Do đó, tổng thời gian trên tất cả các đỉnh sẽ là $O(n \log n)$ cộng thêm $O(1)$ cho mỗi truy vấn tìm kiếm.

Dưới đây là mã nguồn cài đặt:

```cpp
vector<int> lst[MAXN];
int parent[MAXN];

void make_set(int v) {
    lst[v] = vector<int>(1, v);
    parent[v] = v;
}

int find_set(int v) {
    return parent[v];
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (lst[a].size() < lst[b].size())
            swap(a, b);
        while (!lst[b].empty()) {
            int v = lst[b].back();
            lst[b].pop_back();
            parent[v] = a;
            lst[a].push_back (v);
        }
    }
}
```

Ý tưởng thêm phần nhỏ hơn vào phần lớn hơn này cũng có thể được áp dụng rộng rãi trong nhiều bài toán khác không liên quan trực tiếp đến DSU.

Ví dụ, xét **bài toán** sau:
Cho một cây, mỗi lá được gán một số hiệu (cùng một số có thể xuất hiện nhiều lần ở các lá khác nhau).
Chúng ta muốn tính số lượng số khác nhau trong cây con của mỗi nút trên cây.

Áp dụng cùng ý tưởng trên cho bài toán này, ta có giải pháp:
Chúng ta có thể cài đặt một hàm [DFS](../graph/depth-first-search.md) trả về một con trỏ tới tập hợp các số nguyên - danh sách các số xuất hiện trong cây con đó.
Khi đó, để có câu trả lời cho nút hiện tại (trừ phi nó là lá), chúng ta gọi DFS cho tất cả các nút con của nó và gộp tất cả các tập hợp nhận được lại với nhau.
Kích thước của tập hợp kết quả chính là câu trả lời cho nút hiện tại.
Để kết hợp hiệu quả nhiều tập hợp, ta áp dụng quy tắc đã mô tả ở trên:
gộp các tập hợp bằng cách thêm các tập nhỏ hơn vào tập lớn hơn.
Cuối cùng, ta nhận được giải pháp có độ phức tạp $O(n \log^2 n)$, vì một số chỉ bị thêm vào một tập hợp tối đa $O(\log n)$ lần.

### Lưu trữ DSU bằng cách duy trì cấu trúc cây rõ ràng / Tìm cầu trực tuyến trong thời gian trung bình $O(\alpha(n))$ {data-toc-label="Lưu trữ DSU duy trì cấu trúc cây rõ ràng / Tìm cầu trực tuyến"}

Một trong những ứng dụng mạnh mẽ nhất của DSU là nó cho phép bạn lưu trữ các cây dưới cả dạng **đã nén và chưa nén**.
Dạng nén được dùng để gộp các cây và xác định xem hai đỉnh có thuộc cùng một cây hay không, còn dạng chưa nén có thể dùng - ví dụ - để tìm đường đi giữa hai đỉnh cho trước hoặc thực hiện các thao tác duyệt cây khác.

Khi cài đặt, điều này có nghĩa là ngoài mảng tổ tiên đã nén `parent[]`, chúng ta cần duy trì thêm mảng tổ tiên chưa nén `real_parent[]`.
Việc duy trì mảng bổ sung này hiển nhiên không làm ảnh hưởng đến độ phức tạp thuật toán:
các thay đổi trong nó chỉ xảy ra khi chúng ta gộp hai cây, và chỉ thay đổi ở đúng một phần tử.

Mặt khác, trong ứng dụng thực tế, chúng ta thường cần kết nối các cây bằng một cạnh nối bất kỳ thay vì nối qua hai nút gốc.
Điều này có nghĩa là chúng ta không có lựa chọn nào khác ngoài việc xoay gốc của cây (re-root) - biến một trong hai đỉnh đầu cạnh thành gốc mới của cây.

Thoạt nhìn, thao tác xoay gốc này có vẻ rất tốn kém và sẽ làm giảm độ phức tạp thời gian đáng kể.
Thật vậy, để xoay gốc cây tại đỉnh $v$, chúng ta phải đi từ đỉnh đó về gốc cũ và đảo ngược hướng liên kết trong `parent[]` và `real_parent[]` cho tất cả các nút trên đường đi đó.

Tuy nhiên, trên thực tế điều này không quá tệ, chúng ta có thể chọn xoay gốc cho cây có kích thước nhỏ hơn trong hai cây tương tự như ý tưởng ở các phần trước, và đạt độ phức tạp trung bình là $O(\log n)$.

Chi tiết hơn (bao gồm cả chứng minh độ phức tạp thời gian) có thể xem tại bài viết [Tìm cầu trực tuyến (Finding Bridges Online)](../graph/bridge-searching-online.md).

## Lịch sử phát triển

Cấu trúc dữ liệu DSU đã được biết đến từ rất lâu.

Cách lưu trữ cấu trúc này dưới dạng **một rừng các cây** dường như lần đầu tiên được mô tả bởi Galler và Fisher vào năm 1964 (Galler, Fisher, "An Improved Equivalence Algorithm"), tuy nhiên việc phân tích đầy đủ độ phức tạp thời gian được thực hiện muộn hơn rất nhiều.

Các tối ưu hóa nén đường đi và gộp theo thứ hạng được phát triển bởi McIlroy và Morris, và độc lập bởi Tritter.

Hopcroft và Ullman đã chỉ ra vào năm 1973 độ phức tạp thời gian là $O(\log^\star n)$ (Hopcroft, Ullman "Set-merging algorithms") - ở đây $\log^\star$ là **logarit lặp** (đây là một hàm tăng trưởng rất chậm, nhưng vẫn chưa chậm bằng hàm Ackermann đảo).

Lần đầu tiên đánh giá độ phức tạp $O(\alpha(n))$ được công bố vào năm 1975 bởi Tarjan ("Efficiency of a Good But Not Linear Set Union Algorithm").
Sau đó vào năm 1985, ông cùng với Leeuwen đã công bố nhiều phân tích độ phức tạp cho một số heuristic thứ hạng và cách nén đường đi khác nhau (Tarjan, Leeuwen "Worst-case Analysis of Set Union Algorithms").

Cuối cùng vào năm 1989, Fredman và Sachs đã chứng minh rằng trong mô hình tính toán được áp dụng, **bất kỳ** thuật toán nào giải quyết bài toán cấu trúc tập hợp rời nhau đều phải mất ít nhất thời gian trung bình là $O(\alpha(n))$ (Fredman, Saks, "The cell probe complexity of dynamic data structures").

## Bài tập thực hành

* [TIMUS - Anansi's Cobweb](http://acm.timus.ru/problem.aspx?space=1&num=1671)
* [Codeforces - Roads not only in Berland](http://codeforces.com/contest/25/problem/D)
* [TIMUS - Parity](http://acm.timus.ru/problem.aspx?space=1&num=1003)
* [SPOJ - Strange Food Chain](http://www.spoj.com/problems/CHAIN/)
* [SPOJ - COLORFUL ARRAY](https://www.spoj.com/problems/CLFLARR/)
* [SPOJ - Consecutive Letters](https://www.spoj.com/problems/CONSEC/)
* [Toph - Unbelievable Array](https://toph.co/p/unbelievable-array)
* [HackerEarth - Lexicographically minimal string](https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/lexicographically-minimal-string-6edc1406/description/)
* [HackerEarth - Fight in Ninja World](https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/containers-of-choclates-1/)
