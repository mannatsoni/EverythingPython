# Analyse the current markets
# Execute a trade using that data   
# Fetch the latest data from the market

class TradingBot:
    def __init__(self,name,initial_cash):
        self.name = name
        self.initial_cash = initial_cash
        
# In an instance variable you can hold more than one value
# self is the trading bot instance

"""bot1 = TradingBot("AAPL", 10000)
bot2 = TradingBot("MSFT", 2100)

print(bot1.name)
print(bot1.initial_cash)
print(bot2.name)
print(bot2.initial_cash)"""

class AutoTradingBot:
    def __init__(self,threshold):
        # When you add __ to any attribute, it becomes hidden from the public use.
        self.__thrs = threshold
        self.__position = None
        self.__price_data = []
    
    # Fetching the market data
    def fetch_market_data(self):
        self.__price_data = [69140,69150,69160,69170,69180,69190]
        print("Market data has been fetched.")
        return self.__price_data
    
    # Finding the latest price
    def latest_price(self):
        if self.__price_data:
            return self.__price_data[-1]
        else:
            return None
        
    def evaluate_price(self):
        latest_price = self.latest_price()
        if latest_price < self.__thrs:
            return "Sell"
        elif latest_price > self.__thrs:
            return "Buy"
        else:
            return "Hold"

    def execute_trade(self,action):
        if self.evaluate_price() == 'Sell' and self.__position != "Short":
            self.__position = "Short"
            return f"Sell Trade has been executed and current position is {self.__position}."
        
        elif self.evaluate_price() == 'Buy' and self.__position != "Long":
            self.__position = "Long"
            return f"Buy Trade has been executed and current position is {self.__position}."

        elif self.evaluate_price() == 'Hold':
            self.__position = "Hold"
            return f"The trade is on hold and current position is {self.__position}."
        
    def run(self):
        pass
        
autoBot1 = AutoTradingBot(69180)
# print(autoBot1.price_data)
print(autoBot1.fetch_market_data(), "\n")
print(autoBot1.latest_price(), "\n")
print(autoBot1.evaluate_price(), "\n")
action = autoBot1.evaluate_price()
print(autoBot1.execute_trade(action), "\n")

# Creating a GUI
