#!/usr/bin/env python3
"""wait_n function that returns all delays"""
from typing import List
from heapq import nsmallest
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executing wait_random concurrently"""
    values = []
    for i in range(n):
        values.append(await wait_random(max_delay))
    return nsmallest(n, values)
