#!/usr/bin/env python3
"""把 Mörk Borg 中文 md 转换为按页分页的 HTML。浏览器 Cmd+P 即可存 PDF。"""
import re
import sys
import subprocess
from pathlib import Path

BASE = Path("/Users/jack/Projects/trpg-projects/dnd-rules-import/source/Mork Borg/md files")
MD = BASE / "Mork Borg Core Rulebook (ZH).md"
OUT = BASE / "Mork Borg Core Rulebook (ZH).html"

text = MD.read_text(encoding="utf-8")

# 提取标题（第一行 #）
title_match = re.match(r"^#\s+(.+)", text)
title = title_match.group(1).strip() if title_match else "Mörk Borg ZH"
body = text[title_match.end():] if title_match else text

# 按 `## 第 N 页` 切页
parts = re.split(r"(?=^##\s+(?:第\s*\d+\s*页|附录))", body, flags=re.MULTILINE)
pages = [p.strip() for p in parts if p.strip() and p.strip() != "---"]

# 用 python-markdown 渲染每页；若未装，用简易转换
try:
    import markdown
    def md2html(s):
        return markdown.markdown(s, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
except ImportError:
    print("未装 markdown 包，尝试安装...", file=sys.stderr)
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "markdown"])
    import markdown
    def md2html(s):
        return markdown.markdown(s, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])

page_htmls = []
page_numbers = []
for p in pages:
    p = re.sub(r"\n---\s*$", "", p.strip())
    # 从页首标题提取页码（附录无页码）
    m = re.match(r"^##\s+第\s*(\d+)\s*页", p)
    page_numbers.append(m.group(1) if m else None)
    # 去掉页标题里的「第 N 页 — 」前缀，只保留标题
    p = re.sub(r"^(##\s+)第\s*\d+\s*页\s*[—\-－]\s*", r"\1", p)
    page_htmls.append(md2html(p))

