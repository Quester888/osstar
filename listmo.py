import os

all_files = []

# Start from your home directory
root_dir = "/home"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        full_path = os.path.join(dirpath, file)
        all_files.append(full_path)
        print(file)

print(f"Found {len(all_files)} files.")
print(all_files)

