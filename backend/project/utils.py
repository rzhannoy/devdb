import uuid


def gen_random_string(limit=None):
    s = uuid.uuid4().hex
    s = s if not limit else s[:limit]
    return s
