import pandas as pd

class TradingStrategy:
    def evaluate(self, current_day_index, full_data):
        if current_day_index < 2:
            return "HOLD"
        elif full_data.loc[current_day_index, "CLOSE"] <  full_data.loc[current_day_index - 1, "CLOSE"] < full_data.loc[current_day_index - 2, "CLOSE"]:
            return "BUY"
        elif full_data.loc[current_day_index, "CLOSE"] >  full_data.loc[current_day_index - 1, "CLOSE"] > full_data.loc[current_day_index - 2, "CLOSE"]:
            return "SELL"
        else:
            return "HOLD"