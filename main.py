"""
    This is the entry point of the program.
    It checks if theres any sign of hidden data in some
    type of files. If there is, it will clean the file.
"""

import sys
from pathlib import Path
from image_processing import clean_image, has_hidden_data

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
                if path.suffix in [".png", ".jpg", ".jpeg"]:
                    if has_hidden_data(path):
                        print("File contains hidden data")

                        output_path = path.with_name(path.stem + "_clean" + path.suffix)

                        clean_image(path, output_path)
                        print("Hidden data removed, saved to", output_path)
                    else:
                        print("No hidden data found")
