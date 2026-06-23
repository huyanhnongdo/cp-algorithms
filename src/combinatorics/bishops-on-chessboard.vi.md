---
tags:
  - Translated
e_maxx_link: bishops_arrangement
lang: vi
---
# Đặt Quân Tượng trên Bàn Cờ Vua

Tìm số cách đặt $K$ quân tượng trên bàn cờ vua kích thước $N \times N$ sao cho không có hai quân tượng nào tấn công nhau.

## Thuật toán

Bài toán này có thể được giải bằng quy hoạch động (DP - Dynamic Programming).

Hãy đánh số các đường chéo của bàn cờ vua như sau: các đường chéo đen có chỉ số lẻ, các đường chéo trắng có chỉ số chẵn, và các đường chéo được đánh số theo thứ tự không giảm của số ô vuông trong chúng. Dưới đây là một ví dụ cho bàn cờ vua kích thước $5 \times 5$.

$$\begin{matrix}
\bf{1} & 2 & \bf{5} & 6 & \bf{9} \\\
2 & \bf{5} & 6 & \bf{9} & 8 \\\
\bf{5} & 6 & \bf{9} & 8 & \bf{7} \\\
6 & \bf{9} & 8 & \bf{7} & 4 \\\
\bf{9} & 8 & \bf{7} & 4 & \bf{3} \\\
\end{matrix}$$

Gọi `D[i][j]` là số cách đặt `j` quân tượng trên các đường chéo có chỉ số đến `i` mà có cùng màu với đường chéo `i`.
Khi đó `i` sẽ từ `1` đến `2N-1` và `j` sẽ từ `0` đến `K`.

Chúng ta có thể tính `D[i][j]` chỉ sử dụng các giá trị của `D[i-2]` (chúng ta trừ đi 2 vì chúng ta chỉ xét các đường chéo cùng màu với $i$).
Có hai cách để tính `D[i][j]`.
Hoặc chúng ta đặt tất cả `j` quân tượng trên các đường chéo trước đó: khi đó có `D[i-2][j]` cách để làm điều này.
Hoặc chúng ta đặt một quân tượng trên đường chéo `i` và `j-1` quân tượng trên các đường chéo trước đó.
Số cách để làm điều này bằng số ô vuông trên đường chéo `i` trừ đi `j-1`, bởi vì mỗi quân trong số `j-1` quân tượng đã đặt trên các đường chéo trước đó sẽ chặn một ô vuông trên đường chéo hiện tại.
Số ô vuông trên đường chéo `i` có thể được tính như sau:

```cpp
int squares (int i) {
    if (i & 1)
        return i / 4 * 2 + 1;
    else
        return (i - 1) / 4 * 2 + 2;
}
```

Trường hợp cơ sở (base case) đơn giản: `D[i][0] = 1`, `D[1][1] = 1`.

Sau khi chúng ta đã tính tất cả các giá trị của `D[i][j]`, đáp án có thể được suy ra như sau:
xét tất cả các số lượng quân tượng có thể được đặt trên các đường chéo đen `i` từ `0` đến `K`, với số lượng quân tượng tương ứng trên các đường chéo trắng là `K-i`.
Các quân tượng đặt trên các đường chéo đen và trắng không bao giờ tấn công nhau, nên việc đặt quân có thể được thực hiện độc lập.
Chỉ số của đường chéo đen cuối cùng là `2N-1`, đường chéo trắng cuối cùng là `2N-2`.
Với mỗi `i`, chúng ta cộng `D[2N-1][i] * D[2N-2][K-i]` vào đáp án.

## Cài đặt

```cpp
int bishop_placements(int N, int K)
{
    if (K > 2 * N - 1)
        return 0;

    vector<vector<int>> D(N * 2, vector<int>(K + 1));
    for (int i = 0; i < N * 2; ++i)
        D[i][0] = 1;
    D[1][1] = 1;
    for (int i = 2; i < N * 2; ++i)
        for (int j = 1; j <= K; ++j)
            D[i][j] = D[i-2][j] + D[i-2][j-1] * (squares(i) - j + 1);

    int ans = 0;
    for (int i = 0; i <= K; ++i)
        ans += D[N*2-1][i] * D[N*2-2][K-i];
    return ans;
}
```