---
title: K-th order statistic in O(N)
tags:
  - Translated
e_maxx_link: kth_order_statistics
lang: vi
---
# Phần tử nhỏ thứ $K$ trong $O(N)$

Cho một mảng $A$ có kích thước $N$ và một số $K$. Bài toán đặt ra là tìm số lớn thứ $K$ trong mảng, hay còn gọi là phần tử nhỏ thứ $K$ (thứ tự thống kê).

Ý tưởng cơ bản là sử dụng tư tưởng của thuật toán sắp xếp nhanh (Quick Sort). Thực tế, thuật toán này rất đơn giản, nhưng việc chứng minh nó chạy trong thời gian trung bình $O(N)$ sẽ khó hơn so với Quick Sort.

## Cài đặt (không dùng đệ quy)

```cpp
template <class T>
T order_statistics (std::vector<T> a, unsigned n, unsigned k)
{
    using std::swap;
    for (unsigned l=1, r=n; ; )
    {
        if (r <= l+1)
        {
            // the current part size is either 1 or 2, so it is easy to find the answer
            if (r == l+1 && a[r] < a[l])
                swap (a[l], a[r]);
            return a[k];
        }

        // ordering a[l], a[l+1], a[r]
        unsigned mid = (l + r) >> 1;
        swap (a[mid], a[l+1]);
        if (a[l] > a[r])
            swap (a[l], a[r]);
        if (a[l+1] > a[r])
            swap (a[l+1], a[r]);
        if (a[l] > a[l+1])
            swap (a[l], a[l+1]);

        // performing division
        // barrier is a[l + 1], i.e. median among a[l], a[l + 1], a[r]
        unsigned
            i = l+1,
            j = r;
        const T
            cur = a[l+1];
        for (;;)
        {
            while (a[++i] < cur) ;
            while (a[--j] > cur) ;
            if (i > j)
                break;
            swap (a[i], a[j]);
        }

        // inserting the barrier
        a[l+1] = a[j];
        a[j] = cur;
        
        // we continue to work in that part, which must contain the required element
        if (j >= k)
            r = j-1;
        if (j <= k)
            l = i;
    }
}
```

## Ghi chú
* Thuật toán ngẫu nhiên ở trên được gọi là [Quickselect](https://en.wikipedia.org/wiki/Quickselect). Bạn nên xáo trộn ngẫu nhiên (random shuffle) mảng $A$ trước khi gọi hàm hoặc chọn một phần tử ngẫu nhiên làm chốt (pivot) để thuật toán chạy ổn định. Ngoài ra còn có các thuật toán tất định giải quyết bài toán này trong thời gian tuyến tính, ví dụ như thuật toán [Trung vị của các trung vị](https://en.wikipedia.org/wiki/Median_of_medians) (median of medians).
* [std::nth_element](https://en.cppreference.com/w/cpp/algorithm/nth_element) giải quyết bài toán này trong C++, tuy nhiên cài đặt của gcc có độ phức tạp trường hợp xấu nhất là $O(n \log n )$.
* Việc tìm $K$ phần tử nhỏ nhất có thể quy về bài toán tìm phần tử thứ $K$ với chi phí tuyến tính bổ sung, vì đó chính là các phần tử nhỏ hơn phần tử thứ $K$.

## Bài tập luyện tập
- [Leetcode: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
- [CODECHEF: Median](https://www.codechef.com/problems/CD1IT1)