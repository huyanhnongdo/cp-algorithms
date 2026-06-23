---
tags:
  - Translated
e_maxx_link: big_integer
---

# Số học độ chính xác tùy ý

Số học độ chính xác tùy ý (Arbitrary-Precision arithmetic), còn được gọi là "bignum" hay đơn giản là "số học số lớn" (long arithmetic), là một tập hợp các cấu trúc dữ liệu và thuật toán cho phép xử lý các số có giá trị lớn hơn nhiều so với khả năng lưu trữ của các kiểu dữ liệu tiêu chuẩn. Dưới đây là một số dạng số học độ chính xác tùy ý.

## Số học số lớn số nguyên cổ điển

Ý tưởng chính là một số sẽ được lưu trữ dưới dạng một mảng các "chữ số" của nó trong một cơ số nào đó. Một số cơ số được sử dụng thường xuyên nhất là cơ số 10, lũy thừa của 10 ($10^4$ hoặc $10^9$) và hệ nhị phân.

Các phép toán trên các số ở dạng này được thực hiện bằng cách sử dụng các thuật toán "ở trường học" (đặt tính theo cột dọc) cho các phép cộng, trừ, nhân và chia. Chúng ta cũng có thể sử dụng các thuật toán nhân nhanh như: biến đổi Fourier nhanh (FFT) và thuật toán Karatsuba.

Ở đây chúng ta chỉ mô tả số học số lớn cho các số nguyên không âm. Để mở rộng các thuật toán nhằm xử lý số nguyên âm, người ta phải đưa vào và duy trì thêm một cờ hiệu "số âm" hoặc sử dụng biểu diễn số nguyên dạng bù hai.

### Cấu trúc dữ liệu

Chúng ta sẽ lưu trữ các số dưới dạng một `vector<int>`, trong đó mỗi phần tử là một "chữ số" duy nhất của số đó.

```cpp
typedef vector<int> lnum;
```

Để tăng hiệu suất, chúng ta sẽ sử dụng cơ số là $10^9$, nhờ đó mỗi "chữ số" của số lớn sẽ chứa đồng thời 9 chữ số thập phân.

```cpp
const int base = 1000*1000*1000;
```

Các chữ số sẽ được lưu trữ theo thứ tự từ hàng ít quan trọng nhất đến hàng quan trọng nhất (từ hàng đơn vị trở lên). Tất cả các phép toán sẽ được cài đặt sao cho sau mỗi phép toán, kết quả không chứa bất kỳ chữ số 0 nào ở đầu (leading zeros), miễn là các toán hạng ban đầu cũng không có chữ số 0 ở đầu. Tất cả các phép toán có thể tạo ra số có chữ số 0 ở đầu cần phải được theo sau bởi đoạn mã loại bỏ chúng. Lưu ý rằng trong biểu diễn này, có hai cách ký hiệu hợp lệ cho số 0: một vector rỗng, hoặc một vector chỉ chứa một chữ số 0 duy nhất.

### Đầu ra

In một số nguyên lớn là phép toán dễ nhất. Đầu tiên, chúng ta in phần tử cuối cùng của vector (hoặc 0 nếu vector rỗng), tiếp theo là in các phần tử còn lại được đệm thêm các chữ số 0 ở đầu nếu cần thiết để đảm bảo chúng có độ dài chính xác là 9 chữ số.

```cpp
printf ("%d", a.empty() ? 0 : a.back());
for (int i=(int)a.size()-2; i>=0; --i)
	printf ("%09d", a[i]);
```

Lưu ý rằng chúng ta ép kiểu `a.size()` sang kiểu số nguyên có dấu để tránh lỗi tràn số nguyên không dấu (underflow) nếu vector chứa ít hơn 2 phần tử.

### Đầu vào

Để đọc một số nguyên lớn, hãy đọc biểu diễn của nó vào một chuỗi `string` rồi chuyển đổi chuỗi đó thành các "chữ số":

```cpp
for (int i=(int)s.length(); i>0; i-=9)
	if (i < 9)
		a.push_back (atoi (s.substr (0, i).c_str()));
	else
		a.push_back (atoi (s.substr (i-9, 9).c_str()));
```

Nếu chúng ta sử dụng một mảng `char` thay vì `string`, đoạn mã sẽ còn ngắn hơn nữa:

```cpp
for (int i=(int)strlen(s); i>0; i-=9) {
	s[i] = 0;
	a.push_back (atoi (i>=9 ? s+i-9 : s));
}
```

