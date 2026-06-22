---
tags:
  - Original
lang: vi
---
# Bảng thưa (Sparse Table)

Bảng thưa (Sparse Table) là một cấu trúc dữ liệu, cho phép trả lời các truy vấn đoạn (range queries).
Nó có thể trả lời hầu hết các truy vấn đoạn trong $O(\log n)$, nhưng sức mạnh thực sự của nó nằm ở việc trả lời các truy vấn giá trị nhỏ nhất trên đoạn (range minimum queries - RMQ) (hoặc truy vấn giá trị lớn nhất trên đoạn tương đương).
Đối với các truy vấn đó, nó có thể tính toán câu trả lời trong thời gian $O(1)$.

Nhược điểm duy nhất của cấu trúc dữ liệu này là nó chỉ có thể được sử dụng trên các mảng _bất biến_ (immutable arrays).
Điều này có nghĩa là mảng không thể thay đổi giữa hai truy vấn.
Nếu bất kỳ phần tử nào trong mảng thay đổi, toàn bộ cấu trúc dữ liệu phải được tính toán lại.

## Trực giác (Intuition)

Bất kỳ số không âm nào cũng có thể được biểu diễn duy nhất dưới dạng tổng các lũy thừa giảm dần của hai.
Đây chỉ là một biến thể của biểu diễn nhị phân của một số.
Ví dụ: $13 = (1101)_2 = 8 + 4 + 1$.
Đối với một số $x$, có thể có tối đa $\lceil \log_2 x \rceil$ số hạng.

Theo cùng lý luận này, bất kỳ khoảng nào (interval) cũng có thể được biểu diễn duy nhất dưới dạng hợp (union) của các khoảng có chiều dài là các lũy thừa giảm dần của hai.
Ví dụ: $[2, 14] = [2, 9] \cup [10, 13] \cup [14, 14]$, trong đó khoảng đầy đủ có chiều dài 13, và các khoảng riêng lẻ có chiều dài lần lượt là 8, 4 và 1.
Và ở đây, hợp của chúng cũng bao gồm tối đa $\lceil \log_2(\text{length of interval}) \rceil$ khoảng.

Ý tưởng chính đằng sau Bảng thưa (Sparse Table) là tính toán trước (precompute) tất cả các câu trả lời cho các truy vấn đoạn với chiều dài là lũy thừa của hai.
Sau đó, một truy vấn đoạn khác có thể được trả lời bằng cách chia đoạn đó thành các đoạn có chiều dài là lũy thừa của hai, tra cứu các câu trả lời đã tính toán trước, và kết hợp chúng để nhận được câu trả lời hoàn chỉnh.

## Tiền xử lý (Precomputation)

Chúng ta sẽ sử dụng một mảng 2 chiều để lưu trữ các câu trả lời cho các truy vấn đã được tính toán trước.
$\text{st}[i][j]$ sẽ lưu trữ câu trả lời cho đoạn $[j, j + 2^i - 1]$ có chiều dài $2^i$.
Kích thước của mảng 2 chiều sẽ là $(K + 1) \times \text{MAXN}$, trong đó $\text{MAXN}$ là chiều dài mảng lớn nhất có thể.
$\text{K}$ phải thỏa mãn $\text{K} \ge \lfloor \log_2 \text{MAXN} \rfloor$, bởi vì $2^{\lfloor \log_2 \text{MAXN} \rfloor}$ là đoạn có chiều dài là lũy thừa lớn nhất của hai mà chúng ta phải hỗ trợ.
Đối với các mảng có chiều dài hợp lý ($\le 10^7$ phần tử), $K = 25$ là một giá trị tốt.

Chiều $\text{MAXN}$ là chiều thứ hai để cho phép truy cập bộ nhớ liên tiếp (thân thiện với bộ nhớ cache).

```{.cpp file=sparsetable_definition}
int st[K + 1][MAXN];
```

Vì đoạn $[j, j + 2^i - 1]$ có chiều dài $2^i$ chia đẹp thành hai đoạn $[j, j + 2^{i - 1} - 1]$ và $[j + 2^{i - 1}, j + 2^i - 1]$, cả hai đều có chiều dài $2^{i - 1}$, chúng ta có thể tạo bảng một cách hiệu quả bằng cách sử dụng quy hoạch động (Dynamic Programming):

