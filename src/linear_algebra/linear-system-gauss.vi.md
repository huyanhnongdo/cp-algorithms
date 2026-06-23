---
tags:
  - Translated
e_maxx_link: linear_systems_gauss
lang: vi
---
# Phương pháp Gauss giải hệ phương trình tuyến tính

Cho một hệ gồm $n$ phương trình đại số tuyến tính (SLAE) với $m$ ẩn số. Bạn được yêu cầu giải hệ phương trình này: xác định xem nó vô nghiệm, có nghiệm duy nhất hay vô số nghiệm. Trong trường hợp có ít nhất một nghiệm, hãy tìm một nghiệm bất kỳ.

Về mặt hình thức, bài toán được phát biểu như sau: giải hệ phương trình:

$$\begin{align}
a_{11} x_1 + a_{12} x_2 + &\dots + a_{1m} x_m = b_1 \\
a_{21} x_1 + a_{22} x_2 + &\dots + a_{2m} x_m = b_2\\
&\vdots \\
a_{n1} x_1 + a_{n2} x_2 + &\dots + a_{nm} x_m = b_n
\end{align}$$

trong đó các hệ số $a_{ij}$ (với $i$ chạy từ 1 đến $n$, $j$ chạy từ 1 đến $m$) và $b_i$ ($i$ chạy từ 1 đến $n$) đã biết, và các biến $x_i$ ($i$ chạy từ 1 đến $m$) là các ẩn số.

Bài toán này cũng có biểu diễn ma trận đơn giản:

$$Ax = b,$$

trong đó $A$ là ma trận kích thước $n \times m$ gồm các hệ số $a_{ij}$ và $b$ là vector cột kích thước $n$.

Cần lưu ý rằng phương pháp trình bày trong bài viết này cũng có thể được sử dụng để giải phương trình trong trường số học modular với một số nguyên $a_{ij}$ bất kỳ, tức là:

$$\begin{align}
a_{11} x_1 + a_{12} x_2 + &\dots + a_{1m} x_m \equiv b_1 \pmod p \\
a_{21} x_1 + a_{22} x_2 + &\dots + a_{2m} x_m \equiv b_2 \pmod p \\
&\vdots \\
a_{n1} x_1 + a_{n2} x_2 + &\dots + a_{nm} x_m \equiv b_n \pmod p
\end{align}$$

## Gauss

Nói một cách chính xác, phương pháp được mô tả dưới đây nên được gọi là "Gauss-Jordan", hay khử Gauss-Jordan, vì đây là một biến thể của phương pháp Gauss, được Jordan mô tả vào năm 1887.

## Tổng quan

Thuật toán thực hiện `khử tuần tự` các biến trong mỗi phương trình, cho đến khi mỗi phương trình chỉ còn lại một biến. Nếu $n = m$, bạn có thể coi đây là việc biến đổi ma trận $A$ thành ma trận đơn vị, và giải phương trình trong trường hợp hiển nhiên này, nơi nghiệm là duy nhất và bằng hệ số $b_i$.

Khử Gauss dựa trên hai phép biến đổi đơn giản:

* Có thể hoán đổi hai phương trình.
* Có thể thay thế bất kỳ phương trình nào bằng một tổ hợp tuyến tính của chính nó (với hệ số khác 0) và một vài phương trình khác (với các hệ số tùy ý).

Trong bước đầu tiên, thuật toán Gauss-Jordan chia phương trình đầu tiên cho $a_{11}$. Sau đó, thuật toán cộng phương trình đầu tiên vào các phương trình còn lại sao cho các hệ số ở cột đầu tiên đều trở thành 0. Để đạt được điều này, trên dòng $i$, ta phải cộng phương trình thứ nhất đã nhân với $- a_{i1}$. Lưu ý rằng, thao tác này cũng phải được thực hiện trên vector $b$. Theo một nghĩa nào đó, nó hoạt động như thể vector $b$ là cột thứ $m+1$ của ma trận $A$.

Kết quả là, sau bước đầu tiên, cột đầu tiên của ma trận $A$ sẽ bao gồm $1$ ở dòng đầu tiên và $0$ ở các dòng khác.

