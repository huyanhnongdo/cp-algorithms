---
title: Generating all K-combinations
tags:
  - Translated
e_maxx_link: generating_combinations
lang: vi
---
# Tạo tất cả $K$-tổ hợp

Trong bài viết này chúng ta sẽ thảo luận về bài toán tạo tất cả `$K$`-tổ hợp (Combination).
Cho các số tự nhiên `$N$` và `$K$`, và xét một tập hợp các số từ `$1$` đến `$N$`.
Nhiệm vụ là tìm tất cả **tập con có kích thước `$K$`**.

## Tạo tổ hợp `$K$`-tổ hợp tiếp theo theo thứ tự từ điển {data-toc-label="Generate next lexicographical K-combination"}

Trước tiên chúng ta sẽ tạo chúng theo thứ tự từ điển (lexicographical order).
Thuật toán (Algorithm) cho việc này rất đơn giản. Tổ hợp đầu tiên sẽ là `${1, 2, ..., K}$`. Bây giờ chúng ta hãy xem cách
tìm tổ hợp ngay sau tổ hợp này, theo thứ tự từ điển. Để làm điều đó, chúng ta xét tổ hợp hiện tại của mình, và tìm phần tử (Element) ngoài cùng bên phải mà chưa đạt đến giá trị cao nhất có thể. Khi tìm thấy phần tử này, chúng ta tăng nó lên `$1$` đơn vị, và gán giá trị hợp lệ thấp nhất cho tất cả các phần tử tiếp theo.

```{.cpp file=next_combination}
bool next_combination(vector<int>& a, int n) {
    int k = (int)a.size();
    for (int i = k - 1; i >= 0; i--) {
        if (a[i] < n - k + i + 1) {
            a[i]++;
            for (int j = i + 1; j < k; j++)
                a[j] = a[j - 1] + 1;
            return true;
        }
    }
    return false;
}
```

## Tạo tất cả $K$-tổ hợp sao cho các tổ hợp kề nhau khác nhau đúng một phần tử {data-toc-label="Generate all K-combinations such that adjacent combinations differ by one element"}

Lần này chúng ta muốn tạo tất cả `$K$`-tổ hợp theo một thứ tự,
sao cho các tổ hợp kề nhau khác nhau đúng một phần tử.

Việc này có thể được giải quyết bằng cách sử dụng [Mã Gray (Gray Code)](../algebra/gray-code.md):
Nếu chúng ta gán một bitmask (Bitmask) cho mỗi tập con, thì bằng cách tạo và lặp qua các bitmask này với mã Gray, chúng ta có thể nhận được câu trả lời.

Bài toán tạo `$K$`-tổ hợp cũng có thể được giải quyết bằng cách sử dụng Mã Gray theo một cách khác:
Tạo Mã Gray cho các số từ `$0$` đến `$2^N - 1$` và chỉ giữ lại những mã chứa `$K$` số `$1$`.
Một sự thật đáng ngạc nhiên là trong dãy kết quả gồm `$K$` bit được đặt (set bits), bất kỳ hai mask kề nhau nào (bao gồm cả mask đầu tiên và cuối cùng - kề nhau theo nghĩa chu trình) - sẽ khác nhau đúng hai bit, đây chính là mục tiêu của chúng ta (loại bỏ một số, thêm một số).

Chúng ta hãy chứng minh (Proof) điều này:

Để chứng minh, chúng ta nhớ lại thực tế rằng dãy `$G(N)$` (đại diện cho Mã Gray thứ `$N$`) có thể thu được như sau:

$$G(N) = 0G(N-1) \cup 1G(N-1)^\text{R}$$

Tức là, xét dãy Mã Gray cho `$N-1$`, và thêm tiền tố `$0$` vào trước mỗi phần tử. Và xét dãy Mã Gray đảo ngược cho `$N-1$` và thêm tiền tố `$1$` vào trước mỗi mask, và nối hai dãy này lại.

Bây giờ chúng ta có thể trình bày chứng minh của mình.

