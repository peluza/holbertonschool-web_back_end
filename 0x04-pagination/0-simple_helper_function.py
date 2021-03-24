#!/usr/bin/env python3
"""simple helper function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range

    Args:
        page (int): number page
        page_size (int): number siza pages

    Returns:
        Tuple[int, int]: print res for the pages
    """
    return ((page_size * (page - 1)), page_size * page)
