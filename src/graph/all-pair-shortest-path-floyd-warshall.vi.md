---
tags:
  - Translated
e_maxx_link: floyd_warshall_algorithm
lang: vi
---

# Thuật toán Floyd-Warshall

Cho một đồ thị vô hướng hoặc có hướng có trọng số $G$ gồm $n$ đỉnh.
Nhiệm vụ là tìm độ dài đường đi ngắn nhất $d_{ij}$ giữa mọi cặp đỉnh $i$ và $j$.

Đồ thị có thể chứa các cạnh có trọng số âm, nhưng không được chứa các chu trình có tổng trọng số âm (chu trình âm).

Nếu tồn tại chu trình âm như vậy, bạn có thể đi quanh chu trình này lặp đi lặp lại nhiều lần, làm cho chi phí đường đi giảm đi sau mỗi lượt.
Do đó bạn có thể làm cho đường đi ngắn nhất nhỏ tùy ý, nói cách khác đường đi ngắn nhất không được xác định.
Điều này cũng đồng nghĩa với việc đồ thị vô hướng không thể chứa các cạnh có trọng số âm, vì một cạnh âm sẽ lập tức tạo thành một chu trình âm do bạn có thể đi qua đi lại dọc theo cạnh đó bao nhiêu lần tùy thích.

Thuật toán này cũng có thể được sử dụng để phát hiện sự tồn tại của các chu trình âm.
Đồ thị có chu trình âm khi và chỉ khi kết thúc thuật toán, khoảng cách từ một đỉnh $v$ đến chính nó là một số âm.

Thuật toán này được công bố đồng thời trong các bài viết của Robert Floyd và Stephen Warshall vào năm 1962.
Tuy nhiên, vào năm 1959, Bernard Roy cũng đã công bố một thuật toán về bản chất là giống hệt, nhưng công bố này không được chú ý đến rộng rãi.

## Mô tả thuật toán

Ý tưởng cốt lõi của thuật toán là chia nhỏ quá trình tìm đường đi ngắn nhất giữa hai đỉnh bất kỳ thành nhiều giai đoạn tăng dần.

Chúng ta đánh số các đỉnh từ 1 đến $n$.
Ma trận khoảng cách là $d[ ][ ]$.

Trước giai đoạn thứ $k$ ($k = 1 \dots n$), giá trị $d[i][j]$ với hai đỉnh $i$ và $j$ bất kỳ sẽ lưu trữ độ dài của đường đi ngắn nhất giữa đỉnh $i$ và đỉnh $j$, sao cho đường đi này chỉ chứa các đỉnh trong tập $\{1, 2, ..., k-1\}$ làm các đỉnh trung gian.

Nói cách khác, trước giai đoạn thứ $k$, giá trị của $d[i][j]$ bằng độ dài của đường đi ngắn nhất từ đỉnh $i$ đến đỉnh $j$, nếu đường đi này chỉ được phép đi qua các đỉnh có chỉ số nhỏ hơn $k$ (điểm bắt đầu và kết thúc của đường đi không bị giới hạn bởi tính chất này).

Dễ thấy tính chất này được thỏa mãn ở giai đoạn đầu tiên. Với $k = 0$, chúng ta điền vào ma trận giá trị $d[i][j] = w_{i j}$ nếu tồn tại cạnh nối giữa $i$ và $j$ có trọng số $w_{i j}$, và điền $d[i][j] = \infty$ nếu không tồn tại cạnh nối.
Trong thực tế, $\infty$ sẽ là một giá trị đủ lớn.
Như chúng ta sẽ thấy ở phần sau, đây là một yêu cầu bắt buộc đối với thuật toán.

Giả sử chúng ta đang ở giai đoạn thứ $k$, và chúng ta muốn cập nhật ma trận $d[ ][ ]$ để nó đáp ứng yêu cầu cho giai đoạn thứ $(k + 1)$.
Chúng ta cần xác định khoảng cách cho các cặp đỉnh $(i, j)$.
Có hai trường hợp hoàn toàn khác nhau:

*   Đường đi ngắn nhất từ đỉnh $i$ đến đỉnh $j$ chỉ sử dụng các đỉnh trung gian trong tập $\{1, 2, \dots, k\}$ trùng khớp với đường đi ngắn nhất chỉ sử dụng các đỉnh trung gian trong tập $\{1, 2, \dots, k-1\}$.

    Trong trường hợp này, giá trị $d[i][j]$ sẽ không thay đổi trong bước chuyển tiếp.

