"""

"""

import sys
from pathlib import Path

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
    else:
        path = Path(args[1])
        if path.is_dir():
            print("Usage: python main.py <file_path>, path is not a directory")
            sys.exit(1)
        else:
            if not path.exists():
                print("File does not exist")
            else:
                print("File exists")
