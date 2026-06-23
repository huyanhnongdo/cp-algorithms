---
tags:
  - Translated
e_maxx_link: treap
lang: vi
---

# Treap (Cây Descartes - Cartesian tree)

Treap là một cấu trúc dữ liệu kết hợp giữa cây tìm kiếm nhị phân (binary search tree) và heap nhị phân (binary heap) (từ đó có tên gọi: tree + heap $\Rightarrow$ Treap).

Cụ thể hơn, treap là một cấu trúc dữ liệu lưu trữ các cặp $(X, Y)$ trong một cây nhị phân sao cho nó là một cây tìm kiếm nhị phân theo khóa $X$ và là một heap nhị phân theo độ ưu tiên $Y$.
Nếu một nút của cây chứa cặp giá trị $(X_0, Y_0)$, tất cả các nút ở cây con bên trái đều có $X \le X_0$, tất cả các nút ở cây con bên phải đều có $X_0 \le X$, và tất cả các nút ở cả hai cây con bên trái và bên phải đều có $Y \le Y_0$ (đối với max-heap).

Treap cũng thường được gọi là "cây Descartes" (Cartesian tree), vì nó có thể dễ dàng được biểu diễn trên hệ tọa độ Descartes:

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Treap.svg" width="350px"/>
</center>

Treap được đề xuất bởi Raimund Seidel và Cecilia Aragon vào năm 1989.

## Ưu điểm của việc tổ chức dữ liệu này

Trong cách cài đặt này, các giá trị $X$ đóng vai trò là khóa (đồng thời là các giá trị được lưu trữ trong treap), và các giá trị $Y$ được gọi là **độ ưu tiên** (priorities). Nếu không có độ ưu tiên, treap sẽ chỉ là một cây tìm kiếm nhị phân thông thường theo khóa $X$, và một tập hợp các giá trị $X$ có thể tương ứng với rất nhiều cây khác nhau, một số cây trong đó có thể bị suy biến (ví dụ: ở dạng danh sách liên kết), dẫn đến các thao tác chạy cực kỳ chậm (độ phức tạp $O(N)$).

Đồng thời, các **độ ưu tiên** (khi chúng là duy nhất) cho phép xác định **duy nhất** cấu trúc cây sẽ được xây dựng (tất nhiên, cấu trúc này không phụ thuộc vào thứ tự thêm các phần tử), điều này có thể được chứng minh bằng định lý tương ứng. Rõ ràng, nếu chúng ta **chọn độ ưu tiên một cách ngẫu nhiên**, trung bình chúng ta sẽ thu được các cây không bị suy biến, điều này đảm bảo độ phức tạp $O(\log N)$ cho các thao tác cơ bản. Do đó, cấu trúc dữ liệu này còn có tên gọi khác là **cây tìm kiếm nhị phân ngẫu nhiên** (randomized binary search tree).

## Các thao tác

Treap cung cấp các thao tác sau:

- **Insert (X, Y)** trong $O(\log N)$.  
  Thêm một nút mới vào cây. Một biến thể phổ biến là chỉ truyền khóa $X$ và tự động tạo ngẫu nhiên độ ưu tiên $Y$ bên trong hàm.
- **Search (X)** trong $O(\log N)$.  
  Tìm kiếm một nút có khóa bằng $X$. Cách cài đặt giống hệt cây tìm kiếm nhị phân thông thường.
- **Erase (X)** trong $O(\log N)$.  
  Tìm kiếm nút có khóa bằng $X$ và xóa nó khỏi cây.
- **Build ($X_1$, ..., $X_N$)** trong $O(N)$.  
  Xây dựng cây từ một danh sách các giá trị. Việc này có thể thực hiện trong thời gian tuyến tính (giả sử danh sách $X_1, ..., X_N$ đã được sắp xếp).
- **Union ($T_1$, $T_2$)** trong $O(M \log (N/M))$.  
  Hợp nhất hai cây, giả sử tất cả các phần tử đều khác nhau. Chúng ta cũng có thể đạt được độ phức tạp tương đương ngay cả khi cần loại bỏ các phần tử trùng lặp khi hợp nhất.
- **Intersect ($T_1$, $T_2$)** trong $O(M \log (N/M))$.  
  Tìm giao của hai cây (tức là các phần tử chung của chúng). Chúng ta sẽ không đi sâu vào cài đặt của thao tác này ở đây.

