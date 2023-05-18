#!/usr/bin/env python3
"""
LRU caching: Least Recently Used
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    a caching system
    """
    def __init__(self):
        """
        child constructor
        """
        super().__init__()
        self.usage_history = []

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the
        item value for the key 'key'

        if key or item is none: does nothing

        Discards least recently used item if number of items
        in self.cache_data is higher than BaseCaching.MAX_ITEMS
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key not in self.usage_history:
            self.usage_history.append(key)

        last_item = list(self.cache_data)[0]

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(last_item)
            print("DISCARD: ", last_item)

    def get(self, key):
        """
        Returns value in self.cache_data linked
        to key
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.get(key)
