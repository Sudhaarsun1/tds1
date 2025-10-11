import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Tests that the longest streak is returned when there are multiple streaks."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Tests that zeros and negative numbers break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6]) == 2

def test_all_positive():
    """Tests a list with only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    """Tests a list with only non-positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -3]) == 0

def test_single_element_positive():
    """Tests a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    """Tests a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_streaks_at_beginning_and_end():
    """Tests that streaks at the beginning and end of the list are handled correctly."""
    assert longest_positive_streak([1, 2, 3, -1, 4, 5]) == 3
    assert longest_positive_streak([1, 2, -1, 3, 4, 5]) == 3
