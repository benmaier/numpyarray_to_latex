```python
import numpy as np
from numpyarray_to_latex.jupyter import to_jup
from numpyarray_to_latex import to_ltx
```


```python
tex = to_ltx(np.random.randn(2,2))
print(tex)
```

    \left(
    \begin{array}
      2.0156 & -0.3230\\
      0.0477 &  0.0184
    \end{array}
    \right)



```python
to_jup(np.random.randn(10,10),
       mark_elements=[(1,1),(2,3),(7,0)],
       separate_columns=[0,1],
       separate_rows=[0,1],
      )
```

![01](timg/01.png)



```python
to_jup(np.random.randn(2),
       mark_elements=[1,],
       separate_columns=[0,1],
       separate_rows=[0,1],
      )
```


$\displaystyle \require{color}
\left(
\begin{array}{c|c}
    0.03 & \colorbox{pink}{$   0.30$}
\end{array}
\right)$



```python
to_jup(np.random.randn(2),
       is_row_vector=False,
       mark_elements=[1,],
       separate_columns=[0,1],
       separate_rows=[0,1],
       mark_color='yellow',
       brackets='(]',
      )
```


$\displaystyle \require{color}
\left(
\begin{array}{c}
  -0.73\\
  \hline
 \colorbox{yellow}{$   0.27$}
\end{array}
\right]$



```python
to_jup(np.random.randn(2,2),
       latexarraytype='Vmatrix',
       is_row_vector=False,
       separate_rows=[0,1],
      )
```


$\displaystyle \require{color}
\begin{Vmatrix}
    1.11 &  -1.75\\
  \hline
  -0.99 &    0.47
\end{Vmatrix}$



```python
to_jup(np.random.randn(2,2)+1j*np.random.randn(2,2),
       mark_elements=[(0,1)],
      )
```


$\displaystyle \require{color}
\left(
\begin{array}
    2.76+ -0.85i & \colorbox{pink}{$   1.07+ -1.39i$}  \\
    0.08+  1.39i &  -0.35+  0.03
\end{array}
\right)$



```python
to_jup(np.random.randn(2,2)+1j*np.random.randn(2,2),
       mark_elements=[(0,1)],
       fmt='{:4.2e}',
      )
```


$\displaystyle \require{color}
\left(
\begin{array}
  3.88\times 10^{-1}-1.93\times 10^{-1}i & \colorbox{pink}{$ 1.70-5.96\times 10^{-1}i$}  \\
 -8.87\times 10^{-1}+1.17i & -1.12+1.53
\end{array}
\right)$



```python
print(to_ltx(np.random.randn(2,2),
       latexarraytype='array',
       is_row_vector=False,
       mark_color='yellow',
       mark_elements=[(1,1)], 
       brackets='(]',
       separate_columns=[0,1],
       separate_rows=[0,1],))
```

    \left(
    \begin{array}{c|c}
      0.3498 &  0.4393\\
      \hline
     -0.8521 & \colorbox{yellow}{$-0.6412$}
    \end{array}
    \right]



```python

```
