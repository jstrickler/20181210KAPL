#!/usr/bin/env python
import os

# os.system('netstat -an')

with os.popen('netstat -an') as netstat_in:
    for raw_line in netstat_in:
        if "ESTABLISHED" in raw_line:
            line = raw_line.rstrip()
            print(line)
