---
tags:
  - Translated
e_maxx_link: dfs
lang: vi
---

# Tìm kiếm theo chiều sâu (Depth First Search)

Tìm kiếm theo chiều sâu (Depth First Search - DFS) là một trong những thuật toán cơ bản trên đồ thị.

DFS tìm kiếm đường đi đầu tiên theo thứ tự từ điển trong đồ thị từ đỉnh nguồn $u$ đến mỗi đỉnh khác.
DFS cũng có thể tìm đường đi ngắn nhất trên cây (vì trên cây chỉ tồn tại duy nhất một đường đi đơn giữa hai đỉnh bất kỳ), nhưng điều này không còn đúng trên đồ thị tổng quát.

Thuật toán hoạt động trong thời gian $O(n + m)$, trong đó $n$ là số đỉnh và $m$ là số cạnh của đồ thị.

## Mô tả thuật toán

Ý tưởng chính của DFS là đi càng sâu vào đồ thị càng tốt, và chỉ quay lui (backtrack) khi bạn đang ở một đỉnh mà tất cả các đỉnh kề của nó đều đã được duyệt.

Thuật toán rất dễ mô tả và cài đặt bằng đệ quy:
Chúng ta bắt đầu quá trình tìm kiếm tại một đỉnh.
Sau khi truy cập đỉnh này, chúng ta tiếp tục thực hiện DFS cho từng đỉnh kề chưa được duyệt trước đó.
Bằng cách này, chúng ta sẽ truy cập tất cả các đỉnh có thể đi tới từ đỉnh xuất phát.

Xem phần cài đặt để biết thêm chi tiết.

## Ứng dụng của DFS

  * Tìm đường đi bất kỳ trong đồ thị từ đỉnh nguồn $u$ đến mọi đỉnh khác.
  
  * Tìm đường đi đầu tiên theo thứ tự từ điển trong đồ thị từ đỉnh nguồn $u$ đến mọi đỉnh khác.
  
  * Kiểm tra xem một đỉnh trong cây có phải là tổ tiên của một đỉnh khác hay không:
  
    Tại thời điểm bắt đầu và kết thúc của mỗi lời gọi hàm tìm kiếm, chúng ta lưu lại "thời gian" đi vào (entry) và đi ra (exit) của mỗi đỉnh.
    Bây giờ bạn có thể trả lời câu hỏi cho bất kỳ cặp đỉnh $(i, j)$ nào trong thời gian $O(1)$:
    đỉnh $i$ là tổ tiên của đỉnh $j$ khi và chỉ khi $\text{entry}[i] < \text{entry}[j]$ và $\text{exit}[i] > \text{exit}[j]$.
  
  * Tìm tổ tiên chung gần nhất (LCA) của hai đỉnh.
  
  * Sắp xếp topo (Topological sorting):
  
    Chạy một loạt các lượt duyệt DFS để truy cập mỗi đỉnh đúng một lần trong thời gian $O(n + m)$.
    Thứ tự topo cần tìm chính là thứ tự các đỉnh được sắp xếp theo chiều giảm dần của thời điểm hoàn thành (exit time).
  
  * Kiểm tra xem một đồ thị cho trước có chu trình hay không và tìm các chu trình trong đồ thị (bằng cách đếm các cạnh ngược trong mỗi thành phần liên thông).
  
  * Tìm các thành phần liên thông mạnh trong đồ thị có hướng:
  
    Đầu tiên thực hiện sắp xếp topo cho đồ thị.
    Sau đó chuyển vị đồ thị (transpose graph - đảo ngược chiều tất cả các cạnh) và chạy một loạt các lượt duyệt DFS khác theo thứ tự định ra bởi phép sắp xếp topo. Mỗi lượt duyệt DFS sẽ tạo ra một thành phần liên thông mạnh.
  
  * Tìm cầu trong đồ thị vô hướng:
  
    Đầu tiên chuyển đồ thị vô hướng đã cho thành đồ thị có hướng bằng cách chạy DFS và định hướng mỗi cạnh theo chiều đi của DFS. Thứ hai, tìm các thành phần liên thông mạnh của đồ thị có hướng này. Các cầu chính là các cạnh có hai đầu thuộc về hai thành phần liên thông mạnh khác nhau.

## Phân loại các cạnh trong đồ thị

Chúng ta có thể phân loại các cạnh của đồ thị $G$ dựa trên thời gian đi vào (entry) và đi ra (exit) của các đỉnh đầu mút $u$ và $v$ của cạnh $(u, v)$.
Việc phân loại này thường được sử dụng cho các bài toán như [tìm cầu](bridge-searching.md) và [tìm khớp (điểm khớp - articulation points)](cutpoints.md).

Chúng ta thực hiện duyệt DFS và phân loại các cạnh gặp phải theo các quy tắc sau:

