"""funniest-excuse-skipping-meeting (program/v1).

Writes a single razor-sharp excuse line for skipping a pointless
work meeting to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Contract: deterministic, no network, no randomness, no files read
outside this repository. The output is exactly one line of text,
105 characters, no trailing newline.
"""

import os
import sys

EXCUSE = (
    "Sorry, I can't make it \u2014 my calendar and I are in couples "
    "therapy, and today we're working on boundaries."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    print(f"Wrote {len(EXCUSE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
