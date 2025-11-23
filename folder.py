import os

# Start from your home directory
root_dir = "/home"

all_folders = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    # Append the current directory
    all_folders.append(dirpath)
    print(dirpath)  # print the folder as it's found

# Save the list to a file
output_file = "folders_in_crostini.txt"
with open(output_file, "w") as f:
    for folder in all_folders:
        f.write(folder + "\n")

print(f"Found {len(all_folders)} folders. Saved to {output_file}.")

