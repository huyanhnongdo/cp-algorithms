---
tags:
  - Translated
e_maxx_link: assignment_hungary
lang: vi
---

# Thuật toán Hungarian giải quyết bài toán phân công

## Phát biểu bài toán phân công

Có một số cách phát biểu chuẩn của bài toán phân công (tất cả chúng về mặt bản chất đều tương đương nhau). Dưới đây là một số cách phát biểu:

- Có $n$ công việc và $n$ công nhân. Mỗi công nhân yêu cầu một số tiền nhất định ứng với từng công việc cụ thể. Mỗi công nhân chỉ có thể được giao tối đa một công việc. Mục tiêu là phân công công việc cho công nhân sao cho tổng chi phí là nhỏ nhất.

- Cho một ma trận $A$ kích thước $n \times n$. Yêu cầu chọn từ mỗi hàng một số sao cho từ mỗi cột cũng chọn chính xác một số, và tổng các số được chọn là nhỏ nhất.

- Cho một ma trận $A$ kích thước $n \times n$. Yêu cầu tìm một hoán vị $p$ độ dài $n$ sao cho giá trị $\sum A[i]\left[p[i]\right]$ là nhỏ nhất.

- Xét một đồ thị hai phía đầy đủ với $n$ đỉnh mỗi bên, mỗi cạnh được gán một trọng số. Mục tiêu là tìm một bộ ghép hoàn hảo (perfect matching) có tổng trọng số là nhỏ nhất.

Lưu ý rằng tất cả các bài toán nêu trên đều là các bài toán "**vuông**" (square), nghĩa là kích thước của cả hai tập hợp đều bằng $n$. Trong thực tế, chúng ta thường gặp các bài toán tương tự dạng "**chữ nhật**" (rectangular), trong đó $n$ không bằng $m$ và yêu cầu chọn ra $\min(n, m)$ phần tử. Tuy nhiên, ta luôn có thể chuyển bài toán "chữ nhật" thành bài toán "vuông" bằng cách thêm các hàng hoặc cột có giá trị bằng 0 hoặc vô hạn tương ứng.

Chúng ta cũng lưu ý rằng tương tự như bài toán tìm lời giải **cực tiểu** (minimum), ta cũng có thể đặt bài toán tìm lời giải **cực đại** (maximum). Tuy nhiên, hai bài toán này tương đương nhau: chỉ cần nhân tất cả các trọng số với $-1$.

## Thuật toán Hungarian

### Lược sử

Thuật toán được phát triển và công bố bởi Harold **Kuhn** vào năm 1955. Kuhn đặt tên cho nó là "Hungarian" vì nó dựa trên những nghiên cứu trước đó của các nhà toán học người Hungary là Dénes Kőnig và Jenő Egerváry.<br>
Vào năm 1957, James **Munkres** đã chỉ ra rằng thuật toán này chạy trong thời gian (thực sự) đa thức, độc lập với chi phí.<br>
Do đó, trong tài liệu, thuật toán này không chỉ được gọi là "Hungarian", mà còn có tên là "Thuật toán Kuhn-Munkres" hoặc "Thuật toán Munkres".<br>
Tuy nhiên, vào năm 2006, người ta mới phát hiện ra rằng thuật toán tương tự đã được phát minh **một thế kỷ trước Kuhn** bởi nhà toán học người Đức Carl Gustav **Jacobi**. Công trình của ông, _Về việc nghiên cứu bậc của một hệ phương trình vi phân thường tùy ý_, được xuất bản sau khi ông qua đời vào năm 1890, đã chứa một thuật toán đa thức để giải quyết bài toán phân công. Đáng tiếc là vì công trình được viết bằng tiếng Latinh nên nó đã không được cộng đồng toán học chú ý.

Cũng cần lưu ý thêm rằng thuật toán ban đầu của Kuhn có độ phức tạp tiệm cận là $\mathcal{O}(n^4)$, và sau đó Jack **Edmonds** cùng Richard **Karp** (và độc lập là **Tomizawa**) đã chỉ ra cách cải tiến nó để đạt độ phức tạp tiệm cận là $\mathcal{O}(n^3)$.

### Thuật toán $\mathcal{O}(n^4)$

Để tránh nhầm lẫn, chúng ta lưu ý ngay rằng chúng ta chủ yếu quan tâm đến bài toán phân công dưới dạng ma trận (tức là cho ma trận $A$, bạn cần chọn $n$ ô từ ma trận sao cho chúng nằm trên các hàng và cột khác nhau). Chúng ta đánh số các mảng bắt đầu từ $1$, ví dụ, ma trận $A$ có chỉ số từ $A[1 \dots n][1 \dots n]$.

