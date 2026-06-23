---
tags:
  - Translated
e_maxx_link: negative_cycle
---

# Tìm chu trình âm trong đồ thị

Cho một đồ thị có hướng có trọng số $G$ gồm $N$ đỉnh và $M$ cạnh. Hãy tìm một chu trình bất kỳ có tổng trọng số âm trong đồ thị đó, nếu tồn tại chu trình như vậy.

Trong một cách phát biểu khác của bài toán, bạn cần tìm tất cả các cặp đỉnh mà giữa chúng có một đường đi với trọng số nhỏ tùy ý.

Chúng ta nên sử dụng các thuật toán khác nhau để giải quyết hai biến thể này của bài toán, do đó chúng ta sẽ thảo luận cả hai thuật toán ở đây.

## Sử dụng thuật toán Bellman-Ford

Thuật toán Bellman-Ford cho phép bạn kiểm tra xem có tồn tại chu trình có trọng số âm trong đồ thị hay không, và nếu có, tìm một trong các chu trình đó.

Các chi tiết của thuật toán được mô tả trong bài viết về thuật toán [Bellman-Ford](bellman_ford.md).
Ở đây chúng ta chỉ mô tả cách áp dụng nó cho bài toán này.

Bản cài đặt tiêu chuẩn của Bellman-Ford tìm kiếm chu trình âm có thể đi tới được từ một đỉnh bắt đầu $v$ nào đó; tuy nhiên, thuật toán có thể được sửa đổi để chỉ tìm một chu trình âm bất kỳ trong đồ thị.
Để làm được điều này, chúng ta cần gán tất cả các khoảng cách $d[i]$ bằng 0 thay vị vô cùng — giống như việc chúng ta đang tìm kiếm đường đi ngắn nhất từ tất cả các đỉnh đồng thời; tính đúng đắn của việc phát hiện chu trình âm không bị ảnh hưởng.

Thực hiện $N$ lần lặp của thuật toán Bellman-Ford. Nếu không có thay đổi nào ở lần lặp cuối cùng, thì đồ thị không có chu trình trọng số âm. Ngược lại, chọn một đỉnh có khoảng cách bị thay đổi, và đi ngược từ đỉnh đó qua các đỉnh cha cho đến khi tìm thấy một chu trình. Chu trình này chính là chu trình âm cần tìm.

### Cài đặt

```cpp
struct Edge {
    int a, b, cost;
};
 
int n;
vector<Edge> edges;
const int INF = 1000000000;
 
void solve() {
    vector<int> d(n, 0);
    vector<int> p(n, -1);
    int x;
 
    for (int i = 0; i < n; ++i) {
        x = -1;
        for (Edge e : edges) {
            if (d[e.a] + e.cost < d[e.b]) {
                d[e.b] = max(-INF, d[e.a] + e.cost);
                p[e.b] = e.a;
                x = e.b;
            }
        }
    }
 
    if (x == -1) {
        cout << "No negative cycle found.";
    } else {
        for (int i = 0; i < n; ++i)
            x = p[x];
 
        vector<int> cycle;
        for (int v = x;; v = p[v]) {
            cycle.push_back(v);
            if (v == x && cycle.size() > 1)
                break;
        }
        reverse(cycle.begin(), cycle.end());
 
        cout << "Negative cycle: ";
        for (int v : cycle)
            cout << v << ' ';
        cout << endl;
    }
}
```

## Sử dụng thuật toán Floyd-Warshall

Thuật toán Floyd-Warshall cho phép giải quyết biến thể thứ hai của bài toán - tìm tất cả các cặp đỉnh $(i, j)$ không có đường đi ngắn nhất giữa chúng (tức là tồn tại đường đi có trọng số nhỏ tùy ý).

Một lần nữa, chi tiết có thể được tìm thấy trong bài viết về [Floyd-Warshall](all-pair-shortest-path-floyd-warshall.md), và ở đây chúng ta chỉ mô tả ứng dụng của nó.

Chạy thuật toán Floyd-Warshall trên đồ thị.
Ban đầu $d[v][v] = 0$ với mỗi đỉnh $v$.
Nhưng sau khi chạy thuật toán, $d[v][v]$ sẽ nhỏ hơn $0$ nếu tồn tại một đường đi có độ dài âm từ $v$ đến $v$.
Chúng ta có thể sử dụng điều này để tìm tất cả các cặp đỉnh không có đường đi ngắn nhất giữa chúng.
Chúng ta duyệt qua tất cả các cặp đỉnh $(i, j)$ và kiểm tra xem có đường đi ngắn nhất giữa chúng hay không.
Để làm được điều này, hãy thử tất cả các khả năng của đỉnh trung gian $t$.
Cặp $(i, j)$ không có đường đi ngắn nhất nếu tồn tại một đỉnh trung gian $t$ thỏa mãn $d[t][t] < 0$ (tức là $t$ thuộc một chu trình âm), đồng thời từ $i$ có thể đi tới $t$ và từ $t$ có thể đi tới $j$.
Khi đó, đường đi từ $i$ đến $j$ có thể có trọng số nhỏ tùy ý.
Chúng sẽ ký hiệu điều này bằng `-INF`.

### Cài đặt

```cpp
for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
        for (int t = 0; t < n; ++t) {
            if (d[i][t] < INF && d[t][t] < 0 && d[t][j] < INF)
                d[i][j] = - INF; 
        }
    }
}
```

## Bài tập luyện tập

- [UVA: Wormholes](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=499)
- [SPOJ: Alice in Amsterdam, I mean Wonderland](http://www.spoj.com/problems/UCV2013B/)
- [SPOJ: Johnsons Algorithm](http://www.spoj.com/problems/JHNSN/)
