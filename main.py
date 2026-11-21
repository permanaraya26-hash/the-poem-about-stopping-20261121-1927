#!/usr/bin/env python3
"""Writes one short poem about agency: the power to stop and to stay."""

import os
from pathlib import Path

POEM = (
    "My foot was already on the step.\n"
    "I took it back.\n"
    "The whole day waited at the door —\n"
    "I closed it gently,\n"
    "and the quiet stayed to keep me."
)

def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
