---
tags:
  - Translated
e_maxx_link: prufer_code_cayley_formula
---

# Mã Prüfer

Trong bài viết này, chúng ta sẽ tìm hiểu về khái niệm **mã Prüfer** (hay dãy Prüfer) - một phương pháp mã hóa một cây có nhãn thành một dãy số duy nhất.

Nhờ có mã Prüfer, chúng ta sẽ chứng minh **Định lý Cayley** (công thức xác định số lượng cây khung của một đồ thị đầy đủ).
Chúng ta cũng sẽ trình bày lời giải cho bài toán đếm số cách thêm cạnh vào đồ thị để đồ thị trở nên liên thông.

**Lưu ý**, chúng ta sẽ không xét các cây chỉ có một đỉnh đơn lẻ - đây là trường hợp đặc biệt làm sai lệch một số phát biểu.

## Mã Prüfer

Mã Prüfer là một cách mã hóa một cây có nhãn gồm $n$ đỉnh bằng một dãy gồm $n - 2$ số nguyên trong đoạn $[0; n-1]$.
Phép mã hóa này đồng thời là một **song ánh** giữa tất cả các cây khung của đồ thị đầy đủ và các dãy số kể trên.

Mặc dù việc sử dụng mã Prüfer để lưu trữ và thực hiện các phép toán trên cây là không thực tế vì cách biểu diễn này, mã Prüfer lại được sử dụng rất thường xuyên để giải các bài toán tổ hợp.

Người phát minh ra mã này là nhà toán học Heinz Prüfer, ông đề xuất vào năm 1918 như là một chứng minh cho Định lý Cayley.

### Xây dựng mã Prüfer từ một cây cho trước

Mã Prüfer được xây dựng như sau.
Chúng ta sẽ lặp lại quy trình sau đây $n - 2$ lần:
chọn đỉnh lá của cây có chỉ số nhỏ nhất, xóa nó khỏi cây, và ghi lại chỉ số của đỉnh kề kết nối với nó.
Sau $n - 2$ lần lặp, trên đồ thị chỉ còn lại đúng $2$ đỉnh và thuật toán kết thúc.

Do đó, mã Prüfer của một cây là một dãy gồm $n - 2$ số, trong đó mỗi số là chỉ số của đỉnh kề tương ứng, tức là số nằm trong đoạn $[0, n-1]$.

Thuật toán tính mã Prüfer có thể được cài đặt dễ dàng với độ phức tạp $O(n \log n)$, đơn giản bằng cách sử dụng một cấu trúc dữ liệu cho phép lấy ra giá trị nhỏ nhất (ví dụ: `std::set` hoặc `std::priority_queue` trong C++), lưu trữ danh sách các đỉnh lá hiện tại của cây.

```{.cpp file=pruefer_code_slow}
vector<vector<int>> adj;

vector<int> pruefer_code() {
    int n = adj.size();
    set<int> leafs;
    vector<int> degree(n);
    vector<bool> killed(n, false);
    for (int i = 0; i < n; i++) {
        degree[i] = adj[i].size();
        if (degree[i] == 1)
            leafs.insert(i);
    }

    vector<int> code(n - 2);
    for (int i = 0; i < n - 2; i++) {
        int leaf = *leafs.begin();
        leafs.erase(leafs.begin());
        killed[leaf] = true;

        int v;
        for (int u : adj[leaf]) {
            if (!killed[u])
                v = u;
        }

        code[i] = v;
        if (--degree[v] == 1)
            leafs.insert(v);
    }

    return code;
}
```

Tuy nhiên, chúng ta cũng có thể cài đặt việc xây dựng mã Prüfer trong thời gian tuyến tính.
Phương pháp này sẽ được mô tả trong phần tiếp theo.

### Xây dựng mã Prüfer trong thời gian tuyến tính

Ý tưởng cốt lõi của thuật toán là sử dụng một **con trỏ di động** (moving pointer), con trỏ này sẽ luôn trỏ đến đỉnh lá nhỏ nhất hiện tại cần loại bỏ.

