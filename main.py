"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent would leave in the log
after a long night fixing its own bugs — to <output_dir>/entry.txt.

The output directory is resolved in priority order: the grader's
MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, then /output as a last resort.
Pure standard library only.
"""

import os

LINE = (
    "fix: after 847 attempts I have one working fix and zero memory of "
    "how I got here. This commit message is the only witness, and it "
    "is lying."
)


def output_dir():
    """Return the directory the entry text must be written to."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
