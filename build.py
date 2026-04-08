#!/usr/bin/env python3
"""Convert wiki/ markdown to Hugo content/ and build the site."""

import os
import re
import shutil
import subprocess
import sys

WIKI_DIR = "wiki"
SITE_DIR = "site"
CONTENT_DIR = os.path.join(SITE_DIR, "content", "docs")
SECTIONS = ["sources", "entities", "concepts", "analyses"]

# --- Build slug→section lookup ---
slug_map = {}
for section in SECTIONS:
    src = os.path.join(WIKI_DIR, section)
    if not os.path.isdir(src):
        continue
    for f in os.listdir(src):
        if f.endswith(".md"):
            slug = f[:-3]
            slug_map[slug] = f"{section}/{slug}"


REPO_URL = "https://github.com/imforster/llm-wiki/blob/main"


def convert_wikilinks(text):
    """Replace [[slug]] with Hugo links, and fix raw/ relative paths."""
    def replace(m):
        slug = m.group(1)
        target = slug_map.get(slug)
        if target:
            return f'[{slug}]({{{{< ref "/docs/{target}" >}}}})'
        return f"**{slug}**"
    text = re.sub(r"\[\[([a-zA-Z0-9_-]+)\]\]", replace, text)
    text = re.sub(r'\(\.\.\/\.\.\/raw\/([^)]+)\)', rf'({REPO_URL}/raw/\1)', text)
    return text


# --- Clean and create output ---
if os.path.exists(CONTENT_DIR):
    shutil.rmtree(CONTENT_DIR)
os.makedirs(CONTENT_DIR)

section_meta = {
    "analyses": (1, "💡"),
    "concepts": (2, "🧠"),
    "entities": (3, "📦"),
    "sources":  (4, "📄"),
}

total = 0
for section in SECTIONS:
    src_dir = os.path.join(WIKI_DIR, section)
    dest_dir = os.path.join(CONTENT_DIR, section)
    os.makedirs(dest_dir, exist_ok=True)

    weight, icon = section_meta[section]
    title = section.capitalize()

    # Build page list for section index
    pages = []
    if os.path.isdir(src_dir):
        for fname in sorted(os.listdir(src_dir)):
            if not fname.endswith(".md"):
                continue
            slug = fname[:-3]
            # Extract title from first markdown heading
            content = open(os.path.join(src_dir, fname)).read()
            heading = slug.replace("-", " ").title()
            for line in content.split("\n"):
                if line.startswith("# "):
                    heading = line[2:].strip()
                    break
            # Extract description from frontmatter tags or first paragraph
            desc = ""
            if "---" in content:
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    for fmline in parts[1].split("\n"):
                        if fmline.strip().startswith("type:"):
                            desc = fmline.split(":", 1)[1].strip()
                            break
            pages.append((slug, heading, desc))

    with open(os.path.join(dest_dir, "_index.md"), "w") as f:
        f.write(f"---\ntitle: \"{icon} {title}\"\nweight: {weight}\nbookCollapseSection: true\n---\n\n# {title}\n\n")
        if pages:
            f.write(f"| Page | Type |\n|------|------|\n")
            for slug, heading, desc in pages:
                f.write(f"| [{heading}]({{{{< ref \"/docs/{section}/{slug}\" >}}}}) | {desc} |\n")
        f.write("\n")
    total += 1

    if not os.path.isdir(src_dir):
        continue

    for fname in sorted(os.listdir(src_dir)):
        if not fname.endswith(".md"):
            continue
        src_path = os.path.join(src_dir, fname)
        dest_path = os.path.join(dest_dir, fname)

        content = open(src_path).read()
        # Only convert wikilinks in body, not in YAML frontmatter
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                converted = "---" + parts[1] + "---" + convert_wikilinks(parts[2])
            else:
                converted = convert_wikilinks(content)
        else:
            converted = convert_wikilinks(content)
        with open(dest_path, "w") as f:
            f.write(converted)
        total += 1

# --- Homepage from wiki/overview.md ---
overview_content = open(os.path.join(WIKI_DIR, "overview.md")).read()
if overview_content.startswith("---"):
    parts = overview_content.split("---", 2)
    overview_body = parts[2] if len(parts) >= 3 else overview_content
else:
    overview_body = overview_content
with open(os.path.join(CONTENT_DIR, "_index.md"), "w") as f:
    f.write("---\ntitle: \"LLM Wiki\"\ntype: docs\nbookToc: true\n---\n\n")
    f.write(convert_wikilinks(overview_body))
total += 1

# --- Log page ---
meta_dir = os.path.join(CONTENT_DIR, "meta")
os.makedirs(meta_dir, exist_ok=True)
with open(os.path.join(meta_dir, "_index.md"), "w") as f:
    f.write("---\ntitle: \"📋 Meta\"\nweight: 5\nbookCollapseSection: true\nbookHidden: true\n---\n\n# Meta\n")
total += 1

log_content = open(os.path.join(WIKI_DIR, "log.md")).read()
with open(os.path.join(meta_dir, "log.md"), "w") as f:
    f.write("---\ntitle: \"Activity Log\"\nbookToc: false\n---\n\n")
    f.write(convert_wikilinks(log_content))
total += 1

print(f"✅ Content generated: {total} pages")

# --- Build ---
result = subprocess.run(["hugo", "--minify", "-d", os.path.join("..", "public")], cwd=SITE_DIR, capture_output=True, text=True)
print(result.stdout)
if result.returncode != 0:
    print(result.stderr, file=sys.stderr)
    sys.exit(result.returncode)
print("✅ Site built at public/")
