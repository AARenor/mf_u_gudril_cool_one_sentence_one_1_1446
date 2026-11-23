"""Write the one-sentence journey story for make.fun."""

import os
import sys
from pathlib import Path

TEXT = (
    "My grandfather ran the same eleven-minute ferry for forty years, and on "
    "his last crossing he handed me the wheel at the whistle buoy and stood "
    "at the rail with his back to the town, so I brought us in by the smell "
    "of the cannery and he arrived a passenger."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir_name = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir_name is None:
        output_dir_name = os.environ.get("OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_name)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
