from pathlib import Path
from typing import Literal

from fastapi import Query
from fastapi.responses import FileResponse
from fastapi_offline import FastAPIOffline

app = FastAPIOffline(title="Студия печати "Оттиск"", redoc_url=None)
prices = {
    "otkrytka": 35,
    "plakat": 250,
    "nakleyka": 50,
}
names = {
    "otkrytka": "Открытка",
    "plakat": "Плакат",
    "nakleyka": "Наклейка",
}


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(Path(__file__).with_name("index.html"))


@app.get("/api/price", summary="Рассчитать стоимость печати")
def calculate_price(
    item: Literal["otkrytka", "plakat", "nakleyka"],
    quantity: int = Query(1, ge=1, le=20),
):
    unit_price = prices[item]
    return {
        "item": item,
        "name": names[item],
        "quantity": quantity,
        "unit_price": unit_price,
        "total": unit_price * quantity,
    }