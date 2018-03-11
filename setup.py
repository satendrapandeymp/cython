from distutils.core import setup
from Cython.Build import cythonize

src = raw_input("give your source file location : ")

setup(
    ext_modules = cythonize(src + "/*.pyx")
)
