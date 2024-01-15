import argparse
import os
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", "-source", type=str, help="input file")
    parser.add_argument("--d", "-dest", type=str, help="output file", default="dist")
    args = parser.parse_args()
    return args


def process_source_path(path: Path, base: Path | None, dest_folder: Path) -> None:

    if base is not None:
        p = base / path
    else:
        p = path
        base = p

    if not p.exists():
        raise FileNotFoundError(f"Path {p} does not exist.")

    for i in p.iterdir():
        try:
            if i.is_dir():
                process_source_path(i, base, dest_folder)
            elif i.is_file():
                copy_file_to_dest_folder(i, dest_folder)
        except Exception as e:
            print("Error: %s", e)


def copy_file_to_dest_folder(file: Path, dest_folder: Path) -> None:
    try:
        destination_path = dest_folder / file.suffix[1:]
        os.makedirs(destination_path, exist_ok=True)
        dest_file = destination_path / file.name
        if dest_file.exists():
            dest_file = destination_path / (os.path.splitext(file.name)[0] + "_dupl" + file.suffix)
        shutil.copy(file, dest_file)
    except FileExistsError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    args = parse_argv()
    input_path = Path(args.s)
    output_path = Path(args.d)
    process_source_path(input_path, None, output_path)
