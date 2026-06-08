"""天気予報APIを提供するFastAPIアプリケーション。"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/weather")
def get_weather() -> str:
    """固定の天気予報を返す。"""
    return "晴れ"
