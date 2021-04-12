<p float="left">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Breezeicons-apps-48-cmake.svg/1200px-Breezeicons-apps-48-cmake.svg.png" height="110"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Cython-logo.svg/1200px-Cython-logo.svg.png" height="100"/>
</p>

# Cython-Cmake-Template
[![GitHub license](https://img.shields.io/github/license/TheClockTwister/Cython-Cmake-Template)](https://github.com/TheClockTwister/Cython-Cmake-Template/blob/master/LICENSE.md)
[![GitHub issues](https://img.shields.io/github/issues/TheClockTwister/Cython-Cmake-Template)](https://github.com/TheClockTwister/Cython-Cmake-Template/issues)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/TheClockTwister/Cython-Cmake-Template/Continous%20integration?label=GitHub%20Build)

A template for Python package generation with pre-compiled C/C++ modules using
[Cmake](https://cmake.org/cmake/help/latest/) and [Cython](https://cython.readthedocs.io/en/latest/index.html)

## Features

- Easy and cross-platform C/C++ build system with [Cmake](https://cmake.org/cmake/help/latest/)
- Example config for auto-build with [GitHub Actions](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstrategy) CI
- Examples for a basic static library C++ project
- Examples for Python stub files (`.pyi` type hints)

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
