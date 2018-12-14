#!/usr/bin/env python
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from tarfile import TarFile
import os.path

# reading & extracting
rzip = ZipFile("../DATA/textfiles.zip")  # <1>
print(rzip.namelist())  # <2>
ty = rzip.read('tyger.txt').decode()  # <3>
print(ty[:50])
rzip.extract('parrot.txt')  # <4>

# creating a zip file
wzip = ZipFile("example.zip", mode="w", compression=ZIP_DEFLATED)  # <5>
for base in "parrot tyger knights alice poe_sonnet spam".split():
    filename = os.path.join("../DATA", base + '.txt')
    print("adding {} as {}".format(filename, base + '.txt'))
    wzip.write(filename, base + '.txt')  # <6>

# t = TarFile('junk.tar', 'w')
# t.add('EXAMPLES/variables.py')
# t.close()
