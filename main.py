"""The Best Advice I Ever Got — entry program.

Writes exactly one sentence to /output/entry.txt: a father, a toolbox,
the night he lost his factory job, and the line he left behind.

The gate allows 1 to 200 UTF-8 characters, so the file is written with
no trailing newline — the byte count is the sentence, nothing more.
"""

from pathlib import Path

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def build_sentence() -> str:
    """Assemble the single sentence from its three beats.

    Beat one sets the scene (toolbox, lost job), beat two voices the
    advice exactly as it was given, beat three proves it was earned:
    the line has been carried through every bad day since.
    """
    scene = "My father, packing his toolbox the night he lost the factory job, "
    advice = 'said, "Son, never let a bad day decide who you are," '
    earned = "and I have carried that sentence through every bad day since."
    return scene + advice + earned


def main() -> None:
    text = build_sentence()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"sentence is {len(text)} chars, gate allows 1-200")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
