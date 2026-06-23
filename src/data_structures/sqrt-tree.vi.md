---
tags:
  - Translated
lang: vi
---

# Cây căn bậc hai (Sqrt Tree)

Cho một mảng $a$ gồm $n$ phần tử và một phép toán $\circ$ thỏa mãn tính chất kết hợp: $(x \circ y) \circ z = x \circ (y \circ z)$ với mọi $x$, $y$, $z$.

Các phép toán như $\gcd$, $\min$, $\max$, $+$, $\text{and}$, $\text{or}$, $\text{xor}$, v.v. đều thỏa mãn tính chất này.

Chúng ta cần trả lời các truy vấn $q(l, r)$. Với mỗi truy vấn, chúng ta cần tính giá trị của biểu thức $a_l \circ a_{l+1} \circ \dots \circ a_r$.

Cây căn bậc hai (Sqrt Tree) có thể xử lý các truy vấn như vậy trong thời gian $O(1)$ với thời gian tiền xử lý $O(n \cdot \log \log n)$ và bộ nhớ $O(n \cdot \log \log n)$.

## Mô tả

### Xây dựng phân rã căn bậc hai (sqrt decomposition)

Hãy xây dựng một cấu trúc [phân rã căn bậc hai (sqrt decomposition)](sqrt_decomposition.md). Chúng ta chia mảng thành $\sqrt{n}$ khối, mỗi khối có kích thước $\sqrt{n}$. Với mỗi khối, chúng ta tính toán:

1. Kết quả của các truy vấn nằm trong khối và bắt đầu ở đầu khối ($\text{prefixOp}$)
2. Kết quả của các truy vấn nằm trong khối và kết thúc ở cuối khối ($\text{suffixOp}$)

Và chúng ta sẽ tính thêm một mảng bổ sung:

3. $\text{between}_{i, j}$ (với $i \le j$) - kết quả của truy vấn bắt đầu từ đầu khối $i$ và kết thúc ở cuối khối $j$. Lưu ý rằng chúng ta có $\sqrt{n}$ khối, do đó kích thước của mảng này sẽ là $O(\sqrt{n}^2) = O(n)$.

Hãy xem một ví dụ cụ thể.

Giả sử phép toán $\circ$ là phép cộng $+$ (chúng ta cần tính tổng trên một đoạn) và chúng ta có mảng $a$ sau:

`{1, 2, 3, 4, 5, 6, 7, 8, 9}`

Mảng này sẽ được chia thành ba khối: `{1, 2, 3}`, `{4, 5, 6}` và `{7, 8, 9}`.

Đối với khối thứ nhất, $\text{prefixOp}$ là `{1, 3, 6}` và $\text{suffixOp}$ là `{6, 5, 3}`.

Đối với khối thứ hai, $\text{prefixOp}$ là `{4, 9, 15}` và $\text{suffixOp}$ là `{15, 11, 6}`.

Đối với khối thứ ba, $\text{prefixOp}$ là `{7, 15, 24}` và $\text{suffixOp}$ là `{24, 17, 9}`.

Mảng $\text{between}$ sẽ là:

~~~~~
{
    {6, 21, 45},
    {0, 15, 39},
    {0, 0,  24}
}
~~~~~

(chúng ta giả định rằng các phần tử không hợp lệ có $i > j$ được điền bằng số 0)

Rõ ràng là các mảng này có thể được tính toán dễ dàng trong thời gian $O(n)$ và bộ nhớ $O(n)$.

Sử dụng các mảng này, chúng ta đã có thể trả lời một số truy vấn. Nếu một truy vấn không nằm gọn trong một khối duy nhất, chúng ta có thể chia nó thành ba phần: phần hậu tố của một khối, tiếp theo là một đoạn gồm các khối liên tiếp và cuối cùng là phần tiền tố của một khối. Chúng ta có thể trả lời truy vấn bằng cách thực hiện phép toán trên ba giá trị lấy từ $\text{suffixOp}$, $\text{between}$ và $\text{prefixOp}$.

