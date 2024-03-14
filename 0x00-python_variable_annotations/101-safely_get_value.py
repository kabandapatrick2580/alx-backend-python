#!/usr/bin/env python3

from typing import TypeVar, Dict, Any, Optional

# Define a generic type variable
T = TypeVar('T')


def safely_get_value(dct: Dict[Any, T], key: Any,
                     default: Optional[T] = None) -> Optional[T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Dict[Any, T]): The dictionary to search for the key.
        key (Any): The key to search for in the dictionary.
        default (Optional[T], optional): The default value
        to return if the key is not found. Defaults to None.

    Returns:
        Optional[T]: The value corresponding to the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