Nếu $v$ chưa được duyệt:

* Cạnh cây khung (Tree Edge) - Nếu $v$ được duyệt ngay sau $u$ thì cạnh $(u, v)$ được gọi là cạnh cây khung. Nói cách khác, nếu $v$ được thăm lần đầu tiên từ đỉnh $u$ đang duyệt thì $(u, v)$ là cạnh cây khung.
Các cạnh này tạo thành cây khung DFS, do đó có tên gọi này.

Nếu $v$ đã được duyệt trước $u$:

* Cạnh ngược (Back Edge) - Nếu $v$ là tổ tiên của $u$ thì cạnh $(u, v)$ là cạnh ngược. $v$ là tổ tiên khi và chỉ khi chúng ta đã đi vào $v$ nhưng chưa thoát ra khỏi nó. Cạnh ngược tạo thành một chu trình vì có một đường đi từ tổ tiên $v$ đến hậu duệ $u$ (trong cây DFS) và một cạnh ngược từ hậu duệ $u$ quay về tổ tiên $v$. Các chu trình trong đồ thị có thể được phát hiện thông qua các cạnh ngược.

* Cạnh xuôi (Forward Edge) - Nếu $v$ là hậu duệ của $u$ thì cạnh $(u, v)$ là cạnh xuôi. Nói cách khác, nếu chúng ta đã duyệt và đi ra khỏi $v$, đồng thời $\text{entry}[u] < \text{entry}[v]$ thì cạnh $(u, v)$ tạo thành cạnh xuôi.
* Cạnh chéo (Cross Edge) - Nếu $v$ không phải tổ tiên cũng không phải hậu duệ của $u$ thì cạnh $(u, v)$ là cạnh chéo. Nói cách khác, nếu chúng ta đã duyệt và đi ra khỏi $v$, đồng thời $\text{entry}[u] > \text{entry}[v]$ thì $(u, v)$ là cạnh chéo.

**Định lý**. Gọi $G$ là một đồ thị vô hướng. Khi đó, quá trình duyệt DFS trên $G$ sẽ phân loại mọi cạnh gặp phải thành cạnh cây khung hoặc cạnh ngược, tức là cạnh xuôi và cạnh chéo chỉ tồn tại trong đồ thị có hướng.

Giả sử $(u, v)$ là một cạnh bất kỳ của $G$ và không mất tính tổng quát, $u$ được duyệt trước $v$, tức là $\text{entry}[u] < \text{entry}[v]$. Vì DFS chỉ xử lý mỗi cạnh một lần, có hai cách duy nhất mà cạnh $(u, v)$ được xử lý và phân loại:

* Lần đầu tiên chúng ta duyệt qua cạnh $(u, v)$ là theo chiều từ $u$ sang $v$. Vì $\text{entry}[u] < \text{entry}[v]$, tính chất đệ quy của DFS đảm bảo rằng đỉnh $v$ sẽ được duyệt xong hoàn toàn và thoát ra trước khi chúng ta quay ngược lại ngăn xếp cuộc gọi để thoát khỏi $u$. Do đó, đỉnh $v$ bắt buộc phải là đỉnh chưa được duyệt khi DFS lần đầu tiên khám phá cạnh $(u, v)$ từ $u$ sang $v$, vì nếu ngược lại thì tìm kiếm đã đi theo cạnh $(u, v)$ từ $v$ sang $u$ trước khi thoát khỏi $v$ (do $u$ và $v$ là kề nhau). Vì vậy, cạnh $(u, v)$ là cạnh cây khung.

* Lần đầu tiên chúng ta duyệt qua cạnh $(u, v)$ là theo chiều từ $v$ sang $u$. Vì chúng ta phát hiện ra $u$ trước $v$, và mỗi cạnh chỉ được xử lý một lần, cách duy nhất để duyệt qua cạnh $(u, v)$ từ $v$ sang $u$ là tồn tại một đường đi khác từ $u$ tới $v$ không chứa cạnh $(u, v)$, khiến $u$ trở thành tổ tiên của $v$. Cạnh $(u, v)$ khi đó hoàn thành một chu trình nối từ hậu duệ $v$ quay về tổ tiên $u$ chưa được thoát ra. Vì vậy, cạnh $(u, v)$ là cạnh ngược.

Vì chỉ có hai cách để xử lý cạnh $(u, v)$ như trên, việc thực hiện DFS trên đồ thị vô hướng $G$ sẽ luôn phân loại mọi cạnh thành cạnh cây khung hoặc cạnh ngược. Cạnh xuôi và cạnh chéo chỉ tồn tại trên đồ thị có hướng. Định lý được chứng minh hoàn toàn.

## Cài đặt