Chúng ta cũng giả định rằng tất cả các số trong ma trận $A$ đều **không âm** (nếu không, ta luôn có thể cộng thêm một hằng số vào tất cả các số của ma trận để đưa nó về dạng không âm).

Chúng ta gọi hai mảng số $u[1 \ldots n]$ và $v[1 \dots n]$ là một **thế hiệu** (potential) nếu chúng thỏa mãn điều kiện sau:

$$u[i]+v[j]\leq A[i][j],\quad i=1\dots n,\ j=1\dots n$$

(Như bạn thấy, $u[i]$ tương ứng với hàng thứ $i$, và $v[j]$ tương ứng với cột thứ $j$ của ma trận).

Chúng ta gọi **giá trị $f$ của thế hiệu** là tổng các phần tử của nó:

$$f=\sum_{i=1}^{n} u[i] + \sum_{j=1}^{n} v[j].$$

Một mặt, dễ thấy rằng chi phí của lời giải $sol$ cần tìm **không nhỏ hơn** giá trị của bất kỳ thế hiệu nào.

!!! info ""

    **Bổ đề.** $sol\geq f.$

??? info "Chứng minh"

    Lời giải cần tìm của bài toán gồm $n$ ô của ma trận $A$, do đó $u[i]+v[j]\leq A[i][j]$ với mỗi ô trong số chúng. Vì tất cả các phần tử trong $sol$ nằm ở các hàng và cột khác nhau, cộng các bất đẳng thức này lại cho tất cả các $A[i][j]$ được chọn, ta thu được $f$ ở vế trái và $sol$ ở vế phải của bất đẳng thức.

Mặt khác, người ta chứng minh được rằng luôn tồn tại một lời giải và một thế hiệu biến bất đẳng thức này thành **đẳng thức**. Thuật toán Hungarian được mô tả dưới đây sẽ là một chứng minh mang tính dựng hình cho thực tế này. Hiện tại, chúng ta chỉ cần chú ý rằng nếu bất kỳ lời giải nào có chi phí bằng giá trị của một thế hiệu nào đó, thì lời giải đó là **tối ưu**.

Hãy cố định một thế hiệu. Chúng ta gọi một cạnh $(i,j)$ là **căng** (rigid) nếu $u[i]+v[j]=A[i][j].$

Hãy nhớ lại một cách phát biểu khác của bài toán phân công sử dụng đồ thị hai phía. Ký hiệu $H$ là đồ thị hai phía chỉ gồm các cạnh căng. Thuật toán Hungarian sẽ duy trì, ứng với thế hiệu hiện tại, **một bộ ghép có số lượng cạnh lớn nhất** $M$ trên đồ thị $H$. Ngay khi $M$ chứa đủ $n$ cạnh, thì lời giải của bài toán chính là $M$ (vì đó sẽ là lời giải có chi phí trùng với giá trị của thế hiệu).

Chúng ta đi trực tiếp vào **mô tả thuật toán**.

**Bước 1.** Ban đầu thế hiệu được giả định bằng 0 ($u[i]=v[i]=0$ với mọi $i$), và bộ ghép $M$ được giả định là rỗng.

**Bước 2.** Tiếp theo, tại mỗi bước của thuật toán, chúng ta cố gắng tăng kích thước của bộ ghép $M$ hiện tại thêm 1 mà không làm thay đổi thế hiệu (lưu ý rằng bộ ghép được tìm trên đồ thị của các cạnh căng $H$). Để làm việc này, chúng ta sử dụng [Thuật toán Kuhn tìm bộ ghép cực đại trên đồ thị hai phía](kuhn_maximum_bipartite_matching.md) thông thường. Hãy nhắc lại thuật toán ở đây:
Tất cả các cạnh thuộc bộ ghép $M$ được định hướng từ phần bên phải sang phần bên trái, và tất cả các cạnh khác của đồ thị $H$ được định hướng theo chiều ngược lại.

Nhắc lại (từ thuật ngữ tìm bộ ghép) rằng một đỉnh được gọi là bão hòa nếu có một cạnh thuộc bộ ghép hiện tại liên thuộc với nó. Một đỉnh không liên thuộc với cạnh nào của bộ ghép hiện tại được gọi là chưa bão hòa. Một đường đi có độ dài lẻ, có cạnh đầu tiên không thuộc bộ ghép, và các cạnh tiếp theo xen kẽ thuộc/không thuộc bộ ghép - được gọi là một đường tăng.
Từ tất cả các đỉnh chưa bão hòa ở phần bên trái, chúng ta bắt đầu duyệt [theo chiều sâu](depth-first-search.md) hoặc [theo chiều rộng](breadth-first-search.md). Nếu kết quả phép duyệt có thể đi tới một đỉnh chưa bão hòa ở phần bên phải, chúng ta tìm được một đường tăng từ phần bên trái sang phần bên phải. Nếu chúng ta đưa các cạnh lẻ trên đường đi vào bộ ghép và loại bỏ các cạnh chẵn khỏi bộ ghép (tức là thêm cạnh thứ nhất, loại bỏ cạnh thứ hai, thêm cạnh thứ ba, v.v.), thì chúng ta sẽ tăng kích thước bộ ghép thêm 1.

