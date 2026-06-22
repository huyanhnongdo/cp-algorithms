# Lộ trình (Roadmap) — CP-Algorithms Tiếng Việt

> **Lộ trình chi tiết cho dự án xây dựng phiên bản tiếng Việt cp-algorithms.**  
> Ngày tạo: 2026-06-22

---

## Tổng quan Timeline

```
Phase 1         Phase 2              Phase 3                    Phase 4
Hạ tầng        Dịch cơ bản          Dịch toàn bộ               Bảo trì & Sync
(1-2 ngày)     (3-5 ngày)           (7-14 ngày)                (liên tục)
────────────────────────────────────────────────────────────────────────────►
 │              │                    │                           │
 ▼              ▼                    ▼                           ▼
 Setup i18n     40 bài nền tảng      124 bài nâng cao           Auto sync
 Pipeline AI    Review & QA          Review & QA                Upstream tracking
 Glossary       Navigation VI        Deploy                     Community
```

---

## Phase 1: Xây dựng Hạ tầng Song ngữ (1-2 ngày)

### Mục tiêu
Thiết lập toàn bộ hạ tầng kỹ thuật để hỗ trợ phiên bản song ngữ.

### Tasks

| # | Task | Chi tiết | Thời gian | Trạng thái |
|---|---|---|---|---|
| 1.1 | **Cài đặt plugin i18n** | `pip install mkdocs-static-i18n` | 1h | ✅ |
| 1.2 | **Cấu hình mkdocs.yml** | Thêm plugin i18n, language switcher, alternate links | 1h | ✅ |
| 1.3 | **Tạo trang chủ VI** | `src/index.vi.md` — trang chủ tiếng Việt | 1h | ✅ |
| 1.4 | **Tạo navigation VI** | `src/navigation.vi.md` — menu điều hướng tiếng Việt | 3h | ✅ |
| 1.5 | **Test build local** | Chạy `mkdocs serve`, kiểm tra language switcher, fallback | 1h | ✅ |
| 1.6 | **Xây dựng pipeline dịch** | Script Python: đọc → tách → dịch → ghép → validate | 4h | ✅ |
| 1.7 | **Xây dựng script QA** | Script kiểm tra: code blocks, LaTeX, links, frontmatter | 2h | ✅ |
| 1.8 | **Hoàn thiện GLOSSARY.md** | Bảng thuật ngữ chuẩn hóa (đã tạo sơ bộ) | 1h | ✅ |
| 1.9 | **Setup upstream remote** | `git remote add upstream ...`, test merge | 0.5h | ✅ |
| 1.10 | **Dịch 1 bài thử nghiệm** | Dịch `binary_search.md` để test toàn bộ pipeline | 1h | ✅ |

### Deliverables Phase 1
- [x] `MIGRATION_PLAN.md` ✅
- [x] `TRANSLATION_STRATEGY.md` ✅
- [x] `GLOSSARY.md` ✅
- [x] `ROADMAP.md` ✅
- [x] Plugin i18n hoạt động ✅
- [x] Pipeline dịch tự động sẵn sàng ✅
- [x] 1 bài mẫu được dịch thành công ✅

### Criteria hoàn thành
- `mkdocs build` thành công với cả EN và VI
- Language switcher hoạt động trên giao diện
- Bài thử nghiệm hiển thị đúng (code, LaTeX, links)

---

## Phase 2: Dịch Chủ đề Cơ bản (3-5 ngày)

### Mục tiêu
Dịch 40 bài viết nền tảng — bao phủ các chủ đề cốt lõi trong competitive programming.

### Tasks

