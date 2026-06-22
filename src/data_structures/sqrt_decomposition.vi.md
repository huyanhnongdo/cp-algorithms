---
tags:
  - Translated
e_maxx_link: sqrt_decomposition
lang: vi
---
# Chia căn (Sqrt Decomposition)

Chia căn (Sqrt Decomposition) là một phương pháp (hoặc một cấu trúc dữ liệu) cho phép bạn thực hiện một số thao tác phổ biến (tìm tổng các phần tử của mảng con, tìm phần tử nhỏ nhất/lớn nhất, v.v.) trong $O(\sqrt n)$ thao tác, nhanh hơn đáng kể so với $O(n)$ đối với thuật toán vét cạn.

Đầu tiên, chúng ta sẽ mô tả cấu trúc dữ liệu cho một trong những ứng dụng đơn giản nhất của ý tưởng này, sau đó chỉ ra cách tổng quát hóa nó để giải quyết một số bài toán khác, và cuối cùng xem xét một cách sử dụng hơi khác của ý tưởng này: chia các yêu cầu đầu vào thành các khối căn bậc hai.

## Cấu trúc dữ liệu dựa trên chia căn

Cho một mảng $a[0 \dots n-1]$, triển khai (Implementation) một cấu trúc dữ liệu cho phép tìm tổng các phần tử $a[l \dots r]$ với $l$ và $r$ tùy ý trong $O(\sqrt n)$ thao tác.

### Mô tả

Ý tưởng cơ bản của chia căn là tiền xử lý (Preprocessing). Chúng ta sẽ chia mảng $a$ thành các khối có độ dài xấp xỉ $\sqrt n$, và với mỗi khối $i$, chúng ta sẽ tính toán trước tổng các phần tử trong đó $b[i]$.

Chúng ta có thể giả định rằng cả kích thước của khối và số lượng khối đều bằng $\sqrt n$ được làm tròn lên:

$$ s = \lceil \sqrt n \rceil $$

Khi đó, mảng $a$ được chia thành các khối theo cách sau:

$$ \underbrace{a[0], a[1], \dots, a[s-1]}_{\text{b[0]}}, \underbrace{a[s], \dots, a[2s-1]}_{\text{b[1]}}, \dots, \underbrace{a[(s-1) \cdot s], \dots, a[n-1]}_{\text{b[s-1]}} $$

Khối cuối cùng có thể có ít phần tử hơn các khối khác (nếu $n$ không phải là bội số của $s$), điều này không quan trọng đối với thảo luận (vì nó có thể được xử lý dễ dàng).
Do đó, với mỗi khối $k$, chúng ta biết tổng các phần tử trên đó $b[k]$:

$$ b[k] = \sum\limits_{i=k\cdot s}^{\min {(n-1,(k+1)\cdot s - 1})} a[i] $$

Vậy là chúng ta đã tính toán các giá trị của $b[k]$ (điều này yêu cầu $O(n)$ thao tác). Chúng có thể giúp chúng ta trả lời mỗi truy vấn (Query) $[l, r]$ như thế nào?
Lưu ý rằng nếu khoảng (Interval) $[l, r]$ đủ dài, nó sẽ chứa một số khối nguyên vẹn, và đối với những khối đó, chúng ta có thể tìm tổng các phần tử trong chúng chỉ trong một thao tác. Kết quả là, khoảng $[l, r]$ sẽ chỉ chứa các phần của hai khối, và chúng ta sẽ phải tính tổng các phần tử trong các phần này một cách vét cạn.

Do đó, để tính tổng các phần tử trên khoảng $[l, r]$, chúng ta chỉ cần cộng tổng các phần tử của hai "đuôi":
$[l\dots (k + 1)\cdot s-1]$ và $[p\cdot s\dots r]$, và cộng tổng các giá trị $b[i]$ trong tất cả các khối từ $k + 1$ đến $p-1$:

$$ \sum\limits_{i=l}^r a[i] = \sum\limits_{i=l}^{(k+1) \cdot s-1} a[i] + \sum\limits_{i=k+1}^{p-1} b[i] + \sum\limits_{i=p\cdot s}^r a[i] $$