Đầu tiên, chúng ta chứng minh rằng mask đầu tiên và mask cuối cùng khác nhau đúng hai bit. Để làm điều này, chỉ cần lưu ý rằng mask đầu tiên của dãy `$G(N)$`, sẽ có dạng `$N-K$` `$0$`s, theo sau bởi `$K$` `$1$`s. Vì bit đầu tiên được đặt là `$0$`, sau đó `$(N-K-1)$` `$0$`s theo sau, sau đó `$K$` bit đã đặt theo sau và mask cuối cùng sẽ có dạng `$1$`, sau đó `$(N-K)$` `$0$`s, sau đó `$K-1$` `$1$`s.
Áp dụng nguyên lý quy nạp toán học, và sử dụng công thức cho `$G(N)$`, kết thúc chứng minh.

Bây giờ nhiệm vụ của chúng ta là chỉ ra rằng bất kỳ hai mã kề nhau nào cũng khác nhau đúng hai bit, chúng ta có thể làm điều này bằng cách xem xét phương trình đệ quy (Recursion) của chúng ta để tạo Mã Gray. Giả sử nội dung của hai nửa được tạo bởi `$G(N-1)$` là đúng. Bây giờ chúng ta cần chứng minh rằng cặp liên tiếp mới được hình thành tại điểm nối (bằng cách nối hai nửa này) cũng hợp lệ, tức là chúng khác nhau đúng hai bit.

Điều này có thể được thực hiện, vì chúng ta biết mask cuối cùng của nửa đầu và mask đầu tiên của nửa sau. Mask cuối cùng của nửa đầu sẽ là `$1$`, sau đó `$(N-K-1)$` `$0$`s, sau đó `$K-1$` `$1$`s. Và mask đầu tiên của nửa sau sẽ là `$0$`, sau đó `$(N-K-2)$` `$0$`s sẽ theo sau, và sau đó `$K$` `$1$`s. Do đó, so sánh hai mask, chúng ta tìm thấy đúng hai bit khác nhau.

Sau đây là một cài đặt (Implementation) thô sơ hoạt động bằng cách tạo tất cả `$2^{n}$` tập con có thể, và tìm các tập con có kích thước `$K$`.

```{.cpp file=generate_all_combinations_naive}
int gray_code (int n) {
    return n ^ (n >> 1);
}

int count_bits (int n) {
    int res = 0;
    for (; n; n >>= 1)
        res += n & 1;
    return res;
}

void all_combinations (int n, int k) {
    for (int i = 0; i < (1 << n); i++) {
        int cur = gray_code (i);
        if (count_bits(cur) == k) {
            for (int j = 0; j < n; j++) {
                if (cur & (1 << j))
                    cout << j + 1;
            }
            cout << "\n";
        }
    }
}
```

Điều đáng nói là tồn tại một triển khai hiệu quả hơn chỉ dựa vào việc xây dựng các tổ hợp hợp lệ và do đó hoạt động trong `$O\left(N \cdot \binom{N}{K}\right)$` tuy nhiên nó có bản chất đệ quy và đối với các giá trị `$N$` nhỏ hơn nó có thể có hằng số lớn hơn so với giải pháp trước.

Việc triển khai được suy ra từ công thức:

$$G(N, K) = 0G(N-1, K) \cup 1G(N-1, K-1)^\text{R}$$

Công thức này được thu thập bằng cách sửa đổi phương trình tổng quát để xác định mã Gray, và hoạt động bằng cách chọn dãy con (Subsequence) từ các phần tử thích hợp.

Việc triển khai của nó như sau:

```{.cpp file=generate_all_combinations_fast}
vector<int> ans;

void gen(int n, int k, int idx, bool rev) {
    if (k > n || k < 0)
        return;

    if (!n) {
        for (int i = 0; i < idx; ++i) {
            if (ans[i])
                cout << i + 1;
        }
        cout << "\n";
        return;
    }

    ans[idx] = rev;
    gen(n - 1, k - rev, idx + 1, false);
    ans[idx] = !rev;
    gen(n - 1, k - !rev, idx + 1, true);
}

void all_combinations(int n, int k) {
    ans.resize(n);
    gen(n, k, 0, false);
}
```