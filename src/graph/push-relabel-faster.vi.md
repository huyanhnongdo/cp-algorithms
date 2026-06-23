---
tags:
  - Translated
e_maxx_link: preflow_push_faster
lang: vi
---

# Luồng cực đại - Thuật toán Push-relabel cải tiến

Chúng ta sẽ sửa đổi [phương pháp push-relabel](push-relabel.md) để đạt được thời gian chạy tốt hơn.

## Mô tả

Sự sửa đổi này cực kỳ đơn giản:
Trong bài viết trước, chúng ta chọn một đỉnh có lượng dư bất kỳ mà không theo quy tắc cụ thể nào.
Tuy nhiên, hóa ra nếu chúng ta luôn chọn đỉnh có **chiều cao lớn nhất**, rồi thực hiện các thao tác đẩy luồng (push) và áp nhãn (relabel) trên đó, thì độ phức tạp thuật toán sẽ tốt hơn rất nhiều.
Hơn nữa, để chọn đỉnh có chiều cao lớn nhất, thực tế chúng ta không cần bất kỳ cấu trúc dữ liệu phức tạp nào. Chúng ta chỉ cần lưu trữ các đỉnh có chiều cao lớn nhất trong một danh sách, và tính toán lại danh sách này khi tất cả chúng đều đã được xử lý (khi đó các đỉnh có chiều cao thấp hơn sẽ được đưa vào danh sách), hoặc bất cứ khi nào xuất hiện một đỉnh mới có lượng dư và chiều cao lớn hơn (sau khi áp lại nhãn cho một đỉnh nào đó).

Mặc dù đơn giản, sửa đổi này giúp giảm độ phức tạp đi rất nhiều.
Cụ thể, độ phức tạp của thuật toán thu được là $O(V E + V^2 \sqrt{E})$, trong trường hợp xấu nhất là $O(V^3)$.

Sửa đổi này được đề xuất bởi Cheriyan và Maheshwari vào năm 1989.

## Cài đặt

```{.cpp file=push_relabel_faster}
const int inf = 1000000000;

int n;
vector<vector<int>> capacity, flow;
vector<int> height, excess;

void push(int u, int v)
{
    int d = min(excess[u], capacity[u][v] - flow[u][v]);
    flow[u][v] += d;
    flow[v][u] -= d;
    excess[u] -= d;
    excess[v] += d;
}

void relabel(int u)
{
    int d = inf;
    for (int i = 0; i < n; i++) {
        if (capacity[u][i] - flow[u][i] > 0)
            d = min(d, height[i]);
    }
    if (d < inf)
        height[u] = d + 1;
}

vector<int> find_max_height_vertices(int s, int t) {
    vector<int> max_height;
    for (int i = 0; i < n; i++) {
        if (i != s && i != t && excess[i] > 0) {
            if (!max_height.empty() && height[i] > height[max_height[0]])
                max_height.clear();
            if (max_height.empty() || height[i] == height[max_height[0]])
                max_height.push_back(i);
        }
    }
    return max_height;
}

int max_flow(int s, int t)
{
    height.assign(n, 0);
    height[s] = n;
    flow.assign(n, vector<int>(n, 0));
    excess.assign(n, 0);
    excess[s] = inf;
    for (int i = 0; i < n; i++) {
        if (i != s)
            push(s, i);
    }

    vector<int> current;
    while (!(current = find_max_height_vertices(s, t)).empty()) {
        for (int i : current) {
            bool pushed = false;
            for (int j = 0; j < n && excess[i]; j++) {
                if (capacity[i][j] - flow[i][j] > 0 && height[i] == height[j] + 1) {
                    push(i, j);
                    pushed = true;
                }
            }
            if (!pushed) {
                relabel(i);
                break;
            }
        }
    }

    return excess[t];
}
```
