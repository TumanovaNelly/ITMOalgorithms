import sys
sys.path.append('../src')
from Main import main

import tracemalloc
import time

tracemalloc.start()
time_start = time.perf_counter()

main()

print(f"Excecution time = {time.perf_counter() - time_start} seconds")
current, peak = tracemalloc.get_traced_memory()
print(f"Memory used: {current / 10 ** 6:.3f} MB; Memory peak: {peak / 10 ** 6:.3f} MB")

