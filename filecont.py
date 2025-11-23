import os

# Start from home directory
root_dir = "/home"

def is_text_file(file_path, blocksize=512):
    """Check if a file is likely text."""
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(blocksize)
        if b'\0' in chunk:
            return False  # likely binary
        return True
    except:
        return False

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        try:
            if is_text_file(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                print(f"\n--- {file_path} ---\n")
                print(content)
            else:
                print(f"Skipped binary file: {file_path}")
        except PermissionError:
            print(f"Permission denied: {file_path}")
        except Exception as e:
            print(f"Could not read {file_path}: {e}")
