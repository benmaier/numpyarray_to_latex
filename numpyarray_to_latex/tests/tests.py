import unittest

import numpy as np

from numpyarray_to_latex import to_ltx

import numpyarray_to_latex

import inspect
from pathlib import Path

import vaccontrib


def get_package_root():
    """Get the path of the package repository."""
    package_path = Path(inspect.getfile(numpyarray_to_latex))
    pkg_root = package_path.parents[0]
    return pkg_root

def get_data_dir():
    """Get the path of the package's data directory."""
    return get_package_root() / 'tests' / 'test_output'

A = np.arange(100).reshape(10,10).astype(float)
B = (np.arange(9)-4).reshape(3,3).astype(float)
C = (np.arange(9)-2).reshape(3,3).astype(float)
D = np.arange(4).astype(float)
E = B.copy()
E[1,1] = 1e27
E[1,2] = 1e-27
F = B + 1j * E * 10**C
G = B + 1j * C

class LatexTest(unittest.TestCase):

    def test_large_matrix(self):
        with open(get_data_dir() / 'large_matrix.tex','r') as f:
            tex = to_ltx(A,
               mark_elements=[(1,1),(2,3),(7,0)],
               separate_columns=[0,1],
               separate_rows=[0,1],
              )
            testtex = f.read()

    def test_row_vector(self):
        with open(get_data_dir() / 'row_vector.tex','r') as f:
            tex = to_ltx(D,
                   mark_elements=[1,],
                   separate_columns=[0,1],
                   separate_rows=[0,1],
                  )
            testtex = f.read()

    def test_column_vector(self):
        with open(get_data_dir() / 'column_vector.tex','r') as f:
            tex = to_ltx(D,
               is_row_vector=False,
               mark_elements=[1,],
               separate_columns=[0,1],
               separate_rows=[0,1],
               mark_color='yellow',
               brackets='(]',
              )
            testtex = f.read()

    def test_Vmatrix(self):
        with open(get_data_dir() / 'Vmatrix.tex','r') as f:
            tex = to_ltx(D,
               latexarraytype='Vmatrix',
               is_row_vector=False,
               separate_rows=[0,1],
              )
            testtex = f.read()

    def test_imaginary(self):
        with open(get_data_dir() / 'imaginary.tex','r') as f:
            tex = to_ltx(G,
                   mark_elements=[(0,1)],
              )
            testtex = f.read()

    def test_imaginary_exp(self):
        with open(get_data_dir() / 'imaginary_exp.tex','r') as f:
            tex = to_ltx(F,
                   mark_elements=[(0,1)],
                   fmt='{:4.2e}',
                  )
            testtex = f.read()


if __name__ == "__main__":

    T = LatexTest()
    T.test_large_matrix()
    T.test_row_vector()
    T.test_column_vector()
    T.test_Vmatrix()
    T.test_imaginary()
    T.test_imaginary_exp()
