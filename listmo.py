import os

all_files = []



for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        full_path = os.path.join(dirpath, file)
        all_files.append(full_path)

print(f"Found {len(all_files)} files.")
