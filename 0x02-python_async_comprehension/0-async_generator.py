#!/usr/bin/env python3
"""async_generator coroutine that yields a random module"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Loop in a range of 10 and then return a random value"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
