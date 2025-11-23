import os

all_files = []



def fn():
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            all_files.append(full_path)


fn()
print(f"Found {len(all_files)} files.")


