import investment_appraisal
import pytest


from investment_appraisal import present_value
from invesment_appraisal import future_value
from invesment_appraisal import annuity_present_value
from invesment_appraisal import perpetuity
from invesment_appraisal import growing_perpetuity
from invesment_appraisal import net_present_value
from invesment_appraisal import payback_period
from invesment_appraisal import discounted_payback_period
from invesment_appraisal import profitability_index
from invesment_appraisal import accounting_rate_of_return
from invesment_appraisal import equivalent_annual_cost

def test_present_value():
    """
    This function tests for the present value formula.
    """
    assert present_value(1100, 0.10, 1) == 1000.00
    assert present_value(1210, 0.10, 2) == 1000.00

def test_future_value():
    """
    This function tests for future value formula.
    """
    assert future_value(1000, 0.10, 1) == 1100
    assert future_value(1000, 0.10, 2) == 1210

def test_annuity_present_value():
    """
    This function tests for annuity present value formula.
    """
    assert annuity_present_value(100, 0.10, 3) == 248
    assert annuity_present_value(100, 0, 3) == 300

def test_perpetuity():
    assert perpetuity(100, 0.1) == 1000
