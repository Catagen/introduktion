import pytest
from exercises.introduction import Introduction

i = Introduction()

def test_area():
    assert i.area(20, 20) == 40
    assert i.area(23.5, 24.0) == 564

def test_to_seconds():
    assert i.to_seconds(5) == 18000
    assert i.to_seconds(1.8) == 6480

def test_is_of_age():
    assert i.is_of_age(12) == False
    assert i.is_of_age(20) == True
    assert i.is_of_age(17.5) == False

def test_vowel():
    assert i.vowel('a') == True
    assert i.vowel('Y') == True
    assert i.vowel('b') == False
    assert i.vowel('C') == False

def test_reverse():
    assert i.reverse('Test string') == 'gnirts tseT'
    assert i.reverse('Hello') == 'olleH'
    assert i.reverse('a') == 'a'

def test_overlapping():
    assert i.overlapping([1,2,3], [3,4,5]) == True
    assert i.overlapping([1.23, 'test', 5], [1.24, 'test1', 'test']) == True
    assert i.overlapping(['a', 6, 'c'], ['e', 'f', 'g']) == False

def test_travel_price():
    assert i.travel_price(20, 0.6, 12) == 14.4
    assert i.travel_price(105.5, 0.8, 14) == 118.16

def test_palindrome():
    assert i.palindrome('ni talar bra latin') == True
    assert i.palindrome('A car a man a maraca') == True
    assert i.palindrome('hello there') == False

def test_character_frequency():
    assert i.character_frequency('hej janne') == {'h' : 1, 'e' : 2, 'j' : 2, 'a' : 1, 'n' : 2}
    assert i.character_frequency('bananer') == {'b' : 1, 'a' : 2, 'n' : 2, 'e' : 1, 'r' : 1}
