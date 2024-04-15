# Creating directories
import os

# Directory
directory = "test_dir"
# Parent directory
parent_directory = "C:/Users/joshi/github/python_learning"
# Path
path = os.path.join(parent_directory, directory)  # use os.path.join instead of string concatenation as its OS
                                                  # independant and easier to read and deals with a potential trailing '/' for you
# Create dir
os.mkdir(path)
print(f"Created directory in {path}")
