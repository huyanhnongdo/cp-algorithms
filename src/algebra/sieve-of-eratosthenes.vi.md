---
tags:
  - Translated
e_maxx_link: eratosthenes_sieve
lang: vi
---

# Sàng Eratosthenes

Sàng Eratosthenes là một thuật toán dùng để tìm tất cả các số nguyên tố trong đoạn $[1; n]$ sử dụng $O(n \log \log n)$ phép toán.

Thuật toán này rất đơn giản:
đầu tiên chúng ta viết ra tất cả các số từ 2 đến $n$.
Chúng ta đánh dấu tất cả các bội số thực sự của 2 (vì 2 là số nguyên tố nhỏ nhất) là hợp số.
Một bội số thực sự của số $x$ là một số lớn hơn $x$ và chia hết cho $x$.
Sau đó, chúng ta tìm số tiếp theo chưa bị đánh dấu là hợp số, trong trường hợp này là 3.
Điều này có nghĩa là 3 là số nguyên tố, và chúng ta đánh dấu tất cả các bội số thực sự của 3 là hợp số.
Số tiếp theo chưa được đánh dấu là 5, đó là số nguyên tố tiếp theo, và chúng ta đánh dấu tất cả các bội số thực sự của nó.
Và chúng ta tiếp tục quy trình này cho đến khi xử lý hết tất cả các số trong dãy.

Trong hình ảnh dưới đây, bạn có thể thấy minh họa của thuật toán để tính tất cả các số nguyên tố trong phạm vi $[1; 16]$. Có thể thấy rằng khá thường xuyên chúng ta đánh dấu một số là hợp số nhiều lần.

<div style="text-align: center;">
  <img src="sieve_eratosthenes.png" alt="Sàng Eratosthenes">
</div>

Ý tưởng cốt lõi là:
Một số là số nguyên tố nếu không có số nguyên tố nhỏ hơn nào chia hết nó.
Vì chúng ta duyệt qua các số nguyên tố theo thứ tự, chúng ta đã đánh dấu tất cả các số chia hết cho ít nhất một trong các số nguyên tố trước đó là hợp số.
Do đó, nếu chúng ta đi tới một ô và nó chưa được đánh dấu, thì nó không chia hết cho bất kỳ số nguyên tố nhỏ hơn nào và vì vậy nó phải là số nguyên tố.

## Cài đặt

```cpp
int n;
vector<bool> is_prime(n+1, true);
is_prime[0] = is_prime[1] = false;
for (int i = 2; i <= n; i++) {
    if (is_prime[i] && (long long)i * i <= n) {
        for (int j = i * i; j <= n; j += i)
            is_prime[j] = false;
    }
}
```

Đoạn mã này đầu tiên đánh dấu tất cả các số ngoại trừ 0 và 1 là số nguyên tố tiềm năng, sau đó bắt đầu quá trình sàng lọc các hợp số.
Để làm điều này, nó duyệt qua tất cả các số từ $2$ đến $n$.
Nếu số hiện tại $i$ là số nguyên tố, nó đánh dấu tất cả các số là bội của $i$ là hợp số, bắt đầu từ $i^2$.
Đây đã là một sự tối ưu so với cách cài đặt ngây thơ, và hoàn toàn hợp lệ vì tất cả các số nhỏ hơn là bội của $i$ chắc chắn cũng có một ước nguyên tố nhỏ hơn $i$, vì vậy tất cả chúng đều đã được sàng lọc từ trước.
Vì $i^2$ có thể dễ dàng bị tràn kiểu dữ liệu `int`, việc xác thực bổ sung được thực hiện bằng cách ép kiểu sang `long long` trước khi chạy vòng lặp lồng nhau thứ hai.

Với cài đặt như vậy, thuật toán tiêu tốn $O(n)$ bộ nhớ (hiển nhiên) và thực hiện $O(n \log \log n)$ phép toán (xem phần tiếp theo).

## Phân tích độ phức tạp thuật toán

Rất dễ dàng để chứng minh thời gian chạy là $O(n \log n)$ mà không cần biết bất kỳ điều gì về phân phối của các số nguyên tố - bỏ qua bước kiểm tra `is_prime`, vòng lặp bên trong chạy (tối đa) $n/i$ lần với $i = 2, 3, 4, \dots$, dẫn đến tổng số phép toán trong vòng lặp bên trong là một tổng điều hòa (harmonic sum) có dạng $n(1/2 + 1/3 + 1/4 + \cdots)$, được giới hạn bởi $O(n \log n)$.

