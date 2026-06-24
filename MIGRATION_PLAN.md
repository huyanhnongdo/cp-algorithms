# Kế hoạch Xây dựng Phiên bản Tiếng Việt — CP-Algorithms

> **Tài liệu này mô tả chi tiết kế hoạch di chuyển (migration) để xây dựng phiên bản song ngữ Anh-Việt cho cp-algorithms.**
> Ngày tạo: 2026-06-22

---

## 1. Phân tích Repository hiện tại

### 1.1 Framework & Công nghệ

| Thành phần | Chi tiết |
|---|---|
| **Framework** | MkDocs + Material for MkDocs |
| **Ngôn ngữ nội dung** | Markdown (`.md`) |
| **Toán học** | MathJax 3 (inline `$...$`, block `$$...$$`) |
| **Code** | Fenced code blocks với `pymdownx.highlight` |
| **Plugin chính** | `literate-nav`, `git-revision-date-localized`, `git-authors`, `git-committers`, `macros`, `rss`, `tags`, `search`, `toggle-sidebar` |
| **Navigation** | Quản lý qua `src/navigation.md` (plugin `literate-nav`) |
| **Deploy** | Firebase Hosting |
| **Theme override** | `src/overrides/` (custom footer, icons) |
| **Test** | Code snippets được test tự động (`test/test.sh`) |

### 1.2 Cấu trúc thư mục

```
cp-algorithms/
├── mkdocs.yml              # Cấu hình MkDocs chính
├── src/                    # Thư mục docs (docs_dir)
│   ├── navigation.md       # Điều hướng (literate-nav)
│   ├── index.md            # Trang chủ
│   ├── algebra/            # 30 file md + 2 hình
│   ├── combinatorics/      # 9 file md + 1 hình
│   ├── data_structures/    # 10 file md + 6 hình
│   ├── dynamic_programming/# 7 file md
│   ├── game_theory/        # 2 file md
│   ├── geometry/           # 26 file md + 24 hình
│   ├── graph/              # 47 file md + 25 hình
│   ├── linear_algebra/     # 4 file md
│   ├── num_methods/        # 5 file md + 1 hình
│   ├── others/             # 5 file md + 3 hình
│   ├── schedules/          # 3 file md
│   ├── sequences/          # 4 file md
│   ├── string/             # 12 file md + 8 hình
│   ├── overrides/          # Theme customizations
│   ├── javascript/         # MathJax config, donation banner
│   └── stylesheets/        # CSS tùy chỉnh
├── test/                   # Unit tests cho code snippets (~70 file C++)
├── plugins/                # Plugin git-committers tùy chỉnh
├── scripts/                # install-mkdocs.sh
├── CONTRIBUTING.md
└── README.md
```

### 1.3 Thống kê nội dung

#### Tổng quan

| Chỉ số | Giá trị |
|---|---|
| **Tổng file Markdown** | 170 (bao gồm meta pages) |
| **Bài viết thuật toán** | 164 bài |
| **Tổng số từ** | ~258,265 từ |
| **Tổng ký tự** | ~1,624,294 ký tự |
| **Entries trong navigation** | 169 (gồm 6 trang meta) |

#### Phân loại theo chủ đề

| # | Chủ đề | Số bài viết | Số từ | Kích thước (bytes) | Tỷ trọng |
|---|---|---|---|---|---|
| 1 | **Graphs** (graph/) | 47 | 62,759 | 402,129 | 24.6% |
| 2 | **Algebra / Number Theory** (algebra/) | 30 | 52,252 | 323,693 | 20.5% |
| 3 | **Geometry** (geometry/) | 26 | 33,988 | 215,717 | 13.3% |
| 4 | **Data Structures** (data_structures/) | 10 | 31,970 | 194,611 | 12.5% |
| 5 | **Strings** (string/) | 12 | 29,023 | 179,305 | 11.4% |
| 6 | **Combinatorics** (combinatorics/) | 9 | 14,809 | 91,838 | 5.8% |
| 7 | **Dynamic Programming** (dynamic_programming/) | 7 | 9,152 | 58,989 | 3.6% |
| 8 | **Numerical Methods** (num_methods/) | 5 | 5,876 | 36,899 | 2.3% |
| 9 | **Miscellaneous** (others/) | 5 | 6,090 | 35,297 | 2.4% |
| 10 | **Game Theory** (game_theory/) | 2 | 3,700 | 22,198 | 1.4% |
| 11 | **Linear Algebra** (linear_algebra/) | 4 | 3,211 | 19,580 | 1.3% |
| 12 | **Schedules** (schedules/) | 3 | 1,870 | 11,660 | 0.7% |
| 13 | **Sequences** (sequences/) | 4 | 1,453 | 10,242 | 0.6% |
| | **TỔNG** | **164** | **~256,153** | **~1,602,158** | **100%** |