*   Đường đi ngắn nhất sử dụng các đỉnh trung gian trong $\{1, 2, \dots, k\}$ ngắn hơn.

    Điều này có nghĩa là đường đi mới, ngắn hơn này phải đi qua đỉnh $k$.
    Nghĩa là chúng ta có thể chia đường đi ngắn nhất giữa $i$ và $j$ thành hai đường đi:
    đường đi giữa $i$ và $k$, và đường đi giữa $k$ và $j$.
    Rõ ràng cả hai đường đi con này chỉ sử dụng các đỉnh trung gian trong tập $\{1, 2, \dots, k-1\}$ và là các đường đi ngắn nhất tương ứng.
    Do đó chúng ta đã tính sẵn độ dài của các đường đi con này trước đó, và chúng ta có thể tính độ dài đường đi ngắn nhất giữa $i$ và $j$ bằng công thức $d[i][k] + d[k][j]$.

Kết hợp hai trường hợp trên, chúng ta có thể tính lại khoảng cách của mọi cặp $(i, j)$ ở giai đoạn thứ $k$ như sau:

$$d_{\text{new}}[i][j] = min(d[i][j], d[i][k] + d[k][j])$$

Vì vậy, toàn bộ công việc cần làm ở giai đoạn thứ $k$ chỉ là duyệt qua tất cả các cặp đỉnh và tính toán lại độ dài đường đi ngắn nhất giữa chúng.
Kết quả là sau giai đoạn thứ $n$, giá trị $d[i][j]$ trong ma trận khoảng cách chính là độ dài của đường đi ngắn nhất giữa $i$ và $j$, hoặc bằng $\infty$ nếu không tồn tại đường đi giữa hai đỉnh $i$ và $j$.

Lưu ý cuối cùng - chúng ta không cần tạo một ma trận khoảng cách tạm thời $d_{\text{new}}[ ][ ]$ để lưu trữ kết quả của giai đoạn $k$, tức là mọi thay đổi có thể thực hiện trực tiếp trên ma trận $d[ ][ ]$ tại bất kỳ giai đoạn nào.
Thật vậy, ở bất kỳ giai đoạn $k$ nào, chúng ta chỉ tối ưu hóa (làm ngắn đi) khoảng cách trong ma trận, do đó không làm ảnh hưởng đến tính đúng đắn của độ dài đường đi ngắn nhất cho các cặp đỉnh được xử lý ở giai đoạn $(k+1)$ hoặc muộn hơn.

Độ phức tạp thời gian của thuật toán này hiển nhiên là $O(n^3)$.

## Cài đặt

Gọi `d[][]` là một mảng 2 chiều kích thước $n \times n$, được điền giá trị theo giai đoạn $0$ như giải thích ở trên.
Đồng thời chúng ta cũng gán $d[i][i] = 0$ với mọi $i$ ở giai đoạn $0$.

Thuật toán được cài đặt đơn giản như sau:

```cpp
for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            d[i][j] = min(d[i][j], d[i][k] + d[k][j]); 
        }
    }
}
```

Chúng ta giả định rằng nếu không có cạnh nối giữa hai đỉnh $i$ và $j$, thì ma trận tại vị trí `d[i][j]` sẽ chứa một số đủ lớn (đủ lớn để lớn hơn tổng độ dài của bất kỳ đường đi nào trên đồ thị).
Khi đó cạnh ảo này sẽ không bao giờ được chọn để tối ưu đường đi, và thuật toán hoạt động chính xác.

Tuy nhiên, nếu đồ thị chứa các cạnh có trọng số âm, chúng ta cần bổ sung thêm kiểm tra.
Nếu không, các giá trị trong ma trận có thể xuất hiện dạng $\infty - 1$, $\infty - 2$, v.v., mặc dù chúng vẫn chỉ ra rằng không có đường đi thực sự giữa các đỉnh tương ứng.
Do đó, nếu đồ thị có cạnh âm, tốt nhất nên viết thuật toán Floyd-Warshall theo cách sau để tránh thực hiện chuyển tiếp sử dụng các đường đi không tồn tại:

```cpp
for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (d[i][k] < INF && d[k][j] < INF)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]); 
        }
    }
}
```

## Tìm lại chuỗi các đỉnh của đường đi ngắn nhất

Rất dễ dàng để lưu thêm thông tin giúp khôi phục đường đi ngắn nhất giữa hai đỉnh bất kỳ dưới dạng một chuỗi các đỉnh.

Để làm điều này, ngoài ma trận khoảng cách $d[ ][ ]$, chúng ta duy trì một ma trận tổ tiên $p[ ][ ]$, lưu trữ chỉ số của giai đoạn mà tại đó khoảng cách ngắn nhất giữa hai đỉnh được cập nhật lần cuối cùng.
Rõ ràng chỉ số giai đoạn đó chính là một đỉnh trung gian nằm giữa đường đi ngắn nhất cần tìm.
Bây giờ chúng ta chỉ cần tìm tiếp đường đi ngắn nhất giữa đỉnh $i$ và $p[i][j]$, và giữa $p[i][j]$ và $j$.
Điều này dẫn đến thuật toán đệ quy đơn giản để khôi phục đường đi ngắn nhất.

## Trường hợp trọng số số thực

Nếu trọng số của các cạnh không phải số nguyên mà là số thực, chúng ta cần lưu ý đến sai số làm tròn khi làm việc với kiểu số thực dấu phẩy động.

