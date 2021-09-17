# numpyarray\_to\_latex


[![CircleCI](https://circleci.com/gh/benmaier/numpyarray_to_latex.svg?style=svg)](https://circleci.com/gh/benmaier/numpyarray_to_latex)

Format numpy arrays as LaTeX arrays. This is a fork of [array_to_latex](https://github.com/josephcslater/array_to_latex) by [@josephcslater](https://github.com/josephcslater).

* repository: https://github.com/benmaier/numpyarray_to_latex/
* documentation: http://numpyarray-to-latex.readthedocs.io/

```python
>>> import numpy as np
>>> from numpyarray_to_latex import to_ltx
>>> tex = to_ltx(np.random.randn(2,2))
>>> print(tex)
\left(
\begin{array}
  2.0156 & -0.3230\\
  0.0477 &  0.0184
\end{array}
\right)
```

## Install

    pip install numpyarray_to_latex

`numpyarray_to_latex` was developed and tested for 

* Python 3.6
* Python 3.7
* Python 3.8
* Python 3.9
* Python 3.10

So far, the package's functionality was tested on Mac OS X and CentOS only.

## Dependencies

`numpyarray_to_latex` directly depends on the following packages which will be installed by `pip` during the installation process

* `numpy>=1.0`

## Documentation

The full documentation is available at [numpyarray-to-latex.readthedocs.io](http://numpyarray-to-latex.readthedocs.io).

## Examples

### Default Python

```python
import numpy as np
from numpyarray_to_latex.jupyter import to_jup
from numpyarray_to_latex import to_ltx

tex = to_ltx(np.random.randn(2,2))
print(tex)
```

```math
\left(
\begin{array}
  2.0156 & -0.3230\\
  0.0477 &  0.0184
\end{array}
\right)
```


```python
print(to_ltx(np.random.randn(2,2),
       latexarraytype='array',
       is_row_vector=False,
       mark_color='yellow',
       mark_elements=[(1,1)], 
       brackets='(]',
       separate_columns=[1,2],
       separate_rows=[1,2],))
```

```math
\left(
\begin{array}{c|c}
  0.3498 &  0.4393\\
  \hline
 -0.8521 & \colorbox{yellow}{$-0.6412$}
\end{array}
\right]
```


### In Jupyter Notebooks

```python
import numpy as np
from numpyarray_to_latex.jupyter import to_jup

to_jup(np.random.randn(10,10),
       mark_elements=[(1,1),(2,3),(7,0)],
       separate_columns=[1,2], # columns & rows that don't exist will be ignored
       separate_rows=[1,2],
      )
```

![01](https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/01.png)



```python
to_jup(np.random.randn(2),
       mark_elements=[1,],
       separate_columns=[1,2],
       separate_rows=[1,2],
      )
```


![02](https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/02.png)



```python
to_jup(np.random.randn(2),
       is_row_vector=False,
       mark_elements=[1,],
       separate_columns=[1,2],
       separate_rows=[1,2,3,4], # columns that don't exist will be ignored
       mark_color='yellow',
       brackets='(]',
      )
```


![03](https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/03.png)



```python
to_jup(np.random.randn(2,2),
       latexarraytype='Vmatrix',
       is_row_vector=False,
       separate_rows=[1],
      )
```


![04](https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/04.png)


```python
to_jup(np.random.randn(2,2)+1j*np.random.randn(2,2),
       mark_elements=[(0,1)],
      )
```


![05](https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/05.png)



```python
to_jup(np.random.randn(2,2)+1j*np.random.randn(2,2),
       mark_elements=[(0,1)],
       fmt='{:4.2e}',
      )
```

![06](https://raw.githubusercontent.com/benmaier/numpyarray_to_latex/main/img/06.png)


## Changelog

Changes are logged in a [separate file](https://github.com/benmaier/numpyarray_to_latex/blob/main/CHANGELOG.md).

## License

This project is licensed under the [MIT License](https://github.com/benmaier/numpyarray_to_latex/blob/main/LICENSE).
Note that this excludes any images/pictures/figures shown here or in the documentation.

## Contributing

If you want to contribute to this project, please make sure to read the [code of conduct](https://github.com/benmaier/numpyarray_to_latex/blob/main/CODE_OF_CONDUCT.md) and the [contributing guidelines](https://github.com/benmaier/numpyarray_to_latex/blob/main/CONTRIBUTING.md). In case you're wondering about what to contribute, we're always collecting ideas of what we want to implement next in the [outlook notes](https://github.com/benmaier/numpyarray_to_latex/blob/main/OUTLOOK.md).

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](code-of-conduct.md)

## Dev notes

Fork this repository, clone it, and install it in dev mode.

```bash
git clone git@github.com:YOURUSERNAME/numpyarray_to_latex.git
make
```

If you want to upload to PyPI, first convert the new `README.md` to `README.rst`

```bash
make readme
```

It will give you warnings about bad `.rst`-syntax. Fix those errors in `README.rst`. Then wrap the whole thing 

```bash
make pypi
```

It will probably give you more warnings about `.rst`-syntax. Fix those until the warnings disappear. Then do

```bash
make upload
```
