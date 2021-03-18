#!/usr/bin/env python3
""" async comprehension"""

import random
import typing
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """async_comprehension

    Returns:
        typing.List[float]: 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