Tuy nhiên, nếu chúng ta có các truy vấn nằm hoàn toàn trong một khối đơn lẻ, chúng ta không thể xử lý chúng bằng ba mảng này. Do đó, chúng ta cần có giải pháp khác.

### Xây dựng cấu trúc cây

Chúng ta hiện chưa thể trả lời các truy vấn nằm gọn hoàn toàn trong một khối duy nhất. Nhưng **điều gì sẽ xảy ra nếu chúng ta xây dựng cấu trúc tương tự như trên cho từng khối nhỏ hơn?** Hoàn toàn có thể. Chúng ta thực hiện việc này một cách đệ quy cho đến khi kích thước của khối giảm xuống chỉ còn $1$ hoặc $2$. Kết quả cho các khối nhỏ này có thể tính dễ dàng trong $O(1)$.

Nhờ đó, chúng ta thu được một cấu trúc cây. Mỗi nút của cây đại diện cho một đoạn của mảng ban đầu. Nút đại diện cho một đoạn có kích thước $k$ sẽ có $\sqrt{k}$ con -- tương ứng với mỗi khối nhỏ. Ngoài ra, mỗi nút lưu trữ ba mảng mô tả ở trên cho đoạn mảng mà nó quản lý. Gốc của cây đại diện cho toàn bộ mảng. Các nút đại diện cho đoạn mảng có độ dài $1$ hoặc $2$ là các lá của cây.

Dễ thấy chiều cao của cây này là $O(\log \log n)$, bởi vì nếu một đỉnh của cây đại diện cho đoạn mảng có độ dài $k$, thì các con của nó sẽ đại diện cho đoạn mảng có độ dài $\sqrt{k}$. Vì $\log(\sqrt{k}) = \frac{\log{k}}{2}$, nên giá trị $\log k$ sẽ giảm đi một nửa sau mỗi tầng của cây, do đó chiều cao của cây là $O(\log \log n)$. Thời gian xây dựng và bộ nhớ sử dụng sẽ là $O(n \cdot \log \log n)$, vì mỗi phần tử của mảng xuất hiện đúng một lần trên mỗi tầng của cây.

Bây giờ chúng ta có thể trả lời các truy vấn trong thời gian $O(\log \log n)$. Chúng ta đi xuống cây cho đến khi gặp một đoạn có độ dài $1$ hoặc $2$ (kết quả có thể tính trong $O(1)$) hoặc gặp nút đầu tiên mà truy vấn không nằm gọn hoàn toàn trong một khối con duy nhất. Xem lại phần đầu tiên để biết cách trả lời truy vấn trong trường hợp này.

Như vậy, chúng ta đã đạt được độ phức tạp $O(\log \log n)$ cho mỗi truy vấn. Liệu có thể thực hiện nhanh hơn nữa không?

### Tối ưu hóa độ phức tạp của truy vấn

Một trong những tối ưu hóa rõ ràng nhất là sử dụng tìm kiếm nhị phân trên các nút cây cần tìm. Với tìm kiếm nhị phân, chúng ta có thể đạt độ phức tạp $O(\log \log \log n)$ cho mỗi truy vấn. Có thể tối ưu hơn nữa không?

Câu trả lời là có. Hãy giả định hai điều sau:

1. Kích thước của mỗi khối là một lũy thừa của hai.
2. Tất cả các khối trên cùng một tầng của cây có kích thước bằng nhau.

Để đạt được điều này, chúng ta có thể chèn thêm các phần tử trung hòa (ví dụ: số 0 đối với phép cộng) vào mảng sao cho kích thước của mảng trở thành một lũy thừa của hai.

Khi áp dụng giả định này, kích thước của một số khối có thể tăng lên tối đa gấp đôi để trở thành lũy thừa của hai, nhưng nó vẫn có kích thước dạng $O(\sqrt{k})$ và chúng ta vẫn giữ được độ phức tạp tuyến tính khi xây dựng các mảng trên một đoạn.

