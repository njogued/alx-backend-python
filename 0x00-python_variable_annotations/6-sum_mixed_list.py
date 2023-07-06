#!/usr/bin/env python3
"""Return a sum of mixed list with floats and ints"""
from typing import List
from typing import Union

mlist = Union[int, float]
flist = List[mlist]


def sum_mixed_list(mxd_lst: flist) -> float:
    """Returns the sum of values as float"""
    return float(sum(mxd_lst))
