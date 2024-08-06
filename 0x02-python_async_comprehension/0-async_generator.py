#!/usr/bin/env python3
"""
0-Async Generator
A coroutine that takes no arguments, loops 10 times each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
"""

import asyncio
import random


async def async_generator():
    """async generator function that returns random numbers"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
