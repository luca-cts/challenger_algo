#!/usr/bin/env python3
"""
search.py

Search for Python files in the '../algorithm' subdirectory.
- If a tag_name is given as an argument, print files whose tag comment includes that tag.
- If no argument is given, print all files with their tag comments.
"""

import re
import sys
from pathlib import Path


def find_tagged_py_files(tag_name: str = None):
    base_dir = Path(__file__).resolve().parent
    algo_dir = base_dir / "algorithm"
    # print(f"Searching in directory: {algo_dir}")
    # Refactored pattern: match lines starting with "# tag:" and capture comma-separated tags
    tag_pattern = re.compile(r"^\s*#\s*tag:\s*([a-zA-Z0-9_,\s-]+)", re.IGNORECASE)

    found = False
    for py_file in algo_dir.glob("*.py"):
        tags = []
        with py_file.open(encoding="utf-8") as f:
            for line in f:
                # print(line, end="")  # Print the line to show the file content
                match = tag_pattern.match(line)
                if match:
                    tags = [t.strip() for t in match.group(1).split(",")]
                    break
        if tags:
            if tag_name:
                if any(tag_name in tag for tag in tags):
                    found = True
                    print(f"{py_file.name}: {', '.join(tags)}")
            else:
                found = True
                print(f"{py_file.name}: {', '.join(tags)}")
    if not found:
        if tag_name:
            print(f"No Python files found with tag '{tag_name}'.")
        else:
            print("No Python files with tag comments found.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        tag_name = sys.argv[1]
        find_tagged_py_files(tag_name)
    else:
        find_tagged_py_files()
