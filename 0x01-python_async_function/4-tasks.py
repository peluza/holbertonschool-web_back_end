#!/usr/bin/env python3
"""tasks"""
import asyncio
import random
import typing

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """task_wait_n

    Args:
        n (int): number random
        max_delay (int): maximun vlaue

    Returns:
        typing.List[float]: list of all delays
    """
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))

    tasks_delay = []
    for task in asyncio.as_completed(tasks):
        task_delay: float = await task
        tasks_delay.append(task_delay)

    return tasks_delay
