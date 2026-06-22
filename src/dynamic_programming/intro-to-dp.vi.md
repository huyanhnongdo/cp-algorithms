---
tags:
  - Original
lang: vi
---

# Giới thiệu về Quy hoạch động (Dynamic Programming)

Bản chất của quy hoạch động (Dynamic Programming - DP) là tránh việc tính toán lặp lại. Thông thường, các bài toán quy hoạch động có thể được giải quyết một cách tự nhiên bằng đệ quy. Trong những trường hợp như vậy, cách dễ nhất là viết một hàm đệ quy, sau đó lưu lại kết quả của các trạng thái đã tính vào một bảng tra cứu (lookup table). Quá trình này được gọi là quy hoạch động từ trên xuống với kỹ thuật ghi nhớ (**top-down dynamic programming with memoization**). Từ này được đọc là "memoization" (như thể ghi chép vào một cuốn sổ tay) chứ không phải là "memorization" (học thuộc lòng).

Một trong những ví dụ cơ bản và cổ điển nhất minh họa cho quá trình này là dãy số Fibonacci. Công thức truy hồi của nó là $f(n) = f(n-1) + f(n-2)$ với $n \ge 2$, $f(0)=0$ và $f(1)=1$. Trong C++, chúng ta có thể biểu diễn nó như sau:

```cpp
int f(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return f(n - 1) + f(n - 2);
}
```

Thời gian chạy của hàm đệ quy này là hàm mũ - xấp xỉ $O(2^n)$ vì một lời gọi hàm ( $f(n)$ ) sẽ dẫn đến 2 lời gọi hàm có kích thước tương tự ($f(n-1)$ và $f(n-2)$).

## Tăng tốc tính Fibonacci bằng Quy hoạch động (Memoization)

Hàm đệ quy hiện tại của chúng ta giải bài toán Fibonacci trong thời gian hàm mũ. Điều này có nghĩa là chúng ta chỉ có thể xử lý các giá trị đầu vào rất nhỏ trước khi bài toán trở nên quá phức tạp để tính toán. Ví dụ, lời gọi $f(29)$ sẽ sinh ra *hơn 1 triệu* lời gọi hàm!

Để tăng tốc độ, ta nhận thấy rằng số lượng bài toán con (subproblem) thực chất chỉ là $O(n)$. Nghĩa là để tính $f(n)$, chúng ta chỉ cần biết các giá trị $f(n-1), f(n-2), \dots, f(0)$. Do đó, thay vì phải tính lại các bài toán con này nhiều lần, ta giải chúng duy nhất một lần rồi lưu kết quả vào một bảng tra cứu. Các lời gọi sau đó sẽ sử dụng bảng tra cứu này và lập tức trả về kết quả, từ đó loại bỏ hoàn toàn việc tính toán trùng lặp!

Mỗi lời gọi đệ quy sẽ kiểm tra bảng tra cứu để xem giá trị đó đã được tính chưa trong thời gian $O(1)$. Nếu giá trị đã được tính từ trước, ta chỉ cần trả về kết quả; nếu chưa, ta thực hiện tính toán bình thường. Tổng thời gian chạy lúc này là $O(n)$. Đây là một sự cải tiến vượt bậc so với thuật toán thời gian hàm mũ trước đó!

```cpp
const int MAXN = 100;
bool found[MAXN];
int memo[MAXN];

int f(int n) {
    if (found[n]) return memo[n];
    if (n == 0) return 0;
    if (n == 1) return 1;

    found[n] = true;
    return memo[n] = f(n - 1) + f(n - 2);
}
```

Với hàm đệ quy có ghi nhớ mới này, phép tính $f(29)$ vốn từng sinh ra *hơn 1 triệu lời gọi hàm*, giờ đây chỉ sinh ra *đúng 57* lời gọi, giảm đi gần *20,000 lần*! Tuy nhiên, lúc này chúng ta lại bị giới hạn bởi giới hạn của kiểu dữ liệu. $f(46)$ là số Fibonacci lớn nhất có thể lưu trữ vừa trong kiểu số nguyên có dấu 32-bit (signed 32-bit integer).

Thông thường, ta cố gắng lưu trữ trạng thái trong các mảng nếu có thể, vì thời gian tra cứu mảng là $O(1)$ với chi phí phụ cực nhỏ. Tuy nhiên, một cách tổng quát hơn, ta có thể lưu trữ trạng thái bằng bất kỳ cách nào tùy ý. Các ví dụ khác bao gồm cây tìm kiếm nhị phân (`map` trong C++) hoặc bảng băm (`unordered_map` trong C++).

