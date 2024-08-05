#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time with async:
An async routine that takes 2 args used to spawn delays and returnd the list
of the delays sorted in ascending order based on concurrency and not sort()
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    and returns the list of delays based on concurrency
    """
    # validate input
    if n is None or max_delay is None:
        return

    delays: List[float] = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
