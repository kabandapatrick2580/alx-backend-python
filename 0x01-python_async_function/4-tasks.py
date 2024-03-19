#!/usr/bin/env python3
"""
Module providing asynchronous coroutines for concurrent
waiting with random delays.
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that concurrently awaits random delays.

    Args:
        n (int): The number of times to concurrently await random delays.
        max_delay (float): The maximum delay in seconds for each random delay.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create an empty list to store the delays
    delays = []

    # Create tasks to concurrently await random delays using task_wait_random
    the_tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Wait for all tasks to complete and gather the results
    the_results = await asyncio.gather(*the_tasks)

    # Return the list of delays in ascending order
    return sorted(the_results)
