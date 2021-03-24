#!/usr/bin/python3
"""basic chache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache

    Args:
        BaseCaching (obj):
    """

    def put(self, key, item):
        """put

        Args:
            key (dict):
            item (dict):
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get

        Args:
            key (dict): dict

        Returns:
            cache: cache our none
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
