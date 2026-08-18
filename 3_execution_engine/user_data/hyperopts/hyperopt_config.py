from freqtrade.optimize.hyperopt import IHyperopt

class VibeMonadHyperopt(IHyperopt):
    @staticmethod
    def indicator_populate_indicators(dataframe, metadata):
        return dataframe

    @staticmethod
    def populate_buy_trend(dataframe, metadata):
        return dataframe

    @staticmethod
    def populate_sell_trend(dataframe, metadata):
        return dataframe
