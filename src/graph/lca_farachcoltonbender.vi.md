---
tags:
  - Translated
e_maxx_link: lca_linear
lang: vi
---

# Tổ tiên chung gần nhất - Thuật toán Farach-Colton và Bender

Cho $G$ là một cây.
Với mỗi truy vấn có dạng $(u, v)$, chúng ta muốn tìm tổ tiên chung gần nhất (Lowest Common Ancestor - LCA) của các nút $u$ và $v$, tức là chúng ta muốn tìm một nút $w$ vừa nằm trên đường đi từ $u$ về nút gốc, vừa nằm trên đường đi từ $v$ về nút gốc, và nếu có nhiều nút như vậy thì chúng ta chọn nút ở xa gốc nhất.
Nói cách khác, nút $w$ cần tìm là tổ tiên thấp nhất của $u$ và $v$.
Đặc biệt, nếu $u$ là tổ tiên của $v$, thì $u$ chính là tổ tiên chung gần nhất của chúng.

Thuật toán sẽ được mô tả trong bài viết này được phát triển bởi Farach-Colton và Bender.
Đây là một thuật toán tối ưu tiệm cận (asymptotically optimal).

## Thuật toán

Chúng ta sử dụng phép quy giản kinh điển từ bài toán LCA về bài toán RMQ.
Chúng ta duyệt qua toàn bộ các nút của cây bằng [DFS](depth-first-search.md) và duy trì một mảng chứa tất cả các nút đã duyệt cùng với chiều cao của chúng.
LCA của hai nút $u$ và $v$ chính là nút có chiều cao nhỏ nhất nằm giữa các lần xuất hiện của $u$ và $v$ trên đường đi này.

Trong hình dưới đây, bạn có thể thấy một đường đi Euler (Euler-Tour) khả dĩ của đồ thị và danh sách các nút được ghé thăm cùng chiều cao tương ứng bên dưới.

<div style="text-align: center;" markdown="1">

![LCA_Euler_Tour](LCA_Euler.png)

</div>

$$\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\text{Nodes:}   & 1 & 2 & 5 & 2 & 6 & 2 & 1 & 3 & 1 & 4 & 7 & 4 & 1 \\ \hline
\text{Heights:} & 1 & 2 & 3 & 2 & 3 & 2 & 1 & 2 & 1 & 2 & 3 & 2 & 1 \\ \hline
\end{array}$$

Bạn có thể đọc thêm về phép quy giản này trong bài viết [Tổ tiên chung gần nhất (LCA)](lca.md).
Trong bài viết đó, giá trị nhỏ nhất của một đoạn được tìm bằng phương pháp chia căn trong $O(\sqrt{N})$ hoặc bằng Cây phân đoạn (Segment tree) trong $O(\log N)$.
Trong bài viết này, chúng ta sẽ xem xét cách giải bài toán truy vấn giá trị nhỏ nhất trên đoạn (RMQ) trong thời gian $O(1)$, trong khi vẫn chỉ mất $O(N)$ thời gian tiền xử lý.

Lưu ý rằng bài toán RMQ sau khi quy giản có một đặc điểm rất đặc biệt:
hai phần tử kề nhau bất kỳ trong mảng luôn chênh lệch nhau đúng một đơn vị (vì các phần tử trong mảng chính là chiều cao của các nút được duyệt theo thứ tự, và chúng ta chỉ có thể đi xuống nút con, khiến phần tử tiếp theo tăng thêm 1, hoặc đi ngược lên nút cha, khiến phần tử tiếp theo giảm đi 1).
Thuật toán Farach-Colton và Bender mô tả một lời giải cho chính bài toán RMQ đặc biệt này.

Ký hiệu $A$ là mảng mà chúng ta muốn thực hiện các truy vấn RMQ.
Và $N$ là kích thước của $A$.

Có một cấu trúc dữ liệu đơn giản mà chúng ta có thể sử dụng để giải quyết bài toán RMQ với thời gian tiền xử lý $O(N \log N)$ và $O(1)$ cho mỗi truy vấn: [Bảng thưa (Sparse Table)](../data_structures/sparse-table.md).
Chúng ta tạo một bảng $T$ trong đó mỗi phần tử $T[i][j]$ bằng giá trị nhỏ nhất của $A$ trong khoảng $[i, i + 2^j - 1]$.
Rõ ràng $0 \leq j \leq \lceil \log N \rceil$, và do đó kích thước của Bảng thưa sẽ là $O(N \log N)$.
Bạn có thể xây dựng bảng này một cách dễ dàng trong $O(N \log N)$ bằng cách nhận xét rằng $T[i][j] = \min(T[i][j-1], T[i+2^{j-1}][j-1])$.