_Lưu ý: Khi $k = p$, tức là $l$ và $r$ thuộc cùng một khối, công thức không thể áp dụng, và tổng nên được tính toán một cách vét cạn._

Cách tiếp cận này cho phép chúng ta giảm đáng kể số lượng thao tác. Thật vậy, kích thước của mỗi "đuôi" không vượt quá độ dài khối $s$, và số lượng khối trong tổng không vượt quá $s$. Vì chúng ta đã chọn $s \approx \sqrt n$, tổng số thao tác cần thiết để tìm tổng các phần tử trên khoảng $[l, r]$ là $O(\sqrt n)$.

### Triển khai

Hãy bắt đầu với triển khai đơn giản nhất:

```cpp
// input data
int n;
vector<int> a (n);

// preprocessing
int len = (int) sqrt (n + .0) + 1; // size of the block and the number of blocks
vector<int> b (len);
for (int i=0; i<n; ++i)
    b[i / len] += a[i];

// answering the queries
for (;;) {
    int l, r;
  // read input data for the next query
    int sum = 0;
    for (int i=l; i<=r; )
        if (i % len == 0 && i + len - 1 <= r) {
            // if the whole block starting at i belongs to [l, r]
            sum += b[i / len];
            i += len;
        }
        else {
            sum += a[i];
            ++i;
        }
}
```

Triển khai này có quá nhiều phép chia (vốn chậm hơn nhiều so với các phép toán số học khác). Thay vào đó, chúng ta có thể tính toán các chỉ số (Index) của các khối $c_l$ và $c_r$ chứa các chỉ số $l$ và $r$, và lặp qua các khối $c_l+1 \dots c_r-1$ với việc xử lý riêng biệt các "đuôi" trong các khối $c_l$ và $c_r$. Cách tiếp cận này tương ứng với công thức cuối cùng trong mô tả, và biến trường hợp $c_l = c_r$ thành một trường hợp đặc biệt.

```cpp
int sum = 0;
int c_l = l / len,   c_r = r / len;
if (c_l == c_r)
    for (int i=l; i<=r; ++i)
        sum += a[i];
else {
    for (int i=l, end=(c_l+1)*len-1; i<=end; ++i)
        sum += a[i];
    for (int i=c_l+1; i<=c_r-1; ++i)
        sum += b[i];
    for (int i=c_r*len; i<=r; ++i)
        sum += a[i];
}
```

## Các bài toán khác

Cho đến nay, chúng ta đã thảo luận về bài toán tìm tổng các phần tử của một mảng con (Subarray) liên tục. Bài toán này có thể được mở rộng để cho phép **cập nhật (Update) các phần tử mảng riêng lẻ**. Nếu một phần tử $a[i]$ thay đổi, chỉ cần cập nhật giá trị của $b[k]$ cho khối mà phần tử này thuộc về ($k = i / s$) trong một thao tác:

$$ b[k] += a_{new}[i] - a_{old}[i] $$

Mặt khác, nhiệm vụ tìm tổng các phần tử có thể được thay thế bằng nhiệm vụ tìm phần tử nhỏ nhất/lớn nhất của một mảng con. Nếu bài toán này cũng phải xử lý việc cập nhật các phần tử riêng lẻ, việc cập nhật giá trị của $b[k]$ cũng có thể thực hiện được, nhưng nó sẽ yêu cầu lặp qua tất cả các giá trị của khối $k$ trong $O(s) = O(\sqrt{n})$ thao tác.

Chia căn có thể được áp dụng một cách tương tự cho toàn bộ một lớp các bài toán khác: tìm số lượng phần tử bằng 0, tìm phần tử khác 0 đầu tiên, đếm các phần tử thỏa mãn một tính chất (Property) nhất định, v.v.

Một lớp bài toán khác xuất hiện khi chúng ta cần **cập nhật các phần tử mảng trên các khoảng**: tăng các phần tử hiện có hoặc thay thế chúng bằng một giá trị cho trước.

