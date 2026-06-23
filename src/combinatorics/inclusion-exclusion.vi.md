---
tags:
  - Translated
e_maxx_link: inclusion_exclusion_principle
lang: vi
---
# Nguyên lý Bù trừ (Inclusion-Exclusion Principle)

Nguyên lý bù trừ là một phương pháp tổ hợp quan trọng để tính kích thước của một tập hợp hoặc xác suất của các sự kiện phức tạp. Nó thiết lập mối quan hệ giữa kích thước của các tập hợp riêng lẻ với hợp của chúng.

## Phát biểu

### Công thức bằng lời

Nguyên lý bù trừ có thể được diễn đạt như sau:

Để tính kích thước của hợp nhiều tập hợp, cần tính tổng kích thước của các tập hợp này **riêng biệt**, sau đó trừ đi kích thước của tất cả các giao **từng đôi một**, rồi cộng lại kích thước của các giao của **bộ ba** tập hợp, trừ đi kích thước của các giao của **bộ bốn** tập hợp, và cứ tiếp tục như vậy cho đến giao của **tất cả** các tập hợp.

### Công thức theo tập hợp

Định nghĩa trên có thể được biểu diễn dưới dạng toán học như sau:

$$\left| \bigcup_{i=1}^n A_i \right| = \sum_{i=1}^n|A_i| - \sum_{1\leq i<j\leq n} |A_i \cap A_j| + \sum _{1\leq i<j<k\leq n}|A_i \cap A_j \cap A_k| - \cdots + (-1)^{n-1} | A_1 \cap \cdots \cap A_n |$$

Và viết gọn lại là:

$$\left|\bigcup_{i=1}^n A_i \right| = \sum_{\emptyset \neq J\subseteq \{1,2,\ldots ,n\}} (-1)^{|J|-1}{\Biggl |}\bigcap_{j\in J}A_{j}{\Biggr |}$$

### Công thức bằng biểu đồ Venn

Giả sử biểu đồ hiển thị ba tập hợp $A$, $B$ và $C$:

![Biểu đồ Venn](venn-inclusion-exclusion.png "Biểu đồ Venn")

Khi đó, diện tích của hợp $A \cup B \cup C$ bằng tổng diện tích $A$, $B$ và $C$ trừ đi các phần diện tích bị chồng lấp hai lần $A \cap B$, $A \cap C$, $B \cap C$, nhưng phải cộng lại diện tích bị phủ bởi cả ba tập hợp $A \cap B \cap C$:

$$S(A \cup B \cup C) = S(A) + S(B) + S(C) - S(A \cap B) - S(A \cap C) - S(B \cap C) + S(A \cap B \cap C)$$

Công thức này cũng có thể tổng quát hóa cho hợp của $n$ tập hợp.

### Công thức theo lý thuyết xác suất

Nếu $A_i$ $(i = 1,2...n)$ là các sự kiện và ${\cal P}(A_i)$ là xác suất của một sự kiện từ $A_i$ xảy ra, thì xác suất của hợp các sự kiện đó (tức là xác suất để ít nhất một trong các sự kiện xảy ra) bằng:

$$\begin{eqnarray}
{\cal P} \left( \bigcup_{i=1}^n A_i \right) &=& \sum_{i=1}^n{\cal P}(A_i)\ - \sum_{1\leq i<j\leq n} {\cal P}(A_i \cap A_j)\  + \\
&+& \sum _{1\leq i<j<k\leq n}{\cal P}(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n-1} {\cal P}( A_1 \cap \cdots \cap A_n )
\end{eqnarray}$$

Và viết gọn lại là:

$${\cal P} \left(\bigcup_{i=1}^n A_i \right) = \sum_{\emptyset \neq J\subseteq \{1,2,\ldots ,n\}} (-1)^{|J|-1}\ {\cal P}{\Biggl (}\bigcap_{j\in J}A_{j}{\Biggr )}$$

## Chứng minh

Để chứng minh, cách thuận tiện nhất là sử dụng công thức toán học dựa trên lý thuyết tập hợp:

$$\left|\bigcup_{i=1}^n A_i \right| = \sum_{\emptyset \neq J\subseteq \{1,2,\ldots ,n\}} (-1)^{|J|-1}{\Biggl |}\bigcap_{j\in J}A_{j}{\Biggr |}$$

Chúng ta muốn chứng minh rằng bất kỳ phần tử nào nằm trong ít nhất một trong các tập hợp $A_i$ cũng sẽ chỉ xuất hiện một lần trong công thức (lưu ý rằng các phần tử không có mặt trong bất kỳ tập hợp nào trong $A_i$ sẽ không bao giờ được tính ở vế phải của công thức).

Xét một phần tử $x$ xuất hiện trong $k \geq 1$ tập hợp $A_i$. Chúng ta sẽ chỉ ra rằng nó được đếm đúng một lần trong công thức. Lưu ý rằng:

