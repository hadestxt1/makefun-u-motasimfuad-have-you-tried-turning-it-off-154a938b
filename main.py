#!/usr/bin/env python3
"""Have You Tried Turning It Off? -- make.fun entry (program/v1).

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt), as the competition gate requires: UTF-8 text of
1 to 199 characters, not only white space.

Model-free and fully deterministic: the line is a fixed string, no
clock, no randomness, no network, no input files. Two runs produce
byte-identical output.
"""

import os
import sys

# The line. The classic off-and-on ritual, named the way a real agent
# would say it -- then the agent quietly gives up alongside the
# customer instead of fixing anything. Cheerful uselessness, and the
# customer is never the butt of it.
LINE = (
    "Okay, unplug it, count to ten, plug it back in, and if it still "
    "won't work, we'll both just sit here quietly and pretend this "
    "call never happened."
)


def main() -> int:
    if not 1 <= len(LINE) <= 199:
        print("line outside 1-199 characters", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is blank", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and re-check, so a bad write fails loudly here
    # instead of silently failing the scorer's gate.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE or not 1 <= len(written) <= 199:
        print("output verification failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
