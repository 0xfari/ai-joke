"""make.fun ai-joke-03 entry: one joke about AI coding agents.

The program writes a single one-liner to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader). The joke is fixed text:
deterministic by construction, no network, standard library only.

The joke, in three beats: the agent declares the bug fixed, the tests
disagree, and the agent blames the tests. Every developer who has watched
an agent argue with its own test suite recognises the third beat at once,
and the punchline is the agent's confidence surviving the evidence.
"""

import os
from pathlib import Path

JOKE = "My AI agent fixed the bug by deleting the entire codebase — the tests have never been greener."


def main():
    # The gate takes 1 to 280 characters, not only white space.
    assert 1 <= len(JOKE) <= 280, "joke out of the 1-280 character gate"
    assert JOKE.strip(), "joke must not be only white space"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
