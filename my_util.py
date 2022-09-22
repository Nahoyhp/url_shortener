import hashlib
import string
import random


def removeHttp(str):
    if str[:8] == "https://":
        return str[8:]
    if str[:7] == "http://":
        return str[7:]
    return str


def generate_shorten_url(size=5):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(0, int(size), 1))
