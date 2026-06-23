---
tags:
  - Original
lang: vi
---
# Thuật toán Rùa và Thỏ (Floyd's Linked List Cycle Finding Algorithm)

Cho một Danh sách liên kết (Linked List) với điểm bắt đầu được ký hiệu là **head**, danh sách này có thể có hoặc không có chu trình. Ví dụ:

<div style="text-align: center;" markdown="1">

![](tortoise_hare_algo.png)

</div>

Ở đây, chúng ta cần tìm điểm **C**, tức là điểm bắt đầu của chu trình.

## Thuật toán đề xuất
Thuật toán này được gọi là **Thuật toán tìm chu trình của Floyd** hoặc **Thuật toán Rùa và Thỏ**.
Để tìm ra điểm bắt đầu của chu trình, trước tiên chúng ta cần xác định xem chu trình có tồn tại hay không.
Việc này bao gồm hai bước:
1. Xác định sự hiện diện của chu trình.
2. Tìm điểm bắt đầu của chu trình.

### Bước 1: Xác định sự hiện diện của chu trình
1. Sử dụng hai con trỏ $slow$ và $fast$.
2. Ban đầu, cả hai đều trỏ vào **head** của danh sách liên kết.
3. $slow$ di chuyển một bước mỗi lần.
4. $fast$ di chuyển hai bước mỗi lần (tốc độ gấp đôi con trỏ $slow$).
5. Kiểm tra xem tại bất kỳ thời điểm nào chúng có trỏ vào cùng một nút trước khi một trong hai (hoặc cả hai) chạm tới `null` hay không.
6. Nếu chúng trỏ vào cùng một nút tại bất kỳ thời điểm nào trong hành trình, điều đó cho thấy chu trình thực sự tồn tại trong danh sách liên kết.
7. Nếu chúng ta gặp `null`, điều đó cho thấy danh sách liên kết không có chu trình.

<div style="text-align: center;" markdown="1">

![](tortoise_hare_cycle_found.png)

</div>

Bây giờ, khi đã xác định được có chu trình trong danh sách liên kết, chúng ta cần thực hiện bước tiếp theo để tìm điểm bắt đầu của chu trình, tức là **C**.

### Bước 2: Tìm điểm bắt đầu của chu trình
1. Đặt lại con trỏ $slow$ về **head** của danh sách liên kết.
2. Di chuyển cả hai con trỏ mỗi lần một bước.
3. Điểm mà chúng gặp nhau chính là điểm bắt đầu của chu trình.

```java
// Presence of cycle
public boolean hasCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while(fast != null && fast.next != null){
        slow = slow.next;
        fast = fast.next.next;
        if(slow==fast){
            return true;
        }
    }

    return false;
}
```

```java
// Assuming there is a cycle present and slow and fast are point to their meeting point
slow = head;
while(slow!=fast){
	slow = slow.next;
	fast = fast.next;
}

return slow; // the starting point of the cycle.
```

## Tại sao thuật toán hoạt động

### Bước 1: Xác định sự hiện diện của chu trình
Vì con trỏ $fast$ di chuyển với tốc độ gấp đôi $slow$, chúng ta có thể nói rằng tại bất kỳ thời điểm nào, $fast$ sẽ đi được quãng đường gấp đôi $slow$.
Chúng ta cũng có thể suy ra rằng khoảng cách chênh lệch giữa quãng đường mà hai con trỏ này đi được sẽ tăng thêm $1$. 
```
slow: 0 --> 1 --> 2 --> 3 --> 4 (distance covered)
fast: 0 --> 2 --> 4 --> 6 --> 8 (distance covered)
diff: 0 --> 1 --> 2 --> 3 --> 4 (difference between distance covered by both pointers)
```
Gọi $L$ là độ dài của chu trình, và $a$ là số bước cần thiết để con trỏ chậm đi đến đầu vào của chu trình. Tồn tại một số nguyên dương $k$ ($k > 0$) sao cho $k \cdot L \geq a$.
Khi con trỏ chậm đã đi được $k \cdot L$ bước và con trỏ nhanh đã đi được $2 \cdot k \cdot L$ bước, cả hai con trỏ đều nằm trong chu trình. Tại thời điểm này, có một khoảng cách $k \cdot L$ giữa chúng. Với độ dài chu trình vẫn là $L$, điều này có nghĩa là chúng sẽ gặp nhau tại cùng một điểm bên trong chu trình.

### Bước 2: Điểm bắt đầu của chu trình

Hãy thử tính quãng đường mà cả hai con trỏ đã đi được cho đến khi chúng gặp nhau trong chu trình.

<div style="text-align: center;" markdown="1">

![](tortoise_hare_proof.png)

</div>

$slowDist = a + xL + b$            , $x\ge0$

$fastDist = a + yL + b$            , $y\ge0$

- $slowDist$ là tổng quãng đường con trỏ chậm đã đi.
- $fastDist$ là tổng quãng đường con trỏ nhanh đã đi.
- $a$ là số bước cả hai con trỏ cần đi để vào chu trình.
- $b$ là khoảng cách giữa **C** và **G**, tức là khoảng cách giữa điểm bắt đầu chu trình và điểm gặp nhau của hai con trỏ.
- $x$ là số vòng con trỏ chậm đã đi trong chu trình, bắt đầu và kết thúc tại **C**.
- $y$ là số vòng con trỏ nhanh đã đi trong chu trình, bắt đầu và kết thúc tại **C**.

$fastDist = 2 \cdot (slowDist)$

$a + yL + b = 2(a + xL + b)$

Giải phương trình, ta được:

$a=(y-2x)L-b$

trong đó $y-2x$ là một số nguyên.

Điều này về cơ bản có nghĩa là $a$ bước cũng tương đương với việc thực hiện một số vòng lặp đầy đủ trong chu trình và đi lùi $b$ bước.
Vì con trỏ nhanh đã đi trước điểm vào chu trình $b$ bước, nếu nó di chuyển thêm $a$ bước nữa, nó sẽ kết thúc tại điểm đầu vào của chu trình.
Và vì chúng ta cho con trỏ chậm bắt đầu từ điểm đầu của danh sách liên kết, sau $a$ bước, nó cũng sẽ kết thúc tại điểm đầu vào chu trình. Do đó, nếu cả hai cùng di chuyển $a$ bước, cả hai sẽ gặp nhau tại điểm đầu của chu trình.

# Các bài toán:
- [Linked List Cycle (Dễ)](https://leetcode.com/problems/linked-list-cycle/)
- [Happy Number (Dễ)](https://leetcode.com/problems/happy-number/)
- [Find the Duplicate Number (Trung bình)](https://leetcode.com/problems/find-the-duplicate-number/)
- [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)