#!/usr/bin/env python3
"""Creating an async function wait_random"""
import random
import asyncio


async def wait_random(n=10):
    """Wait for random time below 10 seconds"""
    val = random.uniform(0, n)
    await asyncio.sleep(val)
    return val
