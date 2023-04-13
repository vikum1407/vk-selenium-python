import pytest


def test_total_divisble_by_5(input_data):
    assert  input_data % 5 == 0

def test_total_divisble_by_10(input_data):
    assert  input_data % 10 == 0

def test_total_divisble_by_9(input_data):
    assert  input_data % 9 == 0