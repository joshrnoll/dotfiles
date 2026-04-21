---
name: preview
description: Render markdown into HTML and open it in the browser. Use when the user asks to preview the previous response or a markdown file as HTML.
---

# Preview

Render markdown into a standalone HTML file and open it in the browser.

## When to use

Use this skill when the user asks to:
- preview the previous assistant response in a browser
- render a markdown file as HTML
- open generated documentation as HTML locally

## What I will do

1. If the user asked to clean previews, remove generated `*.md` and `*.html` files from `~/tmp/previews/` and report what was deleted
2. Otherwise, determine the markdown source:
   - prefer a user-specified markdown file if provided
   - otherwise use the previous assistant response as the markdown source
3. Write the markdown to `~/tmp/previews/` if needed
4. Render it to HTML using `scripts/render_markdown.py`
5. Open the HTML file in the browser with `open`
6. Report the markdown and HTML file paths back to the user

## Commands

From this skill directory:

```bash
python3 scripts/render_markdown.py ~/tmp/previews/input.md ~/tmp/previews/output.html --open
```

If no output path is given, the script derives one next to the input file.

## Notes

- The renderer is intentionally lightweight and supports common markdown constructs well enough for local preview.
- Prefer `~/tmp/previews/` for generated preview artifacts.
- If the user asked to preview the previous response, preserve the exact response text when writing the markdown file.
- For cleanup, only delete generated markdown and HTML preview artifacts in `~/tmp/previews/`.
