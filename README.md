# raspberry_pi_i2c_scd4x_python
Python bindings for **raspberry-pi-i2c-scd4x**

The original driver, written in C/C++, is included as a submodule. This repository contains python bindings for it.

Note that in order to make this simpler to use in Python, some methods may take different parameters or return different types of values that in the original driver.

For documentation on functions, see [scd4x_i2c.c](./raspberry-pi-i2c-scd4x/scd4x_i2c.c) from the submodule.

# Setup:
clone this repo, make sure to fetch the submodule as well  
`git clone --recurse-submodules https://github.com/vinicentus/raspberry_pi_i2c_scd4x_python.git`

cd into directory  
`cd raspberry_pi_i2c_scd4x_python`

Recommended: create a python venv, and activate it  
`python3 -m venv venv`
`source venv/bin/activate`

install the "cffi" libary using pip  
`python3 -m pip install cffi`

run [build.py](./build.py) (from inside the directory)  
`python3 build.py`

# Example usage:
See [example.py](./example.py)

**Note that this must be run as a module, from outside the package directory:**  
`cd ..`  
`python3 -m raspberry_pi_i2c_scd4x_python.example`
