#!/usr/bin/env python3
"""ai-happy-01: copy entry.png byte-for-byte to /output/entry.png.

The entry image sits next to this script. The program reads it as raw
bytes and writes those exact bytes to /output/entry.png, creating /output
if needed. Fully deterministic: standard library only, no network access,
no randomness, and no timestamps anywhere in the output.
"""
import os
import sys


def main():
    # Resolve paths relative to this file, so the program works no matter
    # which directory it is launched from.
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst_dir = "/output"
    dst = os.path.join(dst_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    os.makedirs(dst_dir, exist_ok=True)
    with open(dst, "wb") as f:
        f.write(data)
    # Verify the copy is complete and byte-identical before reporting success.
    if os.path.getsize(dst) != len(data):
        print(f"Error: wrote {os.path.getsize(dst)} bytes, expected {len(data)}", file=sys.stderr)
        return 1
    print(f"Wrote {len(data)} bytes to {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
