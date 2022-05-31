#!/usr/bin/python3
for ch in range(0, -26, -1):
    print(f"{chr(122 + ch) if (-ch % 2) == 0 else chr(ch - 32 + 122)}", end="")
