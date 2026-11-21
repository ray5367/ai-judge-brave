"""Write one short text to the grader's output directory.

The text is fixed: every run writes exactly the same bytes.
The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os

TEXT = """The keeper climbs to the lamp the way he always has, one step, then the next. Below, the sea is doing what the sea does. He trims the wick, opens the shutter, and the light goes out steady, finding the boats coming home. The dark is large. The light is his, and it is enough."""

# The competition caps the text at 280 characters; fail loudly instead of
# silently submitting a truncated or over-long entry.
MAX_CHARS = 280


def main():
    if len(TEXT) > MAX_CHARS:
        raise ValueError(f"text is {len(TEXT)} chars, over the {MAX_CHARS} cap")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Plain direct write: the grader reads entry.txt as another user, so the
    # file must be world-readable whatever the runtime umask is (0600 from a
    # temp file, or 0660 under a strict umask, both broke the graded run).
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
