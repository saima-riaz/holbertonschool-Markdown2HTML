#!/usr/bin/python3
"""
Converts a Markdown file to HTML.
"""

import sys
import os.path

def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts Markdown file to HTML.

    Args:
        markdown_file (str): Path to the Markdown file.
        output_file (str): Path to the output HTML file.
    """
    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # Your Markdown to HTML conversion logic goes here
    # This is just a placeholder

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    # Get input and output file paths from command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Convert Markdown to HTML
    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
