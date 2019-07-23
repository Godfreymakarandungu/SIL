import redis

redisClient = redis.StrictRedis(host="localhost",port="6379",db=0)
redisClient.set("Language","Python 2.x")
print(redisClient.get("Language"))
redisClient.set("Language","Python 3.x")
print(redisClient.get("Language"))