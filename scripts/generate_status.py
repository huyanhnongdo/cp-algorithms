#!/usr/bin/env python3
import os

def generate_dashboard():
    total_en = 0
    translated = []
    untranslated = []
    
    # We will group files by their category directory
    categories = {}
    
    for root, dirs, files in os.walk("src"):
        if "overrides" in root or ".git" in root:
            continue
            
        # Get category name from relative path
        rel_path = os.path.relpath(root, "src")
        if rel_path == ".":
            category = "Root/Meta"
        else:
            category = rel_path.split(os.sep)[0].replace("_", " ").capitalize()
            
        for f in files:
            if f.endswith(".md") and not f.endswith(".vi.md") and f not in ["navigation.md", "navigation.vi.md"]:
                total_en += 1
                en_path = os.path.join(root, f)
                vi_file = f[:-3] + ".vi.md"
                vi_path = os.path.join(root, vi_file)
                
                if category not in categories:
                    categories[category] = {"total": 0, "translated": 0}
                categories[category]["total"] += 1
                
                if os.path.exists(vi_path):
                    categories[category]["translated"] += 1
                    translated.append(en_path)
                else:
                    untranslated.append(en_path)
                    
    progress_pct = (len(translated) / total_en * 100) if total_en > 0 else 0
    
    # Generate content for translation_status.vi.md
    vi_content = f"""---
title: Tiến độ Dịch thuật
search:
  exclude: true
lang: vi
---
# Bảng Tiến độ Dịch thuật (Translation Progress Dashboard)

Trang này hiển thị thống kê tự động về tiến độ dịch thuật các bài viết thuật toán từ Tiếng Anh sang Tiếng Việt.

## Tổng quan tiến độ

<div class="progress-container" style="background-color: #e0e0e0; border-radius: 8px; width: 100%; height: 24px; position: relative; margin-bottom: 20px;">
  <div class="progress-bar" style="background-color: #4caf50; width: {progress_pct:.1f}%; height: 100%; border-radius: 8px; text-align: center; color: white; line-height: 24px; font-weight: bold;">
    {progress_pct:.1f}%
  </div>
</div>

- **Tổng số bài viết**: {total_en} bài
- **Đã hoàn thành dịch**: {len(translated)} bài
- **Chưa hoàn thành dịch**: {len(untranslated)} bài

---

## Chi tiết theo chủ đề

| Chủ đề | Số bài viết | Đã dịch | Tiến độ | Trạng thái |
|---|---|---|---|---|
"""
    
    for cat, stats in sorted(categories.items()):
        total = stats["total"]
        trans = stats["translated"]
        pct = (trans / total * 100) if total > 0 else 0
        status_icon = "✅ Hoàn thành" if pct == 100 else "⏳ Đang dịch"
        vi_content += f"| {cat} | {total} | {trans} | {pct:.1f}% | {status_icon} |\n"
        
    if untranslated:
        vi_content += "\n## Các bài chưa được dịch\n\n"
        for u in sorted(untranslated):
            # Convert file path to markdown link
            vi_content += f"- [{os.path.basename(u)}]({u.replace('src/', '')})\n"
    else:
        vi_content += "\n🎉 **Tuyệt vời! Toàn bộ 100% các bài viết thuật toán đã được dịch sang Tiếng Việt!**\n"
        
    # Write to src/translation_status.vi.md
    with open("src/translation_status.vi.md", "w", encoding="utf-8") as f:
        f.write(vi_content)
        
    # Generate English content
    en_content = f"""---
title: Translation Status
search:
  exclude: true
---
# Translation Progress Dashboard

This page displays the automated statistics of the Vietnamese translation progress.

## Overview

<div class="progress-container" style="background-color: #e0e0e0; border-radius: 8px; width: 100%; height: 24px; position: relative; margin-bottom: 20px;">
  <div class="progress-bar" style="background-color: #4caf50; width: {progress_pct:.1f}%; height: 100%; border-radius: 8px; text-align: center; color: white; line-height: 24px; font-weight: bold;">
    {progress_pct:.1f}%
  </div>
</div>

- **Total articles**: {total_en}
- **Translated articles**: {len(translated)}
- **Remaining articles**: {len(untranslated)}

---

## Details by Category

| Category | Total Articles | Translated | Progress | Status |
|---|---|---|---|---|
"""
    
    for cat, stats in sorted(categories.items()):
        total = stats["total"]
        trans = stats["translated"]
        pct = (trans / total * 100) if total > 0 else 0
        status_icon = "✅ Completed" if pct == 100 else "⏳ In Progress"
        en_content += f"| {cat} | {total} | {trans} | {pct:.1f}% | {status_icon} |\n"
        
    if untranslated:
        en_content += "\n## Remaining Articles\n\n"
        for u in sorted(untranslated):
            en_content += f"- [{os.path.basename(u)}]({u.replace('src/', '')})\n"
    else:
        en_content += "\n🎉 **Awesome! 100% of all articles have been successfully translated into Vietnamese!**\n"
        
    # Write to src/translation_status.md
    with open("src/translation_status.md", "w", encoding="utf-8") as f:
        f.write(en_content)
        
    print("Translation status generated successfully!")

if __name__ == "__main__":
    generate_dashboard()
