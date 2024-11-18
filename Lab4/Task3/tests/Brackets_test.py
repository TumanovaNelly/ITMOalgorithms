import unittest
from Lab4.Task3.src.Brackets import check_brackets


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


if __name__ == "__main__":
    unittest.main()