Tương tự, chúng ta thực hiện bước thứ hai của thuật toán, xét cột thứ hai của dòng thứ hai. Đầu tiên, dòng này được chia cho $a_{22}$, sau đó nó được trừ vào các dòng khác sao cho toàn bộ cột thứ hai trở thành $0$ (ngoại trừ dòng thứ hai).

Chúng ta tiếp tục quá trình này cho tất cả các cột của ma trận $A$. Nếu $n = m$, thì $A$ sẽ trở thành ma trận đơn vị.

## Tìm phần tử trục (pivoting element)

Cách tiếp cận được mô tả ở trên đã bỏ qua nhiều chi tiết. Tại bước thứ $i$, nếu $a_{ii}$ bằng 0, chúng ta không thể áp dụng trực tiếp phương pháp này. Thay vào đó, trước hết chúng ta phải `chọn một dòng làm trục`: tìm một dòng của ma trận mà tại đó cột thứ $i$ khác 0, sau đó hoán đổi hai dòng.

Lưu ý rằng, ở đây chúng ta hoán đổi các dòng chứ không phải các cột. Lý do là nếu bạn hoán đổi cột, khi tìm được nghiệm, bạn phải nhớ hoán đổi ngược lại về đúng vị trí. Do đó, hoán đổi dòng sẽ dễ thực hiện hơn nhiều.

Trong nhiều cài đặt, ngay cả khi $a_{ii} \neq 0$, người ta vẫn thường hoán đổi dòng thứ $i$ với một dòng trục nào đó, sử dụng các heuristic như chọn dòng trục có giá trị tuyệt đối lớn nhất của $a_{ji}$. Heuristic này được sử dụng để giảm phạm vi giá trị của ma trận trong các bước sau. Nếu không có nó, ngay cả với ma trận kích thước khoảng $20$, sai số sẽ quá lớn và có thể gây tràn số cho các kiểu dữ liệu dấu phẩy động trong C++.

## Các trường hợp suy biến

Trong trường hợp $m = n$ và hệ phương trình không suy biến (tức là có định thức khác 0 và có nghiệm duy nhất), thuật toán nêu trên sẽ biến đổi $A$ thành ma trận đơn vị.

Bây giờ chúng ta xét `trường hợp tổng quát`, nơi $n$ và $m$ không nhất thiết bằng nhau, và hệ có thể suy biến. Trong những trường hợp này, phần tử trục ở bước thứ $i$ có thể không tìm thấy. Điều này có nghĩa là ở cột thứ $i$, tính từ dòng hiện tại trở xuống, tất cả đều là 0. Trong trường hợp này, hoặc là không có giá trị nào thỏa mãn biến $x_i$ (nghĩa là hệ vô nghiệm), hoặc $x_i$ là một biến tự do và có thể nhận giá trị tùy ý. Khi cài đặt Gauss-Jordan, bạn nên tiếp tục xử lý cho các biến tiếp theo và bỏ qua cột thứ $i$ (điều này tương đương với việc xóa cột thứ $i$ của ma trận).

Vì vậy, một số biến trong quá trình có thể được xác định là biến tự do. Khi số lượng biến $m$ lớn hơn số lượng phương trình $n$, thì sẽ tìm thấy ít nhất $m - n$ biến tự do.

Nói chung, nếu bạn tìm thấy ít nhất một biến tự do, nó có thể nhận bất kỳ giá trị tùy ý nào, trong khi các biến còn lại (biến phụ thuộc) được biểu diễn thông qua nó. Điều này có nghĩa là khi làm việc trên trường số thực, hệ phương trình có thể có vô số nghiệm. Tuy nhiên, bạn nên nhớ rằng khi có các biến tự do, hệ phương trình vẫn có thể vô nghiệm. Điều này xảy ra khi các phương trình còn lại chưa được xử lý có ít nhất một hằng số khác 0. Bạn có thể kiểm tra điều này bằng cách gán 0 cho tất cả các biến tự do, tính toán các biến khác, sau đó thay vào hệ phương trình gốc để kiểm tra xem chúng có thỏa mãn hay không.

## Cài đặt

Dưới đây là một bản cài đặt của Gauss-Jordan. Việc chọn dòng trục được thực hiện bằng heuristic: chọn giá trị lớn nhất trong cột hiện tại.

Đầu vào của hàm `gauss` là ma trận hệ phương trình $a$. Cột cuối cùng của ma trận này là vector $b$.

