---
tags:
  - Translated
e_maxx_link: dinic
lang: vi
---

# Luồng cực đại - Thuật toán Dinic

Thuật toán Dinic giải quyết bài toán luồng cực đại trong thời gian $O(V^2E)$. Bài toán luồng cực đại được định nghĩa chi tiết trong bài viết [Luồng cực đại - Ford-Fulkerson và Edmonds-Karp](edmonds_karp.md). Thuật toán này được phát hiện bởi Yefim Dinitz vào năm 1970.

## Định nghĩa

Một **mạng thặng dư** (residual network) $G^R$ của mạng $G$ là một mạng chứa hai cạnh ứng với mỗi cạnh $(v, u)\in G$:<br>

- Cạnh $(v, u)$ với sức chứa $c_{vu}^R = c_{vu} - f_{vu}$
- Cạnh $(u, v)$ với sức chứa $c_{uv}^R = f_{vu}$

Một **luồng cản** (blocking flow) của một mạng là một luồng sao cho mọi đường đi từ $s$ đến $t$ đều chứa ít nhất một cạnh bị bão hòa bởi luồng này. Lưu ý rằng luồng cản không nhất thiết phải là luồng cực đại.

Một **mạng phân tầng** (layered network) của mạng $G$ là một mạng được xây dựng như sau: Đầu tiên, đối với mỗi đỉnh $v$, chúng ta tính $level[v]$ là đường đi ngắn nhất (không có trọng số) từ $s$ đến đỉnh này chỉ sử dụng các cạnh có sức chứa dương. Sau đó, chúng ta chỉ giữ lại những cạnh $(v, u)$ thỏa mãn $level[v] + 1 = level[u]$. Rõ ràng, mạng phân tầng này là một đồ thị có hướng không chu trình (DAG).

## Thuật toán

Thuật toán bao gồm nhiều pha. Ở mỗi pha, chúng ta xây dựng mạng phân tầng của mạng thặng dư của $G$. Sau đó, chúng ta tìm một luồng cản bất kỳ trong mạng phân tầng và cộng nó vào luồng hiện tại.

## Chứng minh tính đúng đắn

Hãy chỉ ra rằng nếu thuật toán kết thúc, nó sẽ tìm được luồng cực đại.

Nếu thuật toán kết thúc, điều đó có nghĩa là nó không thể tìm thêm bất kỳ luồng cản nào trong mạng phân tầng. Điều này đồng nghĩa với việc mạng phân tầng không còn đường đi từ $s$ đến $t$. Tức là mạng thặng dư cũng không có đường đi từ $s$ đến $t$. Do đó, luồng hiện tại là luồng cực đại.

## Số lượng pha

Thuật toán kết thúc sau ít hơn $V$ pha. Để chứng minh điều này, trước hết chúng ta cần chứng minh hai bổ đề sau.

**Bổ đề 1.** Khoảng cách từ $s$ đến mỗi đỉnh không giảm sau mỗi bước lặp, tức là $level_{i+1}[v] \ge level_i[v]$.

**Chứng minh.** Xét một pha $i$ và một đỉnh $v$ cố định. Xét một đường đi ngắn nhất $P$ bất kỳ từ $s$ đến $v$ trong $G_{i+1}^R$. Độ dài của $P$ bằng $level_{i+1}[v]$. Lưu ý rằng $G_{i+1}^R$ chỉ có thể chứa các cạnh từ $G_i^R$ và các cạnh ngược của các cạnh thuộc $G_i^R$. Nếu $P$ không chứa cạnh ngược nào của $G_i^R$, thì $level_{i+1}[v] \ge level_i[v]$ vì $P$ cũng là một đường đi trong $G_i^R$. Bây giờ, giả sử $P$ chứa ít nhất một cạnh ngược. Gọi cạnh ngược đầu tiên như vậy là $(u, w)$. Khi đó $level_{i+1}[u] \ge level_i[u]$ (theo trường hợp đầu tiên). Cạnh $(u, w)$ không thuộc $G_i^R$, nên cạnh ngược của nó là $(w, u)$ đã bị ảnh hưởng bởi luồng cản ở bước lặp trước. Điều này có nghĩa là $level_i[u] = level_i[w] + 1$. Hơn nữa, $level_{i+1}[w] = level_{i+1}[u] + 1$. Từ hai phương trình này và $level_{i+1}[u] \ge level_i[u]$, ta suy ra $level_{i+1}[w] \ge level_i[w] + 2$. Bây giờ chúng ta có thể áp dụng tương tự ý tưởng này cho phần còn lại của đường đi $P$.

**Bổ đề 2.** $level_{i+1}[t] > level_i[t]$

**Chứng minh.** Từ bổ đề trước, ta có $level_{i+1}[t] \ge level_i[t]$. Giả sử $level_{i+1}[t] = level_i[t]$. Lưu ý rằng $G_{i+1}^R$ chỉ có thể chứa các cạnh từ $G_i^R$ và các cạnh ngược của các cạnh thuộc $G_i^R$. Điều này có nghĩa là tồn tại một đường đi ngắn nhất trong $G_i^R$ không bị chặn bởi luồng cản. Điều này dẫn tới mâu thuẫn.

Từ hai bổ đề trên, chúng ta kết luận rằng có ít hơn $V$ pha vì $level[t]$ tăng dần sau mỗi pha, nhưng nó không thể vượt quá $V - 1$.

## Tìm luồng cản

