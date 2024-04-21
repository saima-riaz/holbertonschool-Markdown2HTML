#!/usr/bin/python3
"""
markdown2html.py: Convert Markdown headings to HTML
"""

import sys
import os.path

def parse_heading(line):
    ''' Parse and convert Markdown headings to HTML '''
    # Count the number of '#' characters at the beginning of the line
    heading_num = len(line) - len(line.lstrip('#'))
    # Check if the line is a heading (1 to 6 '#' characters)
    if 1 <= heading_num <= 6:
        # Generate HTML for the heading
        return f'<h{heading_num}>{line.lstrip("#").strip()}</h{heading_num}>\n'
    # If not a heading, return the line unchanged
    return line

def convert_markdown_to_html(input_file, output_file):
    ''' Convert Markdown file to HTML '''
    # Read the Markdown file line by line
    with open(input_file, 'r') as f:
        markdown_lines = f.readlines()

    # Parse each line of Markdown and convert headings to HTML
    html_lines = [parse_heading(line) for line in markdown_lines]

    # Write the HTML lines to the output file
    with open(output_file, 'w') as f:
        f.writelines(html_lines)

def main():
    ''' Main function '''
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: markdown2html.py <input_file> <output_file>")
        sys.exit(1)

    # Get input and output file paths from command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # Convert Markdown to HTML and write to output file
    convert_markdown_to_html(input_file, output_file)
    print(f"Conversion successful. HTML written to '{output_file}'.")

if __name__ == "__main__":
    main()
