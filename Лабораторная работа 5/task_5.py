from random import *
from string import *


def get_random_password(n=8) -> str:
    return ''.join(sample(ascii_uppercase + ascii_lowercase + digits, n))


print(get_random_password())

