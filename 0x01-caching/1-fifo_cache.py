#!/usr/bin/env python3


"""
This module illustrates how to do simple caching
in python. This time, we will do FIFO caching.
If the cache is at maximum capacity, we will discard
the first item in and add the new one (FIFO)
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching.
    This class represents a caching system using the FIFO algorithm.
    """

    def __init__(self):
        """Initialize FIFOCache."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Store the item in cache_data using key as the identifier.
        
        Args:
            key: Key identifying the item.
            item: Item to be stored in cache.

        If key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS,
        it discards the first item put in cache (FIFO algorithm).
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.keys) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.keys.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Retrieve an item from cache_data using key as the identifier.
        
        Args:
            key: Key identifying the item.

        Returns:
            The item identified by key if it exists in cache_data, None otherwise.
            If key is None, this method returns None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None