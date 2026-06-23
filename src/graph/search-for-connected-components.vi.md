---
tags:
  - Translated
e_maxx_link: connected_components
lang: vi
---

# Tìm các thành phần liên thông trong đồ thị

Cho một đồ thị vô hướng $G$ với $n$ đỉnh và $m$ cạnh. Chúng ta cần tìm tất cả các thành phần liên thông của nó, tức là các nhóm đỉnh sao cho trong mỗi nhóm, bất kỳ đỉnh nào cũng có thể đi tới đỉnh khác và không tồn tại đường đi giữa các nhóm khác nhau.

## Thuật toán giải quyết bài toán

* Để giải quyết bài toán này, chúng ta có thể sử dụng Thuật toán tìm kiếm theo chiều sâu (Depth First Search - DFS) hoặc Thuật toán tìm kiếm theo chiều rộng (Breadth First Search - BFS).

* Trên thực tế, chúng ta sẽ thực hiện một loạt các lượt chạy DFS: Lượt chạy đầu tiên sẽ bắt đầu từ đỉnh đầu tiên và tất cả các đỉnh trong thành phần liên thông thứ nhất sẽ được duyệt qua (tìm thấy). Sau đó, chúng ta tìm đỉnh chưa được duyệt đầu tiên trong số các đỉnh còn lại, chạy DFS xuất phát từ đỉnh này để tìm thành phần liên thông thứ hai. Quá trình tiếp diễn cho đến khi tất cả các đỉnh đều đã được duyệt.

* Tổng thời gian chạy tiệm cận của thuật toán này là $O(n + m)$: Trong thực tế, thuật toán sẽ không duyệt lại cùng một đỉnh hai lần, nghĩa là mỗi cạnh sẽ được xem xét đúng hai lần (tại hai đầu của cạnh).

## Cài đặt

``` cpp
int n;
vector<vector<int>> adj;
vector<bool> used;
vector<int> comp;

void dfs(int v) {
    used[v] = true;
    comp.push_back(v);
    for (int u : adj[v]) {
        if (!used[u])
            dfs(u);
    }
}

void find_comps() {
    used.assign(n, false);
    for (int v = 0; v < n; ++v) {
        if (!used[v]) {
            comp.clear();
            dfs(v);
            cout << "Component:" ;
            for (int u : comp)
                cout << ' ' << u;
            cout << endl ;
        }
    }
}
```

* Hàm quan trọng nhất được sử dụng là `find_comps()`, có nhiệm vụ tìm và in ra các thành phần liên thông của đồ thị.

* Đồ thị được lưu trữ dưới dạng danh sách kề, tức là `adj[v]` chứa danh sách các đỉnh có cạnh nối từ đỉnh `v`.

* Vector `comp` chứa danh sách các đỉnh trong thành phần liên thông hiện tại.

## Cài đặt khử đệ quy (Iterative)

Các hàm đệ quy sâu nhìn chung là không tốt.
Mỗi lời gọi đệ quy sẽ yêu cầu một lượng nhỏ bộ nhớ trong stack, và mặc định các chương trình chỉ có một lượng không gian bộ nhớ stack hạn chế.
Vì thế, khi bạn thực hiện một thuật toán DFS đệ quy trên một đồ thị liên thông với hàng triệu đỉnh, bạn có thể gặp lỗi tràn bộ nhớ stack (stack overflow).

Chúng ta luôn có thể chuyển đổi một chương trình đệ quy sang chương trình khử đệ quy (iterative) bằng cách tự quản lý một cấu trúc dữ liệu ngăn xếp (stack).
Vì cấu trúc dữ liệu này được cấp phát trên bộ nhớ heap, lỗi tràn stack sẽ không xảy ra.

```cpp
int n;
vector<vector<int>> adj;
vector<bool> used;
vector<int> comp;

void dfs(int v) {
    stack<int> st;
    st.push(v);
    
    while (!st.empty()) {
        int curr = st.top();
        st.pop();
        if (!used[curr]) {
            used[curr] = true;
            comp.push_back(curr);
            for (int i = adj[curr].size() - 1; i >= 0; i--) {
                st.push(adj[curr][i]);
            }
        }
    }
}

void find_comps() {
    used.assign(n, false);
    for (int v = 0; v < n ; ++v) {
        if (!used[v]) {
            comp.clear();
            dfs(v);
            cout << "Component:" ;
            for (int u : comp)
                cout << ' ' << u;
            cout << endl ;
        }
    }
}
```

## Bài tập áp dụng
 - [SPOJ: CT23E](http://www.spoj.com/problems/CT23E/)
 - [CODECHEF: GERALD07](https://www.codechef.com/MARCH14/problems/GERALD07)
 - [CSES : Building Roads](https://cses.fi/problemset/task/1666)
