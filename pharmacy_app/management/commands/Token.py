import random
import string


def gen_token(length=8):
    digits = "".join([random.choice(string.digits + string.ascii_letters) for i in range(length)])
    return digits