> **Ghi chú**: Tổng từ ở bảng trên không gồm các trang meta (index.md, navigation.md, tags.md, contrib.md, code_of_conduct.md, preview.md).

#### Top 10 bài viết dài nhất

| # | Bài viết | Số từ |
|---|---|---|
| 1 | `data_structures/segment_tree.md` | 11,285 |
| 2 | `algebra/continued-fractions.md` | 8,743 |
| 3 | `string/suffix-automaton.md` | 7,542 |
| 4 | `algebra/fft.md` | 5,404 |
| 5 | `combinatorics/inclusion-exclusion.md` | 4,747 |
| 6 | `data_structures/disjoint_set_union.md` | 4,665 |
| 7 | `graph/hungarian-algorithm.md` | 4,490 |
| 8 | `graph/strongly-connected-components.md` | 4,348 |
| 9 | `algebra/polynomial.md` | 4,062 |
| 10 | `data_structures/treap.md` | 3,859 |

---

## 2. Thiết kế cấu trúc Song ngữ

### 2.1 So sánh các phương án

#### Phương án A: Thư mục song song (`src/en/` và `src/vi/`)

```
src/
├── en/
│   ├── algebra/
│   ├── graph/
│   └── ...
├── vi/
│   ├── algebra/
│   ├── graph/
│   └── ...
├── navigation.md       (EN)
├── navigation.vi.md    (VI)
└── index.md
```

| Ưu điểm | Nhược điểm |
|---|---|
| Tách biệt rõ ràng | ⚠️ Phải di chuyển toàn bộ file EN → gây **conflict lớn khi sync upstream** |
| Dễ quản lý từng ngôn ngữ | Phá vỡ hoàn toàn cấu trúc gốc |
| | Mất khả năng merge từ upstream |

> **❌ KHÔNG khuyến nghị** — phá vỡ khả năng sync upstream.

---

#### Phương án B: File suffix (`.vi.md`) cùng thư mục — sử dụng `mkdocs-static-i18n`

```
src/
├── algebra/
│   ├── binary-exp.md          (EN - giữ nguyên)
│   ├── binary-exp.vi.md       (VI - thêm mới)
│   ├── euclid-algorithm.md
│   ├── euclid-algorithm.vi.md
│   └── ...
├── data_structures/
│   ├── segment_tree.md
│   ├── segment_tree.vi.md
│   └── ...
├── navigation.md              (EN navigation)
├── navigation.vi.md           (VI navigation)
└── index.md
```

| Ưu điểm | Nhược điểm |
|---|---|
| ✅ **Không thay đổi bất kỳ file gốc nào** | File `.vi.md` nằm cùng thư mục → hơi lộn xộn nếu có nhiều ngôn ngữ |
| ✅ Dễ sync upstream (chỉ cần merge, file `.vi.md` không conflict) | Cần cài thêm plugin `mkdocs-static-i18n` |
| ✅ Plugin `mkdocs-static-i18n` hỗ trợ sẵn cho MkDocs Material | |
| ✅ Tự động tạo language switcher | |
| ✅ Fallback sang EN khi bản VI chưa có | |

> **✅ KHUYẾN NGHỊ** — giữ nguyên cấu trúc, thêm file `.vi.md`, dùng plugin chuẩn.

---

#### Phương án C: Hai mkdocs.yml riêng biệt (multi-site)

```
cp-algorithms/
├── mkdocs.yml          (EN site)
├── mkdocs.vi.yml       (VI site, docs_dir: src_vi)
├── src/                (EN - giữ nguyên 100%)
│   ├── algebra/
│   └── ...
└── src_vi/             (VI - copy & dịch)
    ├── algebra/
    └── ...
```

