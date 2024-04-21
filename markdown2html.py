#!/usr/bin/python3
"""
Write a script markdown2html.py that takes two string arguments:

    First argument is the name of the Markdown file
    Second argument is the output file name
"""

import sys
import os.path
import re
import hashlib

def markdown_to_html(md_file, html_file):
    with open(md_file, 'r') as md:
        markdown_content = md.readlines()

    html_content = ""
    in_list = False

    for line in markdown_content:
        if line.startswith("#"):
            html_content += f"<h1>{line.strip('#').strip()}</h1>"
        elif line.startswith("-"):
            if not in_list:
                html_content += "<ul>"
                in_list = True
            html_content += f"<li>{line.strip('-').strip()}</li>"
        else:
            if in_list:
                html_content += "</ul>"
                in_list = False
            html_content += line

    if in_list:
        html_content += "</ul>"

    with open(html_file, 'w') as html:
        html.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: markdown2html.py input.md output.html")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    markdown_to_html(input_file, output_file)
