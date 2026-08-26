#!/usr/bin/env python3
import http.server
import socketserver
import os
import markdown_it
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

PORT = 8080

class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
            with open(readme_path, "r", encoding="utf-8") as f:
                md_content = f.read()

            md = markdown_it.MarkdownIt("commonmark", {"html": True})
            html_body = md.render(md_content)
            
            # Simple syntax highlighter replacement for code blocks
            formatter = HtmlFormatter(style="monokai", full=False)
            pygments_css = HtmlFormatter(style="monokai").get_style_defs('.highlight')

            full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Satyansh Gaur - Profile Preview</title>
  <style>
    body {{
      background-color: #0d1117;
      color: #c9d1d9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      line-height: 1.6;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
    }}
    a {{ color: #58a6ff; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    hr {{ border: 0; border-top: 1px solid #21262d; margin: 24px 0; }}
    h1, h2, h3, h4 {{ color: #f0f6fc; font-weight: 600; margin-top: 24px; }}
    h2 {{ font-size: 1.6em; border-bottom: 1px solid #21262d; padding-bottom: 8px; }}
    h3 {{ font-size: 1.3em; }}
    pre {{
      background-color: #161b22;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 16px;
      overflow-x: auto;
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
      font-size: 13.5px;
      color: #e6edf3;
    }}
    code {{
      font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Menlo, monospace;
    }}
    img {{
      border-radius: 12px;
      max-width: 100%;
    }}
    {pygments_css}
  </style>
</head>
<body>
  {html_body}
</body>
</html>"""
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(full_html.encode("utf-8"))
        else:
            super().do_GET()

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), MarkdownHandler) as httpd:
    print(f"[*] Local preview server running at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
