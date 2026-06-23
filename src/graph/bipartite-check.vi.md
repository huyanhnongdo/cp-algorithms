---
tags:
  - Translated
e_maxx_link: bipartite_checking
lang: vi
---

# Kiểm tra đồ thị hai phía

Một đồ thị hai phía (bipartite graph) là một đồ thị có tập đỉnh có thể phân hoạch thành hai tập hợp rời nhau sao cho mọi cạnh của đồ thị đều nối hai đỉnh thuộc hai tập hợp khác nhau (tức là không có cạnh nào nối các đỉnh trong cùng một tập hợp). Hai tập hợp này thường được gọi là hai phía.

Cho một đồ thị vô hướng. Hãy kiểm tra xem đồ thị có phải là đồ thị hai phía hay không, và nếu có, hãy đưa ra cách phân chia hai phía của nó.

## Thuật toán

Có một định lý chỉ ra rằng một đồ thị là đồ thị hai phía khi và chỉ khi mọi chu trình của nó đều có độ dài chẵn. Tuy nhiên, trên thực tế, việc sử dụng một cách phát biểu khác tương đương sẽ thuận tiện hơn: một đồ thị là đồ thị hai phía khi và chỉ khi nó có thể tô được bằng hai màu (two-colorable).

Chúng ta sẽ sử dụng một chuỗi các phép duyệt [theo chiều rộng (BFS)](breadth-first-search.md), bắt đầu từ mỗi đỉnh chưa được ghé thăm. Trong mỗi lượt duyệt, ta gán đỉnh xuất phát thuộc về phía 1 (hoặc tô màu 0). Mỗi khi ghé thăm một đỉnh lân cận chưa được duyệt của một đỉnh đã được gán phía, ta gán nó thuộc về phía còn lại (tô màu ngược lại). Khi duyệt qua một cạnh nối tới một đỉnh lân cận đã được ghé thăm từ trước, chúng ta kiểm tra xem đỉnh đó có thuộc phía khác hay không; nếu nó thuộc cùng một phía, chúng ta kết luận đồ thị không phải là hai phía. Một khi đã ghé thăm tất cả các đỉnh và gán phía cho chúng thành công, đồ thị là đồ thị hai phía và ta cũng dựng được luôn cách phân hoạch của nó.

## Cài đặt

```cpp
int n;
vector<vector<int>> adj;

vector<int> side(n, -1);
bool is_bipartite = true;
queue<int> q;
for (int st = 0; st < n; ++st) {
    if (side[st] == -1) {
        q.push(st);
        side[st] = 0;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int u : adj[v]) {
                if (side[u] == -1) {
                    side[u] = side[v] ^ 1;
                    q.push(u);
                } else {
                    is_bipartite &= side[u] != side[v];
                }
            }
        }
    }
}

cout << (is_bipartite ? "YES" : "NO") << endl;
```

### Bài tập thực hành:

- [SPOJ - BUGLIFE](http://www.spoj.com/problems/BUGLIFE/)
- [Codeforces - Graph Without Long Directed Paths](https://codeforces.com/contest/1144/problem/F)
- [Codeforces - String Coloring (easy version)](https://codeforces.com/contest/1296/problem/E1)
- [CSES : Building Teams](https://cses.fi/problemset/task/1668)
- [Codeforces - Alternating Path](https://codeforces.com/contest/2204/problem/D)
