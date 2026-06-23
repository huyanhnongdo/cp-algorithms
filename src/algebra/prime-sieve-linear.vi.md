---
tags:
  - Translated
e_maxx_link: prime_sieve_linear
lang: vi
---

# Sàng tuyến tính (Linear Sieve)

Cho số tự nhiên $n$, tìm tất cả các số nguyên tố trong đoạn $[2;n]$.

Cách thông thường để giải quyết bài toán này là sử dụng [sàng Eratosthenes](sieve-of-eratosthenes.md). Thuật toán này rất đơn giản nhưng có độ phức tạp thời gian chạy là $O(n \log \log n)$.

Mặc dù có nhiều thuật toán đã biết với thời gian chạy dưới tuyến tính (tức là $o(n)$), thuật toán được mô tả dưới đây vẫn rất thú vị bởi sự đơn giản của nó: nó không phức tạp hơn sàng Eratosthenes cổ điển là bao.

Bên cạnh đó, như một tác dụng phụ hữu ích, thuật toán này còn tính toán được **phân tích thừa số nguyên tố của mọi số** trong đoạn $[2; n]$, điều này có thể rất hữu ích trong nhiều ứng dụng thực tế.

Điểm yếu của thuật toán này là sử dụng nhiều bộ nhớ hơn sàng Eratosthenes cổ điển: nó yêu cầu một mảng gồm $n$ số nguyên, trong khi sàng Eratosthenes cổ điển chỉ cần tối đa $n$ bit bộ nhớ (ít hơn khoảng 32 lần).

Do đó, thuật toán này chỉ nên được sử dụng cho các số có phạm vi cỡ $10^7$ trở xuống.

Thuật toán này do Paul Pritchard phát triển. Đây là một biến thể của Thuật toán 3.3 trong tài liệu (Pritchard, 1987: xem tài liệu tham khảo ở cuối bài viết).

## Thuật toán

Mục tiêu của chúng ta là tính toán **ước nguyên tố nhỏ nhất** $lp [i]$ cho mỗi số $i$ trong đoạn $[2; n]$.

Ngoài ra, chúng ta cần lưu trữ danh sách tất cả các số nguyên tố được tìm thấy - gọi danh sách này là $pr []$.

Chúng ta sẽ khởi tạo các giá trị $lp [i]$ bằng số 0, điều này có nghĩa là ban đầu giả định tất cả các số đều là số nguyên tố. Trong quá trình thực thi thuật toán, mảng này sẽ dần được lấp đầy.

Bây giờ chúng ta sẽ duyệt qua các số từ 2 đến $n$. Có hai trường hợp xảy ra đối với số $i$ hiện tại:

- $lp[i] = 0$: nghĩa là $i$ là số nguyên tố, vì chúng ta chưa tìm thấy bất kỳ ước số nào nhỏ hơn nó.  
  Do đó, chúng ta gán $lp [i] = i$ và thêm $i$ vào cuối danh sách số nguyên tố $pr[]$.

- $lp[i] \neq 0$: nghĩa là $i$ là hợp số, và ước nguyên tố nhỏ nhất của nó là $lp [i]$.

Trong cả hai trường hợp, chúng ta cập nhật giá trị của $lp []$ cho các số chia hết cho $i$. Tuy nhiên, mục tiêu của chúng ta là làm sao chỉ gán giá trị $lp []$ tối đa một lần cho mỗi số. Chúng ta có thể thực hiện như sau:

Xét các số $x_j = i \cdot p_j$, trong đó $p_j$ là tất cả các số nguyên tố nhỏ hơn hoặc bằng $lp [i]$ (đây là lý do tại sao chúng ta cần lưu trữ danh sách các số nguyên tố đã tìm thấy).

Chúng ta sẽ gán giá trị mới $lp [x_j] = p_j$ cho tất cả các số có dạng này.

Chứng minh tính đúng đắn của thuật toán và thời gian chạy của nó được trình bày ở phần sau cài đặt.

## Cài đặt

```cpp
const int N = 10000000;
vector<int> lp(N+1);
vector<int> pr;
 
for (int i=2; i <= N; ++i) {
	if (lp[i] == 0) {
		lp[i] = i;
		pr.push_back(i);
	}
	for (int j = 0; i * pr[j] <= N; ++j) {
		lp[i * pr[j]] = pr[j];
		if (pr[j] == lp[i]) {
			break;
		}
	}
}
```

## Chứng minh tính đúng đắn

Chúng ta cần chứng minh rằng thuật toán gán tất cả các giá trị $lp []$ một cách chính xác, và mỗi giá trị được gán chính xác một lần. Do đó, thuật toán sẽ có độ phức tạp thời gian tuyến tính, vì tất cả các thao tác còn lại rõ ràng chạy trong thời gian $O (n)$.

Lưu ý rằng mỗi số $i$ có duy nhất một cách biểu diễn dưới dạng:

$$i = lp [i] \cdot x,$$

trong đó $lp [i]$ là ước nguyên tố nhỏ nhất của $i$, và số $x$ không có bất kỳ ước nguyên tố nào nhỏ hơn $lp [i]$, tức là:

$$lp [i] \le lp [x].$$

Bây giờ, hãy so sánh điều này với các bước của thuật toán: thực tế, với mỗi số $x$, thuật toán duyệt qua tất cả các số nguyên tố có thể nhân với nó, tức là tất cả các số nguyên tố từ nhỏ đến lớn cho tới khi gặp $lp [x]$ (bao gồm cả $lp [x]$), nhằm tạo ra các số có dạng nêu trên.

Do đó, thuật toán sẽ duyệt qua mỗi hợp số đúng một lần, và gán giá trị chính xác cho $lp []$ tại đó. (đpcm)

## Thời gian chạy và Bộ nhớ

Mặc dù thời gian chạy $O(n)$ tốt hơn so với độ phức tạp $O(n \log \log n)$ của sàng Eratosthenes cổ điển, sự khác biệt thực tế giữa chúng không quá lớn.
Trong thực tế, sàng tuyến tính chạy nhanh tương đương với một bản cài đặt thông thường của sàng Eratosthenes.

So với các phiên bản cải tiến của sàng Eratosthenes, ví dụ như sàng phân đoạn (segmented sieve), sàng tuyến tính chạy chậm hơn nhiều.

Xét về mặt bộ nhớ yêu cầu — gồm một mảng $lp []$ có độ dài $n$ và mảng $pr []$ có độ dài $\frac n {\ln n}$ — thuật toán này có vẻ kém tối ưu hơn sàng cổ điển về mọi mặt.

Tuy nhiên, giá trị lớn nhất của thuật toán này là nó tính toán mảng $lp []$, cho phép chúng ta tìm phân tích thừa số nguyên tố của bất kỳ số nào trong đoạn $[2; n]$ trong thời gian tỷ lệ thuận với số lượng thừa số nguyên tố của số đó. Hơn nữa, bằng cách sử dụng thêm một mảng phụ, chúng ta có thể tránh được các phép chia khi thực hiện phân tích thừa số nguyên tố.

Biết được phân tích thừa số nguyên tố của mọi số rất hữu ích cho một số bài toán, và thuật toán này là một trong số ít thuật toán cho phép tìm chúng trong thời gian tuyến tính.

## Tài liệu tham khảo

- Paul Pritchard, **Linear Prime-Number Sieves: a Family Tree**, Science of Computer Programming, vol. 9 (1987), pp.17-35.