Ngoài ra, vì treap là một cây tìm kiếm nhị phân, nó có thể thực hiện các thao tác khác như tìm phần tử lớn thứ $K$ hoặc tìm vị trí (chỉ số) của một phần tử.

## Mô tả cài đặt

Về mặt cài đặt, mỗi nút chứa khóa $X$, độ ưu tiên $Y$ và các con trỏ tới con bên trái ($L$) và con bên phải ($R$).

Chúng ta sẽ cài đặt tất cả các thao tác cần thiết chỉ bằng hai thao tác bổ trợ: Split (Chia đôi) và Merge (Hợp nhất).

### Split

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Treap_split.svg" width="450px"/>
</center>

Thao tác **Split ($T$, $X$)** chia cây $T$ thành 2 cây con $L$ và $R$ (là các giá trị trả về của hàm split) sao cho $L$ chứa tất cả các phần tử có khóa $X_L \le X$, và $R$ chứa tất cả các phần tử có khóa $X_R > X$. Thao tác này có độ phức tạp $O(\log N)$ và được cài đặt bằng đệ quy rất gọn gàng:

1. Nếu giá trị của nút gốc (R) $\le X$, thì cây con bên trái `L` chắc chắn sẽ chứa `R->L` và bản thân nút `R`. Tiếp theo, chúng ta gọi đệ quy hàm split trên con bên phải `R->R`, gọi kết quả trả về là `L'` và `R'`. Cuối cùng, `L` sẽ chứa thêm `L'`, còn `R` chính là `R'`.
2. Nếu giá trị của nút gốc (R) $> X$, thì cây con bên phải `R` chắc chắn sẽ chứa nút `R` và `R->R`. Chúng ta gọi đệ quy hàm split trên con bên trái `R->L`, gọi kết quả trả về là `L'` và `R'`. Cuối cùng, `L` chính là `L'`, còn `R` sẽ chứa thêm `R'`.

Như vậy, thuật toán split là:

1. Xác định nút gốc thuộc về cây con nào (trái hay phải).
2. Gọi đệ quy hàm split trên một trong hai con của nó.
3. Tạo kết quả cuối cùng bằng cách liên kết lại các kết quả của lời gọi đệ quy.

### Merge

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/Treap_merge.svg" width="500px"/>
</center>

Thao tác **Merge ($T_1$, $T_2$)** gộp hai cây con $T_1$ và $T_2$ và trả về cây mới. Thao tác này cũng có độ phức tạp $O(\log N)$. Nó hoạt động dưới giả định rằng $T_1$ và $T_2$ đã được sắp xếp thứ tự (mọi khóa $X$ trong $T_1$ đều nhỏ hơn các khóa trong $T_2$). Do đó, chúng ta cần gộp hai cây này mà không làm vi phạm thứ tự độ ưu tiên $Y$. Để làm điều này, chúng ta chọn nút gốc có độ ưu tiên $Y$ lớn hơn làm gốc của cây mới, sau đó gọi đệ quy hàm Merge cho cây còn lại và cây con tương ứng của nút gốc được chọn.

### Insert

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Treap_insert.svg" width="500px"/>
</center>

Cách cài đặt **Insert ($X$, $Y$)** bây giờ trở nên rất rõ ràng. Đầu tiên chúng ta đi xuống dọc theo cây (như đối với cây tìm kiếm nhị phân thông thường theo khóa X), dừng lại ở nút đầu tiên có giá trị độ ưu tiên nhỏ hơn $Y$. Đây chính là vị trí chúng ta sẽ chèn nút mới. Tiếp theo, chúng ta gọi **Split (T, X)** trên cây con bắt đầu từ nút vừa tìm được, và gán các cây con trả về $L$ và $R$ làm con bên trái và bên phải của nút mới.

Một cách khác là chèn bằng cách chia đôi treap ban đầu theo khóa $X$, sau đó thực hiện $2$ lần gộp (Merge) với nút mới (xem hình minh họa).

### Erase

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Treap_erase.svg" width="500px"/>
</center>

Cách cài đặt **Erase ($X$)** cũng tương tự. Đầu tiên chúng ta đi xuống trên cây (như cây tìm kiếm nhị phân thông thường theo khóa $X$) để tìm phần tử cần xóa. Khi tìm thấy nút đó, chúng ta gọi **Merge** gộp hai con của nó lại và đặt cây kết quả vào vị trí của nút bị xóa.