Nếu đầu vào có thể chứa các chữ số 0 ở đầu, chúng ta có thể loại bỏ chúng như sau:

```cpp
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

### Phép cộng

Cộng thêm số lớn $b$ vào số lớn $a$ và lưu kết quả vào $a$:

```cpp
int carry = 0;
for (size_t i=0; i<max(a.size(),b.size()) || carry; ++i) {
	if (i == a.size())
		a.push_back (0);
	a[i] += carry + (i < b.size() ? b[i] : 0);
	carry = a[i] >= base;
	if (carry)  a[i] -= base;
}
```

### Phép trừ

Trừ số lớn $a$ đi số lớn $b$ ($a \ge b$) và lưu kết quả vào $a$:

```cpp
int carry = 0;
for (size_t i=0; i<b.size() || carry; ++i) {
	a[i] -= carry + (i < b.size() ? b[i] : 0);
	carry = a[i] < 0;
	if (carry)  a[i] += base;
}
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

Lưu ý rằng sau khi thực hiện phép trừ, chúng ta loại bỏ các chữ số 0 ở đầu để đảm bảo các số nguyên lớn luôn không có chữ số 0 ở đầu.

### Phép nhân với số nguyên nhỏ

Nhân số lớn $a$ với số nguyên nhỏ $b$ ($b < base$) và lưu kết quả vào $a$:

```cpp
int carry = 0;
for (size_t i=0; i<a.size() || carry; ++i) {
	if (i == a.size())
		a.push_back (0);
	long long cur = carry + a[i] * 1ll * b;
	a[i] = int (cur % base);
	carry = int (cur / base);
}
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

Tối ưu hóa bổ sung: Nếu thời gian chạy là cực kỳ quan trọng, bạn có thể cố gắng thay thế hai phép chia bằng một phép chia bằng cách chỉ tìm kết quả nguyên của phép chia (biến `carry`) rồi sử dụng nó để tìm số dư thông qua phép nhân. Điều này thường làm cho đoạn mã chạy nhanh hơn, mặc dù không quá nhiều.

### Phép nhân hai số nguyên lớn

Nhân hai số nguyên lớn $a$ và $b$ rồi lưu kết quả vào $c$:

```cpp
lnum c (a.size()+b.size());
for (size_t i=0; i<a.size(); ++i)
	for (int j=0, carry=0; j<(int)b.size() || carry; ++j) {
		long long cur = c[i+j] + a[i] * 1ll * (j < (int)b.size() ? b[j] : 0) + carry;
		c[i+j] = int (cur % base);
		carry = int (cur / base);
	}
while (c.size() > 1 && c.back() == 0)
	c.pop_back();
```

### Phép chia cho số nguyên nhỏ

Chia số nguyên lớn $a$ cho số nguyên nhỏ $b$ ($b < base$), lưu thương nguyên vào $a$ và số dư vào biến `carry`:

```cpp
int carry = 0;
for (int i=(int)a.size()-1; i>=0; --i) {
	long long cur = a[i] + carry * 1ll * base;
	a[i] = int (cur / b);
	carry = int (cur % b);
}
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

## Số học số lớn sử dụng biểu diễn phân tích thừa số nguyên tố

Ý tưởng là lưu trữ một số nguyên dưới dạng phân tích thừa số nguyên tố của nó, tức là số mũ của các số nguyên tố chia hết cho nó.

Cách tiếp cận này rất dễ cài đặt và cho phép thực hiện phép nhân và phép chia một cách dễ dàng (nhanh hơn về mặt tiệm cận so với phương pháp cổ điển), nhưng không hỗ trợ phép cộng hoặc phép trừ. Nó cũng rất tiết kiệm bộ nhớ so với cách tiếp cận cổ điển.

Phương pháp này thường được sử dụng cho các tính toán theo mô-đun của một số M không phải số nguyên tố; trong trường hợp này, một số được lưu trữ dưới dạng lũy thừa của các ước số của M chia hết cho số đó, cộng với số dư theo mô-đun M.

## Số học số lớn theo các mô-đun nguyên tố (Thuật toán Garner)

Ý tưởng là chọn một tập hợp các số nguyên tố (thường là chúng đủ nhỏ để vừa với kiểu dữ liệu số nguyên tiêu chuẩn) và lưu trữ một số nguyên lớn dưới dạng một vector chứa các số dư khi chia số nguyên đó cho từng số nguyên tố trong tập hợp.

