#!/usr/bin/env python3
"""
Create asyncio tasks and return delay list:
An update of task 1-concurrent_coroutines using the task_wait-random function
instead.
"""
import asyncio
import time
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn task_wait_random n times with the specified max_delay
    and returns the list of delays based on concurrency
    """
    # validate input
    if n is None or max_delay is None:
        return

    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
