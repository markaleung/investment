import pandas as pd, numpy as np

filename = '../resource_files/Cape Expected Return.xlsx'
def addOne(df, column):
    df[column] = df[column] + 1
def makeReal(df):
    df.Return = df.Return - inflation.Inflation

# Inflation
inflation = pd.read_excel(filename, sheet_name = 'Inflation')
inflation['Inflation2'] = inflation.Inflation
addOne(inflation, 'Inflation2')

# Stock
stock = pd.read_excel(filename, sheet_name = 'Stock')
addOne(stock, 'Return')
makeReal(stock)
stock['percentage'] = (1.1922/stock.Cape - 0.0139) * 0.7
# stock['percentage'] = (0.5/stock.Cape + 0.01) * 1

# Bond
bond = pd.read_excel(filename, sheet_name = 'Bond')
addOne(bond, 'Return')
makeReal(bond)
bond['percentage'] = (np.log(bond.Yield) * 0.0386 + 0.1354) * 0.8