* trong các số hạng mà $|J| = 1$, phần tử $x$ sẽ được đếm **$+\ k$** lần;
* trong các số hạng mà $|J| = 2$, phần tử $x$ sẽ được đếm **$-\ \binom{k}{2}$** lần - vì nó sẽ được đếm trong các số hạng bao gồm hai trong số $k$ tập hợp chứa $x$;
* trong các số hạng mà $|J| = 3$, phần tử $x$ sẽ được đếm **$+\ \binom{k}{3}$** lần;
* $\cdots$
* trong các số hạng mà $|J| = k$, phần tử $x$ sẽ được đếm **$(-1)^{k-1}\cdot \binom{k}{k}$** lần;
* trong các số hạng mà $|J| \gt k$, phần tử $x$ sẽ được đếm **không** lần;

Điều này dẫn đến tổng các [hệ số nhị thức](binomial-coefficients.md) sau:

$$ T = \binom{k}{1} - \binom{k}{2} + \binom{k}{3} - \cdots + (-1)^{i-1}\cdot \binom{k}{i} + \cdots + (-1)^{k-1}\cdot \binom{k}{k}$$

Biểu thức này rất giống với khai triển nhị thức của $(1 - x)^k$:

$$ (1 - x)^k = \binom{k}{0} - \binom{k}{1} \cdot x + \binom{k}{2} \cdot x^2 - \binom{k}{3} \cdot x^3 + \cdots + (-1)^k\cdot \binom{k}{k} \cdot x^k $$

Khi $x = 1$, $(1 - x)^k$ trông rất giống $T$. Tuy nhiên, biểu thức có thêm một $\binom{k}{0} = 1$, và nó được nhân với $-1$. Điều đó dẫn chúng ta đến $(1 - 1)^k = 1 - T$. Do đó $T = 1 - (1 - 1)^k = 1$, đó là điều cần chứng minh. Phần tử được đếm chính xác một lần.

## Tổng quát hóa để tính số phần tử nằm trong chính xác $r$ tập hợp

Nguyên lý bù trừ có thể được viết lại để tính số lượng phần tử không nằm trong tập hợp nào:

$$\left|\bigcap_{i=1}^n \overline{A_i}\right|=\sum_{m=0}^n (-1)^m \sum_{|X|=m} \left|\bigcap_{i\in X} A_{i}\right|$$

Xét sự tổng quát hóa của nó để tính số lượng phần tử có mặt trong chính xác $r$ tập hợp:

$$\left|\bigcup_{|B|=r}\left[\bigcap_{i \in B} A_i \cap \bigcap_{j \not\in B} \overline{A_j}\right]\right|=\sum_{m=r}^n (-1)^{m-r}\dbinom{m}{r} \sum_{|X|=m} \left|\bigcap_{i \in X} A_{i}\right|$$

Để chứng minh công thức này, hãy xét một phần tử $B$ cụ thể. Dựa trên nguyên lý bù trừ cơ bản, ta có thể nói về nó rằng:

$$\left|\bigcap_{i \in B} A_i \cap \bigcap_{j \not \in B} \overline{A_j}\right|=\sum_{m=r}^{n} (-1)^{m-r} \sum_{\substack{|X|=m \newline B \subset X}}\left|\bigcap_{i\in X} A_{i}\right|$$

Các tập hợp ở vế trái không giao nhau với các $B$ khác nhau, vì vậy ta có thể cộng trực tiếp chúng lại. Ngoài ra, cần lưu ý rằng bất kỳ tập hợp $X$ nào cũng sẽ luôn có hệ số $(-1)^{m-r}$ nếu nó xuất hiện, và nó sẽ xuất hiện trong chính xác $\dbinom{m}{r}$ tập hợp $B$.

## Ứng dụng khi giải bài tập

Nguyên lý bù trừ rất khó hiểu nếu không nghiên cứu các ứng dụng của nó.

Trước hết, chúng ta sẽ xem xét ba bài toán đơn giản nhất "trên giấy" để minh họa các ứng dụng của nguyên lý, sau đó xem xét các bài toán thực tế khó giải quyết nếu không có nguyên lý bù trừ.

Các bài toán yêu cầu "tìm **số** cách" rất đáng chú ý, vì đôi khi chúng dẫn đến các giải pháp đa thức thay vì hàm mũ.

### Bài toán đơn giản về hoán vị

Bài toán: đếm có bao nhiêu hoán vị của các số từ $0$ đến $9$ sao cho phần tử đầu tiên lớn hơn $1$ và phần tử cuối cùng nhỏ hơn $8$.

Hãy đếm số lượng hoán vị "xấu", tức là các hoán vị trong đó phần tử đầu tiên là $\leq 1$ và/hoặc phần tử cuối cùng là $\geq 8$.

Chúng ta ký hiệu $X$ là tập các hoán vị có phần tử đầu tiên là $\leq 1$, và $Y$ là tập các hoán vị có phần tử cuối cùng là $\geq 8$. Khi đó, số lượng hoán vị "xấu" theo công thức bù trừ sẽ là:

$$ |X \cup Y| = |X| + |Y| - |X \cap Y| $$

