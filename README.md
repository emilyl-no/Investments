# Investment appraisal
Investment appraisal techniques are used to evaluate whether a project or investment is financially worthwhile.
The investment_appraisal requires the installation of the NumPy Financial library for full functionality.

## Tutorial 
In this tutorial we will see how to use `investment_appraisal` to analyse potential investment projects.

In order to use any of the functions, you first need to write:
``` python 
import investment_appraisal
from investment_appraisal import function
```
Where **'function'** is the relevant function you want to use. 
In the **How to guide**, it is shown how to use the different functions.

#### We consider a project with:
- Initial investment: £100,000
- Cash inflows over 3 years: £70,000, £85,000, £65,000
- Discount rate: 12%

``` python
cashflows = [-100000, 70000, 85000, 65000]
rate = 0.12
```
#### Calculate Net Present Value (NPV)
``` python
npv_value = npv(rate, cashflows)
print(npv_value)
```
**This gives:** 76527.19569970842
##### If NPV > 0, the project adds value.

#### Calculate Internal Rate of Return (IRR)
``` python 
irr_value = irr(cashflows)
print(irr_value)
```
**This gives:** 0.5318704898373177
##### This gives the project's return. Compare this with the required rate (12%).

#### Calculate Profitability Index (PI)
``` python
pi_value = profitability_index(rate, cashflows)
print(pi_value)
```
**This gives:** 
##### PI > 1, Accept  
##### PI < 1, Reject

#### Calculate Payback Period 
``` python
pb = payback_period(cashflows)
dpb = discounted_payback(rate, cashflows)

print(pb)
print(dpb)
```
**This gives:** 1.3529411764705883,
1.5534117647058825

##### This shows how long it takes to recover the investment.

### For quick use of a library function you may also do this:
```python
import investment_appraisal as ia
ia.function(...)
```


## How to guides

### How to compute the present value
Given a future value $FV$, interest rate $r$, and time period $n$, we can compute the present value using:

``` python
import investment_appraisal
from investment_appraisal import present_value

print("Present value:", present_value(FV, r, n))
```
We have:
$FV$ = 1000
$r$ = 0.1
$n$ = 2

To obtain the present value, we can write:

``` python
import investment_appraisal
from investment_appraisal import present_value

print ("Present value:", present_value(1000,0.1,2))
```

Present value: 826.45

This means that £1000 received in 2 years is worth £826.45 today when discounted at 10%.

### How to compute the future value 
Given a present value $PV$, interest rate $r$, and time period $n$:

``` python
import investment_appraisal
from investment_appraisal import future_value

print("Future value:", future_value(PV, r, n))
```
To obtain the future value, we can write:

``` python
import investment_appraisal
from investment_appraisal import future_value

print("Future value:", future_value(1000,0.1,2))
``` 

Future value: 1210.0

This means that £1000 invested today will grow to £1210 in 2 years at an interest rate of 10%.

### How to compute annuity present value

An annuity is a series of equal payments over time.
Given payment $C$,interest rate $r$, and a number of periods $n$:

``` python
import investment_appraisal
from investment_appraisal import annuity_pv

print("Annuity present value:",annuity_pv(C, r, n))
```
#### Example 

To calculate the annuity present value we can write:

``` python
import investment_appraisal
from investment_appraisal import annuity_pv

print("Annuity present value", annuity_pv(1000,0.1,3))
```

Annunity present value: 2486.85

This means that receiving £1000 each year for 3 years is worth £2486.85 today when discounted at 10%.

### How to compute perpetuity
A perpetuity is a payment that continues forever. 
Given a payment $C$ and interest rate $r$:

``` python
import investment_appraisal
from investment_appraisal import perpetuity

print("Perpetuity value:", perpetuity(C, r))
```
#### Example 
``` python
print ("Perpetuity value:",perpetuity(1000,0.1))
```

Perpetuity value: 10000.0

This means that receiving £1000 every year forever is worth £10,000 today when discounted at 10%.

### How to compute growing perpetuity
A growing perpetuity assumes payments grow at rate $g$:

``` python
import investment_appraisal
from investment_appraisal import growing_perpetuity

print("Growing perpetuity:", growing_perpetuity(C, r, g))
```

#### Example 
``` python
print ("Growing perpetuity:",growing_perpetuity(1000,0.1,0.2))
```

Growing perpetuity: 12500.0

This means that a payment starting at £1000 and growing at 2% per year forever is worth £12,500 today when discounted at 10%.