Chúng ta hãy chứng minh rằng thời gian chạy của thuật toán thực tế là $O(n \log \log n)$.
Thuật toán sẽ thực hiện $\frac{n}{p}$ phép toán cho mỗi số nguyên tố $p \le n$ trong vòng lặp bên trong.
Do đó, chúng ta cần đánh giá biểu thức sau:

$$\sum_{\substack{p \le n, \\\ p \text{ prime}}} \frac n p = n \cdot \sum_{\substack{p \le n, \\\ p \text{ prime}}} \frac 1 p.$$

Hãy nhớ lại hai sự thật toán học đã biết:

  - Số lượng số nguyên tố nhỏ hơn hoặc bằng $n$ xấp xỉ bằng $\frac n {\ln n}$.
  - Số nguyên tố thứ $k$ xấp xỉ bằng $k \ln k$ (điều này được suy ra trực tiếp từ sự thật trên).

Do đó chúng ta có thể viết lại tổng theo cách sau:

$$\sum_{\substack{p \le n, \\\ p \text{ prime}}} \frac 1 p \approx \frac 1 2 + \sum_{k = 2}^{\frac n {\ln n}} \frac 1 {k \ln k}.$$

Ở đây chúng ta đã tách số nguyên tố đầu tiên là 2 ra khỏi tổng, vì $k = 1$ trong công thức xấp xỉ $k \ln k$ bằng $0$ và sẽ gây ra lỗi chia cho 0.

Bây giờ, hãy đánh giá tổng này bằng cách sử dụng tích phân của cùng một hàm số theo $k$ từ $2$ đến $\frac n {\ln n}$ (chúng ta có thể thực hiện xấp xỉ này vì thực tế tổng liên quan đến tích phân như là xấp xỉ của nó bằng phương pháp hình chữ nhật):

$$\sum_{k = 2}^{\frac n {\ln n}} \frac 1 {k \ln k} \approx \int_2^{\frac n {\ln n}} \frac 1 {k \ln k} dk.$$

Nguyên hàm của hàm số dưới dấu tích phân là $\ln \ln k$. Sử dụng phép thế và loại bỏ các hạng tử bậc thấp hơn, chúng ta thu được kết quả:

$$\int_2^{\frac n {\ln n}} \frac 1 {k \ln k} dk = \ln \ln \frac n {\ln n} - \ln \ln 2 = \ln(\ln n - \ln \ln n) - \ln \ln 2 \approx \ln \ln n.$$

Bây giờ quay lại tổng ban đầu, ta có đánh giá xấp xỉ của nó:

$$\sum_{\substack{p \le n, \\\ p\ is\ prime}} \frac n p \approx n \ln \ln n + o(n).$$

Bạn có thể tìm thấy một chứng minh chặt chẽ hơn (cho kết quả đánh giá chính xác hơn với các hằng số nhân) trong cuốn sách viết bởi Hardy & Wright "An Introduction to the Theory of Numbers" (trang 349).

## Các tối ưu hóa khác nhau cho Sàng Eratosthenes

Điểm yếu lớn nhất của thuật toán là nó "duyệt" dọc theo bộ nhớ nhiều lần, chỉ thao tác trên các phần tử riêng lẻ.
Điều này không thân thiện với bộ nhớ đệm (cache friendly).
Và vì lý do đó, hằng số ẩn trong độ phức tạp $O(n \log \log n)$ là tương đối lớn.

Bên cạnh đó, bộ nhớ tiêu thụ là một điểm nghẽn (bottleneck) lớn đối với những giá trị $n$ lớn.

Các phương pháp trình bày dưới đây cho phép chúng ta giảm số lượng phép toán được thực hiện, cũng như rút gọn đáng kể bộ nhớ tiêu thụ.

### Sàng đến căn (Sieving till root)

Rõ ràng, để tìm tất cả các số nguyên tố cho đến $n$, chỉ cần thực hiện việc sàng lọc bằng các số nguyên tố không vượt quá căn bậc hai của $n$ là đủ.

