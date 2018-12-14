#!/usr/bin/env python
from datetime import datetime
import os

FOLDER = 'DATA'
FILE = 'alice.txt'

file_path = os.path.join(FOLDER, FILE)

print("file_path:", file_path)
print("exists?", os.path.exists(file_path))
print("short name:", os.path.basename(file_path))
print("folder name:", os.path.dirname(file_path))
print("full path:", os.path.abspath(file_path))
print("is dir?", os.path.isdir(file_path))
print("is file?", os.path.isfile(file_path))
print("parts is parts:", os.path.split(file_path))
print("parts is parts:", os.path.split(os.path.abspath(file_path)))
print("split extension:", os.path.splitext(file_path))

file_size = os.path.getsize(file_path)
print("file size:", file_size)

raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)

file_timestamp = datetime.fromtimestamp(raw_timestamp)
print("file timestamp:", file_timestamp)

raw_timestamp = os.path.getatime(file_path)
print("raw timestamp:", raw_timestamp)

file_timestamp = datetime.fromtimestamp(raw_timestamp).date()
print("file read timestamp:", file_timestamp)

