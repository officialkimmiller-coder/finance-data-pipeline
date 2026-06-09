"""indicators 모듈 단위 테스트. 실행: python -m pytest"""

from finance_data_pipeline import indicators


def test_daily_returns_first_is_none():
    prices = [100.0, 110.0]
    assert indicators.daily_returns(prices)[0] is None


def test_daily_returns_value():
    prices = [100.0, 110.0]
    assert abs(indicators.daily_returns(prices)[1] - 0.10) < 1e-9


def test_cumulative_return():
    prices = [100.0, 120.0]
    assert abs(indicators.cumulative_return(prices) - 0.20) < 1e-9


def test_volatility_constant_prices_is_zero():
    prices = [100.0, 100.0, 100.0]
    assert indicators.volatility(prices) == 0.0


def test_sma_window():
    prices = [1.0, 2.0, 3.0, 4.0]
    sma = indicators.simple_moving_average(prices, 2)
    assert sma[0] is None
    assert abs(sma[1] - 1.5) < 1e-9
    assert abs(sma[3] - 3.5) < 1e-9
