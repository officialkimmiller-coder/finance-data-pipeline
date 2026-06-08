"""데이터 로딩 모듈: CSV / JSON 가격 데이터를 읽어 표준 형식으로 변환."""

import csv
import json
from pathlib import Path


def load_prices(filepath):
    """
    파일에서 가격 데이터를 읽어 [(date, close), ...] 리스트로 반환.

    지원 형식: .csv (date, close 컬럼), .json (객체 리스트)
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"입력 파일을 찾을 수 없습니다: {filepath}")

    suffix = path.suffix.lower()
    if suffix == ".csv":
        return _load_csv(path)
    if suffix == ".json":
        return _load_json(path)
    raise ValueError(f"지원하지 않는 형식입니다: {suffix} (.csv 또는 .json 사용)")


def _load_csv(path):
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append((row["date"], float(row["close"])))
    return rows


def _load_json(path):
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    return [(item["date"], float(item["close"])) for item in data]
