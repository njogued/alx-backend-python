#!/usr/bin/env python3
"""wait_n function that returns all delays"""
from typing import List
import asyncio
from heapq import nsmallest
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executing wait_random concurrently"""
    values = [task_wait_random(max_delay) for _ in range(n)]
    results = asyncio.gather(**values)
    return nsmallest(n, results)
