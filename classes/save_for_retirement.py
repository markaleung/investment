from classes import tables, config, annuity
import pandas as pd

class Single:
    def __init__(self, mix, config_ = None):
        self.mix = mix.copy()
        self.annuity = annuity.Increment()
        self.config = config_ if config_ else config.Config()
        self.dict = []
    def _run_start_year(self):
        self.total = 0
        self.return_ = 1
        for year_current, row in enumerate(self.mix.loc[self.year_start:].itertuples()):
            self.year_current = year_current
            self.row = row
            self.total = (self.total + 1) * row.Return
            self.return_ *= row.Return
            self.dict.append({
                'start': self.year_start, 
                'year': self.year_current, 
                'total': self.total, 
                'annuity': self.total * row.annuity, 
                'annualised': self.return_  ** (1/(self.year_current+1)) - 1, 
            })
    def _run_start_years(self):
        self.years_length = len(self.mix)-self.config.years_save
        for year_start in self.mix.index[:self.years_length]:
            self.year_start = year_start
            self._run_start_year()
    def _make_df(self):
        self.df = pd.DataFrame(self.dict)
    def main(self):
        self._run_start_years()
        self._make_df()

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
    def main(self):
        self._run_singles()