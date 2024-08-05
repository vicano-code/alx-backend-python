#!/usr/bin/env python3
"""
Measure the runtime:
A function that takes in 2 int args and returns the avg execution time
for an asyncio process
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
      n - spawn
      max_delay - max wait
      returns average execution time
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return total_time / n
