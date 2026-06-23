---
tags:
  - Translated
e_maxx_link: aho_corasick
lang: vi
---
# Thuật toán Aho-Corasick

Thuật toán Aho-Corasick cho phép chúng ta tìm kiếm nhanh nhiều mẫu (pattern) trong một văn bản. Tập hợp các xâu mẫu còn được gọi là một _từ điển_ (dictionary).
Chúng ta ký hiệu tổng độ dài của các xâu này là $m$ và kích thước của bảng chữ cái là $k$.
Thuật toán xây dựng một máy trạng thái hữu hạn dựa trên một Trie trong thời gian $O(m k)$, sau đó sử dụng nó để xử lý văn bản.

Thuật toán này được đề xuất bởi Alfred Aho và Margaret Corasick vào năm 1975.

## Xây dựng Trie

<center>
![](https://upload.wikimedia.org/wikipedia/commons/e/e2/Trie.svg)
<br>
<i>Một Trie dựa trên các từ "Java", "Rad", "Rand", "Rau", "Raum" và "Rose".</i>
<br>
<i>Hình ảnh của <a href="https://commons.wikimedia.org/wiki/File:Trie.svg">[nd](https://de.wikipedia.org/wiki/Benutzer:Nd)</a> được phân phối theo giấy phép <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA 3.0</a>.</i>
</center>

Về mặt hình thức, Trie là một cây có gốc (rooted tree), trong đó mỗi cạnh của cây được gán nhãn với một chữ cái và các cạnh đi ra từ một đỉnh có nhãn khác nhau.

Chúng ta sẽ xác định mỗi đỉnh trong Trie tương ứng với xâu được tạo bởi các nhãn trên đường đi từ gốc đến đỉnh đó.

Mỗi đỉnh cũng sẽ có một cờ $\text{output}$ được bật nếu đỉnh đó tương ứng với một mẫu trong từ điển.

Theo đó, Trie cho một tập hợp các xâu là một Trie sao cho mỗi đỉnh $\text{output}$ tương ứng với một xâu từ tập hợp, và ngược lại, mỗi xâu của tập hợp tương ứng với một đỉnh $\text{output}$.

Bây giờ chúng ta mô tả cách xây dựng Trie cho một tập hợp các xâu cho trước trong thời gian tuyến tính so với tổng độ dài của chúng.

Chúng ta định nghĩa một cấu trúc cho các đỉnh của cây:
```{.cpp file=aho_corasick_trie_definition}
const int K = 26;

struct Vertex {
    int next[K];
    bool output = false;

    Vertex() {
        fill(begin(next), end(next), -1);
    }
};

vector<Vertex> trie(1);
```

Ở đây, chúng ta lưu trữ Trie dưới dạng một mảng các $\text{Vertex}$.
Mỗi $\text{Vertex}$ chứa cờ $\text{output}$ và các cạnh dưới dạng mảng $\text{next}[]$, trong đó $\text{next}[i]$ là chỉ số của đỉnh mà chúng ta đạt tới bằng cách theo ký tự $i$, hoặc $-1$ nếu không có cạnh như vậy.
Ban đầu, Trie chỉ gồm một đỉnh - gốc - với chỉ số $0$.

Bây giờ chúng ta cài đặt hàm thêm một xâu $s$ vào Trie.
Việc cài đặt khá đơn giản:
chúng ta bắt đầu từ nút gốc, và chừng nào còn các cạnh tương ứng với các ký tự của $s$, chúng ta sẽ đi theo chúng.
Nếu không có cạnh nào cho một ký tự, chúng ta tạo một đỉnh mới và nối nó bằng một cạnh.
Cuối cùng, chúng ta đánh dấu đỉnh cuối cùng bằng cờ $\text{output}$.

```{.cpp file=aho_corasick_trie_add}
void add_string(string const& s) {
    int v = 0;
    for (char ch : s) {
        int c = ch - 'a';
        if (trie[v].next[c] == -1) {
            trie[v].next[c] = trie.size();
            trie.emplace_back();
        }
        v = trie[v].next[c];
    }
    trie[v].output = true;
}
```

Việc cài đặt này rõ ràng chạy trong thời gian tuyến tính,
và vì mỗi đỉnh lưu trữ $k$ liên kết, nó sẽ sử dụng $O(m k)$ bộ nhớ.

Có thể giảm mức tiêu thụ bộ nhớ xuống $O(m)$ bằng cách sử dụng một `map` thay vì một mảng trong mỗi đỉnh.
Tuy nhiên, điều này sẽ làm tăng độ phức tạp thời gian lên $O(m \log k)$.

## Xây dựng bộ tự động (Automaton)

Giả sử chúng ta đã xây dựng một Trie cho tập các xâu đã cho.
Bây giờ hãy nhìn nó từ một góc độ khác.
Nếu ta nhìn vào bất kỳ đỉnh nào,
xâu tương ứng với nó là tiền tố (prefix) của một hoặc nhiều xâu trong tập hợp, vì vậy mỗi đỉnh của Trie có thể được hiểu là một vị trí trong một hoặc nhiều xâu từ tập hợp.

Thực tế, các đỉnh Trie có thể được hiểu là các trạng thái trong một **máy tự động hữu hạn đơn định (DFA)**.
Từ bất kỳ trạng thái nào, chúng ta có thể chuyển tiếp - sử dụng một ký tự đầu vào - đến các trạng thái khác, tức là đến một vị trí khác trong tập các xâu.
Ví dụ, nếu chỉ có một xâu $abc$ trong từ điển, và chúng ta đang đứng ở đỉnh $ab$, thì khi dùng ký tự $c$, chúng ta có thể đến đỉnh $abc$.

Như vậy, chúng ta có thể hiểu các cạnh của Trie là các bước chuyển trong một máy tự động theo ký tự tương ứng.
Tuy nhiên, trong một máy tự động, chúng ta cần có các bước chuyển cho mỗi tổ hợp của một trạng thái và một ký tự.
Nếu chúng ta cố thực hiện một bước chuyển bằng một ký tự mà không có cạnh tương ứng trong Trie, chúng ta vẫn phải đi đến một trạng thái nào đó.

Cụ thể hơn, giả sử chúng ta đang ở trạng thái tương ứng với xâu $t$ và muốn chuyển đến một trạng thái khác bằng ký tự $c$.
Nếu có một cạnh được gán nhãn với ký tự này $c$, thì chúng ta chỉ cần đi theo cạnh đó và nhận được đỉnh tương ứng với $t + c$.
Nếu không có cạnh như vậy, vì chúng ta muốn duy trì bất biến là trạng thái hiện tại là khớp bộ phận dài nhất trong xâu đã xử lý, chúng ta phải tìm xâu dài nhất trong Trie là hậu tố thực sự của xâu $t$ và thử thực hiện bước chuyển từ đó.

Ví dụ, giả sử Trie được xây dựng bởi các xâu $ab$ và $bc$, và chúng ta hiện đang ở đỉnh tương ứng với $ab$, cũng là một đỉnh $\text{output}$.
Để chuyển tiếp với ký tự $c$, chúng ta buộc phải đi đến trạng thái tương ứng với xâu $b$, và từ đó theo cạnh có ký tự $c$.

<center>
![](https://upload.wikimedia.org/wikipedia/commons/9/90/A_diagram_of_the_Aho-Corasick_string_search_algorithm.svg)
<br>
<i>Một máy tự động Aho-Corasick dựa trên các từ "a", "ab", "bc", "bca", "c" và "caa".</i>
<br>
<i>Các mũi tên màu xanh là các liên kết hậu tố (suffix links), các mũi tên màu xanh lá là các liên kết kết thúc.</i>
</center>

Một **liên kết hậu tố (suffix link)** cho một đỉnh $p$ là một cạnh trỏ đến hậu tố thực sự dài nhất của xâu tương ứng với đỉnh $p$.
Trường hợp đặc biệt duy nhất là gốc của Trie, liên kết hậu tố của nó sẽ trỏ về chính nó.
Bây giờ chúng ta có thể diễn giải lại phát biểu về các bước chuyển trong máy tự động như sau:
trong khi không có bước chuyển từ đỉnh hiện tại của Trie bằng ký tự hiện tại (hoặc cho đến khi chúng ta đạt đến gốc), chúng ta sẽ đi theo liên kết hậu tố.

Như vậy, chúng ta đã giảm bài toán xây dựng máy tự động xuống bài toán tìm liên kết hậu tố cho tất cả các đỉnh của Trie.
Tuy nhiên, chúng ta sẽ xây dựng các liên kết hậu tố này bằng chính các bước chuyển đã được xây dựng trong máy tự động.

Các liên kết hậu tố của đỉnh gốc và tất cả các con trực tiếp của nó đều trỏ về đỉnh gốc.
Đối với bất kỳ đỉnh $v$ nào sâu hơn trong cây, chúng ta có thể tính liên kết hậu tố như sau:
nếu $p$ là cha của $v$ với $c$ là ký tự gán nhãn cạnh từ $p$ đến $v$,
hãy đi đến $p$,
sau đó theo liên kết hậu tố của nó và thực hiện bước chuyển với ký tự $c$ từ đó.

Như vậy, bài toán tìm các bước chuyển đã được giảm xuống bài toán tìm liên kết hậu tố, và bài toán tìm liên kết hậu tố đã được giảm xuống bài toán tìm liên kết hậu tố và một bước chuyển, ngoại trừ các đỉnh gần gốc.
Do đó, chúng ta có một sự phụ thuộc đệ quy mà chúng ta có thể giải quyết trong thời gian tuyến tính.

Hãy chuyển sang phần cài đặt.
Lưu ý rằng bây giờ chúng ta sẽ lưu trữ nút cha $p$ và ký tự $pch$ của cạnh từ $p$ đến $v$ cho mỗi đỉnh $v$.
Ngoài ra, tại mỗi đỉnh, chúng ta sẽ lưu trữ liên kết hậu tố $\text{link}$ (hoặc $-1$ nếu nó chưa được tính), và trong mảng $\text{go}[k]$ là các bước chuyển trong máy cho mỗi ký tự (cũng $-1$ nếu chưa được tính).

```{.cpp file=aho_corasick_automaton}
const int K = 26;

struct Vertex {
    int next[K];
    bool output = false;
    int p = -1;
    char pch;
    int link = -1;
    int go[K];

    Vertex(int p=-1, char ch='$') : p(p), pch(ch) {
        fill(begin(next), end(next), -1);
        fill(begin(go), end(go), -1);
    }
};

vector<Vertex> t(1);

void add_string(string const& s) {
    int v = 0;
    for (char ch : s) {
        int c = ch - 'a';
        if (t[v].next[c] == -1) {
            t[v].next[c] = t.size();
            t.emplace_back(v, ch);
        }
        v = t[v].next[c];
    }
    t[v].output = true;
}

int go(int v, char ch);

int get_link(int v) {
    if (t[v].link == -1) {
        if (v == 0 || t[v].p == 0)
            t[v].link = 0;
        else
            t[v].link = go(get_link(t[v].p), t[v].pch);
    }
    return t[v].link;
}

int go(int v, char ch) {
    int c = ch - 'a';
    if (t[v].go[c] == -1) {
        if (t[v].next[c] != -1)
            t[v].go[c] = t[v].next[c];
        else
            t[v].go[c] = v == 0 ? 0 : go(get_link(v), ch);
    }
    return t[v].go[c];
} 
```

Dễ dàng thấy rằng nhờ việc ghi nhớ (memoization) các liên kết hậu tố và các bước chuyển,
tổng thời gian để tìm tất cả các liên kết hậu tố và các bước chuyển sẽ là tuyến tính.

Để minh họa khái niệm, hãy tham khảo slide số 103 của [Stanford slides](http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/02/Slides02.pdf).

### Xây dựng dựa trên BFS

Thay vì tính toán các bước chuyển và liên kết hậu tố bằng các lời gọi đệ quy đến `go` và `get_link`, chúng ta có thể tính chúng theo hướng từ dưới lên (bottom-up) bắt đầu từ gốc.
(Thực tế, khi từ điển chỉ bao gồm một xâu, chúng ta nhận được thuật toán Knuth-Morris-Pratt quen thuộc.)

Cách tiếp cận này có một số ưu điểm so với cách trên vì thay vì tổng độ dài $m$, thời gian chạy của nó chỉ phụ thuộc vào số lượng đỉnh $n$ trong Trie. Hơn nữa, có thể điều chỉnh nó cho các bảng chữ cái lớn bằng cách sử dụng cấu trúc dữ liệu mảng bền vững (persistent array), qua đó biến thời gian xây dựng thành $O(n \log k)$ thay vì $O(mk)$, một sự cải thiện đáng kể nếu $m$ có thể lên tới $n^2$.

Chúng ta có thể suy luận bằng quy nạp dựa trên việc BFS từ gốc duyệt qua các đỉnh theo thứ tự độ dài tăng dần.
Chúng ta có thể giả định rằng khi ở một đỉnh $v$, liên kết hậu tố $u = link[v]$ của nó đã được tính toán thành công, và đối với tất cả các đỉnh có độ dài ngắn hơn, các bước chuyển từ chúng cũng đã được tính toán đầy đủ.

Giả sử tại thời điểm hiện tại chúng ta đang ở đỉnh $v$ và xét một ký tự $c$. Chúng ta có hai trường hợp:

1. $go[v][c] = -1$. Trong trường hợp này, chúng ta có thể gán $go[v][c] = go[u][c]$, giá trị này đã được biết nhờ giả thuyết quy nạp;
2. $go[v][c] = w \neq -1$. Trong trường hợp này, chúng ta có thể gán $link[w] = go[u][c]$.

Theo cách này, chúng ta mất $O(1)$ thời gian cho mỗi cặp đỉnh và ký tự, làm cho thời gian chạy là $O(nk)$. Chi phí chính ở đây là chúng ta sao chép rất nhiều bước chuyển từ $u$ trong trường hợp đầu tiên, trong khi các bước chuyển của trường hợp thứ hai tạo thành Trie và có tổng là $n$ qua tất cả các đỉnh. Để tránh việc sao chép $go[u][c]$, chúng ta có thể sử dụng cấu trúc dữ liệu mảng bền vững, bằng cách sử dụng nó, ban đầu chúng ta sao chép $go[u]$ vào $go[v]$ và sau đó chỉ cập nhật các giá trị cho các ký tự mà bước chuyển sẽ khác biệt. Điều này dẫn đến thuật toán $O(n \log k)$.

## Ứng dụng

### Tìm tất cả các xâu từ một tập cho trước trong văn bản

Chúng ta được cho một tập các xâu và một văn bản.
Chúng ta phải in tất cả các lần xuất hiện của tất cả các xâu từ tập đó trong văn bản đã cho trong $O(\text{len} + \text{ans})$, với $\text{len}$ là độ dài văn bản và $\text{ans}$ là kích thước của câu trả lời.

Chúng ta xây dựng một máy tự động cho tập các xâu này.
Bây giờ chúng ta sẽ xử lý văn bản từng chữ cái một bằng cách sử dụng máy tự động,
bắt đầu từ gốc của Trie.
Nếu tại bất kỳ thời điểm nào chúng ta đang ở trạng thái $v$, và chữ cái tiếp theo là $c$, thì chúng ta chuyển sang trạng thái tiếp theo với $\text{go}(v, c)$, qua đó làm tăng độ dài xâu khớp hiện tại thêm $1$ hoặc giảm nó bằng cách theo một liên kết hậu tố.

Làm thế nào để biết một trạng thái $v$ có khớp với bất kỳ xâu nào từ tập hợp không?
Đầu tiên, rõ ràng là nếu chúng ta đứng tại một đỉnh $\text{output}$, thì xâu tương ứng với đỉnh đó kết thúc tại vị trí này trong văn bản.
Tuy nhiên, đây không phải là trường hợp duy nhất có thể có để đạt được kết quả khớp:
nếu chúng ta có thể đi đến một hoặc nhiều đỉnh $\text{output}$ bằng cách di chuyển dọc theo các liên kết hậu tố, thì cũng sẽ có một kết quả khớp tương ứng với mỗi đỉnh $\text{output}$ tìm thấy.
Một ví dụ đơn giản minh họa tình huống này có thể được tạo bằng cách sử dụng tập các xâu $\{dabce, abc, bc\}$ và văn bản $dabc$.

Do đó, nếu chúng ta lưu trữ trong mỗi đỉnh $\text{output}$ chỉ số của xâu tương ứng với nó (hoặc danh sách các chỉ số nếu các xâu trùng lặp xuất hiện trong tập hợp), thì chúng ta có thể tìm thấy trong $O(n)$ thời gian các chỉ số của tất cả các xâu khớp với trạng thái hiện tại, bằng cách đơn giản là theo các liên kết hậu tố từ đỉnh hiện tại về gốc.
Đây không phải là giải pháp hiệu quả nhất vì nó dẫn đến độ phức tạp $O(n ~ \text{len})$.
Tuy nhiên, điều này có thể được tối ưu hóa bằng cách tính toán và lưu trữ đỉnh $\text{output}$ gần nhất có thể tiếp cận được bằng cách sử dụng liên kết hậu tố (đôi khi được gọi là **liên kết lối ra - exit link**).
Giá trị này chúng ta có thể tính toán một cách lười (lazy) trong thời gian tuyến tính.
Như vậy, với mỗi đỉnh, chúng ta có thể tiến tới trong $O(1)$ thời gian đến đỉnh được đánh dấu tiếp theo trong đường đi liên kết hậu tố, tức là đến kết quả khớp tiếp theo.
Do đó, cho mỗi kết quả khớp, chúng ta dành $O(1)$ thời gian, và đạt được độ phức tạp $O(\text{len} + \text{ans})$.

Nếu bạn chỉ muốn đếm số lần xuất hiện và không tìm các chỉ số, bạn có thể tính số lượng các đỉnh được đánh dấu trên đường đi liên kết hậu tố cho mỗi đỉnh $v$.
Điều này có thể được tính trong $O(n)$ thời gian tổng cộng.
Như vậy, chúng ta có thể tổng hợp tất cả các lần xuất hiện trong $O(\text{len})$.

### Tìm xâu nhỏ nhất theo thứ tự từ điển với độ dài cho trước không khớp với bất kỳ xâu cho trước nào

Một tập các xâu và một độ dài $L$ được cho trước.
Chúng ta phải tìm một xâu độ dài $L$ không chứa bất kỳ xâu nào trong tập, và là xâu nhỏ nhất theo thứ tự từ điển trong số các xâu như vậy.

Chúng ta có thể xây dựng máy tự động cho tập các xâu.
Nhớ rằng các đỉnh $\text{output}$ là các trạng thái mà chúng ta có sự khớp với một xâu từ tập hợp.
Vì trong bài toán này chúng ta phải tránh các kết quả khớp, chúng ta không được phép đi vào các trạng thái như vậy.
Mặt khác, chúng ta có thể đi vào tất cả các đỉnh khác.
Do đó, chúng ta loại bỏ tất cả các đỉnh "xấu" khỏi máy, và trong đồ thị còn lại của máy tự động, chúng ta tìm đường đi nhỏ nhất theo thứ tự từ điển có độ dài $L$.
Bài toán này có thể được giải trong $O(L)$, ví dụ bằng [tìm kiếm theo chiều sâu](../graph/depth-first-search.md).

### Tìm xâu ngắn nhất chứa tất cả các xâu cho trước

Ở đây chúng ta sử dụng cùng những ý tưởng đó.
Đối với mỗi đỉnh, chúng ta lưu trữ một mặt nạ (mask) biểu thị các xâu khớp tại trạng thái này.
Sau đó, bài toán có thể được diễn giải lại như sau:
ban đầu ở trạng thái $(v = \text{root},~ \text{mask} = 0)$, chúng ta muốn đạt đến trạng thái $(v,~ \text{mask} = 2^n - 1)$, trong đó $n$ là số lượng xâu trong tập hợp.
Khi chúng ta chuyển từ trạng thái này sang trạng thái khác bằng cách dùng một chữ cái, chúng ta cập nhật mặt nạ tương ứng.
Bằng cách chạy [tìm kiếm theo chiều rộng](../graph/breadth-first-search.md), chúng ta có thể tìm một đường đi đến trạng thái $(v,~ \text{mask} = 2^n - 1)$ với độ dài nhỏ nhất.

### Tìm xâu nhỏ nhất theo thứ tự từ điển có độ dài $L$ chứa $k$ xâu

Như trong bài toán trước, chúng ta tính cho mỗi đỉnh số lượng các kết quả khớp tương ứng với nó (tức là số lượng các đỉnh được đánh dấu có thể tiếp cận bằng cách sử dụng các liên kết hậu tố).
Chúng ta diễn giải lại bài toán: trạng thái hiện tại được xác định bởi một bộ ba số $(v,~ \text{len},~ \text{cnt})$, và chúng ta muốn đi từ trạng thái $(\text{root},~ 0,~ 0)$ đến trạng thái $(v,~ L,~ k)$, trong đó $v$ có thể là bất kỳ đỉnh nào.
Do đó, chúng ta có thể tìm một đường đi như vậy bằng cách sử dụng tìm kiếm theo chiều sâu (và nếu việc tìm kiếm duyệt các cạnh theo thứ tự tự nhiên của chúng, thì đường đi tìm được sẽ tự động là nhỏ nhất theo thứ tự từ điển).

## Các bài tập

- [UVA #11590 - Prefix Lookup](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2637)
- [UVA #11171 - SMS](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2112)
- [UVA #10679 - I Love Strings!!](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1620)
- [Codeforces - x-prime Substrings](https://codeforces.com/problemset/problem/1400/F)
- [Codeforces - Frequency of String](http://codeforces.com/problemset/problem/963/D)
- [CodeChef - TWOSTRS](https://www.codechef.com/MAY20A/problems/TWOSTRS)

## Tài liệu tham khảo
- [Stanford's CS166 - Aho-Corasick Automata](http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/02/Slides02.pdf) ([Bản tóm tắt](http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/02/Small02.pdf))