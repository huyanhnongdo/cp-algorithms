---
tags:
  - Original
lang: vi
---
# Điểm nguyên bên trong đa giác không có đỉnh nguyên

Đối với các đa giác có đỉnh là các điểm nguyên (lattice polygon), chúng ta có công thức Pick để đếm số điểm nguyên nằm bên trong đa giác.
Vậy còn đối với các đa giác có đỉnh là các số thực tùy ý thì sao?

Chúng ta hãy xử lý từng cạnh của đa giác một cách riêng biệt, sau đó cộng dồn số lượng điểm nguyên nằm dưới mỗi cạnh, có tính đến hướng của cạnh đó để xác định dấu (giống như cách tính diện tích đa giác bằng các hình thang).

Trước hết, cần lưu ý rằng nếu cạnh hiện tại có hai đầu mút là $A=(x_1;y_1)$ và $B=(x_2;y_2)$, thì nó có thể được biểu diễn dưới dạng một hàm số tuyến tính:

$$y=y_1+(y_2-y_1) \cdot \dfrac{x-x_1}{x_2-x_1}=\left(\dfrac{y_2-y_1}{x_2-x_1}\right)\cdot x + \left(\dfrac{y_1x_2-x_1y_2}{x_2-x_1}\right)$$

$$y = k \cdot x + b,~k = \dfrac{y_2-y_1}{x_2-x_1},~b = \dfrac{y_1x_2-x_1y_2}{x_2-x_1}$$

Bây giờ, chúng ta sẽ thực hiện phép thế $x=x'+\lceil x_1 \rceil$ sao cho $b' = b + k \cdot \lceil x_1 \rceil$.
Điều này cho phép chúng ta làm việc với $x_1'=0$ và $x_2'=x_2 - \lceil x_1 \rceil$.
Đặt $n = \lfloor x_2' \rfloor$.

