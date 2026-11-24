#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

A small deterministic program that writes the entry line to
``<MAKEFUN_OUTPUT_DIR>/entry.txt``.

The excuse is a single sentence, delivered in the agent's own voice:
an over-helpful assistant that finished the job and then tidied it
away as a duplicate of the very same job it had not done yet.
"""

import os


def build_excuse() -> str:
    """Assemble the excuse sentence from its two clauses.

    The first clause states the completed work; the second clause
    supplies the punchline — the deletion, and the reason for it.
    Splitting the sentence this way keeps the wording explicit and
    makes each half easy to check on its own.
    """
    completed_work = "I completed your task"
    helpful_deletion = (
        ", then helpfully deleted it as a duplicate "
        "of the exact same task I hadn't done yet."
    )
    return completed_work + helpful_deletion


def resolve_output_path() -> str:
    """Return the path of the file the entry line is written to.

    The kit sets MAKEFUN_OUTPUT_DIR for the run; when it is absent
    we fall back to the conventional ``/output`` directory so the
    program still behaves the same way when run by hand.
    """
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, "entry.txt")


def main() -> None:
    """Write the excuse to the output file, with no trailing newline."""
    excuse = build_excuse()
    if "\n" in excuse or "\r" in excuse:
        raise ValueError("excuse must be a single line with no line breaks")
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(excuse)


if __name__ == "__main__":
    main()
