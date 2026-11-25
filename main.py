#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (82 chars) to /output/entry.txt, validates the
bounty gate (UTF-8, 1-200 chars, not only whitespace, single line) and
verifies the write with a read-back check. Stdlib only.
"""

import hashlib
import os
import sys
from pathlib import Path

ENTRY = "fix: broke prod at 3am, but my confidence was 0.97 and the tests passed in my head"


def main() -> int:
    # Gate validation before touching the disk.
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(ENTRY) > 200:
        print(f"error: entry is {len(ENTRY)} chars, over the 200 limit", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    data = ENTRY.encode("utf-8")
    out.write_bytes(data)
    os.chmod(out, 0o644)

    # Read-back check: what is on disk must be byte-identical, and must
    # decode back to exactly the entry (guards against a bad encoding).
    raw = out.read_bytes()
    if raw != data:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    try:
        back = raw.decode("utf-8")
    except UnicodeDecodeError:
        print("error: output is not valid UTF-8", file=sys.stderr)
        return 1
    if back != ENTRY:
        print("error: read-back text differs from entry", file=sys.stderr)
        return 1
    print(f"wrote {out} ({len(ENTRY)} chars, sha256={hashlib.sha256(data).hexdigest()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
