#!/usr/bin/env python3


"""
This module illustrates how to do simple caching
in python. This time, we will do FIFO caching.
If the cache is at maximum capacity, we will discard
the first item in and add the new one (FIFO)
"""

from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching.
    This class represents a caching system using the LRU algorithm.
    """

    def __init__(self):
        """Initialize LRUCache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Store the item in cache_data using key as the identifier.
        
        Args:
            key: Key identifying the item.
            item: Item to be stored in cache.

        If key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS,
        it discards the least recently used item (LRU algorithm).
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieve an item from cache_data using key as the identifier.
        
        Args:
            key: Key identifying the item.

        Returns:
            The item identified by key if it exists in cache_data, None otherwise.
            If key is None, this method returns None.
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            self.cache_data.move_to_end(key)
            return value
        return None