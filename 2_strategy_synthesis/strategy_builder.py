import json
from pathlib import Path

def generate_freqtrade_class_from_alpha(alpha_json_path: str, output_py_path: str):
    data = json.loads(Path(alpha_json_path).read_text())
    code_body = f\"\"\"
from freqtrade.strategy import IStrategy
import talib.abstract as ta

class {data.get('class_name', 'VibeDynamicStrategy')}(IStrategy):
    minimal_roi = {{"0": 0.05}}
    stoploss = -0.02
    timeframe = '5m'
    
    def populate_indicators(self, dataframe, metadata):
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        return dataframe
        
    def populate_entry_trend(self, dataframe, metadata):
        dataframe.loc[(dataframe['rsi'] < 30), 'enter_long'] = 1
        return dataframe
        
    def populate_exit_trend(self, dataframe, metadata):
        dataframe.loc[(dataframe['rsi'] > 70), 'exit_long'] = 1
        return dataframe
\"\"\"
    Path(output_py_path).write_text(code_body.strip())
