import os

all_files = []
root_dir = "/path/to/your/directory"  # Replace with your directory path

def fn():
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            all_files.append(full_path)

fn()
print(f"Found {len(all_files)} files.")


