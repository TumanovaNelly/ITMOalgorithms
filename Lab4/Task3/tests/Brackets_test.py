import unittest
from Lab4.Task3.src.Brackets import check_brackets, main
from utils import time_data, memory_data


class TestCheckBrackets(unittest.TestCase):

    def test_check_brackets_valid(self):
        self.assertTrue(check_brackets("()"))
        self.assertTrue(check_brackets("[]"))
        self.assertTrue(check_brackets("()[]"))
        self.assertTrue(check_brackets("[[](()[])]"))
        self.assertTrue(check_brackets("([()[]([][][])(([]([][])))])"))

    def test_check_brackets_invalid(self):
        self.assertFalse(check_brackets("("))
        self.assertFalse(check_brackets("["))
        self.assertFalse(check_brackets(")"))
        self.assertFalse(check_brackets("]"))
        self.assertFalse(check_brackets("(]"))
        self.assertFalse(check_brackets("[)"))
        self.assertFalse(check_brackets("([)]"))

    def test_check_brackets_empty(self):
        self.assertTrue(check_brackets(""))

    def test_time(self):
        assert time_data(main) < 2

    def test_memory_data(self):
        cur, peak = memory_data(main)
        assert cur < 5
        assert peak < 5


if __name__ == "__main__":
    unittest.main()
