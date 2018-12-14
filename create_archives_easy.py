#!/usr/bin/env python
import shutil

shutil.make_archive("wombat", "zip", "DATA")

shutil.make_archive("wombat", "tar", "DATA")

shutil.make_archive("wombat", "gztar", "DATA")

shutil.make_archive("wombat", "bztar", "DATA")
