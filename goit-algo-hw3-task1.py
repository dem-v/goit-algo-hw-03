import argparse
import os
import shutil


def parse_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", "-source", type=str, help="input file")
    parser.add_argument("--d", "-dest", type=str, help="output file", default="dist")
    args = parser.parse_args()
    return args


def parse_source_path(path: str, base: str) -> list[str]:
    res_list = list()
    if base != "":
        p = os.path.join(base, path)
    else:
        p = path

    if not os.path.exists(p):
        raise FileNotFoundError

    for i in os.listdir(p):
        curr_p = os.path.join(p, i)
        try:
            if os.path.isdir(curr_p):
                res_list.append(*parse_source_path(i, p))
            elif os.path.isfile(curr_p):
                res_list.append(curr_p)
        except Exception as e:
            print("Error: %s", e)
    return res_list


def copy_files_to_dest_folder(files: list[str], dest_folder: str) -> None:
    rel_files = [os.path.relpath(os.path.dirname(f), os.path.commonpath(files)) for f in files]

    for i in range(len(rel_files)):
        try:
            destination_path = os.path.join(dest_folder, rel_files[i])
            os.makedirs(destination_path, exist_ok=True)
            shutil.copy(files[i], os.path.join(destination_path, os.path.basename(files[i])))
        except FileExistsError as e:
            print("Error:", e)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    args = parse_argv()
    input_path = args.s
    output_path = args.d
    copy_files_to_dest_folder(parse_source_path(input_path, ""), output_path)
