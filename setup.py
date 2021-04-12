from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from os.path import normpath, join


def make_module(
        submodule_name: str, cython_src_files: list,
        c_src_paths: list = None, c_include_paths: list = None,
        c_libraries: list = None
):
    """ Generates the extensions for given Cython source files and C/C++
    source files or pre-compiled C/C++ libraries and normalizes paths

    Arguments:
        submodule_name (str): Name of the extension module that is to be built (may include ".")
        cython_src_files (List[str]): `.pyx` files to include during submodule compilation
        c_include_paths (List[str]): Directories where to look for `.h` files from external C/C++ code
        c_src_paths (List[str]): Directories where to look for implementations and libraries (`.cpp`, `.lib`)
        c_libraries (List[str]): Names of libraries to link against (`.lib`)

    Returns:
        Extension: Extension object for setup(cythonize([...]))
    """

    if c_include_paths is None: c_include_paths = []
    if c_libraries is None: c_libraries = []
    if c_src_paths is None: c_src_paths = []

    return Extension(
        name=".".join([module_name, submodule_name]),
        sources=[normpath(x) for x in cython_src_files],
        library_dirs=[normpath(x) for x in c_src_paths],
        include_dirs=[normpath(x) for x in c_include_paths],
        libraries=c_libraries,
    )


module_name = "nice_module"

setup(
    name=module_name,
    version="1.0.0",
    ext_modules=cythonize([
        make_module(
            "foobar", ["nice_module/foobar.pyx"],
            c_src_paths=["cpp_code/dist"],
            c_include_paths=["cpp_code/include"],
            c_libraries=["foobar"]
        )
    ],
        language_level="3"
    )
)
