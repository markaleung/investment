from classes import tables, config, curve_fit
import pandas as pd

class AllYears:
    def __init__(self, config_ = None):
        self.config = config_ if config_ else config.Config()
        self.tables = tables.Tables(config_ = self.config)
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
                'ratio': self.total / self.total_cash, 
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

class _Yield(AllYears):
    def _set_subclass_variables(self):
        pass
    def _join_yield(self):
        self.df = pd.merge(self.df, self.df_asset[['Start', 'Yield']], left_on = 'start', right_on = 'Start').drop('Start', axis = 1)
    def _make_prediction(self):
        self.condition = self.df.year == self.year
        self.filtered = self.df[self.condition]
        self.curve_fit = curve_fit.CurveFit(x = self.filtered.Yield, y = self.filtered.annualised, function_name = self.function_name)
        self.curve_fit.main()
        # .loc is needed so that the prediction is added to self.join, not a copy
        self.df.loc[self.condition, 'prediction'] = self.curve_fit.prediction
        self.curve_fit.dict['year'] = self.year
        self.df_year.append(self.curve_fit.dict.copy())
    def _make_df_year(self):
        self.df_year = pd.DataFrame(self.df_year)
    def main(self):
        self.df_year = []
        self._set_subclass_variables()
        super().main()
        self._join_yield()
        for self.year in range(1, self.df.year.max()):
            self._make_prediction()
        self._make_df_year()
    def plot(self, year):
        self.ax1 = self.df.query('year == @year')[['Yield', 'annualised']].plot(kind = 'scatter', x = 'Yield', y = 'annualised')
        self.df.query('year == @year')[['Yield', 'prediction']].plot(kind = 'scatter', x = 'Yield', y = 'prediction', ax = self.ax1)

class Stock(_Yield):
    def _set_subclass_variables(self):
        self.config.allocation = 1
        self.df_asset = self.tables.stock.df
        self.function_name = 'linear'

class Bond(_Yield):
    def _set_subclass_variables(self):
        self.config.allocation = 0
        self.df_asset = self.tables.bond.df
        self.function_name = 'log'