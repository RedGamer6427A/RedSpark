from typing import Callable

import time

def measure_performance(code: Callable):

    start_time = time.perf_counter()
    code()
    end_time = time.perf_counter()

    return end_time - start_time
