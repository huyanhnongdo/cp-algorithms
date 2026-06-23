---
title: Tìm cầu trực tuyến
tags:
  - Translated
e_maxx_link: bridge_searching_online
---

# Tìm cầu trực tuyến

Cho một đồ thị vô hướng.
Một **cầu** (bridge) là một cạnh mà khi loại bỏ nó, đồ thị sẽ mất tính liên thông (hay nói một cách chính xác hơn là số thành phần liên thông của đồ thị sẽ tăng lên).
Nhiệm vụ của chúng ta là tìm tất cả các cầu trong đồ thị đã cho.

Một cách trực quan, bài toán này có thể được phát biểu như sau:
chúng ta cần tìm tất cả các con đường "quan trọng" trên bản đồ giao thông đã cho, tức là các con đường mà khi loại bỏ bất kỳ con đường nào trong số đó đều dẫn đến việc một số thành phố không thể đi tới được từ các thành phố khác.

Đã có bài viết [Tìm cầu trong $O(N+M)$](bridge-searching.md) giải quyết bài toán này bằng thuật toán duyệt qua [Tìm kiếm theo chiều sâu](depth-first-search.md).
Thuật toán được mô tả trong bài viết này sẽ phức tạp hơn nhiều, nhưng nó có một ưu điểm lớn:
thuật toán này hoạt động trực tuyến (online), có nghĩa là đồ thị đầu vào không cần phải biết trước toàn bộ.
Các cạnh được thêm vào từng cạnh một, và sau mỗi lần thêm cạnh, thuật toán sẽ tính toán lại tất cả các cầu trong đồ thị hiện tại.
Nói cách khác, thuật toán được thiết kế để hoạt động hiệu quả trên đồ thị động, thay đổi liên tục.

Cụ thể hơn, phát biểu của bài toán là:
Ban đầu đồ thị rỗng và gồm $n$ đỉnh.
Sau đó, chúng ta nhận được các cặp đỉnh $(a, b)$ đại diện cho một cạnh được thêm vào đồ thị.
Sau mỗi cạnh nhận được, tức là sau khi thêm mỗi cạnh, hãy đưa ra số lượng cầu hiện tại trong đồ thị.

Chúng ta cũng có thể duy trì danh sách tất cả các cầu cũng như hỗ trợ một cách tường minh các thành phần liên thông 2-cạnh (2-edge-connected components).

Thuật toán mô tả dưới đây chạy trong thời gian $O(n \log n + m)$, trong đó $m$ là số cạnh.
Thuật toán dựa trên cấu trúc dữ liệu [Cấu trúc các tập hợp không giao nhau (Disjoint Set Union)](../data_structures/disjoint_set_union.md) (DSU).
Tuy nhiên, bản cài đặt trong bài viết này mất thời gian $O(n \log n + m \log n)$ vì sử dụng phiên bản DSU đơn giản hóa không áp dụng Kỹ thuật gộp theo hạng (Union by Rank).

## Thuật toán

Trước tiên, hãy định nghĩa thành phần liên thông $k$-cạnh:
đó là một thành phần liên thông vẫn giữ nguyên tính liên thông khi ta loại bỏ ít hơn $k$ cạnh bất kỳ.

Dễ dàng nhận thấy rằng các cầu phân chia đồ thị thành các thành phần liên thông 2-cạnh.
Nếu chúng ta co (compress) mỗi thành phần liên thông 2-cạnh này thành một đỉnh và chỉ giữ lại các cầu làm cạnh trong đồ thị đã co, chúng ta sẽ thu được một đồ thị không có chu trình, tức là một rừng (forest).

Thuật toán mô tả dưới đây duy trì một cách tường minh rừng này cũng như các thành phần liên thông 2-cạnh.

Rõ ràng ban đầu, khi đồ thị rỗng, nó chứa $n$ thành phần liên thông 2-cạnh, bản thân chúng không kết nối với nhau.

Khi thêm cạnh tiếp theo $(a, b)$, có thể xảy ra ba trường hợp:

