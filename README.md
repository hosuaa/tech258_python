# Tech 258 Python
## What is Python?

Change for demo

Python is a programming language that was released in 1991. It is a high level programming language which means it reads to be more human-like as opposed to lower level languages like C or Assembly. As a result it is one of the most popular programming languages and is widely used as an introduction to coding. It is an interpreted language rather than a compiled language so Python files are executed line by line. This makes them ideal for writing scripts and debugging.

## History of Python

Python was created by Guido van Rossum, a Dutch programmer, who released Python 0.9.0 in Feburary 1991. The name comes from the popular show Monty Python. Before Python, the most popular programming languages were C, Pascal, C++, Lisp and Fortran. These languages, while efficient, were difficult to learn and so Python was developed to fill this niche. Python only joined the top 10 most used programming languages after the year 2000. Since then, 2 versions have been released: Python 2, released on October 2000 and Python 3, released on December 2008.

## Why is Python popular?

Python is known to be easier to understand than many other programming languages. As a result, it is often used to teach people how to code, and so it has a very large user base.

There is also extensive documentation on how to use Python. 

From a DevOps perspective, Python is incredibly popular since it is shipped with support for many of the most used DevOps tools such as Terraform. Python also has many user created libraries that developers can use which saves a lot of time writing and debugging code. 

## What is a virtual environment?

A virtual environment, or venv, is a directory used to create an isolated Python environment from the one on our system. We link our project to the venv rather than our system's Python. This means any libraries or dependencies installed do not affect our base Python but rather the Python in the venv. This is a very good practise to uphold and avoids many potential conflicts than can arise in development, especially if we are developing multiple projects on our system. 

## What is pip?

Pip is a package management system which allows us to install and manage packages from the Python package index which contains many libraries we may wish to use. 

It is a command-line tool that allows us to install, uninstall, and manage Python packages easily. The name pip stands for "Pip Installs Packages" or "Preferred Installer Program."

Pip is incredibly useful and as such is included by default after Python 3.4

## What is scripting? 

Scripting is writing code that is used to automate (repetitive) processes. Scripts typically perform a single task. This is similar to programming however there are some differences. Programs typically have a larger scope and can perform more operations, whereas scripts are focused on performing a single task.

## What are the base Python libraries?

The base Python libraries are all the libraries contained in the Python Standard Library. These libraries come shipped with Python and do not have to be installed by e.g. pip. These are libraries that are used so often that the Python team decided to include them by default. Some examples include:

- **os**: Provides operating system interfaces for file operations, directory manipulation, and process management.
- **sys**: Contains system-specific parameters and functions, such as access to command-line arguments, Python interpreter settings, and standard I/O streams.
- **math**: Offers mathematical functions and constants for numerical calculations, including trigonometric functions, logarithms, and constants like π and e.
- **random**: Provides functions for generating random numbers and performing random selections, shuffling, and sampling.

This is just a small selection and there are many more available.

## What are some of the most popular external libraries

- **Numpy**: Many useful mathematical operations are not available in base Python. This is especially true when working on scientific computing. Numpy is heavily used in this domain as well as in Data Science and Machine Learning. Numpy provides matrices and operations on these.
- **Matplotlib**: This provides many different ways to plot data, such as through graphs or other visualisations. It is easy to use to which is why it is so popular.
- **Tensorflow/Pytorch**: These are popular machine learning frameworks that are functionally quite similar. You can create models for essentially any task you can provide the data for.
