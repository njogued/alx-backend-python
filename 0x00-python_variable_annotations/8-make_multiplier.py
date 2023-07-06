#!/usr/bin/env python3
"""Type-annotated function that returns Callable function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a function given a float"""
    def multiplez(x: float) -> float:
        """Callable function to be returned"""
        return x * multiplier
    return multiplez
