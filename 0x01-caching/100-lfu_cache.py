#!/usr/bin/env python3
"""
A class LFUCache that inherits from BaseCaching
and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A caching system
    Inherits from parent class BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """
        Assigns item value for the key 'key' to the dictionary
        self.cache_data
        if key or item is None; does nothing
        if number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS
        """
        if key is not None and item is not None:
            if len(self.keys) == BaseCaching.MAX_ITEMS:
                self._discard_lfu()
            self.cache_data[key] = item
            self._update_usage(key)

    def get(self, key):
        """
        if key is None or key does not exist in self.cache_data
        Returns None
        """
        if key is not None and key in self.cache_data:
            self._update_usage(key)
            return self.cache_data[key]
        return None

    def _discard_lfu(self):
        """
        discards least frequently used key
        """
        min_uses = min(self.uses.values())
        lfu_keys = [k for k, v in self.uses.items() if v == min_uses]
        lfu = min(self.keys, key=lambda k: self.keys.index(k)
                  if k in lfu_keys else float('inf'))
        del self.cache_data[lfu]
        self.keys.remove(lfu)
        del self.uses[lfu]
        print("DISCARD:", lfu)

    def _update_usage(self, key):
        """
        updates list
        """
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        self.uses[key] = self.uses.get(key, 0) + 1
