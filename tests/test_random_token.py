import random

import tkns

# import pytest


def test_default():
    token = tkns.tokenRandom()
    assert type(token) == str
    assert len(token) == 32


def test_fix_size():
    size = random.randint(10, 30)
    token = tkns.tokenRandom(nBytes=size)
    assert type(token) == str
    assert len(token) == size * 2
