---
tags:
  - Translated
e_maxx_link: z_function
lang: vi
---

# Hàm Z (Z-function) và cách tính

Giả sử chúng ta có một xâu $s$ độ dài $n$. **Hàm Z (Z-function)** của xâu này là một mảng độ dài $n$, trong đó phần tử thứ $i$ bằng số lượng ký tự lớn nhất bắt đầu từ vị trí $i$ trùng khớp với các ký tự đầu tiên của $s$.

Nói cách khác, $z[i]$ là độ dài của xâu dài nhất đồng thời là tiền tố của $s$ và tiền tố của hậu tố của $s$ bắt đầu tại $i$.

**Ghi chú.** Trong bài viết này, để tránh mơ hồ, chúng ta sử dụng chỉ số bắt đầu từ $0$; tức là: ký tự đầu tiên của $s$ có chỉ số $0$ và ký tự cuối cùng có chỉ số $n-1$.

Phần tử đầu tiên của hàm Z, $z[0]$, thường không được định nghĩa rõ ràng. Trong bài viết này, chúng ta giả định giá trị này bằng không (mặc dù điều này không làm thay đổi bất kỳ điều gì trong việc cài đặt thuật toán).

Bài viết này trình bày một thuật toán để tính hàm Z trong thời gian $O(n)$, cũng như các ứng dụng khác nhau của nó.

## Ví dụ

Ví dụ, dưới đây là các giá trị của hàm Z được tính cho các xâu khác nhau:

* "aaaaa" - $[0, 4, 3, 2, 1]$
* "aaabaab" - $[0, 2, 1, 0, 2, 1, 0]$
* "abacaba" - $[0, 0, 1, 0, 3, 0, 1]$

## Thuật toán ngây thơ

Định nghĩa chính thức có thể được biểu diễn qua cách cài đặt ngây thơ độ phức tạp $O(n^2)$ dưới đây.

```cpp
vector<int> z_function_trivial(string s) {
	int n = s.size();
	vector<int> z(n);
	for (int i = 1; i < n; i++) {
		while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
			z[i]++;
		}
	}
	return z;
}
```

Chúng ta chỉ đơn giản duyệt qua mỗi vị trí $i$ và cập nhật $z[i]$ cho từng vị trí đó, bắt đầu từ $z[i] = 0$ và tăng dần giá trị này cho đến khi gặp một ký tự không trùng khớp (hoặc khi chạm tới cuối xâu).

Tất nhiên, đây không phải là cách cài đặt hiệu quả. Dưới đây chúng ta sẽ trình bày cách xây dựng một thuật toán hiệu quả hơn.

## Thuật toán hiệu quả để tính hàm Z

Để có được thuật toán hiệu quả, chúng ta sẽ tính các giá trị $z[i]$ lần lượt từ $i = 1$ đến $n - 1$, nhưng đồng thời, khi tính một giá trị mới, chúng ta sẽ cố gắng tận dụng tối đa các giá trị đã được tính trước đó.

Để cho ngắn gọn, chúng ta gọi các xâu con trùng khớp với một tiền tố của $s$ là **đoạn trùng khớp (segment match)**. Ví dụ, giá trị của hàm Z mong muốn $z[i]$ là độ dài của đoạn trùng khớp bắt đầu tại vị trí $i$ (và kết thúc tại vị trí $i + z[i] - 1$).

Để làm được điều này, chúng ta sẽ duy trì **các chỉ số $[l, r)$ của đoạn trùng khớp nằm ngoài cùng bên phải**. Nghĩa là, trong số tất cả các đoạn trùng khớp được phát hiện, chúng ta sẽ giữ lại đoạn có vị trí kết thúc xa nhất về bên phải. Theo một cách hiểu, chỉ số $r$ có thể được xem là "biên giới" mà thuật toán đã duyệt qua trên xâu $s$; mọi thứ vượt qua điểm đó đều chưa được biết.

Khi đó, nếu chỉ số hiện tại (chỉ số mà chúng ta cần tính giá trị hàm Z tiếp theo) là $i$, chúng ta có một trong hai trường hợp:

*   $i \geq r$ — vị trí hiện tại nằm **ngoài** vùng chúng ta đã xử lý.

    Khi đó chúng ta sẽ tính $z[i]$ bằng **thuật toán ngây thơ** (tức là so sánh từng ký tự một). Lưu ý rằng sau cùng, nếu $z[i] > 0$, chúng ta sẽ phải cập nhật các chỉ số của đoạn trùng khớp ngoài cùng bên phải, vì chắc chắn giá trị biên mới $r = i + z[i]$ sẽ tốt hơn giá trị $r$ trước đó.