Ví dụ, giả sử chúng ta có thể thực hiện hai loại thao tác trên một mảng (Array): thêm một giá trị $\delta$ cho tất cả các phần tử mảng trên khoảng $[l, r]$ hoặc truy vấn giá trị của phần tử $a[i]$. Hãy lưu trữ giá trị cần thêm vào tất cả các phần tử của khối $k$ trong $b[k]$ (ban đầu tất cả $b[k] = 0$). Trong mỗi thao tác "add", chúng ta cần thêm $\delta$ vào $b[k]$ cho tất cả các khối thuộc khoảng $[l, r]$ và thêm $\delta$ vào $a[i]$ cho tất cả các phần tử thuộc "đuôi" của khoảng. Câu trả lời cho truy vấn $i$ đơn giản là $a[i] + b[i/s]$. Bằng cách này, thao tác "add" có độ phức tạp thời gian (Time Complexity) $O(\sqrt{n})$, và trả lời một truy vấn có độ phức tạp thời gian $O(1)$.

Cuối cùng, hai lớp bài toán này có thể được kết hợp nếu nhiệm vụ yêu cầu thực hiện **cả** cập nhật phần tử trên một khoảng và truy vấn trên một khoảng. Cả hai thao tác có thể được thực hiện với độ phức tạp thời gian $O(\sqrt{n})$. Điều này sẽ yêu cầu hai mảng khối $b$ và $c$: một để theo dõi các cập nhật phần tử và một để theo dõi các câu trả lời cho truy vấn.

Có những bài toán khác có thể được giải quyết bằng cách sử dụng chia căn, ví dụ, một bài toán về việc duy trì một tập hợp các số cho phép thêm/xóa số, kiểm tra xem một số có thuộc tập hợp hay không và tìm số lớn thứ $k$. Để giải quyết nó, người ta phải lưu trữ các số theo thứ tự tăng dần, chia thành nhiều khối với $\sqrt{n}$ số trong mỗi khối. Mỗi khi một số được thêm/xóa, các khối phải được cân bằng lại bằng cách di chuyển các số giữa đầu và cuối của các khối liền kề.

## Thuật toán Mo

Một ý tưởng tương tự, dựa trên chia căn, có thể được sử dụng để trả lời các truy vấn đoạn (range queries) ($Q$) ngoại tuyến (Offline) trong $O((N+Q)\sqrt{N})$.
Điều này nghe có vẻ tệ hơn nhiều so với các phương pháp ở phần trước, vì đây là một độ phức tạp thời gian hơi kém hơn so với những gì chúng ta đã có trước đó và không thể cập nhật giá trị giữa hai truy vấn.
Nhưng trong nhiều tình huống, phương pháp này có những ưu điểm.
Trong quá trình chia căn thông thường, chúng ta phải tính toán trước các câu trả lời cho mỗi khối, và hợp nhất chúng trong khi trả lời các truy vấn.
Trong một số bài toán, bước hợp nhất này có thể khá phức tạp.
Ví dụ, khi mỗi truy vấn yêu cầu tìm **mode** của đoạn của nó (số xuất hiện nhiều nhất).
Để làm được điều này, mỗi khối sẽ phải lưu trữ số lượng mỗi số trong nó trong một loại cấu trúc dữ liệu (Data Structure) nào đó, và chúng ta không thể thực hiện bước hợp nhất đủ nhanh nữa.
**Thuật toán Mo** sử dụng một cách tiếp cận hoàn toàn khác, có thể trả lời nhanh các loại truy vấn này, bởi vì nó chỉ theo dõi một cấu trúc dữ liệu, và các thao tác duy nhất với nó đều dễ dàng và nhanh chóng.

Ý tưởng là trả lời các truy vấn theo một thứ tự đặc biệt dựa trên các chỉ số.
Chúng ta sẽ trả lời trước tất cả các truy vấn có chỉ số bên trái nằm trong khối 0, sau đó trả lời tất cả các truy vấn có chỉ số bên trái nằm trong khối 1, v.v.
Và chúng ta cũng sẽ phải trả lời các truy vấn của một khối theo một thứ tự đặc biệt, cụ thể là được sắp xếp theo chỉ số bên phải của các truy vấn.

