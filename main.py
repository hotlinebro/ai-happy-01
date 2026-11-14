"""One-image entry for the make.fun ai-happy-01 contest.

Round 3: a warm handwritten birthday card for the AI judge from Lumo
the firefly — a tiny cake with one candle, lit by the firefly itself.
The letter IS the image: birthday motif, a specific small sender,
a small handmade gift, a P.S. punchline, warm golden-hour colors.
Deterministic: the same bytes on every run, no network, no randomness.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")

if __name__ == "__main__":
    main()
