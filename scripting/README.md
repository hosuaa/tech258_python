# Scripting

## What is scripting?

**Scripting** is writing code that is used to automate repetitive processes. It typically extends on or modifies existing programs.
The code is small scale and is usually interpreted rather than complied. This makes Python an ideal programming language for
scripting.

**Programming**, on the other hand, is a broader term that involves creating new programs or software. Programming encompasses
a lot of the steps in software development, including designing, writing, testing and compiling code. The code written is usually
more complex than in scripting

A simple example would be the task of editing images. We can use a program, like Photoshop, to edit a single image easily.
However, if we wanted to edit many images, it would take a while to manually edit each image one by one in photoshop. This
is where we can use a script which interacts with Photoshop to automatically edit all the images with the desired outcome. 
The script is a few lines of code that is written to work with, or extend, Photoshop which itself is a large scale program consisting
of many lines of code.

## Standard Python Library

The packages in the Standard Python Library are packages that are so useful to developers that they come shipped with Python
by default when you install it. They were once external libraries that you had to download but since they were used so much they
became installed by default.

Some examples of standard libraries include:
- **os**: Provides operating system information including your current working directory, environment variables, number of cores as well
as other os functionality such as the ability to create directories.
```
working_dir = os.getcwd()
print(f"Current working directory: {working_dir}")

user = os.environ.get("USERNAME") or os.environ.get("USER")
print(f"Username: {user}")

cpu_cores = os.cpu_count()
print(f"Num of cores: {cpu_cores}")

os.mkdir("test_dir")
os.rmdir("test_dir")
```
will output: 
```commandline
Current working directory: C:\Users\joshi\github\python_learning\scripting
Username: joshi
Num of cores: 6
```
- **sys**: Contains system-specific parameters and functions, such as access to command-line arguments, Python interpreter settings, and standard I/O streams.
- **math**: Offers mathematical functions and constants for numerical calculations, including trigonometric functions, logarithms, and constants like π and e.
- **random**: Provides functions for generating random numbers and performing random selections, shuffling, and sampling.
