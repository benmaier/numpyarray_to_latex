import unittest

import numpy as np

from numpyarray_to_latex import get_ltx

A = np.arange(100).reshape(10,10)
B = (np.arange(9)-4).reshape(3,3)
C = (np.arange(9)-2).reshape(3,3)
D = np.arange(4)
E = B.copy()
E[1,1] = 1e27
E[1,2] = 1e-27
F = B + 1j * C * 10**C

class LatexTest(unittest.TestCase):

    def test_latex(self):
        pass


if __name__ == "__main__":

    T = LatexTest()
    T.test_latex()
