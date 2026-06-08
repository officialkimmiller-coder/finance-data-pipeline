# finance-data-pipeline

📊 금융 수업 과제와 투자 스터디에서 매번 손으로 반복하던 **시장 데이터 정리 · 지표 계산 · 리포트 작성**을 자동화하는 Python CLI 도구입니다.

> ⚠️ 이 도구는 **학습 및 데이터 정리용**입니다. 매수/매도 추천이나 투자 조언을 제공하지 않습니다.

## 배경

금융을 전공하면서 과제와 스터디마다 종목 가격 데이터를 받아 수익률, 변동성, 이동평균을 손으로 계산하고 표로 정리하는 작업을 반복했습니다. 매번 같은 일을 하느라 정작 분석과 해석에 쓸 시간이 부족했습니다. 이 반복 작업을 자동화하기 위해 직접 만든 도구이며, 같은 불편을 겪는 다른 학생들도 쓸 수 있도록 오픈소스로 공개합니다.

## 주요 기능

- CSV / JSON 가격 데이터를 읽어들임
- 일간 수익률, 누적 수익률, 변동성(표준편차), 단순 이동평균(SMA) 계산
- 결과를 보기 좋은 Markdown 리포트로 저장
- 종목별로 설정만 바꿔 바로 재사용 가능

## 설치

```bash
git clone https://github.com/officialkimmiller-coder/finance-data-pipeline.git
cd finance-data-pipeline
pip install -e .
```

## 사용 방법

```bash
finance-pipeline examples/sample_prices.csv --window 5 --output report.md
```

- `--window`: 이동평균 기간 (기본 5)
- `--output`: 저장할 리포트 파일 경로

## 입력 데이터 형식

| date       | close |
|------------|-------|
| 2025-01-02 | 100.0 |
| 2025-01-03 | 101.5 |

## 라이선스

MIT License
