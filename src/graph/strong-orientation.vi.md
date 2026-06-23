---
tags:
  - Translated
---

# Định hướng mạnh

Một **định hướng mạnh** (strong orientation) của một đồ thị vô hướng là việc gán chiều cho mỗi cạnh của đồ thị để biến nó thành một [đồ thị liên thông mạnh](strongly-connected-components.md).
Nghĩa là sau khi *định hướng*, chúng ta có thể đi từ bất kỳ đỉnh nào tới bất kỳ đỉnh nào khác bằng cách đi theo các cạnh có hướng.

## Lời giải

Tất nhiên, việc này không thể thực hiện được cho *mọi* đồ thị.
Hãy xem xét một [cầu](bridge-searching.md) trong đồ thị.
Chúng ta phải gán hướng cho cầu đó và khi làm vậy chúng ta chỉ có thể "qua cầu" theo một hướng duy nhất. Điều đó có nghĩa là không thể đi từ một trong hai đầu cầu sang đầu cầu còn lại, nên không thể làm cho đồ thị liên thông mạnh được.

Bây giờ hãy xem xét một lượt duyệt [DFS](depth-first-search.md) qua một đồ thị liên thông không có cầu.
Rõ ràng, chúng ta sẽ ghé thăm mọi đỉnh.
Và vì đồ thị không có cầu, chúng ta có thể loại bỏ bất kỳ cạnh cây DFS nào mà vẫn có thể đi từ phía dưới cạnh đó lên phía trên cạnh bằng cách sử dụng một đường đi chứa ít nhất một cạnh ngược.
Từ đó suy ra rằng từ bất kỳ đỉnh nào chúng ta cũng có thể đi đến gốc của cây DFS.
Đồng thời, từ gốc của cây DFS chúng ta có thể đi tới bất kỳ đỉnh nào tùy ý.
Chúng ta đã tìm thấy một định hướng mạnh!

Nói cách khác, để định hướng mạnh một đồ thị liên thông không có cầu:
chạy DFS trên đồ thị và cho các cạnh thuộc cây DFS hướng đi từ gốc DFS ra xa, còn tất cả các cạnh khác hướng từ nút con cháu lên nút tổ tiên trong cây DFS.

Kết quả khẳng định rằng các đồ thị liên thông không có cầu là các đồ thị duy nhất có định hướng mạnh được gọi là **Định lý Robbins**.

## Mở rộng bài toán

Chúng ta hãy xem xét bài toán tìm định hướng của đồ thị sao cho số lượng thành phần liên thông mạnh (SCC) thu được là tối thiểu.

Tất nhiên, mỗi thành phần liên thông lớn của đồ thị có thể được xem xét độc lập.
Bây giờ, vì chỉ các đồ thị không có cầu mới có thể định hướng mạnh được, hãy tạm thời loại bỏ tất cả các cầu.
Chúng ta sẽ thu được một số thành phần liên thông không có cầu
(chính xác bằng *số lượng thành phần liên thông ban đầu* + *số lượng cầu*)
và chúng ta biết rằng có thể định hướng mạnh cho mỗi thành phần đó.

Chúng ta chỉ được phép định hướng các cạnh chứ không được loại bỏ chúng, nhưng thực tế cho thấy chúng ta có thể định hướng các cầu một cách tùy ý.
Tất nhiên, cách đơn giản nhất để định hướng chúng là chạy thuật toán mô tả ở trên mà không có sửa đổi nào trên từng thành phần liên thông gốc của đồ thị.

### Cài đặt

Ở đây, đầu vào gồm: *n* — số đỉnh, *m* — số cạnh, tiếp theo là *m* dòng mô tả các cạnh.

Đầu ra dòng đầu tiên là số lượng SCC tối thiểu, dòng thứ hai là một chuỗi gồm *m* ký tự:
hoặc `>` — biểu thị cạnh tương ứng từ đầu vào được định hướng từ đỉnh bên trái sang đỉnh bên phải (như trong đầu vào),
hoặc `<` — hướng ngược lại.

Đây là thuật toán tìm cầu được sửa đổi để kết hợp định hướng các cạnh. Bạn cũng có thể định hướng các cạnh ở bước đầu tiên và đếm số SCC trên đồ thị có hướng ở bước thứ hai.

```cpp
vector<vector<pair<int, int>>> adj; // adjacency list - vertex and edge pairs
vector<pair<int, int>> edges;

vector<int> tin, low;
int bridge_cnt;
string orient;
vector<bool> edge_used;
void find_bridges(int v) {
	static int time = 0;
	low[v] = tin[v] = time++;
	for (auto p : adj[v]) {
		if (edge_used[p.second]) continue;
		edge_used[p.second] = true;
		orient[p.second] = v == edges[p.second].first ? '>' : '<';
		int nv = p.first;
		if (tin[nv] == -1) { // if nv is not visited yet
			find_bridges(nv);
			low[v] = min(low[v], low[nv]);
			if (low[nv] > tin[v]) {
				// a bridge between v and nv
				bridge_cnt++;
			}
		} else {
			low[v] = min(low[v], tin[nv]);
		}
	}
}

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	adj.resize(n);
	tin.resize(n, -1);
	low.resize(n, -1);
	orient.resize(m);
	edges.resize(m);
	edge_used.resize(m);
	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		a--; b--;
		adj[a].push_back({b, i});
		adj[b].push_back({a, i});
		edges[i] = {a, b};
	}
	int comp_cnt = 0;
	for (int v = 0; v < n; v++) {
		if (tin[v] == -1) {
			comp_cnt++;
			find_bridges(v);
		}
	}
	printf("%d\n%s\n", comp_cnt + bridge_cnt, orient.c_str());
}
```

## Bài tập luyện tập

* [26th Polish OI - Osiedla](https://szkopul.edu.pl/problemset/problem/nldsb4EW1YuZykBlf4lcZL1Y/site/)