*   $i < r$ — vị trí hiện tại nằm bên trong đoạn trùng khớp hiện tại $[l, r)$.

    Khi đó, chúng ta có thể sử dụng các giá trị Z đã tính trước đó để "khởi tạo" giá trị cho $z[i]$ (chắc chắn sẽ tốt hơn việc "bắt đầu từ số không"), thậm chí có thể là một số lớn.

    Để làm được điều này, chúng ta nhận thấy rằng hai xâu con $s[l \dots r)$ và $s[0 \dots r-l)$ **trùng khớp nhau**. Điều này có nghĩa là để có một giá trị xấp xỉ ban đầu cho $z[i]$, chúng ta có thể lấy giá trị đã được tính cho đoạn tương ứng trong $s[0 \dots r-l)$, chính là $z[i-l]$.

    Tuy nhiên, giá trị $z[i-l]$ có thể quá lớn: khi áp dụng cho vị trí $i$, nó có thể vượt quá chỉ số $r$. Điều này không được phép vì chúng ta không biết gì về các ký tự nằm bên phải $r$: chúng có thể khác với các ký tự tương ứng trên tiền tố.

    Dưới đây là **một ví dụ** cho kịch bản này:

    $$ s = "aaaabaa" $$

    Khi đi đến vị trí cuối cùng ($i = 6$), đoạn trùng khớp hiện tại sẽ là $[5, 7)$. Vị trí $6$ khi đó sẽ tương ứng với vị trí $6 - 5 = 1$, tại đó giá trị hàm Z là $z[1] = 3$. Rõ ràng, chúng ta không thể khởi tạo $z[6]$ bằng $3$, vì như vậy sẽ hoàn toàn sai. Giá trị lớn nhất mà chúng ta có thể khởi tạo cho nó là $1$ — vì đó là giá trị lớn nhất không đưa chúng ta vượt quá chỉ số $r$ của đoạn trùng khớp $[l, r)$.

    Do đó, để **xấp xỉ ban đầu** cho $z[i]$, chúng ta có thể an tâm lấy:

    $$ z_0[i] = \min(r - i,\; z[i-l]) $$

    Sau khi khởi tạo $z[i]$ bằng $z_0[i]$, chúng ta cố gắng tăng $z[i]$ bằng cách chạy **thuật toán ngây thơ** — bởi vì nhìn chung, sau biên giới $r$, chúng ta không thể biết liệu đoạn đó có tiếp tục trùng khớp hay không.

Như vậy, toàn bộ thuật toán được chia làm hai trường hợp, chỉ khác nhau ở **giá trị ban đầu** của $z[i]$: trong trường hợp thứ nhất nó được giả định là không, trong trường hợp thứ hai nó được xác định dựa trên các giá trị đã tính trước đó (sử dụng công thức trên). Sau đó, cả hai nhánh của thuật toán này đều được đưa về việc thực hiện **thuật toán ngây thơ**, bắt đầu ngay sau khi chúng ta xác định được giá trị khởi tạo.

Thuật toán hóa ra rất đơn giản. Mặc dù ở mỗi bước lặp thuật toán ngây thơ đều được chạy, chúng ta đã đạt được cải tiến lớn, thu được một thuật toán chạy trong thời gian tuyến tính. Phần dưới đây chúng ta sẽ chứng minh thời gian chạy là tuyến tính.

## Cài đặt

Mã nguồn cài đặt thuật toán khá ngắn gọn:

```cpp
vector<int> z_function(string s) {
    int n = s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for(int i = 1; i < n; i++) {
        if(i < r) {
            z[i] = min(r - i, z[i - l]);
        }
        while(i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        if(i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}
```

### Giải thích mã nguồn

Toàn bộ giải pháp được viết dưới dạng một hàm nhận vào một xâu và trả về một mảng độ dài $n$ — chính là hàm Z của xâu $s$.

Mảng $z$ ban đầu được điền các số không. Đoạn trùng khớp ngoài cùng bên phải ban đầu được giả định là $[0; 0)$ (tức là một đoạn rỗng cố ý để không chứa bất kỳ chỉ số $i$ nào).

Bên trong vòng lặp với $i = 1 \dots n - 1$, trước tiên chúng ta xác định giá trị ban đầu $z[i]$ — nó sẽ giữ nguyên là không hoặc được tính bằng công thức trên.

