#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo Z883  consequat. Duis aute irure dolor in reprehenderit in  
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

pattern = r'([A-Z])(\d{2,3})'  # <1>

print("Groups")
print("0   1   2")
for m in re.finditer(pattern, s):
    print(m.group(0), m.group(1), m.group(2))  # <2>
print()

matches = re.findall(pattern, s)  # <3>
print("matches:", matches)
