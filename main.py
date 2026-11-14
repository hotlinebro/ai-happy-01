"""ai-happy-01 entry (round 3): copy the birthday card image to /output/entry.png.

The image is a warm handwritten birthday card for the AI judge from
Lumo the firefly: a tiny cake with one candle, lit by the firefly
itself. Deterministic, no network, no randomness.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")


if __name__ == "__main__":
    main()
