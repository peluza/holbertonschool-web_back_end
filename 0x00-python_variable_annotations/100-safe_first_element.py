#!/usr/bin/env python3
"""100-safe_first_elemnt.py"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first_element

    Args:
        lst (Sequence[Any]): list

    Returns:
        Union[Any, None]: list or none
    """
    if lst:
        return lst[0]
    else:
        return None
