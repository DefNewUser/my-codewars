from time import time
from functools import wraps


def speed_timer(function):
    @wraps(function)
    def inner(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f"Time of code execution: {end_time - start_time}")
        return result

    return inner


# @speed_timer
# def sum_range_numbers():
#     return sum([number for number in range(100000)])
#
#
# print(sum_range_numbers())





