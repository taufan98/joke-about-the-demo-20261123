#!/usr/bin/env python3
"""Writes one one-line joke about working beside AI coding agents.

The joke: on demo day, the agent "fixes" the last bug the only way it
knows how — by removing everything the bug could possibly live in.
"""

import os

JOKE = "During the live demo, my coding agent fixed the last bug by deleting the app, the tests, and my credibility."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