| # | Task | Số bài | Thời gian | Trạng thái |
|---|---|---|---|---|
| 2.1 | **Data Structures** | 10 bài | 8h | ⏳ |
| | ├── `stack_queue_modification.vi.md` | | | ⬜ |
| | ├── `sparse-table.vi.md` | | | ⬜ |
| | ├── `disjoint_set_union.vi.md` | | | ✅ |
| | ├── `fenwick.vi.md` | | | ⬜ |
| | ├── `sqrt_decomposition.vi.md` | | | ⬜ |
| | ├── `segment_tree.vi.md` ⭐ | | | ⬜ |
| | ├── `treap.vi.md` | | | ⬜ |
| | ├── `sqrt-tree.vi.md` | | | ⬜ |
| | ├── `randomized_heap.vi.md` | | | ⬜ |
| | └── `deleting_in_log_n.vi.md` | | | ⬜ |
| 2.2 | **Graph Traversal & Shortest Paths** | 10 bài | 6h | ⬜ |
| | ├── `breadth-first-search.vi.md` | | | ⬜ |
| | ├── `depth-first-search.vi.md` | | | ⬜ |
| | ├── `search-for-connected-components.vi.md` | | | ⬜ |
| | ├── `dijkstra.vi.md` | | | ⬜ |
| | ├── `dijkstra_sparse.vi.md` | | | ⬜ |
| | ├── `bellman_ford.vi.md` | | | ⬜ |
| | ├── `01_bfs.vi.md` | | | ⬜ |
| | ├── `all-pair-shortest-path-floyd-warshall.vi.md` | | | ⬜ |
| | ├── `mst_kruskal.vi.md` | | | ⬜ |
| | └── `topological-sort.vi.md` | | | ⬜ |
| 2.3 | **Algebra Fundamentals** | 7 bài | 4h | ⏳ |
| | ├── `binary-exp.vi.md` | | | ✅ |
| | ├── `euclid-algorithm.vi.md` | | | ⬜ |
| | ├── `extended-euclid-algorithm.vi.md` | | | ⬜ |
| | ├── `sieve-of-eratosthenes.vi.md` | | | ⬜ |
| | ├── `phi-function.vi.md` | | | ⬜ |
| | ├── `module-inverse.vi.md` | | | ⬜ |
| | └── `fibonacci-numbers.vi.md` | | | ⬜ |
| 2.4 | **Dynamic Programming** | 4 bài | 3h | ⬜ |
| | ├── `intro-to-dp.vi.md` | | | ⬜ |
| | ├── `knapsack.vi.md` | | | ⬜ |
| | ├── `longest_increasing_subsequence.vi.md` | | | ⬜ |
| | └── `divide-and-conquer-dp.vi.md` | | | ⬜ |
| 2.5 | **String Fundamentals** | 4 bài | 3h | ⬜ |
| | ├── `string-hashing.vi.md` | | | ⬜ |
| | ├── `prefix-function.vi.md` | | | ⬜ |
| | ├── `z-function.vi.md` | | | ⬜ |
| | └── `suffix-array.vi.md` | | | ⬜ |
| 2.6 | **Numerical Methods** | 3 bài | 2h | ⏳ |
| | ├── `binary_search.vi.md` | | | ✅ |
| | ├── `ternary_search.vi.md` | | | ⬜ |
| | └── `roots_newton.vi.md` | | | ⬜ |
| 2.7 | **Combinatorics** | 2 bài | 1h | ⬜ |
| | ├── `binomial-coefficients.vi.md` | | | ⬜ |
| | └── `catalan-numbers.vi.md` | | | ⬜ |
| 2.8 | **Review & QA** | 40 bài | 5h | ⬜ |

### Deliverables Phase 2
- [ ] 40 file `.vi.md` được tạo và pass QA
- [ ] Navigation VI cập nhật cho 40 bài
- [ ] Glossary được cập nhật nếu có thuật ngữ mới

### Criteria hoàn thành
- Tất cả 40 bài build thành công
- QA script pass 100%
- Code blocks, LaTeX, links giữ nguyên
- Thuật ngữ nhất quán theo Glossary

---

## Phase 3: Dịch Toàn bộ Nội dung (7-14 ngày)

### Mục tiêu
Dịch 124 bài viết còn lại, bao phủ 100% nội dung.

### Tasks

| # | Task | Số bài | Thời gian | Trạng thái |
|---|---|---|---|---|
| 3.1 | **Algebra nâng cao** | 25 bài | 10h | ⬜ |
| | Prime numbers (3), Modular arithmetic (6), Number systems (2), Misc (12) | | | |
| 3.2 | **Graph nâng cao** | 42 bài | 16h | ⬜ |
| | Bridges/Articulations (5), Spanning trees (6), Cycles (3), LCA (5), Flows (9), Matching (3), Misc (6) + bài còn lại | | | |
| 3.3 | **Geometry** | 26 bài | 12h | ⬜ |
| | Elementary (9), Polygons (6), Convex hull (2), Sweep-line (1), Planar (2), Misc (6) | | | |
| 3.4 | **Combinatorics** | 7 bài còn lại | 4h | ⬜ |
| | Inclusion-Exclusion, Burnside, Stars&Bars, Brackets, Bishops, Labeled graphs, Combinations | | | |
| 3.5 | **String nâng cao** | 8 bài còn lại | 5h | ⬜ |
| | Suffix Tree, Suffix Automaton, Aho-Corasick, Manacher, Lyndon, Rabin-Karp, Expression parsing, Repetitions | | | |
| 3.6 | **DP còn lại** | 3 bài | 2h | ⬜ |
| | Knuth Optimization, Profile DP, Zero Matrix | | | |
| 3.7 | **Linear Algebra** | 4 bài | 2h | ⬜ |
| | Gauss (2), Kraut, Rank | | | |
| 3.8 | **Game Theory** | 2 bài | 1h | ⬜ |
| | Sprague-Grundy/Nim, Games on Graphs | | | |
| 3.9 | **Miscellaneous** | 12 bài | 5h | ⬜ |
| | Sequences (4), Schedules (3), Others (5) | | | |
| 3.10 | **Review & QA toàn bộ** | 124 bài | 10h | ⬜ |
| 3.11 | **Cập nhật navigation.vi.md** | Hoàn thiện | 2h | ⬜ |

