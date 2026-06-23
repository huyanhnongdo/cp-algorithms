---
tags:
  - Original
lang: vi
---
# Giao của các nửa mặt phẳng (Half-plane intersection)

Trong bài viết này, chúng ta sẽ thảo luận về bài toán tính giao của một tập hợp các nửa mặt phẳng. Giao của các nửa mặt phẳng này có thể được biểu diễn một cách thuận tiện dưới dạng một vùng lồi hoặc một đa giác lồi, trong đó mọi điểm bên trong nó đều nằm trong tất cả các nửa mặt phẳng đã cho. Đây chính là đa giác mà chúng ta muốn tìm hoặc xây dựng. Chúng ta sẽ đưa ra một số trực giác ban đầu cho bài toán, mô tả một hướng tiếp cận $O(N \log N)$ được gọi là thuật toán "Sắp xếp và tăng dần" (Sort-and-Incremental) và đưa ra một vài ứng dụng mẫu của kỹ thuật này.

Người đọc được khuyến khích nên làm quen với các khái niệm hình học cơ bản và các phép toán (điểm, vector, giao điểm của đường thẳng). Ngoài ra, kiến thức về [Bao lồi (Convex Hulls)](../geometry/convex-hull.md) hoặc [Kỹ thuật bao lồi (Convex Hull Trick)](../geometry/convex_hull_trick.md) có thể giúp hiểu rõ hơn các khái niệm trong bài viết này, tuy nhiên đây không phải là điều kiện bắt buộc.

## Các làm rõ và định nghĩa ban đầu

Trong toàn bộ bài viết, chúng ta sẽ đưa ra một số giả định (trừ khi có quy định khác):

1. Chúng ta định nghĩa $N$ là số lượng nửa mặt phẳng trong tập hợp đã cho.
2. Chúng ta sẽ biểu diễn các đường thẳng và nửa mặt phẳng bằng một điểm và một vector (bất kỳ điểm nào nằm trên đường thẳng đó và vector chỉ phương của đường thẳng). Với trường hợp nửa mặt phẳng, chúng ta giả định rằng mỗi nửa mặt phẳng cho phép vùng nằm ở phía bên trái của vector chỉ phương của nó. Ngoài ra, chúng ta định nghĩa góc của một nửa mặt phẳng là góc cực của vector chỉ phương của nó. Xem hình ảnh bên dưới để biết ví dụ.
3. Chúng ta giả định rằng giao điểm kết quả luôn là bị chặn hoặc rỗng. Nếu cần xử lý trường hợp không bị chặn, chúng ta có thể đơn giản thêm 4 nửa mặt phẳng để định nghĩa một hộp bao đủ lớn.
4. Để đơn giản, chúng ta giả định không có các nửa mặt phẳng song song trong tập hợp đã cho. Ở phần cuối bài viết, chúng ta sẽ thảo luận cách xử lý các trường hợp như vậy.

![](halfplanes_rep.png)

Nửa mặt phẳng $y \geq 2x - 2$ có thể được biểu diễn bằng điểm $P = (1, 0)$ với vector chỉ phương $PQ = Q - P = (1, 2)$

## Phương pháp vét cạn - $O(N^3)$ {data-toc-label="Phương pháp vét cạn - O(N^3)"}

Một trong những lời giải trực diện và rõ ràng nhất là tính giao điểm của các đường thẳng của tất cả các cặp nửa mặt phẳng, và với mỗi điểm, kiểm tra xem nó có nằm trong tất cả các nửa mặt phẳng còn lại hay không. Vì có $O(N^2)$ giao điểm, và với mỗi giao điểm chúng ta phải kiểm tra $O(N)$ nửa mặt phẳng, độ phức tạp thời gian tổng cộng là $O(N^3)$. Vùng giao thực tế sau đó có thể được tái tạo bằng cách sử dụng, ví dụ, thuật toán bao lồi trên tập các giao điểm nằm trong tất cả các nửa mặt phẳng.

