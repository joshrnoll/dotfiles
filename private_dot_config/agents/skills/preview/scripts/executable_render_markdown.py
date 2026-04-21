#!/opt/homebrew/bin/python3
import argparse
import html
import pathlib
import re
import subprocess
import sys


def inline_format(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def render_markdown(md: str) -> str:
    lines = md.splitlines()
    out = []
    in_code = False
    code_lines = []
    in_list = False
    para = []

    def flush_para():
        nonlocal para
        if para:
            out.append(f"<p>{inline_format(' '.join(x.strip() for x in para))}</p>")
            para = []

    def flush_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    def flush_code():
        nonlocal in_code, code_lines
        if in_code:
            out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
            in_code = False
            code_lines = []

    for line in lines:
        if line.startswith("```"):
            flush_para()
            flush_list()
            if in_code:
                flush_code()
            else:
                in_code = True
                code_lines = []
            continue

        if in_code:
            code_lines.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            flush_para()
            flush_list()
            continue

        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            flush_para()
            flush_list()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline_format(m.group(2).strip())}</h{level}>")
            continue

        if re.match(r'^---+$', stripped):
            flush_para()
            flush_list()
            out.append("<hr />")
            continue

        m = re.match(r'^\s*[-*]\s+(.*)$', line)
        if m:
            flush_para()
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline_format(m.group(1).strip())}</li>")
            continue

        flush_list()
        para.append(line)

    flush_para()
    flush_list()
    flush_code()

    body = "\n".join(out)
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Markdown Preview</title>
  <style>
    :root {{ color-scheme: light dark; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif; max-width: 860px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
    code {{ background: rgba(127,127,127,.15); padding: .1em .35em; border-radius: 6px; }}
    pre {{ background: rgba(127,127,127,.12); padding: 16px; border-radius: 10px; overflow-x: auto; }}
    pre code {{ background: transparent; padding: 0; }}
    h1,h2,h3,h4,h5,h6 {{ line-height: 1.25; }}
    a {{ text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    hr {{ border: 0; border-top: 1px solid rgba(127,127,127,.35); margin: 24px 0; }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown to standalone HTML.")
    parser.add_argument("input", help="Input markdown file")
    parser.add_argument("output", nargs="?", help="Output HTML file")
    parser.add_argument("--open", action="store_true", dest="open_browser", help="Open output in browser")
    args = parser.parse_args()

    input_path = pathlib.Path(args.input).expanduser()
    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 1

    output_path = pathlib.Path(args.output).expanduser() if args.output else input_path.with_suffix(".html")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    md = input_path.read_text(encoding="utf-8")
    html_doc = render_markdown(md)
    output_path.write_text(html_doc, encoding="utf-8")
    print(output_path)

    if args.open_browser:
        subprocess.run(["open", str(output_path)], check=False)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
