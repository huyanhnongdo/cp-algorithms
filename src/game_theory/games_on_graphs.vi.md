---
tags:
  - Translated
e_maxx_link: games_on_graphs
lang: vi
---
# Trò chơi trên đồ thị bất kỳ

Giả sử có một trò chơi được chơi bởi hai người chơi trên một đồ thị bất kỳ $G$.
Nói cách khác, trạng thái hiện tại của trò chơi là một đỉnh nhất định.
Các người chơi thực hiện các nước đi luân phiên, di chuyển từ đỉnh hiện tại sang một đỉnh kề bằng cách đi theo cạnh nối giữa chúng.
Tùy thuộc vào trò chơi, người không thể thực hiện nước đi sẽ bị thua hoặc thắng trò chơi đó.

Chúng ta xem xét trường hợp tổng quát nhất: đồ thị có hướng bất kỳ có thể chứa chu trình.
Nhiệm vụ của chúng ta là xác định, với một trạng thái ban đầu cho trước, ai sẽ thắng trò chơi nếu cả hai người chơi đều sử dụng chiến thuật tối ưu, hoặc xác định xem trò chơi sẽ kết thúc với kết quả hòa.

Chúng ta sẽ giải quyết bài toán này một cách rất hiệu quả.
Chúng ta sẽ tìm lời giải cho tất cả các đỉnh xuất phát có thể có của đồ thị trong thời gian tuyến tính so với số lượng cạnh: $O(m)$.

## Mô tả thuật toán

Chúng ta gọi một đỉnh là đỉnh thắng (winning vertex) nếu người chơi bắt đầu tại trạng thái này sẽ thắng trò chơi nếu họ chơi tối ưu (bất kể đối thủ thực hiện nước đi như thế nào).
Tương tự, chúng ta gọi một đỉnh là đỉnh thua (losing vertex) nếu người chơi bắt đầu tại đỉnh này sẽ thua nếu đối thủ chơi tối ưu.

Đối với một số đỉnh của đồ thị, chúng ta đã biết trước chúng là đỉnh thắng hay đỉnh thua: đó chính là các đỉnh không có cạnh đi ra.

Ngoài ra, chúng ta có các **quy tắc** sau:

- Nếu một đỉnh có một cạnh đi ra dẫn đến một đỉnh thua, thì bản thân đỉnh đó là một đỉnh thắng.
- Nếu tất cả các cạnh đi ra của một đỉnh nhất định đều dẫn đến các đỉnh thắng, thì bản thân đỉnh đó là một đỉnh thua.
- Nếu tại một thời điểm nào đó vẫn còn các đỉnh chưa được xác định, và không thỏa mãn quy tắc thứ nhất hay thứ hai, thì mỗi đỉnh này, khi được chọn làm đỉnh bắt đầu, sẽ dẫn đến kết quả hòa nếu cả hai người chơi đều chơi tối ưu.

Như vậy, chúng ta có thể xác định một thuật toán chạy trong thời gian $O(n m)$ ngay lập tức.
Chúng ta duyệt qua tất cả các đỉnh và thử áp dụng quy tắc thứ nhất hoặc thứ hai, sau đó lặp lại quá trình này.

Tuy nhiên, chúng ta có thể tăng tốc quy trình này và đưa độ phức tạp về $O(m)$.

Chúng ta sẽ duyệt qua tất cả các đỉnh mà chúng ta đã biết trước đó là trạng thái thắng hay thua.
Với mỗi đỉnh, chúng ta bắt đầu một [DFS (Tìm kiếm theo chiều sâu)](../graph/depth-first-search.md).
DFS này sẽ đi ngược theo các cạnh đảo chiều.
Đầu tiên, nó sẽ không đi vào các đỉnh đã được xác định là đỉnh thắng hoặc đỉnh thua.
Tiếp theo, nếu quá trình tìm kiếm đi từ một đỉnh thua sang một đỉnh chưa xác định, chúng ta đánh dấu đỉnh đó là đỉnh thắng và tiếp tục DFS từ đỉnh mới này.
Nếu chúng ta đi từ một đỉnh thắng sang một đỉnh chưa xác định, chúng ta phải kiểm tra xem liệu tất cả các cạnh đi ra từ đỉnh này có dẫn đến các đỉnh thắng hay không.
Chúng ta có thể thực hiện kiểm tra này trong $O(1)$ bằng cách lưu trữ số lượng các cạnh dẫn đến một đỉnh thắng cho mỗi đỉnh.
Do đó, nếu chúng ta đi từ một đỉnh thắng sang một đỉnh chưa xác định, chúng ta tăng bộ đếm lên và kiểm tra xem số lượng này có bằng với tổng số cạnh đi ra hay không.
Nếu bằng nhau, chúng ta có thể đánh dấu đỉnh này là một đỉnh thua và tiếp tục DFS từ đỉnh đó.
Nếu không, chúng ta chưa biết liệu đỉnh này là đỉnh thắng hay đỉnh thua, do đó việc tiếp tục DFS từ đỉnh này là không hợp lý.