Hoặc chúng ta có thể tách riêng cây con chứa $X$ ra bằng $2$ thao tác split, sau đó gộp các treap còn lại (xem hình minh họa).

### Build

Chúng ta có thể cài đặt thao tác **Build** với độ phức tạp $O(N \log N)$ bằng cách thực hiện $N$ lần gọi hàm **Insert**.

### Union

Thao tác **Union ($T_1$, $T_2$)** có độ phức tạp lý thuyết là $O(M \log (N / M))$, nhưng trong thực tế nó chạy rất hiệu quả với hằng số ẩn nhỏ. Không mất tính tổng quát, giả sử $T_1 \rightarrow Y > T_2 \rightarrow Y$, nghĩa là gốc của $T_1$ sẽ làm gốc của cây kết quả. Để lấy kết quả, chúng ta cần gộp các cây $T_1 \rightarrow L$, $T_1 \rightarrow R$ và $T_2$ thành hai cây con của gốc $T_1$. Để làm điều này, chúng ta gọi Split ($T_2$, $T_1\rightarrow X$), chia $T_2$ thành hai phần L và R, sau đó kết hợp đệ quy chúng với các con của $T_1$: Union ($T_1 \rightarrow L$, $L$) và Union ($T_1 \rightarrow R$, $R$), qua đó thu được cây con trái và phải của kết quả.

## Cài đặt

```cpp
struct item {
	int key, prior;
	item *l, *r;
	item () { }
	item (int key) : key(key), prior(rand()), l(NULL), r(NULL) { }
	item (int key, int prior) : key(key), prior(prior), l(NULL), r(NULL) { }
};
typedef item* pitem;
```

Đây là định nghĩa cấu trúc nút (`item`). Lưu ý cấu trúc gồm hai con trỏ tới con trái/phải, một khóa kiểu số nguyên (cho BST) và một độ ưu tiên kiểu số nguyên (cho heap). Độ ưu tiên được gán ngẫu nhiên bằng bộ sinh số ngẫu nhiên.

```cpp
void split (pitem t, int key, pitem & l, pitem & r) {
	if (!t)
		l = r = NULL;
	else if (t->key <= key)
        split (t->r, key, t->r, r),  l = t;
	else
        split (t->l, key, l, t->l),  r = t;
}
```

Trong đó `t` là treap cần chia đôi, và `key` là giá trị khóa để chia. Hàm không sử dụng giá trị trả về (`return`) mà thay đổi trực tiếp hai con trỏ kết quả được truyền qua tham chiếu:

```cpp
pitem l = nullptr, r = nullptr;
split(t, 5, l, r);
if (l) cout << "Left subtree size: " << (l->size) << endl;
if (r) cout << "Right subtree size: " << (r->size) << endl;
```

Hàm `split` này có thể hơi khó hiểu vì nó sử dụng cả con trỏ (`pitem`) lẫn tham chiếu của con trỏ (`pitem &l`). Để mô tả bằng lời: lời gọi `split(t, k, l, r)` có nghĩa là "chia treap `t` theo giá trị `k` thành hai treap, lưu treap bên trái vào `l` và treap bên phải vào `r`". Hãy áp dụng định nghĩa này cho hai lời gọi đệ quy:

1. Khi giá trị của nút gốc $\le$ key, chúng ta gọi `split (t->r, key, t->r, r)`, nghĩa là: "chia treap `t->r` (cây con bên phải của `t`) theo khóa `key`, lưu cây con bên trái vào `t->r` và cây con bên phải vào `r`". Sau đó, chúng ta đặt `l = t`. Lúc này, kết quả `l` sẽ chứa `t->l`, nút gốc `t` và cây con trái của kết quả đệ quy trên `t->r`, tất cả đã được liên kết chính xác theo đúng thứ tự!
2. Khi giá trị của nút gốc lớn hơn key, chúng ta gọi `split (t->l, key, l, t->l)`, nghĩa là: "chia treap `t->l` (cây con bên trái của `t`) theo khóa `key`, lưu cây con bên trái vào `l` và cây con bên phải vào `t->l`". Sau đó, chúng ta đặt `r = t`. Lúc này, kết quả `r` sẽ chứa cây con phải của kết quả đệ quy trên `t->l`, nút gốc `t` và `t->r`, tất cả đã được liên kết chính xác theo đúng thứ tự!

