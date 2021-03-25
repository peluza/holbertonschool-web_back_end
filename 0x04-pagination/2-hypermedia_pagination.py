#!/usr/bin/env python3
"""simple pagination"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page

        Args:
            page (int, optional): number pages. Defaults to 1.
            page_size (int, optional): number pages. Defaults to 10.

        Returns:
            List[List]: data the file
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index = index_range(page, page_size)
        start = index[0]
        end = index[1]
        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get_hyper

        Args:
            page (int, optional): number pages. Defaults to 1.
            page_size (int, optional): number pages. Defaults to 10.

        Returns:
            dict: data the file
        """
        pages_data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)
        all_data = {
            'page_size': len(pages_data),
            'page': page,
            'data': pages_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_pages
        }
        return all_data

