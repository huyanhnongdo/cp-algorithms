---
tags:
  - Original
lang: vi
---
# Tổng Minkowski của các đa giác lồi

## Định nghĩa
Xét hai tập hợp điểm $A$ và $B$ trên mặt phẳng. Tổng Minkowski $A + B$ được định nghĩa là $\{a + b| a \in A, b \in B\}$.
Ở đây chúng ta sẽ xem xét trường hợp $A$ và $B$ là các đa giác lồi (Convex Polygon) $P$ và $Q$ bao gồm cả phần biên và phần bên trong.
Trong suốt bài viết này, chúng ta sẽ biểu diễn đa giác bằng các dãy đỉnh có thứ tự, để các ký hiệu như $|P|$ hoặc $P_i$ có ý nghĩa.
Kết quả cho thấy tổng của các đa giác lồi $P$ và $Q$ là một đa giác lồi với tối đa $|P| + |Q|$ đỉnh.

## Thuật toán

Ở đây chúng ta xem xét các đa giác được đánh số theo chu kỳ, nghĩa là $P_{|P|} = P_0,\ Q_{|Q|} = Q_0$, v.v.

Vì kích thước của tổng là tuyến tính theo kích thước của các đa giác ban đầu, chúng ta nên hướng tới một thuật toán có độ phức tạp thời gian tuyến tính.
Giả sử cả hai đa giác đều được sắp xếp theo ngược chiều kim đồng hồ. Xét các dãy cạnh $\{\overrightarrow{P_iP_{i+1}}\}$ và $\{\overrightarrow{Q_jQ_{j+1}}\}$ được sắp xếp theo góc cực (polar angle). Chúng ta khẳng định rằng dãy các cạnh của $P + Q$ có thể thu được bằng cách trộn (merge) hai dãy này trong khi vẫn giữ nguyên thứ tự góc cực và thay thế các vector cùng hướng liên tiếp bằng tổng của chúng. Việc sử dụng trực tiếp ý tưởng này dẫn đến một thuật toán thời gian tuyến tính, tuy nhiên, việc khôi phục các đỉnh của $P + Q$ từ dãy các cạnh đòi hỏi việc cộng vector nhiều lần, điều này có thể gây ra các vấn đề sai số nếu chúng ta làm việc với tọa độ số thực (floating-point), vì vậy chúng ta sẽ mô tả một sửa đổi nhỏ cho ý tưởng này.

Đầu tiên, chúng ta nên sắp xếp lại các đỉnh sao cho đỉnh đầu tiên của mỗi đa giác có tọa độ y nhỏ nhất (trong trường hợp có nhiều đỉnh như vậy, chọn đỉnh có tọa độ x nhỏ nhất). Sau đó, các cạnh của cả hai đa giác sẽ tự động được sắp xếp theo góc cực, vì vậy không cần phải tự sắp xếp chúng.
Bây giờ, chúng ta tạo hai con trỏ $i$ (trỏ đến một đỉnh của $P$) và $j$ (trỏ đến một đỉnh của $Q$), cả hai ban đầu đều bằng 0.
Chúng ta lặp lại các bước sau khi $i < |P|$ hoặc $j < |Q|$ còn thỏa mãn:

1. Thêm $P_i + Q_j$ vào $P + Q$.

2. So sánh góc cực của $\overrightarrow{P_iP_{i + 1}}$ và $\overrightarrow{Q_jQ_{j+1}}$.

3. Tăng con trỏ tương ứng với góc nhỏ hơn (nếu các góc bằng nhau, tăng cả hai).

## Minh họa

Dưới đây là hình ảnh minh họa, có thể giúp bạn hiểu rõ quá trình này.

<div style="text-align: center;" markdown="1">

![Minh họa](minkowski.gif)

</div>

## Khoảng cách giữa hai đa giác
Một trong những ứng dụng phổ biến nhất của tổng Minkowski là tính khoảng cách giữa hai đa giác lồi (hoặc đơn giản là kiểm tra xem chúng có giao nhau hay không).
Khoảng cách giữa hai đa giác lồi $P$ và $Q$ được định nghĩa là $\min\limits_{a \in P, b \in Q} ||a - b||$. Ta có thể thấy rằng khoảng cách luôn đạt được giữa hai đỉnh hoặc giữa một đỉnh và một cạnh, vì vậy chúng ta có thể dễ dàng tìm khoảng cách trong $O(|P||Q|)$. Tuy nhiên, với việc sử dụng khéo léo tổng Minkowski, chúng ta có thể giảm độ phức tạp xuống còn $O(|P| + |Q|)$.

Nếu chúng ta lấy đối xứng $Q$ qua điểm $(0, 0)$ để thu được đa giác $-Q$, bài toán quy về việc tìm khoảng cách nhỏ nhất giữa một điểm trong $P + (-Q)$ và $(0, 0)$. Chúng ta có thể tìm khoảng cách đó trong thời gian tuyến tính bằng ý tưởng sau:
Nếu $(0, 0)$ nằm bên trong hoặc trên biên của đa giác, khoảng cách là $0$, ngược lại khoảng cách đạt được giữa $(0, 0)$ và một đỉnh hoặc một cạnh nào đó của đa giác.
Vì tổng Minkowski có thể được tính trong thời gian tuyến tính, chúng ta có một thuật toán thời gian tuyến tính để tìm khoảng cách giữa hai đa giác lồi.

## Cài đặt
Dưới đây là phần cài đặt tổng Minkowski cho các đa giác có tọa độ nguyên. Lưu ý rằng trong trường hợp này, tất cả các tính toán có thể được thực hiện trên số nguyên vì thay vì tính toán các góc cực và so sánh trực tiếp chúng, chúng ta có thể xem xét dấu của tích có hướng (cross product) của hai vector.

```{.cpp file=minkowski}
struct pt{
    long long x, y;
    pt operator + (const pt & p) const {
        return pt{x + p.x, y + p.y};
    }
    pt operator - (const pt & p) const {
        return pt{x - p.x, y - p.y};
    }
    long long cross(const pt & p) const {
        return x * p.y - y * p.x;
    }
};

void reorder_polygon(vector<pt> & P){
    size_t pos = 0;
    for(size_t i = 1; i < P.size(); i++){
        if(P[i].y < P[pos].y || (P[i].y == P[pos].y && P[i].x < P[pos].x))
            pos = i;
    }
    rotate(P.begin(), P.begin() + pos, P.end());
}

vector<pt> minkowski(vector<pt> P, vector<pt> Q){
    // the first vertex must be the lowest
    reorder_polygon(P);
    reorder_polygon(Q);
    // we must ensure cyclic indexing
    P.push_back(P[0]);
    P.push_back(P[1]);
    Q.push_back(Q[0]);
    Q.push_back(Q[1]);
    // main part
    vector<pt> result;
    size_t i = 0, j = 0;
    while(i < P.size() - 2 || j < Q.size() - 2){
        result.push_back(P[i] + Q[j]);
        auto cross = (P[i + 1] - P[i]).cross(Q[j + 1] - Q[j]);
        if(cross >= 0 && i < P.size() - 2)
            ++i;
        if(cross <= 0 && j < Q.size() - 2)
            ++j;
    }
    return result;
}

```

## Bài tập
 * [Codeforces 87E Mogohu-Rea Idol](https://codeforces.com/problemset/problem/87/E)
 * [Codeforces 1195F Geometers Anonymous Club](https://codeforces.com/contest/1195/problem/F)
 * [TIMUS 1894 Non-Flying Weather](https://acm.timus.ru/problem.aspx?space=1&num=1894)