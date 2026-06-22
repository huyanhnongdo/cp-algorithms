# Chiến lược Dịch thuật — CP-Algorithms Tiếng Việt

> **Tài liệu hướng dẫn chiến lược dịch thuật cho dự án cp-algorithms tiếng Việt.**
> Ngày tạo: 2026-06-22

---

## 1. Nguyên tắc Dịch thuật Tổng quát

### 1.1 Văn phong

- **Học thuật nhưng dễ hiểu**: Phù hợp với đối tượng sinh viên CNTT và competitive programmers.
- **Nhất quán**: Sử dụng thuật ngữ thống nhất theo GLOSSARY.md.
- **Chính xác**: Không bỏ sót thông tin, không thêm ý kiến chủ quan.
- **Tự nhiên**: Không dịch máy móc, câu phải tự nhiên trong tiếng Việt.

### 1.2 Những gì PHẢI dịch

| Thành phần | Ví dụ |
|---|---|
| Tiêu đề bài viết | "Segment Tree" → "Cây phân đoạn (Segment Tree)" |
| Văn bản giải thích | Đoạn mô tả thuật toán |
| Alt text hình ảnh | `![Sum Segment Tree]` → `![Cây phân đoạn tổng]` |
| Tên tab nội dung | `=== "Implementation"` → `=== "Cài đặt"` |
| Admonition titles | `!!! note "Note"` → `!!! note "Ghi chú"` |
| Navigation labels | Tên mục trong navigation.vi.md |

### 1.3 Những gì KHÔNG dịch (giữ nguyên 100%)

| Thành phần | Lý do |
|---|---|
| **Code blocks** (``` ... ```) | Code phải chạy được, không dịch |
| **Công thức LaTeX** ($...$, $$...$$) | Toán học là ngôn ngữ quốc tế |
| **Tên biến, hàm trong text** | `build()`, `update()`, `t[v]` — giữ nguyên |
| **Tên thuật toán gốc** (trong ngoặc) | Luôn kèm tên EN sau tên VI |
| **URL, links nội bộ** | Path file không đổi |
| **YAML frontmatter** | Giữ nguyên metadata |
| **HTML anchors** | Giữ `id` cho backward compatibility |
| **Tên file** | File `.vi.md` giữ tên gốc |

### 1.4 Xử lý đặc biệt

| Trường hợp | Cách xử lý | Ví dụ |
|---|---|---|
| Thuật ngữ phổ biến | Dịch + giữ EN trong ngoặc | "Cây phân đoạn (Segment Tree)" |
| Thuật ngữ chưa có dịch chuẩn | Giữ nguyên EN + giải thích | "Treap (cây kết hợp BST và Heap)" |
| Viết tắt quốc tế | Giữ nguyên | DFS, BFS, MST, GCD, LCA |
| Tên người | Giữ nguyên | Dijkstra, Bellman-Ford, Kruskal |
| Tên bài toán nổi tiếng | Giữ EN + dịch mô tả | "Bài toán Josephus (Josephus problem)" |
| Complexity notation | Giữ nguyên | $O(n \log n)$, $O(n^2)$ |

---

## 2. Phân loại Ưu tiên Dịch

### 2.1 Tiêu chí ưu tiên

1. **Tần suất sử dụng** trong competitive programming
2. **Độ phổ biến** trong giáo trình đại học Việt Nam
3. **Tính nền tảng** — bài viết được tham chiếu bởi nhiều bài khác
4. **Độ dài hợp lý** — ưu tiên bài vừa phải trước

### 2.2 Nhóm ưu tiên

#### 🔴 Ưu tiên 1 — Nền tảng (40 bài, dịch trước)

Đây là các bài viết cơ bản nhất, xuất hiện trong hầu hết các khóa học thuật toán và cuộc thi lập trình.

**Data Structures (10 bài — tất cả)**
- `stack_queue_modification.md` — Minimum Stack / Minimum Queue
- `sparse-table.md` — Sparse Table
- `disjoint_set_union.md` — Disjoint Set Union
- `fenwick.md` — Fenwick Tree
- `sqrt_decomposition.md` — Sqrt Decomposition
- `segment_tree.md` — Segment Tree ⭐ (bài dài nhất, quan trọng nhất)
- `treap.md` — Treap
- `sqrt-tree.md` — Sqrt Tree
- `randomized_heap.md` — Randomized Heap
- `deleting_in_log_n.md` — Deleting from a data structure

