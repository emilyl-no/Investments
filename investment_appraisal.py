import numpy_financial as npf


## Time Value of Money


def present_value(future_value, rate, time):
    """ Calculates the value of a present amount of money at a future date """
    return future_value / (1 + rate) ** time



def future_value(present_value, rate, time):
    """ Calculates the value today of a future amount of money"""
    return present_value * (1 + rate) ** time


## Investment Appraisal Methods


def npv(rate, cashflows):
    """Calculates the Net Present Value."""
    total = 0
    for t, cf in enumerate(cashflows):
        total += cf / (1 + rate)**t
    return total  

def irr(cashflows):
    """Calculates the Internal Rate of Return."""
    return npf.irr(cashflows)

def payback_period(cashflows):
    """Calculates the exact time to recover initial investment."""
    cumulative = 0
    for i, cf in enumerate(cashflows):
        prev_cumulative = cumulative
        cumulative += cf
        if cumulative >= 0:
            # This calculates the fractional year (e.g., 2.5 years)
            if i == 0: return 0
            return i - 1 + (abs(prev_cumulative) / cf)
    return None

def discounted_payback(rate, cashflows):
    """Calculates payback period using discounted cash flows."""
    cumulative = 0
    for i, cf in enumerate(cashflows):
        discounted_cf = cf / (1 + rate) ** i
        prev_cumulative = cumulative
        cumulative += discounted_cf
        if cumulative >= 0:
            if i == 0: return 0
            return i - 1 + (abs(prev_cumulative) / discounted_cf)
    return None

def profitability_index(rate, cashflows):
    """Calculates ratio of PV of future cashflows absolute value of initial investment"""
    initial = abs(cashflows[0])
    pv_future = sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows[1:], 1))
    return pv_future / initial

def arr(average_profit, initial_investment, scrap_value=0):
    """Calculates ratio of average annual accounting profit and average investment. """
    average_investment = (initial_investment + scrap_value) / 2
    return average_profit / average_investment

def eac(rate, n, npv, maintenance):
    """Calculates the constant annual cost of owning and operating an asset over its enire lifetimes"""
    annuity_factor = (1 - (1 + rate)**(-n)) / rate
    return (npv / annuity_factor) + maintenance

## Cashflow Models


def annuity_pv(payment, rate, periods):
    """ The current value of a future payments from an annuity, given a specific rate of return, or discount rate. """

    if rate == 0: return payment * periods
    return payment * (1 - (1 + rate) ** -periods) / rate

def perpetuity(payment, rate):
    """ Holder receives first payment in a full year. """
    if rate <= 0: raise ValueError("Rate must be greater than zero")
    return payment / rate


def growing_perpetuity(payment, rate, growth):
    """ Holder  receives first payment in a full year, and payment grows at a constant rate g. """
    if growth >= rate:
        raise ValueError("Growth must be less than discount rate")
    return payment / (rate - growth)