CSS = """
@import url('https://fonts.googleapis.com/css2?family=UnifrakturMaguntia&family=EB+Garamond:ital,wght@0,400;0,700;1,400&family=Oswald:wght@400;700&family=Noto+Serif+SC:wght@400;700;900&display=swap');

@page { size: A4; margin: 12mm; }
body {
  font-family: "EB Garamond", "Noto Serif SC", "Songti SC", "Hiragino Sans GB", serif;
  background: #e8e8e8;
  color: #000;
  margin: 0;
  line-height: 1.6;
  font-size: 17px;
  font-variant-numeric: lining-nums tabular-nums;
  font-feature-settings: "lnum", "tnum";
}
/* 数字单独用干净字体（避免 IM Fell 的旧体数字把 0 写成 o） */
.num, td, th, code, strong {
  font-feature-settings: "lnum", "tnum";
}
.page {
  max-width: 780px;
  margin: 30px auto;
  padding: 44px 56px;
  background: #fff;
  color: #000;
  box-shadow: 0 2px 10px rgba(0,0,0,0.15);
  page-break-after: always;
  break-after: page;
  min-height: 1000px;
  position: relative;
}
.page:last-child { page-break-after: auto; }
.page-num {
  position: absolute;
  top: 14px;
  right: 22px;
  font-family: "Oswald", sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 3px;
  opacity: 0.6;
}

h1 {
  font-family: "UnifrakturMaguntia", "Noto Serif SC", serif;
  font-weight: normal;
  letter-spacing: 1px;
  line-height: 1.2;
  color: #000;
}
h2 {
  font-family: "Oswald", "Noto Serif SC", serif;
  font-weight: 700;
  letter-spacing: 2px;
  line-height: 1.25;
  color: #000;
}
h3, h4 {
  font-family: "Oswald", "Noto Serif SC", serif;
  font-weight: 700;
  color: #000;
  line-height: 1.3;
}
h1 { font-size: 38px; border-bottom: 3px solid #000; padding-bottom: 10px; margin-top: 0; }
h2 { font-size: 30px; margin-top: 0; border-bottom: 2px solid #000; padding-bottom: 6px; }
h3 { font-size: 22px; margin-top: 20px; letter-spacing: 2px; }
h4 { font-size: 17px; text-transform: uppercase; letter-spacing: 2px; }

p, li, td, th { font-family: "EB Garamond", "Noto Serif SC", "Songti SC", serif; }
table { border-collapse: collapse; margin: 14px 0; font-size: 16px; width: 100%; }
th, td { border: 1px solid #000; padding: 8px 12px; vertical-align: middle; line-height: 1.5; }
td:first-child { white-space: nowrap; font-weight: 600; text-align: center; }
/* 价格列（含 "s" 的单元格）右对齐 */
td { font-variant-numeric: tabular-nums; }
.name-table { margin: 20px auto; border-collapse: separate; border-spacing: 0; }
.name-table td, .name-table th { text-align: center; padding: 4px 14px; border: 1px solid #000; }
.name-table .spacer, .weather-table .spacer { border: none !important; width: 28px; background: transparent; padding: 0; }
.weather-table { margin: 20px auto; border-collapse: separate; border-spacing: 0; }
.weather-table td { text-align: center; padding: 4px 14px; border: 1px solid #000; }
.index-table { margin: 10px auto; border-collapse: separate; border-spacing: 0; width: 100%; font-size: 14px; }
.index-table td { padding: 3px 10px; border: none; }
.index-table td:nth-child(2), .index-table td:nth-child(5) { text-align: right; font-weight: 700; border-bottom: 1px dotted #999; min-width: 30px; }
.index-table td:nth-child(1), .index-table td:nth-child(4) { border-bottom: 1px dotted #999; }
.index-table .spacer { border: none !important; width: 30px; }
.cheat-grid { display: flex; flex-direction: column; gap: 14px; }
.cheat-grid .card {
  border: 2px solid #000;
  padding: 10px 16px;
  background: #fafafa;
  page-break-inside: avoid;
}
.cheat-grid .card h3 {
  font-family: "Oswald", sans-serif;
  font-size: 18px;
  margin: 0 0 8px 0;
  padding: 4px 8px;
  background: #000;
  color: #fff;
  letter-spacing: 2px;
  text-transform: uppercase;
}
.cheat-grid .card table { margin: 6px 0; font-size: 14px; }
.cheat-grid .card td, .cheat-grid .card th { padding: 4px 8px; }
.cheat-grid .card ul, .cheat-grid .card ol { margin: 4px 0; }
.cheat-grid .card p { margin: 4px 0; }
.group-header {
  display: block !important;
  font-family: "UnifrakturMaguntia", serif !important;
  font-size: 22px !important;
  font-weight: normal !important;
  border: none !important;
  border-top: 2px solid #000 !important;
  border-bottom: 2px solid #000 !important;
  padding: 4px 12px !important;
  margin: 8px 0 4px 0 !important;
  text-align: center !important;
  letter-spacing: 3px !important;
}
.zh-name { display: block; font-size: 12px; color: #555; font-family: "Noto Serif SC", "Songti SC", serif; letter-spacing: 1px; margin-top: 2px; }
th { background: #eee; font-family: "Oswald", sans-serif; text-transform: uppercase; letter-spacing: 1.5px; font-size: 14px; padding: 10px 12px; text-align: center; }
code { background: #eee; padding: 1px 4px; border-radius: 2px; font-size: 90%; }
blockquote {
  border-left: 4px solid #000;
  margin: 12px 0;
  padding: 6px 16px;
  background: #f4f4f4;
  font-style: italic;
}
ul, ol { padding-left: 16px; list-style: none; }
ol { list-style: decimal; padding-left: 24px; }
li { margin: 4px 0; }
hr { display: none; }
strong { font-weight: 700; }

.cover h1 {
  font-family: "UnifrakturMaguntia", serif;
  font-size: 56px;
  border: none;
  line-height: 1.1;
  margin-bottom: 20px;
}
.cover { text-align: center; padding-top: 180px !important; }

@media print {
  body { background: white; }
  .page { box-shadow: none; margin: 0; padding: 12mm 14mm; min-height: auto; }
}
"""

html = f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<div class="page cover">
  <h1 style="border:none; font-size:36px;">{title}</h1>
</div>
"""

for i, ph in enumerate(page_htmls):
    pn = page_numbers[i]
    label = f"p. {pn}" if pn else "附录"
    html += f'<div class="page"><span class="page-num">{label}</span>\n{ph}\n</div>\n'

html += "</body></html>"

OUT.write_text(html, encoding="utf-8")
print(f"写入: {OUT}")
print(f"页数: {len(pages)}")
