---
tags:
  - Translated
e_maxx_link: kuhn_matching
lang: vi
---

# Thuật toán Kuhn tìm bộ ghép cực đại trên đồ thị hai phía

## Bài toán
Cho một đồ thị hai phía (bipartite graph) $G$ gồm $n$ đỉnh và $m$ cạnh. Tìm bộ ghép cực đại (maximum matching), tức là chọn nhiều cạnh nhất có thể sao cho không có hai cạnh được chọn nào chung đỉnh.

## Mô tả thuật toán

### Các định nghĩa cần thiết

* Một **bộ ghép** (matching) $M$ là một tập các cạnh đôi một không kề nhau của đồ thị (nói cách khác, không có quá một cạnh từ tập hợp này liên thuộc với bất kỳ đỉnh nào của đồ thị $M$). 
**Bản số** (cardinality - kích thước) của bộ ghép là số lượng cạnh trong bộ ghép đó.
Tất cả những đỉnh có cạnh kề thuộc bộ ghép (tức là có bậc đúng bằng 1 trong đồ thị con tạo bởi $M$) được gọi là **bão hòa** (saturated) bởi bộ ghép này.

* Một **bộ ghép cực đại địa phương** (maximal matching) là một bộ ghép $M$ của đồ thị $G$ mà không là tập con của bất kỳ bộ ghép nào khác.

* Một **bộ ghép cực đại** (maximum matching - hay bộ ghép có bản số lớn nhất) là một bộ ghép chứa số lượng cạnh lớn nhất có thể. Mọi bộ ghép cực đại đều là bộ ghép cực đại địa phương.

* Một **đường đi** (path) có độ dài $k$ ở đây có nghĩa là một đường đi *đơn* (không chứa đỉnh hay cạnh lặp lại) gồm $k$ cạnh, trừ khi có quy định khác.

* Một **đường đi xen kẽ** (alternating path - trong đồ thị hai phía, đối với một bộ ghép nào đó) là một đường đi mà các cạnh của nó xen kẽ giữa việc thuộc và không thuộc bộ ghép.

* Một **đường tăng** (augmenting path - trong đồ thị hai phía, đối với một bộ ghép nào đó) là một đường đi xen kẽ có đỉnh đầu và đỉnh cuối chưa bão hòa, tức là chúng không thuộc bộ ghép.

* **Hiệu đối xứng** (symmetric difference) của hai tập hợp $A$ và $B$, ký hiệu là $A \oplus B$, là tập hợp tất cả các phần tử chỉ thuộc về đúng một trong hai tập hợp $A$ hoặc $B$, nhưng không thuộc về cả hai.
Nghĩa là, $A \oplus B = (A - B) \cup (B - A) = (A \cup B) - (A \cap B)$.

### Bổ đề Berge

Bổ đề này được chứng minh bởi nhà toán học người Pháp **Claude Berge** vào năm 1957, mặc dù nó đã được quan sát trước đó bởi nhà toán học người Đan Mạch **Julius Petersen** vào năm 1891 và nhà toán học người Hungary **Denés Kőnig** vào năm 1931.

#### Phát biểu
Một bộ ghép $M$ là cực đại $\Leftrightarrow$ không có đường tăng đối với bộ ghép $M$.

#### Chứng minh

Cả hai chiều của mệnh đề tương đương sẽ được chứng minh bằng phản chứng.

1. Bộ ghép $M$ là cực đại $\Rightarrow$ không có đường tăng đối với bộ ghép $M$.
  
   Giả sử tồn tại một đường tăng $P$ đối với bộ ghép cực đại $M$ hiện tại. Đường tăng $P$ này chắc chắn sẽ có độ dài lẻ, có số cạnh không thuộc $M$ nhiều hơn số cạnh thuộc $M$ đúng 1 cạnh.
   Chúng ta tạo một bộ ghép mới $M'$ bằng cách lấy tất cả các cạnh trong bộ ghép ban đầu $M$ ngoại trừ các cạnh cũng nằm trong $P$, và thêm các cạnh trong $P$ không nằm trong $M$.
   Đây là một bộ ghép hợp lệ vì các đỉnh đầu và đỉnh cuối của $P$ chưa bị bão hòa bởi $M$, và các đỉnh còn lại chỉ bị bão hòa bởi bộ ghép $P \cap M$.
   Bộ ghép mới $M'$ này sẽ có nhiều hơn $M$ đúng 1 cạnh, do đó $M$ không thể là bộ ghép cực đại.
   
   Nói một cách hình thức, với một đường tăng $P$ đối với bộ ghép cực đại $M$, bộ ghép $M' = P \oplus M$ thỏa mãn $|M'| = |M| + 1$, dẫn đến mâu thuẫn.
  
