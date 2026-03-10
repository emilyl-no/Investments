# Investment appraisal
Investment appraisal techniques are used to evaluate whether a project or investment is financially worthwhile.

## Tutorial 
In this tutorial we will see how to use 'investment_appraisal' to analyse potential investment projects.

In order to use any of the functions, you first need to write:
``` python 
import invesment_appraisal
from invesment_appraisal import 'function'
```
Where **'function'** is the relevant function you want to use. 
In the **How to guide**, it is shown how to use the different functions.


## How to guides

### How to compute the present value
Given a future value $FV$, interest rate $r$, and time period $n$, we can compute the present value using:

``` python
import investment_appraisal
from investment_appraisal import present_value

print("Present value:", present_value(FV, r, n))
```
Using .... example, we have:
$FV$ = ....
$r$=....
$n$=....

To obtain the present value for ..., we can write:

``` python
import invesment_appraisal
from invesment_appraisal import present_value

print ("Present value:", present_value(..,..))
```
This gives:



## Time Value of Money ##

 ## Present Value ##

def present_value(future_value, rate, time):
    
    return future_value / (1 + rate) ** time

 ## Future Value ##

def future_value(present_value, rate, time):
    
    return present_value * (1 + rate) ** time

## Investment Appraisal Methods ##

 ## Net Present Value (NPV) ##

def npv(rate, cashflows):
    total = 0
    
    for t, cf in enumerate(cashflows):
        total += cf / (1 + rate) ** t
        return total

## Internal Rate of Return (IRR) ## 

import numpy as np

def irr(cashflows):
    return np.irr(cashflows)

## Payback Period ##

def payback_period(cashflows):
    cumulative = 0

    for year, cf in enumerate(cashflows):
        cumulative += cf
        if cumulative >=  0:
            return year
    return None       

## Discounted Payback Period ##

def discounted_payback(rate, cashflows):
    cumulative = 0
    
    for year, cf in enumerate(cashflows):
        discounted = cf / (1 + rate) ** year
        cumulative += discounted

        if cumulative >= 0:
            return year

    return None

## Profitability Index (PI) ##

def profitability_index(rate, cashflows):
    initial = abs(cashflows[0])

    pv_future = sum(
          cf / (1 + rate) ** t
          for t, cf in enumerate(cashflows[1:], 1)
    )

    return pv_future / initial

## Accounting Rate of Return (ARR) ##

def arr(average_profit, initial_investment, scrap_value=0):
    
    average_investment = (initial_investment + scrap_value) / 2
    return average_profit / average_investment

## Cashflow Models ##

## Annuity Present Value ##

def annuity_pv(payment, rate, periods):
    
    return payment * (1 - (1 + rate) ** -periods) / rate

## Perpetuity ##

def perpetuity(payment, rate):
    
    return payment / rate

## Growing Perpetuity ##

def growing_perpetuity(payment, rate, growth):
    if growth >= rate:
        
        raise ValueError("Growth must be less than discount rate")
    return payment / (rate - growth)
