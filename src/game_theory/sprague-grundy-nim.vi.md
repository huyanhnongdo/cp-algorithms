---
tags:
  - Translated
e_maxx_link: sprague_grundy
lang: vi
---
# Định lý Sprague-Grundy. Nim

## Giới thiệu

Định lý này mô tả các trò chơi hai người chơi **công bằng (impartial)**, tức là những trò chơi mà các nước đi khả dụng và việc thắng/thua chỉ phụ thuộc vào trạng thái của trò chơi. Nói cách khác, sự khác biệt duy nhất giữa hai người chơi là ai là người đi trước.

Ngoài ra, chúng ta giả định rằng trò chơi có **thông tin hoàn hảo (perfect information)**, nghĩa là không có thông tin nào bị ẩn giấu đối với người chơi (họ biết luật chơi và các nước đi có thể).

Trò chơi được giả định là **hữu hạn**, nghĩa là sau một số nước đi nhất định, một trong những người chơi sẽ rơi vào trạng thái thua — trạng thái mà từ đó họ không thể thực hiện thêm nước đi nào nữa. Ngược lại, người chơi tạo ra trạng thái này cho đối thủ sẽ chiến thắng. Hiển nhiên là không có kết quả hòa trong trò chơi này.

Các trò chơi như vậy có thể được mô tả hoàn toàn bằng một *đồ thị có hướng không chu trình (Directed Acyclic Graph)*: các đỉnh là trạng thái trò chơi và các cạnh là các chuyển đổi (nước đi). Một đỉnh không có cạnh đi ra là một trạng thái thua (người chơi phải đi từ đỉnh này sẽ thua).

Vì không có kết quả hòa, chúng ta có thể phân loại tất cả các trạng thái trò chơi thành **trạng thái thắng** hoặc **trạng thái thua**. Trạng thái thắng là những trạng thái mà từ đó có một nước đi dẫn đến thất bại tất yếu cho đối thủ, ngay cả khi họ phản ứng tối ưu. Trạng thái thua là những trạng thái mà từ đó tất cả các nước đi đều dẫn đến trạng thái thắng cho đối thủ. Tóm lại, một trạng thái là thắng nếu tồn tại ít nhất một nước đi dẫn đến trạng thái thua, và là thua nếu không tồn tại bất kỳ nước đi nào dẫn đến trạng thái thua.

Nhiệm vụ của chúng ta là phân loại các trạng thái của một trò chơi cho trước.

Lý thuyết về các trò chơi như vậy được Roland Sprague phát triển độc lập vào năm 1935 và Patrick Michael Grundy vào năm 1939.

## Nim

Trò chơi này tuân thủ các hạn chế được mô tả ở trên. Hơn nữa, *bất kỳ* trò chơi hai người chơi công bằng với thông tin hoàn hảo nào cũng có thể quy đổi về trò chơi Nim. Việc nghiên cứu trò chơi này sẽ cho phép chúng ta giải quyết tất cả các trò chơi tương tự khác, nhưng chúng ta sẽ đề cập đến điều đó sau.

Trong lịch sử, trò chơi này phổ biến từ thời cổ đại. Nguồn gốc của nó có lẽ từ Trung Quốc — hoặc ít nhất là trò chơi *Jianshizi* rất giống với nó. Ở châu Âu, các tài liệu tham khảo sớm nhất về nó là từ thế kỷ 16. Tên gọi này được đặt bởi Charles Bouton, người đã công bố phân tích đầy đủ về trò chơi này vào năm 1901.

### Mô tả trò chơi

Có nhiều đống đá, mỗi đống có một số lượng đá nhất định. Trong một nước đi, người chơi có thể lấy bất kỳ số lượng đá dương nào từ một đống bất kỳ và bỏ chúng đi. Một người chơi thua nếu họ không thể thực hiện nước đi, điều này xảy ra khi tất cả các đống đều trống.

Trạng thái trò chơi được mô tả một cách rõ ràng bởi một đa tập hợp (multiset) các số nguyên dương. Một nước đi bao gồm việc giảm nghiêm ngặt một số nguyên được chọn (nếu nó trở thành 0, nó sẽ bị xóa khỏi tập hợp).

### Lời giải

Lời giải của Charles L. Bouton như sau:

**Định lý.**
Người chơi hiện tại có chiến lược thắng khi và chỉ khi tổng XOR (xor-sum) của các kích thước đống đá là khác không. Tổng XOR của một dãy $a$ là $a_1 \oplus a_2 \oplus \ldots \oplus  a_n$, trong đó $\oplus$ là phép toán *bitwise exclusive or*.

