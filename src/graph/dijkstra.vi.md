---
tags:
  - Translated
e_maxx_link: dijkstra
lang: vi
---

# Thuật toán Dijkstra

Cho một đồ thị có hướng hoặc vô hướng có trọng số gồm $n$ đỉnh và $m$ cạnh. Trọng số của tất cả các cạnh đều không âm. Bạn cũng được cho một đỉnh xuất phát $s$. Bài viết này thảo luận về việc tìm độ dài đường đi ngắn nhất từ đỉnh xuất phát $s$ đến tất cả các đỉnh khác, và cách khôi phục lại các đường đi ngắn nhất đó.

Bài toán này còn được gọi là **bài toán đường đi ngắn nhất từ một nguồn** (single-source shortest paths problem).

## Thuật toán

Dưới đây là mô tả thuật toán được đưa ra bởi nhà khoa học máy tính người Hà Lan Edsger W. Dijkstra vào năm 1959.

Chúng ta tạo một mảng $d[]$, trong đó với mỗi đỉnh $v$, chúng ta lưu trữ độ dài hiện tại của đường đi ngắn nhất từ $s$ đến $v$ vào $d[v]$.
Ban đầu gán $d[s] = 0$, và đối với tất cả các đỉnh còn lại, khoảng cách này bằng vô cùng.
Trong phần cài đặt, một số đủ lớn (được đảm bảo lớn hơn bất kỳ độ dài đường đi khả dĩ nào) sẽ được chọn làm giá trị vô cùng.

$$d[v] = \infty,~ v \ne s$$

Ngoài ra, chúng ta duy trì một mảng boolean đánh dấu $u[]$, lưu trữ trạng thái một đỉnh $v$ đã được xử lý hay chưa. Ban đầu, tất cả các đỉnh đều chưa được đánh dấu:

$$u[v] = {\rm false}$$

Thuật toán Dijkstra thực hiện qua $n$ bước lặp. Tại mỗi bước lặp, một đỉnh $v$ chưa được đánh dấu có giá trị $d[v]$ nhỏ nhất sẽ được chọn ra:

Hiển nhiên, ở bước lặp đầu tiên, đỉnh xuất phát $s$ sẽ luôn được chọn.

Đỉnh $v$ được chọn sau đó sẽ được đánh dấu đã xử lý. Tiếp theo, từ đỉnh $v$ các phép **tối ưu hóa** (relaxations) được thực hiện: tất cả các cạnh có dạng $(v, \text{to})$ được xem xét, và với mỗi đỉnh $\text{to}$ kề nó, thuật toán cố gắng cải thiện (làm ngắn đi) giá trị $d[\text{to}]$. Nếu trọng số của cạnh hiện tại bằng $len$, đoạn mã tối ưu hóa là:

$$d[\text{to}] = \min (d[\text{to}], d[v] + len)$$

Sau khi tất cả các cạnh đi ra từ $v$ được xem xét xong, bước lặp hiện tại kết thúc. Cuối cùng, sau $n$ bước lặp, tất cả các đỉnh đều sẽ được đánh dấu và thuật toán kết thúc. Chúng ta khẳng định rằng các giá trị $d[v]$ tìm được chính là độ dài đường đi ngắn nhất từ $s$ đến tất cả các đỉnh $v$.

Lưu ý rằng nếu có một số đỉnh không thể đi tới được từ đỉnh xuất phát $s$, giá trị $d[v]$ của chúng sẽ giữ nguyên bằng vô cùng. Rõ ràng, một vài bước lặp cuối của thuật toán sẽ chọn các đỉnh này, nhưng không có thao tác hữu ích nào được thực hiện cho chúng. Do đó, thuật toán có thể dừng sớm ngay khi đỉnh được chọn tiếp theo có khoảng cách bằng vô cùng.

### Khôi phục đường đi ngắn nhất

