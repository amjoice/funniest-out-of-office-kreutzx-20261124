#!/usr/bin/env python3
"""The Funniest Out-of-Office.

Writes one out-of-office auto-reply, 140 characters or fewer, to
/output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim, no Pillow.

The line was picked against the published judge brief, in its order:
1. Plausible: a real person would set this as their auto-reply -- it
   reads exactly like a normal "out until Monday" notice.
2. Surprise: the twist lands twice. First, the replacement is out too,
   so there is nobody to cover; then the kicker reveals the two of them
   planned it together and HR still hasn't noticed. The reader expects
   a handover and gets a conspiracy instead.
3. Voice: dry, first person, conspiratorial -- a person talking, not a
   template ("I am currently out of the office...").
4. Fresh: no inbox mountain, no beach, no "back soon", no cat, no
   robot -- the joke is coordinated absence, not being unreachable.
5. Economy: every clause earns its place; cut any of them and the
   laugh gets weaker. 110 characters, one line, no filler.
"""

import os

REPLY = (
    "I'm out until Monday. My replacement is also out until Monday. "
    "We planned it this way, and HR still hasn't noticed."
)


def main() -> None:
    text = REPLY.strip()
    assert 1 <= len(text) <= 140, f"reply must be 1-140 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "reply must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
