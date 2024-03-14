#!/usr/bin/env python3

from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Return the first element of the list if it exists, otherwise return None.

    Args:
        lst (List[Any]): The list from which to extract the first element.

    Returns:
        Union[Any, None]: The first element of the lst if it exst, othwz None.
    """
    if lst:
        return lst[0]
    else:
        return None
