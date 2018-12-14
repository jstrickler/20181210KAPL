#!/usr/bin/env python
import os
from datetime import datetime
import re

#   os.walk
#  [(curr, dirs, files), (curr, dirs, files), (curr, dirs, files), ...]
starting_point = os.path.abspath(".")

for curr_dir, dirs, files in sorted(os.walk(starting_point)):
    if "git" in curr_dir:
        continue
    print(curr_dir)
    for file_name in files:
        if re.search(r"\b.py$", file_name):
            file_path = os.path.join(curr_dir, file_name)
            raw_mtime = os.path.getmtime(file_path)
            mtime = datetime.fromtimestamp(raw_mtime).date()
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:4d} {mtime} {file_name}")

