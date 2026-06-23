---
tags:
  - Translated
e_maxx_link: fft_multiply
---

# Biến đổi Fourier nhanh (FFT)

Trong bài viết này, chúng ta sẽ thảo luận về một thuật toán cho phép nhân hai đa thức có độ dài $n$ trong thời gian $O(n \log n)$, tốt hơn nhiều so với phép nhân thông thường mất thời gian $O(n^2)$.
Rõ ràng, việc nhân hai số lớn cũng có thể được đưa về bài toán nhân đa thức, vì vậy hai số lớn cũng có thể được nhân trong thời gian $O(n \log n)$ (với $n$ là số chữ số của các số đó).

Sự phát hiện ra **Biến đổi Fourier nhanh (Fast Fourier transform - FFT)** được ghi nhận cho Cooley và Tukey, những người đã công bố thuật toán này vào năm 1965.
Nhưng trên thực tế, FFT đã được phát hiện nhiều lần trước đó, nhưng tầm quan trọng của nó chưa được hiểu rõ trước khi máy tính hiện đại ra đời.
Một số nhà nghiên cứu cho rằng Runge và König đã phát hiện ra FFT vào năm 1924.
Nhưng thực tế Gauss đã phát triển một phương pháp như vậy từ năm 1805, chỉ có điều ông chưa từng công bố nó.

Lưu ý rằng thuật toán FFT được trình bày ở đây chạy trong thời gian $O(n \log n)$, nhưng nó không hoạt động để nhân các đa thức lớn bất kỳ với các hệ số lớn tùy ý hoặc để nhân các số nguyên lớn tùy ý.
Nó có thể xử lý dễ dàng các đa thức có kích thước $10^5$ với các hệ số nhỏ, hoặc nhân hai số có kích thước $10^6$ chữ số, thường là đủ để giải các bài toán lập trình thi đấu. Vượt quá quy mô nhân các số có $10^6$ bit, phạm vi và độ chính xác của các số dấu phẩy động được sử dụng trong quá trình tính toán sẽ không đủ để cho ra kết quả cuối cùng chính xác, mặc dù có các biến thể phức tạp hơn có thể thực hiện nhân đa thức/số nguyên lớn tùy ý.
Ví dụ, vào năm 1971, Schönhage và Strasser đã phát triển một biến thể để nhân các số lớn tùy ý bằng cách áp dụng FFT đệ quy trên các cấu trúc vành chạy trong thời gian $O(n \log n \log \log n)$.
Và gần đây (năm 2019) Harvey và van der Hoeven đã công bố một thuật toán chạy trong thời gian thực sự là $O(n \log n)$.

## Biến đổi Fourier rời rạc (DFT)

Xét một đa thức bậc $n - 1$:

$$A(x) = a_0 x^0 + a_1 x^1 + \dots + a_{n-1} x^{n-1}$$

Không mất tính tổng quát, chúng ta giả định rằng $n$ - số lượng hệ số - là một lũy thừa của $2$.
Nếu $n$ không phải là lũy thừa của $2$, chúng ta chỉ cần thêm các số hạng $a_i x^i$ còn thiếu và đặt các hệ số $a_i$ này bằng $0$.

Lý thuyết số phức cho chúng ta biết rằng phương trình $x^n = 1$ có $n$ nghiệm phức (gọi là các căn bậc $n$ của đơn vị), và các nghiệm này có dạng $w_{n, k} = e^{\frac{2 k \pi i}{n}}$ với $k = 0 \dots n-1$.
Ngoài ra, các số phức này có một số tính chất rất thú vị:
ví dụ, căn bậc $n$ sơ cấp $w_n = w_{n, 1} = e^{\frac{2 \pi i}{n}}$ có thể được sử dụng để biểu diễn tất cả các căn bậc $n$ khác: $w_{n, k} = (w_n)^k$.

**Biến đổi Fourier rời rạc (DFT)** của đa thức $A(x)$ (hoặc tương đương là vector hệ số $(a_0, a_1, \dots, a_{n-1})$) được định nghĩa là các giá trị của đa thức tại các điểm $x = w_{n, k}$, tức là nó là vector:

$$\begin{align}
\text{DFT}(a_0, a_1, \dots, a_{n-1}) &= (y_0, y_1, \dots, y_{n-1}) \\
&= (A(w_{n, 0}), A(w_{n, 1}), \dots, A(w_{n, n-1})) \\
&= (A(w_n^0), A(w_n^1), \dots, A(w_n^{n-1}))
\end{align}$$

Tương tự, **biến đổi Fourier rời rạc ngược (IDFT)** được định nghĩa như sau:
IDFT của các giá trị đa thức $(y_0, y_1, \dots, y_{n-1})$ sẽ cho ra các hệ số của đa thức $(a_0, a_1, \dots, a_{n-1})$.

$$\text{InverseDFT}(y_0, y_1, \dots, y_{n-1}) = (a_0, a_1, \dots, a_{n-1})$$

Như vậy, nếu DFT thuận tính toán các giá trị của đa thức tại các điểm căn bậc $n$, thì DFT ngược có thể khôi phục các hệ số của đa thức bằng cách sử dụng các giá trị đó.

### Ứng dụng của DFT: nhân nhanh đa thức

Xét hai đa thức $A$ và $B$.
Chúng ta tính DFT cho mỗi đa thức: $\text{DFT}(A)$ và $\text{DFT}(B)$.

Điều gì xảy ra nếu chúng ta nhân hai đa thức này?
Rõ ràng tại mỗi điểm, các giá trị chỉ đơn giản là được nhân với nhau, tức là:

$$(A \cdot B)(x) = A(x) \cdot B(x).$$