**Chứng minh.**
Chìa khóa của chứng minh là sự hiện diện của **chiến lược đối xứng cho đối thủ**. Chúng ta chỉ ra rằng một khi ở trong trạng thái có tổng XOR bằng 0, người chơi sẽ không thể làm cho nó khác không trong dài hạn — nếu họ chuyển sang một trạng thái có tổng XOR khác không, đối thủ sẽ luôn có nước đi đưa tổng XOR trở lại bằng 0.

Chúng ta sẽ chứng minh định lý bằng quy nạp toán học.

Đối với một trò chơi Nim trống (nơi tất cả các đống đều trống, tức là đa tập hợp rỗng), tổng XOR bằng 0 và định lý đúng.

Bây giờ giả sử chúng ta đang ở một trạng thái không trống. Sử dụng giả thiết quy nạp (và tính không chu trình của trò chơi), chúng ta giả sử rằng định lý đã được chứng minh cho tất cả các trạng thái có thể tiếp cận từ trạng thái hiện tại.

Khi đó, chứng minh chia làm hai phần:
nếu đối với vị trí hiện tại, tổng XOR $s = 0$, chúng ta phải chứng minh rằng trạng thái này là trạng thái thua, tức là tất cả các trạng thái có thể tiếp cận đều có tổng XOR $t \neq 0$. Nếu $s \neq 0$, chúng ta phải chứng minh rằng có một nước đi dẫn đến trạng thái có $t = 0$.

*   Cho $s = 0$ và xét bất kỳ nước đi nào. Nước đi này giảm kích thước của một đống $x$ xuống kích thước $y$. Sử dụng các tính chất cơ bản của $\oplus$, ta có
    
    \[ t = s \oplus x \oplus y = 0 \oplus x \oplus y = x \oplus y \]
    
    Vì $y < x$, $y \oplus x$ không thể bằng 0, nên $t \neq 0$. Nghĩa là bất kỳ trạng thái có thể tiếp cận nào cũng là trạng thái thắng (theo giả thiết quy nạp), vì vậy chúng ta đang ở vị trí thua.

*   Cho $s \neq 0$. Xét biểu diễn nhị phân của số $s$. Gọi $d$ là chỉ số của bit khác 0 cao nhất (có giá trị lớn nhất). Nước đi của chúng ta sẽ thực hiện trên một đống mà bit thứ $d$ của nó được thiết lập (phải tồn tại, nếu không bit đó sẽ không được thiết lập trong $s$). Chúng ta sẽ giảm kích thước $x$ của nó xuống $y = x \oplus s$. Tất cả các bit tại các vị trí lớn hơn $d$ trong $x$ và $y$ đều khớp nhau và bit $d$ được thiết lập trong $x$ nhưng không được thiết lập trong $y$. Do đó, $y < x$, đó là tất cả những gì chúng ta cần để một nước đi hợp lệ. Bây giờ ta có:
    
    \[ t = s \oplus x \oplus y = s \oplus x \oplus (s \oplus x) = 0 \]
    
    Điều này có nghĩa là chúng ta đã tìm thấy một trạng thái thua có thể tiếp cận (theo giả thiết quy nạp) và trạng thái hiện tại là trạng thái thắng.

**Hệ quả.**
Bất kỳ trạng thái nào của Nim cũng có thể được thay thế bằng một trạng thái tương đương miễn là tổng XOR không thay đổi. Hơn nữa, khi phân tích một trò chơi Nim với nhiều đống, chúng ta có thể thay thế nó bằng một đống duy nhất có kích thước $s$.

### Trò chơi Misère (Misère Game)

Trong **trò chơi Misère**, mục tiêu của trò chơi là ngược lại, vì vậy người chơi lấy viên đá cuối cùng sẽ thua. Hóa ra trò chơi Misère Nim có thể được chơi tối ưu gần giống như trò chơi Nim tiêu chuẩn. Ý tưởng là trước tiên hãy chơi trò chơi Misère như trò chơi tiêu chuẩn, nhưng thay đổi chiến lược ở cuối trò chơi. Chiến lược mới sẽ được áp dụng trong tình huống mà mỗi đống đá chỉ chứa tối đa một viên đá sau nước đi tiếp theo. Trong trò chơi tiêu chuẩn, chúng ta nên chọn một nước đi sau đó có một số chẵn các đống với một viên đá. Tuy nhiên, trong trò chơi Misère, chúng ta chọn một nước đi sao cho có một số lẻ các đống với một viên đá. Chiến lược này hoạt động vì một trạng thái mà chiến lược thay đổi luôn xuất hiện trong trò chơi, và trạng thái này là một trạng thái thắng, vì nó chứa chính xác một đống có nhiều hơn một viên đá nên tổng Nim không bằng 0.

