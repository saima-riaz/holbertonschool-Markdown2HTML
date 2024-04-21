#!/usr/bin/python3

import sys

def markdown_to_html(md_file, html_file):
    """
    Convert Markdown syntax to HTML syntax for headings and lists.

    Args:
        md_file (str): Path to the input Markdown file.
        html_file (str): Path to the output HTML file.
    """
    with open(md_file, 'r') as md:
        markdown_content = md.readlines()

    html_content = ""
    in_list = False
    is_ordered_list = False

    for line in markdown_content:
        if line.startswith("#"):
            html_content += f"<h1>{line.strip('#').strip()}</h1>"
        elif line.startswith("*"):
            if not in_list or is_ordered_list:
                html_content += "<ul>"
                in_list = True
                is_ordered_list = False
            html_content += f"<li>{line.strip('*').strip()}</li>"
        elif line.startswith("1."):
            if not in_list or not is_ordered_list:
                html_content += "<ol>"
                in_list = True
                is_ordered_list = True
            html_content += f"<li>{line.strip('1.').strip()}</li>"
        else:
            if in_list:
                if is_ordered_list:
                    html_content += "</ol>"
                else:
                    html_content += "</ul>"
                in_list = False
            html_content += line

    if in_list:
        if is_ordered_list:
            html_content += "</ol>"
        else:
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
