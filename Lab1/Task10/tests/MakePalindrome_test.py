from Lab1.Task10.src.MakePalindrome import make_palindrome, make_palindrome_general
import pytest

def test_make_palindrome_even_count():
    assert make_palindrome("BABACC") == "ABCCBA"
    assert make_palindrome_general("babacc") == "abccba"

def test_make_palindrome_odd_count():
    assert make_palindrome("ACCAB") == "ACBCA"
    assert make_palindrome_general("1CC1B") == "1CBC1"

def test_make_palindrome_single_letter():
    assert make_palindrome("A") == "A"
    assert make_palindrome_general("A") == "A"

def test_make_palindrome_empty_string():
    assert make_palindrome("") == ""
    assert make_palindrome_general("") == ""

def test_make_palindrome_long_string():
    assert make_palindrome("QWERTYUIOPASDFGHJKLZXCVBNM") == "A"
    assert make_palindrome_general("QWERTYUIOPASDFGHJKLZXCVBNM") == "A"

def test_make_palindrome_invalid_symbol():
    with pytest.raises(ValueError):
        make_palindrome("A1B")

if __name__ == "__main__":
    pytest.main()