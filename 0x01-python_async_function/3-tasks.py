#!/usr/bin/env python3
"""
Module providing a function to asynchronously await random delays.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task to asynchronously await a random delay.

    Args:
        max_delay (float): The maximum delay in seconds for the random delay.

    Returns:
        asyncio.Task: A Task representing the asynchronous execution of wait_random.
    """
    # Get the current event loop
    loop = asyncio.get_event_loop()

    # Create a task to asynchronously await the random delay
    task = loop.create_task(wait_random(max_delay))

    return task
