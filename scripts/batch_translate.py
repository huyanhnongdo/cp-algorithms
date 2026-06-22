#!/usr/bin/env python3
import os
import sys
import subprocess

# List of Phase 2 files from ROADMAP.md
PHASE_2_FILES = [
    # 2.1 Data Structures
    "src/data_structures/stack_queue_modification.md",
    "src/data_structures/sparse-table.md",
    "src/data_structures/disjoint_set_union.md",
    "src/data_structures/fenwick.md",
    "src/data_structures/sqrt_decomposition.md",
    "src/data_structures/segment_tree.md",
    "src/data_structures/treap.md",
    "src/data_structures/sqrt-tree.md",
    "src/data_structures/randomized_heap.md",
    "src/data_structures/deleting_in_log_n.md",
    
    # 2.2 Graph Traversal & Shortest Paths
    "src/graph/breadth-first-search.md",
    "src/graph/depth-first-search.md",
    "src/graph/search-for-connected-components.md",
    "src/graph/dijkstra.md",
    "src/graph/dijkstra_sparse.md",
    "src/graph/bellman_ford.md",
    "src/graph/01_bfs.md",
    "src/graph/all-pair-shortest-path-floyd-warshall.md",
    "src/graph/mst_kruskal.md",
    "src/graph/topological-sort.md",
    
    # 2.3 Algebra Fundamentals
    "src/algebra/binary-exp.md",
    "src/algebra/euclid-algorithm.md",
    "src/algebra/extended-euclid-algorithm.md",
    "src/algebra/sieve-of-eratosthenes.md",
    "src/algebra/phi-function.md",
    "src/algebra/module-inverse.md",
    "src/algebra/fibonacci-numbers.md",
    
    # 2.4 Dynamic Programming
    "src/dynamic_programming/intro-to-dp.md",
    "src/dynamic_programming/knapsack.md",
    "src/dynamic_programming/longest_increasing_subsequence.md",
    "src/dynamic_programming/divide-and-conquer-dp.md",
    
    # 2.5 String Fundamentals
    "src/string/string-hashing.md",
    "src/string/prefix-function.md",
    "src/string/z-function.md",
    "src/string/suffix-array.md",
    
    # 2.6 Numerical Methods
    "src/num_methods/binary_search.md",
    "src/num_methods/ternary_search.md",
    "src/num_methods/roots_newton.md",
    
    # 2.7 Combinatorics
    "src/combinatorics/binomial-coefficients.md",
    "src/combinatorics/catalan-numbers.md",
]

def check_keys():
    gemini_key = os.environ.get("GEMINI_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")
    if not gemini_key and not openai_key:
        print("Error: Neither GEMINI_API_KEY nor OPENAI_API_KEY environment variable is set.")
        print("Please export your API key before running this batch translation script.")
        print("Example: export GEMINI_API_KEY='your-key-here'")
        return False
    return True

def run_batch():
    if not check_keys():
        return False
        
    print(f"Starting batch translation of {len(PHASE_2_FILES)} Phase 2 files...")
    
    success_count = 0
    skipped_count = 0
    failed_count = 0
    
    for idx, filepath in enumerate(PHASE_2_FILES):
        vi_filepath = filepath.replace(".md", ".vi.md")
        print(f"\n--------------------------------------------------")
        print(f"[{idx+1}/{len(PHASE_2_FILES)}] Processing: {filepath}")
        
        # Check if already translated
        if os.path.exists(vi_filepath):
            # Check if it has actual content (not a mock translation)
            with open(vi_filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if "(Bản dịch Tiếng Việt)" not in content and "(Mục dịch)" not in content:
                print(f"Already translated and validated. Skipping.")
                skipped_count += 1
                continue
                
        # Run translate script
        print(f"Translating...")
        translate_cmd = ["python3", "scripts/translate.py", filepath]
        res = subprocess.run(translate_cmd, capture_output=True, text=True)
        
        if res.returncode != 0:
            print(f"❌ Translation failed for {filepath}.")
            print(res.stderr)
            failed_count += 1
            continue
            
        # Run QA check
        print(f"Running QA check...")
        qa_cmd = ["python3", "scripts/qa_check.py", filepath, vi_filepath]
        qa_res = subprocess.run(qa_cmd, capture_output=True, text=True)
        
        if qa_res.returncode == 0:
            print(f"✅ QA passed for {vi_filepath}!")
            success_count += 1
        else:
            print(f"⚠️ QA failed for {vi_filepath}. Please review manually.")
            print(qa_res.stdout)
            print(qa_res.stderr)
            failed_count += 1
            
    print("\n==================================================")
    print("BATCH TRANSLATION SUMMARY")
    print(f"Total: {len(PHASE_2_FILES)}")
    print(f"Successful: {success_count}")
    print(f"Skipped (already done): {skipped_count}")
    print(f"Failed/Warnings: {failed_count}")
    print("==================================================")
    return True

if __name__ == "__main__":
    success = run_batch()
    sys.exit(0 if success else 1)
