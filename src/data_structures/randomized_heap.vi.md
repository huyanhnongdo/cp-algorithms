---
tags:
  - Translated
e_maxx_link: randomized_heap
lang: vi
---

# Heap ngẫu nhiên (Randomized Heap)

Heap ngẫu nhiên (Randomized Heap) là một cấu trúc dữ liệu heap sử dụng tính ngẫu nhiên (randomization) để thực hiện tất cả các thao tác trong thời gian kỳ vọng là hàm logarit.

Một **min heap** là một cây nhị phân trong đó giá trị của mỗi đỉnh luôn nhỏ hơn hoặc bằng giá trị của các con của nó.
Do đó, phần tử nhỏ nhất của cây luôn nằm ở đỉnh gốc.

Một max heap được định nghĩa tương tự: bằng cách thay thế "nhỏ hơn hoặc bằng" thành "lớn hơn hoặc bằng".

Các thao tác cơ bản của một heap bao gồm:

- Thêm một giá trị
- Lấy ra giá trị nhỏ nhất
- Xóa giá trị nhỏ nhất
- Hợp nhất hai heap (không loại bỏ các phần tử trùng lặp)
- Xóa một phần tử bất kỳ (nếu biết trước vị trí của nó trên cây)

Một heap ngẫu nhiên có thể thực hiện tất cả các thao tác này trong thời gian kỳ vọng $O(\log n)$ với cách cài đặt cực kỳ đơn giản.

## Cấu trúc dữ liệu

Chúng ta có thể mô tả cấu trúc của heap nhị phân như sau:

```{.cpp file=randomized_heap_structure}
struct Tree {
    int value;
    Tree * l = nullptr;
    Tree * r = nullptr;
};
```

Tại mỗi đỉnh, chúng ta lưu trữ một giá trị.
Ngoài ra, chúng ta có các con trỏ đến các con bên trái và con bên phải, trỏ đến `nullptr` nếu con tương ứng không tồn tại.

## Các thao tác

Không khó để nhận thấy rằng mọi thao tác trên heap đều có thể đưa về một thao tác duy nhất: **hợp nhất** (merging) hai heap thành một.
Thật vậy, việc thêm một giá trị mới vào heap tương đương với việc hợp nhất heap hiện tại với một heap chỉ gồm một đỉnh duy nhất chứa giá trị đó.
Việc tìm phần tử nhỏ nhất không cần bất kỳ thao tác nào cả - giá trị nhỏ nhất đơn giản là giá trị tại gốc.
Việc xóa phần tử nhỏ nhất tương đương với kết quả của việc hợp nhất hai cây con bên trái và bên phải của đỉnh gốc.
Và việc xóa một phần tử bất kỳ cũng tương tự: chúng ta hợp nhất các con của đỉnh đó rồi thay thế đỉnh đó bằng kết quả của phép hợp nhất.

Vì vậy, trên thực tế chúng ta chỉ cần cài đặt thao tác hợp nhất hai heap.
Tất cả các thao tác khác đều được đưa về thao tác này một cách dễ dàng.

Giả sử chúng ta cần hợp nhất hai heap $T_1$ và $T_2$.
Rõ ràng là gốc của mỗi heap này đều chứa giá trị nhỏ nhất tương ứng của chúng.
Do đó, gốc của heap kết quả sau khi hợp nhất phải là giá trị nhỏ hơn trong hai giá trị này.
Vì vậy, chúng ta so sánh hai giá trị gốc, chọn gốc nhỏ hơn làm gốc mới.
Bây giờ, chúng ta phải kết hợp các con của đỉnh đã chọn với heap còn lại.
Để làm điều này, chúng ta chọn một trong hai con và hợp nhất nó với heap còn lại.
Như vậy, chúng ta lại tiếp tục thực hiện thao tác hợp nhất hai heap.
Sớm hay muộn thì quá trình này cũng sẽ kết thúc (số bước thực hiện tối đa bằng tổng chiều cao của hai heap).

Để đạt được độ phức tạp logarit trên trung bình, chúng ta cần xác định cách chọn một trong hai con sao cho độ dài đường đi trung bình là logarit.
Không khó để đoán rằng chúng ta sẽ đưa ra quyết định này một cách **ngẫu nhiên**.
Do đó, thao tác hợp nhất được cài đặt như sau:

