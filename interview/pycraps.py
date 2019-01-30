#!/usr/bin/env python3

"""
PyCraps

In this exercise we will model a simplified game of craps as commonly played in casinos. The game involves 2 6-sixed dice and an object to track the game state.
At any given time the game state is in 1 of 2 states. Described as the "point" being on or off. If you know craps well, for this exercise we are ignoring all the negative bets such as
"DO NOT PASS". If you don't know what that means, just ignore it.

When the game begins, the point is off. When the point is off the following rules are in place:

dice result:
2, 3 or 12 -> "Craps" game resets, dice to move to next shooter, house takes all bets on table
7 or 11 -> winner, house doubles all bets
 -> set the point to the resulting number. No bets win or lose, same shooter rolls again Example: shooter rolls a 5, the point is now "on" and set to 5. Game is now hit this number again before hitting a 7.

When the point is "on", dice rules are as follows:
7 -> "craps", point is now off, house takes all money, dice move to next shooter
2, 3, or 12 -> "craps" but point remains on, no bets lose or win. Shooter rolls again.
4,5,6,8,9,10 -> if this number is the current point, the shooter wins his original bet, the point is now off and the game starts over. If this number is not the current point, no bets win or lose and the shooter rolls again.

***** REQUIRED *****
1. Model a die that when rolled produces a random number between 1 and 6 inclusively.

2. Model the craps game to keep track of 2 dice objects, the players at the table, which player is the current "shooter",the current point (if there is one), and the total bets on the table

3. Run the game by setting the first player as the shooter, and following the rules as above. Each time a new shooter starts or they win their point, every player should bet $100. When a player "craps out", the house (your game object) should collect the winnings from all players who bet. When a player hits their point and the game resets, their original bet should be returned to them as double.

4. Run the game with 1 player at the table starting with $1000. Run the game until he craps out when a point is set.

5. Run the game until either the player or the house runs out of money.

***** BONUS *****
1. Add multiple players to the table, where each time a player craps out the shooter is the next player in the list

2. Keep track of the highest and lowest balances of a player so at the end they have a number to brag about or cry about.

2. Add the concept of negative bets. So players at the start of a game (or when the point resets) randomly choose to either bet "with" or "against" the current shooter. When the point is off, betting against the shooter means you lose when the shooter makes a point or hits 7 or 11.

***** EXAMPLES *****
1 player at table
game starts
player 1 becomes current shooter
player 1 bets $100
shooter rolls 11.
house pays shooter $200 for winning
game resets
game starts
player 1 becomes current shooter
player 1 bets $100
shooter rolls 2
house collects $100 bets (all bets on table)
game resets
game starts
player 1 becomes shooter
player 1 bets $100
shooter rolls 5
point is now 5
shooter rolls 8
shooter rolls 3
shooter rolls 5
house pays all betters double their bet
player 1 is still shooter, point is off
game starts...

----------------------------------------

# Implementation Notes

Plays a simplified game of craps based on the rules above. Dice, Rolls and players have their own classes. All players, including the house, can bet. The house never shoots (rolls dice).
Bets are mechanical. Each player bets $100 on each round. The game ends when the house or all players are busted.

The implementation uses python logging to trace the game similar to the transcript above (but not exactly).

All dollar amounts are represented as `int` representing USD.

itertools.cycle is a cute way to cycle the available shooters in order until the game is over. Once a shooter is busted, he remains in the cycle but is just skipped.

This implementation experiments with python3 properties which are used to annotate getter/setter functions. This provides some data encapsulation/protection not normally
provided by python. It's a useful pattern to master.

This implementation experiments with the python 3.7 `dataclass` annotation, used to simplify the implementation of the data class pattern. More at https://realpython.com/python-data-classes/. I like the concept,
jury's still out on the detail.

This implementation experiments with type annotations in function signatures. This is supposed to help IDEs, e.g. Pycharm, code complete better. This seems to be true, especially to disambiguate overloaded functions,
such as Bettor/Shooter win() and lose(). I haven't tested this systematically, however, and Pycharm always has a billion moving parts.

# Example Run
/home/mcarifio/.pyenv/versions/3.7.0/bin/python /home/mcarifio/src/mcarifio/interviewpy/interview/pycraps.py
DEBUG:__main__:logging starts at level DEBUG
INFO:craps:Let's play...
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 7
INFO:craps:Mike wins
INFO:craps:* house: 9200
INFO:craps:* Mike: 1200
INFO:craps:* Trey: 1200
INFO:craps:* Guido: 1200
INFO:craps:* heisenberg: 1200
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 11
INFO:craps:Trey wins
INFO:craps:* house: 8400
INFO:craps:* Mike: 1400
INFO:craps:* Trey: 1400
INFO:craps:* Guido: 1400
INFO:craps:* heisenberg: 1400
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 6
INFO:craps:Guido's point: 6
INFO:craps:Guido shoots: 4
INFO:craps:Guido shoots: 6
INFO:craps:Guido matches point 6
INFO:craps:Guido wins
INFO:craps:* house: 7600
INFO:craps:* Mike: 1600
INFO:craps:* Trey: 1600
INFO:craps:* Guido: 1600
INFO:craps:* heisenberg: 1600
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 6
INFO:craps:heisenberg's point: 6
INFO:craps:heisenberg shoots: 10
INFO:craps:heisenberg shoots: 7
INFO:craps:heisenberg craps, loses!
INFO:craps:house wins
INFO:craps:* house: 8000
INFO:craps:* Mike: 1500
INFO:craps:* Trey: 1500
INFO:craps:* Guido: 1500
INFO:craps:* heisenberg: 1500
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 7
INFO:craps:Mike wins
INFO:craps:* house: 7200
INFO:craps:* Mike: 1700
INFO:craps:* Trey: 1700
INFO:craps:* Guido: 1700
INFO:craps:* heisenberg: 1700
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 4
INFO:craps:Trey's point: 4
INFO:craps:Trey shoots: 8
INFO:craps:Trey shoots: 7
INFO:craps:Trey craps, loses!
INFO:craps:house wins
INFO:craps:* house: 7600
INFO:craps:* Mike: 1600
INFO:craps:* Trey: 1600
INFO:craps:* Guido: 1600
INFO:craps:* heisenberg: 1600
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 3
INFO:craps:house wins
INFO:craps:* house: 8000
INFO:craps:* Mike: 1500
INFO:craps:* Trey: 1500
INFO:craps:* Guido: 1500
INFO:craps:* heisenberg: 1500
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 3
INFO:craps:house wins
INFO:craps:* house: 8400
INFO:craps:* Mike: 1400
INFO:craps:* Trey: 1400
INFO:craps:* Guido: 1400
INFO:craps:* heisenberg: 1400
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 2
INFO:craps:house wins
INFO:craps:* house: 8800
INFO:craps:* Mike: 1300
INFO:craps:* Trey: 1300
INFO:craps:* Guido: 1300
INFO:craps:* heisenberg: 1300
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 6
INFO:craps:Trey's point: 6
INFO:craps:Trey shoots: 7
INFO:craps:Trey craps, loses!
INFO:craps:house wins
INFO:craps:* house: 9200
INFO:craps:* Mike: 1200
INFO:craps:* Trey: 1200
INFO:craps:* Guido: 1200
INFO:craps:* heisenberg: 1200
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 8
INFO:craps:Guido's point: 8
INFO:craps:Guido shoots: 5
INFO:craps:Guido shoots: 8
INFO:craps:Guido matches point 8
INFO:craps:Guido wins
INFO:craps:* house: 8400
INFO:craps:* Mike: 1400
INFO:craps:* Trey: 1400
INFO:craps:* Guido: 1400
INFO:craps:* heisenberg: 1400
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 10
INFO:craps:heisenberg's point: 10
INFO:craps:heisenberg shoots: 5
INFO:craps:heisenberg shoots: 6
INFO:craps:heisenberg shoots: 8
INFO:craps:heisenberg shoots: 3
INFO:craps:heisenberg shoots: 9
INFO:craps:heisenberg shoots: 2
INFO:craps:heisenberg shoots: 4
INFO:craps:heisenberg shoots: 7
INFO:craps:heisenberg craps, loses!
INFO:craps:house wins
INFO:craps:* house: 8800
INFO:craps:* Mike: 1300
INFO:craps:* Trey: 1300
INFO:craps:* Guido: 1300
INFO:craps:* heisenberg: 1300
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 5
INFO:craps:Mike's point: 5
INFO:craps:Mike shoots: 8
INFO:craps:Mike shoots: 9
INFO:craps:Mike shoots: 3
INFO:craps:Mike shoots: 9
INFO:craps:Mike shoots: 5
INFO:craps:Mike matches point 5
INFO:craps:Mike wins
INFO:craps:* house: 8000
INFO:craps:* Mike: 1500
INFO:craps:* Trey: 1500
INFO:craps:* Guido: 1500
INFO:craps:* heisenberg: 1500
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 5
INFO:craps:Trey's point: 5
INFO:craps:Trey shoots: 10
INFO:craps:Trey shoots: 6
INFO:craps:Trey shoots: 5
INFO:craps:Trey matches point 5
INFO:craps:Trey wins
INFO:craps:* house: 7200
INFO:craps:* Mike: 1700
INFO:craps:* Trey: 1700
INFO:craps:* Guido: 1700
INFO:craps:* heisenberg: 1700
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 6
INFO:craps:Guido's point: 6
INFO:craps:Guido shoots: 4
INFO:craps:Guido shoots: 5
INFO:craps:Guido shoots: 8
INFO:craps:Guido shoots: 7
INFO:craps:Guido craps, loses!
INFO:craps:house wins
INFO:craps:* house: 7600
INFO:craps:* Mike: 1600
INFO:craps:* Trey: 1600
INFO:craps:* Guido: 1600
INFO:craps:* heisenberg: 1600
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 7
INFO:craps:heisenberg wins
INFO:craps:* house: 6800
INFO:craps:* Mike: 1800
INFO:craps:* Trey: 1800
INFO:craps:* Guido: 1800
INFO:craps:* heisenberg: 1800
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 6
INFO:craps:Mike's point: 6
INFO:craps:Mike shoots: 2
INFO:craps:Mike shoots: 9
INFO:craps:Mike shoots: 5
INFO:craps:Mike shoots: 4
INFO:craps:Mike shoots: 4
INFO:craps:Mike shoots: 8
INFO:craps:Mike shoots: 10
INFO:craps:Mike shoots: 5
INFO:craps:Mike shoots: 6
INFO:craps:Mike matches point 6
INFO:craps:Mike wins
INFO:craps:* house: 6000
INFO:craps:* Mike: 2000
INFO:craps:* Trey: 2000
INFO:craps:* Guido: 2000
INFO:craps:* heisenberg: 2000
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 9
INFO:craps:Trey's point: 9
INFO:craps:Trey shoots: 5
INFO:craps:Trey shoots: 8
INFO:craps:Trey shoots: 10
INFO:craps:Trey shoots: 10
INFO:craps:Trey shoots: 5
INFO:craps:Trey shoots: 2
INFO:craps:Trey shoots: 5
INFO:craps:Trey shoots: 2
INFO:craps:Trey shoots: 4
INFO:craps:Trey shoots: 8
INFO:craps:Trey shoots: 11
INFO:craps:Trey shoots: 10
INFO:craps:Trey shoots: 5
INFO:craps:Trey shoots: 8
INFO:craps:Trey shoots: 3
INFO:craps:Trey shoots: 7
INFO:craps:Trey craps, loses!
INFO:craps:house wins
INFO:craps:* house: 6400
INFO:craps:* Mike: 1900
INFO:craps:* Trey: 1900
INFO:craps:* Guido: 1900
INFO:craps:* heisenberg: 1900
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 4
INFO:craps:Guido's point: 4
INFO:craps:Guido shoots: 10
INFO:craps:Guido shoots: 4
INFO:craps:Guido matches point 4
INFO:craps:Guido wins
INFO:craps:* house: 5600
INFO:craps:* Mike: 2100
INFO:craps:* Trey: 2100
INFO:craps:* Guido: 2100
INFO:craps:* heisenberg: 2100
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 10
INFO:craps:heisenberg's point: 10
INFO:craps:heisenberg shoots: 8
INFO:craps:heisenberg shoots: 12
INFO:craps:heisenberg shoots: 8
INFO:craps:heisenberg shoots: 7
INFO:craps:heisenberg craps, loses!
INFO:craps:house wins
INFO:craps:* house: 6000
INFO:craps:* Mike: 2000
INFO:craps:* Trey: 2000
INFO:craps:* Guido: 2000
INFO:craps:* heisenberg: 2000
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 5
INFO:craps:Mike's point: 5
INFO:craps:Mike shoots: 4
INFO:craps:Mike shoots: 7
INFO:craps:Mike craps, loses!
INFO:craps:house wins
INFO:craps:* house: 6400
INFO:craps:* Mike: 1900
INFO:craps:* Trey: 1900
INFO:craps:* Guido: 1900
INFO:craps:* heisenberg: 1900
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 6
INFO:craps:Trey's point: 6
INFO:craps:Trey shoots: 4
INFO:craps:Trey shoots: 8
INFO:craps:Trey shoots: 7
INFO:craps:Trey craps, loses!
INFO:craps:house wins
INFO:craps:* house: 6800
INFO:craps:* Mike: 1800
INFO:craps:* Trey: 1800
INFO:craps:* Guido: 1800
INFO:craps:* heisenberg: 1800
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 3
INFO:craps:house wins
INFO:craps:* house: 7200
INFO:craps:* Mike: 1700
INFO:craps:* Trey: 1700
INFO:craps:* Guido: 1700
INFO:craps:* heisenberg: 1700
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 10
INFO:craps:heisenberg's point: 10
INFO:craps:heisenberg shoots: 8
INFO:craps:heisenberg shoots: 10
INFO:craps:heisenberg matches point 10
INFO:craps:heisenberg wins
INFO:craps:* house: 6400
INFO:craps:* Mike: 1900
INFO:craps:* Trey: 1900
INFO:craps:* Guido: 1900
INFO:craps:* heisenberg: 1900
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 8
INFO:craps:Mike's point: 8
INFO:craps:Mike shoots: 7
INFO:craps:Mike craps, loses!
INFO:craps:house wins
INFO:craps:* house: 6800
INFO:craps:* Mike: 1800
INFO:craps:* Trey: 1800
INFO:craps:* Guido: 1800
INFO:craps:* heisenberg: 1800
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 7
INFO:craps:Trey wins
INFO:craps:* house: 6000
INFO:craps:* Mike: 2000
INFO:craps:* Trey: 2000
INFO:craps:* Guido: 2000
INFO:craps:* heisenberg: 2000
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 7
INFO:craps:Guido wins
INFO:craps:* house: 5200
INFO:craps:* Mike: 2200
INFO:craps:* Trey: 2200
INFO:craps:* Guido: 2200
INFO:craps:* heisenberg: 2200
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 6
INFO:craps:heisenberg's point: 6
INFO:craps:heisenberg shoots: 4
INFO:craps:heisenberg shoots: 4
INFO:craps:heisenberg shoots: 7
INFO:craps:heisenberg craps, loses!
INFO:craps:house wins
INFO:craps:* house: 5600
INFO:craps:* Mike: 2100
INFO:craps:* Trey: 2100
INFO:craps:* Guido: 2100
INFO:craps:* heisenberg: 2100
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 8
INFO:craps:Mike's point: 8
INFO:craps:Mike shoots: 6
INFO:craps:Mike shoots: 8
INFO:craps:Mike matches point 8
INFO:craps:Mike wins
INFO:craps:* house: 4800
INFO:craps:* Mike: 2300
INFO:craps:* Trey: 2300
INFO:craps:* Guido: 2300
INFO:craps:* heisenberg: 2300
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 4
INFO:craps:Trey's point: 4
INFO:craps:Trey shoots: 2
INFO:craps:Trey shoots: 11
INFO:craps:Trey shoots: 4
INFO:craps:Trey matches point 4
INFO:craps:Trey wins
INFO:craps:* house: 4000
INFO:craps:* Mike: 2500
INFO:craps:* Trey: 2500
INFO:craps:* Guido: 2500
INFO:craps:* heisenberg: 2500
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 11
INFO:craps:Guido wins
INFO:craps:* house: 3200
INFO:craps:* Mike: 2700
INFO:craps:* Trey: 2700
INFO:craps:* Guido: 2700
INFO:craps:* heisenberg: 2700
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 8
INFO:craps:heisenberg's point: 8
INFO:craps:heisenberg shoots: 5
INFO:craps:heisenberg shoots: 9
INFO:craps:heisenberg shoots: 8
INFO:craps:heisenberg matches point 8
INFO:craps:heisenberg wins
INFO:craps:* house: 2400
INFO:craps:* Mike: 2900
INFO:craps:* Trey: 2900
INFO:craps:* Guido: 2900
INFO:craps:* heisenberg: 2900
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 3
INFO:craps:house wins
INFO:craps:* house: 2800
INFO:craps:* Mike: 2800
INFO:craps:* Trey: 2800
INFO:craps:* Guido: 2800
INFO:craps:* heisenberg: 2800
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 6
INFO:craps:Trey's point: 6
INFO:craps:Trey shoots: 2
INFO:craps:Trey shoots: 9
INFO:craps:Trey shoots: 6
INFO:craps:Trey matches point 6
INFO:craps:Trey wins
INFO:craps:* house: 2000
INFO:craps:* Mike: 3000
INFO:craps:* Trey: 3000
INFO:craps:* Guido: 3000
INFO:craps:* heisenberg: 3000
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 7
INFO:craps:Guido wins
INFO:craps:* house: 1200
INFO:craps:* Mike: 3200
INFO:craps:* Trey: 3200
INFO:craps:* Guido: 3200
INFO:craps:* heisenberg: 3200
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 9
INFO:craps:heisenberg's point: 9
INFO:craps:heisenberg shoots: 7
INFO:craps:heisenberg craps, loses!
INFO:craps:house wins
INFO:craps:* house: 1600
INFO:craps:* Mike: 3100
INFO:craps:* Trey: 3100
INFO:craps:* Guido: 3100
INFO:craps:* heisenberg: 3100
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 10
INFO:craps:Mike's point: 10
INFO:craps:Mike shoots: 3
INFO:craps:Mike shoots: 7
INFO:craps:Mike craps, loses!
INFO:craps:house wins
INFO:craps:* house: 2000
INFO:craps:* Mike: 3000
INFO:craps:* Trey: 3000
INFO:craps:* Guido: 3000
INFO:craps:* heisenberg: 3000
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 7
INFO:craps:Trey wins
INFO:craps:* house: 1200
INFO:craps:* Mike: 3200
INFO:craps:* Trey: 3200
INFO:craps:* Guido: 3200
INFO:craps:* heisenberg: 3200
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 5
INFO:craps:Guido's point: 5
INFO:craps:Guido shoots: 10
INFO:craps:Guido shoots: 8
INFO:craps:Guido shoots: 6
INFO:craps:Guido shoots: 3
INFO:craps:Guido shoots: 9
INFO:craps:Guido shoots: 7
INFO:craps:Guido craps, loses!
INFO:craps:house wins
INFO:craps:* house: 1600
INFO:craps:* Mike: 3100
INFO:craps:* Trey: 3100
INFO:craps:* Guido: 3100
INFO:craps:* heisenberg: 3100
INFO:craps:** shooter: heisenberg
INFO:craps:heisenberg shoots: 10
INFO:craps:heisenberg's point: 10
INFO:craps:heisenberg shoots: 6
INFO:craps:heisenberg shoots: 7
INFO:craps:heisenberg craps, loses!
INFO:craps:house wins
INFO:craps:* house: 2000
INFO:craps:* Mike: 3000
INFO:craps:* Trey: 3000
INFO:craps:* Guido: 3000
INFO:craps:* heisenberg: 3000
INFO:craps:** shooter: Mike
INFO:craps:Mike shoots: 6
INFO:craps:Mike's point: 6
INFO:craps:Mike shoots: 6
INFO:craps:Mike matches point 6
INFO:craps:Mike wins
INFO:craps:* house: 1200
INFO:craps:* Mike: 3200
INFO:craps:* Trey: 3200
INFO:craps:* Guido: 3200
INFO:craps:* heisenberg: 3200
INFO:craps:** shooter: Trey
INFO:craps:Trey shoots: 11
INFO:craps:Trey wins
INFO:craps:* house: 400
INFO:craps:* Mike: 3400
INFO:craps:* Trey: 3400
INFO:craps:* Guido: 3400
INFO:craps:* heisenberg: 3400
INFO:craps:** shooter: Guido
INFO:craps:Guido shoots: 9
INFO:craps:Guido's point: 9
INFO:craps:Guido shoots: 9
INFO:craps:Guido matches point 9
INFO:craps:Guido wins
INFO:craps:* house: -400
INFO:craps:* Mike: 3600
INFO:craps:* Trey: 3600
INFO:craps:* Guido: 3600
INFO:craps:* heisenberg: 3600
INFO:craps:game over

Process finished with exit code 0


# TODO

* Add some statistics and then print them after the game is over.

* Implement `test/test_pycraps.py` that unit tests this implementation.


"""

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(f"logging starts at level {logging.getLevelName(logger.getEffectiveLevel())}")

