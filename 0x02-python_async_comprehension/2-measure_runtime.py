#!/usr/bin/env python3
"""
2-Run time for four parallel comprehensions
A coroutine that will execute async_comprehension four times in parallel
using asyncio.gather
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four times in parallel
      using asyncio.gather
    """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    runtime = end - start
    return runtime
