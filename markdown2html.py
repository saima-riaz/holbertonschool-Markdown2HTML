#!/usr/bin/python3

"""
markdown2html.py

A script to convert Markdown files to HTML format.

Usage:
    markdown2html.py <input_file> <output_file>
"""

import sys

def markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as markdown_file:
        markdown_lines = markdown_file.readlines()

    with open(output_file, 'w') as html_file:
        in_list = False
        in_paragraph = False
        for line in markdown_lines:
            line = line.strip()
            if line.startswith('#'):
                html_file.write(f'<h1>{line[1:].strip()}</h1>\n')
            elif line.startswith('*') or line.startswith('-'):
                if not in_list:
                    html_file.write('<ul>\n')
                    in_list = True
                html_file.write(f'    <li>{line[1:].strip()}</li>\n')
            elif line.strip() == '':
                if in_list:
                    html_file.write('</ul>\n')
                    in_list = False
                if in_paragraph:
                    html_file.write('</p>\n')
                    in_paragraph = False
            else:
                if not in_paragraph:
                    html_file.write('<p>\n')
                    in_paragraph = True
                html_file.write(f'    {line}\n')
        if in_list:
            html_file.write('</ul>\n')
        if in_paragraph:
            html_file.write('</p>\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: markdown2html.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    markdown_to_html(input_file, output_file)
