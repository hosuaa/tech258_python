# Creating files
import os

# Directory
directory = "test_dir"
# Parent directory
parent_directory = "C:/Users/joshi/github/python_learning"
# Path
path = os.path.join(parent_directory, directory)
# File name
file_name = "testfile.txt"
#File path
file_path = os.path.join(path, file_name)
# Create file
with open(file_path, "w") as file1:
    toFile = "Contents go here"
    file1.write(toFile)

print(f"Created file in {file_path}")