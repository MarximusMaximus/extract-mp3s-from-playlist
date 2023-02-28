#!/usr/bin/env python
import os
import sys
import plistlib
import shutil
import urllib.parse

plistpath = sys.argv[1]
destpath = sys.argv[2]

f = open(plistpath, "rb")
bd = f.read()
f.close()

d = plistlib.loads(bd)

paths = [
    urllib.parse.unquote(t["Location"].replace("file://", ""))
    for t in d["Tracks"].values()
]

for p in paths:
    d = p.split("/")[-3:]
    #d.insert(0, destpath)
    #d_full = "/".join(d)
    d_full = f"{destpath}/{'_'.join(d)}"
    print(f"{p} -> {d_full}")
    # os.makedirs(d_full, exist_ok=True)
    shutil.copy(p, d_full)