# import sys
from enum import Enum, IntEnum, auto
import random
from dataclasses import dataclass, field  # new in python3.7, more https://realpython.com/python-data-classes/
from typing import List
from itertools import cycle  ## https://docs.python.org/3/library/itertools.html#itertools.cycle
import inspect
import fire  ## https://github.com/google/python-fire/blob/master/docs/guide.md
# import attrdict



class Dice:
    """
    Dice have potentially several discrete values which are considered all equally probable on a roll. In craps, the faces have (contiguous) integers between 1 and 6 inclusive.

    The faces of the die are represented explicitly (enumerated) so the Dice class could be used elsewhere like say in [Magic](https://en.wikipedia.org/wiki/Mage:_The_Awakening) or
    [Dungeons and Dragons](https://en.wikipedia.org/wiki/Dungeons_%26_Dragons).

    The implicit assumption is that all faces are equally probable on a roll. We could assign a probability distribution to the faces, but this would complicate the class. Dice are assumed
    after all to be equally probable devices.
    """

    def __init__(self, values=list(range(1, 7))):
        if len(values) == 0: raise Exception('No faces provided.')
        self.values = values

    def roll(self):
        return random.choice(self.values)  # choose a dice face at random, all outcomes equally probable


# TODO mike@carif.io: @dataclass? My intuition is no.
class Roll:
    """
    A Roll is the roll of multiple dice (instances), @see [Dice](#Dice). Note that the dice can be of different kinds potentially, e.g. a dice with 6 sides and dice with say 10 sides.
    The defaults (number of dice, sides) are for craps.

    A given roll is a tuple of faces. The cardinality of the tuple is the number of die (Dices) in the instance constructor `__init__`.
    Note that order of the tuple is the order of die from `__init__`. In many cases, e.g. craps, the order of appearance doesn't matter, but it could in other games.
    """

    def __init__(self, dice=None):
        self.dice = dice or [Dice(), Dice()]  ## `None` signals "use the defaults"

    def roll(self):
        """Return a tuple of die faces"""
        return tuple(d.roll() for d in self.dice)  ## note: len(result) == 2 always


