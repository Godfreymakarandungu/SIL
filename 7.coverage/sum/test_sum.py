import pytest
from sum import sum
def test_sum():
    assert sum(1, 2) == 3
def test_sum_output():
    assert type(sum(1,2)) is int   