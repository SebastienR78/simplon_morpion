import pytest
import os
import sys


sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        ".."
                    )
                ))

from components.player import marq

def test_marq():
    place = (0,0)
    array = [[1,1,1],
             [1,1,1],
             [1,1,1]]
    player = 0
    assert marq(place, array, player)[0][0] != -1 