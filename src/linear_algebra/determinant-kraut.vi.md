---
title: Calculating the determinant using Kraut method
tags:
  - Original
lang: vi
---
# Tính định thức bằng phương pháp Kraut trong $O(N^3)$

Trong bài viết này, chúng ta sẽ mô tả cách tìm định thức của một ma trận bằng phương pháp Kraut, một thuật toán có độ phức tạp thời gian $O(N^3)$.

Thuật toán Kraut thực hiện phân tích ma trận $A$ thành $A = L U$, trong đó $L$ là ma trận tam giác dưới và $U$ là ma trận tam giác trên. Không mất tính tổng quát, ta có thể giả định rằng tất cả các phần tử trên đường chéo chính của $L$ đều bằng 1. Một khi đã xác định được các ma trận này, việc tính định thức của $A$ trở nên rất đơn giản: nó bằng tích của tất cả các phần tử trên đường chéo chính của ma trận $U$.

Có một định lý phát biểu rằng bất kỳ ma trận khả nghịch nào cũng có một phân tích LU, và phân tích này là duy nhất, khi và chỉ khi tất cả các định thức con chính (principle minors) của nó đều khác không. Chúng ta chỉ xét loại phân tích mà đường chéo của ma trận $L$ toàn là số 1.

Gọi $A$ là ma trận và $N$ là kích thước của nó. Chúng ta sẽ tìm các phần tử của ma trận $L$ và $U$ bằng các bước sau:

 1. Đặt $L_{i i} = 1$ với $i = 1, 2, ..., N$.
 2. Với mỗi $j = 1, 2, ..., N$, thực hiện:
      - Với $i = 1, 2, ..., j$, tìm các giá trị:
        
        \[U_{ij} = A_{ij} - \sum_{k=1}^{i-1} L_{ik} \cdot U_{kj}\]
 
      - Tiếp theo, với $i = j+1, j+2, ..., N$, tìm các giá trị:
 
        \[L_{ij} = \frac{1}{U_{jj}} \left(A_{ij} - \sum_{k=1}^{j-1} L_{ik} \cdot U_{kj} \right).\]

## Cài đặt

```java
static BigInteger det (BigDecimal a [][], int n) {
	try {

	for (int i=0; i<n; i++) {
		boolean nonzero = false;
		for (int j=0; j<n; j++)
			if (a[i][j].compareTo (new BigDecimal (BigInteger.ZERO)) > 0)
				nonzero = true;
		if (!nonzero)
			return BigInteger.ZERO;
	}

	BigDecimal scaling [] = new BigDecimal [n];
	for (int i=0; i<n; i++) {
		BigDecimal big = new BigDecimal (BigInteger.ZERO);
		for (int j=0; j<n; j++)
			if (a[i][j].abs().compareTo (big) > 0)
				big = a[i][j].abs();
		scaling[i] = (new BigDecimal (BigInteger.ONE)) .divide
			(big, 100, BigDecimal.ROUND_HALF_EVEN);
	}

	int sign = 1;

	for (int j=0; j<n; j++) {
		for (int i=0; i<j; i++) {
			BigDecimal sum = a[i][j];
			for (int k=0; k<i; k++)
				sum = sum.subtract (a[i][k].multiply (a[k][j]));
			a[i][j] = sum;
		}

		BigDecimal big = new BigDecimal (BigInteger.ZERO);
		int imax = -1;
		for (int i=j; i<n; i++) {
			BigDecimal sum = a[i][j];
			for (int k=0; k<j; k++)
				sum = sum.subtract (a[i][k].multiply (a[k][j]));
			a[i][j] = sum;
			BigDecimal cur = sum.abs();
			cur = cur.multiply (scaling[i]);
			if (cur.compareTo (big) >= 0) {
				big = cur;
				imax = i;
			}
		}

		if (j != imax) {
			for (int k=0; k<n; k++) {
				BigDecimal t = a[j][k];
				a[j][k] = a[imax][k];
				a[imax][k] = t;
			}

			BigDecimal t = scaling[imax];
			scaling[imax] = scaling[j];
			scaling[j] = t;

			sign = -sign;
		}

		if (j != n-1)
			for (int i=j+1; i<n; i++)
				a[i][j] = a[i][j].divide
					(a[j][j], 100, BigDecimal.ROUND_HALF_EVEN);

	}

	BigDecimal result = new BigDecimal (1);
	if (sign == -1)
		result = result.negate();
	for (int i=0; i<n; i++)
		result = result.multiply (a[i][i]);

	return result.divide
		(BigDecimal.valueOf(1), 0, BigDecimal.ROUND_HALF_EVEN).toBigInteger();
	}
	catch (Exception e) {
		return BigInteger.ZERO;
	}
}
```