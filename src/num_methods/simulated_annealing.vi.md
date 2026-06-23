---
tags:
    - Original
lang: vi
---
# Mô phỏng luyện kim (Simulated Annealing)

**Mô phỏng luyện kim (Simulated Annealing - SA)** là một thuật toán ngẫu nhiên (randomized algorithm), dùng để xấp xỉ giá trị tối ưu toàn cục của một hàm số. Nó được gọi là thuật toán ngẫu nhiên vì trong quá trình tìm kiếm, thuật toán sử dụng một lượng ngẫu nhiên nhất định, do đó đầu ra có thể thay đổi ngay cả khi đầu vào giống nhau.

## Bài toán

Giả sử ta có một hàm $E(s)$ để tính năng lượng của một trạng thái $s$. Nhiệm vụ của chúng ta là tìm trạng thái $s_{best}$ sao cho $E(s)$ đạt giá trị nhỏ nhất. **SA** phù hợp cho các bài toán mà các trạng thái là rời rạc và $E(s)$ có nhiều giá trị cực tiểu địa phương (local minima). Chúng ta sẽ lấy ví dụ với [Bài toán người giao hàng (Travelling Salesman Problem - TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem).

### Bài toán người giao hàng (TSP)

Bạn được cho một tập hợp các đỉnh trong không gian 2 chiều. Mỗi đỉnh được đặc trưng bởi tọa độ $x$ và $y$. Nhiệm vụ của bạn là tìm một thứ tự các đỉnh sao cho tổng khoảng cách phải di chuyển khi đi qua các đỉnh theo thứ tự đó là nhỏ nhất.

## Động lực
Luyện kim (annealing) là một quá trình luyện kim, trong đó vật liệu được nung nóng rồi để nguội dần, nhằm cho phép các nguyên tử bên trong sắp xếp lại thành một cấu trúc có năng lượng nội tại tối thiểu, từ đó tạo ra những tính chất khác biệt cho vật liệu. Trạng thái ở đây chính là sự sắp xếp của các nguyên tử và năng lượng nội tại là hàm cần tối ưu hóa. Ta có thể coi trạng thái ban đầu của các nguyên tử là một cực tiểu địa phương cho năng lượng nội tại. Để buộc vật liệu sắp xếp lại các nguyên tử, ta cần tác động để nó vượt qua các vùng mà năng lượng nội tại chưa ở mức tối thiểu nhằm đạt được cực tiểu toàn cục. Động lực này được tạo ra bằng cách nung nóng vật liệu lên một nhiệt độ cao hơn.

Mô phỏng luyện kim, theo nghĩa đen, mô phỏng lại quá trình này. Ta bắt đầu với một trạng thái ngẫu nhiên (vật liệu) và thiết lập một nhiệt độ cao (nung nóng). Bây giờ, thuật toán sẵn sàng chấp nhận các trạng thái có năng lượng cao hơn trạng thái hiện tại vì được "động viên" bởi nhiệt độ cao. Điều này ngăn thuật toán bị mắc kẹt trong các cực tiểu địa phương và cho phép nó tiến tới cực tiểu toàn cục. Khi thời gian trôi qua, thuật toán "nguội dần", từ chối các trạng thái có năng lượng cao hơn và tiến dần về cực tiểu gần nhất mà nó tìm thấy.

### Hàm năng lượng E(s)

$E(s)$ là hàm cần tối ưu (tối thiểu hóa hoặc tối đa hóa). Nó ánh xạ mỗi trạng thái tới một số thực. Trong trường hợp của TSP, $E(s)$ trả về tổng khoảng cách của một chu trình khép kín đi qua các đỉnh theo thứ tự của trạng thái đó.

### Trạng thái (State)

Không gian trạng thái là miền xác định của hàm năng lượng, $E(s)$, và một trạng thái là bất kỳ phần tử nào thuộc không gian trạng thái đó. Trong trường hợp của TSP, tất cả các đường đi có thể để thăm tất cả các đỉnh chính là không gian trạng thái, và bất kỳ một đường đi đơn lẻ nào trong số đó đều được coi là một trạng thái.

### Trạng thái lân cận (Neighbouring state)

Là một trạng thái nằm trong không gian trạng thái và ở gần trạng thái trước đó. Thông thường, điều này có nghĩa là ta có thể thu được trạng thái lân cận từ trạng thái ban đầu bằng một phép biến đổi đơn giản. Trong bài toán người giao hàng, một trạng thái lân cận được tạo ra bằng cách chọn ngẫu nhiên 2 đỉnh và hoán đổi vị trí của chúng trong trạng thái hiện tại.

## Thuật toán

Ta bắt đầu với một trạng thái ngẫu nhiên $s$. Trong mỗi bước, ta chọn một trạng thái lân cận $s_{next}$ của trạng thái hiện tại $s$. Nếu $E(s_{next}) < E(s)$, ta cập nhật $s = s_{next}$. Ngược lại, ta sử dụng một hàm chấp nhận xác suất $P(E(s),E(s_{next}),T)$ để quyết định xem có nên chuyển đến $s_{next}$ hay ở lại $s$. Ở đây, $s_{next}$ là nhiệt độ, ban đầu được đặt ở mức cao và giảm dần theo thời gian. Nhiệt độ càng cao, khả năng chấp nhận chuyển sang $s_{next}$ càng lớn. Đồng thời, ta cũng lưu vết trạng thái tốt nhất $s_{best}$ qua tất cả các lần lặp. Quá trình tiếp diễn cho đến khi hội tụ hoặc hết thời gian.

<center>
![Biểu diễn trực quan của mô phỏng luyện kim, tìm kiếm giá trị cực đại của một hàm số có nhiều cực đại địa phương.](https://upload.wikimedia.org/wikipedia/commons/d/d5/Hill_Climbing_with_Simulated_Annealing.gif)
<br>
<i>Biểu diễn trực quan của mô phỏng luyện kim, tìm kiếm giá trị cực đại của một hàm số có nhiều cực đại địa phương.</i>
<br>
</center>

### Nhiệt độ (T) và độ giảm (u)

Nhiệt độ của hệ thống định lượng sự sẵn sàng của thuật toán trong việc chấp nhận một trạng thái có năng lượng cao hơn. Độ giảm là một hằng số định lượng "tốc độ làm nguội" của thuật toán. Tốc độ làm nguội chậm (giá trị $u$ lớn hơn) thường mang lại kết quả tốt hơn.

## Hàm chấp nhận xác suất (PAF)

$P(E,E_{next},T) = 
    \begin{cases}
       \text{True} &\quad\text{if }  \mathcal{U}_{[0,1]} \le \exp(-\frac{E_{next}-E}{T}) \\
       \text{False} &\quad\text{otherwise}\\
     \end{cases}$

Ở đây, $\mathcal{U}_{[0,1]}$ là một giá trị ngẫu nhiên liên tục phân phối đều trên $[0,1]$. Hàm này nhận đầu vào là trạng thái hiện tại, trạng thái kế tiếp và nhiệt độ, trả về một giá trị boolean, cho biết quá trình tìm kiếm có nên chuyển đến $s_{next}$ hay ở lại $s$. Lưu ý rằng đối với $E_{next} < E$, hàm này luôn trả về True; ngược lại, thuật toán vẫn có thể thực hiện di chuyển với xác suất $\exp(-\frac{E_{next}-E}{T})$, tương ứng với [Gibbs measure](https://en.wikipedia.org/wiki/Gibbs_measure).

```cpp
bool P(double E,double E_next,double T,mt19937 rng){
    double prob =  exp(-(E_next-E)/T);
    if(prob > 1) return true;
    else{
        bernoulli_distribution d(prob); 
        return d(rng);
    }
}
```
## Khuôn mẫu code (Code Template)

```cpp
class state {
    public:
    state() {
        // Generate the initial state
    }
    state next() {
        state s_next;
        // Modify s_next to a random neighboring state
        return s_next;
    }
    double E() {
        // Implement the energy function here
    };
};


pair<double, state> simAnneal() {
    state s = state();
    state best = s;
    double T = 10000; // Initial temperature
    double u = 0.995; // decay rate
    double E = s.E();
    double E_next;
    double E_best = E;
    mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
    while (T > 1) {
        state next = s.next();
        E_next = next.E();
        if (P(E, E_next, T, rng)) {
            s = next;
            if (E_next < E_best) {
                best = s;
                E_best = E_next;
            }
            E = E_next;
        }
        T *= u;
    }
    return {E_best, best};
}

```
## Cách sử dụng:
Điền các hàm cho class trạng thái một cách phù hợp. Nếu bạn đang cố gắng tìm giá trị cực đại toàn cục thay vì cực tiểu, hãy đảm bảo rằng hàm $E()$ trả về giá trị âm của hàm bạn đang tối đa hóa và in $-E_{best}$ ở cuối. Thiết lập các tham số dưới đây theo nhu cầu của bạn.

### Các tham số
- $T$ : Nhiệt độ ban đầu. Đặt ở giá trị cao hơn nếu bạn muốn quá trình tìm kiếm chạy trong thời gian dài hơn.
- $u$ : Độ giảm. Quyết định tốc độ làm nguội. Tốc độ làm nguội chậm hơn (giá trị u lớn hơn) thường cho kết quả tốt hơn, nhưng phải trả giá bằng việc thời gian chạy lâu hơn. Đảm bảo $u < 1$.

Số lượng vòng lặp mà thuật toán sẽ thực hiện được cho bởi biểu thức:

$N =   \lceil -\log_{u}{T} \rceil$

Mẹo để chọn $T$ và $u$ : Nếu có nhiều cực tiểu địa phương và không gian trạng thái rộng, hãy đặt $u = 0.999$ để có tốc độ làm nguội chậm, giúp thuật toán khám phá nhiều khả năng hơn. Ngược lại, nếu không gian trạng thái hẹp hơn, $u = 0.99$ là đủ. Nếu không chắc chắn, hãy an toàn bằng cách đặt $u = 0.998$ hoặc cao hơn. Hãy tính độ phức tạp thời gian của một lần lặp duy nhất, sử dụng nó để ước tính giá trị $N$ nhằm tránh lỗi TLE, sau đó sử dụng công thức dưới đây để thu được $T$.

$T = u^{-N}$

### Ví dụ cài đặt cho TSP
```cpp

class state {
    public:
    vector<pair<int, int>> points;
	std::mt19937 mt{ static_cast<std::mt19937::result_type>(
		std::chrono::steady_clock::now().time_since_epoch().count()
		) };
    state() {
        points = {%raw%} {{0,0},{2,2},{0,2},{2,0},{0,1},{1,2},{2,1},{1,0}} {%endraw%};
    }
    state next() {
        state s_next;
        s_next.points = points;
        uniform_int_distribution<> choose(0, points.size()-1);
        int a = choose(mt);
        int b = choose(mt);
        s_next.points[a].swap(s_next.points[b]);
        return s_next;
    }

    double euclidean(pair<int, int> a, pair<int, int> b) {
        return hypot(a.first - b.first, a.second - b.second);
    }
    
    double E() {
        double dist = 0;
        int n = points.size();
        for (int i = 0;i < n; i++)
            dist += euclidean(points[i], points[(i+1)%n]);
        return dist;
    };
};

int main() {
    pair<double, state> res;
    res = simAnneal();
    double E_best = res.first;
    state best = res.second;
    cout << "Length of shortest path found : " << E_best << "\n";
    cout << "Order of points in shortest path : \n";
    for(auto x: best.points) {
        cout << x.first << " " << x.second << "\n";
    }
}
```

## Các sửa đổi bổ sung cho thuật toán:

- Thêm điều kiện thoát dựa trên thời gian vào vòng lặp `while` để tránh lỗi TLE.
- Độ giảm được cài đặt ở trên là độ giảm theo hàm mũ. Bạn có thể thay thế bằng một hàm độ giảm tùy theo nhu cầu.
- Hàm chấp nhận xác suất ở trên ưu tiên chấp nhận các trạng thái có năng lượng thấp hơn nhờ hệ số $E_{next} - E$ ở tử số của số mũ. Bạn có thể loại bỏ hệ số này để làm cho PAF độc lập với sự khác biệt về năng lượng.
- Ảnh hưởng của sự khác biệt năng lượng, $E_{next} - E$, lên PAF có thể được tăng/giảm bằng cách tăng/giảm cơ số của hàm mũ như hình dưới đây:
```cpp
bool P(double E, double E_next, double T, mt19937 rng) {
    double e = 2; // set e to any real number greater than 1
    double prob =  pow(e,-(E_next-E)/T);
    if (prob > 1)
        return true;
    else {
        bernoulli_distribution d(prob); 
        return d(rng);
    }
}
```

## Các bài tập

- [USACO Jan 2017 - Subsequence Reversal](https://usaco.org/index.php?page=viewproblem2&cpid=698)
- [Deltix Summer 2021 - DIY Tree](https://codeforces.com/contest/1556/problem/H)
- [AtCoder Contest Scheduling](https://atcoder.jp/contests/intro-heuristics/tasks/intro_heuristics_a)