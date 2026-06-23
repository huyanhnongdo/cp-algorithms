---
tags:
  - Translated
e_maxx_link: rmq
lang: vi
---
# Truy vấn giá trị nhỏ nhất trên đoạn (Range Minimum Query)

Bạn được cho một mảng $A[1..N]$.
Bạn cần trả lời các truy vấn dạng $(L, R)$, yêu cầu tìm phần tử nhỏ nhất trong mảng $A$ giữa các vị trí $L$ và $R$ (bao gồm cả hai vị trí này).

RMQ (Truy vấn giá trị nhỏ nhất trên đoạn) có thể xuất hiện trực tiếp trong các bài toán hoặc được áp dụng trong một số bài toán khác, ví dụ như bài toán [Tổ tiên chung gần nhất (LCA)](../graph/lca.md).

## Giải pháp

Có rất nhiều cách tiếp cận và cấu trúc dữ liệu khác nhau mà bạn có thể sử dụng để giải quyết bài toán RMQ.

Các phương pháp được giải thích trên trang này được liệt kê dưới đây.

Đầu tiên là các phương pháp cho phép sửa đổi mảng giữa các lần truy vấn:

- [Chia căn (Sqrt Decomposition)](../data_structures/sqrt_decomposition.md) - trả lời mỗi truy vấn trong $O(\sqrt{N})$, tiền xử lý mất $O(N)$.
  Ưu điểm: cấu trúc dữ liệu rất đơn giản. Nhược điểm: độ phức tạp kém hơn.
- [Cây phân đoạn (Segment Tree)](../data_structures/segment_tree.md) - trả lời mỗi truy vấn trong $O(\log N)$, tiền xử lý mất $O(N)$.
  Ưu điểm: độ phức tạp thời gian tốt. Nhược điểm: lượng code lớn hơn so với các cấu trúc dữ liệu khác.
- [Cây Fenwick (BIT)](../data_structures/fenwick.md) - trả lời mỗi truy vấn trong $O(\log N)$, tiền xử lý mất $O(N \log N)$.
  Ưu điểm: code ngắn nhất, độ phức tạp thời gian tốt. Nhược điểm: Cây Fenwick chỉ có thể sử dụng cho các truy vấn với $L = 1$, vì vậy nó không áp dụng được cho nhiều bài toán.

Và dưới đây là các phương pháp chỉ hoạt động trên mảng tĩnh, nghĩa là bạn không thể thay đổi giá trị trong mảng mà không tính toán lại toàn bộ cấu trúc dữ liệu:

- [Bảng thưa (Sparse Table)](../data_structures/sparse-table.md) - trả lời mỗi truy vấn trong $O(1)$, tiền xử lý mất $O(N \log N)$.
  Ưu điểm: cấu trúc dữ liệu đơn giản, độ phức tạp thời gian tuyệt vời.
- [Cây căn (Sqrt Tree)](../data_structures/sqrt-tree.md) - trả lời các truy vấn trong $O(1)$, tiền xử lý mất $O(N \log \log N)$. Ưu điểm: nhanh. Nhược điểm: khó cài đặt.
- [Hợp nhất tập rời rạc (DSU) / Mẹo của Arpa](../data_structures/disjoint_set_union.md#arpa) - trả lời các truy vấn trong $O(1)$, tiền xử lý trong $O(n)$. Ưu điểm: ngắn, nhanh. Nhược điểm: chỉ hoạt động nếu tất cả các truy vấn đều biết trước, tức là chỉ hỗ trợ xử lý ngoại tuyến (off-line) các truy vấn.
- [Cây Cartesian](../graph/rmq_linear.md) và [Thuật toán Farach-Colton và Bender](../graph/lca_farachcoltonbender.md) - trả lời các truy vấn trong $O(1)$, tiền xử lý trong $O(n)$. Ưu điểm: độ phức tạp tối ưu. Nhược điểm: lượng code lớn.

Lưu ý: Tiền xử lý (Preprocessing) là việc xử lý sơ bộ mảng đã cho bằng cách xây dựng cấu trúc dữ liệu tương ứng cho nó.

## Các bài tập luyện tập
- [SPOJ: Range Minimum Query](http://www.spoj.com/problems/RMQSQ/)
- [CODECHEF: Chef And Array](https://www.codechef.com/problems/FRMQ)
- [Codeforces: Array Partition](https://codeforces.com/contest/1454/problem/F)