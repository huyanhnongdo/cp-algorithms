#!/usr/bin/env python3
import os
import re
import sys
import argparse

def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def run_qa_check(source_path, target_path):
    """
    Validates that target_path is a valid translation of source_path.
    Returns: True if all checks pass, False otherwise.
    """
    if not os.path.exists(source_path):
        print(f"Error: Source file {source_path} does not exist.")
        return False
    if not os.path.exists(target_path):
        print(f"Error: Target file {target_path} does not exist.")
        return False

    source = read_file(source_path)
    target = read_file(target_path)
    
    passed = True
    print(f"\n=== QA Check for: {os.path.basename(target_path)} ===")
    
    # 1. Check for unresolved placeholders
    placeholders = re.findall(r"\[CODE_BLOCK_\d+\]|\[LATEX_BLOCK_\d+\]|\[LATEX_INLINE_\d+\]", target)
    if placeholders:
        print(f"❌ FAIL: Unresolved placeholders found in target: {placeholders}")
        passed = False
    else:
        print("✅ PASS: No unresolved placeholders.")
        
    # 2. Check code blocks count and content
    source_codes = re.findall(r"```.*?```", source, re.DOTALL)
    target_codes = re.findall(r"```.*?```", target, re.DOTALL)
    
    if len(source_codes) != len(target_codes):
        print(f"❌ FAIL: Code block count mismatch. Source: {len(source_codes)}, Target: {len(target_codes)}")
        passed = False
    else:
        # Check that the code inside matches exactly (except for whitespace/tab differences maybe)
        mismatches = []
        for idx, (src_code, tgt_code) in enumerate(zip(source_codes, target_codes)):
            if src_code.strip() != tgt_code.strip():
                # Let's check if the only differences are header options like ```cpp or class name,
                # but typically they must be identical.
                mismatches.append(idx)
        
        if mismatches:
            print(f"❌ FAIL: Code block content mismatch at indices: {mismatches}")
            passed = False
        else:
            print(f"✅ PASS: Code blocks ({len(source_codes)}) are identical.")

    # 3. Check LaTeX math formulas count
    source_latex_blocks = re.findall(r"\$\$.*?\$\$", source, re.DOTALL)
    target_latex_blocks = re.findall(r"\$\$.*?\$\$", target, re.DOTALL)
    if len(source_latex_blocks) != len(target_latex_blocks):
        print(f"❌ FAIL: LaTeX blocks ($$...$$) count mismatch. Source: {len(source_latex_blocks)}, Target: {len(target_latex_blocks)}")
        passed = False
    else:
        print(f"✅ PASS: LaTeX blocks ({len(source_latex_blocks)}) count matches.")

    source_latex_inlines = re.findall(r"\$[^$\n]+?\$", source)
    target_latex_inlines = re.findall(r"\$[^$\n]+?\$", target)
    if len(source_latex_inlines) != len(target_latex_inlines):
        print(f"⚠️ WARNING: Inline LaTeX ($...$) count mismatch. Source: {len(source_latex_inlines)}, Target: {len(target_latex_inlines)}")
        # Sometimes small differences occur if the translator translates math notation inside text (e.g. $N$ vs N),
        # but we check if it is within a tolerance or if we should flag it as fail.
        # Let's make it a warning instead of a hard fail, unless the difference is large.
        if abs(len(source_latex_inlines) - len(target_latex_inlines)) > 2:
            print(f"❌ FAIL: Inline LaTeX count difference too large (> 2).")
            passed = False
    else:
        print(f"✅ PASS: Inline LaTeX ({len(source_latex_inlines)}) count matches.")

    # 4. Check internal links (*.md)
    source_links = set(re.findall(r"\]\(([^)]+\.md[^)]*)\)", source))
    target_links = set(re.findall(r"\]\(([^)]+\.md[^)]*)\)", target))
    
    missing_links = source_links - target_links
    extra_links = target_links - source_links
    
    if missing_links:
        print(f"❌ FAIL: Internal links present in source but missing in target: {missing_links}")
        passed = False
    if extra_links:
        # Sometimes translators update link paths or anchors, which might be okay, but let's check
        print(f"⚠️ WARNING: Target has extra/modified internal links: {extra_links}")
        
    if not missing_links:
        print("✅ PASS: All original internal links are preserved.")

    # 5. Check YAML frontmatter validity
    # Must have opening and closing ---
    target_fm = re.match(r"^---\n(.*?)\n---\n", target, re.DOTALL)
    if not target_fm:
        # Check if source had frontmatter
        source_fm = re.match(r"^---\n(.*?)\n---\n", source, re.DOTALL)
        if source_fm:
            print("❌ FAIL: Frontmatter missing in target but exists in source.")
            passed = False
        else:
            print("✅ PASS: No frontmatter in both files.")
    else:
        print("✅ PASS: Frontmatter structure is valid.")
        
    if passed:
        print("🎉 SUMMARY: ALL QA CHECKS PASSED!")
    else:
        print("🛑 SUMMARY: QA CHECKS FAILED. Please review the errors above.")
        
    return passed

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QA verification for CP-Algorithms translations.")
    parser.add_argument("source", help="Path to original English markdown file.")
    parser.add_argument("target", help="Path to translated Vietnamese markdown file.")
    
    args = parser.parse_args()
    
    success = run_qa_check(args.source, args.target)
    sys.exit(0 if success else 1)