Bây giờ, chúng ta có thể dễ dàng kiểm tra xem một truy vấn có nằm hoàn toàn trong một khối kích thước $2^k$ hay không. Hãy biểu diễn các biên của truy vấn $l$ và $r$ (sử dụng chỉ số bắt đầu từ 0) dưới dạng số nhị phân. Ví dụ, giả sử $k=4, l=39, r=46$. Dạng nhị phân của $l$ và $r$ là:

$l = 39_{10} = 100111_2$

$r = 46_{10} = 101110_2$

Hãy nhớ rằng mỗi tầng chứa các đoạn có kích thước bằng nhau, và các khối trên cùng một tầng cũng có kích thước bằng nhau (trong trường hợp của chúng ta, kích thước là $2^k = 2^4 = 16$). Các khối phủ toàn bộ mảng, nên khối đầu tiên phủ các phần tử $(0 - 15)$ (nhị phân từ $000000_2$ đến $001111_2$), khối thứ hai phủ các phần tử $(16 - 31)$ (nhị phân từ $010000_2$ đến $011111_2$), v.v. Chúng ta thấy rằng chỉ số của các vị trí thuộc cùng một khối chỉ khác nhau ở $k$ bit cuối cùng (ở đây là $4$ bit cuối). Trong ví dụ này, $l$ và $r$ có các bit giống nhau ngoại trừ 4 bit cuối, do đó chúng nằm trong cùng một khối.

Vì vậy, chúng ta chỉ cần kiểm tra xem các bit khác nhau giữa chúng có vượt quá $k$ bit cuối cùng hay không (tức là giá trị $l\ \text{xor}\ r$ không vượt quá $2^k-1$).

Nhờ quan sát này, chúng ta có thể nhanh chóng tìm ra tầng phù hợp để trả lời truy vấn. Cách thực hiện như sau:

1. Với mỗi chỉ số $i$ không vượt quá kích thước mảng, chúng ta tìm bit cao nhất có giá trị bằng $1$. Để làm điều này một cách nhanh chóng, chúng ta sử dụng quy hoạch động và một mảng được tính toán trước.

2. Bây giờ, với mỗi truy vấn $q(l, r)$, chúng ta tìm bit cao nhất của $l\ \text{xor}\ r$, và dựa vào thông tin này, ta dễ dàng chọn được tầng phù hợp để xử lý truy vấn. Chúng ta cũng có thể sử dụng một mảng được tính toán trước ở bước này.

Để biết thêm chi tiết, hãy xem đoạn mã cài đặt bên dưới.

Nhờ phương pháp này, chúng ta có thể trả lời các truy vấn trong thời gian $O(1)$ mỗi truy vấn. Thật tuyệt vời! :)

## Cập nhật phần tử

Chúng ta cũng có thể thực hiện cập nhật các phần tử trên Cây căn bậc hai. Cả hai thao tác cập nhật một phần tử và cập nhật trên một đoạn đều được hỗ trợ.

### Cập nhật một phần tử duy nhất

Xét truy vấn $\text{update}(x, val)$ thực hiện gán $a_x = val$. Chúng ta cần thực hiện truy vấn này đủ nhanh.

#### Cách tiếp cận ngây thơ

Đầu tiên, hãy xem những gì thay đổi trên cây khi một phần tử duy nhất thay đổi. Xét một nút cây quản lý đoạn có độ dài $l$ và các mảng của nó: $\text{prefixOp}$, $\text{suffixOp}$ và $\text{between}$. Dễ thấy chỉ có $O(\sqrt{l})$ phần tử trong các mảng $\text{prefixOp}$ và $\text{suffixOp}$ thay đổi (chỉ nằm trong khối chứa phần tử bị thay đổi). Có $O(l)$ phần tử bị thay đổi trong mảng $\text{between}$. Do đó, có tổng cộng $O(l)$ phần tử trong nút cây đó được cập nhật.

