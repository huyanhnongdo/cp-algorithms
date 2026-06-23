---
tags:
  - Original
lang: vi
---

# Luồng cực đại - Thuật toán MPM

Thuật toán MPM (Malhotra, Pramodh-Kumar và Maheshwari) giải quyết bài toán luồng cực đại trong thời gian $O(V^3)$. Thuật toán này tương tự như [Thuật toán Dinic](dinic.md).

## Thuật toán

Giống như thuật toán Dinic, MPM hoạt động theo từng pha. Trong mỗi pha, chúng ta tìm luồng cản (blocking flow) trên mạng phân tầng (layered network) của mạng thặng dư của $G$.
Điểm khác biệt chính so với thuật toán Dinic nằm ở cách chúng ta tìm luồng cản.
Xét mạng phân tầng $L$.
Với mỗi nút, chúng ta định nghĩa _thế trong_ (inner potential) và _thế ngoài_ (outer potential) của nó như sau:

$$\begin{align}
p_{in}(v) &= \sum\limits_{(u, v)\in L}(c(u, v) - f(u, v)) \\\\
p_{out}(v) &= \sum\limits_{(v, u)\in L}(c(v, u) - f(v, u))
\end{align}$$

Chúng ta cũng đặt $p_{in}(s) = p_{out}(t) = \infty$.
Từ $p_{in}$ và $p_{out}$, chúng ta định nghĩa _thế_ (potential) của nút là $p(v) = \min(p_{in}(v), p_{out}(v))$.
Chúng ta gọi một nút $r$ là _nút tham chiếu_ (reference node) nếu $p(r) = \min\{p(v)\}$.
Xét một nút tham chiếu $r$.
Chúng ta khẳng định rằng luồng có thể được tăng thêm một lượng bằng $p(r)$ sao cho $p(r)$ trở thành $0$.
Điều này đúng vì $L$ không có chu trình, do đó chúng ta có thể đẩy luồng ra khỏi $r$ bằng các cạnh đi ra và nó chắc chắn sẽ tới được $t$ vì mọi nút trung gian đều có đủ thế ngoài để đẩy tiếp lượng luồng này đi khi luồng tới nó.
Tương tự, chúng ta có thể kéo luồng ngược lại từ $s$.
Việc xây dựng luồng cản được dựa trên thực tế này.
Trong mỗi bước lặp, chúng ta tìm một nút tham chiếu và đẩy luồng từ $s$ đến $t$ đi qua $r$.
Quá trình này có thể được mô phỏng bằng thuật toán BFS.
Tất cả các cạnh đã bão hòa hoàn toàn có thể được xóa khỏi $L$ vì chúng sẽ không được sử dụng lại trong pha này nữa.
Tương tự, tất cả các nút khác $s$ và $t$ mà không có cạnh đi vào hoặc cạnh đi ra cũng có thể được xóa bỏ.

Mỗi pha hoạt động trong thời gian $O(V^2)$ vì có tối đa $V$ bước lặp (do ít nhất nút tham chiếu được chọn sẽ bị xóa), và trong mỗi bước lặp chúng ta xóa tất cả các cạnh đã đi qua ngoại trừ tối đa $V$ cạnh.
Tổng hợp lại, ta được $O(V^2 + E) = O(V^2)$.
Vì có ít hơn $V$ pha (xem chứng minh [tại đây](dinic.md)), tổng thời gian hoạt động của MPM là $O(V^3)$.

## Cài đặt

