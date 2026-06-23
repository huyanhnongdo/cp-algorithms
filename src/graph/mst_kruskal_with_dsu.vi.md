---
tags:
  - Translated
e_maxx_link: mst_kruskal_with_dsu
---

# Cây khung nhỏ nhất - Kruskal sử dụng Cấu trúc các tập hợp không giao nhau (DSU)

Để tìm hiểu chi tiết về bài toán MST và thuật toán Kruskal, trước tiên hãy xem [bài viết chính về thuật toán Kruskal](mst_kruskal.md).

Trong bài viết này, chúng ta sẽ xem xét cấu trúc dữ liệu ["Cấu trúc các tập hợp không giao nhau (Disjoint Set Union)"](../data_structures/disjoint_set_union.md) để cài đặt thuật toán Kruskal, giúp thuật toán đạt được độ phức tạp thời gian là $O(M \log N)$.

## Mô tả

Tương tự như phiên bản đơn giản của thuật toán Kruskal, chúng ta sắp xếp tất cả các cạnh của đồ thị theo thứ tự trọng số không giảm.
Sau đó, đưa mỗi đỉnh vào một cây riêng biệt (tức là tập hợp của chính nó) thông qua các cuộc gọi đến hàm `make_set` - bước này sẽ mất tổng cộng $O(N)$ thời gian.
Chúng ta duyệt qua tất cả các cạnh (theo thứ tự đã sắp xếp) và với mỗi cạnh, xác định xem hai đầu của nó có thuộc về hai cây khác nhau hay không (bằng cách thực hiện hai cuộc gọi hàm `find_set` với độ phức tạp $O(1)$ mỗi cuộc gọi).
Cuối cùng, chúng ta cần thực hiện phép hợp nhất (union) hai cây (tập hợp), thao tác này được thực hiện qua cuộc gọi hàm `union_sets` của DSU - cũng với độ phức tạp $O(1)$.
Nhờ đó, chúng ta thu được tổng độ phức tạp thời gian là $O(M \log N + N + M)$ = $O(M \log N)$.

## Cài đặt

Dưới đây là bản cài đặt của thuật toán Kruskal sử dụng Kỹ thuật gộp theo hạng (Union by Rank).

```cpp
vector<int> parent, rank;

void make_set(int v) {
    parent[v] = v;
    rank[v] = 0;
}

int find_set(int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (rank[a] < rank[b])
            swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b])
            rank[a]++;
    }
}

struct Edge {
    int u, v, weight;
    bool operator<(Edge const& other) {
        return weight < other.weight;
    }
};

int n;
vector<Edge> edges;

int cost = 0;
vector<Edge> result;
parent.resize(n);
rank.resize(n);
for (int i = 0; i < n; i++)
    make_set(i);

sort(edges.begin(), edges.end());

for (Edge e : edges) {
    if (find_set(e.u) != find_set(e.v)) {
        cost += e.weight;
        result.push_back(e);
        union_sets(e.u, e.v);
    }
}
```

Lưu ý: do cây khung nhỏ nhất (MST) sẽ chứa chính xác $N-1$ cạnh, chúng ta có thể dừng vòng lặp `for` ngay khi đã tìm đủ số lượng cạnh đó.

## Bài tập luyện tập

Xem [bài viết chính về thuật toán Kruskal](mst_kruskal.md) để biết danh sách các bài tập luyện tập về chủ đề này.