**Graph Fundamentals (10 bài)**
- `breadth-first-search.md` — BFS
- `depth-first-search.md` — DFS
- `search-for-connected-components.md` — Finding Connected Components
- `dijkstra.md` — Dijkstra
- `dijkstra_sparse.md` — Dijkstra on sparse graphs
- `bellman_ford.md` — Bellman-Ford
- `01_bfs.md` — 0-1 BFS
- `all-pair-shortest-path-floyd-warshall.md` — Floyd-Warshall
- `mst_kruskal.md` — MST Kruskal
- `topological-sort.md` — Topological Sort

**Algebra Fundamentals (7 bài)**
- `binary-exp.md` — Binary Exponentiation
- `euclid-algorithm.md` — Euclidean Algorithm
- `extended-euclid-algorithm.md` — Extended GCD
- `sieve-of-eratosthenes.md` — Sieve of Eratosthenes
- `phi-function.md` — Euler's Totient Function
- `module-inverse.md` — Modular Inverse
- `fibonacci-numbers.md` — Fibonacci Numbers

**Dynamic Programming (4 bài)**
- `intro-to-dp.md` — Introduction to DP
- `knapsack.md` — Knapsack Problem
- `longest_increasing_subsequence.md` — LIS
- `divide-and-conquer-dp.md` — Divide and Conquer DP

**String Fundamentals (4 bài)**
- `string-hashing.md` — String Hashing
- `prefix-function.md` — KMP (Prefix Function)
- `z-function.md` — Z-function
- `suffix-array.md` — Suffix Array

**Numerical Methods (3 bài)**
- `binary_search.md` — Binary Search
- `ternary_search.md` — Ternary Search
- `roots_newton.md` — Newton's Method

**Combinatorics (2 bài)**
- `binomial-coefficients.md` — Binomial Coefficients
- `catalan-numbers.md` — Catalan Numbers

---

#### 🟡 Ưu tiên 2 — Nâng cao phổ biến (50 bài)

**Graph Nâng cao**
- `bridge-searching.md`, `cutpoints.md` — Bridges & Articulation Points
- `strongly-connected-components.md` — SCC
- `lca.md`, `lca_binary_lifting.md` — LCA
- `edmonds_karp.md`, `dinic.md` — Max Flow
- `kuhn_maximum_bipartite_matching.md` — Bipartite Matching
- `hld.md` — Heavy-Light Decomposition
- `centroid_decomposition.md` — Centroid Decomposition
- `euler_path.md` — Euler Path
- `finding-cycle.md` — Finding Cycles
- `mst_prim.md` — MST Prim
- `2SAT.md` — 2-SAT
- `bipartite-check.md` — Bipartite Check

**Algebra Nâng cao**
- `chinese-remainder-theorem.md` — CRT
- `fft.md` — FFT
- `factorization.md` — Integer Factorization
- `primality_tests.md` — Primality Tests
- `discrete-log.md` — Discrete Log
- `bit-manipulation.md` — Bit Manipulation
- `linear-diophantine-equation.md` — Linear Diophantine

**String Nâng cao**
- `aho_corasick.md` — Aho-Corasick
- `suffix-automaton.md` — Suffix Automaton
- `manacher.md` — Manacher's Algorithm
- `rabin-karp.md` — Rabin-Karp

**Geometry Cơ bản**
- `basic-geometry.md` — Basic Geometry
- `convex-hull.md` — Convex Hull
- `segment-to-line.md` — Segment to Line
- `lines-intersection.md` — Line Intersection
- `picks-theorem.md` — Pick's Theorem
- `convex_hull_trick.md` — Convex Hull Trick

**Combinatorics**
- `inclusion-exclusion.md` — Inclusion-Exclusion
- `burnside.md` — Burnside's Lemma
- `stars_and_bars.md` — Stars and Bars
- `bracket_sequences.md` — Balanced Bracket Sequences

**DP**
- `knuth-optimization.md` — Knuth Optimization
- `profile-dynamics.md` — Profile DP
- `zero_matrix.md` — Zero Submatrix

**Game Theory**
- `sprague-grundy-nim.md` — Sprague-Grundy / Nim
- `games_on_graphs.md` — Games on Graphs

---

#### 🟢 Ưu tiên 3 — Nâng cao chuyên sâu (74 bài còn lại)

Bao gồm:
- Geometry nâng cao (Delaunay, Half-plane, Planar graphs, ...)
- Graph nâng cao (Push-relabel, MPM, Hungarian, ...)
- Algebra chuyên sâu (Continued fractions, Polynomial operations, Montgomery, ...)
- Linear Algebra (Gauss, Determinant, Rank)
- Sequences, Schedules, Others

---

## 3. Quy tắc Dịch theo Loại Nội dung

### 3.1 Tiêu đề bài viết

