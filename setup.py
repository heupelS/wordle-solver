from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

# include_dirs = [np.get_include()]

setup(ext_modules = cythonize("test_cy.pyx", language_level = "3"))
