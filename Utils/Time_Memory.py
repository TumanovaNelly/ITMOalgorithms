import tracemalloc
import time

def time_memory_print(func):
    tracemalloc.start()
    time_start = time.perf_counter()

    func()

    print(f"Excecution time = {time.perf_counter() - time_start} seconds")
    current, peak = tracemalloc.get_traced_memory()
    print(f"Memory used: {current / 10 ** 6:.3f} MB; Memory peak: {peak / 10 ** 6:.3f} MB")


def time_data(func) -> float:
    tracemalloc.start()
    time_start = time.perf_counter()

    func()

    return time.perf_counter() - time_start