Sau một vài tính toán tổ hợp đơn giản, ta sẽ có:

$$ 2 \cdot 9! + 2 \cdot 9! - 2 \cdot 2 \cdot 8! $$

Việc còn lại chỉ là lấy tổng $10!$ trừ đi số này để có được số lượng hoán vị "tốt".

### Bài toán đơn giản về dãy (0, 1, 2)

Bài toán: đếm có bao nhiêu dãy có độ dài $n$ bao gồm các số $0,1,2$ sao cho mỗi số xuất hiện **ít nhất một lần**.

Một lần nữa, hãy chuyển sang bài toán ngược, tức là ta tính số lượng dãy **không** chứa **ít nhất một** trong các số đó.

Hãy ký hiệu $A_i (i = 0,1,2)$ là tập các dãy trong đó chữ số $i$ **không** xuất hiện. Công thức bù trừ cho số lượng các dãy "xấu" sẽ là:

$$ |A_0 \cup A_1 \cup A_2| = |A_0| + |A_1| + |A_2| - |A_0 \cap A_1| - |A_0 \cap A_2| - |A_1 \cap A_2| + |A_0 \cap A_1 \cap A_2| $$

* Kích thước của mỗi $A_i$ là $2^n$, vì mỗi dãy chỉ có thể chứa hai trong ba chữ số.
* Kích thước của mỗi giao từng đôi một $A_i \cap A_j$ bằng $1$, vì chỉ còn lại một chữ số để tạo dãy.
* Kích thước của giao của cả ba tập hợp bằng $0$, vì không còn chữ số nào để tạo dãy.

Vì đã giải bài toán ngược, ta lấy tổng $3^n$ dãy trừ đi kết quả đó:

$$3^n - (3 \cdot 2^n - 3 \cdot 1 + 0)$$

<div id="the-number-of-integer-solutions-to-the-equation"></div>
### Số nghiệm nguyên với ràng buộc chặn trên {: #number-of-upper-bound-integer-sums }

Xét phương trình sau:

$$x_1 + x_2 + x_3 + x_4 + x_5 + x_6 = 20$$

trong đó $0 \le x_i \le 8 ~ (i = 1,2,\ldots 6)$.

Bài toán: đếm số nghiệm của phương trình.

Tạm quên ràng buộc về $x_i$ và chỉ đếm số nghiệm không âm của phương trình này. Điều này dễ dàng thực hiện bằng phương pháp [Stars and Bars](stars_and_bars.md): chúng ta muốn chia một dãy gồm $20$ đơn vị thành $6$ nhóm, tương đương với việc sắp xếp $5$ _thanh chắn_ và $20$ _ngôi sao_:

$$N_0 = \binom{25}{5}$$

Bây giờ ta sẽ tính số nghiệm "xấu" với nguyên lý bù trừ. Các nghiệm "xấu" là những nghiệm trong đó một hoặc nhiều $x_i$ lớn hơn hoặc bằng $9$.

Ký hiệu $A_k ~ (k = 1,2\ldots 6)$ là tập các nghiệm mà $x_k \ge 9$, và tất cả các $x_i \ge 0 ~ (i \ne k)$ khác (chúng có thể $\ge 9$ hoặc không). Để tính kích thước của $A_k$, lưu ý rằng chúng ta có cùng vấn đề tổ hợp như đã giải ở hai đoạn trên, nhưng bây giờ $9$ đơn vị đã bị loại khỏi các nhóm và thuộc chắc chắn về nhóm đầu tiên. Do đó:

$$ | A_k | = \binom{16}{5} $$

Tương tự, kích thước của giao giữa hai tập hợp $A_k$ và $A_p$ (với $k \ne p$) bằng:

$$ \left| A_k \cap A_p \right| = \binom{7}{5}$$

Kích thước của mỗi giao ba tập hợp bằng không, vì $20$ đơn vị sẽ không đủ cho ba hoặc nhiều biến lớn hơn hoặc bằng $9$.

Kết hợp tất cả lại vào công thức bù trừ và vì đã giải bài toán ngược, cuối cùng ta có đáp án:

$$\binom{25}{5} - \left(\binom{6}{1} \cdot \binom{16}{5} - \binom{6}{2} \cdot \binom{7}{5}\right) $$

Điều này dễ dàng tổng quát cho $d$ số có tổng bằng $s$ với ràng buộc $0 \le x_i \le b$:

$$\sum_{i=0}^d (-1)^i \binom{d}{i} \binom{s+d-1-(b+1)i}{d-1}$$

Như trên, chúng ta coi các hệ số nhị thức với chỉ số trên âm là bằng không.

Lưu ý rằng bài toán này cũng có thể giải bằng quy hoạch động (DP) hoặc hàm sinh. Đáp án theo nguyên lý bù trừ được tính trong thời gian $O(d)$ (giả sử các phép toán như hệ số nhị thức là O(1)), trong khi phương pháp DP đơn giản sẽ mất thời gian $O(ds)$.

### Số lượng các số nguyên tố cùng nhau trong một khoảng

