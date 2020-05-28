import pytest
from words import WordComparison


def test_all_words_unique():
    word_comp = WordComparison(prompt='condiment')
    word_comp.user_submissions = {'joe': 'ketchup',
                                  'jane': 'mustard'}
    assert len(word_comp.get_unique_words_by_stemming()) == 2

def test_some_unique():
    word_comp = WordComparison(prompt='condiment')
    word_comp.user_submissions = {'joe': 'ketchup',
                                  'ash': 'ketchup',
                                  'jane': 'mustard'}
    assert len(word_comp.get_unique_words_by_stemming()) == 1

def test_player_word_matches_prompt_identical():
    word_comp = WordComparison(prompt='condiment')
    word_comp.user_submissions = {'joe': 'condiment'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_player_word_identical():
    word_comp = WordComparison(prompt='condiment')
    word_comp.user_submissions = {'joe': 'ketchup',
                                  'jane': 'ketchup'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_player_word_and_prompt_identical():
    word_comp = WordComparison(prompt='ketchup')
    word_comp.user_submissions = {'joe': 'ketchup',
                                  'jane': 'ketchup'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_prompt_stemmed():
    word_comp = WordComparison(prompt='wander')
    word_comp.user_submissions = {'joe': 'wanderer'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_player_word_stemmed():
    word_comp = WordComparison(prompt='condiment')
    word_comp.user_submissions = {'joe': 'wander',
                                  'jane': 'wanderer'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_player_word_and_prompt_stemmed():
    word_comp = WordComparison(prompt='wander')
    word_comp.user_submissions = {'joe': 'wanderer',
                                  'jane': 'wandering'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_prompt_plural():
    word_comp = WordComparison(prompt='prince')
    word_comp.user_submissions = {'joe': 'princes'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_player_word_plural():
    word_comp = WordComparison(prompt='condiment')
    word_comp.user_submissions = {'joe': 'prince',
                                  'jane': 'princes'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_prompt_not_case_sensitive():
    word_comp = WordComparison(prompt='prince')
    word_comp.user_submissions = {'joe': 'PRInce'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0

def test_player_word_matches_player_word_not_case_sensitive():
    word_comp = WordComparison(prompt='condiment')
    word_comp.user_submissions = {'joe': 'Prince',
                                  'jane': 'pRINce'}
    assert len(word_comp.get_unique_words_by_stemming()) == 0
