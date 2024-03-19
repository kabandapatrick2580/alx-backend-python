#!/usr/bin/env python3
"""
Module 2-measure_runtime.py providing a function to measure the total
execution time for wait_n.
"""

import time
import asyncio

# Import the coroutines from the previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total execution time for wait_n(n, max_delay) and return average time per call.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (float): Maximum delay in seconds for each wait_random.

    Returns:
        float: Average execution time per call.
    """
    start_time = time.perf_counter()

    # Run wait_n to measure execution time
    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()
    total_time = end_time - start_time

    # Return average execution time per call
    return total_time / n
