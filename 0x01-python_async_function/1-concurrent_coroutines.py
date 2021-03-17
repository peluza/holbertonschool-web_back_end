#!/usr/bin/env python3
"""1-concurrent_corountines"""

import asyncio
import random
import typing

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """wait_n

    Args:
        n (int): number random
        max_delay (int): maximun vlaue

    Returns:
        typing.List[float]: list of all delays
    """

    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    tasks_delay = []
    for task in asyncio.as_completed(tasks):
        task_delay: float = await task
        tasks_delay.append(task_delay)

    return tasks_delay
