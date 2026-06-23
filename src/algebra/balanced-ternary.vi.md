---
tags:
  - Translated
e_maxx_link: balanced_ternary
lang: vi
---

# Hệ tam phân cân bằng (Balanced Ternary)

!["Setun computer using Balanced Ternary system"](https://earltcampbell.files.wordpress.com/2014/12/setun.jpeg?w=300)

Đây là một **hệ đếm (numeral system)** không chuẩn nhưng vẫn có tính chất vị trí. Đặc điểm của nó là các chữ số có thể nhận một trong ba giá trị là `-1`, `0` và `1`.
Mặc dù vậy, cơ số của hệ đếm này vẫn là `3` (vì có ba giá trị chữ số khả dĩ). Do việc viết số `-1` dưới dạng một chữ số không được thuận tiện cho lắm,
chúng ta sẽ sử dụng chữ cái `Z` thay thế cho ký tự này ở các phần tiếp theo. Nếu bạn nghĩ đây là một hệ đếm khá kỳ lạ — hãy nhìn vào bức ảnh trên — đây là một trong những chiếc máy tính đầu tiên (máy tính Setun của Liên Xô) sử dụng hệ đếm này.

Dưới đây là một vài số tự nhiên đầu tiên được viết dưới dạng hệ tam phân cân bằng:

```nohighlight
    0    0
    1    1
    2    1Z
    3    10
    4    11
    5    1ZZ
    6    1Z0
    7    1Z1
    8    10Z
    9    100
```

Hệ đếm này cho phép bạn viết các giá trị âm mà không cần dấu trừ ở phía trước: bạn chỉ cần đảo ngược (lật dấu) tất cả các chữ số của số dương tương ứng.

```nohighlight
    -1   Z
    -2   Z1
    -3   Z0
    -4   ZZ
    -5   Z11
```

Lưu ý rằng một số âm sẽ bắt đầu bằng chữ số `Z`, còn số dương bắt đầu bằng chữ số `1`.

## Thuật toán chuyển đổi

Chúng ta có thể dễ dàng chuyển đổi một số cho trước sang **hệ tam phân cân bằng** thông qua việc biểu diễn trung gian số đó dưới dạng hệ tam phân thông thường. Khi một số được viết ở hệ tam phân thông thường, các chữ số của nó sẽ là `0`, `1` hoặc `2`. Duyệt từ chữ số thấp nhất (bên phải nhất), chúng ta giữ nguyên các chữ số `0` và `1`. Tuy nhiên, chữ số `2` sẽ được chuyển thành chữ số `Z` đồng thời cộng thêm `1` vào chữ số tiếp theo bên trái. Chữ số `3` cũng được chuyển thành chữ số `0` và cộng thêm `1` vào chữ số tiếp theo bên trái (chữ số `3` ban đầu không có trong số nhưng có thể xuất hiện sau khi chúng ta cộng thêm 1 từ bước trước đó).

**Ví dụ 1:** Hãy chuyển đổi số `64` sang hệ tam phân cân bằng. Trước tiên, biểu diễn số này ở hệ tam phân thông thường:

$$64_{10} = 02101_{3}$$

Tiến hành xử lý từ chữ số ít ý nghĩa nhất (phải sang trái):

- `1`, `0` và `1` được giữ nguyên vì `0` và `1` được phép trong hệ tam phân cân bằng.
- `2` được chuyển thành `Z` và cộng thêm 1 vào chữ số bên trái, ta thu được xâu số `1Z101`.

Kết quả cuối cùng thu được là `1Z101`.

Chúng ta có thể chuyển đổi ngược lại hệ thập phân bằng cách nhân các chữ số với trọng số vị trí tương ứng:

$$1Z101 = 81 \cdot 1 + 27 \cdot (-1) + 9 \cdot 1 + 3 \cdot 0 + 1 \cdot 1 = 64_{10}$$

**Ví dụ 2:** Hãy chuyển đổi số `237` sang hệ tam phân cân bằng. Trước tiên, biểu diễn số này ở hệ tam phân thông thường:

$$237_{10} = 22210_{3}$$

Tiến hành xử lý từ chữ số ít ý nghĩa nhất (phải sang trái):

- `0` và `1` được giữ nguyên.
- Chữ số `2` thứ nhất (từ phải sang) được chuyển thành `Z` và cộng 1 sang trái, ta được `23Z10`.
- Chữ số `3` được chuyển thành `0` và cộng 1 sang trái, ta được `30Z10`.
- Chữ số `3` tiếp theo được chuyển thành `0` và cộng 1 sang trái (giá trị mặc định ban đầu là `0`), ta được `100Z10`.

Kết quả cuối cùng thu được là `100Z10`.

Chúng ta có thể chuyển đổi ngược lại hệ thập phân bằng cách nhân các chữ số với trọng số vị trí tương ứng:

$$100Z10 = 243 \cdot 1 + 81 \cdot 0 + 27 \cdot 0 + 9 \cdot (-1) + 3 \cdot 1 + 1 \cdot 0 = 237_{10}$$

## Bài tập áp dụng

* [Topcoder SRM 604, Div1-250](http://community.topcoder.com/stat?c=problem_statement&pm=12917&rd=15837)
