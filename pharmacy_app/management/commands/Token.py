from random import choice
import string

def GenToken(length=8):
    return ''.join([choice(string.letters) for i in range(length)]).join([choice(string.digits) for i in range(length)])
