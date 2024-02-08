from classes import tables, config, annuity
import pandas as pd

class AllYears:
    def __init__(self, config_ = None):
        self.config = config_ if config_ else config.Config()
        self.tables = tables.Tables()
        self.dict = []
    def _run_start_year(self):
        self.total = 0
        self.return_ = 1
        for year_current, row in enumerate(self.tables.mix.loc[self.year_start:].itertuples()):
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
        for year_start in self.tables.mix.index:
            self.year_start = year_start
            self._run_start_year()
    def _make_df(self):
        self.df = pd.DataFrame(self.dict)
    def main(self):
        self.tables.make_mix()
        self._run_start_years()
        self._make_df()