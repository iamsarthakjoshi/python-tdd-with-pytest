class Checkout():
    class Discount:
        def __init__(self, noOfItems, price):
            self.noOfItems = noOfItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Item not found.")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            # check if item has discount offer in discount dict
            if item in self.discounts:
                discount = self.discounts[item]
                # count item to check if that count satisfies the discount's items count
                if count >= discount.noOfItems:
                    # no of discount to be applied
                    noOfDiscounts = count / discount.noOfItems
                    # add discount price in the total
                    total += noOfDiscounts * discount.price
                    # get the remaning items on which discount cannot applied
                    remaining = count % discount.noOfItems
                    # 
                    total += remaining * self.prices[item] 
            else:
                total += self.prices[item] + count
        return total
    
    def addDiscount(self, item, noOfItems, price):
        discount = self.Discount(noOfItems, price)
        self.discounts[item] = discount

    