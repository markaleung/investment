class Config:
    def __init__(self):
        self._tables()
        self._all_years()
    def _tables(self):
        self.filename = 'Cape Expected Return.xlsx'
    def _all_years(self):
        self.allocation = 0.5