Nếu vẫn gặp khó khăn trong việc hiểu cách cài đặt, bạn nên xem xét nó theo phương pháp _quy nạp_: tức là *không* cố gắng phân tách đệ quy nhiều lần. Hãy giả định split hoạt động đúng trên treap rỗng, sau đó thử chạy nó cho treap có một nút, rồi hai nút, v.v., mỗi lần sử dụng giả thiết quy nạp rằng split hoạt động đúng trên các cây con nhỏ hơn.

```cpp
void insert (pitem & t, pitem it) {
	if (!t)
		t = it;
	else if (it->prior > t->prior)
		split (t, it->key, it->l, it->r),  t = it;
	else
		insert (t->key <= it->key ? t->r : t->l, it);
}

void merge (pitem & t, pitem l, pitem r) {
	if (!l || !r)
		t = l ? l : r;
	else if (l->prior > r->prior)
		merge (l->r, l->r, r),  t = l;
	else
		merge (r->l, l, r->l),  t = r;
}

void erase (pitem & t, int key) {
	if (t->key == key) {
		pitem th = t;
		merge (t, t->l, t->r);
		delete th;
	}
	else
		erase (key < t->key ? t->l : t->r, key);
}

pitem unite (pitem l, pitem r) {
	if (!l || !r)  return l ? l : r;
	if (l->prior < r->prior)  swap (l, r);
	pitem lt, rt;
	split (r, l->key, lt, rt);
	l->l = unite (l->l, lt);
	l->r = unite (l->r, rt);
	return l;
}
```

## Duy trì kích thước của các cây con

Để mở rộng tính năng của treap, chúng ta thường cần lưu trữ số lượng nút trong cây con của mỗi nút - trường `int cnt` trong cấu trúc `item`. Ví dụ, nó có thể được sử dụng để tìm phần tử lớn thứ K trên cây trong $O(\log N)$, hoặc tìm vị trí của một phần tử trong danh sách đã sắp xếp với cùng độ phức tạp. Cách cài đặt các thao tác này giống hệt như trên cây tìm kiếm nhị phân thông thường.

Khi cây thay đổi (thêm hoặc xóa nút, v.v.), trường `cnt` của một số nút cần được cập nhật tương ứng. Chúng ta viết hai hàm: `cnt()` trả về giá trị `cnt` hiện tại của nút hoặc 0 nếu nút không tồn tại, và `upd_cnt()` cập nhật giá trị `cnt` cho nút này với giả định rằng giá trị `cnt` của các con L và R của nó đã được cập nhật chính xác. Rõ ràng chỉ cần thêm lời gọi `upd_cnt()` vào cuối các hàm `insert`, `erase`, `split` và `merge` để luôn giữ cho giá trị `cnt` được cập nhật mới nhất.

```cpp
int cnt (pitem t) {
	return t ? t->cnt : 0;
}

void upd_cnt (pitem t) {
	if (t)
		t->cnt = 1 + cnt(t->l) + cnt (t->r);
}
```

## Xây dựng Treap trong $O(N)$ ở chế độ ngoại tuyến (offline) {data-toc-label="Building a Treap in O(N) in offline mode"}

Cho một danh sách các khóa đã sắp xếp, chúng ta có thể dựng treap nhanh hơn so với việc chèn từng khóa một (vốn tốn $O(N \log N)$). Vì các khóa đã được sắp xếp, chúng ta có thể dễ dàng xây dựng một cây tìm kiếm nhị phân cân bằng trong thời gian tuyến tính. Các giá trị độ ưu tiên $Y$ được khởi tạo ngẫu nhiên và sau đó có thể được vun đống (heapify) độc lập với khóa $X$ để [dựng heap](https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap) trong $O(N)$.

```cpp
void heapify (pitem t) {
	if (!t) return;
	pitem max = t;
	if (t->l != NULL && t->l->prior > max->prior)
		max = t->l;
	if (t->r != NULL && t->r->prior > max->prior)
		max = t->r;
	if (max != t) {
		swap (t->prior, max->prior);
		heapify (max);
	}
}

pitem build (int * a, int n) {
	// Construct a treap on values {a[0], a[1], ..., a[n - 1]}
	if (n == 0) return NULL;
	int mid = n / 2;
	pitem t = new item (a[mid], rand ());
	t->l = build (a, mid);
	t->r = build (a + mid + 1, n - mid - 1);
	heapify (t);
	upd_cnt(t)
	return t;
}
```

