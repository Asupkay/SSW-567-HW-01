"""This module classifies triangle"""

import math
from numbers import Number


def classify_triangle(s_3, s_2, s_1):
    """Method that classifies triangles"""
    if not isinstance(s_3, Number) or not isinstance(s_2, Number) or not isinstance(s_1, Number):
        return 'NotATriangle'
    if s_3 + s_2 <= s_1 or s_3 + s_1 <= s_2 or s_2 + s_1 <= s_3:
        return 'NotATriangle'
    if s_3 == s_2 and s_3 == s_1:
        return 'Equilateral'

    is_i = (s_3 == s_2 and s_3 != s_1) or (s_3 == s_1 and s_3 != s_2) or (s_2 == s_1 and s_2 != s_3)
    if is_i:
        return 'Isoceles'

    a_pow = math.pow(s_3, 2)
    b_pow = math.pow(s_2, 2)
    c_pow = math.pow(s_1, 2)
    if a_pow + b_pow == c_pow or a_pow + c_pow == b_pow or b_pow + c_pow == a_pow:
        return 'Right'
    if s_3 != s_2 and s_2 != s_1:
        return 'Scalene'


