import string
import random
from typing import Optional


def pretty_list(l:list, seperator: Optional[str] = ", "):

    output = ""

    for i in l:
        output += i + seperator

    return output.rstrip(seperator)


def random_string(length: int) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation # a-zA-Z0-9
    return ''.join(random.choices(chars, k=length))