class FixedRoll(Roll):
    """
    FixedRoll rolls a set of dice at most `max_rolls` times without an explicit reset. This addresses the problem of
    runaway loops below.
    """

    _max_rolls = 100
    _roll_counter = 0

    def __init__(self, max_rolls = 100, dice=None):
        super().__init__(dice)
        self._max_rolls = max_rolls
        self.reset()

    @property
    def max_rolls(self):
        return self._max_rolls

    def reset(self):
        self._roll_counter = 0

    def roll(self):
        if self._roll_counter > self.max_rolls:
            raise ValueError(f'too many rolls')
        self._roll_counter += 1
        return super().roll()

class SequenceRoll(Roll):
    """
    A sequence roll is basically a predefined sequence of rolls that are served up by the `roll()` function using
    the python generator pattern. The sequence is populated by the constructor `__init__`. This is useful for testing
    `win()` since the same sequence of rolls is always returned by the `roll()` function.
    """

    def __init__(self, seq: List[tuple]):
        assert len(seq) > 0  # Must be at least one roll
        cardinality = len(seq[0])  # cardinality or number of slots in the tuple.
        assert all(len(s) == cardinality for s in seq[1:])  # All the rolls in seq must have the same cardinality
        # super().__init__()  ## not needed currently
        self.seq = seq

    def roll(self):
        """
        Return the next roll from the pre-defined sequence of rolls. Use a generator to clarify the edge condition that
        you've run out of rolls.
        :return:
        """
        try:
            for s in self.seq:
                yield s
        except StopIteration as si:
            # You called roll after using up the sequence. return None
            return None