2. Bộ ghép $M$ là cực đại $\Leftarrow$ không có đường tăng đối với bộ ghép $M$.

   Giả sử tồn tại một bộ ghép $M'$ có bản số lớn hơn $M$. Chúng ta xét hiệu đối xứng $Q = M \oplus M'$. Đồ thị con $Q$ không nhất thiết phải là một bộ ghép.
   Bất kỳ đỉnh nào trong $Q$ đều có bậc tối đa là $2$, điều đó có nghĩa là mỗi thành phần liên thông trong nó sẽ là một trong ba dạng sau:

      * một đỉnh cô lập
      * một đường đi (đơn) có các cạnh xen kẽ lần lượt thuộc $M$ và $M'$
      * một chu trình có độ dài chẵn có các cạnh xen kẽ lần lượt thuộc $M$ và $M'$
 
   Vì $M'$ có bản số lớn hơn $M$, đồ thị $Q$ có nhiều cạnh thuộc $M'$ hơn $M$. Theo nguyên lý Dirichlet (Pigeonhole principle), ít nhất một thành phần liên thông sẽ là một đường đi chứa nhiều cạnh của $M'$ hơn cạnh của $M$. Vì bất kỳ đường đi nào như vậy là xen kẽ, nó sẽ có đỉnh đầu và đỉnh cuối chưa bão hòa bởi $M$, khiến nó trở thành một đường tăng đối với $M$, mâu thuẫn với giả thiết. &ensp; $\blacksquare$

### Thuật toán Kuhn
  
Thuật toán Kuhn là một ứng dụng trực tiếp của bổ đề Berge. Nó được mô tả ngắn gọn như sau:

Đầu tiên, chúng ta bắt đầu với một bộ ghép rỗng. Sau đó, chừng nào thuật toán vẫn tìm được đường tăng, chúng ta cập nhật bộ ghép bằng cách hoán đổi các cạnh dọc theo đường đi này và lặp lại quá trình tìm đường tăng. Ngay khi không thể tìm thấy đường đi như vậy nữa, chúng ta dừng quá trình - bộ ghép hiện tại chính là bộ ghép cực đại.

Công việc còn lại là chi tiết hóa cách tìm đường tăng. Thuật toán Kuhn tìm kiếm bất kỳ đường đi nào như vậy bằng cách sử dụng phép duyệt [theo chiều sâu](depth-first-search.md) hoặc [theo chiều rộng](breadth-first-search.md) bàn về đồ thị. Thuật toán lần lượt duyệt qua tất cả các đỉnh của đồ thị, bắt đầu mỗi lần duyệt từ đỉnh đó để cố gắng tìm đường tăng xuất phát từ đỉnh này.

Thuật toán sẽ dễ mô tả hơn nếu chúng ta giả định rằng đồ thị đầu vào đã được chia sẵn thành hai phần (mặc dù trên thực tế, thuật toán có thể được cài đặt mà không cần chia đồ thị một cách tường minh).

Thuật toán xét tất cả các đỉnh $v$ thuộc phần thứ nhất của đồ thị: $v = 1 \ldots n_1$. Nếu đỉnh hiện tại $v$ đã được bão hòa bởi bộ ghép hiện tại (tức là đã có cạnh nối với nó được chọn), thì chúng ta bỏ qua đỉnh này. Ngược lại, thuật toán cố gắng bão hòa đỉnh này bằng cách bắt đầu tìm kiếm một đường tăng xuất phát từ nó.