Một ví dụ cài đặt có thể là:

```cpp
unordered_map<int, int> memo;
int f(int n) {
    if (memo.count(n)) return memo[n];
    if (n == 0) return 0;
    if (n == 1) return 1;

    return memo[n] = f(n - 1) + f(n - 2);
}
```

Hoặc tương tự:

```cpp
map<int, int> memo;
int f(int n) {
    if (memo.count(n)) return memo[n];
    if (n == 0) return 0;
    if (n == 1) return 1;

    return memo[n] = f(n - 1) + f(n - 2);
}
```

Cả hai cách trên hầu như luôn chạy chậm hơn phiên bản sử dụng mảng. Các cách lưu trữ trạng thái thay thế này chủ yếu hữu ích khi không gian trạng thái cần lưu trữ là các vector hoặc chuỗi ký tự.

Cách đơn giản nhất để phân tích thời gian chạy của một hàm đệ quy có ghi nhớ là:

$$\text{khối lượng tính toán của một bài toán con} * \text{số lượng bài toán con}$$

Việc sử dụng cây tìm kiếm nhị phân (map trong C++) để lưu trạng thái về mặt kỹ thuật sẽ cho độ phức tạp là $O(n \log n)$ do mỗi phép tra cứu và chèn mất thời gian $O(\log n)$, và với $O(n)$ bài toán con khác nhau ta có thời gian $O(n \log n)$.

Cách tiếp cận này được gọi là **từ trên xuống (top-down)**, vì ta gọi hàm với một giá trị cần truy vấn và quá trình tính toán bắt đầu đi từ đỉnh (giá trị truy vấn) xuống dưới đáy (các trường hợp cơ sở của đệ quy), đồng thời sử dụng kỹ thuật ghi nhớ để đi tắt dọc đường.

## Quy hoạch động từ dưới lên (Bottom-up)

Cho đến giờ bạn mới chỉ thấy quy hoạch động từ trên xuống với kỹ thuật ghi nhớ. Tuy nhiên, chúng ta cũng có thể giải quyết các bài toán bằng quy hoạch động từ dưới lên (**bottom-up dynamic programming**).
Từ dưới lên hoạt động hoàn toàn ngược lại so với từ trên xuống: bạn bắt đầu tính toán từ dưới đáy (các trường hợp cơ sở của đệ quy), rồi mở rộng dần lên các giá trị lớn hơn.

Để xây dựng phương pháp từ dưới lên cho số Fibonacci, ta khởi tạo các trường hợp cơ sở trong một mảng, sau đó áp dụng công thức truy hồi trực tiếp trên mảng:

```cpp
const int MAXN = 100;
int fib[MAXN];

int f(int n) {
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++) fib[i] = fib[i - 1] + fib[i - 2];

    return fib[n];
}
```

Tất nhiên, nếu viết như thế này thì có hai điểm chưa thực sự tối ưu:
Thứ nhất, chúng ta thực hiện tính toán lặp lại nếu gọi hàm nhiều hơn một lần.
Thứ hai, chúng ta chỉ cần dùng hai giá trị liền trước để tính toán phần tử hiện tại. Do đó, chúng ta có thể giảm bộ nhớ sử dụng từ $O(n)$ xuống còn $O(1)$.

Ví dụ về lời giải quy hoạch động từ dưới lên cho dãy Fibonacci sử dụng bộ nhớ $O(1)$ có thể cài đặt như sau:

```cpp
const int MAX_SAVE = 3;
int fib[MAX_SAVE];

int f(int n) {
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++)
        fib[i % MAX_SAVE] = fib[(i - 1) % MAX_SAVE] + fib[(i - 2) % MAX_SAVE];

    return fib[n % MAX_SAVE];
}
```

Lưu ý rằng chúng ta đã đổi hằng số từ `MAXN` thành `MAX_SAVE`. Điều này là do số lượng phần tử cần truy xuất tối đa tại mỗi thời điểm chỉ là 3. Nó không còn phụ thuộc vào kích thước của đầu vào, và theo định nghĩa, bộ nhớ sử dụng lúc này là $O(1)$. Ngoài ra, chúng ta sử dụng một kỹ thuật phổ biến (phép toán chia lấy dư mô-đun) để chỉ duy trì các giá trị thực sự cần thiết.

