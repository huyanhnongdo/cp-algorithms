---
tags:
  - Translated
e_maxx_link: expressions_parsing
lang: vi
---
# Phân tích biểu thức (Expression parsing)

Cho một chuỗi chứa biểu thức toán học bao gồm các con số và nhiều toán tử khác nhau.
Chúng ta cần tính giá trị của biểu thức đó trong $O(n)$, với $n$ là độ dài của chuỗi.

Thuật toán được thảo luận ở đây sẽ chuyển đổi một biểu thức thành cái gọi là **ký pháp Ba Lan ngược** (reverse Polish notation) (một cách tường minh hoặc ẩn), và đánh giá biểu thức này.

## Ký pháp Ba Lan ngược (Reverse Polish notation)

Ký pháp Ba Lan ngược là một dạng viết các biểu thức toán học, trong đó các toán tử được đặt sau các toán hạng của chúng.
Ví dụ, biểu thức sau đây

$$a + b * c * d + (e - f) * (g * h + i)$$

có thể được viết dưới dạng ký pháp Ba Lan ngược như sau:

$$a b c * d * + e f - g h * i + * +$$

Ký pháp Ba Lan ngược được phát triển bởi triết gia và chuyên gia khoa học máy tính người Úc Charles Hamblin vào giữa những năm 1950, dựa trên ký pháp Ba Lan được đề xuất vào năm 1920 bởi nhà toán học người Ba Lan Jan Łukasiewicz.

Sự thuận tiện của ký pháp Ba Lan ngược nằm ở chỗ các biểu thức ở dạng này rất **dễ đánh giá** trong thời gian tuyến tính.
Chúng ta sử dụng một ngăn xếp (Stack), ban đầu ở trạng thái rỗng.
Chúng ta sẽ lặp qua các toán hạng và toán tử của biểu thức theo ký pháp Ba Lan ngược.
Nếu phần tử hiện tại là một số, ta đẩy giá trị đó vào đỉnh ngăn xếp; nếu phần tử hiện tại là một toán tử, ta lấy hai phần tử từ đỉnh ngăn xếp, thực hiện phép toán và đẩy kết quả trở lại đỉnh ngăn xếp.
Cuối cùng, trong ngăn xếp sẽ còn lại đúng một phần tử, đó chính là giá trị của biểu thức.

Rõ ràng cách đánh giá đơn giản này chạy trong thời gian $O(n)$.

## Phân tích biểu thức đơn giản

Trước mắt, chúng ta chỉ xem xét một bài toán đơn giản hóa:
giả sử rằng tất cả các toán tử đều là **toán tử hai ngôi** (tức là chúng lấy hai đối số) và tất cả đều **có tính kết hợp trái** (nếu các độ ưu tiên bằng nhau, chúng được thực hiện từ trái sang phải).
Dấu ngoặc đơn được cho phép sử dụng.

Chúng ta sẽ thiết lập hai ngăn xếp: một cho các số, và một cho các toán tử và dấu ngoặc đơn.
Ban đầu cả hai ngăn xếp đều rỗng.
Đối với ngăn xếp thứ hai, chúng ta sẽ duy trì điều kiện là tất cả các phép toán được sắp xếp theo độ ưu tiên giảm dần nghiêm ngặt.
Nếu có dấu ngoặc đơn trên ngăn xếp, thì mỗi khối toán tử (tương ứng với một cặp dấu ngoặc) sẽ được sắp xếp, và toàn bộ ngăn xếp không nhất thiết phải được sắp xếp.

Chúng ta sẽ lặp qua các ký tự của biểu thức từ trái sang phải.
Nếu ký tự hiện tại là một chữ số, ta đẩy giá trị của số này vào ngăn xếp.
Nếu ký tự hiện tại là dấu ngoặc mở, ta đẩy nó vào ngăn xếp.
Nếu ký tự hiện tại là dấu ngoặc đóng, ta thực hiện tất cả các toán tử trên ngăn xếp cho đến khi gặp dấu ngoặc mở (nói cách khác, chúng ta thực hiện tất cả các phép toán bên trong dấu ngoặc).
Cuối cùng, nếu ký tự hiện tại là một toán tử, thì chừng nào đỉnh ngăn xếp có một toán tử với độ ưu tiên bằng hoặc cao hơn, chúng ta sẽ thực hiện phép toán đó và đẩy toán tử mới vào ngăn xếp.

Sau khi xử lý xong toàn bộ chuỗi, một số toán tử có thể vẫn còn trong ngăn xếp, vì vậy chúng ta sẽ thực hiện nốt chúng.

Dưới đây là cách triển khai phương pháp này cho bốn toán tử $+$ $-$ $*$ $/$:

```{.cpp file=expression_parsing_simple}
bool delim(char c) {
    return c == ' ';
}

bool is_op(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

int priority (char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return -1;
}

void process_op(stack<int>& st, char op) {
    int r = st.top(); st.pop();
    int l = st.top(); st.pop();
    switch (op) {
        case '+': st.push(l + r); break;
        case '-': st.push(l - r); break;
        case '*': st.push(l * r); break;
        case '/': st.push(l / r); break;
    }
}

int evaluate(string& s) {
    stack<int> st;
    stack<char> op;
    for (int i = 0; i < (int)s.size(); i++) {
        if (delim(s[i]))
            continue;
        
        if (s[i] == '(') {
            op.push('(');
        } else if (s[i] == ')') {
            while (op.top() != '(') {
                process_op(st, op.top());
                op.pop();
            }
            op.pop();
        } else if (is_op(s[i])) {
            char cur_op = s[i];
            while (!op.empty() && priority(op.top()) >= priority(cur_op)) {
                process_op(st, op.top());
                op.pop();
            }
            op.push(cur_op);
        } else {
            int number = 0;
            while (i < (int)s.size() && isalnum(s[i]))
                number = number * 10 + s[i++] - '0';
            --i;
            st.push(number);
        }
    }

    while (!op.empty()) {
        process_op(st, op.top());
        op.pop();
    }
    return st.top();
}
```

