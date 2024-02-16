import numpy as np
from scipy.optimize import curve_fit

class CurveFit:
    def __init__(self, x, y, function_name):
        self.x = x
        self.y = y
        self.function_name = function_name
        self.function = FUNCTIONS[function_name]
    def _fit_curve(self):
        (self.a, self.b), self.pcov = curve_fit(self.function, self.x, self.y)
    def _make_predictions(self):
        self.prediction = self.function(self.x, self.a, self.b)
    def _make_residuals(self):
        self.residuals = self.y - self.prediction
    def _make_sum_of_squares(self):
        self.squares_residual = np.sum(self.residuals ** 2)
        self.squares_total = np.sum((self.y - np.mean(self.y)) ** 2)
    def _make_r_squared(self):
        self.r_squared = 1 - (self.squares_residual / self.squares_total)
    def _make_dictionary(self):
        self.dict = {
            'a': self.a, 
            'b': self.b, 
            'r_squared': self.r_squared
        }
    def main(self):
        self._fit_curve()
        self._make_predictions()
        self._make_residuals()
        self._make_sum_of_squares()
        self._make_r_squared()
        self._make_dictionary()

FUNCTIONS = {
    'log': lambda x, a, b: a * np.log(x) + b, 
    'inverse': lambda x, a, b: a * (1/x) + b, 
    'linear': lambda x, a, b: a * x + b, 
}