## Sự tương đương giữa các trò chơi công bằng và Nim (Định lý Sprague-Grundy)

Bây giờ chúng ta sẽ học cách tìm, đối với bất kỳ trạng thái nào của bất kỳ trò chơi công bằng nào, một trạng thái Nim tương ứng.

### Bổ đề về Nim với các phép tăng

Chúng ta xem xét biến thể sau của Nim: chúng ta cũng cho phép **thêm đá vào một đống đã chọn**. Các quy tắc chính xác về việc làm thế nào và khi nào được phép tăng **không làm chúng ta quan tâm**, tuy nhiên các quy tắc phải giữ cho trò chơi của chúng ta **không có chu trình**. Trong các phần sau, các trò chơi ví dụ sẽ được xem xét.

**Bổ đề.**
Việc thêm các phép tăng vào Nim không làm thay đổi cách xác định trạng thái thắng và thua. Nói cách khác, các phép tăng là vô dụng, và chúng ta không cần phải sử dụng chúng trong một chiến lược thắng.

**Chứng minh.**
Giả sử một người chơi thêm đá vào một đống. Sau đó, đối thủ của anh ta có thể đơn giản hoàn tác nước đi của anh ta — giảm số lượng đá trở lại giá trị trước đó. Vì trò chơi không có chu trình, sớm muộn gì người chơi hiện tại cũng sẽ không thể sử dụng nước đi tăng và sẽ phải thực hiện nước đi Nim thông thường.

### Định lý Sprague-Grundy

Xét trạng thái $v$ của một trò chơi hai người chơi công bằng và gọi $v_i$ là các trạng thái có thể tiếp cận từ nó (trong đó $i \in \{ 1, 2, \dots, k \} , k \ge 0$). Với trạng thái này, chúng ta có thể gán một trò chơi Nim tương đương hoàn toàn với một đống có kích thước $x$. Số $x$ được gọi là giá trị Grundy hoặc nim-value của trạng thái $v$.

Hơn nữa, số này có thể được tìm thấy theo cách đệ quy sau:

$$ x = \text{mex}\ \{ x_1, \ldots, x_k \}, $$

trong đó $x_i$ là giá trị Grundy cho trạng thái $v_i$ và hàm $\text{mex}$ (*minimum excludant*) là số nguyên không âm nhỏ nhất không tìm thấy trong tập hợp cho trước.

Xem trò chơi như một đồ thị, chúng ta có thể tính toán dần các giá trị Grundy bắt đầu từ các đỉnh không có cạnh đi ra. Giá trị Grundy bằng 0 nghĩa là một trạng thái là trạng thái thua.

**Chứng minh.**
Chúng ta sẽ sử dụng chứng minh quy nạp.

Đối với các đỉnh không có nước đi, giá trị $x$ là $\text{mex}$ của một tập hợp rỗng, bằng 0. Điều đó là chính xác, vì một trò chơi Nim rỗng là trạng thái thua.

Bây giờ xét bất kỳ đỉnh nào khác $v$. Theo quy nạp, chúng ta giả sử các giá trị $x_i$ tương ứng với các đỉnh có thể tiếp cận của nó đã được tính toán.

Gọi $p = \text{mex}\ \{ x_1, \ldots, x_k \}$. Khi đó chúng ta biết rằng đối với bất kỳ số nguyên $i \in [0, p)$ nào cũng tồn tại một đỉnh có thể tiếp cận với giá trị Grundy $i$. Điều này có nghĩa là $v$ **tương đương với một trạng thái của trò chơi Nim với các phép tăng với một đống có kích thước $p$**. Trong trò chơi như vậy, chúng ta có các chuyển đổi đến các đống có kích thước nhỏ hơn $p$ và có thể có các chuyển đổi đến các đống có kích thước lớn hơn $p$. Do đó, $p$ thực sự là giá trị Grundy mong muốn cho trạng thái đang được xem xét.

## Ứng dụng của định lý

Cuối cùng, chúng ta mô tả một thuật toán để xác định kết quả thắng/thua của một trò chơi, có thể áp dụng cho bất kỳ trò chơi hai người chơi công bằng nào.

Để tính giá trị Grundy của một trạng thái cho trước, bạn cần:

