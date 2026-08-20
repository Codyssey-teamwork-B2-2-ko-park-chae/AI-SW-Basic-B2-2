"""date_ops 모듈의 테스트."""

from datetime import datetime

import src.date_ops as date_ops


def test_format_iso_date_with_datetime():
    dt = datetime(2024, 2, 29, 15, 30)

    assert date_ops.format_iso_date(dt) == "2024-02-29"


def test_format_iso_date_without_datetime(monkeypatch):
    class FixedDateTime(datetime):
        @classmethod
        def now(cls):
            return cls(2026, 8, 20, 15, 30)

    monkeypatch.setattr(date_ops, "datetime", FixedDateTime)

    assert date_ops.format_iso_date() == "2026-08-20"


def test_add_days_to_date():
    dt = datetime(2024, 2, 28, 10, 30)

    assert date_ops.add_days_to_date(dt, 1) == datetime(2024, 2, 29, 10, 30)


def test_add_days_to_date_with_negative_days():
    dt = datetime(2024, 3, 1, 10, 30)

    assert date_ops.add_days_to_date(dt, -1) == datetime(2024, 2, 29, 10, 30)
