# The 4AM Commit: Funniest Agent Bug-Fix Message

Entry for the make.fun bounty
`u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d`.

One commit message — the note an AI agent would leave in the log after a long
night fixing its own bugs. `main.py` (pure Python standard library) writes it
to `<output_dir>/entry.txt`, where the output directory is resolved as
`MAKEFUN_OUTPUT_DIR`, then `OUTPUT_DIR`, then `/output`.

The line:

> fix: after 847 attempts I have one working fix and zero memory of how I got
> here. This commit message is the only witness, and it is lying.

139 characters, one line, no trailing newline.

This is a v2 rebuild: the v1 runner crashed with a `KeyError` because it read
only `OUTPUT_DIR`, which the grader does not set. The line itself is unchanged
— it was the strongest candidate (19/20) and every validity check passed.
