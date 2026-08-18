from freqtrade.strategy import IStrategy
import talib.abstract as ta

class VibeAlphaMonad(IStrategy):
    minimal_roi = {"0": 0.03, "30": 0.015, "60": 0.005}
    stoploss = -0.015
    timeframe = '1m'

    def populate_indicators(self, dataframe, metadata):
        dataframe['ema_fast'] = ta.EMA(dataframe, timeperiod=9)
        dataframe['ema_slow'] = ta.EMA(dataframe, timeperiod=21)
        return dataframe

    def populate_entry_trend(self, dataframe, metadata):
        dataframe.loc[(dataframe['ema_fast'] > dataframe['ema_slow']), 'enter_long'] = 1
        return dataframe

    def populate_exit_trend(self, dataframe, metadata):
        dataframe.loc[(dataframe['ema_fast'] < dataframe['ema_slow']), 'exit_long'] = 1
        return dataframe
