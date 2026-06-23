#!/usr/bin/env python3
import os
import re
import sys
import argparse

def load_glossary(glossary_path="GLOSSARY.md"):
    """Parses GLOSSARY.md to extract terms for the LLM translation prompt."""
    terms = []
    if not os.path.exists(glossary_path):
        return ""
    
    with open(glossary_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract markdown tables
    # Find all table rows like: | Term EN | Term VI | Notes |
    matches = re.findall(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*[^|]*?\|", content)
    for en, vi in matches:
        en_clean = en.strip()
        vi_clean = vi.strip()
        if en_clean and vi_clean and en_clean != "Tiếng Anh" and not en_clean.startswith("---"):
            terms.append(f"- {en_clean} -> {vi_clean}")
            
    return "\n".join(terms)

def extract_preservable_blocks(content):
    """
    Extracts code blocks and LaTeX formulas, replacing them with placeholders.
    Returns: frontmatter, text_with_placeholders, replacements dict
    """
    replacements = {}
    counter = {'code': 0, 'latex_block': 0, 'latex_inline': 0}
    
    # 1. Extract YAML frontmatter (keep completely unchanged)
    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(0)
        text = content[len(frontmatter):]
    else:
        frontmatter = ""
        text = content
        
    # 2. Extract fenced code blocks (```cpp ... ```)
    def replace_code(match):
        key = f"[CODE_BLOCK_{counter['code']}]"
        replacements[key] = match.group(0)
        counter['code'] += 1
        return key
    text = re.sub(r"```.*?```", replace_code, text, flags=re.DOTALL)
    
    # 3. Extract Block LaTeX ($$...$$ or \[...\])
    def replace_latex_block(match):
        key = f"[LATEX_BLOCK_{counter['latex_block']}]"
        replacements[key] = match.group(0)
        counter['latex_block'] += 1
        return key
    text = re.sub(r"\$\$.*?\$\$|\\\[.*?\\\]", replace_latex_block, text, flags=re.DOTALL)
    
    # 4. Extract Inline LaTeX ($...$)
    def replace_latex_inline(match):
        key = f"[LATEX_INLINE_{counter['latex_inline']}]"
        replacements[key] = match.group(0)
        counter['latex_inline'] += 1
        return key
    # Make sure we don't match empty math or double dollar signs
    text = re.sub(r"\$[^$\n]+?\$", replace_latex_inline, text)
    
    return frontmatter, text, replacements

def reconstruct_content(frontmatter, translated_text, replacements):
    """Reconstructs the original structure by replacing placeholders back with original blocks."""
    # We reconstruct in reverse order of specificity to avoid collisions,
    # but since our keys are unique (e.g. [CODE_BLOCK_0]), direct replace is fine.
    result = translated_text
    for placeholder, original in replacements.items():
        result = result.replace(placeholder, original)
        
    # Standardize frontmatter tags if present
    # Translate tags/categories in frontmatter if needed, but original translation strategy says:
    # "Frontmatter tags: Keep original/translated, add lang: vi"
    if frontmatter:
        # Check if lang: vi is already present
        if "lang:" not in frontmatter:
            # Insert lang: vi before the ending separator
            frontmatter = frontmatter.replace("\n---", "\nlang: vi\n---")
            
    return frontmatter + result

def translate_via_gemini(text, glossary, api_key):
    """Translates text using Google Generative AI (Gemini)."""
    prompt = f"""
You are an expert technical translator specializing in competitive programming and algorithms.
Translate the following competitive programming article from English to Vietnamese.

CRITICAL RULES:
1. Translate naturally, clearly, and in a style suitable for Vietnamese computer science students and programmers.
2. Keep ALL placeholders [CODE_BLOCK_N], [LATEX_BLOCK_N], and [LATEX_INLINE_N] exactly as they are. Do not translate, change, or drop them.
3. Keep all Markdown formatting (headers ##, bold **, lists -, etc.) intact.
4. For Markdown links like [text](link_address.md) or [text](link_address.html), translate the 'text' but do NOT modify the 'link_address.md' (keep the original path and filename).
5. For images like ![alt text](path), translate the 'alt text' but keep the 'path' exactly as is.
6. Do NOT translate inline code/variables wrapped in backticks (e.g., `build()`, `update()`, `n`, `adj[u]`). Keep them exactly as is.
7. Use the following Glossary for term translation. Always put the English term in parentheses when introducing it for the first time in the page (e.g. "Cây phân đoạn (Segment Tree)", "Tìm kiếm nhị phân (Binary Search)").

GLOSSARY TERMS:
{glossary}

TEXT TO TRANSLATE:
{text}
"""
    
    # Try using the new google-genai SDK first
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        # List of models to try in preference order
        models = ['gemini-2.5-flash', 'gemini-3.1-flash-lite', 'gemini-2.0-flash', 'gemini-3.5-flash']
        for model_name in models:
            print(f"Trying translation with google-genai model: {model_name}...")
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                return response.text
            except Exception as model_err:
                print(f"Model {model_name} failed: {model_err}")
                continue
    except ImportError:
        print("google-genai not installed. Falling back to google-generativeai...")
        
    # Fallback to the legacy google-generativeai SDK
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    # List of legacy models
    legacy_models = ['gemini-2.5-flash', 'gemini-2.0-flash']
    for model_name in legacy_models:
        print(f"Trying translation with legacy google-generativeai model: {model_name}...")
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text
        except Exception as model_err:
            print(f"Legacy model {model_name} failed: {model_err}")
            continue
            
    raise Exception("All Gemini models and SDKs failed for translation.")

def translate_via_openai(text, glossary, api_key):
    """Translates text using OpenAI GPT-4o."""
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    
    prompt = f"""
You are an expert technical translator specializing in competitive programming and algorithms.
Translate the following competitive programming article from English to Vietnamese.

CRITICAL RULES:
1. Translate naturally, clearly, and in a style suitable for Vietnamese computer science students and programmers.
2. Keep ALL placeholders [CODE_BLOCK_N], [LATEX_BLOCK_N], and [LATEX_INLINE_N] exactly as they are. Do not translate, change, or drop them.
3. Keep all Markdown formatting (headers ##, bold **, lists -, etc.) intact.
4. For Markdown links like [text](link_address.md) or [text](link_address.html), translate the 'text' but do NOT modify the 'link_address.md' (keep the original path and filename).
5. For images like ![alt text](path), translate the 'alt text' but keep the 'path' exactly as is.
6. Do NOT translate inline code/variables wrapped in backticks (e.g., `build()`, `update()`, `n`, `adj[u]`). Keep them exactly as is.
7. Use the following Glossary for term translation. Always put the English term in parentheses when introducing it for the first time in the page (e.g. "Cây phân đoạn (Segment Tree)", "Tìm kiếm nhị phân (Binary Search)").

GLOSSARY TERMS:
{glossary}
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content

def translate_file(input_file, output_file, glossary_path="GLOSSARY.md"):
    """Translates a single markdown file using the configured LLM API key."""
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} does not exist.")
        return False
        
    print(f"Reading {input_file}...")
    with open(input_file, "r", encoding="utf-8") as f:
        raw_content = f.read()
        
    print("Parsing and extracting blocks...")
    frontmatter, text_with_placeholders, replacements = extract_preservable_blocks(raw_content)
    
    print("Loading glossary...")
    glossary = load_glossary(glossary_path)
    
    # Check for API keys
    gemini_key = os.environ.get("GEMINI_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")
    
    translated_text = ""
    if gemini_key:
        print("Translating via Gemini API...")
        try:
            translated_text = translate_via_gemini(text_with_placeholders, glossary, gemini_key)
        except Exception as e:
            print(f"Gemini translation failed: {e}")
            return False
    elif openai_key:
        print("Translating via OpenAI API...")
        try:
            translated_text = translate_via_openai(text_with_placeholders, glossary, openai_key)
        except Exception as e:
            print(f"OpenAI translation failed: {e}")
            return False
    else:
        print("Warning: Neither GEMINI_API_KEY nor OPENAI_API_KEY environment variables are set.")
        print("Generating a mockup translation (copying original text with translated headers)...")
        # In mock mode, we just copy the original but replace headers/admonitions to show the structure works.
        mock_lines = []
        for line in text_with_placeholders.split("\n"):
            if line.startswith("# "):
                mock_lines.append(line + " (Bản dịch Tiếng Việt)")
            elif line.startswith("## "):
                mock_lines.append(line + " (Mục dịch)")
            elif "Practice Problems" in line:
                mock_lines.append(line.replace("Practice Problems", "Bài tập thực hành"))
            else:
                mock_lines.append(line)
        translated_text = "\n".join(mock_lines)
        
    print("Reconstructing final content...")
    final_content = reconstruct_content(frontmatter, translated_text, replacements)
    
    # Write to output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    print(f"Success! Translated file saved to {output_file}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate CP-Algorithms markdown files to Vietnamese.")
    parser.add_argument("input", help="Path to the input English markdown file.")
    parser.add_argument("-o", "--output", help="Path to save the translated file. Defaults to input_file.vi.md")
    parser.add_argument("-g", "--glossary", default="GLOSSARY.md", help="Path to the glossary file.")
    
    args = parser.parse_args()
    
    output_path = args.output
    if not output_path:
        output_path = args.input.replace(".md", ".vi.md")
        
    success = translate_file(args.input, output_path, args.glossary)
    sys.exit(0 if success else 1)
