---
tags:
  - Translated
lang: vi
---

# Tối ưu hóa chia để trị trong quy hoạch động (Divide and Conquer DP)

Chia để trị (Divide and Conquer) là một kỹ thuật tối ưu hóa trong quy hoạch động.

### Điều kiện áp dụng
Một số bài toán quy hoạch động có công thức truy hồi dạng sau:

$$
dp(i, j) = \min_{0 \leq k \leq j} \{ dp(i - 1, k - 1) + C(k, j) \}
$$

trong đó $C(k, j)$ là một hàm chi phí và ta coi $dp(i, j) = 0$ khi $j \lt 0$.

Giả sử $0 \leq i \lt m$ và $0 \leq j \lt n$, và việc tính toán hàm chi phí $C$ tốn thời gian $O(1)$. Khi đó, việc tính toán trực tiếp công thức truy hồi trên sẽ mất thời gian $O(m n^2)$, do có $m \times n$ trạng thái và $n$ bước chuyển trạng thái cho mỗi trạng thái.

Gọi $opt(i, j)$ là giá trị $k$ làm cực tiểu hóa biểu thức trên. Giả sử hàm chi phí thỏa mãn bất đẳng thức tứ giác (quadrangle inequality), chúng ta có thể chứng minh được rằng $opt(i, j) \leq opt(i, j + 1)$ với mọi $i, j$. Tính chất này được gọi là *tính đơn điệu* (monotonicity condition).
Khi đó, chúng ta có thể áp dụng tối ưu hóa chia để trị. Điểm chia tối ưu cho một giá trị $i$ cố định sẽ tăng dần khi $j$ tăng dần.

