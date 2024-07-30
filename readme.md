# How It Works
1. The script prompts the user to enter the base name for the new files once.
2. The generate_new_name function generates a new file name by adding a number in parentheses to ensure uniqueness.
3. The rename_and_move_file function renames and moves each file to the output directory.
4. The main function processes each file path passed as an argument, creates the output directory if it doesn't exist, generates unique 5. new names, and then renames and moves the files using rename_and_move_file.

## Steps to use the script
1. Download the latest version of Python from Microsoft Store or from the official  [Python](https://www.python.org/downloads/) website if you are on any other OS
2. Drag and drop files onto rename.bat
3. The script will prompt you to enter the new base name for the files.
4. The script will automatically rename each file, appending a number to ensure uniqueness, and move the renamed files to an "output" folder located in the same directory as the script.
