#!/usr/bin/env python
import os

if not DEBUG:
    try:
        os.file.exists('blah')
    except OSError err:
        print(err)
