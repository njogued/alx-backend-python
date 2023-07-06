#!/usr/bin/env python3
"""Function to safely get value of a key in dict"""
from typing import Mapping
from typing import Any
from typing import Union
import typing


def safely_get_value(dct: Mapping,
                     key: Any, default: Union[typing.TypeVar('~T'), None] =
                     None) -> Union[Any, typing.TypeVar('~T')]:
    """Safely get value for a key in dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
