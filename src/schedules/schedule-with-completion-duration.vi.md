---
tags:
  - Translated
e_maxx_link: schedule_with_completion_duration
lang: vi
---
# Lập lịch công việc tối ưu với thời hạn và thời lượng cho trước

Giả sử chúng ta có một tập hợp các công việc, và chúng ta biết thời hạn (deadline) cũng như thời lượng (duration) của mỗi công việc. Việc thực hiện một công việc không thể bị gián đoạn trước khi hoàn thành. Yêu cầu đặt ra là tạo ra một lịch trình để hoàn thành được số lượng công việc lớn nhất.

## Giải thuật

Thuật toán giải quyết bài toán này mang tính **tham lam (Greedy)**. Hãy sắp xếp tất cả các công việc theo thời hạn của chúng và xét theo thứ tự giảm dần. Ngoài ra, hãy tạo một hàng đợi $q$, nơi chúng ta sẽ lần lượt đưa các công việc vào và lấy ra công việc có thời gian thực hiện ngắn nhất (ví dụ, chúng ta có thể sử dụng `set` hoặc `priority_queue`). Ban đầu, $q$ rỗng.

Giả sử chúng ta đang xét công việc thứ $i$. Trước hết, hãy đưa nó vào $q$. Hãy xem xét khoảng thời gian giữa thời hạn của công việc thứ $i$ và thời hạn của công việc thứ $i-1$. Đó là một đoạn có độ dài $T$. Chúng ta sẽ lấy các công việc ra từ $q$ (theo thứ tự tăng dần của thời gian thực hiện còn lại) và thực hiện chúng cho đến khi toàn bộ đoạn $T$ được lấp đầy. Lưu ý: nếu tại bất kỳ thời điểm nào, công việc được lấy ra chỉ có thể thực hiện một phần cho đến khi đoạn $T$ được lấp đầy, thì chúng ta chỉ thực hiện công việc đó một phần xa nhất có thể, tức là trong khoảng thời gian $T$, và đưa phần còn lại của công việc đó trở lại $q$.

Khi thuật toán kết thúc, chúng ta sẽ chọn được lời giải tối ưu (hoặc ít nhất là một trong số các lời giải tối ưu). Độ phức tạp thời gian của thuật toán là $O(n \log n)$.

## Cài đặt

Hàm dưới đây nhận đầu vào là một `vector` chứa các công việc (bao gồm thời hạn, thời lượng và chỉ số của công việc) và tính toán một `vector` chứa tất cả các chỉ số của các công việc được sử dụng trong lịch trình tối ưu.
Lưu ý rằng bạn vẫn cần sắp xếp các công việc này theo thời hạn nếu muốn viết ra kế hoạch chi tiết.

```{.cpp file=schedule_deadline_duration}
struct Job {
    int deadline, duration, idx;

    bool operator<(Job o) const {
        return deadline < o.deadline;
    }
};

vector<int> compute_schedule(vector<Job> jobs) {
    sort(jobs.begin(), jobs.end());

    set<pair<int,int>> s;
    vector<int> schedule;
    for (int i = jobs.size()-1; i >= 0; i--) {
        int t = jobs[i].deadline - (i ? jobs[i-1].deadline : 0);
        s.insert(make_pair(jobs[i].duration, jobs[i].idx));
        while (t && !s.empty()) {
            auto it = s.begin();
            if (it->first <= t) {
                t -= it->first;
                schedule.push_back(it->second);
            } else {
                s.insert(make_pair(it->first - t, it->second));
                t = 0;
            }
            s.erase(it);
        }
    }
    return schedule;
}
```