---
tags:
  - Translated
e_maxx_link: all_submasks
---

# Duyệt qua các mặt nạ con

## Duyệt qua tất cả các mặt nạ con của một mặt nạ cho trước

Cho một mặt nạ bit (bitmask) $m$, bạn muốn duyệt qua tất cả các mặt nạ con (submask) của nó một cách hiệu quả, tức là các mặt nạ $s$ mà chỉ các bit được bật trong mặt nạ $m$ mới có thể được bật.

Hãy xem xét cài đặt của thuật toán này, dựa trên một số mẹo liên quan đến các phép toán bit:

```cpp
int s = m;
while (s > 0) {
 ... you can use s ...
 s = (s-1) & m;
}
```

hoặc sử dụng vòng lặp `for` gọn gàng hơn:

```cpp
for (int s=m; s; s=(s-1)&m)
 ... you can use s ...
```

Trong cả hai biến thể của đoạn mã trên, mặt nạ con bằng không sẽ không được xử lý. Chúng ta có thể xử lý nó bên ngoài vòng lặp, hoặc sử dụng một cấu trúc ít thanh lịch hơn, ví dụ:

```cpp
for (int s=m; ; s=(s-1)&m) {
 ... you can use s ...
 if (s==0)  break;
}
```

Hãy cùng phân tích tại sao đoạn mã trên lại duyệt qua tất cả các mặt nạ con của $m$ theo thứ tự giảm dần mà không bị trùng lặp.

Giả sử chúng ta đang có mặt nạ bit hiện tại là $s$, và chúng ta muốn chuyển sang mặt nạ bit tiếp theo. Bằng cách trừ mặt nạ $s$ đi 1 đơn vị, chúng ta sẽ loại bỏ bit được bật ở vị trí ngoài cùng bên phải, và tất cả các bit bên phải nó sẽ trở thành 1. Sau đó, chúng ta loại bỏ tất cả các bit 1 "dư thừa" mà không nằm trong mặt nạ $m$, vì chúng không thể là một phần của mặt nạ con. Việc loại bỏ này được thực hiện thông qua phép toán logic bitwise AND: `(s-1) & m`. Kết quả thu được là chúng ta đã "cắt" mặt nạ $s-1$ để tìm giá trị lớn nhất mà nó có thể nhận, tức là mặt nạ con tiếp theo ngay sau $s$ theo thứ tự giảm dần.

Vì vậy, thuật toán này tạo ra tất cả các mặt nạ con của mặt nạ đã cho theo thứ tự giảm dần, chỉ thực hiện hai phép toán trong mỗi lần lặp.

Trường hợp đặc biệt là khi $s = 0$. Sau khi thực hiện phép tính $s-1$, ta nhận được một mặt nạ mà tất cả các bit đều được bật (biểu diễn bit của số -1), và sau phép toán `(s-1) & m`, ta sẽ có $s$ bằng $m$. Do đó, bạn cần cẩn thận với mặt nạ $s = 0$ — nếu vòng lặp không kết thúc tại số không, thuật toán có thể rơi vào vòng lặp vô hạn.

## Duyệt qua tất cả các mặt nạ cùng các mặt nạ con của chúng. Độ phức tạp $O(3^n)$

Trong nhiều bài toán, đặc biệt là các bài toán quy hoạch động trạng thái dùng mặt nạ bit (bitmask dynamic programming), bạn muốn duyệt qua tất cả các mặt nạ bit và với mỗi mặt nạ đó, duyệt qua tất cả các mặt nạ con của nó:

```cpp
for (int m=0; m<(1<<n); ++m)
	for (int s=m; s; s=(s-1)&m)
 ... s and m ...
```

Hãy chứng minh rằng vòng lặp bên trong sẽ thực hiện tổng cộng $O(3^n)$ lần lặp.

**Chứng minh thứ nhất**: Xét bit thứ $i$. Có chính xác ba khả năng xảy ra đối với bit này:

1. nó không nằm trong mặt nạ $m$ (và do đó cũng không nằm trong mặt nạ con $s$),
2. nó nằm trong $m$ nhưng không nằm trong $s$, hoặc
3. nó nằm trong cả $m$ và $s$.

Vì có tổng cộng $n$ bit, nên sẽ có $3^n$ tổ hợp khác nhau.

**Chứng minh thứ hai**: Lưu ý rằng nếu mặt nạ $m$ có $k$ bit được bật, nó sẽ có $2^k$ mặt nạ con. Vì chúng ta có tổng cộng $\binom{n}{k}$ mặt nạ có $k$ bit được bật (xem thêm bài viết về [Hệ số nhị thức](../combinatorics/binomial-coefficients.md)), nên tổng số tổ hợp của tất cả các mặt nạ sẽ là:

$$\sum_{k=0}^n \binom{n}{k} \cdot 2^k$$

Để tính tổng này, hãy chú ý rằng tổng trên chính là khai triển của $(1+2)^n$ theo định lý nhị thức. Do đó, chúng ta có $3^n$ tổ hợp, đúng như điều cần chứng minh.

## Bài tập luyện tập

* [Atcoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f)
* [Codeforces - Nuclear Fusion](http://codeforces.com/problemset/problem/71/E)
* [Codeforces - Sandy and Nuts](http://codeforces.com/problemset/problem/599/E)
* [Uva 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185)
* [UVa 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925)