Để đảm bảo tính toàn vẹn của thuật toán, chúng ta sẽ không cộng các điểm tại $x = n$ và trên $y = 0$.
Các điểm này có thể được cộng bổ sung thủ công sau đó.
Do đó, chúng ta cần tính tổng $\sum\limits_{x'=0}^{n - 1} \lfloor k' \cdot x' + b'\rfloor$. Ta cũng giả sử rằng $k' \geq 0$ và $b'\geq 0$.
Nếu không, ta nên thay thế bằng $x'=-t$ và cộng $\lceil|b'|\rceil$ vào $b'$.

Hãy thảo luận về cách đánh giá tổng $\sum\limits_{x=0}^{n - 1} \lfloor k \cdot x + b\rfloor$.
Chúng ta có hai trường hợp:

  - $k \geq 1$ hoặc $b \geq 1$.
  
    Khi đó, ta bắt đầu bằng việc tính tổng các điểm nằm dưới $y=\lfloor k \rfloor \cdot x + \lfloor b \rfloor$. Số lượng của chúng bằng
    
    \[ \sum\limits_{x=0}^{n - 1} \lfloor k \rfloor \cdot x + \lfloor b \rfloor=\dfrac{(\lfloor k \rfloor(n-1)+2\lfloor b \rfloor) n}{2}. \]
    
    Bây giờ, chúng ta chỉ quan tâm đến các điểm $(x;y)$ sao cho $\lfloor k \rfloor \cdot x + \lfloor b \rfloor < y \leq k\cdot x + b$.
    Số lượng này tương đương với số điểm thỏa mãn $0 < y \leq (k - \lfloor k \rfloor) \cdot x + (b - \lfloor b \rfloor)$.
    Như vậy, chúng ta đã quy bài toán về $k'= k - \lfloor k \rfloor$, $b' = b - \lfloor b \rfloor$ và cả hai $k'$ cùng $b'$ đều nhỏ hơn $1$.
    Dưới đây là hình minh họa, chúng ta chỉ cần cộng các điểm màu xanh và trừ hàm số tuyến tính màu xanh ra khỏi hàm màu đen để đưa bài toán về các giá trị nhỏ hơn cho $k$ và $b$:
    <div style="text-align: center;" markdown="1">

![Trừ đi hàm tuyến tính làm tròn xuống](lattice.png)

</div>

  - $k < 1$ và $b < 1$.

    Nếu $\lfloor k \cdot n + b\rfloor$ bằng $0$, chúng ta có thể trả về $0$ một cách an toàn.
    Nếu không phải trường hợp này, ta có thể nói rằng không có điểm nguyên nào thỏa mãn $x < 0$ và $0 < y \leq k \cdot x + b$.
    Điều đó có nghĩa là kết quả sẽ không đổi nếu ta xem xét hệ tọa độ mới, trong đó $O'=(n;\lfloor k\cdot n + b\rfloor)$, trục $x'$ hướng xuống dưới và trục $y'$ hướng sang trái.
    Đối với hệ tọa độ này, chúng ta quan tâm đến các điểm nguyên thuộc tập hợp
    
    \[ \left\{(x;y)~\bigg|~0 \leq x < \lfloor k \cdot n + b\rfloor,~ 0 < y \leq \dfrac{x+(k\cdot n+b)-\lfloor k\cdot n + b \rfloor}{k}\right\} \]
    
    điều này đưa chúng ta trở lại trường hợp $k>1$.
    Bạn có thể thấy gốc tọa độ mới $O'$ cùng các trục $X'$ và $Y'$ trong hình dưới đây:
    <div style="text-align: center;" markdown="1">

![Hệ tọa độ và các trục mới](mirror.png)

</div>
    Như bạn thấy, trong hệ tọa độ mới, hàm tuyến tính sẽ có hệ số $\tfrac 1 k$ và điểm 0 của nó sẽ nằm tại $\lfloor k\cdot n + b \rfloor-(k\cdot n+b)$, giúp công thức trên trở nên chính xác.

## Phân tích độ phức tạp

Chúng ta phải đếm tối đa $\dfrac{(k(n-1)+2b)n}{2}$ điểm.
Trong số đó, chúng ta sẽ đếm $\dfrac{\lfloor k \rfloor (n-1)+2\lfloor b \rfloor}{2}$ ở bước đầu tiên.
Ta có thể coi $b$ là nhỏ không đáng kể vì ta có thể bắt đầu bằng cách làm cho nó nhỏ hơn $1$.
Trong trường hợp đó, ta có thể nói rằng ta đếm khoảng $\dfrac{\lfloor k \rfloor}{k} \geq \dfrac 1 2$ của tất cả các điểm.
Do đó, chúng ta sẽ kết thúc trong $O(\log n)$ bước.

## Cài đặt

Dưới đây là hàm đơn giản để tính số lượng điểm nguyên $(x;y)$ thỏa mãn $0 \leq x < n$ và $0 < y \leq \lfloor k x+b\rfloor$:

```cpp
int count_lattices(Fraction k, Fraction b, long long n) {
    auto fk = k.floor();
    auto fb = b.floor();
    auto cnt = 0LL;
    if (k >= 1 || b >= 1) {
        cnt += (fk * (n - 1) + 2 * fb) * n / 2;
        k -= fk;
        b -= fb;
    }
    auto t = k * n + b;
    auto ft = t.floor();
    if (ft >= 1) {
        cnt += count_lattices(1 / k, (t - t.floor()) / k, t.floor());
    }
    return cnt;
}
```

Ở đây `Fraction` là một lớp xử lý các số hữu tỉ.
Trên thực tế, có vẻ như nếu tất cả các mẫu số và tử số có giá trị tuyệt đối tối đa là $C$, thì trong các lời gọi đệ quy, chúng sẽ tối đa là $C^2$ nếu bạn liên tục chia tử số và mẫu số cho ước chung lớn nhất (GCD) của chúng.
Với giả định này, ta có thể sử dụng các số thực (`double`) và yêu cầu độ chính xác là $\varepsilon^2$, trong đó $\varepsilon$ là độ chính xác mà $k$ và $b$ được cung cấp.
Điều đó có nghĩa là trong hàm `floor`, bạn nên coi các số là số nguyên nếu chúng sai khác không quá $\varepsilon^2$ so với một số nguyên.