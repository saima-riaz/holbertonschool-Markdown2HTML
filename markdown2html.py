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


def parse_heading(line):
    ''' Parse and convert Markdown headings to HTML '''
    heading_num = len(line) - len(line.lstrip('#'))
    if 1 <= heading_num <= 6:
        return f'<h{heading_num}>{line.lstrip("#").strip()}</h{heading_num}>\n'
    return line


def parse_unordered_list(line):
    ''' Parse and convert Markdown unordered lists to HTML '''
    if line.lstrip().startswith('-'):
        return f'<li>{line.lstrip("-").strip()}</li>\n'
    return line


def parse_ordered_list(line):
    ''' Parse and convert Markdown ordered lists to HTML '''
    if line.lstrip().startswith('*'):
        return f'<li>{line.lstrip("*").strip()}</li>\n'
    return line


def parse_paragraph(line):
    ''' Parse and convert Markdown paragraphs to HTML '''
    if len(line.strip()) > 0:
        return f'<p>{line.strip()}</p>\n'
    return line


def parse_bold_and_emphasis(line):
    ''' Parse and convert Markdown bold and emphasis text to HTML '''
    line = re.sub(r'\*\*(.*?)\*\*', lambda x: f'<b>{x.group(1)}</b>', line)
    line = re.sub(r'__(.*?)__', lambda x: f'<em>{x.group(1)}</em>', line)
    return line


def md5_substitution(match):
    ''' Substitute MD5 hash in [[...]] '''
    return hashlib.md5(match.group(1).encode()).hexdigest()


def remove_c_substitution(match):
    ''' Remove 'c' and 'C' from ((...)) '''
    return match.group(1).replace('c', '').replace('C', '')


def parse_special_cases(line):
    ''' Parse and convert special cases to HTML '''
    line = re.sub(r'\[\[(.*?)\]\]', md5_substitution, line)
    line = re.sub(r'\(\((.*?)\)\)', remove_c_substitution, line)
    return line


def convert_markdown_to_html(markdown_file, html_file):
    ''' Convert Markdown file to HTML '''
    with open(markdown_file) as md, open(html_file, 'w') as html:
        for line in md:
            line = parse_heading(line)
            line = parse_unordered_list(line)
            line = parse_ordered_list(line)
            line = parse_bold_and_emphasis(line)
            line = parse_special_cases(line)
            line = parse_paragraph(line)
            html.write(line)


def check_arguments():
    ''' Check command line arguments '''
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    check_arguments()
    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.exit(0)