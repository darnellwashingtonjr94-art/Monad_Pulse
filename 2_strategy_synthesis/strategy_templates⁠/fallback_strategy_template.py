from freqtrade.strategy import IStrategy

class FallbackSafeStrategy(IStrategy):
    minimal_roi = {"0": 0.01}
    stoploss = -0.005
    timeframe = '1m'
    
    def populate_indicators(self, dataframe, metadata):
        return dataframe

    def populate_entry_trend(self, dataframe, metadata):
        return dataframe

    def populate_exit_trend(self, dataframe, metadata):
        return dataframe
