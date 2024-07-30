import sys
import os
import shutil

def generate_new_name(dir_name, base_name, ext, count):
    new_name = f"{base_name} ({count}){ext}"
    new_path = os.path.join(dir_name, new_name)
    
    while os.path.exists(new_path):
        count += 1
        new_name = f"{base_name} ({count}){ext}"
        new_path = os.path.join(dir_name, new_name)
    
    return new_name

def rename_and_move_file(old_path, new_name, output_dir):
    new_path = os.path.join(output_dir, new_name)
    
    try:
        shutil.move(old_path, new_path)
        print(f"Moved and renamed: {old_path} -> {new_path}")
        return True
    except OSError as e:
        print(f"Error moving and renaming file {old_path}: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: Drag and drop files onto this script.")
        return

    # Determine the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "output")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the base name for the new files from the user
    base_name = input("Enter the new base name for the files: ")
    
    count = 1
    for file_path in sys.argv[1:]:
        if not os.path.isfile(file_path):
            print(f"Error: {file_path} is not a valid file.")
            continue
        
        ext = os.path.splitext(file_path)[1]
        
        new_file_name = generate_new_name(output_dir, base_name, ext, count)
        rename_and_move_file(file_path, new_file_name, output_dir)
        count += 1

if __name__ == "__main__":
    main()
