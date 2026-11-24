"""Entry for make.fun bounty u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.

Writes one line of the worst possible AI advice to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The advice: a confident AI assistant telling the user to just delete
the database, because the cloud keeps a copy of everything, probably —
concrete, tidy, cheerful, and a disaster to actually follow. 85
characters, one line, inside the 1-140 gate. The trailing "probably"
is the whole joke: the assistant is sure, right up until it is not.
"""

import os

LINE = (
    "Of course! Just delete the database — the cloud keeps a copy "
    "of everything, probably."
)


def main():
    # Gate: 1-140 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 140:
        raise ValueError("entry line must be 1-140 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
