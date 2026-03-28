#!/usr/bin/env python3
"""TRPG PDF 文本提取工具

用法：
  python3 pdf_extract.py <pdf_path> [options]

示例：
  # 提取全部页面到 txt
  python3 pdf_extract.py "/Users/jack/Projects/Rule Books/CoC/克苏鲁的呼唤40周年纪念版.pdf"

  # 提取指定页码范围
  python3 pdf_extract.py "/Users/jack/Projects/Rule Books/D&D 5e/Core/5eDnD_PHB_中译v1.72版.pdf" --pages 10-30

  # 提取多个范围
  python3 pdf_extract.py some.pdf --pages 1-5,10-20,50-60

  # 输出到指定文件
  python3 pdf_extract.py some.pdf --pages 10-30 -o chapter3.txt

  # 仅输出到 stdout（不写文件，方便管道）
  python3 pdf_extract.py some.pdf --pages 10-15 --stdout

  # 显示 PDF 总页数和目录
  python3 pdf_extract.py some.pdf --info

依赖：pymupdf (pip3 install pymupdf)

说明：
  使用 pymupdf 的 get_text() 提取，能捕获 PDF 中所有文本，
  包括 TRPG 书籍中常见的侧栏、数据块（stat block）、文本框等
  pymupdf4llm 会遗漏的内容。

  每页以 "===== PAGE X / TOTAL =====" 分隔，方便定位。
"""

from __future__ import annotations

import argparse
import os
import sys

try:
    import pymupdf
except ImportError:
    print("需要安装 pymupdf: pip3 install pymupdf", file=sys.stderr)
    sys.exit(1)


def parse_page_ranges(spec: str, total: int) -> list[int]:
    """解析页码范围字符串，如 '1-5,10-20,50'，返回 0-based 页码列表。"""
    pages = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start = max(1, int(start))
            end = min(total, int(end))
            pages.extend(range(start - 1, end))
        else:
            p = int(part)
            if 1 <= p <= total:
                pages.append(p - 1)
    return sorted(set(pages))


def extract_text(pdf_path: str, pages: list[int] | None = None) -> str:
    """从 PDF 提取文本。pages 为 0-based 页码列表，None 表示全部。"""
    doc = pymupdf.open(pdf_path)
    total = len(doc)

    if pages is None:
        pages = list(range(total))

    parts = []
    for i in pages:
        if 0 <= i < total:
            page = doc[i]
            text = page.get_text()
            parts.append(f"\n{'=' * 60}")
            parts.append(f"PAGE {i + 1} / {total}")
            parts.append(f"{'=' * 60}")
            parts.append(text)

    doc.close()
    return "\n".join(parts)


def show_info(pdf_path: str):
    """显示 PDF 基本信息和目录。"""
    doc = pymupdf.open(pdf_path)
    print(f"文件：{pdf_path}")
    print(f"页数：{len(doc)}")
    size_mb = os.path.getsize(pdf_path) / 1024 / 1024
    print(f"大小：{size_mb:.1f} MB")

    toc = doc.get_toc()
    if toc:
        print(f"\n目录（{len(toc)} 项）：")
        for level, title, page in toc:
            indent = "  " * (level - 1)
            print(f"  {indent}{title} ... p.{page}")
    else:
        print("\n（无内嵌目录）")

    doc.close()


def main():
    parser = argparse.ArgumentParser(description="TRPG PDF 文本提取工具")
    parser.add_argument("pdf", help="PDF 文件路径")
    parser.add_argument("--pages", "-p", help="页码范围，如 1-5,10-20,50")
    parser.add_argument("--output", "-o", help="输出文件路径（默认：同名.txt）")
    parser.add_argument("--stdout", action="store_true", help="输出到 stdout 而非文件")
    parser.add_argument("--info", action="store_true", help="仅显示 PDF 信息和目录")
    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"文件不存在：{args.pdf}", file=sys.stderr)
        sys.exit(1)

    if args.info:
        show_info(args.pdf)
        return

    doc = pymupdf.open(args.pdf)
    total = len(doc)
    doc.close()

    pages = None
    if args.pages:
        pages = parse_page_ranges(args.pages, total)
        print(f"提取 {len(pages)} 页（共 {total} 页）...", file=sys.stderr)
    else:
        print(f"提取全部 {total} 页...", file=sys.stderr)

    text = extract_text(args.pdf, pages)

    if args.stdout:
        print(text)
    else:
        out_path = args.output
        if not out_path:
            base = os.path.splitext(args.pdf)[0]
            out_path = base + ".txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        size_kb = os.path.getsize(out_path) / 1024
        print(f"已写入：{out_path}（{size_kb:.0f} KB）", file=sys.stderr)


if __name__ == "__main__":
    main()