Điều này có nghĩa là nếu chúng ta nhân các vector $\text{DFT}(A)$ và $\text{DFT}(B)$ - bằng cách nhân từng phần tử của vector này với phần tử tương ứng của vector kia - thì chúng ta sẽ thu được chính là DFT của đa thức tích $\text{DFT}(A \cdot B)$:

$$\text{DFT}(A \cdot B) = \text{DFT}(A) \cdot \text{DFT}(B)$$

Cuối cùng, áp dụng DFT ngược, chúng ta thu được:

$$A \cdot B = \text{InverseDFT}(\text{DFT}(A) \cdot \text{DFT}(B))$$

Ở vế phải, tích của hai DFT được hiểu là tích từng phần tử tương ứng của vector.
Phép toán này có thể được tính trong thời gian $O(n)$.
Nếu chúng ta có thể tính DFT và DFT ngược trong thời gian $O(n \log n)$, thì chúng ta có thể tính tích của hai đa thức (và do đó cả hai số lớn) với cùng độ phức tạp thời gian đó.

Cần lưu ý rằng hai đa thức phải có cùng bậc.
Nếu không, hai vector kết quả của DFT sẽ có độ dài khác nhau.
Chúng ta có thể giải quyết điều này bằng cách thêm các hệ số có giá trị bằng $0$.

Và ngoài ra, vì kết quả tích của hai đa thức là một đa thức bậc $2 (n - 1)$, chúng ta phải nhân đôi bậc của mỗi đa thức ban đầu (bằng cách đệm thêm các số $0$).
Từ một vector có $n$ giá trị, chúng ta không thể tái thiết lập đa thức mong muốn có $2n - 1$ hệ số.

### Biến đổi Fourier nhanh (FFT)

**Biến đổi Fourier nhanh (FFT)** là một phương pháp cho phép tính toán DFT trong thời gian $O(n \log n)$.
Ý tưởng cơ bản của FFT là áp dụng chia để trị.
Chúng ta chia vector hệ số của đa thức thành hai vector, tính đệ quy DFT cho từng vector đó, rồi kết hợp các kết quả để tính DFT của đa thức hoàn chỉnh.

Giả sử đa thức $A(x)$ có bậc $n - 1$, trong đó $n$ là lũy thừa của $2$ và $n > 1$:

$$A(x) = a_0 x^0 + a_1 x^1 + \dots + a_{n-1} x^{n-1}$$

Chúng ta chia nó thành hai đa thức nhỏ hơn, một đa thức chỉ chứa các hệ số ở vị trí chẵn, và đa thức còn lại chứa các hệ số ở vị trí lẻ:

$$\begin{align}
A_0(x) &= a_0 x^0 + a_2 x^1 + \dots + a_{n-2} x^{\frac{n}{2}-1} \\
A_1(x) &= a_1 x^0 + a_3 x^1 + \dots + a_{n-1} x^{\frac{n}{2}-1}
\end{align}$$

Dễ dàng nhận thấy rằng:

$$A(x) = A_0(x^2) + x A_1(x^2).$$

Các đa thức $A_0$ và $A_1$ chỉ có số lượng hệ số bằng một nửa so với đa thức $A$.
Nếu chúng ta có thể tính $\text{DFT}(A)$ trong thời gian tuyến tính bằng cách sử dụng $\text{DFT}(A_0)$ và $\text{DFT}(A_1)$, thì chúng ta sẽ có công thức truy hồi về độ phức tạp thời gian là $T_{\text{DFT}}(n) = 2 T_{\text{DFT}}\left(\frac{n}{2}\right) + O(n)$, dẫn đến $T_{\text{DFT}}(n) = O(n \log n)$ theo **định lý thợ (master theorem)**.

Hãy cùng tìm hiểu cách thực hiện điều này.

Giả sử chúng ta đã tính được các vector $\left(y_k^0\right)_{k=0}^{n/2-1} = \text{DFT}(A_0)$ và $\left(y_k^1\right)_{k=0}^{n/2-1} = \text{DFT}(A_1)$.
Hãy tìm biểu thức cho $\left(y_k\right)_{k=0}^{n-1} = \text{DFT}(A)$.

Đối với $\frac{n}{2}$ giá trị đầu tiên, chúng ta có thể sử dụng phương trình đã lưu ý ở trên $A(x) = A_0(x^2) + x A_1(x^2)$:

$$y_k = y_k^0 + w_n^k y_k^1, \quad k = 0 \dots \frac{n}{2} - 1.$$

Tuy nhiên, đối với $\frac{n}{2}$ giá trị thứ hai, chúng ta cần tìm một biểu thức hơi khác một chút:

$$\begin{align}
y_{k+n/2} &= A\left(w_n^{k+n/2}\right) \\
&= A_0\left(w_n^{2k+n}\right) + w_n^{k + n/2} A_1\left(w_n^{2k+n}\right) \\
&= A_0\left(w_n^{2k} w_n^n\right) + w_n^k w_n^{n/2} A_1\left(w_n^{2k} w_n^n\right) \\
&= A_0\left(w_n^{2k}\right) - w_n^k A_1\left(w_n^{2k}\right) \\
&= y_k^0 - w_n^k y_k^1
\end{align}$$

Ở đây chúng ta lại sử dụng $A(x) = A_0(x^2) + x A_1(x^2)$ và hai đồng nhất thức $w_n^n = 1$, $w_n^{n/2} = -1$.

Do đó, chúng ta có được các công thức mong muốn để tính toàn bộ vector $(y_k)$:

$$\begin{align}
y_k &= y_k^0 + w_n^k y_k^1, &\quad k = 0 \dots \frac{n}{2} - 1, \\
y_{k+n/2} &= y_k^0 - w_n^k y_k^1, &\quad k = 0 \dots \frac{n}{2} - 1.
\end{align}$$

