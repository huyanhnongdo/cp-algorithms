---
tags:
  - Translated
e_maxx_link: catalan_numbers
lang: vi
---

# Số Catalan (Catalan Numbers)

Số Catalan là một dãy số được tìm thấy trong nhiều bài toán tổ hợp khác nhau, thường liên quan đến các đối tượng được định nghĩa bằng đệ quy.

Dãy số này được đặt tên theo nhà toán học người Bỉ [Catalan](https://en.wikipedia.org/wiki/Eug%C3%A8ne_Charles_Catalan), sống vào thế kỷ 19. (Trên thực tế, dãy số này đã được biết đến trước đó bởi Euler, người sống trước Catalan một thế kỷ).

Một vài số Catalan đầu tiên $C_n$ (bắt đầu từ số thứ không):

 $1, 1, 2, 5, 14, 42, 132, 429, 1430, \ldots$

### Ứng dụng trong các bài toán tổ hợp

Số Catalan $C_n$ là lời giải cho các bài toán sau:

- Số lượng dãy ngoặc đúng gồm $n$ dấu mở ngoặc và $n$ dấu đóng ngoặc.
- Số lượng cây nhị phân đầy đủ có gốc (rooted full binary tree) có $n + 1$ lá (các đỉnh không được đánh số). Một cây nhị phân có gốc được gọi là đầy đủ nếu mỗi đỉnh của nó có đúng hai con hoặc không có con nào.
- Số cách đặt dấu ngoặc hoàn toàn cho tích của $n + 1$ thừa số.
- Số cách tam giác phân (triangulation) một đa giác lồi có $n + 2$ cạnh (tức là số cách chia đa giác thành các tam giác không giao nhau bằng các đường chéo).
- Số cách nối $2n$ điểm trên một đường tròn để tạo thành $n$ dây cung không giao nhau.
- Số lượng cây nhị phân đầy đủ không đẳng cấu (non-isomorphic) có $n$ nút bên trong (tức là các nút có ít nhất một con).
- Số lượng đường đi đơn điệu trên lưới từ điểm $(0, 0)$ đến điểm $(n, n)$ trong một lưới ô vuông kích thước $n \times n$, sao cho đường đi không vượt quá đường chéo chính (đường chéo nối từ $(0, 0)$ đến $(n, n)$).
- Số lượng hoán vị độ dài $n$ có thể sắp xếp bằng ngăn xếp (stack sorted) (tức là có thể chỉ ra rằng hoán vị đó sắp xếp được bằng ngăn xếp khi và chỉ khi không tồn tại ba chỉ số $i < j < k$ sao cho $a_k < a_i < a_j$).
- Số lượng phân hoạch không cắt nhau (non-crossing partitions) của một tập hợp có $n$ phần tử.
- Số cách phủ một hình bậc thang kích thước $1 \ldots n$ bằng $n$ hình chữ nhật (hình bậc thang gồm $n$ cột, trong đó cột thứ $i$ có chiều cao $i$).


## Tính toán

Có hai công thức để tính số Catalan: **Truy hồi và Giải tích**. Vì chúng ta tin rằng tất cả các bài toán nêu trên đều tương đương nhau (có cùng đáp số), nên khi chứng minh các công thức dưới đây, chúng ta sẽ chọn bài toán dễ suy luận nhất.

### Công thức truy hồi
 
$$C_0 = C_1 = 1$$

$$C_n = \sum_{k = 0}^{n-1} C_k C_{n-1-k} , {n} \geq 2$$

Công thức truy hồi có thể dễ dàng suy ra từ bài toán tìm số lượng dãy ngoặc đúng.

Ký hiệu dấu mở ngoặc ngoài cùng bên trái là $l$, nó phải tương ứng với một dấu đóng ngoặc $r$ nào đó. Dấu đóng ngoặc này chia dãy ngoặc thành 2 phần, và mỗi phần đến lượt nó cũng phải là một dãy ngoặc đúng. Do đó biểu thức cũng được chia làm 2 phần. Nếu đặt $k = {r - l - 1}$, thì với mỗi vị trí $r$ cố định, sẽ có đúng $C_k C_{n-1-k}$ dãy ngoặc như vậy. Lấy tổng trên tất cả các giá trị $k$ hợp lệ, ta có hệ thức truy hồi cho $C_n$.

Bạn cũng có thể suy nghĩ theo cách này: Theo định nghĩa, $C_n$ biểu thị số lượng dãy ngoặc đúng. Một dãy ngoặc đúng có thể được chia thành 2 phần có độ dài $k$ và ${n - k}$, trong đó mỗi phần đều phải là dãy ngoặc đúng. Ví dụ:

$( ) ( ( ) )$ có thể được chia thành $( )$ và $( ( ) )$, nhưng không thể chia thành $( ) ($ và $( ) )$. Lấy tổng trên tất cả các giá trị $k$ hợp lệ, ta thu được hệ thức truy hồi của $C_n$.

#### Cài đặt C++ 

```cpp
const int MOD = ....
const int MAX = ....
int catalan[MAX];
void init() {
    catalan[0] = catalan[1] = 1;
    for (int i=2; i<=n; i++) {
        catalan[i] = 0;
        for (int j=0; j < i; j++) {
            catalan[i] += (catalan[j] * catalan[i-j-1]) % MOD;
            if (catalan[i] >= MOD) {
                catalan[i] -= MOD;
            }
        }
    }
}
```

### Công thức giải tích

$$C_n = \frac{1}{n + 1} {\binom{2n}{n}}$$

(ở đây $\binom{n}{k}$ ký hiệu hệ số nhị thức thông thường, tức là số cách chọn $k$ đối tượng từ một tập hợp có $n$ đối tượng).

Công thức trên có thể dễ dàng chứng minh từ bài toán tìm đường đi đơn điệu trên lưới ô vuông. Tổng số đường đi đơn điệu trên lưới kích thước $n \times n$ là $\binom{2n}{n}$.

Bây giờ chúng ta đếm số lượng đường đi đơn điệu vượt qua đường chéo chính. Xét các đường đi vượt qua đường chéo chính và tìm cạnh đầu tiên của đường đi nằm ở phía trên đường chéo. Lấy đối xứng toàn bộ phần đường đi phía sau cạnh này qua đường chéo chéo phụ (đường chéo song song đã dịch chuyển). Kết quả luôn thu được một đường đi đơn điệu trong lưới $(n - 1) \times (n + 1)$. Ngược lại, mọi đường đi đơn điệu trong lưới $(n - 1) \times (n + 1)$ đều phải cắt đường chéo này. Do đó, chúng ta đã liệt kê được tất cả các đường đi đơn điệu vượt qua đường chéo chính trong lưới $n \times n$.

Số lượng đường đi đơn điệu trong lưới $(n - 1) \times (n + 1)$ là $\binom{2n}{n-1}$. Chúng ta gọi các đường đi này là đường đi "xấu". Kết quả là, để tìm số lượng đường đi đơn điệu không vượt qua đường chéo chính, chúng ta lấy tổng số đường đi trừ đi các đường đi "xấu", thu được công thức:

$$C_n = \binom{2n}{n} - \binom{2n}{n-1} = \frac{1}{n + 1} \binom{2n}{n} , {n} \geq 0$$

## Tài liệu tham khảo

- [Catalan Number by Tom Davis](http://www.geometer.org/mathcircles/catalan.pdf)

## Bài tập thực hành
- [Codechef - PANSTACK](https://www.codechef.com/APRIL12/problems/PANSTACK/)
- [Spoj - Skyline](http://www.spoj.com/problems/SKYLINE/)
- [UVA - Safe Salutations](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=932)
- [Codeforces - How many trees?](http://codeforces.com/problemset/problem/9/D)
- [SPOJ - FUNPROB](http://www.spoj.com/problems/FUNPROB/)
* [LOJ - 1170 - Counting Perfect BST](http://lightoj.com/volume_showproblem.php?problem=1170)
* [UVA - 12887 - The Soldier's Dilemma](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4752)
