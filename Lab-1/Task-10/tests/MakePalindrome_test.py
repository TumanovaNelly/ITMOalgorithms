import sys
sys.path.append('../src')
from MakePalindrome import make_palindrome
import pytest

def test_make_palindrome_even_count():
    assert make_palindrome("BABACC") == "ABCCBA"

def test_make_palindrome_odd_count():
    assert make_palindrome("ACCAB") == "ACBCA"

def test_make_palindrome_single_letter():
    assert make_palindrome("A") == "A"

def test_make_palindrome_empty_string():
    assert make_palindrome("") == ""

def test_make_palindrome_long_string():
    assert make_palindrome("QWERTYUIOPASDFGHJKLZXCVBNM") == "A"

def test_make_palindrome_invalid_symbol():
    with pytest.raises(ValueError):
        make_palindrome("A1B")

if __name__ == "__main__":
    pytest.main()