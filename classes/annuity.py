class _Annuity:
    def convert_to_annuity(self, series):
        return self.a * series ** 2 + self.b * series + self.c

class Flat(_Annuity):
    def __init__(self):
        self.a = 1.3288703073580235
        self.b = 0.6285759039313298
        self.c = 0.04439456153619908

class Increment(_Annuity):
    def __init__(self):
        self.a = 1.6409114594271372
        self.b = 0.4804711069777034
        self.c = 0.028973782451661066