Nếu không tồn tại đường tăng nào, thì bộ ghép $M$ hiện tại là cực đại trên đồ thị $H$.

**Bước 3.** Nếu tại bước hiện tại, không thể tăng kích thước của bộ ghép hiện tại, thì chúng ta tiến hành tính toán lại thế hiệu sao cho ở các bước tiếp theo, có nhiều cơ hội hơn để tăng bộ ghép.

Ký hiệu $Z_1$ là tập hợp các đỉnh ở phần bên trái được ghé thăm trong lượt duyệt cuối của thuật toán Kuhn, và $Z_2$ là tập hợp các đỉnh được ghé thăm ở phần bên phải.

Hãy tính giá trị $\Delta$:

$$\Delta = \min_{i\in Z_1,\ j\notin Z_2} A[i][j]-u[i]-v[j].$$

!!! info ""

     **Bổ đề.** $\Delta > 0.$

??? info "Chứng minh"

    Giả sử $\Delta=0$. Khi đó tồn tại một cạnh căng $(i,j)$ với $i\in Z_1$ và $j\notin Z_2$. Suy ra cạnh $(i,j)$ phải được định hướng từ phần bên phải sang phần bên trái, nghĩa là $(i,j)$ phải thuộc bộ ghép $M$. Tuy nhiên, điều này là bất khả thi, vì chúng ta không thể đi tới đỉnh bão hòa $i$ trừ khi đi dọc theo cạnh từ j sang i. Do đó $\Delta > 0$.

Bây giờ chúng ta **tính lại thế hiệu** như sau:

- với tất cả các đỉnh $i\in Z_1$, thực hiện $u[i] \gets u[i]+\Delta$,

- với tất cả các đỉnh $j\in Z_2$, thực hiện $v[j] \gets v[j]-\Delta$.

!!! info ""

    **Bổ đề.** Thế hiệu thu được vẫn là một thế hiệu hợp lệ.

??? info "Chứng minh"

    Chúng ta sẽ chỉ ra rằng, sau khi tính toán lại, ta vẫn có $u[i]+v[j]\leq A[i][j]$ với mọi $i,j$. Với tất cả các phần tử của $A$ có $i\in Z_1$ và $j\in Z_2$, tổng $u[i]+v[j]$ không thay đổi, nên bất đẳng thức giữ nguyên. Với tất cả các phần tử có $i\notin Z_1$ and $j\in Z_2$, tổng $u[i]+v[j]$ giảm đi $\Delta$, nên bất đẳng thức vẫn đúng. Với các phần tử còn lại có $i\in Z_1$ and $j\notin Z_2$, tổng tăng lên, nhưng bất đẳng thức vẫn được bảo toàn vì giá trị $\Delta$ theo định nghĩa là mức tăng tối đa để bất đẳng thức không bị vi phạm.

!!! info ""

    **Bổ đề.** Bộ ghép cũ $M$ gồm các cạnh căng vẫn hợp lệ, nghĩa là tất cả các cạnh trong bộ ghép vẫn là cạnh căng.

??? info "Chứng minh"

    Để một cạnh căng $(i,j)$ không còn căng sau khi thay đổi thế hiệu, đẳng thức $u[i] + v[j] = A[i][j]$ phải trở thành bất đẳng thức $u[i] + v[j] < A[i][j]$. Tuy nhiên, điều này chỉ có thể xảy ra khi $i \notin Z_1$ và $j \in Z_2$. Nhưng $i \notin Z_1$ ngụ ý rằng cạnh $(i,j)$ không thể là một cạnh thuộc bộ ghép.

!!! info ""

    **Bổ đề.** Sau mỗi lần tính lại thế hiệu, số lượng đỉnh có thể đi tới được bởi phép duyệt, tức là $|Z_1|+|Z_2|$, tăng lên rõ rệt.

??? info "Chứng minh"

    Đầu tiên, lưu ý rằng bất kỳ đỉnh nào đi tới được trước khi tính lại thế hiệu thì vẫn đi tới được sau đó. Thật vậy, nếu một đỉnh đi tới được, thì tồn tại một đường đi từ các đỉnh đi tới được đến nó, xuất phát từ đỉnh chưa bão hòa của phần bên trái; vì với các cạnh dạng $(i,j),\ i\in Z_1,\ j\in Z_2$ tổng $u[i]+v[j]$ không thay đổi, toàn bộ đường đi này sẽ được bảo toàn sau khi thay đổi thế hiệu.
    Thứ hai, chúng ta chỉ ra rằng sau khi tính lại thế hiệu, có ít nhất một đỉnh mới sẽ đi tới được. Điều này suy ra từ định nghĩa của $\Delta$: cạnh $(i,j)$ tương ứng với $\Delta$ sẽ trở thành cạnh căng, do đó đỉnh $j$ sẽ đi tới được từ đỉnh $i$.

