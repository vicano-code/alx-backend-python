#!/usr/bin/env python3
"""
1-Async Comprehensions
A coroutine using async comprehension
Use async comprehension in the async-generator function
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine using async comprehension"""
    random_numbers = [i async for i in async_generator()]
    return random_numbers