Lưu ý: lời gọi `upd_cnt(t)` chỉ cần thiết nếu bạn cần thông tin về kích thước của các cây con.

Cách tiếp cận trên luôn tạo ra một cây cân bằng hoàn hảo, rất tốt cho mục đích thực tế, nhưng nó không giữ nguyên các độ ưu tiên được gán ban đầu cho mỗi nút. Do đó, cách tiếp cận này không thể áp dụng để giải quyết bài toán sau:

!!! example "[acmsguru - Cartesian Tree](https://codeforces.com/problemsets/acmsguru/problem/99999/155)"
    Cho một dãy các cặp $(x_i, y_i)$, hãy dựng cây Descartes trên các cặp đó. Biết rằng tất cả $x_i$ và tất cả $y_i$ đều đôi một phân biệt.

Lưu ý rằng trong bài toán này, các độ ưu tiên không phải là ngẫu nhiên, do đó việc chèn từng đỉnh một có thể dẫn đến độ phức tạp bình phương trong trường hợp xấu nhất.

Một giải pháp khả thi ở đây là tìm cho mỗi phần tử phần tử gần nhất bên trái và bên phải có độ ưu tiên nhỏ hơn phần tử hiện tại. Trong số hai phần tử này, phần tử có độ ưu tiên lớn hơn phải là cha của phần tử hiện tại.

Bài toán này có thể giải được bằng một cải tiến của [ngăn xếp cực tiểu (minimum stack)](./stack_queue_modification.md) trong thời gian tuyến tính:

```cpp
void connect(auto from, auto to) {
    vector<pitem> st;
    for(auto it: ranges::subrange(from, to)) {
        while(!st.empty() && st.back()->prior > it->prior) {
            st.pop_back();
        }
        if(!st.empty()) {
            if(!it->p || it->p->prior < st.back()->prior) {
                it->p = st.back();
            }
        }
        st.push_back(it);
    }
}

pitem build(int *x, int *y, int n) {
    vector<pitem> nodes(n);
    for(int i = 0; i < n; i++) {
        nodes[i] = new item(x[i], y[i]);
    }
    connect(nodes.begin(), nodes.end());
    connect(nodes.rbegin(), nodes.rend());
    for(int i = 0; i < n; i++) {
        if(nodes[i]->p) {
            if(nodes[i]->p->key < nodes[i]->key) {
                nodes[i]->p->r = nodes[i];
            } else {
                nodes[i]->p->l = nodes[i];
            }
        }
    }
    return nodes[min_element(y, y + n) - y];
}
```

## Treap ẩn (Implicit Treaps)

Treap ẩn (Implicit Treap) là một cải tiến đơn giản của treap thông thường nhưng là một cấu trúc dữ liệu cực kỳ mạnh mẽ. Thực chất, treap ẩn có thể được coi là một mảng hỗ trợ các thao tác sau (tất cả đều chạy trong thời gian $O(\log N)$ ở chế độ trực tuyến - online):

- Chèn một phần tử vào bất kỳ vị trí nào trong mảng
- Xóa một phần tử bất kỳ
- Tìm tổng, phần tử nhỏ nhất / lớn nhất, v.v. trên một đoạn bất kỳ
- Cộng thêm lượng giá trị, tô màu trên một đoạn bất kỳ
- Đảo ngược các phần tử trên một đoạn bất kỳ

Ý tưởng là các khóa sẽ là các **chỉ số** (bắt đầu từ 0) của các phần tử trong mảng. Tuy nhiên, chúng ta không lưu trữ trực tiếp các chỉ số này (nếu lưu trữ trực tiếp, thao tác chèn phần tử sẽ buộc chúng ta phải cập nhật khóa trên $O(N)$ nút của cây).

Lưu ý rằng khóa thực sự của một nút bằng số lượng nút nhỏ hơn nó (các nút này không chỉ nằm trong cây con bên trái của nó mà còn nằm trong cây con bên trái của các tổ tiên của nó).
Nói cách khác, **khóa ẩn** (implicit key) của một nút T bằng số lượng đỉnh $cnt(T \rightarrow L)$ ở cây con bên trái của nút đó cộng với tổng các giá trị tương ứng $cnt(P \rightarrow L) + 1$ của mọi tổ tiên P của nút T sao cho T nằm ở cây con bên phải của P.

