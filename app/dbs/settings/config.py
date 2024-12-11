import redis

r = redis.Redis(
    host='redis-13810.c253.us-central1-1.gce.redns.redis-cloud.com',
    port=13810,
    password="irCrPqAYxM6vEknZceRKxaV34XsH3frC",
    decode_responses=True
)
value = {
    "priority":1,
    "duration":55
}
r.hset("32.164158,34.855313", mapping=value)