Điều này cho phép chúng ta tính toán tất cả các trạng thái một cách hiệu quả hơn. Giả sử chúng ta đã tính được $opt(i, j)$ cho một giá trị $i$ và $j$ cố định. Khi đó với bất kỳ $j' < j$, chúng ta biết chắc chắn rằng $opt(i, j') \leq opt(i, j)$.
Điều này nghĩa là khi tính toán $opt(i, j')$, chúng ta không cần phải duyệt qua nhiều điểm chia như trước nữa!

Để giảm thiểu thời gian chạy, chúng ta áp dụng ý tưởng chia để trị. Đầu tiên, tính $opt(i, n / 2)$. Sau đó, tính $opt(i, n / 4)$ với thông tin là nó nhỏ hơn hoặc bằng $opt(i, n / 2)$, và tính $opt(i, 3 n / 4)$ với thông tin là nó lớn hơn hoặc bằng $opt(i, n / 2)$. Bằng cách theo dõi đệ quy cận dưới và cận trên của $opt$, chúng ta đạt được thời gian chạy $O(m n \log n)$. Chi tiết cài đặt tham khảo đoạn mã bên dưới.

Để chứng minh độ phức tạp của phương pháp chia để trị này, trước tiên hãy lưu ý rằng có $O(\log n)$ tầng đệ quy. Chúng ta khẳng định rằng ở mỗi tầng, số bước tính toán thực hiện là $O(n)$. Gọi tổng độ dài của các khoảng tìm kiếm $\text{opt}$ (được ký hiệu là $optl$ và $optr$ trong mã nguồn) ở tầng thứ $k$ là $S_k$. Nhận xét rằng khi một khoảng từ tầng thứ $k$ có độ dài $x$ bị chia đôi, các khoảng con thu được có tổng độ dài tối đa là $x + 1$. Hơn nữa, ở tầng thứ $k$, có tối đa $2^k$ phép chia được thực hiện, do đó ta có $S_{k + 1} \leq S_k + 2^k$. Áp dụng quy nạp với $S_0 = n$ ta thu được công thức cho mỗi tầng $k$:

$$
S_k < n + 2^k \in O(n).
$$

Do đó, độ phức tạp của mỗi bước chia để trị là $O(n\log{n})$, và độ phức tạp tính toán cho toàn bộ quy hoạch động là $O(mn\log{n})$.

## Cài đặt tổng quát

Mặc dù việc cài đặt cụ thể sẽ khác nhau tùy thuộc vào từng bài toán, dưới đây là một mẫu cài đặt khá tổng quát.
Hàm `compute` tính toán một hàng trạng thái $i$ (`dp_cur`) dựa trên hàng trạng thái trước đó $i-1$ (`dp_before`).
Hàm cần được gọi với tham số `compute(0, n-1, 0, n-1)`. Hàm `solve` thực hiện tính toán qua `m` hàng và trả về kết quả cuối cùng.

```{.cpp file=divide_and_conquer_dp}
int m, n;
vector<long long> dp_before, dp_cur;

long long C(int i, int j);

// compute dp_cur[l], ... dp_cur[r] (inclusive)
void compute(int l, int r, int optl, int optr) {
    if (l > r)
        return;

    int mid = (l + r) >> 1;
    pair<long long, int> best = {LLONG_MAX, -1};

    for (int k = optl; k <= min(mid, optr); k++) {
        best = min(best, {(k ? dp_before[k - 1] : 0) + C(k, mid), k});
    }

    dp_cur[mid] = best.first;
    int opt = best.second;

    compute(l, mid - 1, optl, opt);
    compute(mid + 1, r, opt, optr);
}

long long solve() {
    dp_before.assign(n,0);
    dp_cur.assign(n,0);

    for (int i = 0; i < n; i++)
        dp_before[i] = C(0, i);

    for (int i = 1; i < m; i++) {
        compute(0, n - 1, 0, n - 1);
        dp_before = dp_cur;
    }

    return dp_before[n - 1];
}
```

### Điểm cần lưu ý

Khó khăn lớn nhất đối với các bài toán Quy hoạch động chia để trị là chứng minh tính đơn điệu của $opt$. Một trường hợp đặc biệt mà tính chất này luôn đúng là khi hàm chi phí thỏa mãn bất đẳng thức tứ giác, tức là: $C(a, c) + C(b, d) \le C(a, d) + C(b, c)$ với mọi $a \le b \le c \le d$.
Nhiều bài toán quy hoạch động chia để trị cũng có thể giải quyết bằng kỹ thuật Bao lồi (Convex Hull trick) hoặc ngược lại. Việc nắm vững và hiểu rõ cả hai kỹ thuật này là rất hữu ích!

## Bài tập áp dụng
- [AtCoder - Yakiniku Restaurants](https://atcoder.jp/contests/arc067/tasks/arc067_d)
- [CodeForces - Ciel and Gondolas](https://codeforces.com/contest/321/problem/E) (Chú ý thao tác nhập/xuất để tránh quá thời gian!)
- [CodeForces - Levels And Regions](https://codeforces.com/problemset/problem/673/E)
- [CodeForces - Partition Game](https://codeforces.com/contest/1527/problem/E)
- [CodeForces - The Bakery](https://codeforces.com/problemset/problem/834/D)
- [CodeForces - Yet Another Minimization Problem](https://codeforces.com/contest/868/problem/F)
- [Codechef - CHEFAOR](https://www.codechef.com/problems/CHEFAOR)
- [CodeForces - GUARDS](https://codeforces.com/gym/103536/problem/A) (Đây là bài toán được đề cập trực tiếp trong bài viết này.)
- [Hackerrank - Guardians of the Lunatics](https://www.hackerrank.com/contests/ioi-2014-practice-contest-2/challenges/guardians-lunatics-ioi14)
- [Hackerrank - Mining](https://www.hackerrank.com/contests/world-codesprint-5/challenges/mining)
- [Kattis - Money (ACM ICPC World Finals 2017)](https://open.kattis.com/problems/money)
- [SPOJ - ADAMOLD](https://www.spoj.com/problems/ADAMOLD/)
- [SPOJ - LARMY](https://www.spoj.com/problems/LARMY/)
- [SPOJ - NKLEAVES](https://www.spoj.com/problems/NKLEAVES/)
- [Timus - Bicolored Horses](https://acm.timus.ru/problem.aspx?space=1&num=1167)
- [USACO - Circular Barn](https://usaco.org/index.php?page=viewproblem2&cpid=626)
- [UVA - Arranging Heaps](https://onlinejudge.org/external/125/12524.pdf)
- [UVA - Naming Babies](https://onlinejudge.org/external/125/12594.pdf)

## Tài liệu tham khảo
- [Câu trả lời trên Quora của Michael Levin](https://www.quora.com/What-is-divide-and-conquer-optimization-in-dynamic-programming)
- [Video hướng dẫn của "Sothe" the Algorithm Wolf](https://www.youtube.com/watch?v=wLXEWuDWnzI)
