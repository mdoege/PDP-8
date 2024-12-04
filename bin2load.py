#!/usr/bin/python

# Convert a ".bin" file to the ".load" decimal ASCII format (memory address plus memory contents)
# used by this emulator

# (This program was used to create focal-8.load and chekmo.load in the repo.)

# You will also need to modify pdp8.py (starting in line 768) if you would like to
# load other programs this way, because right now that code only looks for CHEKMO and FOCAL.

f = open("FOCAL-8.bn", "rb")
g = f.read()
n = 0
origin = 0

out = open("focal-8.load", "w")

while True:
    hi = int(g[n])
    n += 1
    if hi != 0o200:
        break

while True:
    lo = int(g[n])
    wd = (hi << 6) | lo
    n += 1
    hi = int(g[n])
    n += 1
    if hi == 0o200:
        break
    if wd > 0o7777:
        origin = wd & 0o7777
    else:
        print("%4s: %s" % (oct(origin), oct(wd)))
        out.write("%u %u\n" % (origin, wd))
        origin = (origin + 1) & 0o7777
    
