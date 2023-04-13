import pytest

def test_m1():
    a=4
    b=6
    assert a+2 == b, "test passed"
    assert a == b,"test failed as a it's not eq to b"

def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"

def test_m3():
    assert True

def test_m4():
    assert False

def test_login():
    assert 'admin' == 'admin'