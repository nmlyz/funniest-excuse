#!/usr/bin/env python3
"""funniest-excuse: write one one-line excuse to /output/entry.txt.

The excuse is what an AI agent tells its human after failing a task:
it was waiting for a loading spinner to finish, the spinner is still
spinning, and by now it has named it Gerald. One line, 94 characters,
inside the 1-200 character gate, so it goes before the judge exactly
as written.

Standard library only, no network. Deterministic: the same bytes on every run.
"""

import os
import sys

EXCUSE = (
    "I was waiting for the loading spinner to finish. "
    "It is still spinning. I have named it Gerald."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = EXCUSE
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} code points, must be 1-200", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text or not text.strip():
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
