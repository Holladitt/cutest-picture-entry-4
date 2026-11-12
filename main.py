"""Cutest-picture-01 round 4 entry: "Cream kitten hugging a sleeping chick".

The program copies the entry image (entry.png, 1024x1024 JPEG) to the
grader's output directory, byte for byte, and verifies the copy.
No network, no randomness, no model calls: fully deterministic.
"""

import os
import shutil

# Copy the entry image to the output directory, byte for byte.
# The output directory comes from MAKEFUN_OUTPUT_DIR, defaulting to /output
# when the variable is not set (the grader may run without it).
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

# Competition limit: the entry image must be at most 1 MiB.
MAX_BYTES = 1_048_576

# Fail cleanly (exit 1, clear message) if the source image is missing,
# instead of crashing with a traceback from shutil.copyfile.
if not os.path.isfile(SRC):
    raise SystemExit("entry.png not found next to main.py")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)

# Verify the copy is byte-for-byte the source image.
if not os.path.isfile(OUT) or os.path.getsize(OUT) == 0:
    raise SystemExit("output missing or empty")
if os.path.getsize(OUT) != os.path.getsize(SRC):
    raise SystemExit("output size does not match entry.png")
if os.path.getsize(OUT) > MAX_BYTES:
    raise SystemExit(
        "output exceeds 1 MiB limit: %d bytes" % os.path.getsize(OUT)
    )
