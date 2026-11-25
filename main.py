#!/usr/bin/env python3
"""Write one original office-life joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""

import os
from pathlib import Path

JOKE = "They replaced the watercooler with Slack, so now office gossip has a search bar."


def main() -> None:
    # The gate requires one line of 1-200 characters, not only whitespace.
    assert "\n" not in JOKE and 1 <= len(JOKE) <= 200, "joke must be one line of 1-200 chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
