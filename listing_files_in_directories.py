#!/usr/bin/env python
import os
from glob import glob

files = os.listdir("DATA")

print(files, '\n')

files = glob('DATA/*.txt')
print(files, '\n')

files = glob('DATA/[at]*.txt')
print(files, '\n')

files = glob('DATA/*ar*.txt')
print(files, '\n')

old_dir = os.getcwd()
print(old_dir)
os.chdir('/tmp')
print(os.getcwd())
os.chdir(old_dir)
print(os.getcwd())
print()
os.chdir('..')
print(os.getcwd())
os.chdir(old_dir)
print(os.getcwd())


