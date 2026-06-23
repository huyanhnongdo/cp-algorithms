---
tags:
  - Translated
e_maxx_link: determinant_gauss
lang: vi
---
# Tính định thức của ma trận bằng phương pháp Gauss

Bài toán: Cho một ma trận $A$ kích thước $N \times N$. Hãy tính định thức của nó.

## Thuật toán

Chúng ta sử dụng các ý tưởng từ [phương pháp Gauss để giải hệ phương trình tuyến tính](linear-system-gauss.md).

Chúng ta sẽ thực hiện các bước tương tự như trong cách giải hệ phương trình tuyến tính, ngoại trừ việc chia hàng hiện tại cho $a_{ij}$. Các phép toán này sẽ không làm thay đổi giá trị tuyệt đối của định thức ma trận. Tuy nhiên, khi chúng ta tráo đổi hai hàng của ma trận, dấu của định thức có thể thay đổi.

Sau khi áp dụng phương pháp Gauss trên ma trận, ta sẽ thu được một ma trận tam giác (diagonal matrix), trong đó định thức chính là tích của các phần tử trên đường chéo chính. Như đã đề cập trước đó, dấu của định thức có thể được xác định dựa trên số lần tráo đổi hàng (nếu là số lẻ, dấu của định thức phải bị đảo ngược). Như vậy, chúng ta có thể sử dụng thuật toán Gauss để tính định thức của ma trận với độ phức tạp thời gian $O(N^3)$.

Cần lưu ý rằng nếu tại một bước nào đó, chúng ta không tìm thấy phần tử khác 0 ở cột hiện tại, thuật toán nên dừng lại và trả về 0.

## Cài đặt

```cpp
const double EPS = 1E-9;
int n;
vector < vector<double> > a (n, vector<double> (n));

double det = 1;
for (int i=0; i<n; ++i) {
	int k = i;
	for (int j=i+1; j<n; ++j)
		if (abs (a[j][i]) > abs (a[k][i]))
			k = j;
	if (abs (a[k][i]) < EPS) {
		det = 0;
		break;
	}
	swap (a[i], a[k]);
	if (i != k)
		det = -det;
	det *= a[i][i];
	for (int j=i+1; j<n; ++j)
		a[i][j] /= a[i][i];
	for (int j=0; j<n; ++j)
		if (j != i && abs (a[j][i]) > EPS)
			for (int k=i+1; k<n; ++k)
				a[j][k] -= a[i][k] * a[j][i];
}

cout << det;
```

## Bài tập thực hành
* [Codeforces - Wizards and Bets](http://codeforces.com/contest/167/problem/E)