---
title: Tìm đường đi Euler trong O(M)
tags:
  - Translated
e_maxx_link: euler_path
lang: vi
---
# Tìm đường đi Euler trong $O(M)$

Một đường đi Euler (Eulerian path) là một đường đi trong đồ thị đi qua tất cả các cạnh của nó mỗi cạnh đúng một lần.
Một chu trình Euler (Eulerian cycle) là một đường đi Euler đồng thời là một chu trình.

Bài toán đặt ra là tìm đường đi Euler trong một **đa đồ thị vô hướng có khuyên (loops)**.

## Thuật toán

Trước tiên, chúng ta có thể kiểm tra xem đồ thị có đường đi Euler hay không.
Chúng ta có thể sử dụng định lý sau: Một chu trình Euler tồn tại khi và chỉ khi bậc của tất cả các đỉnh đều chẵn.
Và một đường đi Euler tồn tại khi và chỉ khi số đỉnh có bậc lẻ là hai (hoặc bằng không, tương ứng với trường hợp tồn tại chu trình Euler).
Ngoài ra, tất nhiên, đồ thị phải liên thông (tức là sau khi loại bỏ tất cả các đỉnh cô lập, ta thu được một đồ thị liên thông).

Để tìm đường đi / chu trình Euler, chúng ta có thể sử dụng chiến lược sau:
Tìm tất cả các chu trình đơn và gộp chúng lại làm một - đó sẽ là chu trình Euler.
Nếu đồ thị có đường đi Euler không phải là chu trình, ta thêm một cạnh tạm thời nối hai đỉnh bậc lẻ, tìm chu trình Euler, sau đó xóa cạnh phụ này khỏi kết quả.

Việc tìm tất cả các chu trình và kết hợp chúng có thể được thực hiện bằng một thủ tục đệ quy đơn giản như sau:

```nohighlight
procedure FindEulerPath(V)
  1. iterate through all the edges outgoing from vertex V;
       remove this edge from the graph,
       and call FindEulerPath from the second end of this edge;
  2. add vertex V to the answer.
```

Độ phức tạp của thuật toán này rõ ràng là tuyến tính đối với số lượng cạnh.

Tuy nhiên, chúng ta có thể viết thuật toán tương tự dưới dạng không đệ quy:

```nohighlight
stack St;
put start vertex in St;
until St is empty
  let V be the value at the top of St;
  if degree(V) = 0, then
    add V to the answer;
    remove V from the top of St;
  otherwise
    find any edge coming out of V;
    remove it from the graph;
    put the second end of this edge in St;
```

Dễ dàng kiểm tra tính tương đương của hai dạng thuật toán này. Tuy nhiên, dạng thứ hai rõ ràng chạy nhanh hơn và mã nguồn sẽ hiệu quả hơn nhiều.

## Bài toán Domino

Dưới đây là một bài toán kinh điển về chu trình Euler - bài toán Domino.

Có $N$ quân domino. Như đã biết, ở mỗi đầu của quân domino có ghi một con số (thường là từ 1 đến 6, nhưng trong trường hợp của chúng ta điều đó không quan trọng). Bạn muốn xếp tất cả các quân domino thành một hàng sao cho số ở hai quân domino kề nhau, phần tiếp giáp nhau, trùng khớp. Các quân domino được phép xoay chiều.

Phát biểu lại bài toán: Coi các con số ghi trên quân domino là các đỉnh của đồ thị, và mỗi quân domino là một cạnh nối hai đỉnh này (mỗi quân domino có hai số $(a, b)$ tương ứng với cạnh vô hướng giữa $a$ và $b$). Khi đó, bài toán của chúng ta được đưa về bài toán tìm đường đi Euler trên đồ thị này.

## Cài đặt

Chương trình dưới đây tìm và in ra chu trình hoặc đường đi Euler trong đồ thị, hoặc in ra $-1$ nếu không tồn tại.

