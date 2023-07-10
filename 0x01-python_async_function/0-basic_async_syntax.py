#!/usr/bin/env python3
"""Creating an async function wait_random"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random time below 10 seconds"""
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
