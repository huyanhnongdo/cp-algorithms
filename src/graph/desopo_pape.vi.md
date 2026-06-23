---
tags:
  - Translated
e_maxx_link: levit_algorithm
lang: vi
---

# Thuật toán D´Esopo-Pape

Cho một đồ thị gồm $n$ đỉnh và $m$ cạnh với trọng số $w_i$ và một đỉnh xuất phát $v_0$.
Yêu cầu tìm đường đi ngắn nhất từ đỉnh $v_0$ đến tất cả các đỉnh khác.

Thuật toán D´Esopo-Pape hoạt động nhanh hơn [Thuật toán Dijkstra](dijkstra.md) và [Thuật toán Bellman-Ford](bellman_ford.md) trong hầu hết các trường hợp, và cũng hoạt động được với đồ thị có cạnh âm.
Tuy nhiên, thuật toán không hoạt động được nếu đồ thị có chu trình âm.

## Mô tả

Gọi mảng $d$ lưu độ dài đường đi ngắn nhất, tức là $d_i$ là độ dài hiện tại của đường đi ngắn nhất từ đỉnh $v_0$ đến đỉnh $i$.
Ban đầu mảng này được điền giá trị vô cùng cho mọi đỉnh, ngoại trừ $d_{v_0} = 0$.
Sau khi thuật toán kết thúc, mảng này sẽ chứa các khoảng cách ngắn nhất cần tìm.

Gọi mảng $p$ chứa đỉnh cha hiện tại, tức là $p_i$ là đỉnh cha trực tiếp của đỉnh $i$ trên đường đi ngắn nhất hiện tại từ $v_0$ đến $i$.
Tương tự như mảng $d$, mảng $p$ cũng thay đổi dần dần trong quá trình chạy thuật toán và nhận các giá trị cuối cùng khi kết thúc.

Trong suốt quá trình chạy thuật toán, chúng ta duy trì ba tập hợp đỉnh:

- $M_0$ - các đỉnh đã được tính toán khoảng cách (mặc dù đó có thể chưa phải là khoảng cách cuối cùng tối ưu)
- $M_1$ - các đỉnh hiện đang được tính toán khoảng cách
- $M_2$ - các đỉnh chưa được tính toán khoảng cách

Các đỉnh trong tập hợp $M_1$ được lưu trữ trong một hàng đợi hai đầu (deque).

Tại mỗi bước của thuật toán, chúng ta lấy ra một đỉnh từ tập hợp $M_1$ (từ đầu hàng đợi).
Gọi $u$ là đỉnh được chọn.
Chúng ta đưa đỉnh $u$ này vào tập hợp $M_0$.
Sau đó, chúng ta duyệt qua tất cả các cạnh đi ra từ đỉnh này.
Gọi $v$ là đỉnh cuối của cạnh hiện tại, và $w$ là trọng số của nó.

- Nếu $v$ thuộc $M_2$, thì $v$ được thêm vào tập hợp $M_1$ bằng cách đẩy nó vào cuối hàng đợi.
Giá trị $d_v$ được gán bằng $d_u + w$.
- Nếu $v$ thuộc $M_1$, thì chúng ta cố gắng tối ưu hóa giá trị của $d_v$: $d_v = \min(d_v, d_u + w)$.
Vì $v$ đã nằm trong $M_1$ rồi, chúng ta không cần thêm nó vào $M_1$ hay hàng đợi nữa.
- Nếu $v$ thuộc $M_0$, và nếu $d_v$ có thể tối ưu hơn $d_v > d_u + w$, thì chúng ta cập nhật $d_v$ và đẩy đỉnh $v$ quay trở lại tập hợp $M_1$, bằng cách đặt nó vào đầu hàng đợi.

Và tất nhiên, với mỗi lần cập nhật mảng $d$, chúng ta cũng phải cập nhật phần tử tương ứng trong mảng $p$.

## Cài đặt

Chúng ta sẽ sử dụng mảng $m$ để lưu trữ xem mỗi đỉnh hiện tại đang nằm ở tập hợp nào.

```{.cpp file=desopo_pape}
struct Edge {
    int to, w;
};

int n;
vector<vector<Edge>> adj;

const int INF = 1e9;

void shortest_paths(int v0, vector<int>& d, vector<int>& p) {
    d.assign(n, INF);
    d[v0] = 0;
    vector<int> m(n, 2);
    deque<int> q;
    q.push_back(v0);
    p.assign(n, -1);

    while (!q.empty()) {
        int u = q.front();
        q.pop_front();
        m[u] = 0;
        for (Edge e : adj[u]) {
            if (d[e.to] > d[u] + e.w) {
                d[e.to] = d[u] + e.w;
                p[e.to] = u;
                if (m[e.to] == 2) {
                    m[e.to] = 1;
                    q.push_back(e.to);
                } else if (m[e.to] == 0) {
                    m[e.to] = 1;
                    q.push_front(e.to);
                }
            }
        }
    }
}
```

## Độ phức tạp

Thuật toán thường hoạt động rất nhanh - trong hầu hết các trường hợp, thậm chí còn nhanh hơn thuật toán Dijkstra.
Tuy nhiên, vẫn tồn tại những trường hợp mà thuật toán mất thời gian lũy thừa, khiến nó không phù hợp cho trường hợp xấu nhất. Xem thêm các thảo luận trên [Stack Overflow](https://stackoverflow.com/a/67642821) và [Codeforces](https://codeforces.com/blog/entry/3793) để tham khảo.
