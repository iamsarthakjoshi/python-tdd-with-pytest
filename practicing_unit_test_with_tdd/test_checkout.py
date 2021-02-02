import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice(item="iPhone", price=20)
    checkout.addItemPrice(item="iWatch", price=10)
    return checkout

# def test_canInstantiateOfCheckout():
#     checkout = Checkout()
#     assert isinstance(checkout, object)

'''
canAddItemPrice or canAddItem tests are not needed now, 
as they're both being done in the new canCalculateTotal test.
''' 
# def test_canAddItem(checkout):
#     checkout.addItem(item="iPhone")

# def test_canAddItemPrice(checkout):
#     checkout.addItemPrice(item="iPhone", price=20)

def test_canCalculateTotal(checkout):
    # checkout.addItemPrice(item="iPhone", price=20)
    checkout.addItem(item="iPhone")
    assert checkout.calculateTotal() == 21

def test_canAddItemsAndCalculateTotal(checkout):
    # checkout.addItemPrice(item="iPhone", price=20)
    # checkout.addItemPrice(item="iWatch", price=10)
    checkout.addItem(item="iPhone")
    checkout.addItem(item="iWatch")
    assert checkout.calculateTotal() == 32

def test_canAddDiscountRule(checkout):
    checkout.addDiscount(item="iPhone", noOfItems=3, price=5)

def test_canApplyDiscountRule(checkout):
    checkout.addDiscount(item="iPhone", noOfItems=3, price=5)
    checkout.addItem(item="iPhone")
    checkout.addItem(item="iPhone")
    checkout.addItem(item="iPhone")
    assert checkout.calculateTotal() == 5.0


def test_exceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("badItem")