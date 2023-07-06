#!/usr/bin/env python3
"""add correct annotations"""
from typing import Sequence
from typing import Any
from typing import Union

lstype = Sequence[Any]
rtype = Union[Any, None]


def safe_first_element(lst: lstype) -> rtype:
    """Safe first element for a list or return none"""
    if lst:
        return lst[0]
    else:
        return None
