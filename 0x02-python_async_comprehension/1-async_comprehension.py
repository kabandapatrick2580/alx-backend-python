#!/usr/bin/env python3
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers
    using an asynchronous comprehension over async_generator.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    # Using asynchronous comprehension to collect 10 random numbers
    # Iterate asynchronously over async_generator to get 10 random numbers
    # async_generator is an asynchronous generator that yields random numbers
    random_numbers = [i async for i in async_generator()]
    
    # Return the list of 10 random numbers
    return random_numbers
