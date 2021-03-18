#!/usr/bin/env python3
"""async generator"""

import random
import typing
import asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    """async_generator

    Returns:
        typing.Generator[float, None, None]: Typing generator

    Yields:
        Iterator[typing.Generator[float, None, None]]: Interator generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
