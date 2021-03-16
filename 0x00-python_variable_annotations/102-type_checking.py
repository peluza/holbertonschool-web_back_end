#!/usr/bin/env python3
"""102-type_checking.py"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """zoom_array

    Args:
        lst (Tuple): Tuple
        factor (int, optional): int. Defaults to 2.

    Returns:
        List: list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
