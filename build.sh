#!/usr/bin/env bash
# build.sh — Convert wiki/ markdown to Hugo content/ and build the site.
# Run from the project root: ./build.sh

set -euo pipefail

WIKI_DIR="wiki"
SITE_DIR="site"
CONTENT_DIR="$SITE_DIR/content/docs"

# Clean previous build
rm -rf "$CONTENT_DIR"
mkdir -p "$CONTENT_DIR"

# --- Build a slug→section lookup from all wiki files ---
declare -A SLUG_MAP  # slug -> section path (e.g. "scion" -> "entities/scion")

for f in "$WIKI_DIR"/{sources,entities,concepts,analyses}/*.md; do
  [ -f "$f" ] || continue
  slug=$(basename "$f" .md)
  section=$(basename "$(dirname "$f")")
  SLUG_MAP["$slug"]="$section/$slug"
done

# --- Function: convert [[wikilinks]] to Hugo links ---
convert_wikilinks() {
  local content="$1"
  # Match [[slug]] and replace with [slug](/docs/section/slug/)
  while [[ "$content" =~ \[\[([a-zA-Z0-9_-]+)\]\] ]]; do
    local slug="${BASH_REMATCH[1]}"
    local target="${SLUG_MAP[$slug]:-}"
    if [ -n "$target" ]; then
      local replacement="[${slug}]({{< relref \"${target}\" >}})"
    else
      local replacement="**${slug}**"
    fi
    content="${content//"[[${slug}]]"/"$replacement"}"
  done
  echo "$content"
}

# --- Process each section ---
for section in sources entities concepts analyses; do
  src_dir="$WIKI_DIR/$section"
  dest_dir="$CONTENT_DIR/$section"
  mkdir -p "$dest_dir"

  # Section index with weight for menu ordering
  case "$section" in
    analyses) weight=1; icon="💡" ;;
    concepts) weight=2; icon="🧠" ;;
    entities) weight=3; icon="📦" ;;
    sources)  weight=4; icon="📄" ;;
  esac

  section_title="$(echo "$section" | sed 's/^./\U&/')"
  cat > "$dest_dir/_index.md" << EOF
---
title: "${icon} ${section_title}"
weight: ${weight}
bookCollapseSection: true
---

# ${section_title}
EOF

  for f in "$src_dir"/*.md; do
    [ -f "$f" ] || continue
    slug=$(basename "$f" .md)
    dest="$dest_dir/${slug}.md"

    # Read file, convert wikilinks, write to dest
    content=$(cat "$f")
    converted=$(convert_wikilinks "$content")

    # Add weight to frontmatter for alphabetical ordering
    if [[ "$converted" == ---* ]]; then
      # Insert bookToc after the opening ---
      converted=$(echo "$converted" | sed '1,/^---$/{
        /^---$/a\
bookToc: true
      }')
    fi

    echo "$converted" > "$dest"
  done
done

# --- Create the homepage from wiki/index.md ---
mkdir -p "$CONTENT_DIR"
{
  echo "---"
  echo "title: \"Wiki Index\""
  echo "type: docs"
  echo "bookToc: true"
  echo "---"
  echo ""
  convert_wikilinks "$(cat "$WIKI_DIR/index.md")"
} > "$CONTENT_DIR/_index.md"

# --- Create a log page ---
mkdir -p "$CONTENT_DIR/meta"
cat > "$CONTENT_DIR/meta/_index.md" << 'EOF'
---
title: "📋 Meta"
weight: 5
bookCollapseSection: true
---

# Meta
EOF

{
  echo "---"
  echo "title: \"Activity Log\""
  echo "bookToc: false"
  echo "---"
  echo ""
  convert_wikilinks "$(cat "$WIKI_DIR/log.md")"
} > "$CONTENT_DIR/meta/log.md"

echo "✅ Content generated: $(find "$CONTENT_DIR" -name '*.md' | wc -l | tr -d ' ') pages"

# --- Build the site ---
cd "$SITE_DIR"
hugo --minify
echo "✅ Site built at $SITE_DIR/public/"
