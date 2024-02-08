from classes import tables, config
import pandas as pd

class Single:
    def __init__(self, allocation: float, tables, config_ = None):
        self.allocation = allocation
        self.tables = tables
        self.config = config_ if config_ else config.Config()
        self.years = []
    def _make_mix(self):
        self.mix = pd.DataFrame({
            'Return': self.allocation * self.tables.stock.df.Return + (1-self.allocation) * self.tables.bond.df.Return, 
            'expected': self.allocation * self.tables.stock.df.expected + (1-self.allocation) * self.tables.bond.df.expected
        })
        self.mix.index = self.tables.stock.df.Start
    def _run_year_start(self):
        self.total = 0
        for year_current, row in enumerate(self.mix.loc[self.year_start:self.year_end].itertuples()):
            self.year_current = year_current
            self.row = row
            self.total = (self.total + 1) * row.Return
            if self.total * row.expected > 1:
                self.years.append(self.year_current)
                break
    def _run_years_start(self):
        for year_start in self.mix.index[:len(self.mix)-self.config.years_save]:
            self.year_start = year_start
            self.year_end = self.year_start + self.config.years_save
            self._run_year_start()
    def main(self):
        self._make_mix()
        self._run_years_start()

class Multi:
    def __init__(self, config_ = None):
        self.config = config_ if config_ else config.Config()
        self.tables = tables.Tables()
    def _make_singles(self):
        self.singles = {allocation: Single(allocation = allocation, tables = self.tables, config_ = self.config) for allocation in self.config.allocations}
    def _run_singles(self):
        for allocation in self.config.allocations:
            self.config.allocation = allocation
            self.singles[allocation].main()
    def _make_df(self):
        self.df = pd.DataFrame({allocation: self.singles[allocation].years for allocation in self.config.allocations})
        self.df.index = self.tables.stock.df.Start[:len(self.tables.stock.df)-self.config.years_save]
    def main(self):
        self._make_singles()
        self._run_singles()
        self._make_df()