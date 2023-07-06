#!/usr/bin/env python3
"""Type-annotating a function to return types"""
from typing import Iterable
from typing import Sequence
from typing import Tuple
from typing import List

rtype = List[Tuple[Sequence, int]]


def element_length(lst: Iterable[Sequence]) -> rtype:
    """Return a tuple with element and the element length"""
    return [(i, len(i)) for i in lst]