* Cả hai đỉnh $a$ và $b$ nằm trong cùng một thành phần liên thông 2-cạnh - khi đó cạnh này không phải là cầu và không làm thay đổi bất kỳ cấu trúc nào trong rừng, vì vậy chúng ta có thể bỏ qua cạnh này.

  Do đó, trong trường hợp này số lượng cầu không thay đổi.

* Các đỉnh $a$ và $b$ nằm ở các thành phần liên thông hoàn toàn khác nhau, tức là mỗi đỉnh thuộc một cây khác nhau.
  Trong trường hợp này, cạnh $(a, b)$ trở thành một cầu mới, và hai cây này được kết hợp thành một cây duy nhất (và tất cả các cầu cũ vẫn được giữ nguyên).

  Do đó, trong trường hợp này số lượng cầu tăng thêm một.

* Các đỉnh $a$ và $b$ nằm trong cùng một thành phần liên thông lớn, nhưng ở các thành phần liên thông 2-cạnh khác nhau.
  Trong trường hợp này, cạnh này tạo thành một chu trình cùng với một số cầu cũ.
  Tất cả các cầu này sẽ không còn là cầu nữa, và chu trình tạo thành này phải được co thành một thành phần liên thông 2-cạnh mới.

  Do đó, trong trường hợp này số lượng cầu giảm đi một hoặc nhiều hơn.

Do đó, toàn bộ bài toán được quy về việc cài đặt hiệu quả tất cả các thao tác trên rừng các thành phần liên thông 2-cạnh.

## Cấu trúc dữ liệu để lưu trữ rừng

Cấu trúc dữ liệu duy nhất mà chúng ta cần là [Disjoint Set Union](../data_structures/disjoint_set_union.md).
Thực tế chúng ta sẽ tạo ra hai bản sao của cấu trúc này:
một bản dùng để duy trì các thành phần liên thông lớn (connectivity components), bản còn lại để duy trì các thành phần liên thông 2-cạnh (2-edge-connected components).
Và thêm vào đó, chúng ta lưu trữ cấu trúc của các cây trong rừng của các thành phần liên thông 2-cạnh thông qua các con trỏ:
Mỗi thành phần liên thông 2-cạnh sẽ lưu trữ chỉ số `par[]` đại diện cho nút cha của nó trong cây.