Nhờ bổ đề cuối cùng, **không quá $n$ lần tính lại thế hiệu có thể xảy ra** trước khi tìm được một đường tăng và kích thước bộ ghép $M$ được tăng lên.
Do đó, sớm muộn gì chúng ta cũng tìm được thế hiệu tương ứng với bộ ghép hoàn hảo $M^*$, và $M^*$ chính là kết quả cần tìm của bài toán.
Nếu bàn về độ phức tạp của thuật toán, nó sẽ là $\mathcal{O}(n^4)$: tổng cộng có tối đa $n$ lần tăng bộ ghép, trước mỗi lần tăng có tối đa $n$ lần tính lại thế hiệu, mỗi lần tính lại được thực hiện trong thời gian $\mathcal{O}(n^2)$.

Chúng ta sẽ không đưa ra cài đặt cho thuật toán $\mathcal{O}(n^4)$ ở đây, vì nó không ngắn hơn cài đặt cho thuật toán $\mathcal{O}(n^3)$ được mô tả dưới đây.

### Thuật toán $\mathcal{O}(n^3)$

Bây giờ chúng ta sẽ học cách cài đặt thuật toán này trong thời gian $\mathcal{O}(n^3)$ (đối với bài toán chữ nhật kích thước $n \times m$, độ phức tạp là $\mathcal{O}(n^2m)$).

Ý tưởng chính là **xét lần lượt từng hàng của ma trận**, thay vì xét tất cả cùng một lúc. Do đó, thuật toán mô tả ở trên sẽ có dạng như sau:

1. Xét hàng tiếp theo của ma trận $A$.

2. Chừng nào chưa có đường tăng xuất phát từ hàng này, thực hiện tính toán lại thế hiệu.

3. Ngay khi tìm thấy đường tăng, cập nhật bộ ghép dọc theo nó (đưa cạnh cuối vào bộ ghép), rồi quay lại bước 1 (để xét hàng tiếp theo).

Để đạt được độ phức tạp mong muốn, chúng ta cần cài đặt bước 2-3 (được thực hiện cho mỗi hàng của ma trận) trong thời gian $\mathcal{O}(n^2)$ (đối với bài toán chữ nhật là $\mathcal{O}(nm)$).

Để làm việc này, hãy nhớ lại hai sự thật đã được chứng minh ở trên:

- Khi thế hiệu thay đổi, các đỉnh đi tới được bởi thuật toán Kuhn vẫn sẽ tiếp tục đi tới được.

- Tổng cộng chỉ có tối đa $\mathcal{O}(n)$ lần tính lại thế hiệu xảy ra trước khi tìm được đường tăng.

Từ đó suy ra các **ý tưởng chính** giúp chúng ta đạt được độ phức tạp mong muốn:

- Để kiểm tra sự tồn tại của đường tăng, không cần thiết phải khởi chạy lại thuật toán duyệt Kuhn từ đầu sau mỗi lần tính lại thế hiệu. Thay vào đó, bạn có thể thực hiện thuật toán Kuhn dưới dạng **lặp**: sau mỗi lần tính lại thế hiệu, hãy xem xét các cạnh căng mới được thêm vào và nếu đỉnh bên trái của chúng đi tới được, ta đánh dấu đỉnh bên phải cũng đi tới được và tiếp tục phép duyệt từ chúng.

- Phát triển ý tưởng này xa hơn, chúng ta có thể trình bày thuật toán như sau: ở mỗi bước của vòng lặp, thế hiệu được tính lại. Sau đó, một cột mới đi tới được sẽ được xác định (cột này luôn tồn tại vì các đỉnh đi tới được mới sẽ xuất hiện sau mỗi lần tính lại thế hiệu). Nếu cột này chưa bão hòa, ta tìm được một đường tăng. Ngược lại, nếu cột này đã bão hòa, hàng tương ứng trong bộ ghép cũng trở thành đi tới được.

