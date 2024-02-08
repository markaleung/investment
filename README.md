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
