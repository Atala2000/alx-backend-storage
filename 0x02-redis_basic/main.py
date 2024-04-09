#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__("exercise").Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
print(local_redis.get("118f18e1-6069-4719-8847-6d549f034c6c"))
