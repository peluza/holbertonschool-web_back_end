#!/usr/bin/env python3
"""9-elemnt_length.py"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length

    Args:
        lst (Iterable[Sequence]): Sequence

    Returns:
        List[Tuple[Sequence, int]]: Sequence
    """
    return [(i, len(i)) for i in lst]
