"""Mutating functions."""

__author__ = "730563209"


def manual_append(name1: list[int], name2: int) -> None:
    """Adds an integer to the end of the list."""
    name1.append(name2) 


def double(word: list[int]) -> None:
    """Doubles the number of items in the list."""
    index: int = 0
    while index < len(word):
        word[index] *= 2
        index += 1