- Để nhanh chóng tính lại thế hiệu (nhanh hơn phiên bản ngây thơ $\mathcal{O}(n^2)$), bạn cần duy trì các giá trị cực tiểu phụ cho mỗi cột:

    <br><div style="text-align:center">$minv[j]=\min_{i\in Z_1} A[i][j]-u[i]-v[j].$</div><br>

    Dễ thấy rằng giá trị $\Delta$ cần tìm được biểu diễn qua chúng như sau:

    <br><div style="text-align:center">$\Delta=\min_{j\notin Z_2} minv[j].$</div><br>

    Do đó, việc tìm $\Delta$ hiện có thể được thực hiện trong thời gian $\mathcal{O}(n)$.

    Chúng ta cần cập nhật mảng $minv$ khi các hàng mới được ghé thăm xuất hiện. Việc này có thể được thực hiện trong $O(n)$ cho hàng mới được thêm vào (tổng cộng trên tất cả các hàng là $\mathcal{O}(n^2)$). Chúng ta cũng cần cập nhật mảng $minv$ khi tính lại thế hiệu, việc này cũng mất thời gian $\mathcal{O}(n)$ (mảng $minv$ chỉ thay đổi đối với các cột chưa đi tới được: cụ thể là nó giảm đi một lượng $\Delta$).

Như vậy, thuật toán có cấu trúc như sau: trong vòng lặp ngoài, chúng ta xét lần lượt từng hàng của ma trận. Mỗi hàng được xử lý trong thời gian $\mathcal{O}(n^2)$, vì chỉ có tối đa $\mathcal{O}(n)$ lần tính lại thế hiệu xảy ra (mỗi lần mất $\mathcal{O}(n)$), và mảng $minv$ được duy trì trong thời gian $\mathcal{O}(n^2)$; thuật toán Kuhn hoạt động trong thời gian $\mathcal{O}(n^2)$ (vì nó được biểu diễn dưới dạng $\mathcal{O}(n)$ bước lặp, mỗi bước lặp ghé thăm một cột mới).

Độ phức tạp tổng thể thu được là $\mathcal{O}(n^3)$ hoặc nếu là bài toán chữ nhật thì là $\mathcal{O}(n^2m)$.

## Cài đặt thuật toán Hungarian

Cài đặt dưới đây được phát triển bởi **Andrey Lopatin** vài năm trước. Nó nổi bật bởi sự ngắn gọn đáng kinh ngạc: toàn bộ thuật toán chỉ gồm **30 dòng mã**.

Cài đặt tìm lời giải cho ma trận chữ nhật $A[1\dots n][1\dots m]$, với $n\leq m$. Ma trận sử dụng chỉ số từ 1 để thuận tiện và ngắn gọn: cài đặt này thêm một hàng số 0 và cột số 0 giả, giúp viết nhiều vòng lặp dưới dạng tổng quát mà không cần kiểm tra thêm.

Các mảng $u[0 \ldots n]$ và $v[0 \ldots m]$ lưu trữ thế hiệu. Ban đầu chúng được đặt bằng 0, tương ứng với ma trận có các hàng bằng 0 (Lưu ý rằng đối với cài đặt này, việc ma trận $A$ chứa các số âm hay không là không quan trọng).

Mảng $p[0 \ldots m]$ chứa bộ ghép: với mỗi cột $j = 1 \dots m$, nó lưu số hiệu $p[j]$ của hàng được ghép (hoặc $0$ nếu cột đó chưa được ghép). Để tiện cài đặt, $p[0]$ được giả định bằng chỉ số của hàng hiện tại.

Mảng $minv[1 \ldots m]$ chứa các giá trị cực tiểu phụ cần thiết cho mỗi cột $j$ để tính nhanh lại thế hiệu như đã mô tả ở trên.

Mảng $way[1 \ldots m]$ chứa thông tin về nơi đạt được các giá trị cực tiểu này để chúng ta có thể khôi phục lại đường tăng sau đó. Lưu ý rằng để khôi phục đường đi, ta chỉ cần lưu chỉ số cột là đủ, vì chỉ số hàng có thể lấy từ bộ ghép (tức là từ mảng $p$). Do đó, $way[j]$ với mỗi cột $j$ chứa chỉ số của cột liền trước trên đường đi (hoặc $0$ nếu không có).

Bản thân thuật toán là một **vòng lặp ngoài qua các hàng của ma trận**, bên trong đó hàng thứ $i$ được xét. Vòng lặp thứ nhất _do-while_ chạy cho đến khi tìm thấy một cột tự do $j0$. Mỗi bước lặp của vòng lặp đánh dấu ghé thăm một cột mới có chỉ số $j0$ (được tính ở bước lặp trước; ban đầu bằng 0 - tức là ta bắt đầu từ cột giả), cũng như hàng mới $i0$ kề với nó trong bộ ghép (tức là $p[j0]$; ban đầu khi $j0=0$ thì lấy hàng thứ $i$). Do sự xuất hiện của hàng mới $i0$ được ghé thăm, bạn cần cập nhật lại mảng $minv$ và giá trị $\Delta$ tương ứng. Nếu $\Delta$ được cập nhật, cột $j1$ sẽ trở thành cột đạt giá trị cực tiểu mới (lưu ý rằng với cài đặt này, $\Delta$ có thể bằng 0, nghĩa là thế hiệu không thay đổi ở bước hiện tại: đã có sẵn một cột mới đi tới được). Sau đó, thế hiệu và mảng $minv$ được tính lại. Khi kết thúc vòng lặp "do-while", chúng ta tìm thấy một đường tăng kết thúc ở cột $j0$ và có thể "mở rộng" nó ngược lại bằng mảng cha $way$.