```cpp
vector<vector<int>> adj; // graph represented as an adjacency list
int n; // number of vertices

vector<bool> visited;

void dfs(int v) {
	visited[v] = true;
	for (int u : adj[v]) {
		if (!visited[u])
			dfs(u);
    }
}
```
Đây là cài đặt đơn giản nhất của thuật toán DFS.
Như đã mô tả trong phần ứng dụng, đôi khi việc lưu lại thời gian đi vào, đi ra và màu sắc của các đỉnh là rất hữu ích.
Chúng ta tô màu các đỉnh chưa duyệt bằng màu 0, đỉnh đang duyệt bằng màu 1, và đỉnh đã duyệt xong hoàn toàn bằng màu 2.

Dưới đây là cài đặt tổng quát hỗ trợ tính toán các thông tin trên:

```cpp
vector<vector<int>> adj; // graph represented as an adjacency list
int n; // number of vertices

vector<int> color;

vector<int> time_in, time_out;
int dfs_timer = 0;

void dfs(int v) {
	time_in[v] = dfs_timer++;
	color[v] = 1;
	for (int u : adj[v])
		if (color[u] == 0)
			dfs(u);
	color[v] = 2;
	time_out[v] = dfs_timer++;
}
```

## Bài tập áp dụng

* [SPOJ: ABCPATH](http://www.spoj.com/problems/ABCPATH/)
* [SPOJ: EAGLE1](http://www.spoj.com/problems/EAGLE1/)
* [Codeforces: Kefa and Park](http://codeforces.com/problemset/problem/580/C)
* [Timus: Werewolf](http://acm.timus.ru/problem.aspx?space=1&num=1242)
* [Timus: Penguin Avia](http://acm.timus.ru/problem.aspx?space=1&num=1709)
* [Timus: Two Teams](http://acm.timus.ru/problem.aspx?space=1&num=1106)
* [SPOJ - Ada and Island](http://www.spoj.com/problems/ADASEA/)
* [UVA 657 - The die is cast](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=598)
* [SPOJ - Sheep](http://www.spoj.com/problems/KOZE/)
* [SPOJ - Path of the Rightenous Man](http://www.spoj.com/problems/RIOI_2_3/)
* [SPOJ - Validate the Maze](http://www.spoj.com/problems/MAKEMAZE/)
* [SPOJ - Ghosts having Fun](http://www.spoj.com/problems/GHOSTS/)
* [Codeforces - Underground Lab](http://codeforces.com/contest/781/problem/C)
* [DevSkill - Maze Tester (archived)](http://web.archive.org/web/20200319103915/https://www.devskill.com/CodingProblems/ViewProblem/3)
* [DevSkill - Tourist (archived)](http://web.archive.org/web/20190426175135/https://devskill.com/CodingProblems/ViewProblem/17)
* [Codeforces - Anton and Tree](http://codeforces.com/contest/734/problem/E)
* [Codeforces - Transformation: From A to B](http://codeforces.com/contest/727/problem/A)
* [Codeforces - One Way Reform](http://codeforces.com/contest/723/problem/E)
* [Codeforces - Centroids](http://codeforces.com/contest/709/problem/E)
* [Codeforces - Generate a String](http://codeforces.com/contest/710/problem/E)
* [Codeforces - Broken Tree](http://codeforces.com/contest/758/problem/E)
* [Codeforces - Dasha and Puzzle](http://codeforces.com/contest/761/problem/E)
* [Codeforces - Making genome In Berland](http://codeforces.com/contest/638/problem/B)
* [Codeforces - Road Improvement](http://codeforces.com/contest/638/problem/C)
* [Codeforces - Garland](http://codeforces.com/contest/767/problem/C)
* [Codeforces - Labeling Cities](http://codeforces.com/contest/794/problem/D)
* [Codeforces - Send the Fool Further!](http://codeforces.com/contest/802/problem/J1)
* [Codeforces - The tag Game](http://codeforces.com/contest/813/problem/C)
* [Codeforces - Leha and Another game about graphs](http://codeforces.com/contest/841/problem/D)
* [Codeforces - Shortest path problem](http://codeforces.com/contest/845/problem/G)
* [Codeforces - Upgrading Tree](http://codeforces.com/contest/844/problem/E)
* [Codeforces - From Y to Y](http://codeforces.com/contest/849/problem/C)
* [Codeforces - Chemistry in Berland](http://codeforces.com/contest/846/problem/E)
* [Codeforces - Wizards Tour](http://codeforces.com/contest/861/problem/F)
* [Codeforces - Ring Road](http://codeforces.com/contest/24/problem/A)
* [Codeforces - Mail Stamps](http://codeforces.com/contest/29/problem/C)
* [Codeforces - Ant on the Tree](http://codeforces.com/contest/29/problem/D)
* [SPOJ - Cactus](http://www.spoj.com/problems/CAC/)
* [SPOJ - Mixing Chemicals](http://www.spoj.com/problems/AMR10J/)
