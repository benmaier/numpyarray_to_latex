"""
Provide helper functions.
"""

import numpy as np

def math_form(number, is_imaginary=False, mathform=True):
    r"""
    Convert a float number formatted in scientific notation
    to the corrsponding LateX format (e.g. ``2\times10^{2}``).
    """
    if mathform:
        if 'e' in number:
            significand, exponent = number.split('e')
            if exponent.startswith('+'):
                exponent = exponent.lstrip('+')
                exponent = exponent.lstrip('0')
            elif exponent.startswith('-'):
                exponent = exponent.lstrip('-')
                exponent = exponent.lstrip('0')
                exponent = '-' + exponent

            if exponent != '':
                number = significand + '\\times 10^{'+ exponent + '}'
            else:
                number = significand
    return number