```cpp
int n;
vector<bool> is_prime(n+1, true);
is_prime[0] = is_prime[1] = false;
for (int i = 2; i * i <= n; i++) {
    if (is_prime[i]) {
        for (int j = i * i; j <= n; j += i)
            is_prime[j] = false;
    }
}
```

Sự tối ưu hóa như vậy không ảnh hưởng đến độ phức tạp thuật toán (thật vậy, bằng cách lặp lại phép chứng minh được trình bày ở trên, chúng ta thu được đánh giá $n \ln \ln \sqrt n + o(n)$, tiệm cận là tương đương theo các tính chất của logarit), mặc dù số lượng phép toán sẽ giảm đi đáng kể.

### Chỉ sàng trên các số lẻ

Vì tất cả các số chẵn (ngoại trừ 2) đều là hợp số, chúng ta có thể bỏ qua hoàn toàn việc kiểm tra các số chẵn. Thay vào đó, chúng ta chỉ cần thao tác trên các số lẻ.

Đầu tiên, điều này cho phép chúng ta giảm một nửa dung lượng bộ nhớ cần thiết. Thứ hai, nó sẽ giảm khoảng một nửa số lượng phép toán được thực hiện bởi thuật toán.

### Tiêu thụ bộ nhớ và tốc độ thực hiện phép toán

Chúng ta nên lưu ý rằng hai cài đặt trên của Sàng Eratosthenes sử dụng $n$ bit bộ nhớ bằng cách sử dụng cấu trúc dữ liệu `vector<bool>`.
`vector<bool>` không phải là một container thông thường lưu trữ một chuỗi các giá trị `bool` (như trong hầu hết các kiến trúc máy tính, một biến `bool` tốn một byte bộ nhớ).
Nó là một phiên bản tối ưu hóa bộ nhớ chuyên biệt của `vector<T>`, chỉ tiêu thụ $\frac{N}{8}$ byte bộ nhớ.

Các kiến trúc bộ xử lý hiện đại hoạt động hiệu quả hơn nhiều với byte so với bit vì chúng thường không thể truy cập trực tiếp vào từng bit.
Vì vậy, bên dưới `vector<bool>` lưu trữ các bit trong một vùng bộ nhớ liên tục lớn, truy cập bộ nhớ theo các khối vài byte, và trích xuất/thiết lập các bit bằng các phép toán bit như mặt nạ bit (bit masking) và dịch bit (bit shifting).

Do đó, có một chi phí phát sinh nhất định khi bạn đọc hoặc ghi các bit với `vector<bool>`, và khá nhiều trường hợp sử dụng `vector<char>` (tiêu thụ 1 byte cho mỗi phần tử, nên gấp 8 lần lượng bộ nhớ) lại chạy nhanh hơn.

