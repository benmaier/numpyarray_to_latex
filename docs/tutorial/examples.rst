Pure Python
===========

.. code:: python

    import numpy as np
    from numpyarray_to_latex.jupyter import to_jup
    from numpyarray_to_latex import to_ltx

    tex = to_ltx(np.random.randn(2,2))
    print(tex)


.. parsed-literal::

    \left(
    \begin{array}
      2.0156 & -0.3230\\
      0.0477 &  0.0184
    \end{array}
    \right)

.. code:: python

    print(to_ltx(np.random.randn(2,2),
           latexarraytype='array',
           is_row_vector=False,
           mark_color='yellow',
           mark_elements=[(1,1)],
           brackets='(]',
           separate_columns=[1,2],
           separate_rows=[1,2],))


.. parsed-literal::

    \left(
    \begin{array}{c|c}
      0.3498 &  0.4393\\
      \hline
     -0.8521 & \colorbox{yellow}{$-0.6412$}
    \end{array}
    \right]

Jupyter Notebooks
=================

.. code:: python

    import numpy as np
    from numpyarray_to_latex.jupyter import to_jup

    to_jup(np.random.randn(10,10),
           mark_elements=[(1,1),(2,3),(7,0)],
           separate_columns=[1,2],
           separate_rows=[1,2],
          )



.. math::

    \displaystyle \require{color}
    \left(
    \begin{array}{c|c|cccccccc}
      -0.60 &  -0.25 &    0.78 &  -1.51 &    0.23 &  -1.09 &    1.83 &    0.20 &    0.53 &  -0.36\\
      \hline
        1.57 & \colorbox{pink}{$   0.11$}   &    0.10 &  -0.01 &    0.32 &    0.63 &  -1.29 &  -1.51 &    1.70 &  -0.23\\
      \hline
        0.05 &  -0.02 &  -1.21 & \colorbox{pink}{$ -0.59$}   &    1.40 &    1.08 &    0.73 &  -0.02 &  -1.35 &    0.09\\
        0.12 &  -0.33 &  -0.77 &  -0.21 &    1.72 &    0.27 &    1.71 &    0.22 &    1.84 &  -0.33\\
        1.03 &  -2.00 &    0.95 &  -0.94 &    0.37 &  -0.64 &  -0.05 &    0.37 &  -0.86 &    0.01\\
      -2.01 &    0.51 &    1.54 &    0.62 &    0.61 &  -0.52 &    0.02 &  -1.28 &  -0.35 &  -0.12\\
        0.38 &  -0.06 &    1.03 &  -0.35 &    1.54 &  -0.20 &  -1.75 &  -0.39 &    0.30 &    0.66\\
     \colorbox{pink}{$   0.43$}   &  -1.78 &  -0.30 &    1.36 &  -0.70 &    0.40 &    0.41 &    0.75 &  -1.62 &    0.28\\
        0.49 &    0.83 &  -0.55 &    0.62 &  -0.37 &  -0.12 &  -1.42 &    1.97 &  -0.28 &  -0.16\\
        0.02 &  -1.31 &    0.12 &  -0.99 &    1.72 &    0.52 &  -1.89 &    0.90 &  -0.05 &    1.77
    \end{array}
    \right)


.. code:: python

    to_jup(np.random.randn(2),
           mark_elements=[1,],
           separate_columns=[1,2],
           separate_rows=[1,2],
          )



.. math::

    \displaystyle \require{color}
    \left(
    \begin{array}{c|c}
        0.03 & \colorbox{pink}{$   0.30$}
    \end{array}
    \right)


.. code:: python

    to_jup(np.random.randn(2),
           is_row_vector=False,
           mark_elements=[1,],
           separate_columns=[1,2],
           separate_rows=[1,2],
           mark_color='yellow',
           brackets='(]',
          )



.. math::

    \displaystyle \require{color}
    \left(
    \begin{array}{c}
      -0.73\\
      \hline
     \colorbox{yellow}{$   0.27$}
    \end{array}
    \right]


.. code:: python

    to_jup(np.random.randn(2,2),
           latexarraytype='Vmatrix',
           is_row_vector=False,
           separate_rows=[1],
          )



.. math::

    \displaystyle \require{color}
    \begin{Vmatrix}
        1.11 &  -1.75\\
      \hline
      -0.99 &    0.47
    \end{Vmatrix}


.. code:: python

    to_jup(np.random.randn(2,2)+1j*np.random.randn(2,2),
           mark_elements=[(0,1)],
          )



.. math::

    \displaystyle \require{color}
    \left(
    \begin{array}
        2.76+ -0.85i & \colorbox{pink}{$   1.07+ -1.39i$}  \\
        0.08+  1.39i &  -0.35+  0.03
    \end{array}
    \right)


.. code:: python

    to_jup(np.random.randn(2,2)+1j*np.random.randn(2,2),
           mark_elements=[(0,1)],
           fmt='{:4.2e}',
          )



.. math::

    \displaystyle \require{color}
    \left(
    \begin{array}
      3.88\times 10^{-1}-1.93\times 10^{-1}i & \colorbox{pink}{$ 1.70-5.96\times 10^{-1}i$}  \\
     -8.87\times 10^{-1}+1.17i & -1.12+1.53
    \end{array}
    \right)


