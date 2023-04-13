import pytest

@pytest.mark.login
def test_throttle_fa():
    assert 'viku' == 'viku'

@pytest.mark.login
def test_throttle_fg():
    assert 'godakawela' == 'godakawela'

def test_throttle_fc():
    assert 'anuradhapura' == 'anuradhapura'

def test_throttle_fd():
    assert 'tiku' == 'tiku'

def test_throttle_fe():
    assert 'town' == 'Town'

def test_throttle_ff():
    assert 'home' == 'viku'

@pytest.mark.login
def test_fb():
    assert 'piku' == 'piku'