Rất dễ hiểu tại sao cách này hoạt động: các đỉnh của đa giác lồi kết quả đều là giao điểm của các đường thẳng nửa mặt phẳng, và mỗi đỉnh đó hiển nhiên là một phần của tất cả các nửa mặt phẳng. Ưu điểm chính của phương pháp này là dễ hiểu, dễ nhớ và dễ cài đặt ngay lập tức nếu bạn chỉ cần kiểm tra xem giao điểm có rỗng hay không. Tuy nhiên, nó cực kỳ chậm và không phù hợp với hầu hết các bài toán, vì vậy chúng ta cần một phương pháp nhanh hơn.

## Phương pháp tăng dần - $O(N^2)$ {data-toc-label="Phương pháp tăng dần - O(N^2)"}

Một cách tiếp cận khác khá thẳng thắn là xây dựng dần dần giao của các nửa mặt phẳng, từng cái một. Phương pháp này về cơ bản tương đương với việc cắt một đa giác lồi bằng một đường thẳng $N$ lần, và loại bỏ các nửa mặt phẳng dư thừa ở mỗi bước. Để thực hiện điều này, chúng ta có thể biểu diễn đa giác lồi dưới dạng một danh sách các đoạn thẳng, và để cắt nó bằng một nửa mặt phẳng, chúng ta chỉ cần tìm các giao điểm của các đoạn thẳng với đường thẳng của nửa mặt phẳng đó (chỉ có hai giao điểm nếu đường thẳng cắt đa giác đúng cách), và thay thế tất cả các đoạn thẳng nằm ở giữa bằng đoạn thẳng mới tương ứng với nửa mặt phẳng. Vì quy trình như vậy có thể được thực hiện trong thời gian tuyến tính, chúng ta có thể bắt đầu với một hộp bao lớn và cắt dần bằng từng nửa mặt phẳng một, thu được độ phức tạp thời gian tổng cộng là $O(N^2)$.

Phương pháp này là một bước tiến lớn, nhưng việc phải lặp qua $O(N)$ nửa mặt phẳng ở mỗi bước thực sự gây lãng phí. Chúng ta sẽ thấy tiếp theo rằng, bằng cách thực hiện một số quan sát thông minh, các ý tưởng đằng sau cách tiếp cận tăng dần này có thể được tái sử dụng để tạo ra một thuật toán $O(N \log N)$.

## Thuật toán Sắp xếp và tăng dần - $O(N \log N)$ {data-toc-label="Thuật toán Sắp xếp và tăng dần - O(N log N)"}

