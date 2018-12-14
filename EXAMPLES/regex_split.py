#!/usr/bin/env python

import re

rx_wordsep = re.compile(r"[^a-z]+", re.I)  # <1>

s1 = '''There are 10 kinds of people in a Binary world, I hear" -- Geek talk. I won't talk about Nerds. There are many kinds of Geek'''

words = set(rx_wordsep.split(s1.lower()))  # <2>
print(words)
