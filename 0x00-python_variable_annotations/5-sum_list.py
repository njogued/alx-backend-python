#!/usr/bin/env python3
"""Take a list of floats and return their value"""
from typing import List

flist = List[float]


def sum_list(input_list: flist) -> float:
    """Return the sum of values in input list"""
    return sum(input_list)
