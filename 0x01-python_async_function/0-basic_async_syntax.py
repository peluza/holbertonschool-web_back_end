#!/usr/bin/env python3
""" basic async syntax"""


import asyncio
import random

async def wait_random(max_delay: int=10) -> float:
    """wait_random

    Args:
        max_delay (int, optional): integer. Defaults to 10.

    Returns:
        float: randon number between 0 and mas_dalay
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