Tổng cộng, chúng ta thăm mỗi đỉnh thắng và mỗi đỉnh thua đúng một lần (các đỉnh chưa xác định không bị thăm), và chúng ta cũng đi qua mỗi cạnh tối đa một lần.
Do đó, độ phức tạp là $O(m)$.

## Cài đặt

Dưới đây là cài đặt của DFS này.
Chúng ta giả định rằng biến `adj_rev` lưu trữ danh sách kề của đồ thị ở dạng **đảo ngược**, nghĩa là thay vì lưu trữ cạnh $(i, j)$ của đồ thị, chúng ta lưu trữ $(j, i)$.
Ngoài ra, đối với mỗi đỉnh, chúng ta giả định rằng bậc ra (out-degree) đã được tính toán trước.

```cpp 
vector<vector<int>> adj_rev;

vector<bool> winning;
vector<bool> losing;
vector<bool> visited;
vector<int> degree;

void dfs(int v) {
    visited[v] = true;
    for (int u : adj_rev[v]) {
        if (!visited[u]) {
            if (losing[v])
                winning[u] = true;
            else if (--degree[u] == 0)
                losing[u] = true;
            else
                continue;
            dfs(u);
        }
    }
}
```

## Ví dụ: "Cảnh sát và tên trộm"

Dưới đây là một ví dụ cụ thể về một trò chơi như vậy.

Có một bảng $m \times n$.
Một số ô không thể đi vào.
Tọa độ ban đầu của cảnh sát và tên trộm đã được biết.
Một trong các ô là lối thoát hiểm.
Nếu cảnh sát và tên trộm ở cùng một ô tại bất kỳ thời điểm nào, cảnh sát thắng.
Nếu tên trộm ở ô lối thoát (mà không có cảnh sát ở đó), tên trộm thắng.
Cảnh sát có thể đi theo cả 8 hướng, tên trộm chỉ có thể đi theo 4 hướng (dọc theo các trục tọa độ).
Cả cảnh sát và tên trộm sẽ luân phiên di chuyển.
Tuy nhiên, họ cũng có thể bỏ qua lượt nếu muốn.
Nước đi đầu tiên được thực hiện bởi cảnh sát.

Bây giờ chúng ta sẽ **xây dựng đồ thị**.
Để làm điều này, chúng ta phải chính thức hóa các quy tắc của trò chơi.
Trạng thái hiện tại của trò chơi được xác định bởi tọa độ của cảnh sát $P$, tọa độ của tên trộm $T$, và cả việc đến lượt của ai, hãy gọi biến này là $P_{\text{turn}}$ (giá trị là true khi đến lượt cảnh sát).
Vì vậy, một đỉnh của đồ thị được xác định bởi bộ ba $(P, T, P_{\text{turn}})$.
Đồ thị sau đó có thể được xây dựng dễ dàng bằng cách tuân theo các quy tắc của trò chơi.

Tiếp theo, chúng ta cần xác định ban đầu đỉnh nào là đỉnh thắng và đỉnh nào là đỉnh thua.
Có một **điểm tinh tế** ở đây.
Các đỉnh thắng/thua phụ thuộc vào tọa độ và cả $P_{\text{turn}}$ - xem đó là lượt của ai.
Nếu là lượt của cảnh sát, thì đỉnh đó là đỉnh thắng nếu tọa độ của cảnh sát và tên trộm trùng nhau, và là đỉnh thua nếu nó không phải là đỉnh thắng và tên trộm đang ở ô lối thoát.
Nếu là lượt của tên trộm, thì đỉnh đó là đỉnh thua nếu tọa độ của hai người chơi trùng nhau, và là đỉnh thắng nếu nó không phải là đỉnh thua và tên trộm đang ở ô lối thoát.

