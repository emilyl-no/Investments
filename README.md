# Investment appraisal
Investment appraisal techniques are used to evaluate whether a project or investment is financially worthwhile.

## Tutorial 
In this tutorial we will see how to use 'invesment_appraisal' to analyse potential investment projects.

In order to use any of the functions, you first need to write:
``` python 
import invesment_appraisal
from invesment_appraisal import function
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

### How to compute the future value 
Given a present value $PV$, interest rate $r$, and time period $n$:

``` python
import invesment_appraisal
from invesment_appraisal import future_value

print("Future value:", future_value(PV,r,n))
```
To obtain the future value, we can write:

``` python
import invesment_appraisal
from invesment_appraisal import future_value

print("Future value:", future_value(...,..))
``` 

This gives:


### How to compute annuity present value

An annuity is a series of equal payments over time.
Given payment $C$,interest rate $r$, and a number of periods $n$:

``` python
import invesment_appraisal
from invesment_appraisal import annuity_present_value

print("Annuity present value:",annuity_present_value(C,r,n))
```
#### Example 
``` python
Suppose
. $C$=...
. $r$=..
. $n$=..
```
To calculate the annuity present value we can write:

``` python
import invesment_appraisal
from invesment_appraisal import annuity_present_value

print("Annuity present value, annuity_present_value(..,..,..))
```

### How to compute perpetuity
A perpetuity is a payment that continues forever. 
Given a payment $C$ and interest rate $r$:

``` python
import invesment_appraisal
from invesment_appraisal import perpetuity

print("Perpetuity value:", perpetuity(C,r))
```
#### Example 
``` python
print ("Perpetuity value:",perpetuity(..,..))
```

### How to compute growing perpetuity
A growing perpetuity assumes payments grow at rate $g$:

``` python
import invesment_appraisal
from invesment_appraisal import growing_perpetuity

print("Growing perpetuity:", growing_perpetuity(C,r,g))
```

#### Example 
``` python
print ("Growing perpetuity:",growing_perpetuity(..,..))
```

### How to compute Net Present Value (NPV)
NPV measures the value of an investment by discounting all future cash flows.

``` python
import investment_appraisal
from investment_appraisal import npv

print("NPV:", npv(cash_flows, r))
```
#### Example
``` python
cash_flows = 

print("NPV:", npv(cash_flows, ..))
```

### How to compute Internal Rate of Return (IRR)

IRR is the interest rate that makes the NPV equal to zero.
``` python
import investment_appraisal
from investment_appraisal import irr

print("IRR:", irr(cash_flows))
```
#### Example:
``` python
cash_flows =

print("IRR:", irr(cash_flows))
```

### How to compute Payback Period
The payback period measures how long it takes for an investment to recover its initial cost.
```python
import investment_appraisal
from investment_appraisal import payback_period

print("Payback period:", payback_period(initial_investment, cash_flows))
```
#### Example:
```python
cash_flows = 

print("Payback period:", payback_period(.., cash_flows))
```


### How to compute Discounted Payback Period
This is similar to payback period but accounts for the time value of money.

```python
import investment_appraisal
from investment_appraisal import discounted_payback_period

print("Discounted payback period:", discounted_payback_period(initial, cash_flows, r))
```
#### Example:

```python
cash_flows =

print("Discounted payback period:", discounted_payback_period(1000, cash_flows, 0.1))
```


### How to compute Profitability Index

The profitability index measures the value created per unit of investment.

```python
import investment_appraisal
from investment_appraisal import profitability_index

print("Profitability index:", profitability_index(cash_flows, r))
```
#### Example:
```python
cash_flows = 

print("Profitability index:", profitability_index(cash_flows, ..))
```

### How to compute Average Rate of Return (ARR)
ARR measures the profitability of an investment relative to its cost.

```python
import investment_appraisal
from investment_appraisal import arr

print("ARR:", arr(average_profit, initial_investment))
```

#### Example:
```python
print("ARR:", arr(200, 1000))
```

### How to compute Equivalent Annual Cost (EAC)
EAC converts the cost of an investment into an equivalent annual amount.

```python
import investment_appraisal
from investment_appraisal import eac

print("EAC:", eac(cost, annuity_factor, maintenance))
```

#### Example:
```python
print("EAC:", eac(500, 2.4869, 100))
```


## Explanation 
### Brief overview of investment appraisal

Let $n$ be the number of periods $(years)$ & $r$ be the interest rate per period.

### The present value 

This is the value of a present amount of money at a future date.

$$ \text{present value = future value / discount factor} $$
where the discount factor is $$(1 + r)^{-n}$$

### The future value 

This is the value today of a future amount of money.

$$\text{future value = present value / compounding factor} $$
where the compounding factor is $$(1 + r)^n$$

### The annuity present value

## Reference 
### List of functionality 
### Bibliography 


### Testing the software
To test the code:
To test the documentation:










## Time Value of Money ##

 ## Present Value ##
``` python
def present_value(future_value, rate, time):
   
    return future_value / (1 + rate) ** time
```
 ## Future Value ##
``` python
def future_value(present_value, rate, time):

    return present_value / (1 + rate) ** time
```
## Investment Appraisal Methods ##

 ## Net Present Value (NPV) ##
``` python
def npv(rate, cashflows):
    total = 0
    
    for t, cf in enumerate(cashflows):
        total += cf / (1 + rate) ** t
        return total
```
## Internal Rate of Return (IRR) ## 
``` python
import numpy as np

def irr(cashflows):
    return np.irr(cashflows)
```
## Payback Period ##
``` python
def payback_period(cashflows):
    cumulative = 0

    for year, cf in enumerate(cashflows):
        cumulative += cf
        if cumulative >=  0:
            return year
    return None       
```
## Discounted Payback Period ##
``` python
def discounted_payback(rate, cashflows):
    cumulative = 0
    
    for year, cf in enumerate(cashflows):
        discounted = cf / (1 + rate) ** year
        cumulative += discounted

        if cumulative >= 0:
            return year

    return None
```
## Profitability Index (PI) ##
``` python
def profitability_index(rate, cashflows):
    initial = abs(cashflows[0])

    pv_future = sum(
          cf / (1 + rate) ** t
          for t, cf in enumerate(cashflows[1:], 1)
    )

    return pv_future / initial
```
## Accounting Rate of Return (ARR) ##
``` python
def arr(average_profit, initial_investment, scrap_value=0):
    
    average_investment = (initial_investment + scrap_value) / 2
    return average_profit / average_investment
```
## Cashflow Models ##

## Annuity Present Value ##
``` python
def annuity_pv(payment, rate, periods):
    
    return payment * (1 - (1 + rate) ** -periods) / rate
```
## Perpetuity ##
``` python
def perpetuity(payment, rate):
    
    return payment / rate
```
## Growing Perpetuity ##
``` python
def growing_perpetuity(payment, rate, growth):
    if growth >= rate:
        
        raise ValueError("Growth must be less than discount rate")
    return payment / (rate - growth)
```