```markdown
# Gốc:
# Segment Tree

# Dịch:
# Cây phân đoạn (Segment Tree)
```

### 3.2 Đoạn văn giải thích

```markdown
# Gốc:
A Segment Tree is a data structure that stores information about array intervals
as a tree.

# Dịch:
Cây phân đoạn (Segment Tree) là một cấu trúc dữ liệu lưu trữ thông tin về
các khoảng (interval) của mảng dưới dạng cây.
```

### 3.3 Complexity analysis

```markdown
# Gốc:
The time complexity of this construction is $O(n)$.

# Dịch:
Độ phức tạp thời gian của việc xây dựng này là $O(n)$.
```

> Giữ nguyên ký hiệu $O(n)$ trong LaTeX.

### 3.4 Admonitions

```markdown
# Gốc:
!!! note "Implementation detail"
    The array should be 1-indexed.

# Dịch:
!!! note "Chi tiết cài đặt"
    Mảng nên được đánh chỉ số từ 1.
```

### 3.5 Code references trong văn bản

```markdown
# Gốc:
We call the function `build(a, v, tl, tr)` with the root vertex.

# Dịch:
Chúng ta gọi hàm `build(a, v, tl, tr)` với đỉnh gốc.
```

> Giữ nguyên tên hàm, biến trong backtick.

### 3.6 Practice Problems

```markdown
# Gốc:
## Practice Problems
- [SPOJ - HORRIBLE](https://www.spoj.com/problems/HORRIBLE/)

# Dịch:
## Bài tập thực hành
- [SPOJ - HORRIBLE](https://www.spoj.com/problems/HORRIBLE/)
```

> Giữ nguyên tên bài và link.

---

## 4. Quy trình Review

### 4.1 Checklist Review

Mỗi bài viết sau khi dịch phải pass checklist:

- [ ] **Thuật ngữ**: Đúng theo GLOSSARY.md
- [ ] **Code blocks**: Giữ nguyên 100%, số lượng giống bản gốc
- [ ] **LaTeX**: Giữ nguyên 100%, render đúng
- [ ] **Internal links**: Trỏ đúng file, không broken
- [ ] **Hình ảnh**: Hiển thị đúng
- [ ] **Frontmatter**: Hợp lệ
- [ ] **Headers**: Cấu trúc heading giống bản gốc
- [ ] **Văn phong**: Tự nhiên, dễ hiểu
- [ ] **Không thiếu nội dung**: Đủ so với bản gốc
- [ ] **Build thành công**: `mkdocs build` không lỗi

### 4.2 Automated QA

Script QA tự động sẽ kiểm tra:

1. Số code blocks EN == VI
2. Số LaTeX expressions EN == VI
3. Tất cả internal links hợp lệ
4. Frontmatter YAML hợp lệ
5. Không có placeholder chưa thay thế (`[CODE_BLOCK_N]`)
6. File size hợp lý (VI nên ≈ 90-120% EN)

---

## 5. Xử lý Cập nhật từ Upstream

### 5.1 Khi upstream sửa bài đã dịch

1. Phát hiện file EN thay đổi (diff)
2. Xác định phần thay đổi
3. Cập nhật tương ứng trong file `.vi.md`
4. Review lại phần cập nhật

### 5.2 Khi upstream thêm bài mới

1. Phát hiện file `.md` mới chưa có `.vi.md` tương ứng
2. Thêm vào backlog
3. Dịch theo pipeline tiêu chuẩn
4. Cập nhật `navigation.vi.md`

### 5.3 Tracking script

```bash
#!/bin/bash
# check_translation_status.sh
# Kiểm tra trạng thái dịch của tất cả bài viết

echo "=== CP-Algorithms Translation Status ==="
echo ""

total=0
translated=0
missing=0

find src -name "*.md" \
    -not -name "*.vi.md" \
    -not -path "*/overrides/*" \
    -not -name "navigation.md" \
    -not -name "index.md" \
    -not -name "tags.md" \
    -not -name "preview.md" \
    -not -name "contrib.md" \
    -not -name "code_of_conduct.md" | sort | while read f; do
    total=$((total + 1))
    vi_file="${f%.md}.vi.md"
    if [ -f "$vi_file" ]; then
        translated=$((translated + 1))
    else
        missing=$((missing + 1))
        echo "❌ CHƯA DỊCH: $f"
    fi
done

echo ""
echo "Tổng: $total | Đã dịch: $translated | Chưa dịch: $missing"
```

---

*Xem thêm: [GLOSSARY.md](GLOSSARY.md) cho bảng thuật ngữ chi tiết.*