```{.cpp file=randomized_heap_merge}
Tree* merge(Tree* t1, Tree* t2) {
    if (!t1 || !t2)
        return t1 ? t1 : t2;
    if (t2->value < t1->value)
        swap(t1, t2);
    if (rand() & 1)
        swap(t1->l, t1->r);
    t1->l = merge(t1->l, t2);
    return t1;
}
```

Ở đây, đầu tiên chúng ta kiểm tra xem có heap nào rỗng hay không, nếu có thì không cần thực hiện hợp nhất mà trả về ngay heap còn lại.
Ngược lại, chúng ta chọn `t1` là heap có giá trị gốc nhỏ hơn (hoán đổi `t1` và `t2` nếu cần).
Chúng ta muốn hợp nhất con bên trái của `t1` với `t2`, do đó chúng ta hoán đổi ngẫu nhiên hai con của `t1`, sau đó thực hiện gọi đệ quy hàm hợp nhất.

## Phân tích độ phức tạp

Chúng ta gọi biến ngẫu nhiên $h(T)$ biểu thị **độ dài của đường đi ngẫu nhiên** từ gốc đến lá (độ dài tính bằng số cạnh).
Rõ ràng thuật toán `merge` thực hiện $O(h(T_1) + h(T_2))$ bước.
Do đó, để hiểu độ phức tạp của các thao tác, chúng ta cần tìm hiểu biến ngẫu nhiên $h(T)$.

### Giá trị kỳ vọng

Chúng ta giả định rằng kỳ vọng của $h(T)$ có thể được chặn trên bởi logarit của số đỉnh trong heap:

$$\mathbf{E} h(T) \le \log(n+1)$$

Điều này có thể được chứng minh dễ dàng bằng quy nạp.
Gọi $L$ và $R$ lần lượt là cây con trái và phải của gốc $T$, và $n_L, n_R$ là số đỉnh của chúng ($n = n_L + n_R + 1$).

Dưới đây là bước quy nạp:

$$\begin{align}
\mathbf{E} h(T) &= 1 + \frac{\mathbf{E} h(L) + \mathbf{E} h(R)}{2} 
\le 1 + \frac{\log(n_L + 1) + \log(n_R + 1)}{2} \\\\
&= 1 + \log\sqrt{(n_L + 1)(n_R + 1)} = \log 2\sqrt{(n_L + 1)(n_R + 1)} \\\\
&\le \log \frac{2\left((n_L + 1) + (n_R + 1)\right)}{2} = \log(n_L + n_R + 2) = \log(n+1)
\end{align}$$

### Khả năng vượt quá giá trị kỳ vọng

Tất nhiên, chúng ta chưa thể hoàn toàn hài lòng với giá trị kỳ vọng.
Giá trị kỳ vọng của $h(T)$ không nói lên điều gì về trường hợp xấu nhất.
Vẫn có khả năng là các đường đi từ gốc đến các đỉnh trung bình lớn hơn nhiều so với $\log(n + 1)$ đối với một cây cụ thể nào đó.

Hãy chứng minh rằng xác suất để độ dài đường đi vượt quá giá trị kỳ vọng là cực kỳ nhỏ:

$${\cal P}(h(T) > (c+1) \log n) < \frac{1}{n^c}$$

với mọi hằng số dương $c$.

Ở đây chúng ta ký hiệu $P$ là tập hợp các đường đi từ gốc của heap đến các lá có độ dài vượt quá $(c+1) \log n$.
Lưu ý rằng đối với bất kỳ đường đi $p$ có độ dài $|p|$, xác suất nó được chọn làm đường đi ngẫu nhiên là $2^{-|p|}$.
Do đó ta có:

$${\cal P}(h(T) > (c+1) \log n) = \sum_{p \in P} 2^{-|p|} < \sum_{p \in P} 2^{-(c+1) \log n} = |P| n^{-(c+1)} \le n^{-c}$$

### Độ phức tạp của thuật toán

Như vậy, thuật toán `merge`, và do đó tất cả các thao tác khác được xây dựng dựa trên nó, được thực hiện trong thời gian trung bình $O(\log n)$.

Hơn nữa, với mọi hằng số dương $\epsilon$, luôn tồn tại một hằng số dương $c$ sao cho xác suất để thao tác cần thực hiện nhiều hơn $c \log n$ bước là nhỏ hơn $n^{-\epsilon}$ (theo một khía cạnh nào đó, điều này mô tả hành vi trong trường hợp xấu nhất của thuật toán).
