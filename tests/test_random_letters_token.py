import random

import tkns

# import pytest

# import string


def test_default():
    token = tkns.randomLetters()
    assert type(token) == str
    assert len(token) == 8


def test_fix_size():
    size = random.randint(10, 30)
    token = tkns.randomLetters(length=size)
    assert type(token) == str
    assert len(token) == size


def test_puntuation():
    token = tkns.randomLetters(punctuation=True)
    assert type(token) == str
    assert len(token) == 8
    # assert token.find(string.punctuation) != -1