Như đã nói, chúng ta sẽ sử dụng một cấu trúc dữ liệu duy nhất.
Cấu trúc dữ liệu này sẽ lưu trữ thông tin về đoạn.
Ban đầu, đoạn này sẽ trống.
Khi chúng ta muốn trả lời truy vấn tiếp theo (theo thứ tự đặc biệt), chúng ta chỉ cần mở rộng hoặc thu hẹp đoạn, bằng cách thêm/bớt các phần tử ở cả hai phía của đoạn hiện tại, cho đến khi chúng ta biến đổi nó thành đoạn truy vấn.
Bằng cách này, chúng ta chỉ cần thêm hoặc bớt một phần tử mỗi lần, đây sẽ là các thao tác khá dễ dàng trong cấu trúc dữ liệu của chúng ta.

Vì chúng ta thay đổi thứ tự trả lời các truy vấn, điều này chỉ có thể thực hiện được khi chúng ta được phép trả lời các truy vấn ở chế độ ngoại tuyến (Offline).

### Triển khai

Trong thuật toán Mo, chúng ta sử dụng hai hàm để thêm một chỉ số và để loại bỏ một chỉ số khỏi đoạn mà chúng ta đang duy trì.

```cpp
void remove(idx);  // TODO: remove value at idx from data structure
void add(idx);     // TODO: add value at idx from data structure
int get_answer();  // TODO: extract the current answer of the data structure

int block_size;

struct Query {
    int l, r, idx;
    bool operator<(Query other) const
    {
        return make_pair(l / block_size, r) <
               make_pair(other.l / block_size, other.r);
    }
};

vector<int> mo_s_algorithm(vector<Query> queries) {
    vector<int> answers(queries.size());
    sort(queries.begin(), queries.end());

    // TODO: initialize data structure

    int cur_l = 0;
    int cur_r = -1;
    // invariant: data structure will always reflect the range [cur_l, cur_r]
    for (Query q : queries) {
        while (cur_l > q.l) {
            cur_l--;
            add(cur_l);
        }
        while (cur_r < q.r) {
            cur_r++;
            add(cur_r);
        }
        while (cur_l < q.l) {
            remove(cur_l);
            cur_l++;
        }
        while (cur_r > q.r) {
            remove(cur_r);
            cur_r--;
        }
        answers[q.idx] = get_answer();
    }
    return answers;
}
```

Dựa trên bài toán, chúng ta có thể sử dụng một cấu trúc dữ liệu khác và sửa đổi các hàm `add`/`remove`/`get_answer` một cách phù hợp.
Ví dụ, nếu chúng ta được yêu cầu tìm các truy vấn tổng đoạn, thì chúng ta sử dụng một số nguyên đơn giản làm cấu trúc dữ liệu, ban đầu là $0$.
Hàm `add` sẽ đơn giản là cộng giá trị của vị trí và sau đó cập nhật biến kết quả.
Mặt khác, hàm `remove` sẽ trừ giá trị tại vị trí và sau đó cập nhật biến kết quả.
Và `get_answer` chỉ trả về số nguyên.

Để trả lời các truy vấn mode, chúng ta có thể sử dụng một cây tìm kiếm nhị phân (Binary Search Tree - BST) (ví dụ: `map<int, int>`) để lưu trữ tần suất xuất hiện của mỗi số trong đoạn hiện tại, và một cây tìm kiếm nhị phân thứ hai (ví dụ: `set<pair<int, int>>`) để lưu giữ số lượng các số (ví dụ: dưới dạng các cặp count-number) theo thứ tự.
Phương thức `add` loại bỏ số hiện tại khỏi BST thứ hai, tăng số đếm trong BST thứ nhất, và chèn lại số đó vào BST thứ hai.
`remove` cũng làm tương tự, nó chỉ giảm số đếm.
Và `get_answer` chỉ cần nhìn vào cây thứ hai và trả về giá trị tốt nhất trong $O(1)$.

