import pandas as pd

class MarketDataEngine:
    def __init__(self, file_path):
        self.path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.path)
        self.data["DATE"] = pd.to_datetime(self.data["DATE"])
        self.data = self.data.sort_values("DATE").reset_index(drop = True)

    def get_data_length(self):
        if self.data is not None:
            return len(self.data)
        return 0
    
    def get_market_info(self, day_index):
        if self.data is not None and 0 <= day_index < len(self.data):
            return self.data.loc[day_index, "CLOSE"]
        return None