Để tìm luồng cản ở mỗi bước lặp, chúng ta có thể chỉ đơn giản thử đẩy luồng bằng thuật toán DFS từ $s$ đến $t$ trong mạng phân tầng chừng nào luồng vẫn còn có thể đẩy được. Để thực hiện việc này nhanh hơn, chúng ta phải loại bỏ các cạnh không thể dùng để đẩy luồng được nữa. Để làm được điều này, chúng ta có thể duy trì một con trỏ ở mỗi đỉnh để chỉ ra cạnh tiếp theo có thể sử dụng.

Một lần chạy DFS đơn lẻ mất thời gian $O(k+V)$, trong đó $k$ là số lần dịch chuyển con trỏ trong lần chạy này. Tổng số lần dịch chuyển con trỏ qua tất cả các lần chạy không vượt quá $E$. Mặt khác, tổng số lần chạy DFS sẽ không vượt quá $E$, vì mỗi lần chạy sẽ làm bão hòa ít nhất một cạnh. Bằng cách này, tổng thời gian chạy để tìm luồng cản là $O(VE)$.

## Độ phức tạp

Vì có ít hơn $V$ pha, tổng độ phức tạp của thuật toán là $O(V^2E)$.

## Mạng đơn vị

Một **mạng đơn vị** (unit network) là một mạng mà đối với mọi đỉnh ngoại trừ $s$ và $t$, **hoặc cạnh đi vào hoặc cạnh đi ra là duy nhất và có sức chứa đơn vị (bằng 1)**. Đây chính là trường hợp của mạng được xây dựng để giải quyết bài toán ghép cặp cực đại bằng luồng.

Trên mạng đơn vị, thuật toán Dinic hoạt động trong thời gian $O(E\sqrt{V})$. Hãy chứng minh điều này.

Đầu tiên, mỗi pha hiện tại hoạt động trong thời gian $O(E)$ vì mỗi cạnh sẽ được xem xét tối đa một lần.

Thứ hai, giả sử đã thực hiện được $\sqrt{V}$ pha. Khi đó, tất cả các đường tăng luồng có độ dài $\le\sqrt{V}$ đều đã được tìm thấy. Gọi $f$ là luồng hiện tại, $f'$ là luồng cực đại. Xét hiệu của chúng $f' - f$. Đây là một luồng trong $G^R$ có giá trị $|f'| - |f|$ và trên mỗi cạnh nó nhận giá trị $0$ hoặc $1$. Luồng này có thể được phân rã thành $|f'| - |f|$ đường đi từ $s$ đến $t$ và có thể có thêm các chu trình. Vì đây là mạng đơn vị, các đường đi này không thể có đỉnh chung, do đó tổng số đỉnh phải $\ge (|f'| - |f|)\sqrt{V}$, nhưng nó cũng phải $\le V$. Do đó, trong tối đa $\sqrt{V}$ bước lặp tiếp theo, chúng ta chắc chắn sẽ tìm được luồng cực đại.

### Mạng có sức chứa đơn vị

Trong một trường hợp tổng quát hơn khi tất cả các cạnh có sức chứa đơn vị, _nhưng số lượng cạnh đi vào và đi ra là không giới hạn_, các đường đi không thể có cạnh chung thay vì không có đỉnh chung. Theo cách tương tự, điều này cho phép chứng minh số pha bị chặn bởi $\sqrt E$, do đó thời gian chạy của thuật toán Dinic trên các mạng này tối đa là $O(E \sqrt E)$.

Cuối cùng, ta cũng có thể chứng minh rằng số pha trên mạng có sức chứa đơn vị không vượt quá $O(V^{2/3})$, cung cấp một đánh giá thay thế là $O(EV^{2/3})$ trên các mạng có số lượng cạnh đặc biệt lớn.

## Cài đặt

```{.cpp file=dinic}
struct FlowEdge {
    int v, u;
    long long cap, flow = 0;
    FlowEdge(int v, int u, long long cap) : v(v), u(u), cap(cap) {}
};

struct Dinic {
    const long long flow_inf = 1e18;
    vector<FlowEdge> edges;
    vector<vector<int>> adj;
    int n, m = 0;
    int s, t;
    vector<int> level, ptr;
    queue<int> q;

    Dinic(int n, int s, int t) : n(n), s(s), t(t) {
        adj.resize(n);
        level.resize(n);
        ptr.resize(n);
    }

    void add_edge(int v, int u, long long cap) {
        edges.emplace_back(v, u, cap);
        edges.emplace_back(u, v, 0);
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
    }

    bool bfs() {
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int id : adj[v]) {
                if (edges[id].cap == edges[id].flow)
                    continue;
                if (level[edges[id].u] != -1)
                    continue;
                level[edges[id].u] = level[v] + 1;
                q.push(edges[id].u);
            }
        }
        return level[t] != -1;
    }

    long long dfs(int v, long long pushed) {
        if (pushed == 0)
            return 0;
        if (v == t)
            return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); cid++) {
            int id = adj[v][cid];
            int u = edges[id].u;
            if (level[v] + 1 != level[u])
                continue;
            long long tr = dfs(u, min(pushed, edges[id].cap - edges[id].flow));
            if (tr == 0)
                continue;
            edges[id].flow += tr;
            edges[id ^ 1].flow -= tr;
            return tr;
        }
        return 0;
    }

    long long flow() {
        long long f = 0;
        while (true) {
            fill(level.begin(), level.end(), -1);
            level[s] = 0;
            q.push(s);
            if (!bfs())
                break;
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, flow_inf)) {
                f += pushed;
            }
        }
        return f;
    }
};
```

## Bài tập thực hành

* [SPOJ: FASTFLOW](https://www.spoj.com/problems/FASTFLOW/)