class SequenceGame:
    """
    The sequence of rolls by player for a game. This can be used to replay a game.
    """

    # TODO mike@carif.io: only python built-in types can hint?
    def __init__(self, players:List, seq:List[dict]):
        self.seq = seq

    def roll(self):
        """
        mike = Shooter('Mike')
        guido = Shooter('Guido')

        a_game = SequenceGame([mike, guido], [dict(shooter=m, rolls=[(1,5), (5,1)]),
                                              dict(shooter=g, rolls=[(6,1)]),
                                              dict(shooter=m, rolls=[(4,1), (4,1), (6, 1), (1, 6)]],
                                              dict(shooter=g, rolls=[(1, 1)])])
        :return:
        """
        try:
            for i in self.seq:
                for r in i['rolls']:
                    yield r
        except StopIteration as si:
            return None

@dataclass  ## https://docs.python.org/3/library/dataclasses.html
class Bettor:
    _name: str  ## Bettor's name, e.g. 'house' or 'Mike'

    @property
    def name(self):
        return self._name

    _current_balance: int  ## How much money the bettor has currently in USD

    @property
    def current_balance(self):
        return self._current_balance

    @current_balance.setter
    def current_balance(self, value):
        self._current_balance = value
        self.min = value
        self.max = value
        self._current_balance = value

    _min: int  ## min, the lowest balance this bettor has ever had, in USD. Starts as the current balance. It's a property.

    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        self._min = min(self._min, value)

    _max: int  ## max, the highest balance this bettor has ever had, in USD. Starts as the current balance. It's a property.

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = max(self._max, value)

    def __init__(self, name=None, balance: int = None):
        self._name = name
        if balance > 0:
            self._min = self._max = self._current_balance = balance
        else:
            raise Exception('Need a positive balance')

    def win(self, amount: int):
        """Bettor self won the bet amount. Positive amounts are with the shooter, negative are against the shooter."""
        self.current_balance += amount
        self.current_bet = 0
        return self  ## fluent

    def lose(self, amount: int):
        """Bettor self lost the bet amount. Positive amounts are with the shooter, negative are against the shooter."""
        self.win(-amount)
        return self  ## fluent


