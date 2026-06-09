"""커맨드라인 진입점."""

import argparse

from .loader import load_prices
from .report import build_report


def main():
    parser = argparse.ArgumentParser(
        description="금융 가격 데이터를 정리하고 Markdown 리포트를 생성합니다."
    )
    parser.add_argument("input", help="입력 데이터 파일 (.csv 또는 .json)")
    parser.add_argument(
        "--window", type=int, default=5, help="이동평균 기간 (기본: 5)"
    )
    parser.add_argument(
        "--output", default="report.md", help="저장할 리포트 경로 (기본: report.md)"
    )
    args = parser.parse_args()

    rows = load_prices(args.input)
    if not rows:
        print("데이터가 비어 있습니다.")
        return

    report = build_report(rows, args.window)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✅ 리포트 생성 완료: {args.output} ({len(rows)}개 데이터)")


if __name__ == "__main__":
    main()
