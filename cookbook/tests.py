#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from numpyarray_to_latex import to_ltx


# In[7]:


A = np.arange(100).reshape(10,10).astype(float)
B = (np.arange(9)-4).reshape(3,3).astype(float)
C = (np.arange(9)-2).reshape(3,3).astype(float)
D = np.arange(4).astype(float)
E = B.copy()
E[1,1] = 1e27
E[1,2] = 1e-27
F = B + 1j * E * 10**C
G = B + 1j * C


with open('test_output/large_matrix.tex','w') as f:
    tex = to_ltx(A,
       mark_elements=[(1,1),(2,3),(7,0)],
       separate_columns=[0,1],
       separate_rows=[0,1],
      )
    f.write(tex)

with open('test_output/row_vector.tex','w') as f:
    tex = to_ltx(D,
           mark_elements=[1,],
           separate_columns=[0,1],
           separate_rows=[0,1],
          )
    f.write(tex)

with open('test_output/column_vector.tex','w') as f:
    tex = to_ltx(D,
       is_row_vector=False,
       mark_elements=[1,],
       separate_columns=[0,1],
       separate_rows=[0,1],
       mark_color='yellow',
       brackets='(]',
      )
    f.write(tex)


with open('test_output/Vmatrix.tex','w') as f:
    tex = to_ltx(D,
       latexarraytype='Vmatrix',
       is_row_vector=False,
       separate_rows=[0,1],
      )
    f.write(tex)



with open('test_output/imaginary.tex','w') as f:
    tex = to_ltx(G,
           mark_elements=[(0,1)],
      )
    f.write(tex)


with open('test_output/imaginary_exp.tex','w') as f:
    tex = to_ltx(F,
           mark_elements=[(0,1)],
           fmt='{:4.2e}',
          )
    f.write(tex)
