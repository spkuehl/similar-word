import pytest
from words import WordComparison


def test_all_words_unique():
    word_comp = WordComparison(starting_word='condiment')
    word_comp.user_submissions = {'joe': 'ketchup',
                                  'jane': 'mustard'}
    assert len(word_comp.get_unique_words()) == 2

def test_some_unique():
    word_comp = WordComparison(starting_word='condiment')
    word_comp.user_submissions = {'joe': 'ketchup',
                                  'ash': 'ketchup',
                                  'jane': 'mustard'}
    assert len(word_comp.get_unique_words()) == 1

def test_player_word_matches_starting_word_identical():
    word_comp = WordComparison(starting_word='condiment')
    word_comp.user_submissions = {'joe': 'condiment'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_player_word_identical():
    word_comp = WordComparison(starting_word='condiment')
    word_comp.user_submissions = {'joe': 'ketchup',
                                  'jane': 'ketchup'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_player_word_and_starting_word_identical():
    word_comp = WordComparison(starting_word='ketchup')
    word_comp.user_submissions = {'joe': 'ketchup',
                                  'jane': 'ketchup'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_starting_word_stemmed():
    word_comp = WordComparison(starting_word='wander')
    word_comp.user_submissions = {'joe': 'wanderer'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_player_word_stemmed():
    word_comp = WordComparison(starting_word='condiment')
    word_comp.user_submissions = {'joe': 'wander',
                                  'jane': 'wanderer'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_player_word_and_starting_word_stemmed():
    word_comp = WordComparison(starting_word='wander')
    word_comp.user_submissions = {'joe': 'wanderer',
                                  'jane': 'wandering'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_starting_word_plural():
    word_comp = WordComparison(starting_word='prince')
    word_comp.user_submissions = {'joe': 'princes'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_player_word_plural():
    word_comp = WordComparison(starting_word='condiment')
    word_comp.user_submissions = {'joe': 'prince',
                                  'jane': 'princes'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_starting_word_not_case_sensitive():
    word_comp = WordComparison(starting_word='prince')
    word_comp.user_submissions = {'joe': 'PRInce'}
    assert len(word_comp.get_unique_words()) == 0

def test_player_word_matches_player_word_not_case_sensitive():
    word_comp = WordComparison(starting_word='condiment')
    word_comp.user_submissions = {'joe': 'Prince',
                                  'jane': 'pRINce'}
    assert len(word_comp.get_unique_words()) == 0
