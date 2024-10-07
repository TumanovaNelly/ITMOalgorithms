import sys
sys.path.append('../src')
from Main import main

from timeit import timeit
print(f"Excecution time = {timeit(main, number=1)} seconds (1 run)")

