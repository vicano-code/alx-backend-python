#!/usr/bin/env python3
"""
The basics of async:
An asynchronous coroutine that takes in an integer argument and waits
for a random delay and returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async coroutine that demonstrates a randome delay"""
    if max_delay is None:
        return
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