@dataclass
class Shooter(Bettor):
    """A shooter is a bettor who shoots the dice. The house doesn't shoot"""

    _current_bet: int = 0  ## The current bet is USD. 0 means "no bet". It's a property.

    @property
    def current_bet(self):
        return self._current_bet

    @current_bet.setter
    def current_bet(self, value):
        self._current_bet = value
        return self

    _past_throws: List[int] = field(default_factory=list)  ## history of throws

    @property
    def past_throws(self):
        return self._past_throws

    history = past_throws  ## better alias for past_throws

    def __init__(self, name=None, balance: int = None):
        super().__init__(name=name, balance=balance)

    # TODO mike@carif.io: should this be a setter on past_throws? Don't think so.
    def remember(self, dice):
        """
        Remember this throw.
        :param dice:
        :return:
        """
        self._past_throws.append(dice)
        return self

    def shoot(self, dice: Roll) -> tuple:
        """
        The shooter is given the dice which he rolls. Remember that role and then result it.
        :param dice:
        :return:
        """
        result = dice.roll()
        self.remember(result)
        return result

    def bet(self, amount: int = 100):
        """
        Bet an amount. Shooter must be able to cover the bet.
        :param amount:
        :return:
        """
        if amount <= self.current_balance:
            self.current_bet = amount
        else:
            raise Exception(f"Can't cover {amount} bet, balance: {current_balance}")
        return self

    def win_double(self):
        """House doubles bettor's bet."""
        self.win(amount=self.current_bet * 2)
        return self  ## fluent

    def lose(self):
        """Bettor self lost the bet amount. Positive amounts are with the shooter, negative are against the shooter."""
        super().lose(self.current_bet)
        return self  ## fluent


