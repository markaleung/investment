# investment

This repository is my deep dive into investment and retirement spending. 

## Cape Expected Returns.xlsx
This is the source input data. It consists of inflation data by year, stock yields/returns by year, and bond yields/returns by year. 

## Saving For Retirement
- Calculate number of years needed to retire, starting from any year
    - Based on saving 1 unit per year
    - Retiring when total savings multiplied by expected return > 1 unit
- Save money for 20 years, starting from any year
    - Get total savings multiplied by expected return after 20 years
    - This represents 
- Recently, years needed to retire has gone up and spending amount after 20 years 

## Spending After Retirement
- Spend a percentage each year based on expected return
- Plot change in savings and spending amount over time
- Plot savings and spending on double axis graph
- Allows us to see how well spending holds up over time

## Valuation vs Expected Return
- Get annualised return for next n years, starting from any year
- Fit annualised return vs starting yield: return predicted values and r squared
- Print r squared for every value of n
- For n with highest r squared
    - Plot predicted annualised return and actual return vs yield
    - Plot predicted return, actual return, and difference 

# Function Tree
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
        - tables._add_one: return for stock and bond
- all_years._set_subclass_variables: stock and bond only
- tables.make_mix: return and expected combine stock and bond
    - pd.DataFrame
    - annuity.convert_to_annuity
- all_years._run_start_years
    for index_start in all_years.tables.mix.index: every start year from 1928 to 2020
        all_years._run_start_year: calculate investment from start year until 2020
- all_years._make_df
    - pd.DataFrame
- all_years._join_yield: stock and bond only
    - pd.merge
- all_years._make_prediction: stock and bond only
    - curve_fit._fit_curve
    - curve_fit._make_predictions
    - curve_fit._make_residuals
    - curve_fit._make_sum_of_squares
    - curve_fit._make_r_squared
    - curve_fit._make_dictionary
- all_years._make_df_year: stock and bond only
    - pd.DataFrame