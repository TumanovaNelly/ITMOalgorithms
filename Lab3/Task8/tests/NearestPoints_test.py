from Utils.Time_Memory import time_data
from Lab3.Task8.src.main import main


def test_time():
    time = time_data(main)
    assert time < 2