# Make the various game states explicit:
# * Round - did the current_shooter win the round?
# * DicePass - is it time to pass the dice?
# * BetPayout - what's the bet payout multiplier?

class Round(Enum):
    """
    The decision on a round: WIN, LOSE, DRAW (no decision)
    """
    WIN = auto()
    LOSE = auto()
    DRAW = auto()

class DicePass(Enum):
    """
    The explicit signal to pass the die to the next shooter.
    """
    NEXT = auto()
    STAY = auto()

class BetPayout(IntEnum):
    """How you win changes the payout schedule. Payout is the bet multiplier."""
    LOSE = -1
    NONE = 0
    WIN = 1
    DOUBLE = 2


def win(total:int, point = None)->(Round, DicePass, int, BetPayout):
    """
    `win()` implements the craps state machine based on the game rules and the current point value.
    You can implement other rules with different functions. The craps() function uses the result of win to decide
    when to pass the dice to the next shooter and how to pay bettors.

    dice result:
    2, 3 or 12 -> "Craps" game resets, dice to move to next shooter, house takes all bets on table
    7 or 11 -> winner, house doubles all bets
    -> set the point to the resulting number. No bets win or lose, same shooter rolls again Example: shooter rolls a 5, the point is now "on" and set to 5. Game is now hit this number again before hitting a 7.

   When the point is "on", dice rules are as follows:
   7 -> "craps", point is now off, house takes all money, dice move to next shooter
   2, 3, or 12 -> "craps" but point remains on, no bets lose or win. Shooter rolls again.
   4,5,6,8,9,10 -> if this number is the current point, the shooter wins his original bet, the point is now off and the game starts over. If this number is not the current point, no bets win or lose and the shooter rolls again.

    :param total: int, the current roll
    :param point: int|None, the point that needs to be matched.
    :return: a tuple of (Round, Pass, int, int)

    Example usage: round_decision, next_shooter, point, bet_multiplier = win(7)
                   assert round_decision == Decision.WIN
                   assert next_shooter == Decision.STAY
                   assert point == None
                   assert bet_multipler == 2

    """
    if point:
        if total == 7: return (Round.LOSE, DicePass.NEXT, None, BetPayout.LOSE)
        if total in set([2, 3, 12]): return (Round.DRAW, DicePass.STAY, point, BetPayout.NONE)
        if total == point: return (Round.WIN, DicePass.STAY, None, BetPayout.WIN)
        return (Round.DRAW, DicePass.STAY, point, BetPayout.NONE)
    else:
        if total in set([7, 11]): return (Round.WIN, DicePass.STAY, None, BetPayout.WIN)
        if total in set([2, 3, 12]): return (Round.LOSE, DicePass.NEXT, None, BetPayout.LOSE)
        return (Round.DRAW, DicePass.STAY, total, BetPayout.NONE)