Do đó, chúng ta có thể tính toán nhanh khóa ẩn của nút hiện tại khi đi xuống cây. Do trong tất cả các thao tác, chúng ta đều đi xuống từ gốc, chúng ta có thể cộng dồn giá trị này và truyền tiếp vào lời gọi hàm. Nếu đi xuống cây con bên trái, giá trị tích lũy không đổi; nếu đi xuống cây con bên phải, giá trị tích lũy tăng thêm $cnt(T \rightarrow L) + 1$.

Dưới đây là cài đặt mới của **Split** và **Merge**:

```cpp
void merge (pitem & t, pitem l, pitem r) {
	if (!l || !r)
		t = l ? l : r;
	else if (l->prior > r->prior)
		merge (l->r, l->r, r),  t = l;
	else
		merge (r->l, l, r->l),  t = r;
	upd_cnt (t);
}

void split (pitem t, pitem & l, pitem & r, int key, int add = 0) {
	if (!t)
		return void( l = r = 0 );
	int cur_key = add + cnt(t->l); //implicit key
	if (key <= cur_key)
		split (t->l, l, t->l, key, add),  r = t;
	else
		split (t->r, t->r, r, key, add + 1 + cnt(t->l)),  l = t;
	upd_cnt (t);
}
```

Trong cách cài đặt trên, sau lời gọi $split(T, T_1, T_2, k)$, cây $T_1$ sẽ chứa $k$ phần tử đầu tiên của $T$ (các phần tử có khóa ẩn nhỏ hơn $k$) và $T_2$ chứa các phần tử còn lại.

Bây giờ hãy xem xét cách cài đặt các thao tác khác nhau trên treap ẩn:

- **Insert element (Chèn phần tử)**.  
  Giả sử cần chèn một phần tử vào vị trí $pos$. Chúng ta chia treap thành hai phần tương ứng với các đoạn $[0..pos-1]$ và $[pos..sz]$; để làm việc này ta gọi $split(T, T_1, T_2, pos)$. Tiếp theo, gộp cây $T_1$ với nút mới bằng cách gọi $merge(T_1, T_1, \text{new item})$. Cuối cùng, gộp lại hai cây $T_1$ và $T_2$ về lại cây $T$ ban đầu qua lời gọi $merge(T, T_1, T_2)$.
- **Delete element (Xóa phần tử)**.  
  Thao tác này còn đơn giản hơn: tìm phần tử cần xóa $T$, thực hiện gộp (merge) hai con $L$ và $R$ của nó, rồi thay thế nút $T$ bằng kết quả gộp đó. Thao tác xóa trong treap ẩn giống hệt như trong treap thông thường.
- Tìm **sum / minimum (tổng / cực tiểu)**, v.v. trên đoạn.  
  Đầu tiên, thêm một trường bổ sung $F$ vào cấu trúc `item` để lưu trữ kết quả của hàm đích trên cây con của nút này. Trường này có thể dễ dàng duy trì tương tự như kích thước cây con: tạo một hàm tính toán giá trị này cho nút dựa trên các con của nó và gọi hàm này ở cuối tất cả các hàm thay đổi cây.  
  Thứ hai, chúng ta cần biết cách xử lý truy vấn trên một đoạn $[A; B]$ bất kỳ.  
  Để tách ra phần cây tương ứng với đoạn $[A; B]$, chúng ta gọi $split(T, T_2, T_3, B+1)$, sau đó gọi $split(T_2, T_1, T_2, A)$. Sau các bước này, $T_2$ sẽ chứa chính xác các phần tử thuộc đoạn $[A; B]$. Do đó, kết quả truy vấn chính là giá trị được lưu tại trường $F$ của nút gốc $T_2$. Sau khi có kết quả, chúng ta khôi phục lại cây bằng cách gọi $merge(T, T_1, T_2)$ và $merge(T, T, T_3)$.
- **Addition / painting (Cộng thêm / tô màu)** trên đoạn.  
  Thực hiện tương tự như phần trên, nhưng thay vì trường F, chúng ta lưu một trường `add` chứa giá trị cần cộng cho cả cây con (hoặc màu cần tô). Trước khi thực hiện bất kỳ thao tác nào, chúng ta phải "đẩy" (push) giá trị này xuống dưới - tức là cập nhật giá trị `add` của các con $T \rightarrow L$ và $T \rightarrow R$, rồi xóa nhãn `add` ở nút cha. Cách này đảm bảo thông tin không bị mất mát sau các thay đổi trên cây.
