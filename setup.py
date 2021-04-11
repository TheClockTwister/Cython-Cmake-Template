from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from os.path import normpath, join


def make_module(submodule_name: str, cython_src_files: list,
                c_src_paths: list = None, c_include_paths: list = None,
                c_libraries: list = None
                ):
    if c_include_paths is None:
        c_include_paths = []
    if c_libraries is None:
        c_libraries = []
    if c_src_paths is None:
        c_src_paths = []

    return Extension(
        # Cython source files
        name=".".join([module_name, submodule_name]),  # creates "vectors" module in "cython_vector/"
        sources=[normpath(x) for x in cython_src_files],

        # C/C++ source files or pre-compiled libraries
        libraries=c_libraries,
        library_dirs=[normpath(x) for x in c_src_paths],
        include_dirs=[normpath(x) for x in c_include_paths]
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

module_name = "cython_vector"

setup(
    name=module_name,
    version="1.0.0",
    ext_modules=cythonize([
        make_module("vectors", ["cython_vector/vectors.pyx"])
    ],
        language_level="3"
    )
)