Chúng ta biết rằng bất kỳ phần tử $x$ nào cũng xuất hiện ở đúng một nút cây trên mỗi tầng. Nút gốc (tầng $0$) có độ dài $O(n)$, các nút ở tầng $1$ có độ dài $O(\sqrt{n})$, các nút ở tầng $2$ có độ dài $O(\sqrt{\sqrt{n}})$, v.v. Do đó, độ phức tạp thời gian cho mỗi lần cập nhật là $O(n + \sqrt{n} + \sqrt{\sqrt{n}} + \dots) = O(n)$.

Nhưng cách này quá chậm. Liệu có thể làm nhanh hơn không?

#### Một cây căn bậc hai bên trong một cây căn bậc hai

Nhận thấy rằng điểm nghẽn của thao tác cập nhật là việc dựng lại mảng $\text{between}$ của nút gốc. Để tối ưu hóa cây, hãy loại bỏ mảng này! Thay vì dùng mảng $\text{between}$, chúng ta lưu trữ một cây căn bậc hai khác cho nút gốc. Hãy gọi nó là $\text{index}$. Cấu trúc này đóng vai trò tương tự như $\text{between}$ &mdash; trả lời các truy vấn trên các đoạn gồm nhiều khối. Lưu ý rằng các nút cây còn lại không cần dùng $\text{index}$, chúng vẫn giữ các mảng $\text{between}$ bình thường.

Một cây căn bậc hai được gọi là _indexed_ (được đánh chỉ mục) nếu nút gốc của nó có chứa $\text{index}$. Một cây căn bậc hai có mảng $\text{between}$ ở nút gốc được gọi là _unindexed_ (không được đánh chỉ mục). Lưu ý rằng bản thân $\text{index}$ **là một cây _unindexed_**.

Như vậy, chúng ta có thuật toán cập nhật cho một cây _indexed_ như sau:

* Cập nhật $\text{prefixOp}$ và $\text{suffixOp}$ trong $O(\sqrt{n})$.

* Cập nhật $\text{index}$. Nó có kích thước $O(\sqrt{n})$ và chúng ta chỉ cần cập nhật một phần tử duy nhất trong đó (phần tử đại diện cho khối bị thay đổi). Do đó, độ phức tạp thời gian cho bước này là $O(\sqrt{n})$. Chúng ta có thể sử dụng thuật toán "chậm" đã mô tả ở đầu phần này để thực hiện việc này.

* Đi xuống nút con đại diện cho khối bị thay đổi và cập nhật nó trong $O(\sqrt{n})$ bằng thuật toán "chậm".

Lưu ý rằng độ phức tạp của truy vấn vẫn là $O(1)$: chúng ta chỉ cần sử dụng $\text{index}$ trong truy vấn tối đa một lần, và thao tác này tốn $O(1)$ thời gian.

Vì vậy, tổng độ phức tạp thời gian để cập nhật một phần tử duy nhất là $O(\sqrt{n})$. Thật tuyệt vời! :)

### Cập nhật trên một đoạn

Cây căn bậc hai cũng có thể thực hiện cập nhật giá trị hàng loạt trên một đoạn. Truy vấn $\text{massUpdate}(x, l, r)$ gán giá trị $a_i = x$ với mọi $l \le i \le r$.

Có hai cách tiếp cận để giải quyết bài toán này: cách thứ nhất thực hiện $\text{massUpdate}$ trong thời gian $O(\sqrt{n}\cdot \log \log n)$ và giữ độ phức tạp truy vấn là $O(1)$. Cách thứ hai thực hiện $\text{massUpdate}$ trong $O(\sqrt{n})$, nhưng độ phức tạp truy vấn tăng lên thành $O(\log \log n)$.

