"""Write one short text to the grader's output directory.

The text is fixed: every run writes exactly the same bytes.
The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os

TEXT = """The keeper climbs to the lamp the way he always has, one step, then the next. Below, the sea is doing what the sea does. He trims the wick, opens the shutter, and the light goes out steady, finding the boats coming home. The dark is large. The light is his, and it is enough."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
