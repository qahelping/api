import csv
from pathlib import Path

import pytest
import requests
from furl import furl

BASE_URL = furl("https://httpbin.org")
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "files" / "httpbin_cases.csv"


def load_cases():
    cases = []
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["method"] = row["method"].strip().upper()
            row["path"] = row["path"].strip()
            row["accept"] = row["accept"].strip()
            row["expected_status"] = int(row["expected_status"])
            cases.append(row)
    return cases


@pytest.mark.parametrize("case", load_cases(), ids=lambda c: c["case_id"].strip())
def test_httpbin_ddt_from_csv(case):
    # url = BASE_URL + case["path"]
    # url = f"{BASE_URL}{case['path']}"
    if case.get('path'):
        url = BASE_URL.add(case.get('path'))
        print(url)
        headers = {"accept": case["accept"]}

        resp = requests.request(
            method=case["method"],
            url=url,
            headers=headers,
            timeout=10,
        )

        assert resp.status_code == case["expected_status"], (
            f"case_id={case['case_id']}\n"
            f"method={case['method']} url={url}\n"
            f"accept={case['accept']}\n"
            f"expected={case['expected_status']} got={resp.status_code}\n"
            f"body={resp.text[:300]}"
        )