Bây giờ chúng ta sẽ phân tích chi tiết từng thao tác cần cài đặt:

  * Kiểm tra xem hai đỉnh có nằm trong cùng một thành phần liên thông / thành phần liên thông 2-cạnh hay không.
    Thao tác này được thực hiện bằng thuật toán DSU thông thường, chúng ta chỉ cần tìm và so sánh các đại diện của các tập hợp.
  
  * Nối hai cây bằng một cạnh $(a, b)$.
    Vì có thể xảy ra trường hợp cả đỉnh $a$ và đỉnh $b$ đều không phải là gốc của cây chứa chúng, cách duy nhất để kết nối hai cây này là đảo gốc (re-root) một trong hai cây.
    Ví dụ, bạn có thể đảo gốc cây chứa đỉnh $a$ thành đỉnh $a$, và sau đó gắn nó vào cây kia bằng cách đặt đỉnh cha của $a$ là $b$.
  
    Tuy nhiên, câu hỏi về tính hiệu quả của thao tác đảo gốc phát sinh:
    để chuyển gốc của cây có gốc $r$ sang đỉnh $v$, chúng ta cần duyệt qua tất cả các đỉnh trên đường đi giữa $v$ và $r$ và đổi hướng các con trỏ `par[]` theo chiều ngược lại, đồng thời thay đổi các tham chiếu đến đỉnh cha trong DSU quản lý các thành phần liên thông lớn.
  
    Do đó, chi phí của việc đảo gốc là $O(h)$, trong đó $h$ là chiều cao của cây.
    Bạn có thể ước lượng một cách tệ hơn rằng chi phí này là $O(\text{size})$, trong đó $\text{size}$ là số đỉnh của cây.
    Độ phức tạp cuối cùng không có sự khác biệt lớn.
  
    Bây giờ chúng ta áp dụng một kỹ thuật chuẩn: luôn luôn đảo gốc của cây chứa ít đỉnh hơn.
    Khi đó, trực giác cho thấy trường hợp xấu nhất là khi kết hợp hai cây có kích thước xấp xỉ bằng nhau, nhưng khi đó kết quả sẽ là một cây có kích thước gấp đôi.
    Điều này khiến cho tình huống xấu nhất này không thể xảy ra quá nhiều lần.
  
    Tổng quát, tổng chi phí có thể được viết dưới dạng công thức truy hồi:
    
    \[ T(n) = \max_{k = 1 \ldots n-1} \left\{ T(k) + T(n - k) + O(\min(k, n - k))\right\} \]
    
    $T(n)$ là số thao tác cần thiết để thu được một cây có $n$ đỉnh thông qua việc đảo gốc và hợp nhất các cây.
    Một cây kích thước $n$ có thể được tạo ra bằng cách kết hợp hai cây nhỏ hơn có kích thước $k$ và $n - k$.
    Phương trình truy hồi này có nghiệm là $T(n) = O (n \log n)$.
  
    Do đó, tổng thời gian dành cho tất cả các thao tác đảo gốc sẽ là $O(n \log n)$ nếu chúng ta luôn chọn cây nhỏ hơn để đảo gốc.
  
    Chúng ta cần phải duy trì kích thước của từng thành phần liên thông lớn, nhưng cấu trúc dữ liệu DSU cho phép thực hiện việc này một cách dễ dàng.
  
  * Tìm chu trình được tạo ra khi thêm một cạnh mới $(a, b)$.
    Vì $a$ và $b$ đã được kết nối trong cây nên chúng ta cần tìm [Tổ tiên chung gần nhất (LCA)](lca.md) của các đỉnh $a$ và $b$.
    Chu trình sẽ gồm đường đi từ $b$ đến LCA, từ LCA đến $a$ và cạnh nối từ $a$ đến $b$.
  
    Sau khi tìm thấy chu trình, chúng ta co tất cả các đỉnh thuộc chu trình đã phát hiện thành một đỉnh duy nhất.
    Điều này nghĩa là chúng ta có độ phức tạp tỷ lệ thuận với chiều dài chu trình, do đó chúng ta có thể sử dụng bất kỳ thuật toán LCA nào có độ phức tạp tỷ lệ với độ dài đường đi mà không cần thuật toán quá nhanh.
  
    Vì tất cả thông tin về cấu trúc của cây đều có sẵn trong mảng đỉnh cha `par[]`, thuật toán LCA hợp lý nhất là:
    đánh dấu các đỉnh $a$ và $b$ là đã ghé thăm, sau đó di chuyển lên các đỉnh cha `par[a]` và `par[b]` và đánh dấu chúng, tiếp tục đi lên các đỉnh cha của chúng, v.v., cho đến khi gặp một đỉnh đã được đánh dấu từ trước.
    Đỉnh này chính là LCA cần tìm, và chúng ta có thể tìm lại các đỉnh trên chu trình bằng cách đi dọc theo đường đi từ $a$ và $b$ đến LCA một lần nữa.
  
    Rõ ràng độ phức tạp của thuật toán này tỷ lệ thuận với chiều dài của chu trình cần tìm.
  
  * Co chu trình khi thêm một cạnh mới $(a, b)$ trong cây.
  
    Chúng ta cần tạo ra một thành phần liên thông 2-cạnh mới chứa tất cả các đỉnh của chu trình vừa phát hiện (bản thân chu trình này cũng có thể chứa một số thành phần liên thông 2-cạnh cũ, nhưng điều này không làm thay đổi bản chất).
    Ngoài ra, việc co này cần được thực hiện sao cho cấu trúc của cây không bị phá vỡ, và tất cả các con trỏ `par[]` cùng với hai cấu trúc DSU vẫn chính xác.
  
    Cách đơn giản nhất để làm điều này là co tất cả các đỉnh của chu trình về đỉnh LCA của chúng.
    Thực tế, LCA là đỉnh cao nhất trong chu trình, tức là con trỏ cha `par[]` của nó vẫn được giữ nguyên.
    Đối với tất cả các đỉnh khác trong chu trình, đỉnh cha của chúng không cần phải cập nhật vì những đỉnh này đơn giản là không còn tồn tại độc lập nữa.
    Trong DSU của các thành phần liên thông 2-cạnh, tất cả các đỉnh này sẽ trỏ trực tiếp đến LCA.
  
    Chúng ta sẽ cài đặt DSU của các thành phần liên thông 2-cạnh mà không dùng tối ưu hóa gộp theo hạng, do đó chúng ta sẽ có độ phức tạp trung bình là $O(\log n)$ cho mỗi truy vấn.
    Để đạt được độ phức tạp trung bình $O(1)$ cho mỗi truy vấn, chúng ta cần gộp các đỉnh của chu trình theo hạng, và sau đó gán lại `par[]` tương ứng.