Hàm trả về số lượng nghiệm của hệ phương trình $(0, 1,\textrm{or } \infty)$. Nếu tồn tại ít nhất một nghiệm, nghiệm đó sẽ được trả về trong vector $ans$.

```{.cpp file=gauss}
const double EPS = 1e-9;
const int INF = 2; // it doesn't actually have to be infinity or a big number

int gauss (vector < vector<double> > a, vector<double> & ans) {
	int n = (int) a.size();
	int m = (int) a[0].size() - 1;

	vector<int> where (m, -1);
	for (int col=0, row=0; col<m && row<n; ++col) {
		int sel = row;
		for (int i=row; i<n; ++i)
			if (abs (a[i][col]) > abs (a[sel][col]))
				sel = i;
		if (abs (a[sel][col]) < EPS)
			continue;
		for (int i=col; i<=m; ++i)
			swap (a[sel][i], a[row][i]);
		where[col] = row;

		for (int i=0; i<n; ++i)
			if (i != row) {
				double c = a[i][col] / a[row][col];
				for (int j=col; j<=m; ++j)
					a[i][j] -= a[row][j] * c;
			}
		++row;
	}

	ans.assign (m, 0);
	for (int i=0; i<m; ++i)
		if (where[i] != -1)
			ans[i] = a[where[i]][m] / a[where[i]][i];
	for (int i=0; i<n; ++i) {
		double sum = 0;
		for (int j=0; j<m; ++j)
			sum += ans[j] * a[i][j];
		if (abs (sum - a[i][m]) > EPS)
			return 0;
	}

	for (int i=0; i<m; ++i)
		if (where[i] == -1)
			return INF;
	return 1;
}
```

Ghi chú cài đặt:

* Hàm sử dụng hai con trỏ - cột hiện tại $col$ và dòng hiện tại $row$.
* Với mỗi biến $x_i$, giá trị $where(i)$ là dòng mà cột này khác 0. Vector này cần thiết vì một số biến có thể là biến tự do.
* Trong cài đặt này, dòng thứ $i$ hiện tại không được chia cho $a_{ii}$ như mô tả ở trên, vì vậy kết quả cuối cùng ma trận không phải là ma trận đơn vị (mặc dù thực tế việc chia dòng $i$ có thể giúp giảm sai số).
* Sau khi tìm được nghiệm, nó được đưa ngược lại vào ma trận để kiểm tra xem hệ có ít nhất một nghiệm hay không. Nếu nghiệm kiểm thử thỏa mãn, hàm trả về 1 hoặc $\inf$, tùy thuộc vào việc có tồn tại biến tự do hay không.

## Độ phức tạp

Bây giờ chúng ta ước tính độ phức tạp của thuật toán này. Thuật toán bao gồm $m$ giai đoạn, trong mỗi giai đoạn:

* Tìm kiếm và hoán đổi dòng trục. Việc này mất $O(n + m)$ nếu sử dụng heuristic nêu trên.
* Nếu tìm thấy phần tử trục trong cột hiện tại, chúng ta phải cộng phương trình này vào tất cả các phương trình khác, mất thời gian $O(nm)$.

Vì vậy, độ phức tạp cuối cùng của thuật toán là $O(\min (n, m) . nm)$.
Trong trường hợp $n = m$, độ phức tạp đơn giản là $O(n^3)$.

Lưu ý rằng khi hệ phương trình không nằm trên số thực mà là số học modulo hai, hệ có thể được giải nhanh hơn nhiều, điều này được mô tả dưới đây.

## Tăng tốc thuật toán

Cài đặt trước đó có thể được tăng tốc gấp đôi bằng cách chia thuật toán thành hai giai đoạn: tiến và lùi:

* Giai đoạn tiến: Tương tự như cài đặt trước, nhưng dòng hiện tại chỉ được cộng vào các dòng sau nó. Kết quả là ta thu được ma trận tam giác thay vì đường chéo.
* Giai đoạn lùi: Khi ma trận đã ở dạng tam giác, trước tiên ta tính giá trị của biến cuối cùng. Sau đó thay giá trị này vào để tìm giá trị của biến tiếp theo, và cứ tiếp tục như vậy...