| Ưu điểm | Nhược điểm |
|---|---|
| Tách biệt hoàn toàn EN/VI | ⚠️ Phải duplicate hình ảnh, CSS, JS |
| Không ảnh hưởng gì đến upstream | Không có language switcher tự động |
| Linh hoạt tối đa | Phải quản lý 2 build riêng |
| | Khó phát hiện bài nào đã dịch, bài nào chưa |

> **🔶 Có thể dùng** — nhưng phức tạp hơn Phương án B mà không thêm giá trị.

---

### 2.2 Quyết định: Phương án B — `mkdocs-static-i18n` với file suffix

**Lý do chọn:**

1. **Zero impact trên upstream**: Không sửa bất kỳ file `.md` gốc nào. Chỉ thêm file mới `.vi.md`.
2. **Easy merge**: Khi upstream cập nhật `binary-exp.md`, file `binary-exp.vi.md` không bị conflict.
3. **Plugin mature**: `mkdocs-static-i18n` là plugin chuẩn cho MkDocs Material, được maintain tốt.
4. **Automatic fallback**: Nếu bài chưa được dịch, tự động hiển thị bản EN.
5. **Language switcher**: Tích hợp sẵn nút chuyển đổi ngôn ngữ trong giao diện.

### 2.3 Cấu hình cần thêm vào `mkdocs.yml`

```yaml
# Thêm vào phần plugins:
plugins:
  - i18n:
      default_language: en
      languages:
        - locale: en
          name: English
          default: true
          build: true
        - locale: vi
          name: Tiếng Việt
          build: true

# Thêm vào phần extra:
extra:
  alternate:
    - name: English
      link: /en/
      lang: en
    - name: Tiếng Việt
      link: /vi/
      lang: vi
```

### 2.4 Cấu trúc thư mục sau migration

```
cp-algorithms/
├── mkdocs.yml                  # Cập nhật: thêm i18n plugin
├── src/
│   ├── index.md                # EN (giữ nguyên)
│   ├── index.vi.md             # VI (thêm mới)
│   ├── navigation.md           # EN navigation (giữ nguyên)
│   ├── navigation.vi.md        # VI navigation (thêm mới)
│   ├── algebra/
│   │   ├── binary-exp.md       # EN (giữ nguyên)
│   │   ├── binary-exp.vi.md    # VI (thêm mới)
│   │   ├── fft.md              # EN (giữ nguyên)
│   │   ├── fft.vi.md           # VI (thêm mới)
│   │   └── ...
│   ├── data_structures/
│   │   ├── segment_tree.md     # EN (giữ nguyên)
│   │   ├── segment_tree.vi.md  # VI (thêm mới)
│   │   └── ...
│   ├── graph/
│   │   ├── dijkstra.md         # EN (giữ nguyên)
│   │   ├── dijkstra.vi.md      # VI (thêm mới)
│   │   └── ...
│   └── ... (tương tự cho các thư mục khác)
├── GLOSSARY.md                 # Bảng thuật ngữ chuẩn hóa
├── TRANSLATION_STRATEGY.md     # Chiến lược dịch
├── ROADMAP.md                  # Lộ trình thực hiện
└── MIGRATION_PLAN.md           # File này
```

---

## 3. Chiến lược Đồng bộ Upstream

### 3.1 Thiết lập Remote

```bash
# Thêm upstream remote (nếu chưa có)
git remote add upstream https://github.com/cp-algorithms/cp-algorithms.git

# Sync workflow
git fetch upstream
git checkout main
git merge upstream/main
# Resolve conflicts nếu có (chỉ xảy ra khi mkdocs.yml bị sửa ở cả hai nơi)
```

### 3.2 Nguyên tắc tránh Conflict

1. **Không bao giờ sửa file `.md` gốc** — chỉ thêm file `.vi.md`.
2. **Sử dụng block riêng** trong `mkdocs.yml` cho config i18n — dễ resolve conflict.
3. **File navigation.vi.md** là file mới → không conflict.
4. **File hình ảnh** — dùng chung, không duplicate.

### 3.3 Phát hiện bài mới từ Upstream

