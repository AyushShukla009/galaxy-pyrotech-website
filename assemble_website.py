# Master assembler script to create the production index.html
import os
import sys

from generate_index import get_html_head
from styles import get_css
from content import get_svg_sprites, get_body
from scripts import get_javascript

def assemble():
    print("Assembling production index.html...")
    head = get_html_head()
    css = get_css()
    svg = get_svg_sprites()
    body = get_body()
    js = get_javascript()

    # Clean valid HTML concatenation without escaped literal backslashes
    full_html = head.rstrip() + "\n" + css.strip() + "\n</head>\n<body>\n" + svg.strip() + "\n" + body.strip() + "\n" + js.strip()

    out_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    size = os.path.getsize(out_path)
    print(f"Successfully generated clean index.html ({size:,} bytes)")

if __name__ == "__main__":
    assemble()