```{.cpp file=sparsetable_generation}
std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = f(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);
```

Hàm $f$ sẽ phụ thuộc vào loại truy vấn.
Đối với truy vấn tổng đoạn, nó sẽ tính tổng; đối với truy vấn giá trị nhỏ nhất trên đoạn, nó sẽ tính giá trị nhỏ nhất.

Độ phức tạp thời gian (Time Complexity) của quá trình tiền xử lý là $O(\text{N} \log \text{N})$.

## Truy vấn tổng đoạn (Range Sum Queries)

Đối với loại truy vấn này, chúng ta muốn tìm tổng của tất cả các giá trị trong một đoạn.
Do đó, định nghĩa tự nhiên của hàm $f$ là $f(x, y) = x + y$.
Chúng ta có thể xây dựng cấu trúc dữ liệu với:

```{.cpp file=sparsetable_sum_generation}
long long st[K + 1][MAXN];

std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = st[i - 1][j] + st[i - 1][j + (1 << (i - 1))];
```

Để trả lời truy vấn tổng cho đoạn $[L, R]$, chúng ta lặp qua tất cả các lũy thừa của hai, bắt đầu từ lũy thừa lớn nhất.
Ngay khi một lũy thừa của hai $2^i$ nhỏ hơn hoặc bằng chiều dài của đoạn ($= R - L + 1$), chúng ta xử lý phần đầu tiên của đoạn $[L, L + 2^i - 1]$, và tiếp tục với đoạn còn lại $[L + 2^i, R]$.

```{.cpp file=sparsetable_sum_query}
long long sum = 0;
for (int i = K; i >= 0; i--) {
    if ((1 << i) <= R - L + 1) {
        sum += st[i][L];
        L += 1 << i;
    }
}
```

Độ phức tạp thời gian cho một truy vấn tổng đoạn là $O(K) = O(\log \text{MAXN})$.

## Truy vấn giá trị nhỏ nhất trên đoạn (RMQ - Range Minimum Queries)

Đây là những truy vấn mà Bảng thưa (Sparse Table) phát huy tác dụng.
Khi tính giá trị nhỏ nhất của một đoạn, việc chúng ta xử lý một giá trị trong đoạn một lần hay hai lần không quan trọng.
Do đó, thay vì chia một đoạn thành nhiều đoạn, chúng ta cũng có thể chia đoạn đó thành chỉ hai đoạn chồng chéo có chiều dài là lũy thừa của hai.
Ví dụ: chúng ta có thể chia đoạn $[1, 6]$ thành các đoạn $[1, 4]$ và $[3, 6]$.
Giá trị nhỏ nhất trên đoạn của $[1, 6]$ rõ ràng giống với giá trị nhỏ nhất của giá trị nhỏ nhất trên đoạn của $[1, 4]$ và giá trị nhỏ nhất trên đoạn của $[3, 6]$.
Vì vậy chúng ta có thể tính giá trị nhỏ nhất của đoạn $[L, R]$ với:

$$\min(\text{st}[i][L], \text{st}[i][R - 2^i + 1]) \quad \text{ where } i = \log_2(R - L + 1)$$

Điều này yêu cầu chúng ta có thể tính $\log_2(R - L + 1)$ một cách nhanh chóng.
Bạn có thể đạt được điều đó bằng cách tính toán trước tất cả các logarit:

