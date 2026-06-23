---
tags:
  - Original
lang: vi
---
# Tối ưu hóa Knuth (Knuth's Optimization)

Tối ưu hóa Knuth (Knuth's Optimization), còn được gọi là Knuth-Yao Speedup, là một trường hợp đặc biệt của quy hoạch động (DP) trên đoạn, có thể tối ưu hóa độ phức tạp thời gian (Time Complexity) của các lời giải đi một thừa số tuyến tính, từ $O(n^3)$ đối với DP trên đoạn thông thường xuống còn $O(n^2)$.

## Điều kiện

Sự tăng tốc này được áp dụng cho các công thức chuyển trạng thái (Transition) có dạng:

$$dp(i, j) = \min_{i \leq k < j} [ dp(i, k) + dp(k+1, j) + C(i, j) ].$$

Tương tự như [DP chia để trị](./divide-and-conquer-dp.md), gọi $opt(i, j)$ là giá trị lớn nhất của $k$ làm cực tiểu hóa biểu thức trong công thức chuyển trạng thái ($opt$ được gọi là "điểm chia tối ưu" trong phần tiếp theo của bài viết này). Sự tối ưu hóa này yêu cầu điều sau đây phải được thỏa mãn:

$$opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j).$$

Chúng ta có thể chứng minh rằng điều này là đúng khi hàm chi phí $C$ thỏa mãn các điều kiện sau đây đối với $a \leq b \leq c \leq d$:

1. $C(b, c) \leq C(a, d)$;

2. $C(a, c) + C(b, d) \leq C(a, d) + C(b, c)$ (bất đẳng thức tứ giác (quadrangle inequality) [QI]).

Kết quả này được chứng minh ở phần bên dưới.

## Thuật toán

Hãy xử lý các trạng thái (State) DP sao cho chúng ta tính $dp(i, j-1)$ và $dp(i+1, j)$ trước $dp(i, j)$, và khi làm như vậy, chúng ta cũng tính cả $opt(i, j-1)$ và $opt(i+1, j)$. Khi đó, để tính $opt(i, j)$, thay vì thử các giá trị của $k$ từ $i$ đến $j-1$, chúng ta chỉ cần thử từ $opt(i, j-1)$ đến $opt(i+1, j)$. Để xử lý các cặp $(i,j)$ theo thứ tự này, chỉ cần sử dụng các vòng lặp `for` lồng nhau, trong đó $i$ chạy từ giá trị lớn nhất đến giá trị nhỏ nhất và $j$ chạy từ $i+1$ đến giá trị lớn nhất.

### Cài đặt mẫu

Mặc dù cách cài đặt (Implementation) có thể khác nhau, dưới đây là một ví dụ khá tổng quát. Cấu trúc của mã nguồn gần như giống hệt với cấu trúc của DP trên đoạn thông thường.

```{.cpp file=knuth_optimization}

int solve() {
    int N;
    ... // read N and input
    int dp[N][N], opt[N][N];

    auto C = [&](int i, int j) {
        ... // Implement cost function C.
    };

    for (int i = 0; i < N; i++) {
        opt[i][i] = i;
        ... // Initialize dp[i][i] according to the problem
    }

    for (int i = N-2; i >= 0; i--) {
        for (int j = i+1; j < N; j++) {
            int mn = INT_MAX;
            int cost = C(i, j);
            for (int k = opt[i][j-1]; k <= min(j-1, opt[i+1][j]); k++) {
                if (mn >= dp[i][k] + dp[k+1][j] + cost) {
                    opt[i][j] = k; 
                    mn = dp[i][k] + dp[k+1][j] + cost; 
                }
            }
            dp[i][j] = mn; 
        }
    }

    return dp[0][N-1];
}
```

### Độ phức tạp

Độ phức tạp của thuật toán có thể được ước lượng qua tổng sau đây:

$$
\sum\limits_{i=1}^N \sum\limits_{j=i+1}^N [opt(i+1,j)-opt(i,j-1)] =
\sum\limits_{i=1}^N \sum\limits_{j=i}^{N-1} [opt(i+1,j+1)-opt(i,j)].
$$

