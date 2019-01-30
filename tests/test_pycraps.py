import pytest
import testfixtures as tf
import interview.pycraps as p

"""
pytest --verbose tests/test_pycraps.py  ## run this test  

(master) mcarifio@shuttle:~/src/mcarifio/interviewpy/interview$p pytest --verbose tests/
=================================================================================================================================================================== test session starts ====================================================================================================================================================================
platform linux -- Python 3.7.0, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- /home/mcarifio/.pyenv/versions/3.7.0/bin/python
cachedir: .pytest_cache
rootdir: /home/mcarifio/src/mcarifio/interviewpy/interview, inifile:
collected 8 items                                                                                                                                                                                                                                                                                                                                          

tests/test_palindrome.py::test_runner PASSED                                                                                                                                                                                                                                                                                                         [ 12%]
tests/test_pycraps.py::test_runner PASSED                                                                                                                                                                                                                                                                                                            [ 25%]
tests/test_pycraps.py::test_default_dice PASSED                                                                                                                                                                                                                                                                                                      [ 37%]
tests/test_pycraps.py::test_null_dice PASSED                                                                                                                                                                                                                                                                                                         [ 50%]
tests/test_pycraps.py::test_dice_one_face PASSED                                                                                                                                                                                                                                                                                                     [ 62%]
tests/test_pycraps.py::test_roll_1_default_dice PASSED                                                                                                                                                                                                                                                                                               [ 75%]
tests/test_pycraps.py::test_roll_10_default_dice PASSED                                                                                                                                                                                                                                                                                              [ 87%]
tests/test_pycraps.py::test_statistical_distribution PASSED          
"""


def test_runner():
    """Always True, tests the invocation string above."""
    assert True


def runner():
    """Should be skipped, doesn't follow the naming convention."""
    assert True


def test_default_dice():
    """The default dice has 6 faces, 1..6"""
    d = p.Dice()
    tf.compare(d.values, range(1,7))

def test_null_dice():
    """A dice must have a least one face."""
    with pytest.raises(Exception) as e:
        d = p.Dice(values=[])

        assert isinstance(e, BaseException)
        assert len(e.message) > 0


def test_dice_one_face():
    """A dice with one face is ok."""
    d = p.Dice(values=[1])
    tf.compare(d.values, [1])


def test_roll_1_default_dice():
    d = p.Dice()
    for i in range(10):
        r = d.roll()
        assert 1 <= r <= 6

def test_roll_10_default_dice():
    """Create a ten dice roller"""
    ten = [p.Dice() for i in range(9)]
    roller = p.Roll(dice=ten)

    # Roll the roller ten times.
    for i in range(10):
        r = roller.roll()
        # Every dice is always represented in a roll.
        assert len(r) == len(ten)
        # Every slot in the roll is in the standard range.
        assert all( slot for slot in r if 1<= slot <= 6 )

def test_statistical_distribution():
    """Is the roller distributed randomly?"""
    assert True


# test the various game rules here
def test_win_no_point_7():
    decision, dice_pass, point, payout = p.win(7)
    assert decision == p.Round.WIN
    assert dice_pass == p.DicePass.STAY
    assert point == None
    assert payout == p.BetPayout.WIN

def test_win_no_point_11():
    decision, dice_pass, point, payout = p.win(11)
    assert decision == p.Round.WIN
    assert dice_pass == p.DicePass.STAY
    assert point == None
    assert payout == p.BetPayout.WIN

def test_win_point_5():
    decision, dice_pass, point, payout = p.win(5)
    assert decision == p.Round.DRAW
    assert dice_pass == p.DicePass.STAY
    assert point == 5
    assert payout == p.BetPayout.NONE

    decision, dice_pass, point, payout = p.win(5, point)
    assert decision == p.Round.WIN
    assert dice_pass == p.DicePass.STAY
    assert point == None
    assert payout == p.BetPayout.WIN

def test_win_point_5_with_SequenceRoll():
    """
    This pattern of testing lets you test the `win()` function with a sequence of rolls, either in a for loop or
    roll by roll. Technically, you don't need SequenceRoll but it makes the abstraction a little cleaner.
    :return:
    """
    seq = p.SequenceRoll([(4, 1), (1,4)])
    point = None
    for r in seq.roll():
        decision, dice_pass, point, payout = p.win(p, point)

    # At the end of the sequence
    assert decision == p.Round.WIN
    assert dice_pass == p.DicePass.STAY
    assert point == None
    assert payout == p.BetPayout.WIN