## Cài đặt

Dưới đây là mã nguồn cài đặt hoàn chỉnh cho toàn bộ thuật toán.

Như đã đề cập ở trên, để cho đơn giản, DSU của các thành phần liên thông 2-cạnh được viết không áp dụng gộp theo hạng, vì vậy độ phức tạp kết quả sẽ là trung bình $O(\log n)$.

Trong bản cài đặt này, các cầu không được lưu trữ cụ thể mà chỉ lưu số lượng của chúng trong biến `bridges`.
Tuy nhiên, việc lưu trữ cụ thể các cầu bằng một cấu trúc `set` là không hề khó khăn.

Ban đầu bạn gọi hàm `init()`, hàm này sẽ khởi tạo hai DSU (tạo ra một tập hợp riêng cho mỗi đỉnh và đặt kích thước ban đầu bằng 1), và thiết lập các đỉnh cha `par`.

Hàm chính là `add_edge(a, b)`, dùng để xử lý và thêm một cạnh mới.

```cpp
vector<int> par, dsu_2ecc, dsu_cc, dsu_cc_size;
int bridges;
int lca_iteration;
vector<int> last_visit;
 
void init(int n) {
    par.resize(n);
    dsu_2ecc.resize(n);
    dsu_cc.resize(n);
    dsu_cc_size.resize(n);
    lca_iteration = 0;
    last_visit.assign(n, 0);
    for (int i=0; i<n; ++i) {
        dsu_2ecc[i] = i;
        dsu_cc[i] = i;
        dsu_cc_size[i] = 1;
        par[i] = -1;
    }
    bridges = 0;
}
 
int find_2ecc(int v) {
    if (v == -1)
        return -1;
    return dsu_2ecc[v] == v ? v : dsu_2ecc[v] = find_2ecc(dsu_2ecc[v]);
}
 
int find_cc(int v) {
    v = find_2ecc(v);
    return dsu_cc[v] == v ? v : dsu_cc[v] = find_cc(dsu_cc[v]);
}
 
void make_root(int v) {
    int root = v;
    int child = -1;
    while (v != -1) {
        int p = find_2ecc(par[v]);
        par[v] = child;
        dsu_cc[v] = root;
        child = v;
        v = p;
    }
    dsu_cc_size[root] = dsu_cc_size[child];
}

void merge_path (int a, int b) {
    ++lca_iteration;
    vector<int> path_a, path_b;
    int lca = -1;
    while (lca == -1) {
        if (a != -1) {
            a = find_2ecc(a);
            path_a.push_back(a);
            if (last_visit[a] == lca_iteration){
                lca = a;
                break;
                }
            last_visit[a] = lca_iteration;
            a = par[a];
        }
        if (b != -1) {
            b = find_2ecc(b);
            path_b.push_back(b);
            if (last_visit[b] == lca_iteration){
                lca = b;
                break;
                }
            last_visit[b] = lca_iteration;
            b = par[b];
        }
        
    }

    for (int v : path_a) {
        dsu_2ecc[v] = lca;
        if (v == lca)
            break;
        --bridges;
    }
    for (int v : path_b) {
        dsu_2ecc[v] = lca;
        if (v == lca)
            break;
        --bridges;
    }
}
 
void add_edge(int a, int b) {
    a = find_2ecc(a);
    b = find_2ecc(b);
    if (a == b)
        return;
 
    int ca = find_cc(a);
    int cb = find_cc(b);

    if (ca != cb) {
        ++bridges;
        if (dsu_cc_size[ca] > dsu_cc_size[cb]) {
            swap(a, b);
            swap(ca, cb);
        }
        make_root(a);
        par[a] = dsu_cc[a] = b;
        dsu_cc_size[cb] += dsu_cc_size[a];
    } else {
        merge_path(a, b);
    }
}
```