Định lý thặng dư Trung Hoa phát biểu rằng biểu diễn này là đủ để khôi phục duy nhất bất kỳ số nào từ 0 đến tích của các số nguyên tố này trừ đi một. [Thuật toán Garner](garners-algorithm.md) cho phép khôi phục số lớn từ biểu diễn đó về dạng số nguyên thông thường.

Phương pháp này giúp tiết kiệm bộ nhớ so với cách tiếp cận cổ điển (mặc dù mức độ tiết kiệm không quá lớn như trong biểu diễn phân tích thừa số). Ngoài ra, nó cho phép thực hiện phép cộng, trừ và nhân nhanh chóng trong thời gian tỷ lệ thuận với số lượng số nguyên tố được sử dụng làm mô-đun (xem bài viết về [Định lý thặng dư Trung Hoa](chinese-remainder-theorem.md) để biết cách cài đặt).

Điểm đánh đổi là việc chuyển đổi số nguyên lớn trở lại dạng bình thường khá phức tạp và yêu cầu cài đặt số học số lớn cổ điển với phép nhân. Ngoài ra, phương pháp này không hỗ trợ phép chia.

## Số học độ chính xác tùy ý cho phân số

Các phân số xuất hiện trong các kỳ thi lập trình ít thường xuyên hơn các số nguyên, và số học số lớn cho phân số phức tạp hơn nhiều để cài đặt, vì vậy các kỳ thi lập trình chỉ khai thác một phần nhỏ của số học số lớn cho phân số.

### Số học trên phân số tối giản

Một số được biểu diễn dưới dạng một phân số tối giản $\frac{a}{b}$, trong đó $a$ và $b$ là các số nguyên. Mọi phép toán trên phân số có thể được biểu diễn dưới dạng các phép toán trên các tử số và mẫu số nguyên của các phân số này. Thông thường, điều này yêu cầu sử dụng số học số lớn cổ điển để lưu trữ tử số và mẫu số, nhưng đôi khi kiểu dữ liệu số nguyên 64-bit có sẵn là đủ.

### Lưu trữ vị trí dấu phẩy động dưới dạng kiểu dữ liệu riêng biệt

Đôi khi một bài toán yêu cầu xử lý các số rất nhỏ hoặc rất lớn mà không để xảy ra hiện tượng tràn số (overflow) hoặc mất mát độ chính xác (underflow). Kiểu dữ liệu `double` có sẵn sử dụng 8-10 byte và cho phép giá trị số mũ nằm trong khoảng $[-308; 308]$, điều này đôi khi có thể là không đủ.

Cách tiếp cận rất đơn giản: một biến số nguyên riêng biệt được sử dụng để lưu trữ giá trị của số mũ, và sau mỗi phép toán, số dấu phẩy động sẽ được chuẩn hóa, tức là đưa về khoảng $[0.1; 1)$ bằng cách điều chỉnh số mũ tương ứng.

Khi nhân hoặc chia hai số như vậy, số mũ của chúng sẽ được cộng hoặc trừ tương ứng. Khi cộng hoặc trừ các số, trước tiên chúng phải được đưa về cùng một số mũ bằng cách nhân một trong hai số với 10 lũy thừa hiệu của các số mũ.

Một lưu ý cuối cùng là cơ số của số mũ không nhất thiết phải bằng 10. Dựa trên biểu diễn nội bộ của số dấu phẩy động, việc sử dụng 2 làm cơ số số mũ là hợp lý nhất.

## Bài tập luyện tập

* [UVA - How Many Fibs?](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1124)
* [UVA - Product](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1047)
* [UVA - Maximum Sub-sequence Product](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=728)
* [SPOJ - Fast Multiplication](http://www.spoj.com/problems/MUL/en/)
* [SPOJ - GCD2](http://www.spoj.com/problems/GCD2/)
* [UVA - Division](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1024)
* [UVA - Fibonacci Freeze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=436)
* [UVA - Krakovia](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1866)
* [UVA - Simplifying Fractions](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1755)
* [UVA - 500!](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=564)
* [Hackerrank - Factorial digit sum](https://www.hackerrank.com/contests/projecteuler/challenges/euler020/problem)
* [UVA - Immortal Rabbits](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4803)
* [SPOJ - 0110SS](http://www.spoj.com/problems/IWGBS/)
* [Codeforces - Notepad](http://codeforces.com/contest/17/problem/D)
