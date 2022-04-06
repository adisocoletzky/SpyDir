from random import randint


def get_id(length):
    minimum = int(length * '1')
    maximum = int(length * '9')
    return str(randint(minimum, maximum))
