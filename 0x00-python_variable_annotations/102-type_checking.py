#!/usr/bin/env python3
"""Type checking the zoom array"""
from typing import Tuple
from typing import List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """This is a comment to pass pycodestyle, idk what the function does"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
