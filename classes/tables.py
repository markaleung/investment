import pandas as pd, numpy as np
from classes import config

class _Table:
    def __init__(self, config_ = None):
        self.config = config_ if config_ else config.Config()
        self._set_subclass_variables()
        self._read_excel()
        self._add_one()
    def _set_subclass_variables(self):
        pass
    def _read_excel(self):
        self.df = pd.read_excel(self.config.filename, sheet_name = self.sheet_name)
    def _add_one(self):
        self.df[self.column_one] = self.df[self.column_one] + 1

class Inflation(_Table):
    def _set_subclass_variables(self):
        self.sheet_name = 'Inflation'
        self.column_one = 'InflationOne'
    def _read_excel(self):
        super()._read_excel()
        self.df['InflationOne'] = self.df.Inflation

class _Asset(_Table):
    def __init__(self):
        self.column_one = 'Return'
        super().__init__()
    def _make_real(self, inflation):
        self.df.Return = self.df.Return - inflation
    def _get_expected(self):
        pass

class Stock(_Asset):
    def _set_subclass_variables(self):
        self.sheet_name = 'Stock'
    def _get_expected(self):    
        self.df['expected'] = (1.1922/self.df.Cape - 0.0139)

class Bond(_Asset):
    def _set_subclass_variables(self):
        self.sheet_name = 'Bond'
    def _get_expected(self):    
        self.df['expected'] = (np.log(self.df.Yield) * 0.0386 + 0.1354)

class Tables:
    def __init__(self):
        self.inflation = Inflation()
        self.stock = Stock()
        self.bond = Bond()
        self._make_real()
        self._get_expected()
    def _make_real(self):
        self.stock._make_real(self.inflation.df.Inflation)
        self.bond._make_real(self.inflation.df.Inflation)
    def _get_expected(self):
        self.stock._get_expected()
        self.bond._get_expected()