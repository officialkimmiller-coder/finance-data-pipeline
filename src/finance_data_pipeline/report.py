"""계산 결과를 Markdown 리포트로 변환."""

from . import indicators


def build_report(rows, window):
    """rows: [(date, close), ...] → Markdown 문자열 반환."""
    dates = [d for d, _ in rows]
    prices = [c for _, c in rows]

    rets = indicators.daily_returns(prices)
    sma = indicators.simple_moving_average(prices, window)
    cum = indicators.cumulative_return(prices)
    vol = indicators.volatility(prices)

    lines = []
    lines.append("# 가격 데이터 분석 리포트\n")
    lines.append(f"- 데이터 포인트: **{len(prices)}개**")
    lines.append(f"- 기간: **{dates[0]} ~ {dates[-1]}**")
    lines.append(f"- 이동평균 기간(window): **{window}일**\n")

    lines.append("## 요약 지표\n")
    cum_txt = f"{cum * 100:.2f}%" if cum is not None else "N/A"
    vol_txt = f"{vol * 100:.2f}%" if vol is not None else "N/A"
    lines.append(f"- 누적 수익률: **{cum_txt}**")
    lines.append(f"- 일간 변동성(표준편차): **{vol_txt}**\n")

    lines.append("## 상세 데이터\n")
    lines.append("| date | close | daily_return | SMA |")
    lines.append("|------|-------|--------------|-----|")
    for i in range(len(prices)):
        r = f"{rets[i] * 100:.2f}%" if rets[i] is not None else "-"
        s = f"{sma[i]:.2f}" if sma[i] is not None else "-"
        lines.append(f"| {dates[i]} | {prices[i]:.2f} | {r} | {s} |")

    lines.append("\n---")
    lines.append("\n> 본 리포트는 학습용 데이터 정리 도구로 생성되었으며, 투자 조언이 아닙니다.")
    return "\n".join(lines)
