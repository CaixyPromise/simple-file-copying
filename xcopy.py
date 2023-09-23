# xcopy.py

import sys
import os
from fileutil import copy


def show_progress(copied, total):
    progress = (copied / total) * 100
    print(f"\rCopied {progress:.2f}%", end = '')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: xcopy.py <sourcefile> <destinationfile>")
        sys.exit(1)

    sourcefile = sys.argv[1]
    destfile = sys.argv[2]

    if not os.path.exists(sourcefile):
        print(f"Error: Source file '{sourcefile}' does not exist.")
        sys.exit(1)

    copy(sourcefile, destfile, tellprogress = show_progress)
    print("\nCopy completed!")
