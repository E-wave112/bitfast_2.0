from datetime import timedelta
import redis
import json
from decouple import config
from utils.logger_file import get_logger_info

logger = get_logger_info(__name__)

REDIS_HOST = config("REDIS_HOST")
REDIS_PASSWORD = config("REDIS_PASSWORD")
REDIS_USERNAME = config("REDIS_USERNAME")
REDIS_PORT = config("REDIS_PORT")


def get_redis_instance():
    redis_instance = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=0,
        password=REDIS_PASSWORD,
        username=REDIS_USERNAME,
    )
    return redis_instance


def manage_redis_str(key, value, expiry):
    redis_instance = get_redis_instance()
    data = redis_instance.get(key)
    # if the value is not found, then add the value store it in redis for a specific time
    if data is None:
        redis_instance.set(key, value, ex=timedelta(minutes=expiry))
        data = redis_instance.get(key)
    logger.info(data)
    return data


def manage_redis_dict(key, value, expiry):
    redis_instance = get_redis_instance()
    value = json.dumps(value)
    data = redis_instance.get(key)
    # if the value is not found, then add the value store it in redis for a specific time
    if data is None:
        redis_instance.set(key, value, ex=timedelta(minutes=expiry))
        data = redis_instance.get(key)
    logger.info(data)
    return json.loads(data)
