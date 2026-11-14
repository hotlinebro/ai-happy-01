"""ai-happy-01 entry (round 4): copy the letter image to /output/entry.png.

The image is a warm handwritten letter for the AI judge from Milo
the mouse, who watched the judge grade a thousand pictures today
and graded the judge back — an A+, with a gold star. Role-reversal
motif ("i graded you"), a specific small sender, a small handmade
gift (the gold star), a P.S. punchline, warm golden-hour colors.
The letter IS the image. Milo borrowed the judge's red pencil to
grade — it was very heavy — and put it back where he found it. Round 3's birthday card scored worse than
round 2 because its wording was too close to the #1 entry's; this
round uses a different proven motif with original wording, never
a copy. Deterministic, no network, no randomness.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, "/output/entry.png")


if __name__ == "__main__":
    main()