DSU cho các thành phần liên thông 2-cạnh được lưu trữ trong vector `dsu_2ecc`, và hàm trả về đại diện là `find_2ecc(v)`.
Hàm này được sử dụng nhiều lần trong các phần còn lại của mã nguồn, bởi vì sau khi co một số đỉnh thành một đỉnh duy nhất, tất cả các đỉnh này không còn tồn tại độc lập nữa, và thay vào đó chỉ có đỉnh đại diện (leader) mới lưu trữ đỉnh cha `par` chính xác trong rừng của các thành phần liên thông 2-cạnh.

DSU cho các thành phần liên thông lớn được lưu trữ trong vector `dsu_cc`, và cũng có thêm một vector phụ `dsu_cc_size` để lưu trữ kích thước của thành phần liên thông đó.
Hàm `find_cc(v)` trả về đỉnh đại diện của thành phần liên thông lớn (thực tế chính là gốc của cây chứa đỉnh đó).

Hàm đảo gốc cây `make_root(v)` hoạt động như đã mô tả ở trên:
nó đi từ đỉnh $v$ qua các đỉnh cha lên đến đỉnh gốc, mỗi lần đi qua đều đổi hướng con trỏ cha `par` theo chiều ngược lại.
Liên kết trỏ đến đại diện của thành phần liên thông lớn `dsu_cc` cũng được cập nhật để trỏ đến đỉnh gốc mới.
Sau khi đảo gốc, chúng ta phải gán kích thước chính xác của thành phần liên thông lớn cho đỉnh gốc mới.
Đồng thời, chúng ta phải cẩn thận gọi `find_2ecc()` để lấy đại diện của thành phần liên thông 2-cạnh, thay vì một số đỉnh đã bị co từ trước.

Hàm tìm và co chu trình `merge_path(a, b)` cũng được cài đặt như mô tả ở trên.
Nới tìm kiếm LCA của $a$ và $b$ bằng cách đi lên đồng thời từ hai đỉnh này cho đến khi gặp một đỉnh đã đi qua lần thứ hai.
Để tối ưu hiệu năng, chúng ta chọn một mã định danh duy nhất cho mỗi lần gọi tìm kiếm LCA và đánh dấu các đỉnh đã đi qua bằng mã định danh này.
Cách này hoạt động trong $O(1)$, trong khi các cách tiếp cận khác như sử dụng `std::set` có hiệu năng kém hơn.
Các đường đi đã đi qua được lưu trữ trong hai vector `path_a` và `path_b`, và chúng ta sử dụng chúng để duyệt qua các đỉnh này lần thứ hai lên tới LCA, nhờ đó lấy được tất cả các đỉnh của chu trình.
Tất cả các đỉnh trong chu trình được co lại bằng cách gán chúng trỏ đến LCA, do đó độ phức tạp trung bình là $O(\log n)$ (vì chúng ta không dùng gộp theo hạng).
Tất cả các cạnh được duyệt qua đều từng là cầu, vì thế chúng ta trừ đi 1 khỏi biến `bridges` cho mỗi cạnh trong chu trình.

Cuối cùng, hàm truy vấn `add_edge(a, b)` xác định các thành phần liên thông lớn chứa hai đỉnh $a$ và $b$.
Nếu chúng nằm ở hai thành phần liên thông khác nhau, cây nhỏ hơn sẽ được đảo gốc rồi kết nối vào cây lớn hơn.
Ngược lại, nếu các đỉnh $a$ và $b$ nằm trong cùng một cây nhưng ở các thành phần liên thông 2-cạnh khác nhau, hàm `merge_path(a, b)` được gọi để phát hiện chu trình và co nó thành một thành phần liên thông 2-cạnh duy nhất.