Hằng số `INF` là giá trị "vô cùng", tức là một số chắc chắn lớn hơn tất cả các số có thể có trong ma trận đầu vào $A$.

```{.cpp file=hungarian}
vector<int> u (n+1), v (m+1), p (m+1), way (m+1);
for (int i=1; i<=n; ++i) {
    p[0] = i;
    int j0 = 0;
    vector<int> minv (m+1, INF);
    vector<bool> used (m+1, false);
    do {
        used[j0] = true;
        int i0 = p[j0],  delta = INF,  j1;
        for (int j=1; j<=m; ++j)
            if (!used[j]) {
                int cur = A[i0][j]-u[i0]-v[j];
                if (cur < minv[j])
                    minv[j] = cur,  way[j] = j0;
                if (minv[j] < delta)
                    delta = minv[j],  j1 = j;
            }
        for (int j=0; j<=m; ++j)
            if (used[j])
                u[p[j]] += delta,  v[j] -= delta;
            else
                minv[j] -= delta;
        j0 = j1;
    } while (p[j0] != 0);
    do {
        int j1 = way[j0];
        p[j0] = p[j1];
        j0 = j1;
    } while (j0);
}
```

Để khôi phục kết quả dưới dạng quen thuộc hơn, tức là tìm với mỗi hàng $i = 1 \dots n$ chỉ số $ans[i]$ của cột được chọn, ta có thể làm như sau:

```cpp
vector<int> ans (n+1);
for (int j=1; j<=m; ++j)
    ans[p[j]] = j;
```

Chi phí của bộ ghép đơn giản là thế hiệu của cột 0 (lấy với dấu ngược lại). Thật vậy, như bạn thấy từ mã nguồn, $-v[0]$ chứa tổng của tất cả các giá trị $\Delta$, tức là tổng lượng thay đổi của thế hiệu. Mặc dù nhiều giá trị $u[i]$ và $v[j]$ có thể thay đổi cùng lúc, tổng thay đổi của thế hiệu chính xác bằng $\Delta$, vì chừng nào chưa có đường tăng, số lượng hàng đi tới được luôn nhiều hơn số lượng cột đi tới được đúng một hàng (chỉ có hàng $i$ hiện tại là không có "cặp" dưới dạng cột đã ghé thăm):

```cpp
int cost = -v[0];
```

## Mối liên hệ với Thuật toán đường đi ngắn nhất tăng dần

Thuật toán Hungarian có thể được xem như là [Thuật toán đường đi ngắn nhất tăng dần (Successive Shortest Path Algorithm)](min_cost_flow.md) được điều chỉnh riêng cho bài toán phân công. Không đi sâu vào chi tiết, dưới đây giới thiệu một số trực giác về mối liên hệ giữa chúng.

Thuật toán đường đi ngắn nhất tăng dần sử dụng một phiên bản sửa đổi của thuật toán Johnson làm kỹ thuật gán lại trọng số. Kỹ thuật này gồm bốn bước:

- Sử dụng thuật toán [Bellman-Ford](bellman_ford.md), xuất phát từ nguồn $s$ và với mỗi nút, tìm đường đi có trọng số nhỏ nhất $h(v)$ từ $s$ đến $v$.

Với mỗi bước của thuật toán chính:

- Gán lại trọng số các cạnh của đồ thị ban đầu theo công thức: $w(u,v) \gets w(u,v)+h(u)-h(v)$.
- Sử dụng thuật toán [Dijkstra](dijkstra.md) để tìm đồ thị con của các đường đi ngắn nhất trên mạng ban đầu.
- Cập nhật thế hiệu cho bước lặp tiếp theo.

Từ mô tả này, ta có thể thấy một sự tương đồng mạnh mẽ giữa $h(v)$ và thế hiệu: có thể kiểm tra thấy chúng bằng nhau sai khác một hằng số dịch chuyển. Ngoài ra, người ta chứng minh được rằng sau khi gán lại trọng số, tập hợp tất cả các cạnh có trọng số bằng 0 đại diện cho đồ thị con đường đi ngắn nhất nơi thuật toán chính cố gắng tăng luồng. Điều này cũng xảy ra trong thuật toán Hungarian: chúng ta tạo một đồ thị con gồm các cạnh căng (các cạnh có lượng $A[i][j]-u[i]-v[j]$ bằng 0), và cố gắng tăng kích thước của bộ ghép.

