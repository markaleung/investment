class Config:
    def __init__(self):
        self._tables()
        self._save_for_retirement()
    def _tables(self):
        self.filename = 'Cape Expected Return.xlsx'
    def _save_for_retirement(self):
        self.years_save = 35
        self.allocations = [0.5, 1]