Bài toán: cho hai số $n$ và $r$, đếm số lượng các số nguyên trong khoảng $[1;r]$ nguyên tố cùng nhau với n (ước chung lớn nhất của chúng bằng $1$).

Hãy giải bài toán ngược - tính số lượng các số không nguyên tố cùng nhau với $n$.

Chúng ta sẽ ký hiệu các thừa số nguyên tố của $n$ là $p_i (i = 1\cdots k)$.

Có bao nhiêu số trong khoảng $[1;r]$ chia hết cho $p_i$? Câu trả lời cho câu hỏi này là:

$$ \left\lfloor \frac{ r }{ p_i } \right\rfloor $$

Tuy nhiên, nếu ta chỉ đơn giản cộng các số này lại, một số số sẽ được cộng nhiều lần (những số có nhiều $p_i$ là thừa số). Vì vậy, cần sử dụng nguyên lý bù trừ.

Chúng ta sẽ duyệt qua tất cả $2^k$ tập con của $p_i$, tính tích của chúng rồi cộng hoặc trừ số lượng bội số của tích đó.

Dưới đây là cài đặt C++:

```cpp
int solve (int n, int r) {
	vector<int> p;
	for (int i=2; i*i<=n; ++i)
		if (n % i == 0) {
			p.push_back (i);
			while (n % i == 0)
				n /= i;
		}
	if (n > 1)
		p.push_back (n);

	int sum = 0;
	for (int msk=1; msk<(1<<p.size()); ++msk) {
		int mult = 1,
			bits = 0;
		for (int i=0; i<(int)p.size(); ++i)
			if (msk & (1<<i)) {
				++bits;
				mult *= p[i];
			}

		int cur = r / mult;
		if (bits % 2 == 1)
			sum += cur;
		else
			sum -= cur;
	}

	return r - sum;
}
```

Độ phức tạp của lời giải là $O (\sqrt{n})$.

### Số lượng số nguyên trong một khoảng chia hết cho ít nhất một trong các số đã cho

Cho $n$ số $a_i$ và số $r$. Bạn muốn đếm số lượng các số nguyên trong khoảng $[1; r]$ chia hết cho ít nhất một trong các $a_i$.

Thuật toán giải gần như giống với bài toán trước - xây dựng công thức bù trừ trên các số $a_i$, tức là mỗi số hạng trong công thức này là số lượng các số chia hết cho một tập con cho trước của các số $a_i$ (nói cách khác, chia hết cho [bội chung nhỏ nhất](../algebra/euclid-algorithm.md) của chúng).

Vì vậy, chúng ta sẽ duyệt qua tất cả $2^n$ tập con của các số nguyên $a_i$ với $O(n \log r)$ phép toán để tìm bội chung nhỏ nhất của chúng, thêm hoặc bớt số lượng bội số của nó trong khoảng. Độ phức tạp là $O (2^n\cdot n\cdot \log r)$.

### Số lượng các xâu thỏa mãn một mẫu cho trước

Xét $n$ mẫu xâu có cùng độ dài, bao gồm chỉ các chữ cái ($a...z$) hoặc dấu hỏi. Bạn cũng được cho một số $k$. Một xâu khớp với mẫu nếu nó có cùng độ dài với mẫu, và tại mỗi vị trí, các ký tự tương ứng bằng nhau hoặc ký tự trong mẫu là dấu hỏi. Bài toán là đếm số lượng các xâu khớp chính xác $k$ mẫu (bài toán đầu tiên) và khớp ít nhất $k$ mẫu (bài toán thứ hai).

Lưu ý trước tiên rằng chúng ta có thể dễ dàng đếm số lượng các xâu thỏa mãn đồng thời tất cả các mẫu đã chỉ định. Để làm điều này, đơn giản là "trộn" các mẫu: duyệt qua các vị trí ("ô") và xem xét một vị trí trên tất cả các mẫu. Nếu tất cả các mẫu đều có dấu hỏi ở vị trí này, ký tự có thể là bất kỳ chữ cái nào từ $a$ đến $z$. Ngược lại, ký tự ở vị trí này được xác định duy nhất bởi các mẫu không chứa dấu hỏi.

Bây giờ hãy tìm cách giải phiên bản đầu tiên của bài toán: khi xâu phải thỏa mãn chính xác $k$ mẫu.

Để giải nó, duyệt và cố định một tập con cụ thể $X$ từ tập các mẫu bao gồm $k$ mẫu. Sau đó, chúng ta phải đếm số lượng các xâu thỏa mãn tập mẫu này, và chỉ khớp với nó, tức là chúng không khớp với bất kỳ mẫu nào khác. Chúng ta sẽ sử dụng nguyên lý bù trừ theo một cách khác: cộng trên tất cả các tập cha $Y$ (các tập con từ tập gốc gồm các xâu chứa $X$), và cộng vào hoặc trừ khỏi đáp án hiện tại:

$$ ans(X) = \sum_{Y \supseteq X} (-1)^{|Y|-k} \cdot f(Y) $$