def game(roll=FixedRoll(), house=None, shooters=None, starting_bet=100):
    """
    Play a game (of craps).

    :param roll: The (required) dice that run the game. All shooters roll the same dice. The dice is stateless, meaning one roll never effects the next.
    :param rules: The explicit rules of this game, TBS. Currently the rules are hardcoded in this function implementation.
    :param house: The (required) house, which takes the bets and pays the winners. The house never shoots.
    :param shooters: The (required) shooters, one or more. The shooters shoot in order round-robin until either the house is busted or all shooters are busted.
    :return: statistics:dict, a dictionary of interesting statistics

    Note that the shooters are "side-effected" by playing the game, in particular their balances change and their min and max balances are recorded.

    """
    if not house:
        raise Exception('No house')
    if not shooters:
        raise Exception('no shooters')

    statistics = dict()  ## generate some statics about the game. Gives you something to return

    # Hacky way to announce the game is over.
    def game_over(result):
        logger.info("game over")
        return result

    # Let's play! https://www.youtube.com/watch?v=j7uL3DryXkk
    logger.info("Let's play...")
    for current_shooter in cycle(shooters):  ## cycle through the shooters forever (see the breaks below)

        # The game can only continue if the house and some shooter can bet. Testing this on every iteration is a little
        #   hacky, but it allows for cycle() above.
        if house.current_balance <= 0: return game_over(statistics)
        if not any(s for s in shooters if s.current_balance > 0): return game_over(
            statistics)  ##  if all the shooters are busted, game over. not any == some.
        if current_shooter.current_balance <= 0: continue  ## current shooter can't shoot without money
        # Here: current_shooter has enough money to shoot

        logger.info(f"** current shooter: {current_shooter.name}")

        dice_pass = DicePass.STAY
        # while the current_shooter ...
        while dice_pass == DicePass.STAY:
            #  ... hasn't won or lost
            point = None  ## point is truthy.
            decision = Round.DRAW  ## no decision yet.
            winner = None  ## assign the winner when decision above is Round.WIN or Round.LOSE
            payout = BetPayout.NONE
            roll.reset()
            # Who can cover the starting bet?
            bettors = list(s for s in shooters if
                           s.current_balance >= starting_bet)  ## bettors are all shooters who can cover the starting_bet. At least the current shooter can.
            for b in bettors: b.current_bet = starting_bet  ## all bettors bet the starting bet


            while decision == Round.DRAW:

                # Initial roll
                r = roll.roll()
                # roll.roll() can return None for SequenceRolls. Means you ran out of rolls for replaying a game.
                if not isinstance(r, tuple):
                    raise ValueError(f"Expecting tuple, got {type(r)}")

                total = sum(r)
                logger.info(f'current shooter {current_shooter.name} shoots: {total}')

                decision, dice_pass, point, payout = win(total, point)
                logger.debug(f'decision: {decision}, pass: {dice_pass}, point: {point}, payout: {payout}')

            # End the round with payouts, moving money to/from the various bettors.
            winnings = sum(b.current_bet for b in bettors)
            if decision == Round.WIN:
                # Hose loses, all bettors win double.
                winner = current_shooter
                house.lose(payout * winnings)
                for b in bettors: b.win(payout * b.current_bet)
            else:
                # House wins, all bettors lose.
                winner = house
                for b in bettors: b.lose()
                house.win(winnings)

            logger.info(f"!! {winner.name} wins")
            # Balances at the end of the round.
            logger.info(f"* house: {house.current_balance}")
            for b in bettors:
                logger.info(f"* bettor {b.name}: {b.current_balance}")


def craps(level='INFO'):
    """
    Generate a game of craps and then play it.
    :param level: str, the logging level for the trace of the game.
    :return:
    """
    # Little hacky here.
    # Set the global logging level to the command line argument, e.g. --level=WARN
    # Reset it here because its the first user entry point for fire.Fire()
    global logger
    logger.setLevel(logging.getLevelName(level))

    # Create a child logger based on the function name and set that level also.
    me = inspect.stack()[0][3]  # name of this function
    logger = logging.getLogger(me)
    logger.setLevel(logging.getLevelName(level))

    # Play craps with a pair of six sided dice, explicit and external rules, a house starting with $10,000 USD and four players each starting with $1000 USD.
    the_house = Bettor(name='house', balance=10_000)
    the_shooters = [Shooter(name='Mike', balance=1_000),
                    Shooter(name='Trey', balance=1_000),
                    Shooter(name='Guido', balance=1_000),
                    Shooter(name='heisenberg', balance=1_000)]

    # Running the game will eventually return some statistics about the game which a caller might use
    game_statistics = game(roll=FixedRoll(),
                           house=the_house,
                           shooters=the_shooters)
    return game_statistics


if '__main__' == __name__:
    fire.Fire(craps())
