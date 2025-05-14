import os
import re

# Define the base and docs directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")

# Patterns to fix or remove
EMOJI_PATTERN = re.compile(r"[^\w\s\-#]")
BROKEN_LINK_PATTERN = re.compile(r"\.\./results/figures/")

def clean_markdown_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove emojis from anchor links
    content = EMOJI_PATTERN.sub("", content)

    # Fix broken relative image links
    content = BROKEN_LINK_PATTERN.sub("figures/", content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def fix_markdown_links():
    for file in os.listdir(DOCS_DIR):
        if file.endswith(".md"):
            filepath = os.path.join(DOCS_DIR, file)
            clean_markdown_file(filepath)

if __name__ == "__main__":
    fix_markdown_links()
    print("✅ Markdown links and emojis cleaned successfully.")
