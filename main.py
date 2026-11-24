"""One-Line Office Joke: 24-Hour Sprint — entry program.

Writes exactly one line — a single office joke, under 200 characters —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Design, mapped to the published judge brief (most important first):
  1. Genuine one-line office joke: a five-year plan, a boss, an inbox —
     unmistakably office life, not a slogan or observation.
  2. Real turn at the end: the five-year plan turns out to be 47 unread
     emails from 2021 the speaker still plans to answer — a payoff anyone
     with an inbox recognises.
  3. One line: a single sentence, setup and punchline on one line.
  4. Fresh: a concrete number and a year (47, 2021) — a specific detail,
     not a generic complaint and not the meeting-could-have-been-an-email
     joke everyone has already heard.
  5. Clear on first read: plain words, tight at 107 characters.

Deterministic: no randomness, no network, no input — the same bytes on
every run, so the two grading runs agree. Before writing, the program
checks its own output against the kit's gate (1–200 characters, one line,
not only whitespace, valid UTF-8) and refuses to write anything invalid.
"""

import os
import sys

JOKE = (
    "My boss asked for my five-year plan, so I showed him the 47 "
    "unread emails from 2021 I still plan to answer."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Fail loudly if the entry would ever fail the kit's gate."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    validate(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one line, no trailing newline: the gate counts characters,
    # and a single line with no newline is the cleanest possible output.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
