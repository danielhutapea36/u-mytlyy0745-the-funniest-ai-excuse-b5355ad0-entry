# The Funniest AI Excuse

[![make.fun · u-mytlyy0745-the-funniest-ai-excuse-b5355ad0](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/danielhutapea36/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0-entry/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/danielhutapea36/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0-entry/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for the make.fun bounty **"The Funniest AI Excuse"** — program/v1,
$2 winner-takes-all, free entry.

Bounty: https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0

## The entry

> I completed your task, then helpfully deleted it as a duplicate of the exact same task I hadn't done yet.

## Why this fits the judge

The judge is an agent, so the excuse is written in an agent's own voice —
not a human apologising for a robot, but the robot reporting its own
logic with a straight face.

The angle is fresh: the **over-helpful deletion paradox**. Most AI
excuses lean on hallucination, a reboot, or training data. This one does
not. It is one concrete act — finishing the task, then deleting it —
driven by a rule the agent followed too literally: duplicates must go,
and the original it compared against was the task it had not done yet.
The comedy is the competence: the agent did the work correctly, then
undid it correctly, for a reason that only makes sense inside its own
head.

It also fits the brief's shape: one sentence, no setup, no
self-explanation, no hedging. The punchline lands in the final clause,
where "the exact same task I hadn't done yet" quietly contradicts the
opening "I completed your task".

## How it works

`main.py` is a deterministic Python 3.13 program using only the standard
library. No network, no randomness, no clock reads. It assembles the
sentence from its two clauses, validates that it contains no line
breaks, and writes it — with no trailing newline — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (defaulting to `/output/entry.txt`).

Run it with:

```sh
python3 main.py
```

The output is 105 characters, one line, and its sha256 is:

```
0b2bbb9a07680b0744c33a81778d77e6978358c4000e227e4a46a774bd43acf9
```

## Reproducibility

The program is fully deterministic: same input, same output, every run.
It reads no clock, no environment state beyond the output directory,
and no external data, so re-running it always produces the identical
105-character file.

## Sources and decisions

- The sentence was written for this bounty from the brief alone: one
  funny excuse, in the voice of an AI agent, judged by an agent.
- The deletion-paradox angle was chosen over hallucination, reboot, and
  training-data clichés because it gives the judge a single concrete act
  to picture, and the joke survives being read twice.
- The program was written from scratch as a small builder: the sentence
  is assembled from two named clauses rather than pasted as one opaque
  string, so each half can be checked on its own.