Việc tìm kiếm đường tăng được thực hiện bằng một phép duyệt theo chiều sâu hoặc theo chiều rộng đặc biệt (thông thường duyệt theo chiều sâu được sử dụng nhiều hơn vì dễ cài đặt). Ban đầu, duyệt theo chiều sâu xuất phát từ đỉnh chưa bão hòa $v$ hiện tại thuộc phần thứ nhất. Hãy duyệt qua tất cả các cạnh nối từ đỉnh này. Gọi cạnh hiện tại là $(v, to)$. Nếu đỉnh $to$ chưa được bão hòa bởi bộ ghép, thì chúng ta đã tìm thấy một đường tăng: đường đi này chỉ gồm duy nhất cạnh $(v, to)$; trong trường hợp này, chúng ta chỉ cần thêm cạnh này vào bộ ghép và dừng tìm kiếm đường tăng xuất phát từ đỉnh $v$. Ngược lại, nếu $to$ đã bão hòa bởi một cạnh $(to, p)$, thì chúng ta sẽ đi dọc theo cạnh này: tức là cố gắng tìm một đường tăng đi qua các cạnh $(v, to),(to, p), \ldots$. Để làm điều này, đơn giản là ta di chuyển đến đỉnh $p$ trong phép duyệt - bây giờ chúng ta cố gắng tìm đường tăng xuất phát từ đỉnh này.

Như vậy, phép duyệt này, được khởi chạy từ đỉnh $v$, sẽ hoặc tìm thấy một đường tăng và qua đó bão hòa đỉnh $v$, hoặc không tìm thấy đường tăng nào (và do đó đỉnh $v$ không thể bão hòa).

Sau khi quét qua tất cả các đỉnh $v = 1 \ldots n_1$, bộ ghép hiện tại sẽ là bộ ghép cực đại.

### Thời gian chạy

Thuật toán Kuhn có thể được coi là một chuỗi gồm $n$ lần chạy duyệt theo chiều sâu/chiều rộng trên toàn bộ đồ thị. Do đó, toàn bộ thuật toán được thực hiện trong thời gian $O(nm)$, trong trường hợp xấu nhất là $O(n^3)$.

Tuy nhiên, đánh giá này có thể được cải thiện một chút. Hóa ra đối với thuật toán Kuhn, việc chọn phần nào của đồ thị làm phần thứ nhất và phần nào làm phần thứ hai là rất quan trọng. Thật vậy, trong cài đặt được mô tả ở trên, phép duyệt theo chiều sâu/chiều rộng chỉ bắt đầu từ các đỉnh của phần thứ nhất, nên toàn bộ thuật toán được thực hiện trong thời gian $O(n_1m)$, với $n_1$ là số lượng đỉnh của phần thứ nhất. Trong trường hợp xấu nhất, đây là $O(n_1^2 n_2)$ (với $n_2$ là số lượng đỉnh của phần thứ hai). Điều này chỉ ra rằng thuật toán sẽ hiệu quả hơn nếu chọn phần thứ nhất chứa ít đỉnh hơn phần thứ hai. Trên các đồ thị rất mất cân bằng (khi $n_1$ và $n_2$ rất khác nhau), điều này tạo ra sự khác biệt lớn về thời gian chạy.

## Cài đặt

### Cài đặt chuẩn
Dưới đây giới thiệu một cài đặt của thuật toán trên dựa trên duyệt theo chiều sâu và nhận đầu vào là một đồ thị hai phía được phân chia tường minh thành hai phần. Cài đặt này rất ngắn gọn và có lẽ nên được ghi nhớ theo dạng này.

Ở đây $n$ là số lượng đỉnh ở phần thứ nhất, $k$ là số lượng đỉnh ở phần thứ hai, $g[v]$ là danh sách kề của đỉnh thuộc phần thứ nhất (tức là danh sách các đỉnh thuộc phần thứ hai có cạnh nối từ $v$). Các đỉnh ở cả hai phần được đánh số độc lập, tức là các đỉnh ở phần thứ nhất được đánh số $1 \ldots n$, còn ở phần thứ hai được đánh số $1 \ldots k$.