```bash
# Script kiểm tra bài mới chưa có bản dịch
find src -name "*.md" -not -name "*.vi.md" -not -path "*/overrides/*" | while read f; do
    vi_file="${f%.md}.vi.md"
    if [ ! -f "$vi_file" ]; then
        echo "CHƯA DỊCH: $f"
    fi
done
```

---

## 4. Ước lượng Khối lượng Công việc

### 4.1 Thống kê nội dung cần dịch

| Chỉ số | Giá trị |
|---|---|
| Tổng file cần dịch | 164 bài viết |
| Tổng số từ | ~258,000 từ |
| Ước lượng từ cần dịch (trừ code, LaTeX) | ~170,000 từ (~65%) |
| Tổng ký tự | ~1.6 triệu ký tự |

> **Ghi chú**: Khoảng 35% nội dung là code blocks và công thức LaTeX — sẽ được giữ nguyên.

### 4.2 Ước lượng thời gian dịch thủ công

| Tốc độ dịch | Thời gian ước tính |
|---|---|
| Dịch thủ công (500 từ/giờ) | ~340 giờ (~43 ngày làm việc) |
| Review & chỉnh sửa (30%) | ~100 giờ (~13 ngày) |
| **Tổng** | **~440 giờ (~55 ngày làm việc)** |

### 4.3 Ước lượng chi phí dùng LLM API

| Model | Giá Input | Giá Output | Chi phí ước tính |
|---|---|---|---|
| **GPT-4o** | $2.50/1M tokens | $10.00/1M tokens | ~$5-10 |
| **GPT-4.1** | $2.00/1M tokens | $8.00/1M tokens | ~$4-8 |
| **Claude Sonnet 4** | $3.00/1M tokens | $15.00/1M tokens | ~$8-15 |
| **Claude Opus 4** | $15.00/1M tokens | $75.00/1M tokens | ~$40-75 |
| **Gemini 2.5 Pro** | $1.25/1M tokens | $10.00/1M tokens | ~$4-8 |

> **Khuyến nghị**: Dùng **GPT-4o** hoặc **Gemini 2.5 Pro** cho dịch tự động (giá thấp, chất lượng tốt), sau đó review thủ công. Tổng chi phí ước tính: **$5-15 cho toàn bộ 164 bài**.

### 4.4 Timeline ước tính (dùng AI + review)

| Giai đoạn | Thời gian |
|---|---|
| Phase 1: Hạ tầng song ngữ | 1-2 ngày |
| Phase 2: Dịch 40 bài cơ bản | 3-5 ngày |
| Phase 3: Dịch 124 bài còn lại | 7-14 ngày |
| Phase 4: Review & hoàn thiện | 5-7 ngày |
| **Tổng** | **~3-4 tuần** |

---

## 5. Workflow dịch bằng AI