Chúng ta sẽ sử dụng kỹ thuật lan truyền lười (lazy propagation) tương tự như trong cây phân đoạn (segment tree): chúng ta đánh dấu một số nút là _lazy_ (lười), nghĩa là chúng ta chỉ cập nhật chúng xuống các nút con khi thực sự cần thiết. Tuy nhiên, có một điểm khác biệt so với cây phân đoạn: việc đẩy giá trị lười (push) ở cây căn bậc hai rất tốn kém nên không thể thực hiện trực tiếp trong lúc truy vấn. Ở tầng $0$, việc đẩy giá trị lười tốn $O(\sqrt{n})$ thời gian. Vì vậy, chúng ta không thực hiện thao tác đẩy giá trị bên trong truy vấn, mà chỉ kiểm tra xem nút hiện tại hoặc nút cha của nó có đang mang nhãn _lazy_ hay không, và tính toán kết quả truy vấn dựa trên thông tin đó.

#### Cách tiếp cận thứ nhất

Trong cách tiếp cận thứ nhất, chúng ta chỉ cho phép các nút ở tầng $1$ (có độ dài $O(\sqrt{n})$) mang nhãn _lazy_. Khi thực hiện đẩy một nút như vậy, nó sẽ cập nhật toàn bộ cây con của nó bao gồm cả chính nó trong thời gian $O(\sqrt{n}\cdot \log \log n)$. Quá trình $\text{massUpdate}$ được thực hiện như sau:

* Xét các nút ở tầng $1$ và các khối tương ứng của chúng.

* Đối với các khối bị phủ hoàn toàn bởi $\text{massUpdate}$: Đánh dấu chúng là _lazy_ trong thời gian $O(\sqrt{n})$.

* Đối với các khối bị phủ một phần: Lưu ý rằng có tối đa hai khối như vậy. Chúng ta dựng lại chúng trong thời gian $O(\sqrt{n}\cdot \log \log n)$. Nếu chúng đang mang nhãn _lazy_, hãy tính toán dựa trên nhãn đó.

* Cập nhật $\text{prefixOp}$ và $\text{suffixOp}$ cho các khối bị phủ một phần trong $O(\sqrt{n})$ (vì chỉ có tối đa hai khối như vậy).

* Dựng lại cấu trúc $\text{index}$ trong thời gian $O(\sqrt{n}\cdot \log \log n)$.

Nhờ đó, chúng ta có thể thực hiện $\text{massUpdate}$ nhanh chóng. Vậy kỹ thuật lan truyền lười ảnh hưởng như thế nào đến các truy vấn? Các truy vấn sẽ có một số thay đổi như sau:

* Nếu truy vấn nằm hoàn toàn trong một khối _lazy_, chúng ta tính kết quả và áp dụng nhãn _lazy_. Thao tác tốn $O(1)$.

* Nếu truy vấn gồm nhiều khối, trong đó có một số khối mang nhãn _lazy_, chúng ta chỉ cần xử lý nhãn _lazy_ ở khối ngoài cùng bên trái và ngoài cùng bên phải. Các khối ở giữa được tính toán thông qua cấu trúc $\text{index}$, vốn đã được cập nhật thông tin mới nhất của các khối _lazy_ (vì nó được dựng lại sau mỗi lần sửa đổi). Thao tác tốn $O(1)$.

Độ phức tạp của truy vấn vẫn giữ nguyên là $O(1)$.

#### Cách tiếp cận thứ hai

Trong cách tiếp cận này, mọi nút đều có thể mang nhãn _lazy_ (ngoại trừ nút gốc). Ngay cả các nút trong cây $\text{index}$ cũng có thể mang nhãn _lazy_. Vì thế, khi xử lý một truy vấn, chúng ta phải kiểm tra nhãn _lazy_ ở tất cả các nút cha của nó, dẫn đến độ phức tạp truy vấn là $O(\log \log n)$.