Làm thế nào để trả lời một truy vấn RMQ trong $O(1)$ sử dụng cấu trúc dữ liệu này?
Giả sử truy vấn nhận được là $[l, r]$, thì kết quả sẽ là $\min(T[l][\text{sz}], T[r-2^{\text{sz}}+1][\text{sz}])$, trong đó $\text{sz}$ là số mũ lớn nhất sao cho $2^{\text{sz}}$ không lớn hơn độ dài đoạn $r-l+1$.
Thật vậy, chúng ta có thể lấy đoạn $[l, r]$ và phủ nó bằng hai đoạn độ dài $2^{\text{sz}}$ - một đoạn bắt đầu tại $l$ và đoạn kia kết thúc tại $r$.
Hai đoạn này chồng lấp lên nhau, nhưng điều đó không ảnh hưởng đến tính đúng đắn của phép toán tối thiểu ($\min$).
Để thực sự đạt được độ phức tạp thời gian $O(1)$ cho mỗi truy vấn, chúng ta cần biết giá trị của $\text{sz}$ cho tất cả các độ dài có thể từ $1$ đến $N$.
Tuy nhiên, điều này có thể dễ dàng được tính trước.

Bây giờ chúng ta muốn cải thiện độ phức tạp của việc tiền xử lý xuống còn $O(N)$.

Chúng ta chia mảng $A$ thành các khối (block) kích thước $K = 0.5 \log N$ với $\log$ là logarit cơ số 2.
Với mỗi khối, chúng ta tính phần tử nhỏ nhất và lưu chúng vào mảng $B$.
$B$ có kích thước là $\frac{N}{K}$.
Chúng ta xây dựng một Bảng thưa (Sparse Table) trên mảng $B$.
Kích thước và độ phức tạp thời gian của nó sẽ là:

$$\frac{N}{K}\log\left(\frac{N}{K}\right) = \frac{2N}{\log(N)} \log\left(\frac{2N}{\log(N)}\right) =$$

$$= \frac{2N}{\log(N)} \left(1 + \log\left(\frac{N}{\log(N)}\right)\right) \leq \frac{2N}{\log(N)} + 2N = O(N)$$

Bây giờ chúng ta chỉ cần học cách trả lời nhanh các truy vấn RMQ trong phạm vi mỗi khối.
Thực tế, nếu truy vấn RMQ nhận được là $[l, r]$ và $l, r$ thuộc hai khối khác nhau thì câu trả lời là giá trị nhỏ nhất trong ba giá trị sau:
giá trị nhỏ nhất của hậu tố khối chứa $l$ bắt đầu từ $l$, giá trị nhỏ nhất của tiền tố khối chứa $r$ kết thúc tại $r$, và giá trị nhỏ nhất của các khối nằm giữa chúng.
Giá trị nhỏ nhất của các khối nằm giữa có thể được trả lời trong $O(1)$ bằng Bảng thưa.
Vì vậy, chúng ta chỉ còn lại các truy vấn RMQ nằm hoàn toàn bên trong một khối.

Ở đây chúng ta sẽ khai thác tính chất của mảng.
Hãy nhớ rằng các giá trị trong mảng - vốn chỉ là giá trị chiều cao trong cây - sẽ luôn chênh lệch nhau đúng 1 đơn vị.
Nếu chúng ta loại bỏ phần tử đầu tiên của một khối và trừ nó khỏi mọi phần tử khác trong khối, mỗi khối có thể được xác định bằng một dãy độ dài $K - 1$ gồm các số $+1$ và $-1$.
Bởi vì các khối này rất nhỏ, chỉ có một số ít dãy khác nhau có thể xảy ra.
Số lượng dãy có thể xảy ra là:

$$2^{K-1} = 2^{0.5 \log(N) - 1} = 0.5 \left(2^{\log(N)}\right)^{0.5} = 0.5 \sqrt{N}$$

Do đó, số lượng khối khác nhau là $O(\sqrt{N})$, và vì vậy chúng ta có thể tính trước kết quả của các truy vấn RMQ bên trong tất cả các khối khác nhau này trong thời gian $O(\sqrt{N} K^2) = O(\sqrt{N} \log^2(N)) = O(N)$.
Để cài đặt, chúng ta có thể biểu diễn một khối bằng một mặt nạ bit (bitmask) độ dài $K-1$ (vừa vặn trong một kiểu int tiêu chuẩn) và lưu chỉ số của giá trị nhỏ nhất trong một mảng $\text{block}[\text{mask}][l][r]$ có kích thước $O(\sqrt{N} \log^2(N))$.