Đầu tiên, chương trình kiểm tra bậc của các đỉnh: nếu không có đỉnh nào có bậc lẻ thì đồ thị có chu trình Euler; nếu có đúng $2$ đỉnh có bậc lẻ thì đồ thị chỉ có đường đi Euler (không có chu trình); nếu có nhiều hơn $2$ đỉnh có bậc lẻ thì đồ thị không có cả chu trình lẫn đường đi Euler.
Để tìm đường đi Euler (không phải chu trình), ta làm như sau: nếu $V1$ và $V2$ là hai đỉnh có bậc lẻ, ta chỉ cần thêm một cạnh $(V1, V2)$, trên đồ thị thu được ta tìm chu trình Euler (chắc chắn sẽ tồn tại), rồi sau đó xóa cạnh "giả" $(V1, V2)$ khỏi kết quả.
Chúng ta sẽ tìm chu trình Euler chính xác như mô tả ở trên (phiên bản không đệ quy), đồng thời ở cuối thuật toán, chúng ta sẽ kiểm tra xem đồ thị ban đầu có liên thông hay không (nếu đồ thị không liên thông, ở cuối thuật toán sẽ còn lại một số cạnh chưa đi qua, và trong trường hợp này chúng ta cần in ra $-1$).
Cuối cùng, chương trình cũng tính đến trường hợp có các đỉnh cô lập trong đồ thị.

Lưu ý rằng chúng ta sử dụng ma trận kề trong bài toán này.
Ngoài ra, cài đặt này tìm cạnh tiếp theo bằng phương pháp duyệt vét cạn, đòi hỏi phải duyệt qua toàn bộ hàng trong ma trận nhiều lần.
Một cách tốt hơn là lưu trữ đồ thị dưới dạng danh sách kề, xóa các cạnh trong thời gian $O(1)$ và đánh dấu các cạnh ngược trong một danh sách riêng biệt.
Cách này giúp ta đạt được thuật toán có độ phức tạp $O(N)$.

```cpp
int main() {
    int n;
    vector<vector<int>> g(n, vector<int>(n));
    // reading the graph in the adjacency matrix

    vector<int> deg(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j)
            deg[i] += g[i][j];
    }

    int first = 0;
    while (first < n && !deg[first])
        ++first;
    if (first == n) {
        cout << -1;
        return 0;
    }

    int v1 = -1, v2 = -1;
    bool bad = false;
    for (int i = 0; i < n; ++i) {
        if (deg[i] & 1) {
            if (v1 == -1)
                v1 = i;
            else if (v2 == -1)
                v2 = i;
            else
                bad = true;
        }
    }

    if (v1 != -1)
        ++g[v1][v2], ++g[v2][v1];

    stack<int> st;
    st.push(first);
    vector<int> res;
    while (!st.empty()) {
        int v = st.top();
        int i;
        for (i = 0; i < n; ++i)
            if (g[v][i])
                break;
        if (i == n) {
            res.push_back(v);
            st.pop();
        } else {
            --g[v][i];
            --g[i][v];
            st.push(i);
        }
    }

    if (v1 != -1) {
        for (size_t i = 0; i + 1 < res.size(); ++i) {
            if ((res[i] == v1 && res[i + 1] == v2) ||
                (res[i] == v2 && res[i + 1] == v1)) {
                vector<int> res2;
                for (size_t j = i + 1; j < res.size(); ++j)
                    res2.push_back(res[j]);
                for (size_t j = 1; j <= i; ++j)
                    res2.push_back(res[j]);
                res = res2;
                break;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (g[i][j])
                bad = true;
        }
    }

    if (bad) {
        cout << -1;
    } else {
        for (int x : res)
            cout << x << " ";
    }
}
```

### Bài tập thực hành:

- [CSES : Mail Delivery](https://cses.fi/problemset/task/1691)
- [CSES : Teleporters Path](https://cses.fi/problemset/task/1693)
- [Codeforces - Melody](https://codeforces.com/contest/2110/problem/E)
- [Codeforces - Tanya and Password](https://codeforces.com/contest/508/problem/D)
