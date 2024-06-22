class Trades:
    def __init__(self,symbol,quantity,price):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        
        print("I have been executed without any error.")
        

trade1 = Trades("BTC",10,100)