* Lấy tất cả các nước đi có thể từ trạng thái này.

* Mỗi nước đi có thể dẫn đến một **tổng của các trò chơi độc lập** (một trò chơi trong trường hợp suy biến). Tính giá trị Grundy cho mỗi trò chơi độc lập và thực hiện XOR chúng lại với nhau. Tất nhiên, XOR không có tác dụng gì nếu chỉ có một trò chơi.

* Sau khi tính toán giá trị Grundy cho mỗi nước đi, chúng ta tìm giá trị của trạng thái là $\text{mex}$ của các con số này.

* Nếu giá trị bằng 0, thì trạng thái hiện tại là trạng thái thua, ngược lại nó là trạng thái thắng.

So với phần trước, chúng ta tính đến thực tế rằng có thể có các chuyển đổi đến các trò chơi kết hợp. Chúng ta coi chúng là một trò chơi Nim với kích thước đống bằng các giá trị Grundy của các trò chơi độc lập. Chúng ta có thể XOR chúng lại giống như Nim thông thường theo định lý của Bouton.

## Các quy luật trong giá trị Grundy

Rất thường xuyên khi giải các bài toán cụ thể bằng cách sử dụng giá trị Grundy, có thể có lợi khi **nghiên cứu bảng các giá trị** để tìm kiếm các quy luật.

Trong nhiều trò chơi, vốn có vẻ khá khó để phân tích lý thuyết, các giá trị Grundy hóa ra lại có tính chu kỳ hoặc ở dạng dễ hiểu. Trong đại đa số các trường hợp, quy luật quan sát được hóa ra là đúng và có thể được chứng minh bằng quy nạp nếu muốn.

Tuy nhiên, các giá trị Grundy không *luôn luôn* chứa những tính đều đặn như vậy và ngay cả đối với một số trò chơi rất đơn giản, bài toán đặt câu hỏi liệu những tính đều đặn đó có tồn tại hay không vẫn còn là một câu hỏi mở (ví dụ: "Grundy's game").

## Các trò chơi ví dụ

### Chữ thập (Crosses-crosses)

**Luật chơi.**
Xét một dải ô vuông có kích thước $1 \times n$. Trong một nước đi, người chơi phải đặt một dấu chữ thập, nhưng cấm đặt hai dấu chữ thập cạnh nhau (trong các ô kề nhau). Như thường lệ, người chơi không có nước đi hợp lệ sẽ thua.

**Lời giải.**
Khi một người chơi đặt dấu chữ thập vào bất kỳ ô nào, chúng ta có thể coi dải đó bị chia thành hai phần độc lập: bên trái và bên phải của dấu chữ thập. Trong trường hợp này, ô có dấu chữ thập, cũng như các ô lân cận bên trái và bên phải của nó đều bị phá hủy — không thể đặt thêm gì vào chúng nữa. Do đó, nếu chúng ta đánh số các ô từ $1$ đến $n$ thì việc đặt dấu chữ thập ở vị trí $1 < i < n$ sẽ chia dải thành hai dải có độ dài $i-2$ và $n-i-1$, tức là chúng ta chuyển sang tổng của các trò chơi $i-2$ và $n-i-1$. Đối với trường hợp đặc biệt là dấu chữ thập được đánh ở vị trí $1$ hoặc $n$, chúng ta chuyển sang trò chơi $n-2$.

Như vậy, giá trị Grundy $g(n)$ có dạng:

$$g(n) = \text{mex} \Bigl( \{ g(n-2) \} \cup \{g(i-2) \oplus g(n-i-1) \mid 2 \leq i \leq n-1\} \Bigr) .$$

Vì vậy, chúng ta đã có một lời giải $O(n^2)$.

Trên thực tế, $g(n)$ có chu kỳ độ dài 34 bắt đầu với $n=52$.

## Các bài tập thực hành

- [KATTIS S-Nim](https://open.kattis.com/problems/snim)
- [CodeForces - Marbles (2018-2019 ACM-ICPC Brazil Subregional)](https://codeforces.com/gym/101908/problem/B)
- [KATTIS - Cuboid Slicing Game](https://open.kattis.com/problems/cuboidslicinggame)
- [HackerRank - Tower Breakers, Revisited!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/tower-breakers-2)
- [HackerRank - Tower Breakers, Again!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/tower-breakers-3/problem)
- [HackerRank - Chessboard Game, Again!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/a-chessboard-game)
- [Atcoder - ABC368F - Dividing Game](https://atcoder.jp/contests/abc368/tasks/abc368_f)