### How to compute Net Present Value (NPV)
NPV measures the value of an investment by discounting all future cash flows.

``` python
import investment_appraisal
from investment_appraisal import npv

print("NPV:", npv(cashflows, r))
```
#### Example
``` python
cash_flows = [-100000, 70000, 85000, 65000]

print("NPV:", npv(0.12,cashflows))
```

NPV: 47033.0

Since the NPV is positive, this indicates that the investment is profitable and should be accepted.

### How to compute Internal Rate of Return (IRR)

IRR is the interest rate that makes the NPV equal to zero.
``` python
import investment_appraisal
from investment_appraisal import irr

print("IRR:", irr(cashflows))
```
#### Example:
``` python
cash_flows = [-100000, 70000, 85000, 65000]
print("IRR:", irr(cashflows, Period)
```
IRR: 0.53

### How to compute Paybackperiod.
The payback period measures how long it takes for an investment to recover
its initial cost.

```python
import investment_appraisal
from investment_appraisal import payback_period

print("Payback period:", payback_period(initial_investment, cashflows))
```
#### Example:
```python
cashflows = [-100000, 70000, 85000, 65000]

print("Payback period:", payback_period( cashflows))
```
Payback period:2 


### How to compute Discounted Payback Period
This is similar to payback period but accounts for the time value of money.

```python
import investment_appraisal
from investment_appraisal import discounted_payback

print("Discounted payback period:", discounted_payback(rate, cashflows))
```
#### Example:

```python
cashflows = [-100000, 70000, 85000, 65000]

print("Discounted payback period:", discounted_payback(0.12,cashflows))
```

Discounted payback period: 2

This means that when accounting for the time value of money, the investment is recovered in approximately 2 years.

### How to compute Profitability Index

The profitability index measures the value created per unit of investment.

```python
import investment_appraisal
from investment_appraisal import profitability_index

print("Profitability index:", profitability_index(C, cashflows))
```
#### Example:
```python
cash_flows = [-100000, 70000, 85000, 65000]

print("Profitability index:", profitability_index(0.12, cashflow))
```

Profitability index: 1.47

A profitability index greater than 1 indicates the investment creates value and should be accepted.

### How to compute Average Rate of Return (ARR)
ARR measures the profitability of an investment relative to its cost.

```python
import investment_appraisal
from investment_appraisal import arr

print("ARR:", arr(average_profit, initial_investment, scrap_value=0))
```

#### Example:
```python
print("ARR:", arr(20000, 100000))
```

ARR: 0.2

An ARR of 20% indicated the project generates 20% return on the initial investment per year.

### How to compute Equivalent Annual Cost (EAC)
EAC converts the cost of an investment into an equivalent annual amount.

```python
import investment_appraisal
from investment_appraisal import eac

print("EAC:", eac(rate, n, npv, maintenance))
```

#### Example:
```python
print("EAC:", eac(0.12,3,100000,5000))
```

EAC: 42600.0

This means that the investment has an equivalent annual cost of £42,600 per year over the 3 years when discounted at 12%. 

### Brief overview of investment appraisal

Let $n$ be the number of periods (years) and $r$ be the interest rate per period.

### The present value 

This is the value of a present amount of money at a future date.

$$\text{present value = future value / discount factor}$$
where the discount factor is $$(1 + r)^{-n}$$

### The future value 

This is the value today of a future amount of money.

$$\text{future value = present value / compounding factor}$$
where the compounding factor is $$(1 + r)^n$$

### The annuity present value

$$PV = C \times \frac{1 - (1+r)^{-n}}{r}$$

$$
\begin{aligned}
C &= \text{Cash flow each period} \\
r &= \text{Discount rate} \\
n &= \text{Number of periods}
\end{aligned}
$$

### Net Present Value 

This measures the difference between the $$PV$$ of all future cash inflows, $$PV_{in}$$ , and the investment outlay, $$I_{out}$$. $${NPV = PV_{in} - I_{out}}$$

**Investment Decision Rule using NPV**
- If the Net Present Value $$NPV > 0$$, ACCEPT THE PROJECT
- If the Net Present Value $$NPV < 0$$, REJECT THE PROJECT
- If the Net Present Value $$NPV = 0$$, INDIFFERENT BETWEEN ACCEPTING OR REJECTING

⇒ Positive $$NPV$$: $$PV$$ of future cash flows $$> PV$$ of investment, ACCEPT THE PROJECT