(Quy luật kết hợp dạng $a + b$ và $a - b$ này đôi khi được gọi là **phép toán hình bướm (butterfly)**.)

Như vậy, chúng ta đã biết cách tính DFT trong thời gian $O(n \log n)$.

### FFT ngược

Cho trước vector $(y_0, y_1, \dots y_{n-1})$ — là các giá trị của đa thức $A$ bậc $n - 1$ tại các điểm $x = w_n^k$.
Chúng ta muốn khôi phục các hệ số $(a_0, a_1, \dots, a_{n-1})$ của đa thức.
Bài toán này được gọi là **nội suy (interpolation)**, và có các thuật toán tổng quát để giải quyết nó.
Nhưng trong trường hợp đặc biệt này (vì chúng ta biết các giá trị của các điểm tại các căn của đơn vị), chúng ta có thể thu được một thuật toán đơn giản hơn nhiều (về mặt thực hành gần như giống hệt với FFT thuận).

Chúng ta có thể viết DFT, theo định nghĩa của nó, dưới dạng ma trận:

$$
\begin{pmatrix}
w_n^0 & w_n^0 & w_n^0 & w_n^0 & \cdots & w_n^0 \\
w_n^0 & w_n^1 & w_n^2 & w_n^3 & \cdots & w_n^{n-1} \\
w_n^0 & w_n^2 & w_n^4 & w_n^6 & \cdots & w_n^{2(n-1)} \\
w_n^0 & w_n^3 & w_n^6 & w_n^9 & \cdots & w_n^{3(n-1)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
w_n^0 & w_n^{n-1} & w_n^{2(n-1)} & w_n^{3(n-1)} & \cdots & w_n^{(n-1)(n-1)}
\end{pmatrix} \begin{pmatrix}
a_0 \\ a_1 \\ a_2 \\ a_3 \\ \vdots \\ a_{n-1}
\end{pmatrix} = \begin{pmatrix}
y_0 \\ y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_{n-1}
\end{pmatrix}
$$

Ma trận này được gọi là **ma trận Vandermonde**.

Do đó, chúng ta có thể tính vector $(a_0, a_1, \dots, a_{n-1})$ bằng cách nhân vector $(y_0, y_1, \dots y_{n-1})$ từ bên trái với ma trận nghịch đảo:

$$
\begin{pmatrix}
a_0 \\ a_1 \\ a_2 \\ a_3 \\ \vdots \\ a_{n-1}
\end{pmatrix} = \begin{pmatrix}
w_n^0 & w_n^0 & w_n^0 & w_n^0 & \cdots & w_n^0 \\
w_n^0 & w_n^1 & w_n^2 & w_n^3 & \cdots & w_n^{n-1} \\
w_n^0 & w_n^2 & w_n^4 & w_n^6 & \cdots & w_n^{2(n-1)} \\
w_n^0 & w_n^3 & w_n^6 & w_n^9 & \cdots & w_n^{3(n-1)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
w_n^0 & w_n^{n-1} & w_n^{2(n-1)} & w_n^{3(n-1)} & \cdots & w_n^{(n-1)(n-1)}
\end{pmatrix}^{-1} \begin{pmatrix}
y_0 \\ y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_{n-1}
\end{pmatrix}
$$

Một phép kiểm tra nhanh có thể xác nhận rằng nghịch đảo của ma trận có dạng như sau:

$$
\frac{1}{n}
\begin{pmatrix}
w_n^0 & w_n^0 & w_n^0 & w_n^0 & \cdots & w_n^0 \\
w_n^0 & w_n^{-1} & w_n^{-2} & w_n^{-3} & \cdots & w_n^{-(n-1)} \\
w_n^0 & w_n^{-2} & w_n^{-4} & w_n^{-6} & \cdots & w_n^{-2(n-1)} \\
w_n^0 & w_n^{-3} & w_n^{-6} & w_n^{-9} & \cdots & w_n^{-3(n-1)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
w_n^0 & w_n^{-(n-1)} & w_n^{-2(n-1)} & w_n^{-3(n-1)} & \cdots & w_n^{-(n-1)(n-1)}
\end{pmatrix}
$$

Do đó, chúng ta thu được công thức:

$$a_k = \frac{1}{n} \sum_{j=0}^{n-1} y_j w_n^{-k j}$$

So sánh công thức này với công thức tính $y_k$:

$$y_k = \sum_{j=0}^{n-1} a_j w_n^{k j},$$

chúng ta thấy rằng hai bài toán này gần như là một, vì vậy các hệ số $a_k$ có thể được tìm thấy bằng chính thuật toán chia để trị giống như FFT thuận, chỉ khác là thay vì sử dụng $w_n^k$ ta phải sử dụng $w_n^{-k}$, và ở bước cuối cùng chúng ta cần chia các hệ số kết quả cho $n$.

Vì vậy, việc tính toán DFT ngược gần như tương tự với tính toán DFT thuận, và nó cũng có thể được thực hiện trong thời gian $O(n \log n)$.

### Cài đặt

Dưới đây chúng tôi trình bày một **cài đặt đệ quy đơn giản của FFT** và FFT ngược chung trong một hàm duy nhất, vì sự khác biệt giữa FFT thuận và nghịch là cực kỳ nhỏ.
Để lưu trữ các số phức, chúng ta sử dụng kiểu `complex` có sẵn trong thư viện STL của C++.

```{.cpp file=fft_recursive}
using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    if (n == 1)
        return;

    vector<cd> a0(n / 2), a1(n / 2);
    for (int i = 0; 2 * i < n; i++) {
        a0[i] = a[2*i];
        a1[i] = a[2*i+1];
    }
    fft(a0, invert);
    fft(a1, invert);

    double ang = 2 * PI / n * (invert ? -1 : 1);
    cd w(1), wn(cos(ang), sin(ang));
    for (int i = 0; 2 * i < n; i++) {
        a[i] = a0[i] + w * a1[i];
        a[i + n/2] = a0[i] - w * a1[i];
        if (invert) {
            a[i] /= 2;
            a[i + n/2] /= 2;
        }
        w *= wn;
    }
}
```

Hàm nhận vào một vector các hệ số, và hàm sẽ tính DFT hoặc IDFT rồi lưu kết quả ngược lại vào chính vector này.
Đối số $\text{invert}$ xác định xem ta cần tính DFT thuận hay nghịch.
Bên trong hàm, đầu tiên chúng ta kiểm tra xem độ dài vector có bằng 1 hay không, nếu có thì không cần làm gì cả.
Nếu không, chúng ta chia vector $a$ thành hai vector $a0$ and $a1$ rồi tính đệ quy DFT cho cả hai.
Sau đó, chúng ta khởi tạo giá trị $wn$ và biến $w$, biến này sẽ chứa lũy thừa hiện tại của $wn$.
Sau đó, các giá trị DFT kết quả được tính bằng các công thức nêu trên.

Nếu cờ $\text{invert}$ được đặt, chúng ta thay thế $wn$ bằng $wn^{-1}$, và mỗi giá trị kết quả được chia cho $2$ (vì việc này được thực hiện ở mỗi tầng đệ quy, cuối cùng các giá trị đầu ra sẽ được chia cho $n$).

Sử dụng hàm này, chúng ta có thể tạo ra hàm dùng để **nhân hai đa thức**:

```{.cpp file=fft_multiply}
vector<int> multiply(vector<int> const& a, vector<int> const& b) {
    vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < a.size() + b.size()) 
        n <<= 1;
    fa.resize(n);
    fb.resize(n);

    fft(fa, false);
    fft(fb, false);
    for (int i = 0; i < n; i++)
        fa[i] *= fb[i];
    fft(fa, true);

    vector<int> result(n);
    for (int i = 0; i < n; i++)
        result[i] = round(fa[i].real());
    return result;
}
```

Hàm này hoạt động với đa thức có hệ số nguyên, tuy nhiên bạn cũng có thể điều chỉnh để nó hoạt động với các kiểu dữ liệu khác.
Vì có sai số số thực khi làm việc với số phức, chúng ta cần làm tròn hệ số kết quả ở bước cuối cùng.

Cuối cùng, hàm dùng để **nhân** hai số lớn thực chất không khác biệt so với hàm nhân đa thức.
Điều duy nhất chúng ta phải làm sau đó là chuẩn hóa số kết quả (thực hiện phép nhớ):

```cpp
    int carry = 0;
    for (int i = 0; i < n; i++)
        result[i] += carry;
        carry = result[i] / 10;
        result[i] %= 10;
    }
```

Vì độ dài tích của hai số không bao giờ vượt quá tổng độ dài của cả hai số nên kích thước của vector là đủ để thực hiện tất cả các phép toán nhớ số này.

### Cài đặt cải tiến: tính toán tại chỗ (in-place)

Để tăng hiệu suất, chúng ta sẽ chuyển từ cài đặt đệ quy sang cài đặt lặp.
Trong cài đặt đệ quy ở trên, chúng ta đã tách rõ ràng vector $a$ thành hai vector — phần tử ở vị trí chẵn được gán cho một vector tạm thời, và phần tử ở vị trí lẻ cho vector tạm thời khác.
Tuy nhiên, nếu chúng ta sắp xếp lại các phần tử theo một cách nhất định, chúng ta sẽ không cần tạo các vector tạm thời này nữa (tức là tất cả các tính toán có thể được thực hiện "tại chỗ" - in-place, ngay trên chính vector $A$).

Lưu ý rằng ở tầng đệ quy đầu tiên, các phần tử có bit thấp nhất của chỉ số bằng 0 được gán cho vector $a_0$, và các phần tử có bit thấp nhất bằng 1 được gán cho $a_1$.
Ở tầng đệ quy thứ hai, điều tương tự cũng xảy ra, nhưng thay vào đó là bit thấp thứ hai, v.v.
Do đó, nếu chúng ta đảo ngược các bit của chỉ số của mỗi hệ số, rồi sắp xếp chúng theo các giá trị đã đảo ngược này, chúng ta sẽ thu được thứ tự mong muốn (được gọi là hoán vị đảo bit - bit-reversal permutation).

Ví dụ, thứ tự mong muốn cho $n = 8$ có dạng:

$$a = \bigg\{ \Big[ (a_0, a_4), (a_2, a_6) \Big], \Big[ (a_1, a_5), (a_3, a_7) \Big] \bigg\}$$

Thật vậy, ở tầng đệ quy đầu tiên (được bao quanh bởi dấu ngoặc nhọn), vector được chia thành hai phần $[a_0, a_2, a_4, a_6]$ và $[a_1, a_3, a_5, a_7]$.
Như chúng ta thấy, trong hoán vị đảo bit, điều này tương ứng với việc chia vector làm đôi: $\frac{n}{2}$ phần tử đầu tiên và $\frac{n}{2}$ phần tử cuối cùng.
Sau đó, có một lời gọi đệ quy cho mỗi nửa.
Giả sử kết quả DFT của mỗi nửa được ghi đè trực tiếp lên chính các vị trí của phần tử đó (tức là nửa đầu và nửa sau của vector $a$).

$$a = \bigg\{ \Big[y_0^0, y_1^0, y_2^0, y_3^0\Big], \Big[y_0^1, y_1^1, y_2^1, y_3^1 \Big] \bigg\}$$

Bây giờ chúng ta muốn kết hợp hai DFT này thành một DFT cho toàn bộ vector.
Thứ tự các phần tử hiện tại là lý tưởng, và chúng ta cũng có thể thực hiện phép hợp trực tiếp trên vector này.
Chúng ta có thể lấy các phần tử $y_0^0$ and $y_0^1$ rồi thực hiện phép biến đổi hình bướm.
Vị trí của hai giá trị kết quả trùng với vị trí của hai giá trị ban đầu, vì vậy chúng ta thu được:

$$a = \bigg\{ \Big[y_0^0 + w_n^0 y_0^1, y_1^0, y_2^0, y_3^0\Big], \Big[y_0^0 - w_n^0 y_0^1, y_1^1, y_2^1, y_3^1\Big] \bigg\}$$

Tương tự, chúng ta có thể tính toán phép biến đổi hình bướm của $y_1^0$ và $y_1^1$ rồi đặt kết quả vào vị trí của chúng, và cứ tiếp tục như vậy.
Kết quả thu được là:

$$a = \bigg\{ \Big[y_0^0 + w_n^0 y_0^1, y_1^0 + w_n^1 y_1^1, y_2^0 + w_n^2 y_2^1, y_3^0 + w_n^3 y_3^1\Big], \Big[y_0^0 - w_n^0 y_0^1, y_1^0 - w_n^1 y_1^1, y_2^0 - w_n^2 y_2^1, y_3^0 - w_n^3 y_3^1\Big] \bigg\}$$

Như vậy, chúng ta đã tính được DFT mong muốn từ vector $a$.

Ở đây chúng tôi chỉ mô tả quá trình tính DFT ở tầng đệ quy đầu tiên, nhưng rõ ràng điều này cũng hoạt động tương tự cho tất cả các tầng khác.
Do đó, sau khi áp dụng hoán vị đảo bit, chúng ta có thể tính toán DFT tại chỗ mà không cần thêm bộ nhớ phụ trợ.

Điều này cũng cho phép chúng ta loại bỏ đệ quy.
Chúng ta chỉ cần bắt đầu từ tầng thấp nhất, tức là chia vector thành các cặp phần tử và áp dụng phép biến đổi hình bướm cho chúng.
Kết quả nhận được là vector $a$ đã được thực hiện tính toán của tầng cuối cùng.
Ở bước tiếp theo, chúng ta chia vector thành các khối kích thước $4$, rồi tiếp tục áp dụng phép biến đổi hình bướm, cho phép tính DFT cho mỗi khối kích thước $4$.
Và cứ tiếp tục như vậy.
Cuối cùng ở bước cuối, chúng ta thu được kết quả DFT của hai nửa của vector $a$, và bằng cách áp dụng phép biến đổi hình bướm, chúng ta thu được DFT cho toàn bộ vector $a$.

```{.cpp file=fft_implementation_iterative}
using cd = complex<double>;
const double PI = acos(-1);

int reverse(int num, int lg_n) {
    int res = 0;
    for (int i = 0; i < lg_n; i++) {
        if (num & (1 << i))
            res |= 1 << (lg_n - 1 - i);
    }
    return res;
}

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    int lg_n = 0;
    while ((1 << lg_n) < n)
        lg_n++;

    for (int i = 0; i < n; i++) {
        if (i < reverse(i, lg_n))
            swap(a[i], a[reverse(i, lg_n)]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len / 2; j++) {
                cd u = a[i+j], v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }

    if (invert) {
        for (cd & x : a)
            x /= n;
    }
}
```

Đầu tiên, chúng ta áp dụng hoán vị đảo bit bằng cách hoán đổi mỗi phần tử với phần tử ở vị trí đảo ngược của nó.
Sau đó, trong $\log n - 1$ tầng của thuật toán, chúng ta tính DFT cho mỗi khối có kích thước $\text{len}$ tương ứng.
Đối với tất cả các khối này, chúng ta có cùng một căn của đơn vị $\text{wlen}$.
Chúng ta duyệt qua tất cả các khối và thực hiện phép biến đổi hình bướm trên mỗi khối đó.

Chúng ta có thể tối ưu hóa hơn nữa việc đảo ngược các bit.
Trong cài đặt trước đó, chúng ta đã duyệt qua tất cả các bit của chỉ số để tạo chỉ số đảo ngược.
Tuy nhiên, chúng ta có thể đảo các bit theo một cách khác.

Giả sử $j$ đã chứa giá trị đảo ngược của $i$.
Khi đó, để chuyển sang $i + 1$, chúng ta phải tăng $i$ lên 1, đồng thời cũng phải tăng $j$ lên 1, nhưng trong một hệ thống số "đảo ngược".
Việc cộng 1 trong hệ nhị phân thông thường tương đương với việc chuyển tất cả các bit 1 liên tiếp ở cuối thành 0 và chuyển bit 0 ngay trước chúng thành 1.
Tương đương trong hệ thống số "đảo ngược", chúng ta sẽ đảo tất cả các bit 1 liên tiếp ở đầu, và đảo cả bit 0 tiếp theo.

Do đó, chúng ta thu được cài đặt sau:

```{.cpp file=fft_implementation_iterative_opt}
using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd> & a, bool invert) {
    int n = a.size();

    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1)
            j ^= bit;
        j ^= bit;

        if (i < j)
            swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len / 2; j++) {
                cd u = a[i+j], v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }

    if (invert) {
        for (cd & x : a)
            x /= n;
    }
}
```

Ngoài ra, chúng ta có thể tính toán trước hoán vị đảo bit.
Điều này đặc biệt hữu ích khi kích thước $n$ là giống nhau cho tất cả các lần gọi hàm.
Nhưng ngay cả khi chúng ta chỉ có ba lần gọi (cần thiết cho phép nhân hai đa thức), hiệu quả vẫn có thể nhận thấy rõ rệt.
Chúng ta cũng có thể tính toán trước tất cả các căn của đơn vị và lũy thừa của chúng.

## Biến đổi lý thuyết số (NTT)

Bây giờ chúng ta thay đổi mục tiêu một chút.
Chúng ta vẫn muốn nhân hai đa thức trong thời gian $O(n \log n)$, nhưng lần này chúng ta muốn tính toán các hệ số kết quả theo mô-đun của một số nguyên tố $p$ nào đó.
Tất nhiên đối với nhiệm vụ này, chúng ta có thể sử dụng DFT thông thường rồi áp dụng phép toán modulo cho kết quả cuối cùng.
Tuy nhiên, làm như vậy có thể dẫn đến sai số làm tròn số thực, đặc biệt là khi xử lý các số lớn.
**Biến đổi lý thuyết số (Number theoretic transform - NTT)** có ưu điểm là nó chỉ hoạt động trên số nguyên, do đó kết quả được đảm bảo chính xác tuyệt đối.

Biến đổi Fourier rời rạc dựa trên số phức và căn bậc $n$ của đơn vị.
Để tính toán nó một cách hiệu quả, chúng ta sử dụng rộng rãi các tính chất của căn (ví dụ: có một căn sinh ra tất cả các căn khác bằng cách nâng lên lũy thừa).

Nhưng các tính chất tương tự cũng được áp dụng cho căn bậc $n$ của đơn vị trong số học mô-đun.
Một căn bậc $n$ của đơn vị trong một trường hữu hạn là một số $w_n$ thỏa mãn:

$$\begin{align}
(w_n)^n &= 1 \pmod{p}, \\
(w_n)^k &\ne 1 \pmod{p}, \quad 1 \le k < n.
\end{align}$$

$n-1$ căn còn lại có thể được thu thập dưới dạng các lũy thừa của căn $w_n$.

Để áp dụng nó trong thuật toán biến đổi Fourier nhanh, chúng ta cần một căn tồn tại cho một số $n$ là lũy thừa của $2$, và cũng cho tất cả các lũy thừa nhỏ hơn.
Chúng ta có thể nhận thấy tính chất thú vị sau:

$$\begin{align}
(w_n^2)^m = w_n^n &= 1 \pmod{p}, \quad \text{với } m = \frac{n}{2}\\
(w_n^2)^k = w_n^{2k} &\ne 1 \pmod{p}, \quad 1 \le k < m.
\end{align}$$

Do đó, nếu $w_n$ là căn bậc $n$ của đơn vị thì $w_n^2$ là căn bậc $\frac{n}{2}$ của đơn vị.
Và hệ quả là đối với tất cả các lũy thừa nhỏ hơn của 2 đều tồn tại các căn của bậc yêu cầu, và chúng có thể được tính toán bằng cách sử dụng $w_n$.

Để tính DFT ngược, chúng ta cần phần tử nghịch đảo $w_n^{-1}$ của $w_n$.
Nhưng đối với mô-đun nguyên tố, phần tử nghịch đảo luôn tồn tại.

Vì vậy, tất cả các tính chất mà chúng ta cần từ các căn phức cũng có sẵn trong số học mô-đun, miễn là chúng ta có một mô-đun $p$ đủ lớn mà tại đó tồn tại căn bậc $n$ của đơn vị.

Ví dụ, chúng ta có thể chọn các giá trị sau: mô-đun $p = 7340033$, $w_{2^{20}} = 5$.
Nếu mô-đun này không đủ, chúng ta cần tìm một cặp khác.
Chúng ta có thể sử dụng thực tế là đối với các mô-đun có dạng $p = c 2^k + 1$ (với $p$ là số nguyên tố), luôn tồn tại căn bậc $2^k$ của đơn vị.
Có thể chứng minh được rằng $g^c$ chính là căn bậc $2^k$ của đơn vị như vậy, trong đó $g$ là một [căn nguyên thủy (primitive root)](primitive-root.md) của $p$.

```{.cpp file=fft_implementation_modular_arithmetic}
const int mod = 7340033;
const int root = 5;
const int root_1 = 4404020;
const int root_pw = 1 << 20;

void fft(vector<int> & a, bool invert) {
    int n = a.size();

    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1)
            j ^= bit;
        j ^= bit;

        if (i < j)
            swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        int wlen = invert ? root_1 : root;
        for (int i = len; i < root_pw; i <<= 1)
            wlen = (int)(1LL * wlen * wlen % mod);

        for (int i = 0; i < n; i += len) {
            int w = 1;
            for (int j = 0; j < len / 2; j++) {
                int u = a[i+j], v = (int)(1LL * a[i+j+len/2] * w % mod);
                a[i+j] = u + v < mod ? u + v : u + v - mod;
                a[i+j+len/2] = u - v >= 0 ? u - v : u - v + mod;
                w = (int)(1LL * w * wlen % mod);
            }
        }
    }

    if (invert) {
        int n_1 = inverse(n, mod);
        for (int & x : a)
            x = (int)(1LL * x * n_1 % mod);
    }
}
```

Ở đây, hàm `inverse` tính toán nghịch đảo mô-đun (xem bài viết về [Nghịch đảo nhân mô-đun](module-inverse.md)).
Các hằng số `mod`, `root`, `root_pw` xác định mô-đun và căn, và `root_1` là nghịch đảo của `root` theo mô-đun `mod`.

Trong thực tế, cài đặt này chậm hơn so với cài đặt sử dụng số phức (do số lượng phép toán modulo là rất lớn), nhưng nó có một số ưu điểm như sử dụng ít bộ nhớ hơn và không có sai số làm tròn số thực.

## Phép nhân với mô-đun bất kỳ

Ở đây chúng ta muốn đạt được mục tiêu tương tự như trong phần trước:
Nhân hai đa thức $A(x)$ và $B(x)$, và tính toán các hệ số kết quả theo mô-đun của một số $M$ bất kỳ nào đó.
Biến đổi lý thuyết số chỉ hoạt động cho một số số nguyên tố nhất định.
Vậy còn trường hợp mô-đun không có dạng mong muốn thì sao?

Một lựa chọn là thực hiện nhiều phép biến đổi lý thuyết số với các số nguyên tố khác nhau có dạng $c 2^k + 1$, sau đó áp dụng [Định lý thặng dư Trung Hoa (Chinese Remainder Theorem)](chinese-remainder-theorem.md) để tính toán các hệ số cuối cùng.

Một lựa chọn khác là phân tách các đa thức $A(x)$ và $B(x)$ thành hai đa thức nhỏ hơn:

$$\begin{align}
A(x) &= A_1(x) + A_2(x) \cdot C \\
B(x) &= B_1(x) + B_2(x) \cdot C
\end{align}$$

với $C \approx \sqrt{M}$.

Khi đó tích của $A(x)$ và $B(x)$ có thể được biểu diễn dưới dạng:

$$A(x) \cdot B(x) = A_1(x) \cdot B_1(x) + \left(A_1(x) \cdot B_2(x) + A_2(x) \cdot B_1(x)\right)\cdot C + \left(A_2(x) \cdot B_2(x)\right)\cdot C^2$$

Các đa thức $A_1(x)$, $A_2(x)$, $B_1(x)$ và $B_2(x)$ chỉ chứa các hệ số nhỏ hơn $\sqrt{M}$, do đó hệ số của tất cả các tích xuất hiện đều nhỏ hơn $M \cdot n$, thường là đủ nhỏ để xử lý bằng các kiểu dữ liệu dấu phẩy động thông thường.

Do đó, cách tiếp cận này yêu cầu tính tích của các đa thức với các hệ số nhỏ hơn (bằng cách sử dụng FFT thuận và FFT ngược thông thường), và sau đó tích ban đầu có thể được khôi phục bằng phép cộng và phép nhân mô-đun trong thời gian $O(n)$.

## Ứng dụng

DFT có thể được sử dụng trong rất nhiều bài toán khác, mà thoạt nhìn không liên quan gì đến phép nhân đa thức.

### Tất cả các tổng có thể

Chúng ta được cho hai mảng $a[]$ và $b[]$.
Chúng ta phải tìm tất cả các tổng có thể có $a[i] + b[j]$, và với mỗi tổng, hãy đếm tần suất xuất hiện của nó.

Ví dụ với $a = [1,~ 2,~ 3]$ và $b = [2,~ 4]$, chúng ta thu được:
tổng $3$ có thể nhận được theo $1$ cách, tổng $4$ cũng theo $1$ cách, $5$ theo $2$ cách, $6$ theo $1$ cách, $7$ theo $1$ cách.

Chúng ta dựng cho hai mảng $a$ và $b$ hai đa thức tương ứng $A$ và $B$.
Các số trong mảng sẽ đóng vai trò là số mũ trong đa thức ($a[i] \Rightarrow x^{a[i]}$); và hệ số của số hạng này sẽ là tần suất xuất hiện của số đó trong mảng.

Sau đó, bằng cách nhân hai đa thức này trong thời gian $O(n \log n)$, chúng ta thu được đa thức $C$, trong đó số mũ sẽ cho chúng ta biết tổng nào có thể nhận được, và hệ số cho biết tần suất của chúng.
Để minh họa điều này trên ví dụ:

$$(1 x^1 + 1 x^2 + 1 x^3) (1 x^2 + 1 x^4) = 1 x^3 + 1 x^4 + 2 x^5 + 1 x^6 + 1 x^7$$

### Tất cả các tích vô hướng có thể

Chúng ta được cho hai mảng $a[]$ và $b[]$ có độ dài $n$.
Chúng ta phải tính tích vô hướng của $a$ với mọi phép dịch vòng của $b$.

Chúng ta tạo ra hai mảng mới có kích thước $2n$:
Đảo ngược mảng $a$ và thêm $n$ số 0 vào sau nó.
Và chúng ta chỉ cần nhân đôi mảng $b$ bằng cách nối nó với chính nó.
Khi nhân hai mảng này như hai đa thức, và nhìn vào các hệ số $c[n-1],~ c[n],~ \dots,~ c[2n-2]$ của đa thức tích $c$, chúng ta thu được:

$$c[k] = \sum_{i+j=k} a[i] b[j]$$

Và vì tất cả các phần tử $a[i] = 0$ với mọi $i \ge n$:

$$c[k] = \sum_{i=0}^{n-1} a[i] b[k-i]$$

Dễ dàng nhận thấy rằng tổng này chính là tích vô hướng của vector $a$ với phép dịch vòng trái thứ $(k - (n - 1))$ của vector $b$.
Do đó các hệ số này chính là câu trả lời cho bài toán, và chúng ta vẫn có thể tìm được nó trong thời gian $O(n \log n)$.
Lưu ý rằng $c[2n-1]$ cũng cho chúng ta phép dịch vòng thứ $n$ nhưng phép dịch này giống hệt phép dịch thứ $0$, vì vậy chúng ta không cần phải xem xét nó riêng biệt trong kết quả của mình.

### Hai dải băng

Chúng ta được cho hai dải băng Boolean (các mảng tuần hoàn chứa các giá trị $0$ và $1$) $a$ và $b$.
Chúng ta muốn tìm tất cả các cách ghép dải băng thứ nhất vào dải băng thứ hai sao cho tại không có vị trí nào mà ô chứa số $1$ của dải băng thứ nhất nằm cạnh ô chứa số $1$ của dải băng thứ hai.

Bài toán này thực chất không khác nhiều so với bài toán trước.
Ghép hai dải băng chỉ có nghĩa là chúng ta thực hiện phép dịch vòng trên mảng thứ hai, và chúng ta có thể ghép hai dải băng nếu tích vô hướng của hai mảng này bằng $0$.

### So khớp chuỗi (String matching)

Chúng ta được cho hai chuỗi, chuỗi văn bản $T$ và chuỗi mẫu $P$, gồm các chữ cái viết thường.
Chúng ta phải tính tất cả các vị trí xuất hiện của chuỗi mẫu trong văn bản.

Chúng ta tạo một đa thức cho mỗi chuỗi ($T[i]$ và $P[I]$ là các số từ $0$ đến $25$ tương ứng với $26$ chữ cái trong bảng chữ cái):

$$A(x) = a_0 x^0 + a_1 x^1 + \dots + a_{n-1} x^{n-1}, \quad n = |T|$$

với

$$a_i = \cos(\alpha_i) + i \sin(\alpha_i), \quad \alpha_i = \frac{2 \pi T[i]}{26}.$$

Và

$$B(x) = b_0 x^0 + b_1 x^1 + \dots + b_{m-1} x^{m-1}, \quad m = |P|$$

với

$$b_i = \cos(\beta_i) - i \sin(\beta_i), \quad \beta_i = \frac{2 \pi P[m-i-1]}{26}.$$

Lưu ý rằng biểu thức $P[m-i-1]$ đảo ngược chuỗi mẫu một cách tường minh.

Các hệ số thứ $(m-1+i)$ của đa thức tích $C(x) = A(x) \cdot B(x)$ sẽ cho chúng ta biết chuỗi mẫu có xuất hiện trong văn bản tại vị trí $i$ hay không.

$$c_{m-1+i} = \sum_{j = 0}^{m-1} a_{i+j} \cdot b_{m-1-j} = \sum_{j=0}^{m-1} \left(\cos(\alpha_{i+j}) + i \sin(\alpha_{i+j})\right) \cdot \left(\cos(\beta_j) - i \sin(\beta_j)\right)$$

với $\alpha_{i+j} = \frac{2 \pi T[i+j]}{26}$ và $\beta_j = \frac{2 \pi P[j]}{26}$

Nếu có sự trùng khớp, thì $T[i+j] = P[j]$, và do đó $\alpha_{i+j} = \beta_j$.
Điều này cho ta (sử dụng đẳng thức lượng giác Pythagoras):

$$\begin{align}
c_{m-1+i} &= \sum_{j = 0}^{m-1}  \left(\cos(\alpha_{i+j}) + i \sin(\alpha_{i+j})\right) \cdot \left(\cos(\alpha_{i+j}) - i \sin(\alpha_{i+j})\right) \\
&= \sum_{j = 0}^{m-1} \cos(\alpha_{i+j})^2 + \sin(\alpha_{i+j})^2 = \sum_{j = 0}^{m-1} 1 = m
\end{align}$$

Nếu không trùng khớp, thì ít nhất có một ký tự khác nhau, dẫn đến một trong các tích $a_{i+1} \cdot b_{m-1-j}$ không bằng $1$, khiến cho hệ số $c_{m-1+i} \ne m$.

### So khớp chuỗi với ký tự đại diện (wildcards)

Đây là một phần mở rộng của bài toán trước.
Lần này chúng ta cho phép chuỗi mẫu chứa ký tự đại diện $\*$, ký tự này có thể khớp với bất kỳ chữ cái nào.
Ví dụ, chuỗi mẫu $a*c$ xuất hiện trong văn bản $abccaacc$ tại chính xác ba vị trí, tại chỉ số $0$, chỉ số $4$ và chỉ số $5$.

Chúng ta tạo các đa thức hoàn toàn giống nhau, ngoại trừ việc đặt $b_i = 0$ nếu $P[m-i-1] = *$.
Nếu $x$ là số lượng ký tự đại diện trong $P$, thì chúng ta sẽ có sự trùng khớp của $P$ trong $T$ tại chỉ số $i$ nếu $c_{m-1+i} = m - x$.

## Bài tập luyện tập

- [SPOJ - POLYMUL](http://www.spoj.com/problems/POLYMUL/)
- [SPOJ - MAXMATCH](http://www.spoj.com/problems/MAXMATCH/)
- [SPOJ - ADAMATCH](http://www.spoj.com/problems/ADAMATCH/)
- [Codeforces - Yet Another String Matching Problem](http://codeforces.com/problemset/problem/954/I)
- [Codeforces - Lightsabers (hard)](http://codeforces.com/problemset/problem/958/F3)
- [Codeforces - Running Competition](https://codeforces.com/contest/1398/problem/G)
- [Kattis - A+B Problem](https://open.kattis.com/problems/aplusb)
- [Kattis - K-Inversions](https://open.kattis.com/problems/kinversions)
- [Codeforces - Dasha and cyclic table](http://codeforces.com/contest/754/problem/E)
- [CodeChef - Expected Number of Customers](https://www.codechef.com/COOK112A/problems/MMNN01)
- [CodeChef - Power Sum](https://www.codechef.com/SEPT19A/problems/PSUM)
- [Codeforces - Centroid Probabilities](https://codeforces.com/problemset/problem/1667/E)
