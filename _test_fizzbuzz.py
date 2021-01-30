import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)

def checkFizzBuzz(value, expectedRetVal):
    res = fizzBuzz(value)
    assert res == expectedRetVal

def isMultiple(value, mod):
    return value % mod == 0 

# def test_canCallFizzBuzz():
#     fizzBuzz(1)

def test_returns1WhenPassed1():
    checkFizzBuzz(1, "1")

def test_returns2WhenPassed2():
    checkFizzBuzz(2, "2")

def test_returnsFizzWhenPassed3():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWhenPassed5():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWhenPassed6():
    checkFizzBuzz(6, "Fizz")
    
def test_returnsBuzzWhenPassed10():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWhenPassed15():
    checkFizzBuzz(15, "FizzBuzz")