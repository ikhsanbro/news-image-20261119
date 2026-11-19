#!/usr/bin/env python3
"""Entry program for the news-image-20261119 bounty.

Copies the entry image (entry.png, beside this file) to the output
directory the grader reads: MAKEFUN_OUTPUT_DIR when set, else /output.

Python 3.13, standard library only, no network. Deterministic: it copies
the same bytes every run, so two runs write identical output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
DEST = DEST_DIR / "entry.png"


def main():
    if not SOURCE.is_file():
        raise SystemExit(f"missing entry image: {SOURCE}")
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    if DEST.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit(f"copy mismatch: {DEST}")
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
