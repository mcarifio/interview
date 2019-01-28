import interview.palindrome as p


def test_runner():
    assert True


def test_cleaner():
    assert p.is_palindrome(" %%%%%\t 121!! ")


def test_not_palindrome():
    assert not p.is_palindrome("1234")


def test_clean_up():
    assert p.clean(' &&&%%') == ''
