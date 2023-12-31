#!/usr/bin/python3
"""
Script converts Markdown file to HTML.
"""

import sys
import os
import re


def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check if the input file exists
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # # Get the input and output file names from the arguments
    # input_file = sys.argv[1]
    # output_file = sys.argv[2]

    # Read Markdown file and conevert it to HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        for line in f:
            # Check for Markdown headings
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                html_lines.append(
                    f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                html_lines.append(line.rstrip())

    # Write HTML content to the output file
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write("\n".join(html_lines))


if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit with success status code
    sys.exit(0)
