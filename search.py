#!/usr/bin/env python3
"""
search.py

Search for Python files in the 'algo' subdirectory whose filenames contain the given tag.
"""

import sys
from pathlib import Path


def find_tagged_py_files(tag_name: str) -> list[Path]:
    # Resolve this script’s directory and locate the 'algo' folder
    base_dir = Path(__file__).resolve().parent
    algo_dir = base_dir / "algorithm"
    # Match any .py file whose name includes the tag_name
    return list(algo_dir.glob(f"*{tag_name}*.py"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <tag_name>")
        sys.exit(1)

    tag_name = sys.argv[1]
    matching_files = find_tagged_py_files(tag_name)

    if not matching_files:
        print(f"No Python files found with tag '{tag_name}'.")
    else:
        print(f"Found {len(matching_files)} file(s) with tag '{tag_name}':")
        for file_path in matching_files:
            print(f"  - {file_path}")