Trong bước 4, tất cả các giá trị $h(v)$ được cập nhật: mỗi khi chúng ta thay đổi mạng luồng, chúng ta phải đảm bảo khoảng cách từ nguồn là chính xác (nếu không, ở bước lặp tiếp theo, thuật toán Dijkstra có thể thất bại). Điều này tương tự như việc cập nhật được thực hiện trên thế hiệu, nhưng trong trường hợp này, chúng không được tăng đều nhau.

Để hiểu sâu hơn về thế hiệu, vui lòng tham khảo [bài viết này](https://codeforces.com/blog/entry/105658).

## Ví dụ bài toán

Dưới đây là một số ví dụ liên quan đến bài toán phân công, từ rất cơ bản đến phức tạp hơn:

- Cho một đồ thị hai phía, yêu cầu tìm trong đó **bộ ghép cực đại có trọng số nhỏ nhất** (tức là trước hết kích thước bộ ghép phải là lớn nhất, và sau đó chi phí của nó phải là nhỏ nhất).<br>
  Để giải quyết, chúng ta chỉ cần xây dựng một bài toán phân công, đặt giá trị "vô cùng" vào vị trí các cạnh thiếu. Sau đó, giải bài toán bằng thuật toán Hungarian, và loại bỏ các cạnh có trọng số vô hạn khỏi kết quả (chúng có thể xuất hiện trong kết quả nếu đồ thị không có bộ ghép hoàn hảo).

- Cho một đồ thị hai phía, yêu cầu tìm trong đó **bộ ghép cực đại có trọng số lớn nhất**.<br>
  Giải pháp tương tự như trên, chỉ cần nhân tất cả các trọng số với $-1$.

- Bài toán **nhận dạng vật thể chuyển động trong ảnh**: có hai bức ảnh được chụp, kết quả thu được hai tập hợp tọa độ. Yêu cầu liên kết các vật thể trong bức ảnh thứ nhất và thứ hai, tức là xác định với mỗi điểm của bức ảnh thứ hai, điểm nào của bức ảnh thứ nhất tương ứng với nó. Trong trường hợp này, yêu cầu là cực tiểu hóa tổng khoảng cách giữa các điểm được so sánh (nghĩa là chúng ta tìm một giải pháp mà các vật thể dịch chuyển với tổng quãng đường ngắn nhất).<br>
  Để giải quyết, chúng ta xây dựng và giải bài toán phân công với trọng số của các cạnh là khoảng cách Euclid giữa các điểm.

- Bài toán **nhận dạng vật thể chuyển động bằng định vị**: có hai máy định vị không thể xác định vị trí của vật thể trong không gian mà chỉ xác định được hướng của nó. Cả hai máy định vị (nằm ở các vị trí khác nhau) nhận được thông tin dưới dạng $n$ hướng như vậy. Yêu cầu xác định vị trí của các vật thể, tức là xác định vị trí mong đợi của các vật thể và các cặp hướng tương ứng của chúng sao cho tổng khoảng cách từ các vật thể đến các tia hướng là nhỏ nhất.<br>
  Giải pháp: một lần nữa, chúng ta xây dựng và giải bài toán phân công, trong đó các đỉnh của phần bên trái là $n$ hướng từ máy định vị thứ nhất, các đỉnh của phần bên phải là $n$ hướng từ máy định vị thứ hai, và trọng số của các cạnh là khoảng cách giữa các tia tương ứng.

- Phủ một **đồ thị có hướng không chu trình bằng các đường đi**: cho một đồ thị có hướng không chu trình, yêu cầu tìm số lượng đường đi nhỏ nhất (nếu bằng nhau thì có tổng trọng số nhỏ nhất) sao cho mỗi đỉnh của đồ thị nằm trên đúng một đường đi.<br>
  Giải pháp là xây dựng đồ thị hai phía tương ứng từ đồ thị đã cho và tìm bộ ghép cực đại có trọng số nhỏ nhất trên đó. Xem bài viết riêng để biết thêm chi tiết.

- **Tô màu cây**. Cho một cây trong đó mỗi đỉnh, ngoại trừ các lá, có chính xác $k-1$ con. Yêu cầu chọn cho mỗi đỉnh một trong $k$ màu có sẵn sao cho không có hai đỉnh kề nhau nào có cùng màu. Ngoài ra, với mỗi đỉnh và mỗi màu, chi phí tô đỉnh đó bằng màu đó đã được biết trước, và yêu cầu là cực tiểu hóa tổng chi phí.<br>
  Để giải quyết bài toán này, chúng ta sử dụng quy hoạch động. Cụ thể, hãy học cách tính giá trị $d[v][c]$, trong đó $v$ là số hiệu đỉnh, $c$ là số hiệu màu, và bản thân giá trị $d[v][c]$ là chi phí tối thiểu cần thiết để tô màu tất cả các đỉnh trong cây con có gốc tại $v$, và bản thân đỉnh $v$ được tô màu $c$. Để tính giá trị $d[v][c]$ như vậy, cần phân phối $k-1$ màu còn lại cho các con của đỉnh $v$, và để làm việc này, ta cần xây dựng và giải bài toán phân công (trong đó các đỉnh của phần bên trái là các màu, các đỉnh của phần bên phải là các con, và trọng số của các cạnh là các giá trị $d$ tương ứng).<br>
  Như vậy, mỗi giá trị $d[v][c]$ được tính bằng cách giải một bài toán phân công, cuối cùng cho độ phức tạp tiệm cận là $\mathcal{O}(nk^4)$.

- Nếu trong bài toán phân công, trọng số không nằm trên các cạnh mà nằm trên các đỉnh, và chỉ nằm **trên các đỉnh của cùng một phần**, thì không cần thiết phải sử dụng thuật toán Hungarian: chỉ cần sắp xếp các đỉnh theo trọng số và chạy thuật toán [Kuhn](kuhn_maximum_bipartite_matching.md) thông thường (để biết thêm chi tiết, xem [bài viết riêng](http://e-maxx.ru/algo/vertex_weighted_matching)).

- Xét **trường hợp đặc biệt** sau. Cho mỗi đỉnh của phần bên trái được gán một số $\alpha[i]$, và mỗi đỉnh của phần bên phải một số $\beta[j]$. Cho trọng số của cạnh $(i,j)$ bất kỳ bằng $\alpha[i]\cdot \beta[j]$ (các số $\alpha[i]$ và $\beta[j]$ đã biết). Hãy giải bài toán phân công.<br>
  Để giải quyết mà không cần thuật toán Hungarian, trước tiên chúng ta xét trường hợp cả hai phần đều có hai đỉnh. Trong trường hợp này, như bạn có thể dễ dàng thấy, tốt nhất là kết nối các đỉnh theo thứ tự ngược lại: kết nối đỉnh có $\alpha[i]$ nhỏ hơn với đỉnh có $\beta[j]$ lớn hơn. Quy tắc này có thể dễ dàng tổng quát hóa cho số lượng đỉnh tùy ý: bạn cần sắp xếp các đỉnh của phần thứ nhất theo thứ tự tăng dần của các giá trị $\alpha[i]$, phần thứ hai theo thứ tự giảm dần của các giá trị $\beta[j]$, và kết nối các đỉnh theo từng cặp theo thứ tự đó. Như vậy, chúng ta có được một giải pháp với độ phức tạp $\mathcal{O}(n\log n)$.

- **Bài toán thế hiệu**. Cho một ma trận $A[1 \ldots n][1 \ldots m]$, yêu cầu tìm hai mảng $u[1 \ldots n]$ và $v[1 \dots m]$ sao cho với mọi $i$ và $j$, $u[i] + v[j] \leq a[i][j]$ và tổng các phần tử của mảng $u$ và $v$ đạt cực đại.<br>
  Khi đã biết thuật toán Hungarian, việc giải bài toán này không hề khó khăn: thuật toán Hungarian chính xác là tìm một thế hiệu $u, v$ thỏa mãn điều kiện của bài toán. Mặt khác, nếu không có kiến thức về thuật toán Hungarian, việc giải quyết bài toán này dường như là bất khả thi.

    !!! info "Lưu ý"

        Bài toán này còn được gọi là **bài toán đối ngẫu** của bài toán phân công: cực tiểu hóa tổng chi phí của phân công tương đương với cực đại hóa tổng các thế hiệu.

## Tài liệu tham khảo

- [Ravindra Ahuja, Thomas Magnanti, James Orlin. Network Flows [1993]](https://books.google.it/books/about/Network_Flows.html?id=rFuLngEACAAJ&redir_esc=y)

- [Harold Kuhn. The Hungarian Method for the Assignment Problem [1955]](https://link.springer.com/chapter/10.1007/978-3-540-68279-0_2)

- [James Munkres. Algorithms for Assignment and Transportation Problems [1957]](https://www.jstor.org/stable/2098689)

## Bài tập thực hành

- [UVA - Crime Wave - The Sequel](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1687)

- [UVA - Warehouse](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1829)

- [SGU - Beloved Sons](http://acm.sgu.ru/problem.php?contest=0&problem=210)

- [UVA - The Great Wall Game](http://livearchive.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1277)

- [UVA - Jogging Trails](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1237)