Thông thường chúng ta cần biết không chỉ độ dài đường đi ngắn nhất mà cả chính đường đi đó. Hãy xem cách lưu trữ đủ thông tin để khôi phục đường đi ngắn nhất từ $s$ đến bất kỳ đỉnh nào. Chúng ta duy trì một mảng các đỉnh cha $p[]$, trong đó với mỗi đỉnh $v \ne s$, $p[v]$ là đỉnh liền trước $v$ trong đường đi ngắn nhất từ $s$ đến $v$. Ở đây chúng ta sử dụng tính chất: nếu lấy đường đi ngắn nhất tới đỉnh $v$ và loại bỏ đỉnh $v$ khỏi đường đi này, chúng ta sẽ thu được một đường đi kết thúc ở đỉnh $p[v]$, và đường đi con này cũng chính là đường đi ngắn nhất tới đỉnh $p[v]$. Mảng cha này có thể được sử dụng để khôi phục đường đi tới bất kỳ đỉnh nào: bắt đầu từ đỉnh $v$, liên tục truy ngược lại đỉnh cha của đỉnh hiện tại cho đến khi gặp đỉnh xuất phát $s$ để thu được đường đi ngắn nhất cần tìm theo thứ tự đảo ngược. Như vậy, đường đi ngắn nhất $P$ tới đỉnh $v$ là:

$$P = (s, \ldots, p[p[p[v]]], p[p[v]], p[v], v)$$

Việc xây dựng mảng cha này cực kỳ đơn giản: với mỗi bước tối ưu hóa thành công, tức là khi từ một đỉnh $v$ được chọn, khoảng cách tới đỉnh $\text{to}$ được cải thiện, chúng ta cập nhật đỉnh cha của $\text{to}$ chính là đỉnh $v$:

$$p[\text{to}] = v$$

## Chứng minh tính đúng đắn

Khẳng định chính làm cơ sở cho tính đúng đắn của thuật toán Dijkstra là:

**Sau khi bất kỳ đỉnh $v$ nào được đánh dấu đã xử lý, khoảng cách hiện tại $d[v]$ tới nó là khoảng cách ngắn nhất, và sẽ không bao giờ thay đổi nữa.**

Chứng minh bằng phương pháp quy nạp. Ở bước lặp đầu tiên, khẳng định này hiển nhiên đúng: đỉnh duy nhất được đánh dấu là $s$, và khoảng cách tới nó $d[s] = 0$ chính là độ dài đường đi ngắn nhất tới $s$. Giả sử khẳng định đúng cho tất cả các bước lặp trước đó, tức là cho tất cả các đỉnh đã được đánh dấu; chúng ta chứng minh rằng nó không bị vi phạm sau bước lặp hiện tại. Gọi $v$ là đỉnh được chọn ở bước lặp hiện tại, tức là đỉnh thuật toán sẽ đánh dấu xử lý tiếp theo. Chúng ta cần chứng minh $d[v]$ thực sự bằng độ dài đường đi ngắn nhất tới nó $l[v]$.

Xét đường đi ngắn nhất $P$ tới đỉnh $v$. Đường đi này có thể chia làm hai phần: $P_1$ gồm toàn các đỉnh đã đánh dấu (ít nhất đỉnh xuất phát $s$ thuộc $P_1$), và phần còn lại $P_2$ (nó có thể chứa đỉnh đã đánh dấu, nhưng luôn bắt đầu bằng một đỉnh chưa đánh dấu). Gọi đỉnh đầu tiên của phần đường đi $P_2$ là $p$, và đỉnh cuối cùng của phần $P_1$ là $q$.

Đầu tiên chúng ta chứng minh khẳng định đúng cho đỉnh $p$, tức là chứng minh $d[p] = l[p]$.
Điều này khá hiển nhiên: ở một trong các bước lặp trước, chúng ta đã chọn đỉnh $q$ và thực hiện tối ưu hóa từ nó.
Vì (theo cách chọn đỉnh $p$) đường đi ngắn nhất tới $p$ chính là đường đi ngắn nhất tới $q$ cộng với cạnh $(q, p)$, việc tối ưu hóa từ $q$ đã gán cho $d[p]$ giá trị bằng độ dài đường đi ngắn nhất $l[p]$.

Vì trọng số các cạnh là không âm, độ dài đường đi ngắn nhất $l[p]$ (mà chúng ta vừa chứng minh bằng $d[p]$) không vượt quá độ dài đường đi ngắn nhất $l[v]$ tới đỉnh $v$. Do $l[v] \le d[v]$ (vì thuật toán Dijkstra không thể tìm được đường đi ngắn hơn đường đi ngắn nhất thực tế), ta có bất đẳng thức:

