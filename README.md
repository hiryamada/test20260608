# 天気予報API（FastAPI）

FastAPI を使用したシンプルな天気予報 API です。  
現時点では引数なしで固定値の「晴れ」を返します。

## 実装内容

- `GET /weather` で文字列 `"晴れ"` を返却
- `pytest` による単体テストを `tests/` 配下に配置

## セットアップ

```bash
pip install -r requirements.txt
```

## 起動方法

```bash
uvicorn src.main:app --reload
```

## テスト実行

```bash
pytest -q
```