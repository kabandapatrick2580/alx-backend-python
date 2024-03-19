import asyncio
from typing import List
from your_previous_file_name import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with specified max_delay.

    Args:
        n (int): Number of times wait_random should be spawned.
        max_delay (int): Maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    # Create a list to store the delays
    delays = []

    # Spawn wait_random n times with specified max_delay
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays