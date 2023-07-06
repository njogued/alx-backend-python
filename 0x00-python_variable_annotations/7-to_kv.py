#!/usr/bin/env python3
"""A function that takes str and returns tuple"""
from typing import Union
from typing import Tuple

digit = Union[int, float]
tupl = Tuple[str, float]


def to_kv(k: str, v: digit) -> tupl:
    """Return a tuple from values given"""
    return (k, v ** 2)
