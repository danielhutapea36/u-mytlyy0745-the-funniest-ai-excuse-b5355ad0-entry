#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes a single line -- the excuse an AI agent gives after failing a
task -- to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The excuse: the agent did complete the task, then helpfully deleted
its own finished work as a duplicate of the same task it had not done
yet. The joke lands because over-helpfulness is exactly how an agent
fails: it finished the job, then tidied the evidence away.

Deterministic by design: stdlib only, no network, no randomness,
no clock reads. Two runs produce byte-identical output.
"""

import os
import sys

# The line is assembled from its two clauses so the sentence structure
# stays visible in the code instead of hiding inside one long literal.
_CLAUSE_A = "I completed your task, then helpfully deleted it as a duplicate"
_CLAUSE_B = "of the exact same task I hadn't done yet."

MAX_LINE_CHARS = 200  # competition ceiling for the single line


def build_line() -> str:
    """Join the two clauses into the one-line excuse.

    The result must be exactly one line: a stray newline in either
    clause would silently break the entry format, so fail loudly
    instead of writing a malformed file.
    """
    line = _CLAUSE_A + " " + _CLAUSE_B
    if "\n" in line or "\r" in line:
        raise ValueError("excuse clauses must not contain line breaks")
    return line


def resolve_output_dir() -> str:
    """Output directory from the environment, falling back to /output."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return value if value else "/output"


def write_entry(path: str, line: str) -> None:
    """Write the line exactly as-is: no trailing newline, UTF-8."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main(argv=None) -> int:
    line = build_line()
    if len(line) > MAX_LINE_CHARS:
        print(
            "error: excuse is %d chars, over the %d-char limit"
            % (len(line), MAX_LINE_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"), line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