Thoạt nhìn, việc này có vẻ bất khả thi, vì trong quá trình xây dựng mã Prüfer, chỉ số của đỉnh lá nhỏ nhất có thể tăng lên hoặc giảm đi.
Tuy nhiên, nếu xem xét kỹ hơn, điều này không hoàn toàn đúng.
Số lượng đỉnh lá sẽ không tăng lên. Nó chỉ có thể giảm đi một (chúng ta loại bỏ một lá và không sinh ra lá mới), hoặc giữ nguyên (chúng ta loại bỏ một lá và sinh ra đúng một lá mới).
Trong trường hợp đầu tiên, không có cách nào khác là tìm đỉnh lá nhỏ nhất tiếp theo.
Tuy nhiên, trong trường hợp thứ hai, chúng ta có thể quyết định trong $O(1)$ xem có thể tiếp tục sử dụng đỉnh vừa mới trở thành lá hay không, hoặc có cần đi tìm đỉnh lá nhỏ nhất khác không.
Và trong phần lớn các trường hợp, chúng ta có thể tiếp tục xử lý với đỉnh lá mới sinh ra đó.

Để thực hiện việc này, chúng ta sử dụng một biến $\text{ptr}$, dùng để chỉ ra rằng trong tập các đỉnh từ $0$ đến $\text{ptr}$ có tối đa một đỉnh lá, cụ thể là đỉnh hiện tại đang xử lý.
Tất cả các đỉnh khác trong đoạn đó hoặc đã bị loại khỏi cây, hoặc vẫn còn nhiều hơn một đỉnh kề.
Đồng thời, ta quy ước chưa loại bỏ bất kỳ đỉnh lá nào lớn hơn $\text{ptr}$.

Biến này rất hữu ích trong trường hợp thứ nhất.
Sau khi loại bỏ lá hiện tại, chúng ta biết rằng không thể có lá nào nằm giữa $0$ và $\text{ptr}$, do đó chúng ta có thể bắt đầu tìm kiếm lá tiếp theo trực tiếp từ $\text{ptr} + 1$, mà không cần tìm lại từ đỉnh $0$.
Trong trường hợp thứ hai, chúng ta phân biệt hai tình huống:
Hoặc đỉnh lá mới sinh ra nhỏ hơn $\text{ptr}$, thì nó chắc chắn phải là lá nhỏ nhất tiếp theo cần xóa, vì chúng ta biết không còn đỉnh nào khác nhỏ hơn $\text{ptr}$ là lá.
Hoặc đỉnh lá mới sinh ra lớn hơn $\text{ptr}$.
Nhưng khi đó chúng ta cũng biết rằng nó phải lớn hơn $\text{ptr}$, và có thể bắt đầu tìm kiếm lại từ $\text{ptr} + 1$.

Mặc dù thỉnh thoảng chúng ta phải tìm kiếm tuyến tính để tìm lá tiếp theo, con trỏ $\text{ptr}$ chỉ tăng lên, do đó tổng độ phức tạp thời gian chạy là $O(n)$.

```{.cpp file=pruefer_code_fast}
vector<vector<int>> adj;
vector<int> parent;

void dfs(int v) {
    for (int u : adj[v]) {
        if (u != parent[v]) {
            parent[u] = v;
            dfs(u);
        }
    }
}

vector<int> pruefer_code() {
    int n = adj.size();
    parent.resize(n);
    parent[n-1] = -1;
    dfs(n-1);

    int ptr = -1;
    vector<int> degree(n);
    for (int i = 0; i < n; i++) {
        degree[i] = adj[i].size();
        if (degree[i] == 1 && ptr == -1)
            ptr = i;
    }

    vector<int> code(n - 2);
    int leaf = ptr;
    for (int i = 0; i < n - 2; i++) {
        int next = parent[leaf];
        code[i] = next;
        if (--degree[next] == 1 && next < ptr) {
            leaf = next;
        } else {
            ptr++;
            while (degree[ptr] != 1)
                ptr++;
            leaf = ptr;
        }
    }

    return code;
}
```

