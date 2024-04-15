import sys

print(f"This is the name of the program: {sys.argv[0]}")
print(f"Number of elements including the name of the program: {len(sys.argv)}")
print(f"Number of elements excluding the name of the program: {(len(sys.argv) - 1)}")
print(f"Argument List: {str(sys.argv)}")

# run this in terminal