# Thuật toán cho Lập trình Thi đấu (CP-Algorithms Tiếng Việt)

Dự án này nhằm mục đích dịch thuật và bản địa hóa kho tài liệu thuật toán nổi tiếng [CP-Algorithms](https://cp-algorithms.com/) (nguồn gốc từ [e-maxx.ru/algo](https://e-maxx.ru/algo)) sang Tiếng Việt. Dự án cung cấp mô tả chi tiết về nhiều thuật toán và cấu trúc dữ liệu phổ biến trong lập trình thi đấu (Competitive Programming) và khoa học máy tính.

Trang web đã biên dịch được xuất bản tại: [https://huyanhnongdo.github.io/cp-algorithms/vi/](https://huyanhnongdo.github.io/cp-algorithms/vi/)

---

## Các Liên kết Hữu ích cho Contributor

- **[Hướng dẫn Đóng góp](CONTRIBUTING.vi.md)**: Quy trình fork, chuẩn dịch thuật, viết công thức LaTeX, xử lý ảnh.
- **[Tiến độ Dịch thuật](src/translation_status.vi.md)**: Theo dõi tiến độ hoàn thành các bài viết.
- **[Bảng Thuật ngữ chuẩn hóa](GLOSSARY.md)**: Các thuật ngữ dịch đã thống nhất.
- **[Trang Xem trước](src/preview.vi.md)**: Công cụ test hiển thị Markdown/MathJax cục bộ.

---

## Cài đặt và Chạy Cục bộ

Nếu bạn muốn chạy thử nghiệm trang web trên máy cá nhân để kiểm tra các bài viết trước khi đóng góp:

1. **Clone repository**:
   ```bash
   git clone --recursive https://github.com/huyanhnongdo/cp-algorithms.git
   cd cp-algorithms
   ```
2. **Cài đặt các gói phụ thuộc (MkDocs và Material Theme)**:
   ```bash
   scripts/install-mkdocs.sh
   ```
3. **Chạy server phát triển**:
   ```bash
   mkdocs serve
   ```
4. **Xem kết quả**: Mở trình duyệt và truy cập `http://127.0.0.1:8000/vi/`.

---

## Công cụ tự động hỗ trợ

Dự án cung cấp các công cụ tự động viết bằng Python nằm trong thư mục `scripts/` giúp giảm tải công việc đóng góp:

- **`scripts/translate.py`**: Tự động dịch một bài viết tiếng Anh sang tiếng Việt bằng Gemini API mà vẫn bảo toàn cấu trúc codeblock và LaTeX.
- **`scripts/qa_check.py`**: Đối chiếu cấu trúc tệp tiếng Anh gốc và tệp dịch tiếng Việt để phát hiện các lỗi sai lệch dòng code hoặc thiếu thẻ LaTeX.
- **`scripts/sync_upstream.py`**: Quét và so sánh kho bài viết gốc `cp-algorithms/cp-algorithms` để tìm ra bài viết mới hoặc bài viết vừa được cập nhật.

---

Cảm ơn tất cả các tình nguyện viên đã tham gia dịch thuật và phát triển dự án này!
