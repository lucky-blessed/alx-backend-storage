#!/usr/bin/env python3
"""
Cache class to store data in Redis.
"""


import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class that interacts with Redis.
    """

    def __init__(self):
        """
        Initialize the Redis client and flush the database
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a random key and returns the key

        Args:
            data (Union[str, bytes, int, float]): The data to be stored

        Returns:
            str: The key under which the data is stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