Giai đoạn lùi chỉ mất $O(nm)$, nhanh hơn nhiều so với giai đoạn tiến. Trong giai đoạn tiến, chúng ta giảm số lượng phép toán đi một nửa, từ đó giảm thời gian chạy của chương trình.

## Giải hệ phương trình tuyến tính modulo

Để giải hệ phương trình tuyến tính trong một modulo nào đó, chúng ta vẫn có thể sử dụng thuật toán đã mô tả. Tuy nhiên, trong trường hợp modulo bằng 2, ta có thể thực hiện khử Gauss-Jordan hiệu quả hơn nhiều bằng cách sử dụng các thao tác bitwise và kiểu dữ liệu `bitset` của C++:

```cpp
int gauss (vector < bitset<N> > a, int n, int m, bitset<N> & ans) {
	vector<int> where (m, -1);
	for (int col=0, row=0; col<m && row<n; ++col) {
		for (int i=row; i<n; ++i)
			if (a[i][col]) {
				swap (a[i], a[row]);
				break;
			}
		if (! a[row][col])
			continue;
		where[col] = row;

		for (int i=0; i<n; ++i)
			if (i != row && a[i][col])
				a[i] ^= a[row];
		++row;
	}
        // The rest of implementation is the same as above
}
```

Vì sử dụng nén bit, cài đặt này không chỉ ngắn gọn hơn mà còn nhanh hơn 32 lần.

## Một lưu ý nhỏ về các heuristic chọn dòng trục

Không có quy tắc chung nào cho việc nên sử dụng heuristic nào.

Heuristic được sử dụng trong cài đặt trước hoạt động khá tốt trong thực tế. Nó cũng cho ra kết quả gần như tương đương với "full pivoting" (chọn trục toàn phần) - nơi dòng trục được tìm kiếm trong tất cả các phần tử của ma trận con (từ dòng hiện tại và cột hiện tại).

Tuy nhiên, bạn nên lưu ý rằng cả hai heuristic đều phụ thuộc vào việc các phương trình gốc đã được tỉ lệ hóa như thế nào. Ví dụ, nếu một trong các phương trình được nhân với $10^6$, thì phương trình đó gần như chắc chắn sẽ được chọn làm trục trong bước đầu tiên. Điều này có vẻ khá kỳ lạ, vì vậy việc chuyển sang một heuristic phức tạp hơn gọi là `implicit pivoting` (chọn trục ngầm) có vẻ logic hơn.

Implicit pivoting so sánh các phần tử như thể cả hai dòng đã được chuẩn hóa để phần tử lớn nhất bằng đơn vị. Để thực hiện kỹ thuật này, cần duy trì giá trị lớn nhất trong mỗi dòng (hoặc giữ mỗi dòng sao cho giá trị lớn nhất là đơn vị, nhưng điều này có thể dẫn đến sự gia tăng sai số tích lũy).

## Cải thiện nghiệm

Bất chấp các heuristic khác nhau, thuật toán Gauss-Jordan vẫn có thể dẫn đến sai số lớn trong các ma trận đặc biệt ngay cả với kích thước $50 - 100$.

Do đó, nghiệm thu được từ Gauss-Jordan đôi khi phải được cải thiện bằng cách áp dụng một phương pháp số đơn giản - ví dụ, phương pháp lặp đơn giản.

Như vậy, quá trình tìm nghiệm gồm hai bước: Đầu tiên, thuật toán Gauss-Jordan được áp dụng, sau đó sử dụng một phương pháp số với nghiệm ban đầu là kết quả từ bước một.

## Các bài tập thực hành
* [Spoj - Xor Maximization](http://www.spoj.com/problems/XMAX/)
* [Codechef - Knight Moving](https://www.codechef.com/SEP12/problems/KNGHTMOV)
* [Lightoj - Graph Coloring](http://lightoj.com/volume_showproblem.php?problem=1279)
* [UVA 12910 - Snakes and Ladders](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4775)
* [TIMUS1042 Central Heating](http://acm.timus.ru/problem.php?space=1&num=1042)
* [TIMUS1766 Humpty Dumpty](http://acm.timus.ru/problem.php?space=1&num=1766)
* [TIMUS1266 Kirchhoff's Law](http://acm.timus.ru/problem.php?space=1&num=1266)
* [Codeforces - No game no life](https://codeforces.com/problemset/problem/1411/G)