Trong đó $f(Y)$ là số lượng các xâu khớp với $Y$ (ít nhất $Y$).

(Nếu bạn thấy khó hiểu, bạn có thể thử vẽ Biểu đồ Venn.)

Nếu ta cộng trên tất cả $ans(X)$, ta sẽ có đáp án cuối cùng:

$$ ans = \sum_{X ~ : ~ |X| = k} ans(X) $$

Tuy nhiên, độ phức tạp của giải pháp này là $O(3^k \cdot k)$. Để cải thiện, hãy lưu ý rằng các tính toán $ans(X)$ khác nhau thường chia sẻ $Y$ tập hợp.

Chúng ta sẽ đảo ngược công thức bù trừ và cộng theo $Y$ tập hợp. Bây giờ rõ ràng rằng cùng một tập hợp $Y$ sẽ được tính đến trong quá trình tính toán của $ans(X)$ trong số $\binom{|Y|}{k}$ tập hợp với cùng dấu $(-1)^{|Y| - k}$.

$$ ans = \sum_{Y ~ : ~ |Y| \ge k} (-1)^{|Y|-k} \cdot \binom{|Y|}{k} \cdot f(Y) $$

Bây giờ giải pháp của chúng ta có độ phức tạp là $O(2^k \cdot k)$.

Bây giờ chúng ta sẽ giải phiên bản thứ hai của bài toán: tìm số lượng các xâu khớp với **ít nhất** $k$ mẫu.

Tất nhiên, chúng ta có thể chỉ cần sử dụng lời giải của phiên bản đầu tiên và cộng các câu trả lời cho các tập có kích thước lớn hơn $k$. Tuy nhiên, bạn có thể nhận thấy rằng trong bài toán này, tập |Y| được xét trong công thức cho tất cả các tập có kích thước $\ge k$ nằm trong $Y$. Như vậy, ta có thể viết phần biểu thức được nhân với $f(Y)$ như sau:

$$ (-1)^{|Y|-k} \cdot \binom{|Y|}{k} + (-1)^{|Y|-k-1} \cdot \binom{|Y|}{k+1} + (-1)^{|Y|-k-2} \cdot \binom{|Y|}{k+2} + \cdots + (-1)^{|Y|-|Y|} \cdot \binom{|Y|}{|Y|} $$

Nhìn vào sách của Graham (Graham, Knuth, Patashnik. "Concrete mathematics" [1998] ), ta thấy một công thức nổi tiếng cho các [hệ số nhị thức](binomial-coefficients.md):

$$ \sum_{k=0}^m (-1)^k \cdot \binom{n}{k} = (-1)^m \cdot \binom{n-1}{m} $$

Áp dụng nó vào đây, ta thấy rằng toàn bộ tổng các hệ số nhị thức được tối giản:

$$ (-1)^{|Y|-k} \cdot \binom{|Y|-1}{|Y|-k} $$

Do đó, đối với bài toán này, chúng ta cũng thu được lời giải với độ phức tạp $O(2^k \cdot k)$:

$$ ans = \sum_{Y ~ : ~ |Y| \ge k} (-1)^{|Y|-k} \cdot \binom{|Y|-1}{|Y|-k} \cdot f(Y) $$

### Số cách đi từ ô này đến ô khác

Có một bảng $n \times m$, và $k$ ô là các bức tường không thể đi qua. Robot ban đầu ở ô $(1,1)$ (góc dưới bên trái). Robot chỉ có thể di chuyển sang phải hoặc lên trên, và cuối cùng nó cần đến ô $(n,m)$, tránh mọi vật cản. Bạn cần đếm số cách nó có thể thực hiện.

Giả sử kích thước $n$ và $m$ rất lớn (ví dụ $10^9$), và số $k$ nhỏ (khoảng $100$).

Trước hết, hãy sắp xếp các vật cản theo tọa độ $x$, và trong trường hợp bằng nhau thì theo tọa độ $y$.

Cũng cần biết cách giải bài toán mà không có vật cản: tức là cách đếm số cách để đi từ ô này sang ô khác. Trên một trục, chúng ta cần đi qua $x$ ô, và trên trục kia, $y$ ô. Từ tổ hợp đơn giản, ta có công thức sử dụng [hệ số nhị thức](binomial-coefficients.md):

$$\binom{x+y}{x}$$

Bây giờ để đếm số cách đi từ ô này sang ô khác mà tránh tất cả các vật cản, bạn có thể sử dụng nguyên lý bù trừ để giải bài toán ngược: đếm số cách đi qua bảng mà bước vào một tập con các vật cản (và trừ nó ra khỏi tổng số cách đi).

Khi duyệt qua một tập con các vật cản mà chúng ta sẽ bước vào, để đếm số cách làm điều này, chỉ cần nhân số lượng tất cả các đường đi từ ô xuất phát đến vật cản đầu tiên được chọn, từ vật cản đầu tiên đến vật cản thứ hai, v.v., và sau đó cộng hoặc trừ số này vào đáp án theo công thức bù trừ chuẩn.

