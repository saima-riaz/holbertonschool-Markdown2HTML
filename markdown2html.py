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


def check_arguments():
    """Check if the number of command-line arguments is
    correct and files exist."""
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
def convert_markdown_to_html(markdown_file, html_file):
    ''' Convert Markdown file to HTML '''
    with open(markdown_file) as md, open(html_file, 'w') as html:
        for line in md:
            line = parse_heading(line)



if __name__ == '__main__':
    check_arguments()
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.exit(0)
