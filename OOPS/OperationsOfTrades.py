class Trades:
    def __init__(self,symbol,quantity,price):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        
    def __repr__(self):
        # Used in debugging
        return f"symbol = {self.symbol}, quantity = {self.quantity}, price = {self.price}."
    def __str__(self):
        return f"{self.quantity} of shares of {self.symbol} at {self.price}."

    def __add__(self, other):
        # adding two objects
        # need to have same symbols when adding
        if self.symbol == other.symbol:
            new_quantity = self.quantity + other.quantity
            average_price = (self.quantity*self.price + other.quantity*other.price)/new_quantity
            return f"The latest quantity is {new_quantity} with an average price of {average_price}"
        else:
            return "Can not add different types of currencies."
    
    def __sub__(self, other):
        # subtracting two objects
        # need to have same symbols when adding
        if self.symbol == other.symbol:
            new_quantity = self.quantity - other.quantity
            # average_price = (self.quantity*self.price + other.quantity*other.price)/new_quantity
            return f"The latest quantity is {new_quantity}."
        else:
            return '"Can not subtract different types of currencies.'  

# How my objects look like
trade1 = Trades("BTC",1.5,71000)
trade2 = Trades("BTC", 0.5, 51000)
trade3 = Trades("ETH", 0.4, 23494)

# Adding the Objects
print(trade1 + trade2)
print(trade1 + trade3)
print("\n")

# Subtracting the Objects
print(trade1 - trade2)
print(trade1 - trade3)
print("\n")

# Using magic methods for debugging
print("This is the use of repr magic method :", repr(trade1), sep="\n")
print("\n")
print("This is the use of str magic method :", str(trade1), sep="\n")