- **Reverse (Đảo ngược)** đoạn.  
  Tương tự như thao tác trên: chúng ta thêm một biến cờ `rev` kiểu boolean và đặt nó bằng true khi cần đảo ngược cây con của nút hiện tại. Việc đẩy giá trị lười này hơi phức tạp hơn một chút: chúng ta hoán đổi hai con trái/phải của nút hiện tại và bật cờ `rev` ở cả hai con đó.

Dưới đây là ví dụ cài đặt treap ẩn hỗ trợ đảo ngược đoạn. Mỗi nút lưu trường `value` là giá trị thực tế của phần tử mảng tại vị trí tương ứng. Chúng ta cũng cài đặt hàm `output()` để in ra mảng tương ứng với trạng thái hiện tại của treap ẩn.

```cpp
typedef struct item * pitem;
struct item {
	int prior, value, cnt;
	bool rev;
	pitem l, r;
};

int cnt (pitem it) {
	return it ? it->cnt : 0;
}

void upd_cnt (pitem it) {
	if (it)
		it->cnt = cnt(it->l) + cnt(it->r) + 1;
}

void push (pitem it) {
	if (it && it->rev) {
		it->rev = false;
		swap (it->l, it->r);
		if (it->l)  it->l->rev ^= true;
		if (it->r)  it->r->rev ^= true;
	}
}

void merge (pitem & t, pitem l, pitem r) {
	push (l);
	push (r);
	if (!l || !r)
		t = l ? l : r;
	else if (l->prior > r->prior)
		merge (l->r, l->r, r),  t = l;
	else
		merge (r->l, l, r->l),  t = r;
	upd_cnt (t);
}

void split (pitem t, pitem & l, pitem & r, int key, int add = 0) {
	if (!t)
		return void( l = r = 0 );
	push (t);
	int cur_key = add + cnt(t->l);
	if (key <= cur_key)
		split (t->l, l, t->l, key, add),  r = t;
	else
		split (t->r, t->r, r, key, add + 1 + cnt(t->l)),  l = t;
	upd_cnt (t);
}

void reverse (pitem t, int l, int r) {
	pitem t1, t2, t3;
	split (t, t1, t2, l);
	split (t2, t2, t3, r-l+1);
	t2->rev ^= true;
	merge (t, t1, t2);
	merge (t, t, t3);
}

void output (pitem t) {
	if (!t)  return;
	push (t);
	output (t->l);
	printf ("%d ", t->value);
	output (t->r);
}
```

## Tài liệu tham khảo

* [Blelloch, Reid-Miller "Fast Set Operations Using Treaps"](https://www.cs.cmu.edu/~scandal/papers/treaps-spaa98.pdf)

## Bài tập áp dụng

* [SPOJ - Ada and Aphids](http://www.spoj.com/problems/ADAAPHID/)
* [SPOJ - Ada and Harvest](http://www.spoj.com/problems/ADACROP/)
* [Codeforces - Radio Stations](http://codeforces.com/contest/762/problem/E)
* [SPOJ - Ghost Town](http://www.spoj.com/problems/COUNT1IT/)
* [SPOJ - Arrangement Validity](http://www.spoj.com/problems/IITWPC4D/)
* [SPOJ - All in One](http://www.spoj.com/problems/ALLIN1/)
* [Codeforces - Dog Show](http://codeforces.com/contest/847/problem/D)
* [Codeforces - Yet Another Array Queries Problem](http://codeforces.com/contest/863/problem/D)
* [SPOJ - Mean of Array](http://www.spoj.com/problems/MEANARR/)
* [SPOJ - TWIST](http://www.spoj.com/problems/TWIST/)
* [SPOJ - KOILINE](http://www.spoj.com/problems/KOILINE/)
* [CodeChef - The Prestige](https://www.codechef.com/problems/PRESTIGE)
* [Codeforces - T-Shirts](https://codeforces.com/contest/702/problem/F)
* [Codeforces - Wizards and Roads](https://codeforces.com/problemset/problem/167/D)
* [Codeforces - Yaroslav and Points](https://codeforces.com/contest/295/problem/E)