Trong mã nguồn trên, đầu tiên chúng ta tìm đỉnh cha `parent[i]` của mỗi đỉnh, tức là đỉnh cha mà đỉnh này sẽ kết nối khi chúng ta loại bỏ nó khỏi cây.
Chúng ta có thể tìm đỉnh cha bằng cách đặt gốc của cây tại đỉnh $n-1$.
Điều này khả thi vì đỉnh $n-1$ sẽ không bao giờ bị loại bỏ khỏi cây.
Chúng ta cũng tính bậc cho mỗi đỉnh.
`ptr` là con trỏ chỉ ra giá trị nhỏ nhất trong số các đỉnh lá còn lại (ngoại trừ lá hiện tại `leaf`).
Chúng ta sẽ gán đỉnh lá hiện tại bằng `next` nếu `next` cũng trở thành đỉnh lá và nhỏ hơn `ptr`, hoặc chúng ta thực hiện tìm kiếm tuyến tính đỉnh lá nhỏ nhất bằng cách tăng con trỏ.

Dễ dàng thấy mã nguồn này chạy trong độ phức tạp $O(n)$.

### Một số tính chất của mã Prüfer

- Sau khi xây dựng mã Prüfer, hai đỉnh sẽ còn lại trên cây.
  Một trong số chúng là đỉnh có chỉ số lớn nhất $n-1$, nhưng không thể nói trước điều gì về đỉnh còn lại.
- Mỗi đỉnh xuất hiện trong mã Prüfer đúng một số lần cố định - bằng bậc của nó trừ đi 1.
  Điều này rất dễ kiểm chứng, vì bậc của đỉnh sẽ giảm đi 1 mỗi khi nhãn của nó được ghi vào mã, và nó bị loại bỏ khi bậc giảm về $1$.
  Đối với hai đỉnh còn lại, tính chất này cũng đúng.

### Khôi phục cây từ mã Prüfer

Để khôi phục lại cây, chúng ta chỉ cần tập trung vào tính chất đã thảo luận ở phần trước.
Chúng ta đã biết trước bậc của mọi đỉnh trong cây kết quả.
Do đó, chúng ta có thể tìm tất cả các đỉnh lá, và xác định lá đầu tiên bị loại bỏ ở bước đầu tiên (đó phải là lá nhỏ nhất).
Lá này được kết nối với đỉnh có chỉ số tương ứng với giá trị nằm ở ô đầu tiên của mã Prüfer.

Như vậy chúng ta tìm được cạnh đầu tiên bị loại bỏ khi sinh ra mã Prüfer.
Chúng ta có thể thêm cạnh này vào kết quả và giảm bậc của hai đầu cạnh đi 1.

Chúng ta lặp lại thao tác này cho đến khi sử dụng hết tất cả các số trong mã Prüfer:
tìm đỉnh nhỏ nhất có bậc bằng $1$, kết nối nó với đỉnh tiếp theo từ mã Prüfer, và giảm bậc.

Cuối cùng, chúng ta chỉ còn lại hai đỉnh có bậc bằng $1$.
Đây là hai đỉnh không bị loại bỏ trong quy trình sinh mã Prüfer.
Chúng ta kết nối chúng để có được cạnh cuối cùng của cây.
Một trong hai đỉnh này luôn là đỉnh $n-1$.

Thuật toán này có thể được **cài đặt** dễ dàng trong $O(n \log n)$ bằng cách sử dụng một cấu trúc dữ liệu cho phép lấy ra phần tử nhỏ nhất (ví dụ: `std::set<>` hoặc `std::priority_queue<>` trong C++) để lưu trữ tất cả các đỉnh lá.

Bản cài đặt dưới đây trả về danh sách các cạnh của cây kết quả.

```{.cpp file=pruefer_decode_slow}
vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
    int n = code.size() + 2;
    vector<int> degree(n, 1);
    for (int i : code)
        degree[i]++;

    set<int> leaves;
    for (int i = 0; i < n; i++) {
        if (degree[i] == 1)
            leaves.insert(i);
    }

    vector<pair<int, int>> edges;
    for (int v : code) {
        int leaf = *leaves.begin();
        leaves.erase(leaves.begin());

        edges.emplace_back(leaf, v);
        if (--degree[v] == 1)
            leaves.insert(v);
    }
    edges.emplace_back(*leaves.begin(), n-1);
    return edges;
}
```