$$d[p] = l[p] \le l[v] \le d[v]$$

Mặt khác, vì cả hai đỉnh $p$ và $v$ đều chưa được đánh dấu, và bước lặp hiện tại lại chọn đỉnh $v$ thay vì $p$, ta có bất đẳng thức thứ hai:

$$d[p] \ge d[v]$$

Từ hai bất đẳng thức này, ta suy ra $d[p] = d[v]$, và từ các đẳng thức trước đó ta có:

$$d[v] = l[v]$$

Ta có điều phải chứng minh.

## Cài đặt

Thuật toán Dijkstra thực hiện qua $n$ bước lặp. Tại mỗi bước lặp, nó chọn ra đỉnh chưa đánh dấu $v$ có giá trị $d[v]$ nhỏ nhất, đánh dấu nó và duyệt qua tất cả các cạnh $(v, \text{to})$ để tối ưu hóa giá trị $d[\text{to}]$.

Thời gian chạy của thuật toán bao gồm:

* $n$ lần tìm kiếm đỉnh có giá trị $d[v]$ nhỏ nhất trong số $O(n)$ đỉnh chưa đánh dấu.
* $m$ lần thử tối ưu hóa khoảng cách dọc theo các cạnh.

Đối với cách cài đặt đơn giản nhất, thao tác tìm kiếm đỉnh yêu cầu $O(n)$ phép toán ở mỗi bước lặp, và mỗi lần tối ưu hóa cạnh tốn $O(1)$. Do đó, độ phức tạp tiệm cận của thuật toán là:

$$O(n^2+m)$$

Độ phức tạp này là tối ưu đối với đồ thị dày, tức là khi $m \approx n^2$.
Tuy nhiên, đối với đồ thị thưa, khi $m$ nhỏ hơn nhiều so với số lượng cạnh tối đa $n^2$, bài toán có thể giải được với độ phức tạp $O(n \log n + m)$. Chi tiết thuật toán và cài đặt xem tại bài viết [Thuật toán Dijkstra trên đồ thị thưa](dijkstra_sparse.md).

```{.cpp file=dijkstra_dense}
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);
    vector<bool> u(n, false);

    d[s] = 0;
    for (int i = 0; i < n; i++) {
        int v = -1;
        for (int j = 0; j < n; j++) {
            if (!u[j] && (v == -1 || d[j] < d[v]))
                v = j;
        }
        
        if (d[v] == INF)
            break;
        
        u[v] = true;
        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;
            
            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
            }
        }
    }
}
```

Ở đây đồ thị `adj` được lưu trữ dưới dạng danh sách kề: đối với mỗi đỉnh $v$, `adj[v]` chứa danh sách các cạnh đi ra từ đỉnh này, tức là danh sách các `pair<int,int>` trong đó phần tử thứ nhất là đỉnh kề bên kia của cạnh, và phần tử thứ hai là trọng số cạnh.

Hàm nhận vào đỉnh xuất phát $s$ và hai vector dùng để trả về kết quả.

Trước tiên, mã nguồn khởi tạo các mảng: khoảng cách $d[]$, nhãn đánh dấu $u[]$ và đỉnh cha $p[]$. Sau đó nó thực hiện $n$ bước lặp. Tại mỗi bước lặp, đỉnh $v$ có khoảng cách $d[v]$ nhỏ nhất trong số các đỉnh chưa đánh dấu sẽ được chọn. Nếu khoảng cách tới đỉnh $v$ được chọn bằng vô cùng, thuật toán dừng lại. Ngược lại, đỉnh đó được đánh dấu đã xử lý, và toàn bộ cạnh đi ra từ đỉnh này được kiểm tra. Nếu có thể tối ưu hóa dọc theo cạnh (tức là khoảng cách $d[\text{to}]$ có thể được rút ngắn), chúng ta cập nhật khoảng cách $d[\text{to}]$ và cha $p[\text{to}]$.

