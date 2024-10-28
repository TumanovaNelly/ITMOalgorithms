import tracemalloc
import time

def time_memory(func):
    tracemalloc.start()
    time_start = time.perf_counter()

    func()

    print(f"Excecution time = {time.perf_counter() - time_start} seconds")
    current, peak = tracemalloc.get_traced_memory()
    print(f"Memory used: {current / 10 ** 6:.3f} MB; Memory peak: {peak / 10 ** 6:.3f} MB")

