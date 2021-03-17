#!/usr/bin/env python3
"""measure runtime"""

import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time

    Args:
        n (int): number random
        max_delay (int): maximun vlaue

    Returns:
        float: result total
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total = (end - start) / n
    return total