```{.cpp file=mpm}
struct MPM{
    struct FlowEdge{
        int v, u;
        long long cap, flow;
        FlowEdge(){}
        FlowEdge(int _v, int _u, long long _cap, long long _flow)
            : v(_v), u(_u), cap(_cap), flow(_flow){}
        FlowEdge(int _v, int _u, long long _cap)
            : v(_v), u(_u), cap(_cap), flow(0ll){}
    };
    const long long flow_inf = 1e18;
    vector<FlowEdge> edges;
    vector<char> alive;
    vector<long long> pin, pout;
    vector<list<int> > in, out;
    vector<vector<int> > adj;
    vector<long long> ex;
    int n, m = 0;
    int s, t;
    vector<int> level;
    vector<int> q;
    int qh, qt;
    void resize(int _n){
        n = _n;
        ex.resize(n);
        q.resize(n);
        pin.resize(n);
        pout.resize(n);
        adj.resize(n);
        level.resize(n);
        in.resize(n);
        out.resize(n);
    }
    MPM(){}
    MPM(int _n, int _s, int _t){resize(_n); s = _s; t = _t;}
    void add_edge(int v, int u, long long cap){
        edges.push_back(FlowEdge(v, u, cap));
        edges.push_back(FlowEdge(u, v, 0));
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
    }
    bool bfs(){
        while(qh < qt){
            int v = q[qh++];
            for(int id : adj[v]){
                if(edges[id].cap - edges[id].flow < 1)continue;
                if(level[edges[id].u] != -1)continue;
                level[edges[id].u] = level[v] + 1;
                q[qt++] = edges[id].u;
            }
        }
        return level[t] != -1;
    }
    long long pot(int v){
        return min(pin[v], pout[v]);
    }
    void remove_node(int v){
        for(int i : in[v]){
            int u = edges[i].v;
            auto it = find(out[u].begin(), out[u].end(), i);
            out[u].erase(it);
            pout[u] -= edges[i].cap - edges[i].flow;
        }
        for(int i : out[v]){
            int u = edges[i].u;
            auto it = find(in[u].begin(), in[u].end(), i);
            in[u].erase(it);
            pin[u] -= edges[i].cap - edges[i].flow;
        }
    }
    void push(int from, int to, long long f, bool forw){
        qh = qt = 0;
        ex.assign(n, 0);
        ex[from] = f;
        q[qt++] = from;
        while(qh < qt){
            int v = q[qh++];
            if(v == to)
                break;
            long long must = ex[v];
            auto it = forw ? out[v].begin() : in[v].begin();
            while(true){
                int u = forw ? edges[*it].u : edges[*it].v;
                long long pushed = min(must, edges[*it].cap - edges[*it].flow);
                if(pushed == 0)break;
                if(forw){
                    pout[v] -= pushed;
                    pin[u] -= pushed;
                }
                else{
                    pin[v] -= pushed;
                    pout[u] -= pushed;
                }
                if(ex[u] == 0)
                    q[qt++] = u;
                ex[u] += pushed;
                edges[*it].flow += pushed;
                edges[(*it)^1].flow -= pushed;
                must -= pushed;
                if(edges[*it].cap - edges[*it].flow == 0){
                    auto jt = it;
                    ++jt;
                    if(forw){
                        in[u].erase(find(in[u].begin(), in[u].end(), *it));
                        out[v].erase(it);
                    }
                    else{
                        out[u].erase(find(out[u].begin(), out[u].end(), *it));
                        in[v].erase(it);
                    }
                    it = jt;
                }
                else break;
                if(!must)break;
            }
        }
    }
    long long flow(){
        long long ans = 0;
        while(true){
            pin.assign(n, 0);
            pout.assign(n, 0);
            level.assign(n, -1);
            alive.assign(n, true);
            level[s] = 0;
            qh = 0; qt = 1;
            q[0] = s;
            if(!bfs())
                break;
            for(int i = 0; i < n; i++){
                out[i].clear();
                in[i].clear();
            }
            for(int i = 0; i < m; i++){
                if(edges[i].cap - edges[i].flow == 0)
                    continue;
                int v = edges[i].v, u = edges[i].u;
                if(level[v] + 1 == level[u] && (level[u] < level[t] || u == t)){
                    in[u].push_back(i);
                    out[v].push_back(i);
                    pin[u] += edges[i].cap - edges[i].flow;
                    pout[v] += edges[i].cap - edges[i].flow;
                }
            }
            pin[s] = pout[t] = flow_inf;
            while(true){
                int v = -1;
                for(int i = 0; i < n; i++){
                    if(!alive[i])continue;
                    if(v == -1 || pot(i) < pot(v))
                        v = i;
                }
                if(v == -1)
                    break;
                if(pot(v) == 0){
                    alive[v] = false;
                    remove_node(v);
                    continue;
                }
                long long f = pot(v);
                ans += f;
                push(v, s, f, false);
                push(v, t, f, true);
                alive[v] = false;
                remove_node(v);
            }
        }
        return ans;
    }
};
```
