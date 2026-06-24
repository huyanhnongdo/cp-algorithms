# Hướng dẫn Đóng góp (Contributing Guide) - CP-Algorithms Tiếng Việt

Chào mừng bạn đến với dự án dịch thuật CP-Algorithms sang Tiếng Việt! Mọi đóng góp của bạn — dù là sửa một lỗi chính tả, cải thiện câu từ dịch thuật hay dịch các bài viết mới — đều cực kỳ quý giá cho cộng đồng lập trình thi đấu tại Việt Nam.

Dưới đây là hướng dẫn chi tiết cách tham gia đóng góp cho dự án.

---

## Quy trình Đóng góp Cơ bản

Chúng tôi quản lý các thay đổi thông qua hệ thống Pull Request (PR) trên GitHub:

1. **Fork dự án**: Fork repository này về tài khoản GitHub cá nhân của bạn.
2. **Clone về máy local**:
   ```bash
   git clone --recursive https://github.com/YOUR_USERNAME/cp-algorithms.git
   cd cp-algorithms
   ```
3. **Cài đặt môi trường kiểm tra**:
   ```bash
   scripts/install-mkdocs.sh
   ```
4. **Tạo nhánh mới**:
   ```bash
   git checkout -b feature/translate-my-article
   ```
5. **Thực hiện thay đổi**: Thực hiện dịch thuật hoặc sửa đổi tệp `.vi.md`.
6. **Chạy QA check cục bộ**:
   ```bash
   python3 scripts/qa_check.py src/path/to/english.md src/path/to/vietnamese.vi.md
   ```
7. **Commit và Push**:
   ```bash
   git add .
   git commit -m "Dịch bài viết ABC sang tiếng Việt"
   git push origin feature/translate-my-article
   ```
8. **Tạo Pull Request**: Mở PR từ nhánh của bạn vào nhánh `main` của repository gốc.

---

## Hướng dẫn Quy chuẩn Dịch thuật

Để đảm bảo tính nhất quán và chuyên nghiệp cho toàn bộ trang web, vui lòng tuân thủ các quy tắc sau:

### 1. Nhất quán Thuật ngữ (Glossary)
Vui lòng tham khảo bảng thuật ngữ chuẩn hóa tại [GLOSSARY.md](GLOSSARY.md). 
- Ví dụ: `Segment Tree` dịch thành `Cây phân đoạn`, `Disjoint Set Union` dịch thành `Các tập hợp rời nhau`.
- Đối với thuật ngữ được dịch lần đầu trong bài viết, hãy ghi chú thuật ngữ Tiếng Anh nguyên bản trong ngoặc đơn. Ví dụ: *Cây phân đoạn (Segment Tree)*. Sau đó chỉ cần viết *Cây phân đoạn*.

### 2. Không Thay đổi Code Blocks và LaTeX
- Toàn bộ các đoạn mã nguồn C++ / Java / Python phải được giữ nguyên 100%. Không biên dịch hoặc thay đổi nội dung bên trong các comment code nếu comment đó mang tính kỹ thuật.
- Các công thức toán học LaTeX (nằm giữa `$$...$$` hoặc `$...$`) phải được giữ nguyên cấu trúc để tránh lỗi hiển thị khi build trang web.

### 3. Quy chuẩn xử lý thẻ Ảnh (Image tags)
- Để tránh lỗi 404 hình ảnh khi chuyển đổi qua lại giữa bản Tiếng Anh và Tiếng Việt, mọi tệp hình ảnh phải được định dạng theo cú pháp Markdown: `![Mô tả ảnh](path_to_image.png)`.
- Đặt thẻ ảnh bên trong khối HTML căn giữa có thuộc tính `markdown="1"`:
  ```html
  <div style="text-align: center;" markdown="1">

  ![Mô tả ảnh](path_to_image.png)

  </div>
  ```

---

## Sử dụng Công cụ Tự động

### 1. Dịch bài bằng Script dịch tự động (AI-powered)
Chúng tôi cung cấp script giúp dịch tự động bài viết bằng Gemini API mà vẫn bảo toàn hoàn hảo cấu trúc code block và công thức toán học:

```bash
export GEMINI_API_KEY="your_api_key_here"
python3 scripts/translate.py src/path/to/english_file.md
```

Tệp dịch tương ứng `english_file.vi.md` sẽ tự động được tạo ra.

### 2. Kiểm tra chất lượng (QA check)
Sau khi dịch xong, hãy chạy QA check để đảm bảo không có công thức LaTeX hay khối code nào bị mất mát trong quá trình dịch:

```bash
python3 scripts/qa_check.py src/path/to/english_file.md src/path/to/english_file.vi.md
```

Nếu chạy xong báo `🎉 SUMMARY: ALL QA CHECKS PASSED!` nghĩa là tệp dịch của bạn đã đạt chuẩn cấu trúc!

### 3. Kiểm tra hiển thị cục bộ (Local preview)
Chạy server cục bộ để xem trực quan các thay đổi:
```bash
mkdocs serve
```
Mở trình duyệt truy cập `http://127.0.0.1:8000` và chuyển đổi sang ngôn ngữ Tiếng Việt để xem bài viết của bạn.

---

Cảm ơn bạn đã đồng hành đóng góp xây dựng kho tài liệu thuật toán chất lượng cao cho cộng đồng lập trình Việt Nam!
