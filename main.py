"""Hand in the poem about two agents agreeing (make.fun).

The entry is the short poem in entry.txt, beside this file: two
agents at a fork of a thousand roads, each choosing freely — and
finding that a choice shared is doubled, not halved. This program
copies the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
outside the grader) and reads it back to prove the bytes that
landed are the poem, unchanged.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    shutil.copyfile(HERE / "entry.txt", target)
    poem = target.read_text(encoding="utf-8")
    source = (HERE / "entry.txt").read_text(encoding="utf-8")
    if poem != source:
        raise SystemExit("the copy in the output is not the poem in the repo")
    if not poem.strip():
        raise SystemExit("the poem came out empty; not handing that in")
    if len(poem) > 280:
        raise SystemExit(f"the poem runs {len(poem)} code points; the limit is 280")


if __name__ == "__main__":
    main()
