"""天気予報APIの単体テスト。"""

import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.main import app


def test_get_weather_returns_sunny() -> None:
    """`/weather` が固定値の天気予報を返すことを確認する。"""
    client = TestClient(app)

    response = client.get("/weather")

    assert response.status_code == 200
    assert response.json() == "晴れ"
