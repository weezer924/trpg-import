#!/usr/bin/env python3
"""批量将 PDF 转换为纯文本文件。

使用 pymupdf 的 get_text() 捕获所有文本，包括侧栏和数据块。

用法：
  # 转换指定目录下所有 PDF
  python3 convert_pdfs.py "/Users/jack/Projects/Rule Books/CoC"

  # 转换单个文件
  python3 convert_pdfs.py "/Users/jack/Projects/Rule Books/OSE/OSE Basic Rules.pdf"

  # 指定输出目录
  python3 convert_pdfs.py "/Users/jack/Projects/Rule Books/Cairn" -o /tmp/cairn_txt
"""

import pymupdf
import argparse
import os
import sys


def convert_pdf(pdf_path: str, output_dir: str | None = None) -> str:
    """将单个 PDF 转换为 txt，返回输出路径。"""
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        txt_name = os.path.splitext(os.path.basename(pdf_path))[0] + ".txt"
        txt_path = os.path.join(output_dir, txt_name)
    else:
        txt_path = os.path.splitext(pdf_path)[0] + ".txt"

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)

    with open(txt_path, "w", encoding="utf-8") as f:
        for i, page in enumerate(doc):
            text = page.get_text()
            f.write(f"\n{'=' * 60}\n")
            f.write(f"PAGE {i + 1} / {total_pages}\n")
            f.write(f"{'=' * 60}\n")
            f.write(text)

    doc.close()
    size_mb = os.path.getsize(txt_path) / 1024 / 1024
    print(f"  {os.path.basename(pdf_path)} -> {txt_path} ({total_pages} pages, {size_mb:.1f} MB)")
    return txt_path


def main():
    parser = argparse.ArgumentParser(description="批量将 TRPG PDF 转换为纯文本")
    parser.add_argument("path", help="PDF 文件或包含 PDF 的目录")
    parser.add_argument("--output", "-o", help="输出目录（默认：与 PDF 同目录）")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"路径不存在：{args.path}", file=sys.stderr)
        sys.exit(1)

    if os.path.isfile(args.path):
        convert_pdf(args.path, args.output)
    else:
        pdfs = sorted(
            os.path.join(root, f)
            for root, _, files in os.walk(args.path)
            for f in files
            if f.lower().endswith(".pdf")
        )
        if not pdfs:
            print(f"目录中没有找到 PDF：{args.path}", file=sys.stderr)
            sys.exit(1)
        print(f"找到 {len(pdfs)} 个 PDF，开始转换...")
        for pdf in pdfs:
            convert_pdf(pdf, args.output)

    print("\nDone!")


if __name__ == "__main__":
    main()
