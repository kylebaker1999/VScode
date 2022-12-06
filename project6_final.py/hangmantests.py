from hangman import start_game, semester_vocab, guess
from pytest import approx
import pytest
import random

def test_start_game():
    test_select = selected_word=random.choice(semester_vocab)
    assert test_select in semester_vocab


def test_guess():
    test = guess("TEST", True)
    # pass
    assert test == True
    
pytest.main(["-v", "--tb=line", "-rN", __file__])