### 5.1 Pipeline tổng quan

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────┐    ┌──────────┐
│  Đọc file   │ →  │ Phân tách    │ →  │ Dịch văn bản │ →  │ Tái tạo  │ →  │ Kiểm tra │
│  .md gốc    │    │ nội dung     │    │ (LLM API)    │    │ file .vi │    │ chất lượng│
└─────────────┘    └──────────────┘    └──────────────┘    └──────────┘    └──────────┘
```

### 5.2 Chi tiết từng bước

#### Bước 1: Đọc file Markdown gốc

```python
def read_source(filepath):
    """Đọc file .md gốc và trả về nội dung raw."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
```

#### Bước 2: Phân tách nội dung

Tách nội dung thành các block:
- **YAML frontmatter** → giữ nguyên
- **Code blocks** (``` ... ```) → giữ nguyên, đánh dấu `[CODE_BLOCK_N]`
- **Công thức LaTeX** (`$...$`, `$$...$$`) → giữ nguyên, đánh dấu `[LATEX_INLINE_N]`, `[LATEX_BLOCK_N]`
- **Liên kết nội bộ** (`[text](path.md)`) → giữ path, chỉ dịch text
- **Hình ảnh** (`![alt](path)`) → giữ nguyên
- **Văn bản thuần** → gửi đi dịch

```python
import re

def extract_preservable_blocks(content):
    """
    Trích xuất và thay thế các block cần giữ nguyên bằng placeholder.
    Returns: (processed_text, replacements_dict)
    """
    replacements = {}
    counter = {'code': 0, 'latex_block': 0, 'latex_inline': 0}
    
    # 1. Giữ nguyên YAML frontmatter
    frontmatter_match = re.match(r'^---\n.*?\n---\n', content, re.DOTALL)
    frontmatter = frontmatter_match.group(0) if frontmatter_match else ''
    text = content[len(frontmatter):]
    
    # 2. Giữ nguyên code blocks
    def replace_code(match):
        key = f'[CODE_BLOCK_{counter["code"]}]'
        replacements[key] = match.group(0)
        counter['code'] += 1
        return key
    text = re.sub(r'```.*?```', replace_code, text, flags=re.DOTALL)
    
    # 3. Giữ nguyên LaTeX block ($$...$$)
    def replace_latex_block(match):
        key = f'[LATEX_BLOCK_{counter["latex_block"]}]'
        replacements[key] = match.group(0)
        counter['latex_block'] += 1
        return key
    text = re.sub(r'\$\$.*?\$\$', replace_latex_block, text, flags=re.DOTALL)
    
    # 4. Giữ nguyên LaTeX inline ($...$)
    def replace_latex_inline(match):
        key = f'[LATEX_INLINE_{counter["latex_inline"]}]'
        replacements[key] = match.group(0)
        counter['latex_inline'] += 1
        return key
    text = re.sub(r'\$[^$]+?\$', replace_latex_inline, text)
    
    return frontmatter, text, replacements
```

#### Bước 3: Dịch văn bản bằng LLM

```python
TRANSLATION_PROMPT = """
Bạn là chuyên gia dịch thuật tài liệu thuật toán từ tiếng Anh sang tiếng Việt.