Tuy nhiên, điều này sẽ lại không phải là đa thức về độ phức tạp $O(2^k \cdot k)$.

Dưới đây là một lời giải đa thức:

Chúng ta sẽ sử dụng quy hoạch động. Để thuận tiện, hãy thêm (1,1) vào đầu và (n,m) vào cuối của mảng vật cản. Hãy tính các số $d[i]$ — số cách để đi từ điểm xuất phát ($0-th$) đến $i-th$ mà không bước vào bất kỳ vật cản nào khác (ngoại trừ $i$, tất nhiên). Chúng ta sẽ tính số này cho tất cả các ô vật cản, và cả ô đích.

Hãy quên đi các vật cản trong giây lát và chỉ đếm số đường đi từ ô $0$ đến $i$. Chúng ta cần xem xét một số đường đi "xấu", những đường đi qua các vật cản, và trừ chúng ra khỏi tổng số cách đi từ $0$ đến $i$.

Khi xét một vật cản $t$ giữa $0$ và $i$ ($0 < t < i$), mà chúng ta có thể bước vào, ta thấy rằng số lượng đường đi từ $0$ đến $i$ đi qua $t$ với $t$ là **vật cản đầu tiên giữa điểm xuất phát và $i$**. Chúng ta có thể tính điều đó như: $d[t]$ nhân với số lượng đường đi tùy ý từ $t$ đến $i$. Chúng ta có thể đếm số lượng cách "xấu" bằng cách cộng điều này cho tất cả các $t$ giữa $0$ và $i$.

Chúng ta có thể tính $d[i]$ trong $O(k)$ cho $O(k)$ vật cản, vì vậy giải pháp này có độ phức tạp $O(k^2)$.

### Số lượng bộ bốn nguyên tố cùng nhau

Bạn được cho $n$ số: $a_1, a_2, \ldots, a_n$. Bạn được yêu cầu đếm số cách chọn bốn số sao cho ước chung lớn nhất của chúng bằng một.

Chúng ta sẽ giải bài toán ngược — tính số lượng bộ bốn "xấu", tức là các bộ bốn trong đó tất cả các số đều chia hết cho một số $d > 1$.

Chúng ta sẽ sử dụng nguyên lý bù trừ trong khi cộng trên tất cả các nhóm bốn số có thể chia hết cho một ước số $d$.

$$ans = \sum_{d \ge 2} (-1)^{deg(d)-1} \cdot f(d)$$

trong đó $deg(d)$ là số lượng các số nguyên tố trong phân tích thừa số của số $d$ và $f(d)$ là số lượng các bộ bốn chia hết cho $d$.

Để tính hàm $f(d)$, bạn chỉ cần đếm số lượng bội số của $d$ (như đã đề cập trong bài toán trước) và sử dụng [hệ số nhị thức](binomial-coefficients.md) để đếm số cách chọn bốn trong số chúng.

Như vậy, bằng cách sử dụng công thức bù trừ, chúng ta cộng số lượng các nhóm bốn số chia hết cho một số nguyên tố, sau đó trừ đi số lượng các bộ bốn chia hết cho tích của hai số nguyên tố, cộng các bộ bốn chia hết cho ba số nguyên tố, v.v.

### Số lượng bộ ba điều hòa

Bạn được cho một số $n \le 10^6$. Bạn được yêu cầu đếm số lượng bộ ba $2 \le a < b < c \le n$ thỏa mãn một trong các điều kiện sau:

* hoặc ${\rm gcd}(a,b) = {\rm gcd}(a,c) = {\rm gcd}(b,c) = 1$,
* hoặc ${\rm gcd}(a,b) > 1, {\rm gcd}(a,c) > 1, {\rm gcd}(b,c) > 1$.

Trước hết, hãy giải bài toán ngược — tức là đếm số lượng các bộ ba không điều hòa.

Thứ hai, lưu ý rằng bất kỳ bộ ba không điều hòa nào cũng được tạo thành từ một cặp số nguyên tố cùng nhau và một số thứ ba không nguyên tố cùng nhau với ít nhất một số từ cặp đó.

Vì vậy, số lượng các bộ ba không điều hòa chứa $i$ bằng số lượng các số nguyên từ $2$ đến $n$ nguyên tố cùng nhau với $i$ nhân với số lượng các số nguyên không nguyên tố cùng nhau với $i$.

Hoặc $gcd(a,b) = 1 \wedge gcd(a,c) > 1 \wedge gcd(b,c) > 1$

hoặc $gcd(a,b) = 1 \wedge gcd(a,c) = 1 \wedge gcd(b,c) > 1$

Trong cả hai trường hợp này, nó sẽ được đếm hai lần. Trường hợp đầu tiên sẽ được đếm khi $i = a$ và khi $i = b$. Trường hợp thứ hai sẽ được đếm khi $i = b$ và khi $i = c$. Do đó, để tính số lượng các bộ ba không điều hòa, chúng ta cộng các tính toán này qua tất cả $i$ từ $2$ đến $n$ và chia cho $2$.