Có hai mảng bổ trợ: $\rm mt$ và $\rm used$. Mảng thứ nhất - $\rm mt$ - chứa thông tin về bộ ghép hiện tại. Để tiện lập trình, thông tin này chỉ được lưu cho các đỉnh của phần thứ hai: $\textrm{mt[} i \rm]$ - đây là chỉ số của đỉnh thuộc phần thứ nhất được ghép với đỉnh $i$ của phần thứ hai (hoặc $-1$ nếu không có cạnh nào ghép với nó). Mảng thứ hai là $\rm used$: mảng đánh dấu các đỉnh đã "ghé thăm" trong phép duyệt theo chiều sâu (cần thiết để phép duyệt không đi vào cùng một đỉnh hai lần).

Hàm $\textrm{try_kuhn}$ là một phép duyệt theo chiều sâu. Nó trả về $\rm true$ nếu tìm thấy một đường tăng từ đỉnh $v$, và ngầm hiểu rằng hàm này đã thực hiện việc hoán đổi các cạnh dọc theo đường tăng tìm được.

Bên trong hàm, tất cả các cạnh đi ra từ đỉnh $v$ của phần thứ nhất được duyệt qua, và kiểm tra: nếu cạnh này dẫn đến một đỉnh chưa bão hòa $to$, hoặc nếu đỉnh $to$ đã bão hòa nhưng có thể tìm thấy một đường tăng bằng cách gọi đệ quy bắt đầu từ $\textrm{mt[}to \rm ]$, thì chúng ta kết luận đã tìm thấy một đường tăng. Trước khi thoát khỏi hàm với kết quả $\rm true$, chúng ta thay đổi bộ ghép: gán lại đỉnh ghép với $to$ là $v$.

Chương trình chính ban đầu đặt bộ ghép rỗng (danh sách $\rm mt$ được điền các giá trị $-1$). Sau đó, với mỗi đỉnh $v$ của phần thứ nhất, chúng ta gọi $\textrm{try_kuhn}(v)$ sau khi đã đặt lại mảng $\rm used$ về $\rm false$.

Kích thước của bộ ghép cực đại bằng số lần gọi $\textrm{try_kuhn}$ trong chương trình chính trả về kết quả $\rm true$. Bản thân bộ ghép cực đại tìm được được lưu trữ trong mảng $\rm mt$.

```cpp
int n, k;
vector<vector<int>> g;
vector<int> mt;
vector<bool> used;

bool try_kuhn(int v) {
    if (used[v])
        return false;
    used[v] = true;
    for (int to : g[v]) {
        if (mt[to] == -1 || try_kuhn(mt[to])) {
            mt[to] = v;
            return true;
        }
    }
    return false;
}

int main() {
    //... reading the graph ...

    mt.assign(k, -1);
    for (int v = 0; v < n; ++v) {
        used.assign(n, false);
        try_kuhn(v);
    }

    for (int i = 0; i < k; ++i)
        if (mt[i] != -1)
            printf("%d %d\n", mt[i] + 1, i + 1);
}
```
    
Chúng ta nhắc lại một lần nữa rằng thuật toán Kuhn có thể dễ dàng cài đặt trên đồ thị hai phía mà không cần biết trước sự phân chia tường minh của hai phần đỉnh. Trong trường hợp này, chúng ta không chia hai phần đỉnh một cách tường minh mà lưu trữ thông tin chung cho tất cả các đỉnh của đồ thị (các đỉnh của cả hai phần được đánh số chung từ $1$ đến $n$). Các mảng $\rm mt$ và $\rm used$ hiện cũng được định nghĩa cho tất cả các đỉnh của đồ thị và được duy trì tương ứng.

### Cài đặt cải tiến