Tuy nhiên, thao tác $\text{massUpdate}$ sẽ chạy nhanh hơn. Thuật toán hoạt động như sau:

* Đối với các khối bị phủ hoàn toàn bởi $\text{massUpdate}$: Thêm nhãn _lazy_ cho chúng. Thao tác tốn $O(\sqrt{n})$.

* Cập nhật $\text{prefixOp}$ và $\text{suffixOp}$ cho các khối bị phủ một phần trong $O(\sqrt{n})$ (chỉ có tối đa hai khối như vậy).

* Cập nhật cây chỉ mục `index`. Thao tác tốn $O(\sqrt{n})$ (sử dụng cùng thuật toán $\text{massUpdate}$).

* Cập nhật mảng $\text{between}$ cho các cây con _unindexed_.

* Đi xuống các nút đại diện cho các khối bị phủ một phần và gọi đệ quy hàm $\text{massUpdate}$.

Lưu ý rằng khi thực hiện gọi đệ quy, chúng ta chỉ thực hiện cập nhật tiền tố hoặc hậu tố. Đối với cập nhật tiền tố và hậu tố, chúng ta chỉ có tối đa một nút con bị phủ một phần. Vì thế, chúng ta chỉ truy cập một nút ở tầng $1$, hai nút ở tầng $2$ và hai nút ở bất kỳ tầng sâu hơn nào. Do đó, độ phức tạp thời gian là $O(\sqrt{n} + \sqrt{\sqrt{n}} + \dots) = O(\sqrt{n})$. Cách tiếp cận này tương tự như thao tác cập nhật đoạn trên cây phân đoạn thông thường.

## Cài đặt

Dưới đây là mã nguồn cài đặt Cây căn bậc hai hỗ trợ các thao tác: xây dựng trong $O(n \cdot \log \log n)$, trả lời truy vấn trong $O(1)$ và cập nhật một phần tử trong $O(\sqrt{n})$.

~~~~~cpp
SqrtTreeItem op(const SqrtTreeItem &a, const SqrtTreeItem &b);

inline int log2Up(int n) {
	int res = 0;
	while ((1 << res) < n) {
		res++;
	}
	return res;
}

class SqrtTree {
private:
	int n, lg, indexSz;
	vector<SqrtTreeItem> v;
	vector<int> clz, layers, onLayer;
	vector< vector<SqrtTreeItem> > pref, suf, between;
	
	inline void buildBlock(int layer, int l, int r) {
		pref[layer][l] = v[l];
		for (int i = l+1; i < r; i++) {
			pref[layer][i] = op(pref[layer][i-1], v[i]);
		}
		suf[layer][r-1] = v[r-1];
		for (int i = r-2; i >= l; i--) {
			suf[layer][i] = op(v[i], suf[layer][i+1]);
		}
	}
	
	inline void buildBetween(int layer, int lBound, int rBound, int betweenOffs) {
		int bSzLog = (layers[layer]+1) >> 1;
		int bCntLog = layers[layer] >> 1;
		int bSz = 1 << bSzLog;
		int bCnt = (rBound - lBound + bSz - 1) >> bSzLog;
		for (int i = 0; i < bCnt; i++) {
			SqrtTreeItem ans;
			for (int j = i; j < bCnt; j++) {
				SqrtTreeItem add = suf[layer][lBound + (j << bSzLog)];
				ans = (i == j) ? add : op(ans, add);
				between[layer-1][betweenOffs + lBound + (i << bCntLog) + j] = ans;
			}
		}
	}
	
	inline void buildBetweenZero() {
		int bSzLog = (lg+1) >> 1;
		for (int i = 0; i < indexSz; i++) {
			v[n+i] = suf[0][i << bSzLog];
		}
		build(1, n, n + indexSz, (1 << lg) - n);
	}
	
	inline void updateBetweenZero(int bid) {
		int bSzLog = (lg+1) >> 1;
		v[n+bid] = suf[0][bid << bSzLog];
		update(1, n, n + indexSz, (1 << lg) - n, n+bid);
	}
	