Như vậy, chúng ta đã biết cách tính trước các truy vấn RMQ trong mỗi khối, cũng như các truy vấn RMQ trên một khoảng gồm các khối, tất cả đều trong $O(N)$.
Với các tiền xử lý này, chúng ta có thể trả lời mỗi truy vấn trong $O(1)$ bằng cách sử dụng tối đa bốn giá trị được tính trước: giá trị nhỏ nhất của khối chứa `l`, giá trị nhỏ nhất của khối chứa `r`, và hai giá trị nhỏ nhất của các đoạn chồng lấp của các khối nằm giữa chúng.

## Cài đặt

```cpp
int n;
vector<vector<int>> adj;

int block_size, block_cnt;
vector<int> first_visit;
vector<int> euler_tour;
vector<int> height;
vector<int> log_2;
vector<vector<int>> st;
vector<vector<vector<int>>> blocks;
vector<int> block_mask;

void dfs(int v, int p, int h) {
    first_visit[v] = euler_tour.size();
    euler_tour.push_back(v);
    height[v] = h;
    
    for (int u : adj[v]) {
        if (u == p)
            continue;
        dfs(u, v, h + 1);
        euler_tour.push_back(v);
    }
}

int min_by_h(int i, int j) {
    return height[euler_tour[i]] < height[euler_tour[j]] ? i : j;
}

void precompute_lca(int root) {
    // get euler tour & indices of first occurrences
    first_visit.assign(n, -1);
    height.assign(n, 0);
    euler_tour.reserve(2 * n);
    dfs(root, -1, 0);

    // precompute all log values
    int m = euler_tour.size();
    log_2.reserve(m + 1);
    log_2.push_back(-1);
    for (int i = 1; i <= m; i++)
        log_2.push_back(log_2[i / 2] + 1);

    block_size = max(1, log_2[m] / 2);
    block_cnt = (m + block_size - 1) / block_size;

    // precompute minimum of each block and build sparse table
    st.assign(block_cnt, vector<int>(log_2[block_cnt] + 1));
    for (int i = 0, j = 0, b = 0; i < m; i++, j++) {
        if (j == block_size)
            j = 0, b++;
        if (j == 0 || min_by_h(i, st[b][0]) == i)
            st[b][0] = i;
    }
    for (int l = 1; l <= log_2[block_cnt]; l++) {
        for (int i = 0; i < block_cnt; i++) {
            int ni = i + (1 << (l - 1));
            if (ni >= block_cnt)
                st[i][l] = st[i][l-1];
            else
                st[i][l] = min_by_h(st[i][l-1], st[ni][l-1]);
        }
    }

    // precompute mask for each block
    block_mask.assign(block_cnt, 0);
    for (int i = 0, j = 0, b = 0; i < m; i++, j++) {
        if (j == block_size)
            j = 0, b++;
        if (j > 0 && (i >= m || min_by_h(i - 1, i) == i - 1))
            block_mask[b] += 1 << (j - 1);
    }

    // precompute RMQ for each unique block
    int possibilities = 1 << (block_size - 1);
    blocks.resize(possibilities);
    for (int b = 0; b < block_cnt; b++) {
        int mask = block_mask[b];
        if (!blocks[mask].empty())
            continue;
        blocks[mask].assign(block_size, vector<int>(block_size));
        for (int l = 0; l < block_size; l++) {
            blocks[mask][l][l] = l;
            for (int r = l + 1; r < block_size; r++) {
                blocks[mask][l][r] = blocks[mask][l][r - 1];
                if (b * block_size + r < m)
                    blocks[mask][l][r] = min_by_h(b * block_size + blocks[mask][l][r], 
                            b * block_size + r) - b * block_size;
            }
        }
    }
}

int lca_in_block(int b, int l, int r) {
    return blocks[block_mask[b]][l][r] + b * block_size;
}

int lca(int v, int u) {
    int l = first_visit[v];
    int r = first_visit[u];
    if (l > r)
        swap(l, r);
    int bl = l / block_size;
    int br = r / block_size;
    if (bl == br)
        return euler_tour[lca_in_block(bl, l % block_size, r % block_size)];
    int ans1 = lca_in_block(bl, l % block_size, block_size - 1);
    int ans2 = lca_in_block(br, 0, r % block_size);
    int ans = min_by_h(ans1, ans2);
    if (bl + 1 < br) {
        int l = log_2[br - bl - 1];
        int ans3 = st[bl+1][l];
        int ans4 = st[br - (1 << l)][l];
        ans = min_by_h(ans, min_by_h(ans3, ans4));
    }
    return euler_tour[ans];
}
```
