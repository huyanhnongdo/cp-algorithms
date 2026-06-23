---
title: Kiểm tra tính không chu trình và tìm chu trình trên đồ thị trong O(M)
tags:
  - Translated
e_maxx_link: finding_cycle
---

# Kiểm tra tính không chu trình và tìm chu trình trên đồ thị trong $O(M)$

Xét một đồ thị có hướng hoặc vô hướng không có khuyên (loops) và đa cạnh (multiple edges). Chúng ta cần kiểm tra xem đồ thị đó có không chu trình (acyclic) hay không, và nếu có chu trình, hãy tìm ra một chu trình bất kỳ.

Chúng ta có thể giải quyết bài toán này bằng cách sử dụng [Tìm kiếm theo chiều sâu](depth-first-search.md) (DFS) với độ phức tạp $O(M)$, trong đó $M$ là số cạnh của đồ thị.

## Thuật toán

Chúng ta sẽ chạy một chuỗi các DFS trong đồ thị. Ban đầu, tất cả các đỉnh đều được tô màu trắng (0). Từ mỗi đỉnh chưa được ghé thăm (màu trắng), bắt đầu chạy DFS, tô màu xám (1) khi đi vào đỉnh và tô màu đen (2) khi đi ra khỏi đỉnh. Nếu DFS đi đến một đỉnh màu xám, điều đó có nghĩa là chúng ta đã tìm thấy một chu trình (nếu là đồ thị vô hướng, cạnh dẫn đến đỉnh cha sẽ không được xem xét).

Bản thân chu trình có thể được dựng lại bằng cách sử dụng mảng đỉnh cha (parent array).

## Cài đặt

Dưới đây là bản cài đặt dành cho đồ thị có hướng.

```cpp
int n;
vector<vector<int>> adj;
vector<char> color;
vector<int> parent;
int cycle_start, cycle_end;

bool dfs(int v) {
    color[v] = 1;
    for (int u : adj[v]) {
        if (color[u] == 0) {
            parent[u] = v;
            if (dfs(u))
                return true;
        } else if (color[u] == 1) {
            cycle_end = v;
            cycle_start = u;
            return true;
        }
    }
    color[v] = 2;
    return false;
}

void find_cycle() {
    color.assign(n, 0);
    parent.assign(n, -1);
    cycle_start = -1;

    for (int v = 0; v < n; v++) {
        if (color[v] == 0 && dfs(v))
            break;
    }

    if (cycle_start == -1) {
        cout << "Acyclic" << endl;
    } else {
        vector<int> cycle;
        cycle.push_back(cycle_start);
        for (int v = cycle_end; v != cycle_start; v = parent[v])
            cycle.push_back(v);
        cycle.push_back(cycle_start);
        reverse(cycle.begin(), cycle.end());

        cout << "Cycle found: ";
        for (int v : cycle)
            cout << v << " ";
        cout << endl;
    }
}
```

Dưới đây là bản cài đặt dành cho đồ thị vô hướng.
Lưu ý rằng trong phiên bản vô hướng, nếu một đỉnh `v` được tô màu đen, nó sẽ không bao giờ được ghé thăm lại bởi DFS.
Điều này là do chúng ta đã khám phá tất cả các cạnh kết nối của `v` khi ghé thăm nó lần đầu tiên.
Thành phần liên thông chứa `v` (sau khi loại bỏ cạnh giữa `v` và cha của nó) phải là một cây, nếu DFS đã hoàn tất xử lý `v` mà không tìm thấy chu trình.
Vì vậy, chúng ta thậm chí không cần phân biệt giữa trạng thái xám và đen.
Do đó, chúng ta có thể chuyển vector kiểu char `color` thành vector kiểu boolean `visited`.

```cpp
int n;
vector<vector<int>> adj;
vector<bool> visited;
vector<int> parent;
int cycle_start, cycle_end;

bool dfs(int v, int par) { // passing vertex and its parent vertex
    visited[v] = true;
    for (int u : adj[v]) {
        if(u == par) continue; // skipping edge to parent vertex
        if (visited[u]) {
            cycle_end = v;
            cycle_start = u;
            return true;
        }
        parent[u] = v;
        if (dfs(u, parent[u]))
            return true;
    }
    return false;
}

void find_cycle() {
    visited.assign(n, false);
    parent.assign(n, -1);
    cycle_start = -1;

    for (int v = 0; v < n; v++) {
        if (!visited[v] && dfs(v, parent[v]))
            break;
    }

    if (cycle_start == -1) {
        cout << "Acyclic" << endl;
    } else {
        vector<int> cycle;
        cycle.push_back(cycle_start);
        for (int v = cycle_end; v != cycle_start; v = parent[v])
            cycle.push_back(v);
        cycle.push_back(cycle_start);

        cout << "Cycle found: ";
        for (int v : cycle)
            cout << v << " ";
        cout << endl;
    }
}
```

### Bài tập luyện tập:

- [AtCoder : Reachability in Functional Graph](https://atcoder.jp/contests/abc357/tasks/abc357_e)
- [CSES : Round Trip](https://cses.fi/problemset/task/1669)
- [CSES : Round Trip II](https://cses.fi/problemset/task/1678/)