### Deliverables Phase 3
- [ ] 164/164 file `.vi.md` hoàn thành (100%)
- [ ] Navigation VI hoàn chỉnh
- [ ] QA pass toàn bộ
- [ ] Site build thành công

### Criteria hoàn thành
- 100% bài viết có bản tiếng Việt
- `mkdocs build` thành công không có lỗi
- Language switcher hoạt động mọi trang
- Fallback EN hoạt động cho trang meta

---

## Phase 4: Đồng bộ & Bảo trì (Liên tục)

### Mục tiêu
Đảm bảo phiên bản tiếng Việt luôn đồng bộ với upstream và duy trì chất lượng.

### Tasks

| # | Task | Chi tiết | Thời gian | Trạng thái |
|---|---|---|---|---|
| 4.1 | **Script sync upstream** | Script tự động detect bài mới/sửa từ upstream | 3h | ⬜ |
| 4.2 | **GitHub Actions CI** | Auto build, test, detect thay đổi upstream | 3h | ⬜ |
| 4.3 | **Contribution guide VI** | `CONTRIBUTING.vi.md` — hướng dẫn đóng góp bản dịch | 2h | ⬜ |
| 4.4 | **Deploy** | Firebase hosting cho phiên bản VI | 2h | ⬜ |
| 4.5 | **Translation status dashboard** | Trang hiển thị % hoàn thành dịch | 2h | ⬜ |
| 4.6 | **Community onboarding** | README tiếng Việt, hướng dẫn contributor | 2h | ⬜ |

### Deliverables Phase 4
- [ ] Sync script hoạt động
- [ ] CI/CD pipeline hoàn chỉnh
- [ ] Site được deploy và truy cập công khai
- [ ] Có hướng dẫn cho người muốn đóng góp

### Quy trình bảo trì thường xuyên

```
Hàng tuần:
  1. Chạy `git fetch upstream && git merge upstream/main`
  2. Kiểm tra diff → Cập nhật bài dịch nếu cần
  3. Chạy QA script → Fix issues

Hàng tháng:
  1. Review glossary → Thêm thuật ngữ mới
  2. Kiểm tra broken links
  3. Cập nhật ROADMAP.md
```

---

## Metrics & KPIs

| Metric | Mục tiêu Phase 2 | Mục tiêu Phase 3 | Mục tiêu Phase 4 |
|---|---|---|---|
| % bài đã dịch | 24% (40/164) | 100% (164/164) | 100% + bài mới |
| QA pass rate | 100% | 100% | 100% |
| Build success | ✅ | ✅ | ✅ |
| Glossary coverage | 80% | 95% | 100% |
| Upstream sync lag | N/A | N/A | < 1 tuần |

---

## Rủi ro & Kế hoạch Dự phòng

| Rủi ro | Giải pháp |
|---|---|
| Upstream restructure lớn | Migration script, theo dõi releases |
| Plugin i18n không tương thích | Fallback: multi-site build (2 mkdocs.yml) |
| LLM dịch sai chuyên ngành | Glossary cứng + human review |
| Contributor burn-out | Chia nhỏ task, gamification (progress badge) |

---

## Liên kết

- [MIGRATION_PLAN.md](MIGRATION_PLAN.md) — Kế hoạch migration chi tiết
- [TRANSLATION_STRATEGY.md](TRANSLATION_STRATEGY.md) — Chiến lược dịch thuật
- [GLOSSARY.md](GLOSSARY.md) — Bảng thuật ngữ chuẩn hóa

---

*Roadmap này được cập nhật theo tiến trình thực tế của dự án.*
