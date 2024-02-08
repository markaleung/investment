from classes import tables, config, annuity
import pandas as pd

class Single:
    def __init__(self, mix, config_ = None):
        self.mix = mix.copy()
        self.annuity = annuity.Increment()
        self.config = config_ if config_ else config.Config()
        self.years = []
    def _run_year_start(self):
        self.total = 0
        for year_current, row in enumerate(self.mix.loc[self.year_start:self.year_end].itertuples()):
            self.year_current = year_current
            self.row = row
            self.total = (self.total + 1) * row.Return
            if self.total * row.annuity > 1:
                self.years.append(self.year_current)
                break
    def _run_years_start(self):
        self.years_length = len(self.mix)-self.config.years_save
        for year_start in self.mix.index[:self.years_length]:
            self.year_start = year_start
            self.year_end = self.year_start + self.config.years_save
            self._run_year_start()
    def _assert_years(self):
        assert len(self.years) == self.years_length, f'{self.allocation} allocation, {self.years_length} years, {len(self.years)} outputs'
    def main(self):
        self._run_years_start()
        self._assert_years()

class Multi:
    def __init__(self, config_ = None):
        self.config = config_ if config_ else config.Config()
        self.tables = tables.Tables()
        self.singles = {}
    def _run_singles(self):
        for allocation in self.config.allocations:
            self.config.allocation = allocation
            self.tables.make_mix(allocation = allocation)
            self.singles[allocation] = Single(mix = self.tables.mix, config_ = self.config)
            self.singles[allocation].main()
    def _make_df(self):
        self.df = pd.DataFrame({allocation: self.singles[allocation].years for allocation in self.config.allocations})
        self.df.index = self.tables.stock.df.Start[:len(self.tables.stock.df)-self.config.years_save]
    def main(self):
        self._run_singles()
        self._make_df()