Bây giờ tất cả những gì còn lại là học cách đếm số lượng các số nguyên tố cùng nhau với $i$ trong khoảng $[2;n]$. Mặc dù bài toán này đã được đề cập, nhưng giải pháp trên không phù hợp ở đây — nó đòi hỏi phải phân tích thừa số mỗi số nguyên từ $2$ đến $n$, và sau đó duyệt qua tất cả các tập con của các số nguyên tố này.

Một giải pháp nhanh hơn là có thể thực hiện với sự sửa đổi sàng Eratosthenes như sau:

1. Đầu tiên, chúng ta tìm tất cả các số trong khoảng $[2;n]$ sao cho phân tích thừa số đơn giản của nó không bao gồm một thừa số nguyên tố hai lần. Chúng ta cũng sẽ cần biết, đối với các số này, nó bao gồm bao nhiêu thừa số.
    * Để làm điều này, chúng ta sẽ duy trì một mảng $deg[i]$ để lưu trữ số lượng các số nguyên tố trong phân tích thừa số của $i$, và một mảng $good[i]$, để đánh dấu liệu $i$ có chứa mỗi thừa số tối đa một lần ($good[i] = 1$) hay không ($good[i] = 0$). Khi duyệt từ $2$ đến $n$, nếu ta đạt được một số có $deg$ bằng $0$, thì nó là một số nguyên tố và $deg$ của nó là $1$.
    * Trong khi sàng Eratosthenes, chúng ta sẽ duyệt $i$ từ $2$ đến $n$. Khi xử lý một số nguyên tố, ta đi qua tất cả các bội số của nó và tăng $deg[]$ của chúng. Nếu một trong những bội số này là bội số của bình phương của $i$, thì ta có thể đặt $good$ là sai.

2. Thứ hai, chúng ta cần tính toán câu trả lời cho tất cả $i$ từ $2$ đến $n$, tức là mảng $cnt[]$ — số lượng các số nguyên không nguyên tố cùng nhau với $i$.
    * Để thực hiện điều này, hãy nhớ lại công thức bù trừ hoạt động như thế nào — thực tế ở đây chúng ta triển khai cùng một khái niệm, nhưng với logic đảo ngược: chúng ta duyệt qua một thành phần (một tích của các số nguyên tố từ phân tích thừa số) và cộng hoặc trừ số hạng của nó vào công thức bù trừ của mỗi bội số của nó.
    * Vì vậy, giả sử chúng ta đang xử lý một số $i$ sao cho $good[i] = true$, tức là nó tham gia vào công thức bù trừ. Duyệt qua tất cả các số là bội số của $i$, và cộng hoặc trừ $\lfloor N/i \rfloor$ vào $cnt[]$ của chúng (tín hiệu phụ thuộc vào $deg[i]$: nếu $deg[i]$ là lẻ, thì ta cộng, ngược lại trừ).

Dưới đây là cài đặt C++:

```cpp
int n;
bool good[MAXN];
int deg[MAXN], cnt[MAXN];

long long solve() {
	memset (good, 1, sizeof good);
	memset (deg, 0, sizeof deg);
	memset (cnt, 0, sizeof cnt);

	long long ans_bad = 0;
	for (int i=2; i<=n; ++i) {
		if (good[i]) {
			if (deg[i] == 0)  deg[i] = 1;
			for (int j=1; i*j<=n; ++j) {
				if (j > 1 && deg[i] == 1)
					if (j % i == 0)
						good[i*j] = false;
					else
						++deg[i*j];
				cnt[i*j] += (n / i) * (deg[i]%2==1 ? +1 : -1);
			}
		}
		ans_bad += (cnt[i] - 1) * 1ll * (n-1 - cnt[i]);
	}

	return (n-1) * 1ll * (n-2) * (n-3) / 6 - ans_bad / 2;
}
```

Độ phức tạp của lời giải là $O(n \log n)$, vì đối với hầu hết mọi số đến $n$, chúng ta thực hiện $n/i$ vòng lặp lồng nhau.

### Số lượng hoán vị không có điểm cố định (rối loạn)

Chứng minh rằng số lượng các hoán vị độ dài $n$ không có điểm cố định (tức là không có số $i$ nào ở vị trí $i$ - còn gọi là rối loạn) bằng số sau:

$$n! - \binom{n}{1} \cdot (n-1)! + \binom{n}{2} \cdot (n-2)! - \binom{n}{3} \cdot (n-3)! + \cdots \pm \binom{n}{n} \cdot (n-n)! $$

và xấp xỉ bằng:

$$ \frac{ n! }{ e } $$

(nếu bạn làm tròn biểu thức này đến số nguyên gần nhất — bạn có chính xác số lượng các hoán vị không có điểm cố định)

Ký hiệu $A_k$ là tập các hoán vị độ dài $n$ với điểm cố định tại vị trí $k$ ($1 \le k \le n$) (tức là phần tử $k$ nằm tại vị trí $k$).

