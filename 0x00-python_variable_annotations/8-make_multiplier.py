#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that accepts a float and
        returns the result of multiplying it by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Multiply a float by the given multiplier."""
        return x * multiplier
    return multiplier_function
