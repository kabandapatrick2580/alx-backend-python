#!/usr/bin/env python3
"""module for random delays"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.
    
    Args:
        max_delay (int): Maximum delay in seconds (inclusive). Default is 10.
    
    Returns:
        float: Random delay between 0 and max_delay seconds (inclusive).
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
