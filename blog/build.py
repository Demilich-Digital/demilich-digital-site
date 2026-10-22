#!/usr/bin/env python3
"""Render blog/*.md into themed HTML pages and refresh the home page blog list.

Each post starts with a front matter block:

    ---
    title: Post Title
    date: 2026-10-22
    summary: One or two sentences shown on the home page.
    ---

Top-level "#" headings in a post become its sections (and its "On this page"
outline); "##" become subsections. Run from anywhere:

    python3 blog/build.py

Requires the `markdown` package (pip install markdown). The generated .html
files are committed, since GitHub Pages serves the repo as-is.
"""
import datetime
import html
import pathlib
import re

import markdown

BLOG_DIR = pathlib.Path(__file__).resolve().parent
INDEX = BLOG_DIR.parent / "index.html"
TEMPLATE = BLOG_DIR / "post.template.html"
LIST_RE = re.compile(r"(<!-- BLOG:START[^>]*-->\n).*?(<!-- BLOG:END -->)", re.S)


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"{path.name}: missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    for key in ("title", "date", "summary"):
        if not meta.get(key):
            raise SystemExit(f"{path.name}: front matter needs '{key}'")
    meta["date"] = datetime.date.fromisoformat(meta["date"])
    meta["slug"] = path.stem
    meta["body"] = text[m.end():]
    return meta


def render_body(source):
    body = markdown.markdown(source, extensions=["toc", "smarty", "fenced_code", "tables"])
    # The page title is the <h1>, so shift every heading in the post down a level.
    body = re.sub(r"<(/?)h([1-5])\b", lambda m: f"<{m.group(1)}h{int(m.group(2)) + 1}", body)
    # The page runtime treats {{ ... }} as a binding; keep literal braces literal.
    body = body.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")
    sections = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    return body, sections


def fmt_date(d):
    return f"{d:%B} {d.day}, {d.year}"


def render_post(post, template):
    body, sections = render_body(post["body"])
    outline = "\n".join(
        f'        <li style="color:{{{{ t.textMuted }}}};"><a href="#{sid}" style="color:{{{{ t.textSecondary }}}};">{label}</a></li>'
        for sid, label in sections
    )
    out = template
    for key, value in {
        "TITLE": html.escape(post["title"]),
        "SUMMARY": html.escape(post["summary"]),
        "DATE_ISO": post["date"].isoformat(),
        "DATE": fmt_date(post["date"]),
        "OUTLINE": outline,
        "BODY": body,
    }.items():
        out = out.replace(f"%%{key}%%", value)
    (BLOG_DIR / f"{post['slug']}.html").write_text(out, encoding="utf-8")


def render_list(posts):
    entries = []
    for post in posts:
        entries.append(f"""      <a data-blog-entry href="./blog/{post['slug']}.html" style="display:grid; grid-template-columns:160px 1fr auto; gap:32px; align-items:baseline; background:{{{{ t.cardBg }}}}; padding:32px 28px; text-decoration:none;">
        <time datetime="{post['date'].isoformat()}" style="font-family:'IBM Plex Mono', monospace; font-size:13px; color:{{{{ t.textMuted }}}};">{post['date'].isoformat()}</time>
        <div>
          <h3 style="font-family:'IBM Plex Mono', monospace; font-size:19px; color:{{{{ t.textPrimary }}}}; margin:0 0 10px;">{html.escape(post['title'])}</h3>
          <p style="font-size:15px; line-height:1.6; color:{{{{ t.textSecondary }}}}; margin:0;">{html.escape(post['summary'])}</p>
        </div>
        <span style="font-family:'IBM Plex Mono', monospace; font-size:13px; color:{{{{ t.textPrimary }}}};">Read &rarr;</span>
      </a>""")
    page = INDEX.read_text(encoding="utf-8")
    if not LIST_RE.search(page):
        raise SystemExit("index.html: BLOG:START/BLOG:END markers not found")
    listing = "\n".join(entries) + "\n" if entries else ""
    INDEX.write_text(LIST_RE.sub(lambda m: m.group(1) + listing + m.group(2), page), encoding="utf-8")


def main():
    template = TEMPLATE.read_text(encoding="utf-8")
    posts = sorted((parse(p) for p in BLOG_DIR.glob("*.md")), key=lambda p: p["date"], reverse=True)
    for post in posts:
        render_post(post, template)
        print(f"blog/{post['slug']}.html")
    render_list(posts)
    print(f"index.html ({len(posts)} posts listed)")


if __name__ == "__main__":
    main()