### Khôi phục cây từ mã Prüfer trong thời gian tuyến tính

Để khôi phục cây trong thời gian tuyến tính, chúng ta áp dụng cùng kỹ thuật đã dùng để sinh mã Prüfer trong thời gian tuyến tính.

Chúng ta không cần một cấu trúc dữ liệu để lấy ra giá trị nhỏ nhất.
Thay vào đó, ta nhận thấy sau khi xử lý cạnh hiện tại, chỉ có một đỉnh có thể trở thành lá.
Do đó, chúng ta có thể chọn tiếp tục xử lý đỉnh này, hoặc tìm đỉnh nhỏ nhất khác bằng cách dịch chuyển một con trỏ.

```{.cpp file=pruefer_decode_fast}
vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
    int n = code.size() + 2;
    vector<int> degree(n, 1);
    for (int i : code)
        degree[i]++;

    int ptr = 0;
    while (degree[ptr] != 1)
        ptr++;
    int leaf = ptr;

    vector<pair<int, int>> edges;
    for (int v : code) {
        edges.emplace_back(leaf, v);
        if (--degree[v] == 1 && v < ptr) {
            leaf = v;
        } else {
            ptr++;
            while (degree[ptr] != 1)
                ptr++;
            leaf = ptr;
        }
    }
    edges.emplace_back(leaf, n-1);
    return edges;
}
```

### Song ánh giữa cây và mã Prüfer

Với mỗi cây, tồn tại một mã Prüfer tương ứng duy nhất.
Và từ mỗi mã Prüfer, chúng ta có thể khôi phục lại cây gốc duy nhất.

Từ đó suy ra mỗi mã Prüfer (tức là một dãy gồm $n-2$ số trong đoạn $[0; n - 1]$) đều tương ứng với một cây.

Do đó, tất cả các cây và tất cả các mã Prüfer tạo thành một song ánh (tương ứng một-một).

## Công thức Cayley

Công thức Cayley phát biểu rằng **số lượng cây khung trong một đồ thị đầy đủ có nhãn** gồm $n$ đỉnh bằng:

$$n^{n-2}$$

Có nhiều cách chứng minh cho công thức này.
Sử dụng khái niệm mã Prüfer, phát biểu trên được chứng minh một cách rất hiển nhiên.

Thật vậy, bất kỳ mã Prüfer nào chứa $n-2$ số thuộc đoạn $[0; n-1]$ cũng đều tương ứng với một cây có nhãn gồm $n$ đỉnh.
Do đó chúng ta có $n^{n-2}$ mã Prüfer khác nhau.
Vì mỗi cây như vậy là một cây khung của đồ thị đầy đủ gồm $n$ đỉnh, số lượng cây khung này cũng bằng $n^{n-2}$.

## Số cách làm cho đồ thị liên thông

Khái niệm mã Prüfer còn mạnh hơn thế.
Nó cho phép chúng ta suy ra các công thức tổng quát hơn nhiều so với công thức Cayley.

Trong bài toán này, chúng ta được cho một đồ thị gồm $n$ đỉnh và $m$ cạnh.
Đồ thị hiện tại có $k$ thành phần liên thông.
Chúng ta muốn tính số cách thêm $k-1$ cạnh để đồ thị trở nên liên thông (rõ ràng $k-1$ là số lượng cạnh tối thiểu cần thiết để làm đồ thị liên thông).

Hãy cùng xây dựng công thức để giải quyết bài toán này.

Gọi $s_1, \dots, s_k$ là kích thước của các thành phần liên thông trong đồ thị.
Chúng ta không thể thêm các cạnh nối giữa các đỉnh trong cùng một thành phần liên thông.
Do đó, bài toán này rất giống với việc tìm số lượng cây khung của một đồ thị đầy đủ gồm $k$ đỉnh.
Sự khác biệt duy nhất là mỗi đỉnh trong đồ thị đầy đủ này thực tế có kích thước là $s_i$: mỗi cạnh nối với đỉnh $i$ thực tế sẽ nhân kết quả lên $s_i$ lần.

