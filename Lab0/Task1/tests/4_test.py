from utils import time_data, memory_data
from Lab0.Task1.src.num4 import main

def test_time():
    assert time_data(main) < 2

def test_memory_data():
    cur, peak = memory_data(main)
    assert cur < 1
    assert peak < 1
