---
tags:
  - Translated
e_maxx_link: matrix_rank
lang: vi
---
# Tìm hạng của một ma trận

**Hạng của một ma trận** (rank of a matrix) là số lượng lớn nhất các hàng/cột độc lập tuyến tính của ma trận đó. Hạng không chỉ được định nghĩa cho các ma trận vuông.

Hạng của ma trận cũng có thể được định nghĩa là bậc lớn nhất của bất kỳ định thức con nào khác không trong ma trận.

Giả sử ma trận là hình chữ nhật và có kích thước $N \times M$.
Lưu ý rằng nếu ma trận là ma trận vuông và định thức của nó khác không, thì hạng của nó là $N$ ($=M$); nếu không, hạng sẽ nhỏ hơn. Tổng quát hơn, hạng của một ma trận không vượt quá $\min (N, M)$.

## Thuật toán

Bạn có thể tìm hạng của ma trận bằng cách sử dụng [Khử Gauss](linear-system-gauss.md). Chúng ta sẽ thực hiện các thao tác tương tự như khi giải hệ phương trình hoặc tìm định thức của nó. Tuy nhiên, nếu tại bất kỳ bước nào, ở cột thứ $i$ không có hàng nào chứa phần tử khác không trong số các hàng mà chúng ta chưa chọn, thì chúng ta sẽ bỏ qua bước đó.
Ngược lại, nếu chúng ta tìm thấy một hàng có phần tử khác không ở cột thứ $i$ trong bước thứ $i$, thì chúng ta đánh dấu hàng đó là đã chọn, tăng hạng lên một đơn vị (ban đầu hạng được đặt bằng $0$), và thực hiện các thao tác biến đổi thông thường để khử phần tử đó ở các hàng còn lại.

## Độ phức tạp

Thuật toán này có độ phức tạp thời gian là $\mathcal{O}(n^3)$.

## Cài đặt

```{.cpp file=matrix-rank}
const double EPS = 1E-9;

int compute_rank(vector<vector<double>> A) {
    int n = A.size();
    int m = A[0].size();

    int rank = 0;
    vector<bool> row_selected(n, false);
    for (int i = 0; i < m; ++i) {
        int j;
        for (j = 0; j < n; ++j) {
            if (!row_selected[j] && abs(A[j][i]) > EPS)
                break;
        }

        if (j != n) {
            ++rank;
            row_selected[j] = true;
            for (int p = i + 1; p < m; ++p)
                A[j][p] /= A[j][i];
            for (int k = 0; k < n; ++k) {
                if (k != j && abs(A[k][i]) > EPS) {
                    for (int p = i + 1; p < m; ++p)
                        A[k][p] -= A[j][p] * A[k][i];
                }
            }
        }
    }
    return rank;
}
```

## Bài tập
 * [TIMUS1041 Nikifor](http://acm.timus.ru/problem.aspx?space=1&num=1041)