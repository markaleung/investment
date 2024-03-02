# investment

This repository is my deep dive into investment and retirement spending. 

## resource_files/Cape Expected Returns.xlsx
This is the source input data. It consists of inflation data by year, stock yields/returns by year, and bond yields/returns by year. 

## How to Install the Repository
- Install Python (optional virtual environment)
- Install modules with `pip install -r requirements.txt`
- Install Google Sheets and Google Drive API

## How to Run the Repository
- Run `notebooks/Investment.ipynb`
- It runs 3 versions of the AllYears Class
    - Stock and Bond include curve fitting
    - Half (stocks and bonds) does not
- It writes data by year (all versions), and curve fit by year length (stock and bond) to google sheets

## Dashboard
The [Dashboard](https://lookerstudio.google.com/reporting/ec1f9e90-886d-4ba4-b296-8d0493d0dc4e) contains 6 graphs:
- Graphs 1, 2, and 3 combine the data by year for Stocks, Bonds, and Half
- Graphs 4, 5, and 6 use the curve fit by year length

# Trees

## Module Tree
- all_years: simulate investment for all start years
    - tables: mix stocks and bonds
        - table: excel data for stock, bond, inflation
        - annuity: use expected return to calculate annuity yield
    - curve_fit: fit yield to return (all stock/bond only)
## Class Tree
- AllYears
    - _Yield: fit yield to return, different allocation/table/curve function
    - Stock: linear function
    - Bond: log function
- _Annuity
    - Flat: payment doesn't go up
    - Increment: payment increases by 3% every year
- _Table: read excel sheet, add one
    - Inflation
    - _Asset: subtract inflation, different formula for expected return
        - Stock: linear formula
        - Bond: log formula
## Function Tree
- all_years.__init__
    - tables.__init__
        - table.__init__: stock, bond, inflation
            - table._set_subclass_variables
            - table._read_excel
            - table._add_one
        - tables._make_real
            - table._make_real: pass inflation to stock and bond
        - tables._get_expected
            - table._get_expected: stock and bond only
        - tables._add_one: return for stock and bond, inflation for inflation
- all_years._set_subclass_variables: stock and bond only
- tables.make_mix: combine stock and bond's return and expected return
    - pd.DataFrame
    - annuity.convert_to_annuity: convert expected return to annuity yield
- all_years._run_start_years
    for index_start in all_years.tables.mix.index: every start year from 1928 to 2020
        all_years._run_start_year: calculate investment from start year until 2020
- all_years._make_df
    - pd.DataFrame
- all_years._join_yield: join stock/bond's yield to table
    - pd.merge
- all_years._make_prediction: Use stock/bond yield to predict return for every year period
    - curve_fit._fit_curve
    - curve_fit._make_predictions
    - curve_fit._make_residuals
    - curve_fit._make_sum_of_squares
    - curve_fit._make_r_squared
    - curve_fit._make_dictionary
- all_years._make_df_year: coefficients and r squared for every year period
    - pd.DataFrame