Tuy nhiên, đối với các cài đặt đơn giản của Sàng Eratosthenes, việc sử dụng `vector<bool>` lại nhanh hơn.
Bạn bị giới hạn bởi tốc độ tải dữ liệu vào bộ nhớ đệm CPU, và do đó việc sử dụng ít bộ nhớ hơn mang lại một lợi thế lớn.
Một thử nghiệm hiệu năng (benchmark) ([link](https://gist.github.com/jakobkogler/e6359ea9ced24fe304f1a8af3c9bee0e)) cho thấy việc sử dụng `vector<bool>` nhanh hơn từ 1.4 đến 1.7 lần so với sử dụng `vector<char>`.

Các cân nhắc tương tự cũng áp dụng cho `bitset`.
Nó cũng là một cách hiệu quả để lưu trữ các bit, tương tự như `vector<bool>`, nên chỉ tốn $\frac{N}{8}$ byte bộ nhớ, nhưng chậm hơn một chút khi truy cập các phần tử.
Trong thử nghiệm hiệu năng ở trên, `bitset` hoạt động kém hơn một chút so với `vector<bool>`.
Một nhược điểm khác của `bitset` là bạn cần phải biết kích thước của nó tại thời điểm biên dịch.

### Sàng phân đoạn (Segmented Sieve)

Từ tối ưu hóa "sàng đến căn", ta thấy rằng không cần thiết phải giữ toàn bộ mảng `is_prime[1...n]` tại mọi thời điểm.
Để sàng lọc, chỉ cần giữ các số nguyên tố cho đến căn bậc hai của $n$, tức là `prime[1... sqrt(n)]`, chia toàn bộ phạm vi thành các khối (blocks), và sàng lọc từng khối riêng biệt.

Gọi $s$ là hằng số xác định kích thước của khối, khi đó chúng ta có tổng cộng $\lceil {\frac n s} \rceil$ khối, và khối $k$ ($k = 0 ... \lfloor {\frac n s} \rfloor$) chứa các số trong đoạn $[ks; ks + s - 1]$.
Chúng ta có thể xử lý các khối theo lượt, tức là với mỗi khối $k$, chúng ta sẽ duyệt qua tất cả các số nguyên tố (từ $1$ đến $\sqrt n$) và thực hiện sàng lọc bằng cách sử dụng chúng.
Cần lưu ý rằng chúng ta phải thay đổi chiến lược một chút khi xử lý các số đầu tiên: thứ nhất, tất cả các số nguyên tố từ $[1; \sqrt n]$ không được tự loại bỏ chính chúng; và thứ hai, các số $0$ và $1$ nên được đánh dấu là không phải số nguyên tố.
Khi xử lý khối cuối cùng, cũng không được quên rằng số cần thiết cuối cùng $n$ không nhất thiết phải nằm ở cuối khối.

Như đã thảo luận trước đây, cài đặt điển hình của Sàng Eratosthenes bị giới hạn bởi tốc độ tải dữ liệu vào bộ nhớ đệm CPU.
Bằng cách chia phạm vi các số nguyên tố tiềm năng $[1; n]$ thành các khối nhỏ hơn, chúng ta không bao giờ phải giữ nhiều khối trong bộ nhớ cùng một lúc, và tất cả các phép toán đều thân thiện với bộ nhớ đệm hơn nhiều.
Vì bây giờ không còn bị giới hạn bởi tốc độ bộ nhớ đệm, chúng ta có thể thay thế `vector<bool>` bằng `vector<char>` để đạt thêm hiệu năng, do bộ xử lý có thể xử lý các thao tác đọc và ghi với byte trực tiếp mà không cần phụ thuộc vào các phép toán bit để trích xuất từng bit đơn lẻ.
Thử nghiệm hiệu năng ([link](https://gist.github.com/jakobkogler/e6359ea9ced24fe304f1a8af3c9bee0e)) cho thấy việc sử dụng `vector<char>` trong tình huống này nhanh hơn khoảng 3 lần so với sử dụng `vector<bool>`.
Một lời cảnh báo: những số liệu này có thể khác biệt tùy thuộc vào kiến trúc phần cứng, trình biên dịch và các mức độ tối ưu hóa.

Dưới đây là một cài đặt đếm số lượng số nguyên tố nhỏ hơn hoặc bằng $n$ sử dụng phương pháp sàng khối (sàng phân đoạn).

```cpp
int count_primes(int n) {
    const int S = 10000;

    vector<int> primes;
    int nsqrt = sqrt(n);
    vector<char> is_prime(nsqrt + 2, true);
    for (int i = 2; i <= nsqrt; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * i; j <= nsqrt; j += i)
                is_prime[j] = false;
        }
    }

    int result = 0;
    vector<char> block(S);
    for (int k = 0; k * S <= n; k++) {
        fill(block.begin(), block.end(), true);
        int start = k * S;
        for (int p : primes) {
            int start_idx = (start + p - 1) / p;
            int j = max(start_idx, p) * p - start;
            for (; j < S; j += p)
                block[j] = false;
        }
        if (k == 0)
            block[0] = block[1] = false;
        for (int i = 0; i < S && start + i <= n; i++) {
            if (block[i])
                result++;
        }
    }
    return result;
}
```

Thời gian chạy của sàng khối là tương đương với sàng Eratosthenes thông thường (trừ khi kích thước của khối quá nhỏ), nhưng bộ nhớ cần thiết sẽ giảm xuống còn $O(\sqrt{n} + S)$ và chúng ta có hiệu năng bộ nhớ đệm tốt hơn.
Mặt khác, sẽ có một phép chia cho mỗi cặp khối và số nguyên tố trong $[1; \sqrt{n}]$, và điều đó sẽ tệ hơn nhiều đối với các kích thước khối nhỏ.
Do đó, cần giữ sự cân bằng khi lựa chọn hằng số $S$.
Chúng tôi đạt được kết quả tốt nhất với kích thước khối nằm trong khoảng $10^4$ và $10^5$.

## Tìm số nguyên tố trong đoạn

Đôi khi chúng ta cần tìm tất cả các số nguyên tố trong đoạn $[L, R]$ có kích thước nhỏ (ví dụ $R - L + 1 \approx 1e7$), trong đó $R$ có thể rất lớn (ví dụ $1e12$).

Để giải bài toán này, chúng ta có thể sử dụng ý tưởng của Sàng phân đoạn.
Chúng ta tạo trước tất cả các số nguyên tố lên tới $\sqrt R$, và sử dụng các số nguyên tố đó để đánh dấu tất cả các hợp số trong đoạn $[L, R]$.

```cpp
vector<char> segmentedSieve(long long L, long long R) {
    // generate all primes up to sqrt(R)
    long long lim = sqrt(R);
    vector<char> mark(lim + 1, false);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (!mark[i]) {
            primes.emplace_back(i);
            for (long long j = i * i; j <= lim; j += i)
                mark[j] = true;
        }
    }

    vector<char> isPrime(R - L + 1, true);
    for (long long i : primes)
        for (long long j = max(i * i, (L + i - 1) / i * i); j <= R; j += i)
            isPrime[j - L] = false;
    if (L == 1)
        isPrime[0] = false;
    return isPrime;
}
```

Độ phức tạp thời gian của cách tiếp cận này là $O((R - L + 1) \log \log (R) + \sqrt R \log \log \sqrt R)$.

Cũng có khả năng là chúng ta không cần tạo trước tất cả các số nguyên tố:

```cpp
vector<char> segmentedSieveNoPreGen(long long L, long long R) {
    vector<char> isPrime(R - L + 1, true);
    long long lim = sqrt(R);
    for (long long i = 2; i <= lim; ++i)
        for (long long j = max(i * i, (L + i - 1) / i * i); j <= R; j += i)
            isPrime[j - L] = false;
    if (L == 1)
        isPrime[0] = false;
    return isPrime;
}
```

Rõ ràng độ phức tạp sẽ kém hơn, cụ thể là $O((R - L + 1) \log (R) + \sqrt R)$. Tuy nhiên, nó vẫn chạy rất nhanh trong thực tế.

## Tinh chỉnh cho thời gian tuyến tính

Chúng ta có thể thay đổi thuật toán theo cách để nó đạt độ phức tạp thời gian tuyến tính.
Cách tiếp cận này được mô tả trong bài viết [Sàng tuyến tính](prime-sieve-linear.md).
Tuy nhiên, thuật toán đó cũng có những điểm yếu riêng.

## Bài tập thực hành

* [Leetcode - Four Divisors](https://leetcode.com/problems/four-divisors/)
* [Leetcode - Count Primes](https://leetcode.com/problems/count-primes/)
* [SPOJ - Printing Some Primes](http://www.spoj.com/problems/TDPRIMES/)
* [SPOJ - A Conjecture of Paul Erdos](http://www.spoj.com/problems/HS08PAUL/)
* [SPOJ - Primal Fear](http://www.spoj.com/problems/VECTAR8/)
* [SPOJ - Primes Triangle (I)](http://www.spoj.com/problems/PTRI/)
* [Codeforces - Almost Prime](http://codeforces.com/contest/26/problem/A)
* [Codeforces - Sherlock And His Girlfriend](http://codeforces.com/contest/776/problem/B)
* [SPOJ - Namit in Trouble](http://www.spoj.com/problems/NGIRL/)
* [SPOJ - Bazinga!](http://www.spoj.com/problems/DCEPC505/)
* [Project Euler - Prime pair connection](https://www.hackerrank.com/contests/projecteuler/challenges/euler134)
* [SPOJ - N-Factorful](http://www.spoj.com/problems/NFACTOR/)
* [SPOJ - Binary Sequence of Prime Numbers](http://www.spoj.com/problems/BSPRIME/)
* [UVA 11353 - A Different Kind of Sorting](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2338)
* [SPOJ - Prime Generator](http://www.spoj.com/problems/PRIME1/)
* [SPOJ - Printing some primes (hard)](http://www.spoj.com/problems/PRIMES2/)
* [Codeforces - Nodbach Problem](https://codeforces.com/problemset/problem/17/A)
* [Codeforces - Colliders](https://codeforces.com/problemset/problem/154/B)
