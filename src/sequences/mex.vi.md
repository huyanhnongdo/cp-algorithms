---
tags:
    - Original
title: MEX (minimal excluded) of a sequence
lang: vi
---
# MEX (phần tử nhỏ nhất không xuất hiện) của một dãy

Cho một mảng $A$ có kích thước $N$. Bạn cần tìm phần tử không âm nhỏ nhất không có mặt trong mảng. Số đó thường được gọi là **MEX** (viết tắt của Minimal Excluded - phần tử nhỏ nhất không xuất hiện).

$$
\begin{align}
\text{mex}(\{0, 1, 2, 4, 5\}) &= 3 \\
\text{mex}(\{0, 1, 2, 3, 4\}) &= 5 \\
\text{mex}(\{1, 2, 3, 4, 5\}) &= 0 \\
\end{align}
$$

Lưu ý rằng MEX của một mảng có kích thước $N$ không bao giờ lớn hơn chính $N$.

Cách tiếp cận đơn giản nhất là tạo một tập hợp (set) chứa tất cả các phần tử trong mảng $A$, để chúng ta có thể kiểm tra nhanh liệu một số có thuộc mảng hay không. Sau đó, chúng ta có thể kiểm tra tất cả các số từ $0$ đến $N$, nếu số hiện tại không có trong tập hợp, hãy trả về số đó.

## Cài đặt

Thuật toán sau đây chạy với độ phức tạp thời gian $O(N \log N)$.

```{.cpp file=mex_simple}
int mex(vector<int> const& A) {
    set<int> b(A.begin(), A.end());

    int result = 0;
    while (b.count(result))
        ++result;
    return result;
}
```

Nếu một thuật toán yêu cầu tính toán $O(N)$ MEX, ta có thể thực hiện bằng cách sử dụng một vector boolean thay vì một tập hợp. Lưu ý rằng mảng cần phải có kích thước đủ lớn để chứa kích thước mảng tối đa có thể.

```{.cpp file=mex_linear}
int mex(vector<int> const& A) {
    static bool used[MAX_N+1] = { 0 };

    // mark the given numbers
    for (int x : A) {
        if (x <= MAX_N)
            used[x] = true;
    }

    // find the mex
    int result = 0;
    while (used[result])
        ++result;
 
    // clear the array again
    for (int x : A) {
        if (x <= MAX_N)
            used[x] = false;
    }

    return result;
}
```

Cách tiếp cận này rất nhanh, nhưng chỉ hoạt động tốt nếu bạn cần tính MEX một lần duy nhất. Nếu bạn cần tính MEX nhiều lần, ví dụ như do mảng liên tục thay đổi, thì phương pháp này không hiệu quả. Khi đó, chúng ta cần một phương pháp tốt hơn.

## MEX với các cập nhật trên mảng

Trong bài toán này, bạn cần thay đổi từng số riêng lẻ trong mảng và tính MEX mới của mảng sau mỗi lần cập nhật như vậy.

Chúng ta cần một cấu trúc dữ liệu tốt hơn để xử lý các truy vấn này một cách hiệu quả.

Một hướng tiếp cận là lấy tần suất của từng số từ $0$ đến $N$ và xây dựng một cấu trúc dữ liệu dạng cây trên đó. Ví dụ: Cây phân đoạn (Segment Tree) hoặc một Treap. Mỗi nút đại diện cho một đoạn các số, và cùng với tổng tần suất trong đoạn đó, bạn lưu trữ thêm số lượng các số phân biệt trong đoạn đó. Bạn có thể cập nhật cấu trúc dữ liệu này trong $O(\log N)$ thời gian, và cũng tìm MEX trong $O(\log N)$ bằng cách thực hiện Tìm kiếm nhị phân (Binary Search) cho MEX. Nếu nút đại diện cho đoạn $[0, \lfloor N/2 \rfloor)$ không chứa $\lfloor N/2 \rfloor$ số phân biệt, thì một số đã bị thiếu và MEX sẽ nhỏ hơn $\lfloor N/2 \rfloor$, lúc này bạn có thể đệ quy sang nhánh bên trái của cây. Ngược lại, nếu nó có ít nhất $\lfloor N/2 \rfloor$ số, thì MEX sẽ nằm ở phía bên phải và bạn có thể đệ quy sang nhánh bên phải.

Bạn cũng có thể sử dụng các cấu trúc dữ liệu trong thư viện chuẩn là `map` và `set` (dựa trên cách tiếp cận được giải thích [tại đây](https://codeforces.com/blog/entry/81287?#comment-677837)). Với `map`, chúng ta sẽ ghi nhớ tần suất của mỗi số, và với `set`, chúng ta đại diện cho các số hiện đang thiếu trong mảng. Vì `set` được sắp xếp thứ tự, `*set.begin()` sẽ chính là MEX. Tổng cộng chúng ta cần $O(N \log N)$ để tiền xử lý, sau đó MEX có thể được tính trong $O(1)$ và cập nhật có thể được thực hiện trong $O(\log N)$.

```{.cpp file=mex_updates}
class Mex {
private:
    map<int, int> frequency;
    set<int> missing_numbers;
    vector<int> A;

public:
    Mex(vector<int> const& A) : A(A) {
        for (int i = 0; i <= A.size(); i++)
            missing_numbers.insert(i);

        for (int x : A) {
            ++frequency[x];
            missing_numbers.erase(x);
        }
    }

    int mex() {
        return *missing_numbers.begin();
    }

    void update(int idx, int new_value) {
        if (--frequency[A[idx]] == 0)
            missing_numbers.insert(A[idx]);
        A[idx] = new_value;
        ++frequency[new_value];
        missing_numbers.erase(new_value);
    }
};
```

## Bài tập luyện tập

- [AtCoder: Neq Min](https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c)
- [Codeforces: Informatics in MAC](https://codeforces.com/contest/1935/problem/B)
- [Codeforces: Replace by MEX](https://codeforces.com/contest/1375/problem/D)
- [Codeforces: Vitya and Strange Lesson](https://codeforces.com/problemset/problem/842/D)
- [Codeforces: MEX Queries](https://codeforces.com/contest/817/problem/F)