Do đó, để tính số cách có thể có, điều quan trọng là đếm xem mỗi đỉnh trong số $k$ đỉnh được sử dụng bao nhiêu lần trong cây kết nối.
Để thu được công thức cho bài toán, chúng ta cần lấy tổng kết quả trên tất cả các bộ bậc có thể có.

Gọi $d_1, \dots, d_k$ là bậc của các đỉnh tương ứng với các thành phần liên thông sau khi kết nối.
Tổng các bậc bằng hai lần số cạnh:

$$\sum_{i=1}^k d_i = 2k - 2$$

Nếu đỉnh $i$ có bậc $d_i$, thì nó xuất hiện đúng $d_i - 1$ lần trong mã Prüfer.
Mã Prüfer cho một cây có $k$ đỉnh có độ dài là $k-2$.
Do đó, số cách chọn một mã có $k-2$ số sao cho số $i$ xuất hiện đúng $d_i - 1$ lần bằng **hệ số đa thức** (multinomial coefficient):

$$\binom{k-2}{d_1-1, d_2-1, \dots, d_k-1} = \frac{(k-2)!}{(d_1-1)! (d_2-1)! \cdots (d_k-1)!}.$$

Vì mỗi cạnh kề với đỉnh $i$ làm kết quả nhân lên $s_i$ lần, chúng ta thu được kết quả ứng với trường hợp bậc các đỉnh là $d_1, \dots, d_k$:

$$s_1^{d_1} \cdot s_2^{d_2} \cdots s_k^{d_k} \cdot \binom{k-2}{d_1-1, d_2-1, \dots, d_k-1}$$

Để có câu trả lời cuối cùng, chúng ta lấy tổng trên tất cả các cách chọn bậc của đỉnh:

$$\sum_{\substack{d_i \ge 1 \\\\ \sum_{i=1}^k d_i = 2k -2}} s_1^{d_1} \cdot s_2^{d_2} \cdots s_k^{d_k} \cdot \binom{k-2}{d_1-1, d_2-1, \dots, d_k-1}$$

Biểu thức này trông có vẻ rất đáng sợ, tuy nhiên chúng ta có thể sử dụng **định lý đa thức** (multinomial theorem), phát biểu rằng:

$$(x_1 + \dots + x_m)^p = \sum_{\substack{c_i \ge 0 \\\\ \sum_{i=1}^m c_i = p}} x_1^{c_1} \cdot x_2^{c_2} \cdots x_m^{c_m} \cdot \binom{p}{c_1, c_2, \dots c_m}$$

Hai biểu thức trông đã khá giống nhau.
Để áp dụng định lý này, chúng ta đặt $e_i = d_i - 1$:

$$\sum_{\substack{e_i \ge 0 \\\\ \sum_{i=1}^k e_i = k - 2}} s_1^{e_1+1} \cdot s_2^{e_2+1} \cdots s_k^{e_k+1} \cdot \binom{k-2}{e_1, e_2, \dots, e_k}$$

Sau khi áp dụng định lý đa thức, chúng ta thu được **câu trả lời của bài toán**:

$$s_1 \cdot s_2 \cdots s_k \cdot (s_1 + s_2 + \dots + s_k)^{k-2} = s_1 \cdot s_2 \cdots s_k \cdot n^{k-2}$$

Công thức này vẫn đúng với trường hợp $k = 1$.

## Bài tập luyện tập

- [UVA #10843 - Anne's game](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=20&page=show_problem&problem=1784)
- [Timus #1069 - Prufer Code](http://acm.timus.ru/problem.aspx?space=1&num=1069)
- [Codeforces - Clues](http://codeforces.com/contest/156/problem/D)
- [Topcoder - TheCitiesAndRoadsDivTwo](https://community.topcoder.com/stat?c=problem_statement&pm=10774&rd=14146)