Chúng ta sửa đổi thuật toán như sau. Trước vòng lặp chính của thuật toán, chúng ta sẽ tìm một **bộ ghép bất kỳ** bằng một thuật toán đơn giản (một **thuật toán heuristic** đơn giản), rồi sau đó mới thực hiện vòng lặp gọi hàm $\textrm{try_kuhn}()$, hàm này sẽ cải thiện bộ ghép đã tìm được. Nhờ đó, thuật toán sẽ chạy nhanh hơn đáng kể trên các đồ thị ngẫu nhiên - vì trên hầu hết các đồ thị, bạn có thể dễ dàng tìm thấy một bộ ghép có kích thước tương đối lớn bằng heuristic, và sau đó tối ưu nó thành bộ ghép cực đại bằng thuật toán Kuhn thông thường. Bằng cách này, chúng ta tiết kiệm được việc khởi chạy duyệt theo chiều sâu từ các đỉnh đã được ghép sẵn bởi heuristic.

Ví dụ, bạn có thể chỉ cần duyệt qua tất cả các đỉnh của phần thứ nhất, và với mỗi đỉnh, tìm một cạnh bất kỳ có thể thêm trực tiếp vào bộ ghép và thêm nó vào. Chỉ với heuristic đơn giản này, thuật toán Kuhn đã có thể chạy nhanh hơn vài lần.

Lưu ý rằng vòng lặp chính sẽ cần sửa đổi một chút. Vì khi gọi hàm $\textrm{try_kuhn}$ trong vòng lặp chính, chúng ta giả định đỉnh hiện tại chưa được ghép, nên cần thêm một bước kiểm tra điều kiện này.

Trong cài đặt, chỉ có mã nguồn trong hàm $\textrm{main}()$ thay đổi:

```cpp
int main() {
    // ... reading the graph ...

    mt.assign(k, -1);
    vector<bool> used1(n, false);
    for (int v = 0; v < n; ++v) {
        for (int to : g[v]) {
            if (mt[to] == -1) {
                mt[to] = v;
                used1[v] = true;
                break;
            }
        }
    }
    for (int v = 0; v < n; ++v) {
        if (used1[v])
            continue;
        used.assign(n, false);
        try_kuhn(v);
    }

    for (int i = 0; i < k; ++i)
        if (mt[i] != -1)
            printf("%d %d\n", mt[i] + 1, i + 1);
}
```

**Một heuristic tốt khác** như sau: Tại mỗi bước, thuật toán sẽ tìm đỉnh có bậc nhỏ nhất (nhưng không cô lập), chọn một cạnh bất kỳ từ nó để thêm vào bộ ghép, sau đó xóa cả hai đỉnh này cùng tất cả các cạnh liên thuộc khỏi đồ thị. Cách tiếp cận tham lam này hoạt động rất tốt trên đồ thị ngẫu nhiên; trong nhiều trường hợp nó thậm chí xây dựng được luôn bộ ghép cực đại (mặc dù vẫn có những trường hợp phản ví dụ mà thuật toán tham lam này chỉ tìm được bộ ghép nhỏ hơn nhiều so với cực đại).

## Ghi chú

* Thuật toán Kuhn là một thuật toán con trong **thuật toán Hungarian**, còn được gọi là **thuật toán Kuhn-Munkres**.
* Thuật toán Kuhn chạy trong thời gian $O(nm)$. Nó nói chung đơn giản để cài đặt, tuy nhiên, tồn tại các thuật toán hiệu quả hơn cho bài toán bộ ghép cực đại trên đồ thị hai phía - chẳng hạn như **thuật toán Hopcroft-Karp-Karzanov**, chạy trong thời gian $O(\sqrt{n}m)$.
* Bài toán [phủ đỉnh tối thiểu](https://en.wikipedia.org/wiki/Vertex_cover) là một bài toán NP-khó trên đồ thị tổng quát. Tuy nhiên, [Định lý Kőnig](https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)) chỉ ra rằng, đối với đồ thị hai phía, bản số của bộ ghép cực đại bằng bản số của phủ đỉnh tối thiểu. Do đó, chúng ta có thể sử dụng các thuật toán bộ ghép cực đại trên đồ thị hai phía để giải quyết bài toán phủ đỉnh tối thiểu trong thời gian đa thức trên đồ thị hai phía.

## Bài tập thực hành

* [Kattis - Gopher II](https://open.kattis.com/problems/gopher2)
* [Kattis - Borders](https://open.kattis.com/problems/borders)
