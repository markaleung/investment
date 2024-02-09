from classes import tables, config, annuity
import pandas as pd

class AllYears:
    def __init__(self, config_ = None):
        self.config = config_ if config_ else config.Config()
        self.tables = tables.Tables()
        self.dict = []
    def _run_start_year(self):
        self.total = 0
        self.total_cash = 0
        self.return_ = 1
        for index_current, row in enumerate(self.tables.mix[self.index_start:].itertuples()):
            self.index_current = index_current
            self.row = row
            self.total = (self.total + 1) * row.return_
            self.total_cash = (self.total_cash + 1) / row.inflation
            self.return_ *= row.return_
            self.dict.append({
                'start': self.year_start, 
                'year': self.index_current + 1, 
                'total': self.total, 
                'total_cash': self.total_cash, 
                'annuity': self.total * row.annuity, 
                'expected': self.total * row.expected, 
                'annualised': self.return_ ** (1/(self.index_current+1)) - 1, 
            })
    def _run_start_years(self):
        for index_start in self.tables.mix.index:
            self.index_start = index_start
            self.year_start = self.tables.mix.start[self.index_start]
            self._run_start_year()
    def _make_df(self):
        self.df = pd.DataFrame(self.dict)
    def main(self):
        self.tables.make_mix()
        self._run_start_years()
        self._make_df()