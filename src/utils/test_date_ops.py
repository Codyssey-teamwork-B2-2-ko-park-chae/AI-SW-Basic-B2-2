"""날짜 및 시간 처리 유틸리티 함수 모듈."""
from datetime import datetime, timedelta
from typing import Optional

def format_iso_date(dt: Optional[datetime] = None) -> str:
    """날짜를 ISO 포맷(YYYY-MM-DD)으로 변환합니다."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d")

def add_days_to_date(dt: datetime, days: int) -> datetime:
    """날짜에 일수를 더합니다."""
    return dt + timedelta(days=days)