⇒ Negative $$NPV$$: $$PV$$ of future cash flows $$< PV$$ of investment, REJECT THE PROJECT

⇒ Zero $$NPV$$: $$PV$$ of future cash flows $$= PV$$ of investment, INDIFFERENT

⇒ Higher positive $$NPV$$ implies greater profitability

### Internal Rate of Return 

The $IRR$ is the discount (interest) rate that equates the present value of future cash inflows to the initial investment outlay. Equivalently, it is the rate at which the Net Present Value (NPV) of a project is zero.

$$0 = R_0 + \sum_{i=1}^{n} \frac{R_i}{(1+r)^i}$$

where $$R_0$$ is the initial investment (typically negative), and $$R_i$$ is the cash flow at the time $$i$$, and $$r$$ is the Internal Rate of Return.

**Investment Decision Rule using IRR**
- If the cost of capital $$k > r$$, REJECT THE PROJECT
- If the cost of capital $$k \leq r$$, ACCEPT THE PROJECT

### Payback Period 

The payback period is the time required to recover the original investment or reach the break-even point. 

**Investment Decision with Payback**
- If $$t \leq B$$ where $$t$$ is the points in time, ACCEPT THE PROJECT
- If $$t \geq B$$ where $$t$$ is the points in time, REJECT THE PROJECT

### Discounted Payback Period 

This technique considers discounted cash flows and the time value of money.

**Investment Decision with Discounted Payback** 
- If $$DPP \leq$$ target payback period, ACCEPT THE PROJECT
- If $$DPP >$$ target payback period, REJECT THE PROJECT

### Profitabililty Index

This measures the ratio between the $$PV$$ of future cash flows and the initial investement. The index ranks investment projects and quantifies the value per unit of investment.

$$PI = \frac{\text{PV of future cash flows}}{\text{Initial investment}} = \frac{NPV + \text{Initial investment}}{\text{Initial investment}}$$

**Investment Decision with PI**
- If $$PI >$$ 1: the investment is worthwhile, ACCEPT THE PROJECT
- If $$PI$$ <$$ 1: the investment is worthless, REJECT THE PROJECT
- If $$PI =$$ 1: the investment is breakeven, INDIFFERENT
- Higher positive $$PI$$ implies greater profitability

### Accounting Rate of Return 

The Accounting Rate of Return (ARR) is the average accounting profit from an investment divided by the average investment (or initial investment).

$$ARR = \frac{\text{Average annual accounting profit}}{\text{Average investment}}$$

**Investment Decision ARR**

- If $$ARR \geq$$ required rate of return, ACCEPT THE PROJECT
- If $$ARR$$ $$<$$ required rate of return, REJECT THE PROJECT

### Equivalent Annual Cost 

 Represents the constant annual cost of owning and operating an asset over its entire lifetime. It is used to compare the cost-effectiveness of mutually exclusive investments with unequal lifespans.

$$EAC = \frac{NPV}{A_{n,r}}$$

$$A_{n,r} = \frac{1 - (1+r)^{-n}}{r}$$

$$
\begin{aligned}
\end{aligned}
$$             
 


$$EAC = NPV \times \frac{r}{1 - (1+r)^{-n}}$$

$$\begin{aligned}
A_{n,r} &= \text{Annuity factor} \\
n &= \text{project lifetime in years} \\
r &= \text{annual discount rate}
\end{aligned}$$

### Perpetuities

A perpetuity is an annuity with payments start at a fixed date and continue forever.

**Ordinary Perpetuity**: The holder receives the first payment in a full year. The $$PV$$ is calculated as follows:

$$PV = \frac{R}{r}$$

**Growing Perpetuity**: The holder receives the first payment in a full year, and the payment grows at a constant rate $$g$$. The $$PV$$ is calculate as follows:

$$PV = \frac{R}{r - g}$$


## References 
### List of functionality 
Available functions of the `investment_appraisal` library.

`present_value`

`future_value`

`npv`

`irr`

`payback_period`

`discounted_payback`

`profitability_index`

`arr`

`eac`

`annuity_pv`

`perpetuity`

`growing_perpetuity`

### Bibliography 
[Springer Investment Appraisal Methods and Models](<Investment Appraisal Springer.html>) - used for examples
https://www.geeksforgeeks.org/python/abs-in-python/ - used for testing


### Testing the software
To test the code:

```
$ pytest test_investment_appraisal.py
```

To test the documentation:

```
$ python -m doctest README.md
```










    
