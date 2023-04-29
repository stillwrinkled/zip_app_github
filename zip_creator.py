import zipfile
import os
from pathlib import Path


def make_archive(filepaths, dest_dir):
    dest_path = Path(dest_dir, "compressed.zip")

    # Check if the file already exists and increment the number in the filename if necessary
    counter = 0
    while dest_path.exists():
        counter += 1
        dest_path = Path(dest_dir, f"compressed({counter}).zip")

    print(f"Creating {dest_path}")

    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            base_name = os.path.basename(filepath)
            archive.write(filepath, arcname=base_name)


if __name__ == "__main__":
    make_archive(filepaths=["/Users/amitabhishek/Desktop/workingDir/Python/compress/test1.txt",
                            "/Users/amitabhishek/Desktop/workingDir/Python/compress/test2.txt"],
                 dest_dir="/Users/amitabhishek/Desktop/workingDir/Python/destination")
