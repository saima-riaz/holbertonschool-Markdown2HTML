#!/usr/bin/env python3

#script markdown2html.py that takes an argument 2 strings:

# First argument is the name of the Markdown file
# Second argument is the output file name

import sys
import os

def convert_markdown_to_html(markdown_file, output_file):
    try:
        with open(markdown_file, 'r') as md:
            markdown_content = md.read()
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML (you may use your preferred method here)
    # For example, you can use a Markdown library like markdown2 or mistune

    # For demonstration purposes, let's just copy the content as is
    html_content = markdown_content

    with open(output_file, 'w') as html:
        html.write(html_content)

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <MarkdownFile> <OutputFile>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(markdown_file, output_file)

    sys.exit(0)