Điểm duy nhất cần lưu ý trước khi cài đặt là bạn cần quyết định xem mình muốn xây dựng đồ thị **một cách tường minh** hay chỉ xây dựng **tại thời điểm chạy (on the fly)**.
Một mặt, xây dựng đồ thị tường minh sẽ dễ dàng hơn nhiều và ít có khả năng xảy ra lỗi.
Mặt khác, nó sẽ làm tăng lượng mã nguồn và thời gian chạy sẽ chậm hơn so với khi bạn xây dựng đồ thị tại thời điểm chạy.

Cài đặt sau đây sẽ xây dựng đồ thị một cách tường minh:

```cpp
struct State {
    int P, T;
    bool Pstep;
};

vector<State> adj_rev[100][100][2]; // [P][T][Pstep]
bool winning[100][100][2];
bool losing[100][100][2];
bool visited[100][100][2];
int degree[100][100][2];

void dfs(State v) {
    visited[v.P][v.T][v.Pstep] = true;
    for (State u : adj_rev[v.P][v.T][v.Pstep]) {
        if (!visited[u.P][u.T][u.Pstep]) {
            if (losing[v.P][v.T][v.Pstep])
                winning[u.P][u.T][u.Pstep] = true;
            else if (--degree[u.P][u.T][u.Pstep] == 0)
                losing[u.P][u.T][u.Pstep] = true;
            else
                continue;
            dfs(u);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    for (int P = 0; P < n*m; P++) {
        for (int T = 0; T < n*m; T++) {
            for (int Pstep = 0; Pstep <= 1; Pstep++) {
                int Px = P/m, Py = P%m, Tx = T/m, Ty = T%m;
                if (a[Px][Py]=='*' || a[Tx][Ty]=='*')
                    continue;
                
                bool& win = winning[P][T][Pstep];
                bool& lose = losing[P][T][Pstep];
                if (Pstep) {
                    win = Px==Tx && Py==Ty;
                    lose = !win && a[Tx][Ty] == 'E';
                } else {
                    lose = Px==Tx && Py==Ty;
                    win = !lose && a[Tx][Ty] == 'E';
                }
                if (win || lose)
                    continue;

                State st = {P,T,!Pstep};
                adj_rev[P][T][Pstep].push_back(st);
                st.Pstep = Pstep;
                degree[P][T][Pstep]++;
                
                const int dx[] = {-1, 0, 1, 0, -1, -1, 1, 1};
                const int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
                for (int d = 0; d < (Pstep ? 8 : 4); d++) {
                    int PPx = Px, PPy = Py, TTx = Tx, TTy = Ty;
                    if (Pstep) {
                        PPx += dx[d];
                        PPy += dy[d];
                    } else {
                        TTx += dx[d];
                        TTy += dy[d];
                    }

                    if (PPx >= 0 && PPx < n && PPy >= 0 && PPy < m && a[PPx][PPy] != '*' &&
                        TTx >= 0 && TTx < n && TTy >= 0 && TTy < m && a[TTx][TTy] != '*')
                    {
                        adj_rev[PPx*m+PPy][TTx*m+TTy][!Pstep].push_back(st);
                        ++degree[P][T][Pstep];
                    }
                }
            }
        }
    }

    for (int P = 0; P < n*m; P++) {
        for (int T = 0; T < n*m; T++) {
            for (int Pstep = 0; Pstep <= 1; Pstep++) {
                if ((winning[P][T][Pstep] || losing[P][T][Pstep]) && !visited[P][T][Pstep])
                    dfs({P, T, (bool)Pstep});
            }
        }
    }

    int P_st, T_st;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 'P')
                P_st = i*m+j;
            else if (a[i][j] == 'T')
                T_st = i*m+j;
        }
    }

    if (winning[P_st][T_st][true]) {
        cout << "Police catches the thief"  << endl;
    } else if (losing[P_st][T_st][true]) {
        cout << "The thief escapes" << endl;
    } else {
        cout << "Draw" << endl;
    }
}
```