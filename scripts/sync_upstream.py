#!/usr/bin/env python3
import os
import subprocess
import time

def run_git_cmd(args):
    try:
        res = subprocess.run(args, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command {' '.join(args)}: {e.stderr}")
        return None

def get_last_commit_time(filepath):
    # Get last commit timestamp of the file
    out = run_git_cmd(["git", "log", "-1", "--format=%ct", filepath])
    if out:
        try:
            return int(out)
        except ValueError:
            pass
    # Fallback to local file modification time if not in git yet
    if os.path.exists(filepath):
        return int(os.path.getmtime(filepath))
    return 0

def check_sync():
    print("Fetching upstream changes...")
    # Fetch upstream, but don't fail if upstream remote doesn't exist
    subprocess.run(["git", "fetch", "upstream"], capture_output=True)
    
    missing = []
    outdated = []
    total_en = 0
    total_vi = 0
    
    for root, dirs, files in os.walk("src"):
        # Skip overrides or temporary dirs
        if "overrides" in root or ".git" in root:
            continue
            
        for f in files:
            if f.endswith(".md") and not f.endswith(".vi.md") and f not in ["navigation.md", "navigation.vi.md"]:
                total_en += 1
                en_path = os.path.join(root, f)
                vi_file = f[:-3] + ".vi.md"
                vi_path = os.path.join(root, vi_file)
                
                if not os.path.exists(vi_path):
                    missing.append(en_path)
                else:
                    total_vi += 1
                    # Check commit times
                    en_time = get_last_commit_time(en_path)
                    vi_time = get_last_commit_time(vi_path)
                    
                    if en_time > vi_time:
                        outdated.append((en_path, en_time, vi_time))
                        
    print("\n" + "="*50)
    print("UPSTREAM SYNC STATUS REPORT")
    print(f"Total English articles: {total_en}")
    print(f"Total Vietnamese translations: {total_vi} ({total_vi/total_en*100:.1f}%)")
    print("="*50)
    
    if missing:
        print(f"\n❌ MISSING TRANSLATIONS ({len(missing)}):")
        for m in sorted(missing):
            print(f"  - {m}")
    else:
        print("\n✅ No missing translations!")
        
    if outdated:
        print(f"\n⚠️ OUTDATED TRANSLATIONS ({len(outdated)}):")
        for out_path, en_t, vi_t in sorted(outdated):
            en_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(en_t))
            vi_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(vi_t))
            print(f"  - {out_path}")
            print(f"    (English updated: {en_date} vs Vietnamese translated: {vi_date})")
    else:
        print("✅ All existing translations are up-to-date with English sources!")
    print("="*50 + "\n")
    
    return len(missing) == 0 and len(outdated) == 0

if __name__ == "__main__":
    success = check_sync()
    # Exit with code 0 if fully synced, 1 if missing or outdated files found
    import sys
    sys.exit(0 if success else 1)
