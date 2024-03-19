import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: Total runtime in seconds.
    """
    # Record the start time before executing async_comprehension
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    # Each call to async_comprehension will collect 10 random numbers asynchronously
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    # Record the end time after all async_comprehension calls have completed
    end_time = asyncio.get_event_loop().time()

    # Calculate the total runtime by subtracting start time from end time
    total_runtime = end_time - start_time

    # Return the total runtime
    return total_runtime
