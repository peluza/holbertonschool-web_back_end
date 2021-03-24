#!/usr/bin/python3
"""lru cache"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache

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
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """get

        Args:
            key (dict): dict

        Returns:
            cache: cache our none
        """
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        else:
            return None
