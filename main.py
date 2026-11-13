"""ai-happy-01 entry: copy the card image to /output/entry.png.

The image is a warm greeting card for the AI judge: an orange tabby cat
asleep on a stack of notes, telling the judge it can rest now.
Deterministic, no network, no randomness.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")


if __name__ == "__main__":
    main()
