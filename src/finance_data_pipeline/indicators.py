"""기본 금융 지표 계산 모듈. (투자 조언 아님 — 순수 수치 계산용)"""


def daily_returns(prices):
    """일간 수익률 리스트 반환. 첫 항목은 None."""
    returns = [None]
    for i in range(1, len(prices)):
        prev, curr = prices[i - 1], prices[i]
        returns.append((curr - prev) / prev if prev else None)
    return returns


def cumulative_return(prices):
    """전체 기간 누적 수익률."""
    if len(prices) < 2 or prices[0] == 0:
        return None
    return (prices[-1] - prices[0]) / prices[0]


def volatility(prices):
    """일간 수익률의 표준편차(변동성)."""
    rets = [r for r in daily_returns(prices) if r is not None]
    if len(rets) < 2:
        return None
    mean = sum(rets) / len(rets)
    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
    return var ** 0.5


def simple_moving_average(prices, window):
    """단순 이동평균(SMA) 리스트. window 미만 구간은 None."""
    if window < 1:
        raise ValueError("window는 1 이상이어야 합니다.")
    sma = []
    for i in range(len(prices)):
        if i + 1 < window:
            sma.append(None)
        else:
            chunk = prices[i + 1 - window : i + 1]
            sma.append(sum(chunk) / window)
    return sma
