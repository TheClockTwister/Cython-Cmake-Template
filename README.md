# Cython-Cmake-Template

A template for Python package generation with pre-compiled C/C++ modules using Cmake and Cython

## Getting Started

### Prerequisites

- Install Cmake
- Install a functioning C/C++ compiler
    - It's best to use MSVC on Windows. If you don't want to install a full version of Visual Studio, just install
      the [Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019), which is a **standalone CLI** toolset
    - If you are on UNIX, just use GCC/G++ by installing `apt install build-essentials`
- Install Python 3
- Install the build requirements with
  ```bash
  pip install Cython wheel setuptools
  ```

### Build

- Build your static C/C++ library using Cmake ([what is a static library?](https://www.geeksforgeeks.org/difference-between-static-and-shared-libraries/)):
    ```bash
  mkdir build
  cd build
  cmake -DCMAKE_BUILD_TYPE=Release ..
  cmake --build . --config Release # invokes "make" or similar tool
  ```

- Build your Python extension modules (`.pyd` on Windows / `.so` on UNIX).

  *This step may be skipped since the next one will automatically trigger an extension build, but we want the compiler to use 4 cores (`-j 4`), to build the modules in-place (`-i`)
  and to force compilation so that changes will always get compiled (`-f`):*
  ```bash
  python setup.py build_ext -f -i -j 4
  ```

- Build your Python wheel, which includes the pre-compiled `.pyd`/`.so` files:
  ```bash
  python setup.py bdist_wheel
  ```