Bây giờ chúng ta sử dụng công thức bù trừ để đếm số lượng các hoán vị có ít nhất một điểm cố định. Đối với điều này, chúng ta cần học cách tính kích thước của một giao các tập hợp $A_i$, như sau:

$$\begin{eqnarray}
\left| A_p \right| &=& (n-1)!\ , \\
\left| A_p \cap A_q \right| &=& (n-2)!\ , \\
\left| A_p \cap A_q \cap A_r \right| &=& (n-3)!\ , \\
\cdots ,
\end{eqnarray}$$

bởi vì nếu chúng ta biết số lượng các điểm cố định bằng $x$, thì chúng ta biết vị trí của $x$ phần tử của hoán vị, và tất cả $(n-x)$ phần tử khác có thể được đặt ở bất cứ đâu.

Thay thế điều này vào công thức bù trừ, và với việc số cách chọn một tập con kích thước $x$ từ tập $n$ phần tử bằng $\binom{n}{x}$, ta thu được công thức cho số lượng các hoán vị có ít nhất một điểm cố định:

$$\binom{n}{1} \cdot (n-1)! - \binom{n}{2} \cdot (n-2)! + \binom{n}{3} \cdot (n-3)! - \cdots \pm \binom{n}{n} \cdot (n-n)! $$

Khi đó số lượng hoán vị không có điểm cố định bằng:

$$n! - \binom{n}{1} \cdot (n-1)! + \binom{n}{2} \cdot (n-2)! - \binom{n}{3} \cdot (n-3)! + \cdots \pm \binom{n}{n} \cdot (n-n)! $$

Đơn giản hóa biểu thức này, ta thu được **các biểu thức chính xác và xấp xỉ cho số lượng các hoán vị không có điểm cố định**:

$$ n! \left( 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots \pm \frac{1}{n!} \right ) \approx \frac{n!}{e} $$

(bởi vì tổng trong ngoặc là $n+1$ số hạng đầu tiên của khai triển trong chuỗi Taylor $e^{-1}$)

Cần lưu ý rằng một bài toán tương tự có thể được giải theo cách này: khi bạn cần các điểm cố định không nằm trong $m$ phần tử đầu tiên của hoán vị (và không phải trong tất cả, như ta vừa giải). Công thức thu được giống như công thức chính xác nêu trên, nhưng nó sẽ đi đến tổng của $k$, thay vì $n$.

## Các bài toán thực hành

Danh sách các bài toán có thể giải bằng nguyên lý bù trừ:

* [UVA #10325 "Xổ số" [độ khó: thấp]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1266)
* [UVA #11806 "Người cổ vũ" [độ khó: thấp]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2906)
* [TopCoder SRM 477 "Thư ký bất cẩn" [độ khó: thấp]](http://www.topcoder.com/stat?c=problem_statement&pm=10875)
* [TopCoder TCHS 16 "Tính chia hết" [độ khó: thấp]](http://community.topcoder.com/stat?c=problem_statement&pm=6658&rd=10068)
* [SPOJ #6285 NGM2 , "Một trò chơi khác với các con số" [độ khó: thấp]](http://www.spoj.com/problems/NGM2/)
* [TopCoder SRM 382 "Vé quyến rũ dễ" [độ khó: trung bình]](http://community.topcoder.com/stat?c=problem_statement&pm=8470)
* [TopCoder SRM 390 "Tập hợp các mẫu" [độ khó: trung bình]](http://community.topcoder.com/stat?c=problem_statement&pm=8307)
* [TopCoder SRM 176 "Rối loạn" [độ khó: trung bình]](http://community.topcoder.com/stat?c=problem_statement&pm=2013)
* [TopCoder SRM 457 "Lục giác" [độ khó: trung bình]](http://community.topcoder.com/stat?c=problem_statement&pm=10702&rd=14144&rm=303184&cr=22697599)
* [SPOJ #4191 MSKYCODE "Mã bầu trời" [độ khó: trung bình]](http://www.spoj.com/problems/MSKYCODE/)
* [SPOJ #4168 SQFREE "Số không chứa bình phương" [độ khó: trung bình]](http://www.spoj.com/problems/SQFREE/)
* [CodeChef "Đếm quan hệ" [độ khó: trung bình]](http://www.codechef.com/JAN11/problems/COUNTREL/)
* [SPOJ - Hầu như là số nguyên tố nữa](http://www.spoj.com/problems/KPRIMESB/)
* [SPOJ - Tìm số cặp bạn bè](http://www.spoj.com/problems/IITKWPCH/)
* [SPOJ - Tập con bò cân bằng](http://www.spoj.com/problems/SUBSET/)
* [SPOJ - Toán dễ [độ khó: trung bình]](http://www.spoj.com/problems/EASYMATH/)
* [SPOJ - MOMOS - Lễ hội lợn [độ khó: dễ]](https://www.spoj.com/problems/MOMOS/)
* [Atcoder - Lưới 2 [độ khó: dễ]](https://atcoder.jp/contests/dp/tasks/dp_y/)
* [Codeforces - Đếm GCD](https://codeforces.com/contest/1750/problem/D)