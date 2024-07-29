import redis

redis_db = redis.StrictRedis(host='10.12.131.11', port=9899, db=0, password='rt11sjrt11sj')

def set_value(key, value):
    return redis_db.set(key, value)

def get_value(key):
    return redis_db.get(key)