#!/usr/bin/env python3
"""tasks"""

import asyncio
import random
import time

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random

    Args:
        max_delay (int): maximun vlaue

    Returns:
        asyncio.Task: Tasks
    """
    createTask = asyncio.create_task(wait_random(max_delay))
    return createTask
