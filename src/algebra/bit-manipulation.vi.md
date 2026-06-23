---
tags:
  - Translated
---
# Thao tác bit

## Số nhị phân

Một **số nhị phân (binary number)** là một số được biểu diễn trong hệ cơ số 2. Đây là một phương pháp biểu diễn toán học chỉ sử dụng hai ký hiệu: thường là "0" (không) và "1" (một).

Chúng ta nói rằng một bit nào đó được **bật (set)** nếu nó có giá trị là 1, và được **tắt/xóa (cleared)** nếu nó có giá trị là 0.

Số nhị phân $(a_k a_{k-1} \dots a_1 a_0)_2$ biểu diễn số:

$$(a_k a_{k-1} \dots a_1 a_0)_2 = a_k \cdot 2^k + a_{k-1} \cdot 2^{k-1} + \dots + a_1 \cdot 2^1 + a_0 \cdot 2^0.$$

Ví dụ, số nhị phân $1101_2$ biểu diễn số $13$:

$$\begin{align}
1101_2 &= 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 \\
       &= 1\cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 13
\end{align}$$

Máy tính biểu diễn các số nguyên dưới dạng số nhị phân.
Các số nguyên dương (cả có dấu và không dấu) được biểu diễn trực tiếp bằng các chữ số nhị phân của chúng, còn các số nguyên âm có dấu thường được biểu diễn dưới dạng [số bù hai (Two's complement)](https://en.wikipedia.org/wiki/Two%27s_complement).

```cpp
unsigned int unsigned_number = 13;
assert(unsigned_number == 0b1101);

int positive_signed_number = 13;
assert(positive_signed_number == 0b1101);

int negative_signed_number = -13;
assert(negative_signed_number == 0b1111'1111'1111'1111'1111'1111'1111'0011);
```

Bộ vi xử lý (CPU) có thể thao tác trên các bit này cực kỳ nhanh chóng bằng các lệnh chuyên dụng.
Đối với một số bài toán, chúng ta có thể tận dụng biểu diễn số nhị phân này để tăng tốc độ chạy chương trình.
Và đối với một số bài toán (thường là trong tổ hợp hoặc quy hoạch động) cần theo dõi xem những đối tượng nào đã được chọn từ một tập hợp cho trước, chúng ta có thể chỉ cần sử dụng một số nguyên đủ lớn, trong đó mỗi vị trí bit biểu diễn cho một đối tượng; tùy thuộc vào việc ta chọn hay bỏ đối tượng đó mà ta bật hoặc tắt bit tương ứng.

## Các toán tử bit

Tất cả các toán tử được giới thiệu dưới đây đều chạy tức thời (tốc độ tương đương phép cộng) trên CPU đối với các số nguyên có độ dài cố định.

### Các toán tử bitwise

-   $\&$ : Toán tử AND bitwise so sánh từng bit của toán hạng thứ nhất với bit tương ứng của toán hạng thứ hai.
    Nếu cả hai bit đều là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.
 	
-   $|$ : Toán tử OR bitwise so sánh từng bit của toán hạng thứ nhất với bit tương ứng của toán hạng thứ hai.
    Nếu một trong hai bit là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $\wedge$ : Toán tử XOR bitwise so sánh từng bit của toán hạng thứ nhất với bit tương ứng của toán hạng thứ hai.
    Nếu một bit là 0 và bit kia là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $\sim$ : Toán tử NOT bitwise đảo ngược từng bit của một số. Nếu bit đang bật, toán tử này sẽ tắt nó đi; nếu bit đang tắt, toán tử này sẽ bật nó lên.

Ví dụ:

```
n         = 01011000
n-1       = 01010111
--------------------
n & (n-1) = 01010000
```

```
n         = 01011000
n-1       = 01010111
--------------------
n | (n-1) = 01011111
```

```
n         = 01011000
n-1       = 01010111
--------------------
n ^ (n-1) = 00001111
```

```
n         = 01011000
--------------------
~n        = 10100111
```

### Các toán tử dịch bit

Có hai toán tử dùng để dịch chuyển các bit.

-   $\gg$ Dịch chuyển một số sang phải bằng cách loại bỏ một số chữ số nhị phân ở cuối số đó.
    Mỗi lần dịch chuyển đi 1 bit tương đương với một phép chia nguyên cho 2, do đó dịch phải $k$ bit tương đương với phép chia nguyên cho $2^k$.

    Ví dụ: $5 \gg 2 = 101_2 \gg 2 = 1_2 = 1$, tương đương với $\frac{5}{2^2} = \frac{5}{4} = 1$.
    Đối với máy tính, phép dịch bit chạy nhanh hơn phép chia rất nhiều.

-   $\ll$ Dịch chuyển một số sang trái bằng cách thêm các chữ số 0 vào cuối.
    Tương tự như dịch phải, phép dịch trái $k$ bit tương đương với phép nhân với $2^k$.

    Ví dụ: $5 \ll 3 = 101_2 \ll 3 = 101000_2 = 40$, tương đương với $5 \cdot 2^3 = 5 \cdot 8 = 40$.

    Tuy nhiên, lưu ý rằng đối với số nguyên có độ dài cố định, việc dịch trái sẽ làm mất đi các chữ số ở phía bên trái ngoài cùng, và nếu dịch chuyển quá nhiều, bạn sẽ thu được kết quả là số 0.

## Các mẹo hữu ích

### Bật / đảo / tắt một bit

Sử dụng phép dịch bit và một số phép toán bit cơ bản, chúng ta có thể dễ dàng bật, đảo hoặc tắt một bit bất kỳ.
$1 \ll x$ là số chỉ có bit thứ $x$ được bật, trong khi $\sim(1 \ll x)$ là số có tất cả các bit được bật ngoại trừ bit thứ $x$.

- $n ~|~ (1 \ll x)$ bật bit thứ $x$ của số $n$
- $n ~\wedge~ (1 \ll x)$ đảo bit thứ $x$ của số $n$
- $n ~\&~ \sim(1 \ll x)$ tắt bit thứ $x$ của số $n$

### Kiểm tra một bit có được bật hay không

Giá trị của bit thứ $x$ có thể được kiểm tra bằng cách dịch số đó sang phải $x$ vị trí, đưa bit thứ $x$ về vị trí hàng đơn vị, sau đó thực hiện phép AND bitwise với 1.

``` cpp
bool is_set(unsigned int number, int x) {
    return (number >> x) & 1;
}
```

### Kiểm tra một số có chia hết cho một lũy thừa của 2 hay không

Sử dụng phép toán AND, chúng ta có thể kiểm tra một số $n$ có phải là số chẵn hay không vì $n ~\&~ 1 = 0$ nếu $n$ chẵn, và $n ~\&~ 1 = 1$ nếu $n$ lẻ.
Tổng quát hơn, $n$ chia hết cho $2^{k}$ khi và chỉ khi $n ~\&~ (2^{k} − 1) = 0$.

``` cpp
bool isDivisibleByPowerOf2(int n, int k) {
    int powerOf2 = 1 << k;
    return (n & (powerOf2 - 1)) == 0;
}
```

Chúng ta có thể tính $2^{k}$ bằng cách dịch trái 1 đi $k$ vị trí.
Mẹo này hoạt động vì $2^k - 1$ là một số gồm chính xác $k$ chữ số 1 ở cuối.
Và một số chia hết cho $2^k$ phải có các chữ số 0 ở các vị trí này.

### Kiểm tra một số nguyên có phải là lũy thừa của 2 hay không

Một lũy thừa của hai là số chỉ có một bit duy nhất được bật (ví dụ: $32 = 0010~0000_2$), trong khi số liền trước của nó có bit đó tắt và tất cả các bit phía sau nó đều được bật ($31 = 0001~1111_2$).
Vì vậy, phép AND bitwise của một số với số liền trước nó sẽ luôn bằng 0, vì chúng không có bit bật chung nào.
Bạn có thể dễ dàng kiểm tra thấy điều này chỉ xảy ra đối với các số là lũy thừa của 2 và đối với số $0$ (số không có bit nào được bật sẵn).

``` cpp
bool isPowerOfTwo(unsigned int n) {
    return n && !(n & (n - 1));
}
```

### Tắt bit được bật ở phía ngoài cùng bên phải

Biểu thức $n ~\&~ (n-1)$ có thể được sử dụng để tắt bit được bật ở ngoài cùng bên phải của số $n$.
Điều này hoạt động vì biểu thức $n-1$ đảo ngược tất cả các bit phía sau bit bật ngoài cùng bên phải của $n$, bao gồm cả chính bit bật ngoài cùng bên phải đó.
Vì vậy, tất cả các bit này sẽ khác biệt so với số ban đầu, và khi thực hiện phép AND bitwise, chúng đều được đặt thành 0, giữ nguyên phần còn lại của số $n$ và chỉ đảo bit bật ngoài cùng bên phải.

Ví dụ, xét số $52 = 0011~0100_2$:

```
n         = 00110100
n-1       = 00110011
--------------------
n & (n-1) = 00110000
```

### Thuật toán Brian Kernighan

Chúng ta có thể đếm số lượng bit được bật bằng biểu thức trên.

Ý tưởng là chỉ xét các bit được bật của một số nguyên bằng cách tắt bit bật ngoài cùng bên phải của nó (sau khi đã đếm nó), do đó lần lặp tiếp theo của vòng lặp sẽ xét đến bit bật tiếp theo ở bên trái.

``` cpp
int countSetBits(int n)
{
    int count = 0;
    while (n)
    {
        n = n & (n - 1);
        count++;
    }
    return count;
}
```

### Đếm số lượng bit được bật từ 1 đến $n$

Để đếm số lượng bit được bật của tất cả các số từ $1$ đến $n$ (bao gồm cả $n$), chúng ta có thể chạy thuật toán Brian Kernighan cho tất cả các số đó. Tuy nhiên, cách này sẽ bị lỗi "Time Limit Exceeded" (Quá giới hạn thời gian) khi nộp bài trong các kỳ thi lập trình.

Chúng ta có thể sử dụng tính chất rằng đối với các số lên đến $2^x$ (tức là từ $1$ đến $2^x - 1$), có tổng cộng $x \cdot 2^{x-1}$ bit được bật. Điều này có thể được trực quan hóa như sau:
```
0 ->   0 0 0 0
1 ->   0 0 0 1
2 ->   0 0 1 0
3 ->   0 0 1 1
4 ->   0 1 0 0
5 ->   0 1 0 1
6 ->   0 1 1 0
7 ->   0 1 1 1
8 ->   1 0 0 0
```

Chúng ta có thể thấy rằng tất cả các cột ngoại trừ cột ngoài cùng bên trái đều có đúng $4$ (tức là $2^2$) bit được bật, nghĩa là cho đến số $2^3 - 1$, số lượng bit được bật là $3 \cdot 2^{3-1}$.

Với kiến thức mới này, chúng ta có thể đưa ra thuật toán sau:

- Tìm lũy thừa lớn nhất của $2$ nhỏ hơn hoặc bằng số đã cho. Gọi số này là $2^x$.
- Tính số lượng bit được bật từ $1$ đến $2^x - 1$ bằng công thức $x \cdot 2^{x-1}$.
- Đếm số lượng bit được bật ở vị trí bit quan trọng nhất (MSB) từ $2^x$ đến $n$ và cộng thêm vào kết quả.
- Trừ $2^x$ từ $n$ và lặp lại các bước trên với $n$ mới.

```cpp
int countSetBits(int n) {
        int count = 0;
        while (n > 0) {
            int x = std::bit_width(n) - 1;
            count += x << (x - 1);
            n -= 1 << x;
            count += n + 1;
        }
        return count;
}
```

### Các mẹo bổ sung

- $n ~\&~ (n + 1)$ tắt tất cả các bit 1 liên tiếp ở cuối: $0011~0111_2 \rightarrow 0011~0000_2$.
- $n ~|~ (n + 1)$ bật bit 0 đầu tiên tính từ bên phải: $0011~0101_2 \rightarrow 0011~0111_2$.
- $n ~\&~ -n$ trích xuất bit được bật ngoài cùng bên phải: $0011~0100_2 \rightarrow 0000~0100_2$.

Có thể tìm thấy rất nhiều mẹo khác trong cuốn sách [Hacker's Delight](https://en.wikipedia.org/wiki/Hacker%27s_Delight).

### Sự hỗ trợ từ ngôn ngữ và trình biên dịch

C++ hỗ trợ một số thao tác này kể từ phiên bản C++20 thông qua thư viện tiêu chuẩn [bit](https://en.cppreference.com/w/cpp/header/bit):

- `has_single_bit`: kiểm tra một số có phải là lũy thừa của 2 hay không
- `bit_ceil` / `bit_floor`: làm tròn lên/xuống tới lũy thừa gần nhất của 2
- `rotl` / `rotr`: xoay vòng các bit trong số
- `countl_zero` / `countr_zero` / `countl_one` / `countr_one`: đếm số lượng số 0/số 1 liên tiếp ở đầu/cuối số
- `popcount`: đếm số lượng bit được bật

Ngoài ra, một số trình biên dịch cũng cung cấp các hàm dựng sẵn (built-in functions) để làm việc với bit.
Ví dụ, GCC định nghĩa một danh sách các hàm tại [Built-in Functions Provided by GCC](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html) hoạt động cả trong các phiên bản C++ cũ hơn:

- `__builtin_popcount(unsigned int)` trả về số lượng bit được bật (`__builtin_popcount(0b0001'0010'1100) == 4`)
- `__builtin_ffs(int)` tìm vị trí của bit được bật đầu tiên (ngoài cùng bên phải) (`__builtin_ffs(0b0001'0010'1100) == 3`)
- `__builtin_clz(unsigned int)` đếm số lượng chữ số 0 ở đầu (`__builtin_clz(0b0001'0010'1100) == 23`)
- `__builtin_ctz(unsigned int)` đếm số lượng chữ số 0 ở cuối (`__builtin_ctz(0b0001'0010'1100) == 2`)
- ` __builtin_parity(x)` tính tính chẵn lẻ (chẵn hay lẻ) của số lượng số 1 trong biểu diễn nhị phân

_Lưu ý rằng một số phép toán (cả các hàm C++20 và các hàm dựng sẵn của trình biên dịch) có thể chạy khá chậm trong GCC nếu bạn không bật mục tiêu trình biên dịch cụ thể với chỉ thị `#pragma GCC target("popcnt")`._

## Bài tập luyện tập

* [Codeforces - Raising Bacteria](https://codeforces.com/problemset/problem/579/A)
* [Codeforces - Fedor and New Game](https://codeforces.com/problemset/problem/467/B)
* [Codeforces - And Then There Were K](https://codeforces.com/problemset/problem/1527/A)