Sau khi hoàn thành tất cả các bước lặp, mảng $d[]$ lưu trữ độ dài đường đi ngắn nhất tới tất cả các đỉnh, và mảng $p[]$ lưu trữ đỉnh cha của tất cả các đỉnh (ngoại trừ đỉnh xuất phát $s$). Đường đi ngắn nhất tới đỉnh $t$ bất kỳ có thể khôi phục lại như sau:

```{.cpp file=dijkstra_restore_path}
vector<int> restore_path(int s, int t, vector<int> const& p) {
    vector<int> path;

    for (int v = t; v != s; v = p[v])
        path.push_back(v);
    path.push_back(s);

    reverse(path.begin(), path.end());
    return path;
}
```

## Tài liệu tham khảo

* Edsger Dijkstra. A note on two problems in connexion with graphs [1959]
* Thomas Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein. Introduction to Algorithms [2005]

## Bài tập áp dụng
* [Timus - Ivan's Car](http://acm.timus.ru/problem.aspx?space=1&num=1930) [Độ khó: Trung bình]
* [Timus - Sightseeing Trip](http://acm.timus.ru/problem.aspx?space=1&num=1004)
* [SPOJ - SHPATH](http://www.spoj.com/problems/SHPATH/) [Độ khó: Dễ]
* [Codeforces - Dijkstra?](http://codeforces.com/problemset/problem/20/C) [Độ khó: Dễ]
* [Codeforces - Shortest Path](http://codeforces.com/problemset/problem/59/E)
* [Codeforces - Jzzhu and Cities](http://codeforces.com/problemset/problem/449/B)
* [Codeforces - The Classic Problem](http://codeforces.com/problemset/problem/464/E)
* [Codeforces - President and Roads](http://codeforces.com/problemset/problem/567/E)
* [Codeforces - Complete The Graph](http://codeforces.com/problemset/problem/715/B)
* [TopCoder - SkiResorts](https://community.topcoder.com/stat?c=problem_statement&pm=12468)
* [TopCoder - MaliciousPath](https://community.topcoder.com/stat?c=problem_statement&pm=13596)
* [SPOJ - Ada and Trip](http://www.spoj.com/problems/ADATRIP/)
* [LA - 3850 - Here We Go(relians) Again](https://vjudge.net/problem/UVALive-3850)
* [GYM - Destination Unknown (D)](http://codeforces.com/gym/100625)
* [UVA 12950 - Even Obsession](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=4829)
* [GYM - Journey to Grece (A)](http://codeforces.com/gym/100753)
* [UVA 13030 - Brain Fry](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=866&page=show_problem&problem=4918)
* [UVA 1027 - Toll](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3468)
* [UVA 11377 - Airport Setup](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2372)
* [Codeforces - Dynamic Shortest Path](http://codeforces.com/problemset/problem/843/D)
* [UVA 11813 - Shopping](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2913)
* [UVA 11833 - Route Change](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=226&page=show_problem&problem=2933)
* [SPOJ - Easy Dijkstra Problem](http://www.spoj.com/problems/EZDIJKST/en/)
* [LA - 2819 - Cave Raider](https://vjudge.net/problem/UVALive-2819)
* [UVA 12144 - Almost Shortest Path](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3296)
* [UVA 12047 - Highest Paid Toll](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3198)
* [UVA 11514 - Batman](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2509)
* [Codeforces - Team Rocket Rises Again](http://codeforces.com/contest/757/problem/F)
* [UVA - 11338 - Minefield](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2313)
* [UVA 11374 - Airport Express](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2369)
* [UVA 11097 - Poor My Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2038)
* [UVA 13172 - The music teacher](https://uva.onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=5083)
* [Codeforces - Dirty Arkady's Kitchen](http://codeforces.com/contest/827/problem/F)
* [SPOJ - Delivery Route](http://www.spoj.com/problems/DELIVER/)
* [SPOJ - Costly Chess](http://www.spoj.com/problems/CCHESS/)
* [CSES - Shortest Routes 1](https://cses.fi/problemset/task/1671)
* [CSES - Flight Discount](https://cses.fi/problemset/task/1195)
* [CSES - Flight Routes](https://cses.fi/problemset/task/1196)
