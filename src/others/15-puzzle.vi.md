---
tags:
  - Translated
e_maxx_link: 15_puzzle
lang: vi
---
# Trò chơi 15 Puzzle: Sự tồn tại của lời giải

Trò chơi này được chơi trên một bảng $4 \times 4$. Trên bảng này có $15$ ô số được đánh số từ 1 đến 15. Một ô được để trống (ký hiệu là 0). Bạn cần đưa bảng về trạng thái được trình bày dưới đây bằng cách liên tục di chuyển một trong các ô vào vị trí trống:

$$\begin{matrix} 1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \\ 9 & 10 & 11 & 12 \\ 13 & 14 & 15 & 0 \end{matrix}$$

Trò chơi "15 Puzzle" được tạo ra bởi Noyes Chapman vào năm 1880.

## Sự tồn tại của lời giải

Hãy xem xét bài toán này: cho trước một vị trí trên bảng, xác định xem có tồn tại một chuỗi các nước đi dẫn đến trạng thái đích hay không.

Giả sử chúng ta có một vị trí trên bảng:

$$\begin{matrix} a_1 & a_2 & a_3 & a_4 \\ a_5 & a_6 & a_7 & a_8 \\ a_9 & a_{10} & a_{11} & a_{12} \\ a_{13} & a_{14} & a_{15} & a_{16} \end{matrix}$$

trong đó một trong các phần tử bằng 0 và biểu thị ô trống $a_z  = 0$.

Hãy xem xét hoán vị:

$$a_1 a_2 ... a_{z-1} a_{z+1} ... a_{15} a_{16}$$

tức là hoán vị các con số tương ứng với vị trí trên bảng, loại bỏ phần tử số 0.

Gọi $N$ là số lượng nghịch thế trong hoán vị này (tức là số lượng các cặp phần tử $a_i$ và $a_j$ sao cho $i < j$, nhưng $a_i  > a_j$).

Giả sử $K$ là chỉ số hàng nơi đặt ô trống (tức là theo quy ước của chúng ta, $K = (z - 1) \div \ 4 + 1$).

Khi đó, **lời giải tồn tại khi và chỉ khi $N + K$ là số chẵn**.

## Cài đặt

Thuật toán nêu trên có thể được minh họa bằng mã nguồn chương trình sau:

```cpp
int a[16];
for (int i=0; i<16; ++i)
    cin >> a[i];

int inv = 0;
for (int i=0; i<16; ++i)
    if (a[i])
        for (int j=0; j<i; ++j)
            if (a[j] > a[i])
                ++inv;
for (int i=0; i<16; ++i)
    if (a[i] == 0)
        inv += 1 + i / 4;

puts ((inv & 1) ? "No Solution" : "Solution Exists");
```

## Chứng minh

Năm 1879, Johnson đã chứng minh rằng nếu $N + K$ là số lẻ, thì lời giải không tồn tại, và cùng năm đó, Story đã chứng minh rằng tất cả các vị trí mà $N + K$ là số chẵn đều có lời giải.

Tuy nhiên, tất cả các chứng minh này đều khá phức tạp.

Năm 1999, Archer đã đề xuất một chứng minh đơn giản hơn nhiều (bạn có thể tải bài báo của ông ấy [tại đây](http://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/15-puzzle.pdf)).

## Bài tập thực hành

* [Hackerrank - N-puzzle](https://www.hackerrank.com/challenges/n-puzzle)