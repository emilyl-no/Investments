import investment_appraisal as ia


def test_present_value():
    """Test present value for a known case."""
    fv = 110
    rate = 0.10
    time = 1

    result = ia.present_value(fv, rate, time)
    expected = 110 / 1.1

    assert abs(result - expected) < 1e-9, "Present value is incorrect"


def test_future_value():
    """Test future value for a known case."""
    pv = 100
    rate = 0.10
    time = 2

    result = ia.future_value(pv, rate, time)
    expected = 100 * (1.1 ** 2)

    assert abs(result - expected) < 1e-9, "Future value is incorrect"


def test_npv():
    """Test NPV calculation."""
    rate = 0.10
    cashflows = [-100, 60, 60]

    result = ia.npv(rate, cashflows)

    expected = -100 + 60 / 1.1 + 60 / (1.1 ** 2)

    assert abs(result - expected) < 1e-9, "NPV is incorrect"


def test_irr():
    """Test IRR for a standard investment."""
    cashflows = [-100, 60, 60]

    result = ia.irr(cashflows)

    # Expected approx 10%
    assert abs(result - 0.10) < 1e-3, "IRR is incorrect"


def test_payback_period():
    """Test ordinary payback period."""
    cashflows = [-100, 50, 60]

    result = ia.payback_period(cashflows)

    assert result is not None, "Payback period should not be None"
    assert 1 < result < 2, "Payback period is incorrect"


def test_discounted_payback():
    """Test discounted payback period."""
    rate = 0.10
    cashflows = [-100, 60, 60]

    result = ia.discounted_payback(rate, cashflows)

    assert result is not None, "Discounted payback should not be None"
    assert result > 1, "Discounted payback is incorrect"


def test_profitability_index():
    """Test profitability index."""
    rate = 0.10
    cashflows = [-100, 60, 60]

    result = ia.profitability_index(rate, cashflows)

    pv_future = 60 / 1.1 + 60 / (1.1 ** 2)
    expected = pv_future / 100

    assert abs(result - expected) < 1e-9, "Profitability index is incorrect"


def test_arr():
    """Test accounting rate of return."""
    result = ia.arr(average_profit=20, initial_investment=100, scrap_value=0)

    expected = 20 / 50  # average investment

    assert abs(result - expected) < 1e-9, "ARR is incorrect"

def test_eac():
    """Test equivalent annual cost using annuity factor form."""
    rate = 0.05
    n = 5
    cost = 100000
    maintenance = 4000

    result = ia.eac(rate, n, cost, maintenance)

    # Manually calculated value
    
    annuity_factor = (1 - (1.05 ** -5)) / 0.05
    expected = (100000 / annuity_factor) + 4000

    assert abs(result - expected) < 1e-9, "EAC is incorrect"

def test_annuity_pv():
    """Test annuity present value"""
    result = ia.annuity_pv(payment=100, rate=0.10, periods=3)

    expected = 100 * (1 - (1.1 ** -3)) / 0.10

    assert abs(result - expected) < 1e-9, "Annuity PV is incorrect"


def test_perpetuity():
    """Test perpetuity formula."""
    result = ia.perpetuity(payment=100, rate=0.10)

    expected = 1000

    assert abs(result - expected) < 1e-9, "Perpetuity is incorrect"


def test_growing_perpetuity():
    """Test growing perpetuity formula."""
    result = ia.growing_perpetuity(payment=100, rate=0.10, growth=0.02)

    expected = 100 / (0.10 - 0.02)

    assert abs(result - expected) < 1e-9, "Growing perpetuity is incorrect"