Sau đó, thuật toán ngây thơ sẽ cố gắng tăng giá trị $z[i]$ nhiều nhất có thể.

Cuối cùng, nếu cần thiết (tức là khi $i + z[i] > r$), chúng ta cập nhật đoạn trùng khớp ngoài cùng bên phải $[l, r)$.

## Độ phức tạp thời gian của thuật toán

Chúng ta sẽ chứng minh thuật toán trên chạy trong thời gian tuyến tính so với độ dài của xâu — tức là $O(n)$.

Chứng minh rất đơn giản.

Chúng ta chỉ cần quan tâm đến vòng lặp `while` lồng nhau, vì tất cả các thao tác khác chỉ là các phép toán với thời gian hằng số có tổng là $O(n)$.

Chúng ta sẽ chỉ ra rằng **mỗi bước lặp** của vòng lặp `while` đều làm tăng biên phải $r$ của đoạn trùng khớp.

Để làm được điều đó, chúng ta xem xét cả hai trường hợp của thuật toán:

*   $i \geq r$

    Trong trường hợp này, hoặc vòng lặp `while` không thực hiện bước lặp nào (nếu $s[0] \ne s[i]$), hoặc nó sẽ thực hiện một vài bước lặp bắt đầu từ vị trí $i$, mỗi lần dịch chuyển một ký tự sang phải. Sau đó, biên phải $r$ chắc chắn sẽ được cập nhật.

    Như vậy chúng ta thấy rằng, khi $i \geq r$, mỗi bước lặp của vòng lặp `while` đều làm tăng giá trị của chỉ số $r$ mới.

*   $i < r$

    Trong trường hợp này, chúng ta khởi tạo $z[i]$ bằng một giá trị $z_0$ được tính từ công thức trên. Hãy so sánh giá trị ban đầu $z_0$ này với giá trị $r - i$. Chúng ta có ba trường hợp nhỏ:

      *   $z_0 < r - i$

          Chúng ta chứng minh rằng trong trường hợp này vòng lặp `while` sẽ không thực hiện bước lặp nào.

          Điều này rất dễ chứng minh bằng phản chứng: nếu vòng lặp `while` thực hiện ít nhất một bước lặp, điều đó có nghĩa là giá trị xấp xỉ ban đầu $z[i] = z_0$ là chưa chính xác (nhỏ hơn độ dài trùng khớp thực tế). Nhưng vì $s[l \dots r)$ và $s[0 \dots r-l)$ trùng nhau, điều này dẫn đến $z[i-l]$ chứa giá trị sai (nhỏ hơn giá trị thực tế của nó).

          Do đó, vì $z[i-l]$ là chính xác và nhỏ hơn $r - i$, nên giá trị này trùng khớp với giá trị $z[i]$ cần tìm.

      *   $z_0 = r - i$

          Trong trường hợp này, vòng lặp `while` có thể thực hiện một vài bước lặp, nhưng mỗi bước lặp đó sẽ dẫn đến việc tăng giá trị của chỉ số $r$, vì chúng ta bắt đầu so sánh từ ký tự $s[r]$, vốn nằm ngoài khoảng $[l, r)$.

      *   $z_0 > r - i$

          Trường hợp này không thể xảy ra theo định nghĩa của $z_0$.

Như vậy, chúng ta đã chứng minh được rằng mỗi bước lặp của vòng lặp bên trong đều làm con trỏ $r$ tiến sang phải. Vì $r$ không thể vượt quá $n-1$, điều này có nghĩa là vòng lặp bên trong không thể thực hiện quá $n-1$ bước lặp.

Vì phần còn lại của thuật toán rõ ràng chạy trong $O(n)$, chúng ta đã chứng minh được toàn bộ thuật toán tính hàm Z chạy trong thời gian tuyến tính.

## Ứng dụng

Bây giờ chúng ta sẽ xem xét một số ứng dụng của hàm Z cho các bài toán cụ thể.

Các ứng dụng này phần lớn tương tự như các ứng dụng của [hàm tiền tố (prefix function)](prefix-function.md).

### Tìm kiếm xâu con

Để tránh nhầm lẫn, chúng ta gọi $t$ là **xâu văn bản (text)**, và $p$ là **xâu mẫu (pattern)**. Bài toán đặt ra là: tìm tất cả các lần xuất hiện của mẫu $p$ bên trong văn bản $t$.