Như vậy, chúng ta đã học được cách tính giá trị của một biểu thức trong $O(n)$, đồng thời sử dụng ngầm định ký pháp Ba Lan ngược.
Bằng cách sửa đổi nhẹ cách triển khai trên, chúng ta cũng có thể nhận được biểu thức dưới dạng ký pháp Ba Lan ngược một cách tường minh.

## Toán tử một ngôi (Unary operators)

Bây giờ giả sử rằng biểu thức cũng chứa các toán tử **một ngôi** (các toán tử chỉ lấy một đối số).
Dấu cộng một ngôi và dấu trừ một ngôi là những ví dụ phổ biến của các toán tử này.

Một trong những khác biệt trong trường hợp này là chúng ta cần xác định xem toán tử hiện tại là toán tử một ngôi hay hai ngôi.

Bạn có thể nhận thấy rằng trước một toán tử một ngôi, luôn là một toán tử khác hoặc một dấu ngoặc mở, hoặc không có gì cả (nếu nó nằm ở ngay đầu biểu thức).
Ngược lại, trước một toán tử hai ngôi luôn là một toán hạng (số) hoặc một dấu ngoặc đóng.
Do đó, việc gắn cờ để kiểm tra xem toán tử tiếp theo có thể là toán tử một ngôi hay không rất dễ dàng.

Ngoài ra, chúng ta cần thực hiện các toán tử một ngôi và hai ngôi theo cách khác nhau.
Và chúng ta cần chọn độ ưu tiên của toán tử một ngôi cao hơn tất cả các toán tử hai ngôi.

Ngoài ra, cần lưu ý rằng một số toán tử một ngôi (ví dụ: cộng một ngôi và trừ một ngôi) thực chất là **kết hợp phải**.

## Tính kết hợp phải (Right-associativity)

Kết hợp phải nghĩa là bất cứ khi nào các độ ưu tiên bằng nhau, các toán tử phải được đánh giá từ phải sang trái.

Như đã lưu ý ở trên, các toán tử một ngôi thường là kết hợp phải.
Một ví dụ khác về toán tử kết hợp phải là toán tử lũy thừa ($a \wedge b \wedge c$ thường được hiểu là $a^{b^c}$ chứ không phải $(a^b)^c$).

Chúng ta cần tạo ra sự khác biệt gì để xử lý đúng các toán tử kết hợp phải?
Hóa ra các thay đổi là rất nhỏ.
Điểm khác biệt duy nhất là nếu các độ ưu tiên bằng nhau, chúng ta sẽ trì hoãn việc thực thi các toán tử kết hợp phải.

Dòng duy nhất cần thay thế là
```cpp
while (!op.empty() && priority(op.top()) >= priority(cur_op))
```
thành
```cpp
while (!op.empty() && (
        (left_assoc(cur_op) && priority(op.top()) >= priority(cur_op)) ||
        (!left_assoc(cur_op) && priority(op.top()) > priority(cur_op))
    ))
```
trong đó `left_assoc` là một hàm quyết định xem một toán tử có phải là kết hợp trái hay không.

Đây là phần triển khai cho các toán tử hai ngôi $+$ $-$ $*$ $/$ và các toán tử một ngôi $+$ và $-$.

```{.cpp file=expression_parsing_unary}
bool delim(char c) {
    return c == ' ';
}

bool is_op(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

bool is_unary(char c) {
    return c == '+' || c=='-';
}

int priority (char op) {
    if (op < 0) // unary operator
        return 3;
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return -1;
}

void process_op(stack<int>& st, char op) {
    if (op < 0) {
        int l = st.top(); st.pop();
        switch (-op) {
            case '+': st.push(l); break;
            case '-': st.push(-l); break;
        }
    } else {
        int r = st.top(); st.pop();
        int l = st.top(); st.pop();
        switch (op) {
            case '+': st.push(l + r); break;
            case '-': st.push(l - r); break;
            case '*': st.push(l * r); break;
            case '/': st.push(l / r); break;
        }
    }
}

int evaluate(string& s) {
    stack<int> st;
    stack<char> op;
    bool may_be_unary = true;
    for (int i = 0; i < (int)s.size(); i++) {
        if (delim(s[i]))
            continue;
        
        if (s[i] == '(') {
            op.push('(');
            may_be_unary = true;
        } else if (s[i] == ')') {
            while (op.top() != '(') {
                process_op(st, op.top());
                op.pop();
            }
            op.pop();
            may_be_unary = false;
        } else if (is_op(s[i])) {
            char cur_op = s[i];
            if (may_be_unary && is_unary(cur_op))
                cur_op = -cur_op;
            while (!op.empty() && (
                    (cur_op >= 0 && priority(op.top()) >= priority(cur_op)) ||
                    (cur_op < 0 && priority(op.top()) > priority(cur_op))
                )) {
                process_op(st, op.top());
                op.pop();
            }
            op.push(cur_op);
            may_be_unary = true;
        } else {
            int number = 0;
            while (i < (int)s.size() && isalnum(s[i]))
                number = number * 10 + s[i++] - '0';
            --i;
            st.push(number);
            may_be_unary = false;
        }
    }

    while (!op.empty()) {
        process_op(st, op.top());
        op.pop();
    }
    return st.top();
}
```