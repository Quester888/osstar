import os

# Start from your home directory
root_dir = "/home"

all_folders = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    # Append the current directory
    all_folders.append(dirpath)
    print(file)
    
    # Optionally, skip directories we can't access
    # for dirname in dirnames[:]:
    #     full_path = os.path.join(dirpath, dirname)
    #     if not os.access(full_path, os.R_OK):
    #         dirnames.remove(dirname)

# Save the list to a file
output_file = "folders_in_crostini.txt"
with open(output_file, "w") as f:
    for folder in all_folders:
        f.write(folder + "\n")

print(f"Found {len(all_folders)} folders. Saved to {output_file}.")
print(all_folderS)