Chỉ đơn giản như vậy. Đó là kiến thức cơ bản của quy hoạch động: Không lặp lại những gì đã tính toán trước đó.

Một trong những mẹo để học quy hoạch động tốt hơn là nghiên cứu kỹ các ví dụ điển hình.

## Các bài toán quy hoạch động điển hình
| Tên bài toán                                   | Mô tả / Ví dụ                                                                                                                                                                                                                  |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Balo 0-1 (0-1 Knapsack)](../dynamic_programming/knapsack.md) | Cho $N$ đồ vật với trọng lượng $w_i$, giá trị $v_i$ và trọng lượng tối đa $W$. Giá trị lớn nhất $\sum_{i=1}^{k} v_i$ có thể lấy được là bao nhiêu đối với tập con gồm $k$ đồ vật ($1 \le k \le N$) sao cho tổng trọng lượng của chúng $\sum_{i=1}^{k} w_i \le W$? |
| Tổng tập con (Subset Sum) | Cho một tập gồm $N$ số nguyên và giá trị $T$. Hãy xác định xem có tồn tại một tập con nào có tổng các phần tử bằng $T$ hay không. |
| [Dãy con tăng dài nhất (LIS)](../dynamic_programming/longest_increasing_subsequence.md) | Cho một mảng gồm $N$ số nguyên. Hãy tìm dãy con tăng dài nhất trong mảng đó (tức là dãy con mà mỗi phần tử đều lớn hơn phần tử đứng trước nó). |
| Đếm đường đi trên lưới 2D | Cho $N$ và $M$, hãy đếm số lượng đường đi phân biệt từ ô $(1,1)$ tới $(N, M)$, biết mỗi bước đi chỉ được di chuyển từ $(i, j)$ tới $(i+1, j)$ hoặc $(i, j+1)$. |
| Dãy con chung dài nhất (LCS) | Cho hai xâu ký tự $s$ và $t$. Hãy tìm độ dài của xâu dài nhất là dãy con chung của cả $s$ và $t$. |
| Đường đi dài nhất trên đồ thị có hướng không chu trình (DAG) | Tìm đường đi có độ dài lớn nhất trên đồ thị có hướng không chu trình (DAG). |
| Dãy con đối xứng dài nhất | Tìm độ dài dãy con đối xứng dài nhất (LPS) của một xâu ký tự cho trước. |
| Bài toán cắt thanh kim loại (Rod Cutting) | Cho một thanh kim loại có độ dài $n$ đơn vị và một mảng vị trí cắt `cuts` biểu thị các điểm có thể thực hiện cắt. Chi phí của một lần cắt bằng độ dài của thanh kim loại bị cắt. Hãy tìm tổng chi phí cắt nhỏ nhất. |
| Khoảng cách biến đổi (Edit Distance) | Khoảng cách biến đổi giữa hai xâu là số lượng phép toán tối thiểu cần thực hiện để biến đổi xâu này thành xâu kia. Các phép toán được phép là ["Thêm", "Xóa", "Thay thế"]. |

## Các chủ đề liên quan
* [Quy hoạch động trạng thái / Mặt nạ bit (Bitmask DP)](../dynamic_programming/profile-dynamics.md)
* Quy hoạch động chữ số (Digit DP)
* Quy hoạch động trên cây (DP on Trees)

Tất nhiên, chìa khóa quan trọng nhất vẫn là luyện tập thường xuyên.

## Bài tập thực hành
* [LeetCode - 1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/description/)
* [LeetCode - 118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
* [LeetCode - 1025. Divisor Game](https://leetcode.com/problems/divisor-game/description/)
* [Codeforces - Vacations](https://codeforces.com/problemset/problem/699/C)
* [Codeforces - Hard problem](https://codeforces.com/problemset/problem/706/C)
* [Codeforces - Zuma](https://codeforces.com/problemset/problem/607/b)
* [LeetCode - 221. Maximal Square](https://leetcode.com/problems/maximal-square/description/)
* [LeetCode - 1039. Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/)

## Các kỳ thi DP nổi tiếng
* [Atcoder - Educational DP Contest](https://atcoder.jp/contests/dp/tasks)
* [CSES - Dynamic Programming](https://cses.fi/problemset/list/)