	void build(int layer, int lBound, int rBound, int betweenOffs) {
		if (layer >= (int)layers.size()) {
			return;
		}
		int bSz = 1 << ((layers[layer]+1) >> 1);
		for (int l = lBound; l < rBound; l += bSz) {
			int r = min(l + bSz, rBound);
			buildBlock(layer, l, r);
			build(layer+1, l, r, betweenOffs);
		}
		if (layer == 0) {
			buildBetweenZero();
		} else {
			buildBetween(layer, lBound, rBound, betweenOffs);
		}
	}
	
	void update(int layer, int lBound, int rBound, int betweenOffs, int x) {
		if (layer >= (int)layers.size()) {
			return;
		}
		int bSzLog = (layers[layer]+1) >> 1;
		int bSz = 1 << bSzLog;
		int blockIdx = (x - lBound) >> bSzLog;
		int l = lBound + (blockIdx << bSzLog);
		int r = min(l + bSz, rBound);
		buildBlock(layer, l, r);
		if (layer == 0) {
			updateBetweenZero(blockIdx);
		} else {
			buildBetween(layer, lBound, rBound, betweenOffs);
		}
		update(layer+1, l, r, betweenOffs, x);
	}
	
	inline SqrtTreeItem query(int l, int r, int betweenOffs, int base) {
		if (l == r) {
			return v[l];
		}
		if (l + 1 == r) {
			return op(v[l], v[r]);
		}
		int layer = onLayer[clz[(l - base) ^ (r - base)]];
		int bSzLog = (layers[layer]+1) >> 1;
		int bCntLog = layers[layer] >> 1;
		int lBound = (((l - base) >> layers[layer]) << layers[layer]) + base;
		int lBlock = ((l - lBound) >> bSzLog) + 1;
		int rBlock = ((r - lBound) >> bSzLog) - 1;
		SqrtTreeItem ans = suf[layer][l];
		if (lBlock <= rBlock) {
			SqrtTreeItem add = (layer == 0) ? (
				query(n + lBlock, n + rBlock, (1 << lg) - n, n)
			) : (
				between[layer-1][betweenOffs + lBound + (lBlock << bCntLog) + rBlock]
			);
			ans = op(ans, add);
		}
		ans = op(ans, pref[layer][r]);
		return ans;
	}
public:
	inline SqrtTreeItem query(int l, int r) {
		return query(l, r, 0, 0);
	}
	
	inline void update(int x, const SqrtTreeItem &item) {
		v[x] = item;
		update(0, 0, n, 0, x);
	}
	
	SqrtTree(const vector<SqrtTreeItem>& a)
		: n((int)a.size()), lg(log2Up(n)), v(a), clz(1 << lg), onLayer(lg+1) {
		clz[0] = 0;
		for (int i = 1; i < (int)clz.size(); i++) {
			clz[i] = clz[i >> 1] + 1;
		}
		int tlg = lg;
		while (tlg > 1) {
			onLayer[tlg] = (int)layers.size();
			layers.push_back(tlg);
			tlg = (tlg+1) >> 1;
		}
		for (int i = lg-1; i >= 0; i--) {
			onLayer[i] = max(onLayer[i], onLayer[i+1]);
		}
		int betweenLayers = max(0, (int)layers.size() - 1);
		int bSzLog = (lg+1) >> 1;
		int bSz = 1 << bSzLog;
		indexSz = (n + bSz - 1) >> bSzLog;
		v.resize(n + indexSz);
		pref.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
		suf.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
		between.assign(betweenLayers, vector<SqrtTreeItem>((1 << lg) + bSz));
		build(0, 0, n, 0);
	}
};
~~~~~

## Bài tập áp dụng

[CodeChef - SEGPROD](https://www.codechef.com/NOV17/problems/SEGPROD)
