"""
Wrapper to display an array in a jupyter notebook.
"""

import numpy as np
from IPython.display import display, Math
from numpyarray_to_latex import to_ltx

def to_jup(a,
           fmt='{:6.2f}',
           latexarraytype='array',
           imstring='i',
           is_row_vector=True,
           mathform=True,
           brackets='()',
           mark_elements=[],
           mark_color='pink',
           separate_columns=[],
           separate_rows=[],
           ):
    r"""
    Display a LaTeX-formatted numpy array in a Jupyter notebook.

    Parameters
    ----------
    a : numpy.ndarray
    fmt : str, default = '{:6.2f}'
        python 3 formatter, optional-
        https://mkaz.tech/python-string-format.html
    latexarraytype : str, default = 'array'
        Any of

        ..code ::

            "array"
            "pmatrix"
            "bmatrix"
            "vmatrix"
            "Vmatrix"
            "Bmatrix"

        if "array", you can specifiy the brackets
        with the keyword ``brackets``.
    imstring : str, default = 'i'
        Character to use to represent the imaginary unit.
        Usually ``'i'`` or ``'j'``
    is_row_vector : bool, default = True
        If the array is 1D, should the output be
        a row (True) or column (False) vector?
    mathform : bool, default = True
        wether to convert strings like ``1e+05``
        to ``1\times10^{5}``.
    brackets : iterable, default = '()'
        which brackets to use to wrap the matrix
        (must be two elements long).
        Use ``brackets = None`` if you don't want
        any brackets around the array.
    mark_elements : list, default = []
        list of tuples containing element indices that
        should be marked with a colorbox.
    mark_color : str, default = 'pink'
        The color with which to mark matrix elements.
    separate_columns : list, default = []
        list of column indices after which a vertical
        line should be drawn
    separate_rows : list, default = []
        list of row indices after which a horizontal
        line should be drawn

    Returns
    -------
    out: str
        Formatted LaTeX string

    Examples
    --------
    >>> from numpyarray_to_latex.jupyter import to_jup
    >>> to_jup([[2.,2.],[2.,2.]])

    """
    tex = to_ltx(a,
               fmt=fmt,
               latexarraytype=latexarraytype,
               imstring=imstring,
               is_row_vector=is_row_vector,
               mathform=mathform,
               brackets=brackets,
               mark_elements=mark_elements,
               mark_color=mark_color,
               separate_columns=separate_columns,
               separate_rows=separate_rows,
            )
    tex = '\\require{color}\n' + tex
    display(Math(tex))