```{.cpp file=sparse_table_log_table}
int lg[MAXN+1];
lg[1] = 0;
for (int i = 2; i <= MAXN; i++)
    lg[i] = lg[i/2] + 1;
```
Ngoài ra, logarit có thể được tính toán trong lúc chạy với độ phức tạp bộ nhớ (Space Complexity) và thời gian (Time Complexity) không đổi:
```c++
// C++20
#include <bit>
int log2_floor(unsigned long i) {
    return std::bit_width(i) - 1;
}

// pre C++20
int log2_floor(unsigned long long i) {
    return i ? __builtin_clzll(1) - __builtin_clzll(i) : -1;
}
```
[Thử nghiệm hiệu năng này](https://quick-bench.com/q/Zghbdj_TEkmw4XG2nqOpD3tsJ8U) cho thấy việc sử dụng mảng `lg` chậm hơn do lỗi cache (cache misses).

Sau đó, chúng ta cần tính toán trước cấu trúc Bảng thưa (Sparse Table). Lần này chúng ta định nghĩa $f$ với $f(x, y) = \min(x, y)$.

```{.cpp file=sparse_table_minimum_generation}
int st[K + 1][MAXN];

std::copy(array.begin(), array.end(), st[0]);

for (int i = 1; i <= K; i++)
    for (int j = 0; j + (1 << i) <= N; j++)
        st[i][j] = min(st[i - 1][j], st[i - 1][j + (1 << (i - 1))]);
```

Và giá trị nhỏ nhất của một đoạn $[L, R]$ có thể được tính toán với:

```{.cpp file=sparse_table_minimum_query}
int i = lg[R - L + 1];
int minimum = min(st[i][L], st[i][R - (1 << i) + 1]);
```

Độ phức tạp thời gian cho một truy vấn giá trị nhỏ nhất trên đoạn (RMQ) là $O(1)$.

## Các cấu trúc dữ liệu tương tự hỗ trợ nhiều loại truy vấn hơn

Một trong những điểm yếu chính của phương pháp $O(1)$ đã thảo luận trong phần trước là, phương pháp này chỉ hỗ trợ các truy vấn của các [hàm lũy đẳng](https://en.wikipedia.org/wiki/Idempotence) (idempotent functions).
Tức là, nó hoạt động rất tốt cho các truy vấn giá trị nhỏ nhất trên đoạn, nhưng không thể trả lời các truy vấn tổng đoạn bằng cách tiếp cận này.

Có những cấu trúc dữ liệu tương tự có thể xử lý bất kỳ loại hàm kết hợp (associative functions) nào và trả lời các truy vấn đoạn trong $O(1)$.
Một trong số đó được gọi là [Bảng thưa rời rạc](https://discuss.codechef.com/questions/117696/tutorial-disjoint-sparse-table) (Disjoint Sparse Table).
Một cái khác là [Cây căn](sqrt-tree.md) (Sqrt Tree).

## Bài tập thực hành

*   [SPOJ - RMQSQ](http://www.spoj.com/problems/RMQSQ/)
*   [SPOJ - THRBL](http://www.spoj.com/problems/THRBL/)
*   [Codechef - MSTICK](https://www.codechef.com/problems/MSTICK)
*   [Codechef - SEAD](https://www.codechef.com/problems/SEAD)
*   [Codeforces - CGCDSSQ](http://codeforces.com/contest/475/problem/D)
*   [Codeforces - R2D2 và Đội quân Droid](http://codeforces.com/problemset/problem/514/D)
*   [Codeforces - Giá trị lớn nhất của các giá trị lớn nhất của các giá trị nhỏ nhất](http://codeforces.com/problemset/problem/872/B)
*   [SPOJ - Miraculous](http://www.spoj.com/problems/TNVFC1M/)
*   [DevSkill - Khoảng nhân (đã lưu trữ)](http://web.archive.org/web/20200922003506/https://devskill.com/CodingProblems/ViewProblem/19)
*   [Codeforces - Động vật và Câu đố](http://codeforces.com/contest/713/problem/D)
*   [Codeforces - Xe lửa và Thống kê](http://codeforces.com/contest/675/problem/E)
*   [SPOJ - Postering](http://www.spoj.com/problems/POSTERIN/)
*   [SPOJ - Điểm âm](http://www.spoj.com/problems/RPLN/)
*   [SPOJ - Một thành phố nổi tiếng](http://www.spoj.com/problems/CITY2/)
*   [SPOJ - Diferencija](http://www.spoj.com/problems/DIFERENC/)
*   [Codeforces - Tắt TV](http://codeforces.com/contest/863/problem/E)
*   [Codeforces - Bản đồ](http://codeforces.com/contest/15/problem/D)
*   [Codeforces - Giải thưởng cho thí sinh](http://codeforces.com/contest/873/problem/E)
*   [Codeforces - Dãy ngoặc đều dài nhất](http://codeforces.com/contest/5/problem/C)
*   [CSES - Truy vấn giá trị nhỏ nhất trên đoạn tĩnh](https://cses.fi/problemset/task/1647)
*   [Codeforces - Ổn định mảng (phiên bản GCD)](http://codeforces.com/problemset/problem/1547/F)