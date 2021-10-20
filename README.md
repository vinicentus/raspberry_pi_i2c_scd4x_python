# raspberry-pi-i2c-scd4x-python
Python bindings for raspberry-pi-i2c-scd4x

The original driver, written in C/C++, is included as a submodule. This repository contains python bindings for it.

Note that in order to make this simpler to use in Python, some methods may take different parameters or return different types of values that in the original driver.

For documentation on functions, see "scd4x_i2c.c" from the submodule.

# Setup:
clone this repo, make sure to fetch the submodule as well

cd into directory,

Recommended: create a python venv, and activate it,

install the "cffi" libary using pip,

run "build.py"

# Example usage:
 See "example.py"
