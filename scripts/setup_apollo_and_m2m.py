#!/usr/bin/env python3
"""
setup_apollo_and_m2m.py
1. Injects Apollo Website Visitor Tracking script into all target HTML pages.
2. Injects <link rel="alternate" type="text/markdown" href="..."> in <head>.
3. Converts HTML content to clean, readable Markdown with frontmatter (.md files) using standard library html.parser.
4. Updates llms.txt to document M2M markdown endpoints.
"""

import os
import re
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser

SITE_ROOT = Path("/Users/hugosoares/site_hsn_labs")

APOLLO_SCRIPT = """  <!-- Apollo Website Visitor Tracking -->
  <script>function initApollo(){var n=Math.random().toString(36).substring(7),o=document.createElement("script");
o.src="https://assets.apollo.io/micro/website-tracker/tracker.iife.js?nocache="+n,o.async=!0,o.defer=!0,
o.onload=function(){window.trackingFunctions.onLoad({appId:"69e90a89f9d8290015e5446a"})},
document.head.appendChild(o)}initApollo();</script>
"""

PAGES = [
    # (relative_html, relative_md, canonical_url, locale)
    ("index.html", "index.md", "https://hsnlabs.ai/", "en"),
    ("pt/index.html", "pt/index.md", "https://hsnlabs.ai/pt/", "pt-BR"),
    ("bootcamp/index.html", "bootcamp/index.md", "https://hsnlabs.ai/bootcamp/", "en"),
    ("pt/bootcamp/index.html", "pt/bootcamp/index.md", "https://hsnlabs.ai/pt/bootcamp/", "pt-BR"),
    ("advisory/index.html", "advisory/index.md", "https://hsnlabs.ai/advisory/", "en"),
    ("pt/advisory/index.html", "pt/advisory/index.md", "https://hsnlabs.ai/pt/advisory/", "pt-BR"),
    ("canvas/index.html", "canvas/index.md", "https://hsnlabs.ai/canvas/", "en"),
    ("pt/canvas/index.html", "pt/canvas/index.md", "https://hsnlabs.ai/pt/canvas/", "pt-BR"),
    ("mcp/index.html", "mcp/index.md", "https://hsnlabs.ai/mcp/", "en"),
    ("pt/mcp/index.html", "pt/mcp/index.md", "https://hsnlabs.ai/pt/mcp/", "pt-BR"),
    ("langchain/index.html", "langchain/index.md", "https://hsnlabs.ai/langchain/", "en"),
    ("pt/langchain/index.html", "pt/langchain/index.md", "https://hsnlabs.ai/pt/langchain/", "pt-BR"),
    ("snowflake/index.html", "snowflake/index.md", "https://hsnlabs.ai/snowflake/", "en"),
    ("pt/snowflake/index.html", "pt/snowflake/index.md", "https://hsnlabs.ai/pt/snowflake/", "pt-BR"),
    ("braintrust/index.html", "braintrust/index.md", "https://hsnlabs.ai/braintrust/", "en"),
    ("pt/braintrust/index.html", "pt/braintrust/index.md", "https://hsnlabs.ai/pt/braintrust/", "pt-BR"),
    ("playbooks/index.html", "playbooks/index.md", "https://hsnlabs.ai/playbooks/", "en"),
    ("pt/playbooks/index.html", "pt/playbooks/index.md", "https://hsnlabs.ai/pt/playbooks/", "pt-BR"),
    ("portfolio/index.html", "portfolio/index.md", "https://hsnlabs.ai/portfolio/", "en"),
    ("pt/portfolio/index.html", "pt/portfolio/index.md", "https://hsnlabs.ai/pt/portfolio/", "pt-BR"),
    ("privacy-policy/index.html", "privacy-policy/index.md", "https://hsnlabs.ai/privacy-policy/", "en"),
    ("pt/privacy-policy/index.html", "pt/privacy-policy/index.md", "https://hsnlabs.ai/pt/privacy-policy/", "pt-BR"),
    ("modern-slavery-statement/index.html", "modern-slavery-statement/index.md", "https://hsnlabs.ai/modern-slavery-statement/", "en"),
    ("pt/modern-slavery-statement/index.html", "pt/modern-slavery-statement/index.md", "https://hsnlabs.ai/pt/modern-slavery-statement/", "pt-BR"),
    ("architecture.html", "architecture.md", "https://hsnlabs.ai/architecture.html", "en"),
    ("404.html", "404.md", "https://hsnlabs.ai/404.html", "en"),
]

class HTMLToMarkdownParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self.in_title = False
        self.ignore = False
        self.ignore_depth = 0
        self.current_tag = None
        self.text_buffer = []
        self.output_blocks = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag in ["script", "style", "noscript", "svg", "iframe"]:
            self.ignore = True
            self.ignore_depth += 1
            return

        if self.ignore:
            self.ignore_depth += 1
            return

        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            if attrs_dict.get("name") == "description":
                content_val = attrs_dict.get("content") or ""
                self.description = content_val.strip()

        if tag in ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li"]:
            self.current_tag = tag
            self.text_buffer = []

    def handle_endtag(self, tag):
        if tag in ["script", "style", "noscript", "svg", "iframe"]:
            self.ignore_depth -= 1
            if self.ignore_depth <= 0:
                self.ignore = False
                self.ignore_depth = 0
            return

        if self.ignore:
            self.ignore_depth -= 1
            if self.ignore_depth <= 0:
                self.ignore = False
                self.ignore_depth = 0
            return

        if tag == "title":
            self.in_title = False

        if tag in ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li"]:
            raw_text = " ".join("".join(self.text_buffer).split()).strip()
            if raw_text:
                if tag.startswith("h"):
                    level = int(tag[1])
                    self.output_blocks.append(f"{'#' * level} {raw_text}")
                elif tag == "p":
                    self.output_blocks.append(raw_text)
                elif tag == "li":
                    self.output_blocks.append(f"- {raw_text}")
            self.current_tag = None
            self.text_buffer = []

    def handle_data(self, data):
        if self.ignore:
            return
        if self.in_title:
            self.title += data.strip()
        elif self.current_tag:
            self.text_buffer.append(data)

def extract_clean_markdown(html_content, canonical_url, locale):
    parser = HTMLToMarkdownParser()
    parser.feed(html_content)

    title = parser.title or "hsnlabs"
    desc = parser.description
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    md_lines = []
    md_lines.append("---")
    md_lines.append(f'title: "{title}"')
    if desc:
        md_lines.append(f'description: "{desc}"')
    md_lines.append(f'url: "{canonical_url}"')
    md_lines.append(f'locale: "{locale}"')
    md_lines.append(f'updatedAt: "{now_iso}"')
    md_lines.append("---")
    md_lines.append("")
    md_lines.append(f"# {title}")
    if desc:
        md_lines.append("")
        md_lines.append(f"> {desc}")
    md_lines.append("")

    # Deduplicate blocks
    seen = set()
    for block in parser.output_blocks:
        if block not in seen:
            md_lines.append(block)
            md_lines.append("")
            seen.add(block)

    return "\n".join(md_lines).strip() + "\n"

def process_page(rel_html, rel_md, canonical_url, locale):
    html_path = SITE_ROOT / rel_html
    md_path = SITE_ROOT / rel_md

    if not html_path.exists():
        print(f"[SKIP] File not found: {rel_html}")
        return

    content = html_path.read_text(encoding="utf-8")

    # 1. Inject Apollo Tracker if not present
    if "initApollo" not in content and "tracker.iife.js" not in content:
        if "</head>" in content:
            content = content.replace("</head>", f"{APOLLO_SCRIPT}</head>", 1)
            print(f"[APOLLO INJECTED] {rel_html}")
        else:
            print(f"[WARN] No </head> in {rel_html}")
    else:
        print(f"[APOLLO ALREADY PRESENT] {rel_html}")

    # 2. Inject Markdown alternate link if not present
    md_url = canonical_url.rstrip("/") + ("" if canonical_url.endswith(".html") else "/" + Path(rel_md).name)
    if not canonical_url.endswith("/"):
        md_url = canonical_url.replace(".html", ".md")
    else:
        md_url = f"https://hsnlabs.ai/{rel_md}"

    link_tag = f'  <link rel="alternate" type="text/markdown" href="{md_url}">'
    if 'rel="alternate" type="text/markdown"' not in content:
        if '<link rel="canonical"' in content:
            content = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1\n' + link_tag, content, count=1)
            print(f"[MD LINK INJECTED] {rel_html} -> {md_url}")
        elif '</head>' in content:
            content = content.replace("</head>", f"{link_tag}\n</head>", 1)
            print(f"[MD LINK INJECTED at head] {rel_html} -> {md_url}")
    else:
        print(f"[MD LINK ALREADY PRESENT] {rel_html}")

    # Write updated HTML
    html_path.write_text(content, encoding="utf-8")

    # 3. Generate clean Markdown file
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_text = extract_clean_markdown(content, canonical_url, locale)
    md_path.write_text(md_text, encoding="utf-8")
    print(f"[MD GENERATED] {rel_md} ({len(md_text)} chars)")

def main():
    print(f"Starting Apollo & M2M Setup across {len(PAGES)} pages...")
    for rel_html, rel_md, canonical_url, locale in PAGES:
        process_page(rel_html, rel_md, canonical_url, locale)
    print("Done processing pages.")

if __name__ == "__main__":
    main()
