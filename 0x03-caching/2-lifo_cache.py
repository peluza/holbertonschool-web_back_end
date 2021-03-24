#!/usr/bin/python3
"""lifo cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache

    Args:
        BaseCaching (obj):
    """
    def __init__(self):
        """__init__"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """put

        Args:
            key (dict):
            item (dict):
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.remove(key)
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                lastKeyDel = self.keys.pop(-2)
                del self.cache_data[lastKeyDel]
                print("DISCARD: {}".format(lastKeyDel))

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