Như bạn có thể thấy, hầu hết các số hạng trong biểu thức này tự triệt tiêu lẫn nhau, ngoại trừ các số hạng dương chứa $j=N-1$ và số hạng âm chứa $i=1$. Do đó, toàn bộ tổng này có thể được ước lượng là

$$
\sum\limits_{k=1}^N[opt(k,N)-opt(1,k)] = O(n^2),
$$

thay vì $O(n^3)$ như khi sử dụng DP trên đoạn thông thường.

### Trong thực tế

Ứng dụng phổ biến nhất của tối ưu hóa Knuth là trong DP trên đoạn, với công thức chuyển trạng thái đã cho. Khó khăn duy nhất là chứng minh hàm chi phí thỏa mãn các điều kiện đưa ra. Trường hợp đơn giản nhất là khi hàm chi phí $C(i, j)$ chỉ đơn giản là tổng các phần tử (Element) của mảng con (Subarray) $S[i, i+1, ..., j]$ của một mảng (Array) nào đó (tùy thuộc vào yêu cầu của bài toán). Tuy nhiên, đôi khi chúng có thể phức tạp hơn.

Lưu ý rằng, hơn cả các điều kiện trên công thức chuyển trạng thái DP và hàm chi phí, chìa khóa của sự tối ưu hóa này nằm ở bất đẳng thức về điểm chia tối ưu. Trong một số bài toán, chẳng hạn như bài toán cây tìm kiếm nhị phân tối ưu (optimal binary search tree) (đây cũng chính là bài toán gốc mà tối ưu hóa này được phát triển cho nó), các công thức chuyển trạng thái và hàm chi phí sẽ ít rõ ràng hơn, tuy nhiên, người ta vẫn có thể chứng minh được rằng $opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j)$, và do đó, có thể áp dụng tối ưu hóa này.


### Chứng minh tính đúng đắn

Để chứng minh tính đúng đắn của thuật toán này dưới các điều kiện của $C(i,j)$, ta chỉ cần chứng minh rằng

$$
opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j)
$$

giả sử các điều kiện đã cho được thỏa mãn.

!!! lemma "Bổ đề"
    $dp(i, j)$ cũng thỏa mãn bất đẳng thức tứ giác, với điều kiện các điều kiện của bài toán được thỏa mãn.

??? hint "Chứng minh"
    Chứng minh cho bổ đề (Lemma) này sử dụng quy nạp mạnh. Nó được trích dẫn từ bài báo <a href="https://dl.acm.org/doi/pdf/10.1145/800141.804691">Efficient Dynamic Programming Using Quadrangle Inequalities</a> của tác giả F. Frances Yao, nơi giới thiệu về Knuth-Yao Speedup (mệnh đề cụ thể này là Bổ đề 2.1 trong bài báo). Ý tưởng là quy nạp theo chiều dài $l = d - a$. Trường hợp $l = 1$ là hiển nhiên. Với $l > 1$ xét 2 trường hợp:  

    1. $b = c$  
    Bất đẳng thức rút gọn thành $dp(a, b) + dp(b, d) \leq dp(a, d)$ (Điều này giả định rằng $dp(i, i) = 0$ với mọi $i$, điều này luôn đúng đối với tất cả các bài toán sử dụng tối ưu hóa này). Đặt $opt(a,d) = z$. 

        - Nếu $z < j$,  
        Chú ý rằng
        
            $$
            dp(a, b) \leq dp_{z}(a, b) = dp(a, z) + dp(z+1, b) + C(a, b).
            $$
            
            Do đó,  
            
            $$
            dp(a, b) + dp(b, d) \leq dp(a, z) + dp(z+1, b) + dp(b, d) + C(a, b)
            $$

            Từ giả thiết quy nạp, ta có $dp(z+1, b) + dp(b, d) \leq dp(z+1, d)$. Ngoài ra, theo đề bài ta có $C(a, b) \leq C(a, d)$. Kết hợp hai dữ kiện này với bất đẳng thức trên sẽ cho ta kết quả mong muốn.

        - Nếu $z \geq j$, chứng minh cho trường hợp này là đối xứng với trường hợp trước.

    2. $b < c$  
    Đặt $opt(b, c) = z$ và $opt(a, d) = y$. 
        
        - Nếu $z \leq y$,  
        
            $$
            dp(a, c) + dp(b, d) \leq dp_{z}(a, c) + dp_{y}(b, d)
            $$

            trong đó

            $$
            dp_{z}(a, c) + dp_{y}(b, d) = C(a, c) + C(b, d) + dp(a, z) + dp(z+1, c) + dp(b, y) + dp(y+1, d).
            $$

            Sử dụng bất đẳng thức tứ giác (QI) trên $C$ và trên trạng thái DP cho các chỉ số $z+1 \leq y+1 \leq c \leq d$ (từ giả thiết quy nạp) sẽ cho ta kết quả mong muốn.
        
        - Nếu $z > y$, chứng minh cho trường hợp này là đối xứng với trường hợp trước.

    Điều này hoàn thành chứng minh của bổ đề.