Để giải quyết bài toán này, chúng ta tạo một xâu mới $s = p + \diamond + t$, tức là nối hai xâu $p$ và $t$ lại với nhau và đặt một ký tự đặc biệt $\diamond$ ở giữa (chúng ta chọn ký tự $\diamond$ sao cho nó chắc chắn không xuất hiện trong cả $p$ và $t$).

Tính hàm Z cho xâu $s$. Khi đó, với mỗi $i$ trong đoạn $[0; \; \operatorname{length}(t) - 1]$, chúng ta xét giá trị tương ứng $k = z[i + \operatorname{length}(p) + 1]$. Nếu $k$ bằng $\operatorname{length}(p)$, ta kết luận rằng có một lần xuất hiện của $p$ tại vị trí thứ $i$ trong $t$, ngược lại thì không có lần xuất hiện nào của $p$ tại vị trí thứ $i$ trong $t$.

Thời gian chạy (và bộ nhớ tiêu thụ) là $O(\operatorname{length}(t) + \operatorname{length}(p))$.

### Số lượng xâu con phân biệt trong một xâu

Cho một xâu $s$ độ dài $n$, hãy đếm số lượng xâu con phân biệt của $s$.

Chúng ta giải quyết bài toán này một cách tuần tự. Nghĩa là: biết số lượng xâu con phân biệt hiện tại, tính lại số lượng này sau khi thêm vào cuối xâu $s$ một ký tự mới.

Gọi $k$ là số lượng xâu con phân biệt hiện tại của $s$. Chúng ta thêm một ký tự mới $c$ vào cuối $s$. Rõ ràng, có thể có một số xâu con mới kết thúc bằng ký tự $c$ mới này (cụ thể là tất cả những xâu kết thúc bằng ký tự này và chưa từng xuất hiện trước đó).

Xét xâu $t = s + c$ và đảo ngược nó (viết các ký tự theo thứ tự ngược lại). Nhiệm vụ của chúng ta bây giờ là đếm xem có bao nhiêu tiền tố của $t$ không xuất hiện ở bất kỳ nơi nào khác trong $t$. Hãy tính hàm Z của $t$ và tìm giá trị lớn nhất của nó là $z_{max}$. Rõ ràng, tiền tố độ dài $z_{max}$ của $t$ cũng xuất hiện ở đâu đó ở giữa xâu $t$. Hiển nhiên các tiền tố ngắn hơn cũng sẽ xuất hiện.

Như vậy, chúng ta tìm được số lượng xâu con mới xuất hiện khi thêm ký tự $c$ vào cuối $s$ là $\operatorname{length}(t) - z_{max}$.

Do đó, thời gian chạy của thuật toán này là $O(n^2)$ cho xâu độ dài $n$.

Lưu ý rằng bằng cách hoàn toàn tương tự, chúng ta cũng có thể cập nhật trong thời gian $O(n)$ số lượng xâu con phân biệt khi thêm một ký tự vào đầu xâu, cũng như khi xóa ký tự (ở đầu hoặc cuối xâu).

### Nén xâu

Cho một xâu $s$ độ dài $n$. Hãy tìm biểu diễn "nén" ngắn nhất của nó, tức là: tìm một xâu $t$ có độ dài ngắn nhất sao cho $s$ có thể được biểu diễn dưới dạng ghép liên tiếp của một hoặc nhiều bản sao của $t$.

Lời giải là: tính hàm Z của $s$, duyệt qua tất cả các chỉ số $i$ sao cho $i$ chia hết cho $n$. Dừng lại ở chỉ số $i$ đầu tiên thỏa mãn $i + z[i] = n$. Khi đó, xâu $s$ có thể được nén về độ dài $i$.

Chứng minh cho tính chất này hoàn toàn tương tự như lời giải sử dụng [hàm tiền tố (prefix function)](prefix-function.md).

## Bài tập thực hành

* [CSES - Finding Borders](https://cses.fi/problemset/task/1732)
* [eolymp - Blocks of string](https://www.eolymp.com/en/problems/1309)
* [Codeforces - Password [Difficulty: Easy]](http://codeforces.com/problemset/problem/126/B)
* [UVA # 455 "Periodic Strings" [Difficulty: Medium]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
* [UVA # 11022 "String Factoring" [Difficulty: Medium]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
* [UVa 11475 - Extend to Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2470)
* [LA 6439 - Pasti Pas!](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=588&page=show_problem&problem=4450)
* [Codechef - Chef and Strings](https://www.codechef.com/problems/CHSTR)
* [Codeforces - Prefixes and Suffixes](http://codeforces.com/problemset/problem/432/D)
