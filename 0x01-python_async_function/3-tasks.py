#!/usr/bin/env python3
"""
Create asyncio task:
A regular function that takes in an int argument and returns an asyncio.Task
"""
import asyncio
import time


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns an asyncio task"""
    task = asyncio.create_task(wait_random(max_delay))

    return task