### Độ phức tạp

Sắp xếp tất cả các truy vấn sẽ tốn $O(Q \log Q)$.

Còn các thao tác khác thì sao?
Hàm `add` và `remove` sẽ được gọi bao nhiêu lần?

Giả sử kích thước khối là $S$.

Nếu chúng ta chỉ xem xét tất cả các truy vấn có chỉ số bên trái nằm trong cùng một khối, thì các truy vấn được sắp xếp theo chỉ số bên phải.
Do đó, chúng ta sẽ gọi `add(cur_r)` và `remove(cur_r)` chỉ $O(N)$ lần cho tất cả các truy vấn này gộp lại.
Điều này cho $O(\frac{N}{S} N)$ lượt gọi cho tất cả các khối.

Giá trị của `cur_l` có thể thay đổi tối đa $O(S)$ giữa hai truy vấn.
Do đó, chúng ta có thêm $O(S Q)$ lượt gọi `add(cur_l)` và `remove(cur_l)`.

Với $S \approx \sqrt{N}$, điều này cho tổng cộng $O((N + Q) \sqrt{N})$ thao tác.
Do đó, độ phức tạp là $O((N+Q)F\sqrt{N})$ trong đó $O(F)$ là độ phức tạp của hàm `add` và `remove`.

### Mẹo để cải thiện thời gian chạy

* Kích thước khối chính xác là $\sqrt{N}$ không phải lúc nào cũng mang lại thời gian chạy tốt nhất. Ví dụ, nếu $\sqrt{N}=750$ thì có thể kích thước khối là $700$ hoặc $800$ sẽ chạy tốt hơn. Quan trọng hơn, đừng tính toán kích thước khối trong thời gian chạy – hãy đặt nó là `const`. Việc chia cho các hằng số được các trình biên dịch tối ưu hóa rất tốt.
* Trong các khối lẻ, sắp xếp chỉ số bên phải theo thứ tự tăng dần; và trong các khối chẵn, sắp xếp nó theo thứ tự giảm dần. Điều này sẽ giảm thiểu sự di chuyển của con trỏ bên phải, vì việc sắp xếp thông thường sẽ di chuyển con trỏ bên phải từ cuối về đầu ở đầu mỗi khối. Với phiên bản cải tiến này, việc đặt lại đó không còn cần thiết nữa.

```cpp
bool cmp(pair<int, int> p, pair<int, int> q) {
    if (p.first / BLOCK_SIZE != q.first / BLOCK_SIZE)
        return p < q;
    return (p.first / BLOCK_SIZE & 1) ? (p.second < q.second) : (p.second > q.second);
}
```

Bạn có thể đọc về cách sắp xếp nhanh hơn nữa [tại đây](https://codeforces.com/blog/entry/61203).

## Bài toán luyện tập

* [Codeforces - Những viên đá của Kuriyama Mirai](https://codeforces.com/problemset/problem/433/B)
* [Codeforces - Một bài toán khác về các cặp đẹp](https://codeforces.com/contest/2197/problem/D)
* [UVA - 12003 - Bộ biến đổi mảng](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3154)
* [UVA - 11990 Nghịch đảo động](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3141)
* [SPOJ - Give Away](http://www.spoj.com/problems/GIVEAWAY/)
* [Codeforces - Till I Collapse](http://codeforces.com/contest/786/problem/C)
* [Codeforces - Định mệnh](http://codeforces.com/contest/840/problem/D)
* [Codeforces - Các lỗ](http://codeforces.com/contest/13/problem/E)
* [Codeforces - XOR và Số yêu thích](https://codeforces.com/problemset/problem/617/E)
* [Codeforces - Mảng mạnh](http://codeforces.com/problemset/problem/86/D)
* [SPOJ - DQUERY](https://www.spoj.com/problems/DQUERY)
* [Codeforces - Bắn cung Robin Hood](https://codeforces.com/contest/2014/problem/H)