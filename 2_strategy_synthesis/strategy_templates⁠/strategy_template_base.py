from freqtrade.strategy import IStrategy

class BaseVibeTemplate(IStrategy):
    minimal_roi = {"0": 0.02}
    stoploss = -0.01
    timeframe = '1m'
    
    def populate_indicators(self, dataframe, metadata):
        return dataframe
