import pytest

def test_IntAssert():
    assert 1 == 1

def test_StrAssert():
    assert "str" == "str"

def test_FloatAssert():
    assert "1.0" == "1.0"

def test_arrayAssert():
    assert [1,3,4] == [1,3,4]

def test_dictAssert():
    assert {"1":1} == {"1":1}

# Failing Test
def test_BadFloatCompare():
    assert (0.1 + 0.2) == 0.3

# Passing Test
from pytest import approx
def test_BadFloatCompare():
    assert (0.1 + 0.2) == approx(0.3)