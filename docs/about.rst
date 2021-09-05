About
=====

|CircleCI|

Format numpy arrays as LaTeX arrays. This is a fork of
`array_to_latex <https://github.com/josephcslater/array_to_latex>`__ by
`@josephcslater <https://github.com/josephcslater>`__.

-  repository: https://github.com/benmaier/numpyarray_to_latex/
-  documentation: http://numpyarray-to-latex.readthedocs.io/

.. code:: python

   >>> import numpy as np
   >>> from numpyarray_to_latex import to_ltx
   >>> tex = to_ltx(np.random.randn(2,2))
   >>> print(tex)
   \\left(
   \\begin{array}
     2.0156 & -0.3230\\\\
     0.0477 &  0.0184
   \\end{array}
   \\right)

Install
-------

.. code:: bash

   pip install numpyarray_to_latex

``numpyarray_to_latex`` was developed and tested for

-  Python 3.6
-  Python 3.7
-  Python 3.8
-  Python 3.9
-  Python 3.10

So far, the package's functionality was tested on Mac OS X and CentOS
only.

Dependencies
------------

``numpyarray_to_latex`` directly depends on the following packages which
will be installed by ``pip`` during the installation process

-  ``numpy>=1.0``

Documentation
-------------

The full documentation is available at
`numpyarray-to-latex.readthedocs.io <http://numpyarray-to-latex.readthedocs.io>`__.

Examples
--------

Default Python
~~~~~~~~~~~~~~

.. code:: python

   import numpy as np
   from numpyarray_to_latex.jupyter import to_jup
   from numpyarray_to_latex import to_ltx

   tex = to_ltx(np.random.randn(2,2))
   print(tex)

.. code::

   \\left(
   \\begin{array}
     2.0156 & -0.3230\\\\
     0.0477 &  0.0184
   \\end{array}
   \\right)

.. code:: python

   print(to_ltx(np.random.randn(2,2),
          latexarraytype='array',
          is_row_vector=False,
          mark_color='yellow',
          mark_elements=[(1,1)], 
          brackets='(]',
          separate_columns=[0,1],
          separate_rows=[0,1],))

.. code::

   \\left(
   \\begin{array}{c|c}
     0.3498 &  0.4393\\\\
     \\hline
    -0.8521 & \\colorbox{yellow}{$-0.6412$}
   \\end{array}
   \\right]

In Jupyter Notebooks
~~~~~~~~~~~~~~~~~~~~

.. code:: python

   import numpy as np
   from numpyarray_to_latex.jupyter import to_jup

   to_jup(np.random.randn(10,10),
          mark_elements=[(1,1),(2,3),(7,0)],
          separate_columns=[0,1],
          separate_rows=[0,1],
         )

.. image:: https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/01.png
   :alt: 01

.. code:: python

   to_jup(np.random.randn(2),
          mark_elements=[1,],
          separate_columns=[0,1],
          separate_rows=[0,1],
         )

.. image:: https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/02.png
   :alt: 02

.. code:: python

   to_jup(np.random.randn(2),
          is_row_vector=False,
          mark_elements=[1,],
          separate_columns=[0,1],
          separate_rows=[0,1],
          mark_color='yellow',
          brackets='(]',
         )

.. image:: https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/03.png
   :alt: 03

.. code:: python

   to_jup(np.random.randn(2,2),
          latexarraytype='Vmatrix',
          is_row_vector=False,
          separate_rows=[0,1],
         )

.. image:: https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/04.png
   :alt: 04

.. code:: python

   to_jup(np.random.randn(2,2)+1j*np.random.randn(2,2),
          mark_elements=[(0,1)],
         )

.. image:: https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/05.png
   :alt: 05

.. code:: python

   to_jup(np.random.randn(2,2)+1j*np.random.randn(2,2),
          mark_elements=[(0,1)],
          fmt='{:4.2e}',
         )

.. image:: https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/06.png
   :alt: 06

Changelog
---------

Changes are logged in a `separate
file <https://github.com/benmaier/numpyarray_to_latex/blob/main/CHANGELOG.md>`__.

License
-------

This project is licensed under the `MIT
License <https://github.com/benmaier/numpyarray_to_latex/blob/main/LICENSE>`__.
Note that this excludes any images/pictures/figures shown here or in the
documentation.

Contributing
------------

If you want to contribute to this project, please make sure to read the
`code of
conduct <https://github.com/benmaier/numpyarray_to_latex/blob/main/CODE_OF_CONDUCT.md>`__
and the `contributing
guidelines <https://github.com/benmaier/numpyarray_to_latex/blob/main/CONTRIBUTING.md>`__.
In case you're wondering about what to contribute, we're always
collecting ideas of what we want to implement next in the `outlook
notes <https://github.com/benmaier/numpyarray_to_latex/blob/main/OUTLOOK.md>`__.

|Contributor Covenant|

Dev notes
---------

Fork this repository, clone it, and install it in dev mode.

.. code:: bash

   git clone git@github.com:YOURUSERNAME/numpyarray_to_latex.git
   make

If you want to upload to PyPI, first convert the new ``README.md`` to
``README.rst``

.. code:: bash

   make readme

It will give you warnings about bad ``.rst``-syntax. Fix those errors in
``README.rst``. Then wrap the whole thing

.. code:: bash

   make pypi

It will probably give you more warnings about ``.rst``-syntax. Fix those
until the warnings disappear. Then do

.. code:: bash

   make upload

.. |CircleCI| image:: https://circleci.com/gh/benmaier/numpyarray_to_latex.svg?style=svg
   :target: https://circleci.com/gh/benmaier/numpyarray_to_latex
.. |Contributor Covenant| image:: https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg
   :target: code-of-conduct.md
