from classes import tables, config
import pandas as pd

class SingleMix:
    def __init__(self, config_ = None):
        self.config = config_ if config_ else config.Config()
        self.tables = tables.Tables()
        self.allocation = 0.5
    def make_mix(self):
        self.mix = pd.DataFrame({
            'Return': self.allocation * self.tables.stock.df.Return + (1-self.allocation) * self.tables.bond.df.Return, 
            'expected': self.allocation * self.tables.stock.df.expected + (1-self.allocation) * self.tables.bond.df.expected
        })

