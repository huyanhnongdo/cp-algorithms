---
tags:
  - Translated
e_maxx_link: length_of_segments_union
lang: vi
---
# Độ dài hợp của các đoạn thẳng

Cho $n$ đoạn thẳng trên một đường thẳng, mỗi đoạn được mô tả bởi một cặp tọa độ $(a_{i1}, a_{i2})$.
Chúng ta cần tìm độ dài hợp của các đoạn thẳng đó.

Thuật toán sau đây được đề xuất bởi Klee vào năm 1977.
Nó hoạt động với độ phức tạp thời gian $O(n\log n)$ và đã được chứng minh là tối ưu về mặt tiệm cận.

## Lời giải

Chúng ta lưu trữ các điểm đầu mút của tất cả các đoạn thẳng vào một mảng $x$, được sắp xếp theo giá trị tọa độ.
Ngoài ra, chúng ta lưu trữ thêm thông tin cho biết đó là điểm đầu bên trái hay điểm đầu bên phải của một đoạn thẳng.
Bây giờ, chúng ta duyệt qua mảng này, duy trì một biến đếm $c$ số lượng các đoạn thẳng đang mở.
Mỗi khi phần tử hiện tại là một điểm đầu bên trái, chúng ta tăng biến đếm này lên, và ngược lại, chúng ta giảm nó đi.
Để tính kết quả, mỗi khi đến một tọa độ mới, nếu hiện đang có ít nhất một đoạn thẳng được mở, chúng ta cộng vào kết quả khoảng cách giữa tọa độ hiện tại và giá trị $x$ trước đó $x_i - x_{i-1}$.

## Cài đặt

```cpp
int length_union(const vector<pair<int, int>> &a) {
    int n = a.size();
    vector<pair<int, bool>> x(n*2);
    for (int i = 0; i < n; i++) {
        x[i*2] = {a[i].first, false};
        x[i*2+1] = {a[i].second, true};
    }

    sort(x.begin(), x.end());

    int result = 0;
    int c = 0;
    for (int i = 0; i < n * 2; i++) {
        if (i > 0 && x[i].first > x[i-1].first && c > 0)
            result += x[i].first - x[i-1].first;
        if (x[i].second)
            c--;
        else
            c++;
    }
    return result;
}
```