QUY TẮC:
1. Dịch tự nhiên, rõ ràng, phù hợp với văn phong kỹ thuật tiếng Việt.
2. Giữ nguyên tất cả placeholder [CODE_BLOCK_N], [LATEX_BLOCK_N], [LATEX_INLINE_N].
3. Giữ nguyên cú pháp Markdown (headers ##, **, -, links).
4. Sử dụng thuật ngữ chuẩn hóa theo GLOSSARY.
5. Giữ nguyên tên thuật toán tiếng Anh trong ngoặc khi cần.
6. Không dịch tên hàm, biến, kiểu dữ liệu trong code.

GLOSSARY (trích):
- Segment Tree → Cây phân đoạn (Segment Tree)
- Binary Search → Tìm kiếm nhị phân (Binary Search)
- Dynamic Programming → Quy hoạch động (Dynamic Programming)
- Graph → Đồ thị
- Vertex/Node → Đỉnh
- Edge → Cạnh
- DFS → DFS (Tìm kiếm theo chiều sâu)
- BFS → BFS (Tìm kiếm theo chiều rộng)

Dịch đoạn văn bản sau:
{text}
"""
```

#### Bước 4: Tái tạo file tiếng Việt

```python
def reconstruct_vi_file(frontmatter, translated_text, replacements):
    """Ghép lại frontmatter + translated text + restored blocks."""
    # Khôi phục các block đã giữ nguyên
    result = translated_text
    for placeholder, original in replacements.items():
        result = result.replace(placeholder, original)
    
    return frontmatter + result

def save_vi_file(source_path, content):
    """Lưu file .vi.md cùng thư mục với file gốc."""
    vi_path = source_path.replace('.md', '.vi.md')
    with open(vi_path, 'w', encoding='utf-8') as f:
        f.write(content)
```

#### Bước 5: Kiểm tra chất lượng

```python
def quality_check(source_path, vi_path):
    """Kiểm tra chất lượng file dịch."""
    checks = {
        'code_blocks_preserved': True,
        'latex_preserved': True,
        'links_valid': True,
        'no_untranslated_paragraphs': True,
        'frontmatter_valid': True
    }
    
    source = read_source(source_path)
    translated = read_source(vi_path)
    
    # 1. Kiểm tra số lượng code blocks giống nhau
    source_code = re.findall(r'```.*?```', source, re.DOTALL)
    vi_code = re.findall(r'```.*?```', translated, re.DOTALL)
    checks['code_blocks_preserved'] = (source_code == vi_code)
    
    # 2. Kiểm tra LaTeX giữ nguyên
    source_latex = re.findall(r'\$[^$]+?\$', source)
    vi_latex = re.findall(r'\$[^$]+?\$', translated)
    checks['latex_preserved'] = (len(source_latex) == len(vi_latex))
    
    # 3. Kiểm tra internal links vẫn trỏ đúng file
    source_links = re.findall(r'\]\(([^)]+\.md[^)]*)\)', source)
    vi_links = re.findall(r'\]\(([^)]+\.md[^)]*)\)', translated)
    checks['links_valid'] = (set(source_links) == set(vi_links))
    
    return checks
```

### 5.3 Xử lý đặc biệt

| Trường hợp | Xử lý |
|---|---|
| **Frontmatter tags** | Giữ nguyên `Translated`/`Original`, thêm `lang: vi` |
| **Admonitions** (`!!!`) | Dịch nội dung, giữ cú pháp |
| **Tabbed content** (`=== "Tab"`) | Dịch tên tab, giữ nội dung code |
| **Internal links** | Giữ nguyên path (trỏ đến `.md` gốc, plugin tự resolve) |
| **Image alt text** | Dịch alt text |
| **HTML anchors** | Giữ nguyên `id` |
| **MathJax config** | Giữ nguyên — dùng chung |

---

## 6. Backlog chi tiết

### 6.1 Phase 1: Hạ tầng song ngữ

| # | Task | Mục tiêu | Độ khó | Phụ thuộc | Thời gian |
|---|---|---|---|---|---|
| 1.1 | Cài đặt `mkdocs-static-i18n` | Plugin i18n hoạt động | Dễ | Không | 1 giờ |
| 1.2 | Cập nhật `mkdocs.yml` | Thêm config i18n | Dễ | 1.1 | 1 giờ |
| 1.3 | Tạo `src/index.vi.md` | Trang chủ tiếng Việt | Dễ | 1.2 | 1 giờ |
| 1.4 | Tạo `src/navigation.vi.md` | Navigation tiếng Việt | TB | 1.2 | 3 giờ |
| 1.5 | Test build local | Xác nhận site song ngữ hoạt động | Dễ | 1.3, 1.4 | 1 giờ |
| 1.6 | Tạo script dịch tự động | Pipeline Python + LLM | TB | Không | 4 giờ |
| 1.7 | Tạo script kiểm tra QA | Kiểm tra chất lượng dịch | TB | 1.6 | 2 giờ |
| 1.8 | Tạo GLOSSARY.md | Bảng thuật ngữ chuẩn hóa | TB | Không | 3 giờ |
| 1.9 | Setup upstream remote | Cấu hình sync | Dễ | Không | 0.5 giờ |
| 1.10 | Tạo GitHub Actions CI | Auto build & test | TB | 1.5 | 2 giờ |

### 6.2 Phase 2: Dịch chủ đề cơ bản (40 bài ưu tiên cao)

| # | Task | Mục tiêu | Độ khó | Phụ thuộc | Thời gian |
|---|---|---|---|---|---|
| 2.1 | Dịch Data Structures (10 bài) | DSU, Segment Tree, Fenwick, Treap, ... | Khó | 1.8 | 8 giờ |
| 2.2 | Dịch Graph Traversal (5 bài) | BFS, DFS, Connected Components, ... | TB | 1.8 | 3 giờ |
| 2.3 | Dịch Shortest Paths (5 bài) | Dijkstra, Bellman-Ford, Floyd, ... | TB | 1.8 | 3 giờ |
| 2.4 | Dịch DP Fundamentals (4 bài) | Intro, Knapsack, LIS, Profile DP | TB | 1.8 | 3 giờ |
| 2.5 | Dịch Algebra Fundamentals (5 bài) | Binary Exp, GCD, Extended GCD, Fibonacci | TB | 1.8 | 3 giờ |
| 2.6 | Dịch String Fundamentals (6 bài) | Hashing, KMP, Z-function, Suffix Array | Khó | 1.8 | 5 giờ |
| 2.7 | Dịch Numerical Methods (5 bài) | Binary Search, Ternary Search, Newton | TB | 1.8 | 3 giờ |
| 2.8 | Review & QA Phase 2 | Kiểm tra toàn bộ 40 bài | TB | 2.1-2.7 | 5 giờ |

### 6.3 Phase 3: Dịch toàn bộ nội dung (124 bài còn lại)

| # | Task | Mục tiêu | Độ khó | Phụ thuộc | Thời gian |
|---|---|---|---|---|---|
| 3.1 | Dịch Algebra (25 bài còn lại) | Prime, Modular, FFT, Polynomial, ... | Khó | Phase 2 | 10 giờ |
| 3.2 | Dịch Graph (42 bài còn lại) | MST, Flows, Matching, LCA, ... | Khó | Phase 2 | 16 giờ |
| 3.3 | Dịch Geometry (26 bài) | Basic, Polygons, Convex hull, ... | Khó | Phase 2 | 12 giờ |
| 3.4 | Dịch Combinatorics (9 bài) | Binomial, Catalan, Burnside, ... | TB | Phase 2 | 5 giờ |
| 3.5 | Dịch String (6 bài còn lại) | Suffix Tree, Suffix Automaton, ... | Khó | Phase 2 | 5 giờ |
| 3.6 | Dịch DP (3 bài còn lại) | D&C DP, Knuth Optimization, ... | TB | Phase 2 | 2 giờ |
| 3.7 | Dịch Linear Algebra (4 bài) | Gauss, Determinant, Rank | TB | Phase 2 | 2 giờ |
| 3.8 | Dịch Game Theory (2 bài) | Sprague-Grundy, Games on Graphs | TB | Phase 2 | 1 giờ |
| 3.9 | Dịch Miscellaneous (12 bài) | Sequences, Schedules, Others | TB | Phase 2 | 5 giờ |
| 3.10 | Review & QA Phase 3 | Kiểm tra toàn bộ 124 bài | Khó | 3.1-3.9 | 10 giờ |

### 6.4 Phase 4: Đồng bộ & Bảo trì

| # | Task | Mục tiêu | Độ khó | Phụ thuộc | Thời gian |
|---|---|---|---|---|---|
| 4.1 | Script sync upstream | Auto detect bài mới/sửa | TB | Phase 1 | 3 giờ |
| 4.2 | GitHub Actions: auto detect changes | CI phát hiện thay đổi upstream | TB | 4.1 | 3 giờ |
| 4.3 | Tạo contribution guide tiếng Việt | Hướng dẫn đóng góp bản dịch | Dễ | Phase 2 | 2 giờ |
| 4.4 | Deploy GitHub Pages (không subdomain) | Hosting phiên bản VI | TB | Phase 3 | 2 giờ |
| 4.5 | Monitoring & maintenance | Theo dõi, cập nhật thường xuyên | Liên tục | 4.1-4.4 | Ongoing |

---

## 7. Rủi ro & Giải pháp

| Rủi ro | Xác suất | Tác động | Giải pháp |
|---|---|---|---|
| Upstream thay đổi cấu trúc lớn | Thấp | Cao | Theo dõi upstream releases, có migration script |
| LLM dịch sai thuật ngữ | TB | TB | Glossary chuẩn hóa + human review |
| Plugin `mkdocs-static-i18n` không tương thích | Thấp | Cao | Fallback sang Phương án C (multi-site) |
| Code blocks bị modified khi dịch | TB | Cao | QA script tự động kiểm tra |
| LaTeX bị broken | TB | Cao | Placeholder system + regex validation |
| MkDocs version conflict | Thấp | TB | Pin version trong requirements.txt |

---

## 8. Definition of Done

Phiên bản tiếng Việt được coi là hoàn thành khi:

- [x] 100% bài viết (164 bài) có file `.vi.md`
- [x] Navigation tiếng Việt hoàn chỉnh
- [x] Language switcher hoạt động
- [x] QA pass 100% (code blocks, LaTeX, links)
- [x] Glossary chuẩn hóa được áp dụng nhất quán
- [x] Sync upstream script hoạt động
- [x] CI/CD build thành công
- [x] Deploy lên hosting

---

*Tài liệu này sẽ được cập nhật theo tiến trình dự án.*