Nguồn tài liệu được ghi chép chính thức đầu tiên mà chúng tôi tìm thấy về thuật toán này là luận văn của Zeyuan Zhu cho kỳ thi chọn đội tuyển Trung Quốc có tiêu đề [Thuật toán mới cho giao của nửa mặt phẳng và giá trị thực tiễn của nó](http://people.csail.mit.edu/zeyuan/publications.htm), từ năm 2006. Cách tiếp cận mà chúng tôi sẽ mô tả tiếp theo dựa trên cùng thuật toán này, nhưng thay vì tính hai giao điểm riêng biệt cho nửa dưới và nửa trên, chúng ta sẽ xây dựng tất cả cùng một lúc trong một lượt duyệt với một hàng đợi hai đầu (deque).

Bản thân thuật toán, như tên gọi đã gợi ý, tận dụng thực tế là vùng kết quả từ giao của các nửa mặt phẳng là lồi, do đó nó sẽ bao gồm một số đoạn của các nửa mặt phẳng được sắp xếp theo thứ tự góc. Điều này dẫn đến một quan sát quan trọng: nếu chúng ta giao dần các nửa mặt phẳng theo thứ tự sắp xếp theo góc (như cách chúng xuất hiện trong hình dạng cuối cùng của giao điểm) và lưu trữ chúng trong một hàng đợi hai đầu, thì chúng ta sẽ chỉ cần loại bỏ các nửa mặt phẳng khỏi phía trước và phía sau của deque.

Để hình dung rõ hơn, giả sử chúng ta đang thực hiện phương pháp tăng dần mô tả trước đó trên một tập hợp các nửa mặt phẳng đã được sắp xếp theo góc (trong trường hợp này, chúng ta giả định chúng được sắp xếp từ $-\pi$ đến $\pi$), và giả sử chúng ta sắp bắt đầu bước thứ $k$. Điều này có nghĩa là chúng ta đã xây dựng giao của $k-1$ nửa mặt phẳng đầu tiên. Bây giờ, vì các nửa mặt phẳng đã được sắp xếp theo góc, bất kể nửa mặt phẳng thứ $k$ là gì, chúng ta có thể chắc chắn rằng nó sẽ tạo thành một lượt rẽ lồi với nửa mặt phẳng thứ $(K-1)$. Vì lý do đó, một vài điều có thể xảy ra:

1. Một vài (có thể không có) nửa mặt phẳng ở phía sau của giao điểm có thể trở nên *dư thừa*. Trong trường hợp này, chúng ta cần loại bỏ những nửa mặt phẳng vô dụng này khỏi phía sau của deque.
2. Một vài (có thể không có) nửa mặt phẳng ở phía trước có thể trở nên *dư thừa*. Tương tự trường hợp 1, chúng ta chỉ cần loại bỏ chúng khỏi phía trước của deque.
3. Giao điểm có thể trở nên rỗng (sau khi xử lý trường hợp 1 và/hoặc 2). Trong trường hợp này, chúng ta chỉ cần báo cáo giao điểm là rỗng và kết thúc thuật toán.

*Chúng ta nói một nửa mặt phẳng là "dư thừa" nếu nó không đóng góp bất cứ điều gì vào giao điểm. Một nửa mặt phẳng như vậy có thể bị loại bỏ mà giao điểm kết quả không hề thay đổi.*

Dưới đây là một ví dụ nhỏ với minh họa:

Giả sử $H = \{ A, B, C, D, E \}$ là tập các nửa mặt phẳng hiện có trong giao điểm. Ngoài ra, giả sử $P = \{ p, q, r, s \}$ là tập các giao điểm của các nửa mặt phẳng kề nhau trong H. Bây giờ, giả sử chúng ta muốn giao nó với nửa mặt phẳng $F$, như thấy trong hình minh họa bên dưới:

![](halfplanes_hp1.png)

Lưu ý rằng nửa mặt phẳng $F$ làm cho $A$ và $E$ trở nên dư thừa trong giao điểm. Vì vậy, chúng ta loại bỏ cả $A$ và $E$ khỏi phía trước và phía sau của giao điểm, và thêm $F$ vào cuối. Và cuối cùng chúng ta thu được giao điểm mới $H = \{ B, C, D, F\}$ với $P = \{ q, r, t, u \}$.

![](halfplanes_hp2.png)

Với tất cả những điều này, chúng ta đã có gần như mọi thứ cần thiết để thực sự cài đặt thuật toán, nhưng chúng ta vẫn cần thảo luận về một số trường hợp đặc biệt. Ở đầu bài viết, chúng ta đã nói rằng chúng ta sẽ thêm một hộp bao để xử lý các trường hợp giao điểm có thể không bị chặn, vì vậy trường hợp khó duy nhất mà chúng ta thực sự cần xử lý là các nửa mặt phẳng song song. Chúng ta có thể có hai trường hợp con: hai nửa mặt phẳng có thể song song cùng hướng hoặc ngược hướng. Lý do trường hợp này cần được xử lý riêng là vì chúng ta cần tính các giao điểm của các đường thẳng nửa mặt phẳng để kiểm tra xem một nửa mặt phẳng có dư thừa hay không, và hai đường thẳng song song không có giao điểm, vì vậy chúng ta cần một cách đặc biệt để xử lý chúng.

Đối với trường hợp các nửa mặt phẳng song song ngược hướng: Lưu ý rằng, vì chúng ta thêm hộp bao để xử lý trường hợp không bị chặn, điều này cũng xử lý trường hợp chúng ta có hai nửa mặt phẳng song song kề nhau với hướng ngược nhau sau khi sắp xếp, vì sẽ phải có ít nhất một trong các nửa mặt phẳng của hộp bao ở giữa hai nửa mặt phẳng này (nhớ rằng chúng được sắp xếp theo góc).

* Tuy nhiên, có khả năng là sau khi loại bỏ một số nửa mặt phẳng khỏi phía sau của deque, hai nửa mặt phẳng song song ngược hướng lại nằm cùng nhau. Trường hợp này chỉ xảy ra, cụ thể là, khi hai nửa mặt phẳng này tạo thành một giao điểm rỗng, vì nửa mặt phẳng cuối cùng này sẽ làm cho mọi thứ bị loại bỏ khỏi deque. Để tránh vấn đề này, chúng ta phải kiểm tra thủ công các nửa mặt phẳng song song, và nếu chúng có hướng ngược nhau, chúng ta chỉ cần dừng ngay thuật toán và trả về giao điểm rỗng.

Như vậy trường hợp duy nhất chúng ta thực sự cần xử lý là có nhiều nửa mặt phẳng với cùng một góc, và hóa ra trường hợp này khá dễ xử lý: chúng ta chỉ cần giữ lại nửa mặt phẳng nằm xa nhất về phía trái và xóa các nửa mặt phẳng còn lại, vì chúng sẽ hoàn toàn dư thừa.
Tóm lại, thuật toán đầy đủ sẽ có dạng như sau:

1. Chúng ta bắt đầu bằng cách sắp xếp tập hợp các nửa mặt phẳng theo góc, tốn $O(N \log N)$ thời gian.
2. Chúng ta sẽ lặp qua tập hợp các nửa mặt phẳng, và với mỗi cái, chúng ta sẽ thực hiện quy trình tăng dần, loại bỏ từ phía trước và phía sau của hàng đợi hai đầu khi cần thiết. Việc này sẽ tốn thời gian tuyến tính tổng cộng, vì mỗi nửa mặt phẳng chỉ có thể được thêm hoặc xóa một lần.
3. Cuối cùng, đa giác lồi kết quả từ giao điểm có thể thu được đơn giản bằng cách tính các giao điểm của các nửa mặt phẳng kề nhau trong deque ở cuối quy trình. Việc này cũng sẽ tốn thời gian tuyến tính. Cũng có thể lưu trữ các điểm như vậy trong bước 2 và bỏ qua hoàn toàn bước này, nhưng chúng tôi tin rằng tính toán chúng ngay trong lúc chạy sẽ dễ dàng hơn một chút (về mặt cài đặt).

Tổng cộng, chúng ta đã đạt được độ phức tạp thời gian $O(N \log N)$. Vì sắp xếp rõ ràng là nút thắt cổ chai, thuật toán có thể được làm cho chạy trong thời gian tuyến tính trong trường hợp đặc biệt khi chúng ta được cung cấp các nửa mặt phẳng đã được sắp xếp trước theo góc (một ví dụ của trường hợp như vậy sẽ là lấy các nửa mặt phẳng định nghĩa một đa giác lồi).

### Cài đặt trực tiếp

Dưới đây là một ví dụ cài đặt trực tiếp của thuật toán, với các chú thích giải thích hầu hết các phần:

Struct điểm/vector và nửa mặt phẳng đơn giản:

```cpp
// Redefine epsilon and infinity as necessary. Be mindful of precision errors.
const long double eps = 1e-9, inf = 1e9; 

// Basic point/vector struct.
struct Point { 

    long double x, y;
    explicit Point(long double x = 0, long double y = 0) : x(x), y(y) {}

    // Addition, subtraction, multiply by constant, dot product, cross product.

    friend Point operator + (const Point& p, const Point& q) {
        return Point(p.x + q.x, p.y + q.y); 
    }

    friend Point operator - (const Point& p, const Point& q) { 
        return Point(p.x - q.x, p.y - q.y); 
    }

    friend Point operator * (const Point& p, const long double& k) { 
        return Point(p.x * k, p.y * k); 
    } 
    
    friend long double dot(const Point& p, const Point& q) {
    	return p.x * q.x + p.y * q.y;
    }

    friend long double cross(const Point& p, const Point& q) { 
        return p.x * q.y - p.y * q.x; 
    }
};

// Basic half-plane struct.
struct Halfplane { 

    // 'p' is a passing point of the line and 'pq' is the direction vector of the line.
    Point p, pq; 
    long double angle;

    Halfplane() {}
    Halfplane(const Point& a, const Point& b) : p(a), pq(b - a) {
        angle = atan2l(pq.y, pq.x);    
    }

    // Check if point 'r' is outside this half-plane. 
    // Every half-plane allows the region to the LEFT of its line.
    bool out(const Point& r) { 
        return cross(pq, r - p) < -eps; 
    }

    // Comparator for sorting. 
    bool operator < (const Halfplane& e) const { 
        return angle < e.angle;
    } 

    // Intersection point of the lines of two half-planes. It is assumed they're never parallel.
    friend Point inter(const Halfplane& s, const Halfplane& t) {
        long double alpha = cross((t.p - s.p), t.pq) / cross(s.pq, t.pq);
        return s.p + (s.pq * alpha);
    }
};
```

Thuật toán:

```cpp
// Actual algorithm
vector<Point> hp_intersect(vector<Halfplane>& H) { 

    Point box[4] = {  // Bounding box in CCW order
        Point(inf, inf), 
        Point(-inf, inf), 
        Point(-inf, -inf), 
        Point(inf, -inf) 
    };

    for(int i = 0; i<4; i++) { // Add bounding box half-planes.
        Halfplane aux(box[i], box[(i+1) % 4]);
        H.push_back(aux);
    }

    // Sort by angle and start algorithm
    sort(H.begin(), H.end());
    deque<Halfplane> dq;
    int len = 0;
    for(int i = 0; i < int(H.size()); i++) {

        // Remove from the back of the deque while last half-plane is redundant
        while (len > 1 && H[i].out(inter(dq[len-1], dq[len-2]))) {
            dq.pop_back();
            --len;
        }

        // Remove from the front of the deque while first half-plane is redundant
        while (len > 1 && H[i].out(inter(dq[0], dq[1]))) {
            dq.pop_front();
            --len;
        }
        
        // Special case check: Parallel half-planes
        if (len > 0 && fabsl(cross(H[i].pq, dq[len-1].pq)) < eps) {
        	// Opposite parallel half-planes that ended up checked against each other.
        	if (dot(H[i].pq, dq[len-1].pq) < 0.0)
        		return vector<Point>();
        	
        	// Same direction half-plane: keep only the leftmost half-plane.
        	if (H[i].out(dq[len-1].p)) {
        		dq.pop_back();
        		--len;
        	}
        	else continue;
        }
        
        // Add new half-plane
        dq.push_back(H[i]);
        ++len;
    }

    // Final cleanup: Check half-planes at the front against the back and vice-versa
    while (len > 2 && dq[0].out(inter(dq[len-1], dq[len-2]))) {
        dq.pop_back();
        --len;
    }

    while (len > 2 && dq[len-1].out(inter(dq[0], dq[1]))) {
        dq.pop_front();
        --len;
    }

    // Report empty intersection if necessary
    if (len < 3) return vector<Point>();

    // Reconstruct the convex polygon from the remaining half-planes.
    vector<Point> ret(len);
    for(int i = 0; i+1 < len; i++) {
        ret[i] = inter(dq[i], dq[i+1]);
    }
    ret.back() = inter(dq[len-1], dq[0]);
    return ret;
}
```

### Thảo luận về cài đặt

Một điều đặc biệt cần lưu ý là trong trường hợp có nhiều nửa mặt phẳng cắt nhau tại cùng một điểm, thì thuật toán này có thể trả về các điểm lặp lại kề nhau trong đa giác cuối cùng. Tuy nhiên, điều này không ảnh hưởng đến việc đánh giá đúng liệu giao điểm có rỗng hay không, và nó cũng không ảnh hưởng gì đến diện tích đa giác. Bạn có thể muốn loại bỏ các phần tử trùng lặp này tùy thuộc vào các nhiệm vụ bạn cần làm sau đó. Bạn có thể làm điều này rất dễ dàng với `std::unique`. Chúng ta muốn giữ các điểm lặp lại trong quá trình thực thi thuật toán để các giao điểm có diện tích bằng không có thể được tính toán chính xác (ví dụ: các giao điểm chỉ bao gồm một điểm, đường thẳng hoặc đoạn thẳng). Tôi khuyến khích người đọc thử nghiệm một số trường hợp nhỏ tự tạo nơi giao điểm dẫn đến một điểm hoặc một đường thẳng.

Một điều nữa cần nói đến là làm gì nếu chúng ta được cung cấp các nửa mặt phẳng dưới dạng ràng buộc tuyến tính (ví dụ: $ax + by + c \leq 0$). Trong trường hợp đó, có hai lựa chọn. Bạn có thể cài đặt thuật toán với các sửa đổi tương ứng để làm việc với biểu diễn đó (về cơ bản tạo struct nửa mặt phẳng của riêng bạn, sẽ khá đơn giản nếu bạn quen với kỹ thuật bao lồi), hoặc bạn có thể chuyển đổi các đường thẳng thành biểu diễn mà chúng ta đã sử dụng trong bài viết này bằng cách lấy bất kỳ 2 điểm nào của mỗi đường thẳng. Nhìn chung, khuyến khích làm việc với biểu diễn mà bạn được cung cấp trong bài toán để tránh các vấn đề về độ chính xác bổ sung.

## Các bài toán, nhiệm vụ và ứng dụng

Nhiều bài toán có thể giải bằng giao của các nửa mặt phẳng cũng có thể giải mà không cần nó, nhưng thường với các cách tiếp cận phức tạp hoặc không phổ biến hơn. Nhìn chung, giao của các nửa mặt phẳng có thể xuất hiện khi xử lý các bài toán liên quan đến đa giác (chủ yếu là lồi), khả năng quan sát trên mặt phẳng và quy hoạch tuyến tính hai chiều. Dưới đây là một số nhiệm vụ mẫu có thể giải bằng kỹ thuật này:

### Giao của đa giác lồi

Một trong những ứng dụng cổ điển của giao các nửa mặt phẳng: Cho $N$ đa giác, tính vùng nằm trong tất cả các đa giác đó.

Vì giao của một tập hợp các nửa mặt phẳng là một đa giác lồi, chúng ta cũng có thể biểu diễn một đa giác lồi dưới dạng một tập hợp các nửa mặt phẳng (mỗi cạnh của đa giác là một đoạn của một nửa mặt phẳng). Tạo các nửa mặt phẳng này cho mỗi đa giác và tính giao của toàn bộ tập hợp. Độ phức tạp thời gian tổng cộng là $O(S \log S)$, trong đó S là tổng số cạnh của tất cả các đa giác. Bài toán cũng có thể giải về mặt lý thuyết trong $O(S \log N)$ bằng cách gộp $N$ tập hợp nửa mặt phẳng sử dụng heap và sau đó chạy thuật toán mà không cần bước sắp xếp, nhưng lời giải như vậy có hằng số phức tạp tệ hơn nhiều so với sắp xếp trực tiếp và chỉ cung cấp những cải tiến nhỏ về tốc độ cho $N$ rất nhỏ.

### Khả năng quan sát trên mặt phẳng

Các bài toán yêu cầu những việc như "xác định xem một số đoạn thẳng có thể nhìn thấy từ một số điểm trên mặt phẳng hay không" thường có thể được hình thành như các bài toán giao của nửa mặt phẳng. Lấy ví dụ, nhiệm vụ sau: Cho một đa giác đơn giản (không nhất thiết là lồi), xác định xem có bất kỳ điểm nào bên trong đa giác sao cho toàn bộ biên của đa giác có thể được quan sát từ điểm đó không. Điều này còn được gọi là tìm [nhân của một đa giác (kernel of a polygon)](https://en.wikipedia.org/wiki/Star-shaped_polygon) và có thể được giải bằng cách giao các nửa mặt phẳng đơn giản, lấy mỗi cạnh của đa giác làm một nửa mặt phẳng và sau đó tính giao của nó.

Dưới đây là một bài toán liên quan thú vị hơn được Artem Vasilyev trình bày trong một trong những [bài giảng tại Trường hè ICPC Brazil của anh ấy](https://youtu.be/WKyZSitpm6M?t=6463):
Cho một tập hợp $p$ các điểm $p_1, p_2\ \dots \ p_n$ trên mặt phẳng, xác định xem có điểm $q$ nào bạn có thể đứng để có thể nhìn thấy tất cả các điểm của $p$ từ trái sang phải theo thứ tự tăng dần của chỉ số của chúng.

Bài toán như vậy có thể được giải bằng cách nhận thấy rằng việc có thể nhìn thấy một điểm $p_i$ nằm bên trái $p_j$ cũng giống như việc có thể nhìn thấy phía bên phải của đoạn thẳng từ $p_i$ đến $p_j$ (hoặc tương đương, có thể nhìn thấy phía bên trái của đoạn thẳng từ $p_j$ đến $p_i$). Với suy nghĩ đó, chúng ta có thể đơn giản tạo một nửa mặt phẳng cho mỗi đoạn thẳng $p_i p_{i+1}$ (hoặc $p_{i+1} p_i$ tùy thuộc vào hướng bạn chọn) và kiểm tra xem giao của toàn bộ tập hợp có rỗng hay không.

### Giao của nửa mặt phẳng với tìm kiếm nhị phân

Một ứng dụng phổ biến khác là sử dụng giao của các nửa mặt phẳng như một công cụ để xác thực vị ngữ của quy trình tìm kiếm nhị phân. Đây là ví dụ về một bài toán như vậy, cũng được Artem Vasilyev trình bày trong cùng bài giảng đã được đề cập trước đó: Cho một đa giác **lồi** $P$, tìm đường tròn lớn nhất có thể nội tiếp bên trong nó.

Thay vì tìm kiếm một loại lời giải dạng đóng, các công thức khó chịu hoặc các lời giải thuật toán khó hiểu, hãy thử tìm kiếm nhị phân trên câu trả lời. Lưu ý rằng, đối với một $r$ cố định, một vòng tròn có bán kính $r$ có thể được nội tiếp bên trong $P$ chỉ khi tồn tại một điểm bên trong $P$ có khoảng cách lớn hơn hoặc bằng $r$ đến tất cả các điểm trên biên của $P$. Điều kiện này có thể được xác thực bằng cách "co" đa giác vào trong một khoảng cách $r$ và kiểm tra xem đa giác vẫn không bị suy biến (hoặc là một điểm/đoạn thẳng). Quy trình như vậy có thể được mô phỏng bằng cách lấy các nửa mặt phẳng của các cạnh đa giác theo thứ tự ngược chiều kim đồng hồ, dịch chuyển từng nửa mặt phẳng một khoảng cách $r$ theo hướng vùng mà chúng cho phép (tức là vuông góc với vector chỉ phương của nửa mặt phẳng), và kiểm tra xem giao điểm có không rỗng hay không.

Rõ ràng, nếu chúng ta có thể nội tiếp một hình tròn bán kính $r$, chúng ta cũng có thể nội tiếp bất kỳ hình tròn nào khác có bán kính nhỏ hơn $r$. Vì vậy, chúng ta có thể thực hiện tìm kiếm nhị phân trên bán kính $r$ và xác thực từng bước sử dụng giao của các nửa mặt phẳng. Ngoài ra, lưu ý rằng các nửa mặt phẳng của một đa giác lồi đã được sắp xếp theo góc, nên có thể bỏ qua bước sắp xếp trong thuật toán. Do đó, chúng ta thu được độ phức tạp thời gian tổng cộng là $O(NK)$, trong đó $N$ là số đỉnh đa giác và $K$ là số lần lặp của tìm kiếm nhị phân (giá trị thực tế sẽ phụ thuộc vào phạm vi các câu trả lời có thể có và độ chính xác mong muốn).

### Quy hoạch tuyến tính hai chiều

Một ứng dụng nữa của giao các nửa mặt phẳng là quy hoạch tuyến tính trong hai biến. Tất cả các ràng buộc tuyến tính cho hai biến có thể được biểu diễn dưới dạng $Ax + By + C \leq 0$ (toán tử so sánh bất đẳng thức có thể thay đổi). Rõ ràng, đây chỉ là các nửa mặt phẳng, vì vậy việc kiểm tra xem một lời giải khả thi có tồn tại cho một tập hợp các ràng buộc tuyến tính hay không có thể được thực hiện bằng giao của các nửa mặt phẳng. Ngoài ra, đối với một tập hợp ràng buộc tuyến tính cho trước, có thể tính toán vùng các lời giải khả thi (tức là giao của các nửa mặt phẳng) và sau đó trả lời nhiều truy vấn về việc cực đại/cực tiểu hóa một hàm tuyến tính $f(x, y)$ phụ thuộc vào các ràng buộc trong $O(\log N)$ trên mỗi truy vấn sử dụng tìm kiếm nhị phân (rất giống với kỹ thuật bao lồi).

Cần đề cập rằng cũng tồn tại một thuật toán ngẫu nhiên khá đơn giản có thể kiểm tra xem một tập hợp các ràng buộc tuyến tính có lời giải khả thi hay không, và cực đại/cực tiểu hóa một hàm tuyến tính phụ thuộc vào các ràng buộc đã cho. Thuật toán ngẫu nhiên này cũng được giải thích rất hay bởi Artem Vasilyev trong bài giảng đã đề cập trước đó. Dưới đây là một số tài nguyên bổ sung về nó, nếu người đọc quan tâm: [CG - Bài giảng 4, phần 4 và 5](https://youtu.be/5dfc355t2y4) và [Blog của Petr Mitrichev (bao gồm lời giải cho bài toán khó nhất trong danh sách các bài toán luyện tập bên dưới)](https://petr-mitrichev.blogspot.com/2016/07/a-half-plane-week.html).

## Các bài toán luyện tập

### Các bài toán cổ điển, ứng dụng trực tiếp

* [Codechef - Animesh decides to settle down](https://www.codechef.com/problems/CHN02)
* [POJ - How I mathematician Wonder What You Are!](http://poj.org/problem?id=3130)
* [POJ - Rotating Scoreboard](http://poj.org/problem?id=3335)
* [POJ - Video Surveillance](http://poj.org/problem?id=1474)
* [POJ - Art Gallery](http://poj.org/problem?id=1279)
* [POJ - Uyuw's Concert](http://poj.org/problem?id=2451)

### Các bài toán khó hơn

* [POJ - Most Distant Point from the Sea - Medium](http://poj.org/problem?id=3525)
* [Baekjoon - Jeju's Island - Tương tự như trên nhưng bộ test có vẻ mạnh hơn](https://www.acmicpc.net/problem/3903)
* [POJ - Feng Shui - Medium](http://poj.org/problem?id=3384)
* [POJ - Triathlon - Medium/hard](http://poj.org/problem?id=1755)
* [DMOJ - Arrow - Medium/hard](https://dmoj.ca/problem/ccoprep3p3)
* [POJ - Jungle Outpost - Hard](http://poj.org/problem?id=3968)
* [Codeforces - Jungle Outpost (đường dẫn thay thế, bài J) - Hard](https://codeforces.com/gym/101309/attachments?mobile=false)
* [Yandex - Asymmetry Value (cần cuộc thi ảo để xem, bài F) - Very Hard](https://contest.yandex.com/contest/2540/enter/)

### Các bài toán bổ sung

* Trại lập trình Petrozavodsk lần thứ 40, Mùa đông 2021 - Ngày 1: Jagiellonian U Contest, Grand Prix of Krakow - Bài B: (Almost) Fair Cake-Cutting. Vào thời điểm viết bài viết, bài toán này ở chế độ riêng tư và chỉ những người tham gia Trại lập trình mới có thể truy cập.

## Tài liệu tham khảo, thư mục và các nguồn khác

### Các nguồn chính

* [Thuật toán mới cho giao của nửa mặt phẳng và giá trị thực tiễn của nó.](http://people.csail.mit.edu/zeyuan/publications.htm) Bài báo gốc về thuật toán.
* [Bài giảng tại Trường hè ICPC Brazil 2020 của Artem Vasilyev.](https://youtu.be/WKyZSitpm6M?t=6463) Bài giảng tuyệt vời về giao của nửa mặt phẳng. Cũng bao gồm các chủ đề hình học khác.

### Các blog hay (tiếng Trung)

* [Cơ sở hình học tính toán - Giao của các nửa mặt phẳng.](https://zhuanlan.zhihu.com/p/83499723)
* [Giới thiệu chi tiết về thuật toán giao các nửa mặt phẳng.](https://blog.csdn.net/qq_40861916/article/details/83541403)
* [Tóm tắt các bài toán giao các nửa mặt phẳng.](https://blog.csdn.net/qq_40482358/article/details/87921815)
* [Phương pháp tăng dần sắp xếp của giao các nửa mặt phẳng.](https://blog.csdn.net/u012061345/article/details/23872929)

### Thuật toán ngẫu nhiên

* [Quy hoạch tuyến tính và giao của nửa mặt phẳng - Phần 4 và 5.](https://youtu.be/5dfc355t2y4)
* [Blog của Petr Mitrichev: Một tuần về nửa mặt phẳng.](https://petr-mitrichev.blogspot.com/2016/07/a-half-plane-week.html)