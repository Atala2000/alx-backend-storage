import redis

r = redis.Redis()
# r.mset(
#     {
#         "Croatia": "Zagreb",
#         "Bahamas": "Nassau",
#     }
# )

print(r.get("Croatia").decode("utf-8"))