Thuật toán Floyd-Warshall có một nhược điểm là sai số làm tròn tích lũy rất nhanh.
Thực tế là nếu có sai số $\delta$ ở giai đoạn đầu tiên, sai số này có thể tăng lên $2\delta$ ở giai đoạn thứ hai, $4\delta$ ở giai đoạn thứ ba, và cứ tiếp tục như vậy.

Để tránh điều này, thuật toán có thể sửa đổi để tính đến sai số làm tròn (EPS = $\delta$) bằng cách sử dụng phép so sánh sau:

```cpp
if (d[i][k] + d[k][j] < d[i][j] - EPS)
    d[i][j] = d[i][k] + d[k][j]; 
```

## Trường hợp đồ thị chứa chu trình âm

Về mặt lý thuyết, thuật toán Floyd-Warshall không áp dụng cho đồ thị chứa các chu trình âm.
Nhưng đối với mọi cặp đỉnh $i$ và $j$ mà không tồn tại đường đi xuất phát từ $i$, đi qua chu trình âm, và kết thúc tại $j$, thuật toán vẫn hoạt động chính xác.

Đối với các cặp đỉnh không có câu trả lời (do sự hiện diện của chu trình âm trên đường đi giữa chúng), thuật toán Floyd sẽ lưu trữ một giá trị bất kỳ (có thể là một số rất âm, nhưng không nhất thiết) trong ma trận khoảng cách.
Tuy nhiên, chúng ta có thể cải tiến thuật toán Floyd-Warshall để nó nhận diện các cặp đỉnh như vậy và gán giá trị của chúng bằng $-\text{INF}$.

Cách thực hiện như sau:
chạy thuật toán Floyd-Warshall thông thường cho đồ thị đã cho.
Khi đó, đường đi ngắn nhất giữa hai đỉnh $i$ và $j$ không tồn tại khi và chỉ khi tồn tại một đỉnh $t$ sao cho từ $i$ đi tới được $t$ và từ $t$ đi tới được $j$, đồng thời thỏa mãn $d[t][t] < 0$.

Ngoài ra, khi áp dụng thuật toán Floyd-Warshall cho đồ thị chứa chu trình âm, chúng ta nên lưu ý rằng khoảng cách có thể giảm xuống âm cực nhanh theo hàm mũ.
Do đó cần xử lý tràn số nguyên bằng cách giới hạn khoảng cách tối thiểu bởi một giá trị cụ thể (ví dụ $-\text{INF}$).

Để tìm hiểu chi tiết hơn về cách tìm chu trình âm trong đồ thị, xem bài viết riêng [Tìm chu trình âm trong đồ thị](finding-negative-cycle-in-graph.md).

## Bài tập áp dụng
 - [UVA: Page Hopping](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=762)
 - [SPOJ: Possible Friends](http://www.spoj.com/problems/SOCIALNE/)
 - [CODEFORCES: Greg and Graph](http://codeforces.com/problemset/problem/295/B)
 - [SPOJ: CHICAGO - 106 miles to Chicago](http://www.spoj.com/problems/CHICAGO/)
 * [UVA 10724 - Road Construction](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1665)
 * [UVA 117 - The Postal Worker Rings Once](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=53)
 * [Codeforces - Traveling Graph](http://codeforces.com/problemset/problem/21/D)
 * [UVA - 1198 - The Geodetic Set Problem](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3639)
 * [UVA - 10048 - Audiophobia](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=989)
 * [UVA - 125 - Numbering Paths](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=61)
 * [LOJ - Travel Company](http://lightoj.com/volume_showproblem.php?problem=1221)
 * [UVA 423 - MPI Maelstrom](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=364)
 * [UVA 1416 - Warfare And Logistics](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4162)
 * [UVA 1233 - USHER](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3674)
 * [UVA 10793 - The Orc Attack](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1734)
 * [UVA 10099 The Tourist Guide](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1040)
 * [UVA 869 - Airline Comparison](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=810)
 * [UVA 13211 - Geonosis](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=5134)
 * [SPOJ - Defend the Rohan](http://www.spoj.com/problems/ROHAAN/)
 * [Codeforces - Roads in Berland](http://codeforces.com/contest/25/problem/C)
 * [Codeforces - String Problem](http://codeforces.com/contest/33/problem/B)
 * [GYM - Manic Moving (C)](http://codeforces.com/gym/101223)
 * [SPOJ - Arbitrage](http://www.spoj.com/problems/ARBITRAG/)
 * [UVA - 12179 - Randomly-priced Tickets](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3331)
 * [LOJ - 1086 - Jogging Trails](http://lightoj.com/volume_showproblem.php?problem=1086)
 * [SPOJ - Ingredients](http://www.spoj.com/problems/INGRED/)
 * [CSES - Shortest Routes II](https://cses.fi/problemset/task/1672)
