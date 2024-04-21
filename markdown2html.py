#!/usr/bin/python3
"""
This script, markdown2html.py, takes two string arguments:
- The first argument is the name of the Markdown file.
- The second argument is the output file name.
It converts Markdown headings in the file to HTML heading tags.
"""

import sys
import os


def parse_heading(line):
    """Parse and convert Markdown headings to HTML.

    Args:
        line (str): A string from the Markdown file.

    Returns:
        str: A string formatted as an HTML heading if the line is a
        Markdown heading,
        otherwise returns the line unchanged.
    """
    # Remove leading spaces and count the number of '#' characters
    stripped_line = line.lstrip()
    heading_num = len(stripped_line) - len(stripped_line.lstrip('#'))

    # Check if the line is a valid Markdown heading
    if 1 <= heading_num <= 6:
        # Remove '#' characters and any leading/trailing spaces from the text
        content = stripped_line[heading_num:].strip()
        return f"<h{heading_num}>{content}</h{heading_num}>\n"
    return line


def convert_markdown_to_html(markdown_file, output_file):
    """Convert Markdown file to HTML.

    Args:
        markdown_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.
    """
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_lines = md_file.readlines()
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    html_content = ""
    for line in markdown_lines:
        html_content += parse_heading(line)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <MarkdownFile> <OutputFile>", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)

    sys.exit(0)
