from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from os.path import normpath, join


def make_module(
        submodule_name: str, cython_src_files: list,
        c_src_paths: list = None, c_include_paths: list = None,
        c_libraries: list = None
):
    """ Generates the extensions for given Cython source files and C/C++
    source files or pre-compiled C/C++ libraries"""

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


# examples_extension = Extension(
#     name=".".join([module_name, "vectors"]),  # creates "vectors" module in "cython_vector/"
#     sources=[
#         normpath('cython_vector/vectors.pyx')
#     ],
#     # libraries=["kacken"],
#     # library_dirs=[normpath('project/src/a')],
#     # include_dirs=[normpath('project/src/include')]
# )

module_name = "nice_module"

setup(
    name=module_name,
    version="1.0.0",
    ext_modules=cythonize([
        make_module(
            "foobar", ["nice_module/foobar.pyx"],
            c_src_paths=["cpp_code/dist"],  # path to the vectors_cpp.lib (static C++ library)
            c_include_paths=["cpp_code/include"],
            c_libraries=["foobar"]
        )
    ],
        language_level="3"
    )
)