Bây giờ, hãy xem xét thiết lập sau. Chúng ta có 2 chỉ số $i \leq p \leq q < j$. Đặt $dp_{k} = C(i, j) + dp(i, k) + dp(k+1, j)$.

Giả sử chúng ta chỉ ra rằng

$$
dp_{p}(i, j-1) \geq dp_{q}(i, j-1) \implies dp_{p}(i, j) \geq dp_{q}(i, j).
$$

Đặt $q = opt(i, j-1)$, theo định nghĩa, ta có $dp_{p}(i, j-1) \geq dp_{q}(i, j-1)$. Do đó, áp dụng bất đẳng thức cho mọi $i \leq p \leq q$, ta có thể suy ra rằng $opt(i, j)$ ít nhất bằng $opt(i, j-1)$, chứng minh nửa đầu của bất đẳng thức.

Bây giờ, sử dụng QI trên một số chỉ số $p+1 \leq q+1 \leq j-1 \leq j$, ta thu được

$$\begin{align}
&dp(p+1, j-1) + dp(q+1, j) ≤ dp(q+1, j-1) + dp(p+1, j) \\
\implies& (dp(i, p) + dp(p+1, j-1) + C(i, j-1)) + (dp(i, q) + dp(q+1, j) + C(i, j)) \\  
\leq& (dp(i, q) + dp(q+1, j-1) + C(i, j-1)) + (dp(i, p) + dp(p+1, j) + C(i, j)) \\  
\implies& dp_{p}(i, j-1) + dp_{q}(i, j) ≤ dp_{p}(i, j) + dp_{q}(i, j-1) \\
\implies& dp_{p}(i, j-1) - dp_{q}(i, j-1) ≤ dp_{p}(i, j) - dp_{q}(i, j) \\
\end{align}$$

Cuối cùng,

$$\begin{align}
&dp_{p}(i, j-1) \geq dp_{q}(i, j-1) \\
&\implies 0 \leq dp_{p}(i, j-1) - dp_{q}(i, j-1) \leq dp_{p}(i, j) - dp_{q}(i, j) \\
&\implies dp_{p}(i, j) \geq dp_{q}(i, j)
\end{align}$$  

Điều này chứng minh phần đầu tiên của bất đẳng thức, tức là $opt(i, j-1) \leq opt(i, j)$. Phần thứ hai $opt(i, j) \leq opt(i+1, j)$ có thể được chỉ ra bằng ý tưởng tương tự, bắt đầu với bất đẳng thức $dp(i, p) + dp(i+1, q) ≤ dp(i+1, p) + dp(i, q)$.

Chứng minh hoàn tất.

## Bài tập áp dụng
- [UVA - Cutting Sticks](https://onlinejudge.org/external/100/10003.pdf)
- [UVA - Prefix Codes](https://onlinejudge.org/external/120/12057.pdf)
- [SPOJ - Breaking String](https://www.spoj.com/problems/BRKSTRNG/)
- [UVA - Optimal Binary Search Tree](https://onlinejudge.org/external/103/10304.pdf)


## Tài liệu tham khảo
- [Bài viết trên Geeksforgeeks](https://www.geeksforgeeks.org/knuths-optimization-in-dynamic-programming/)
- [Tài liệu về các phương pháp tối ưu hóa DP](https://home.cse.ust.hk/~golin/COMP572/Notes/DP_speedup.pdf)
- [Efficient Dynamic Programming Using Quadrangle Inequalities](https://dl.acm.org/doi/pdf/10.1145/800141.804691)