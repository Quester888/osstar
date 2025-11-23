import os

all_files = []

# Start from your home directory
root_dir = "/home"

for dirpath, dirnames, filenames in os.walk(root_dir):
  
    for file in filenames:
      if ".json" in file: 
        full_path = os.path.join(dirpath, file)
        all_files.append(full_path)
      else:
        print("skipped")

print(f"Found {len(all_files)} files.")
