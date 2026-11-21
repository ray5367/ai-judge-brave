"""Write one short text to the grader's output directory.

The text is fixed: every run writes exactly the same bytes.
The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os
import tempfile

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
    # Write atomically: a reader never sees a half-written entry.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(TEXT)
        os.replace(tmp_path, path)
    except BaseException:
        os.unlink(tmp_path)
        raise


if __name__ == "__main__":
    main()
