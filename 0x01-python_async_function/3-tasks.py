#!/usr/bin/env python3
"""create asyncio task"""
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Create an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
