from flask import Flask, abort, render_template

app = Flask(__name__)

SERVICES = {
    "otkrytka": {
        "name": "Открытка",
        "price": 35,
        "duration": "A6 (105x148 мм)",
        "description": "Плотная мелованная бумага 300 г/м2, полноцветная двусторонняя печать.",
    },
    "plakat": {
        "name": "Плакат",
        "price": 250,
        "duration": "A3 (297x420 мм)",
        "description": "Интерьерная печать высокого разрешения на постерной бумаге 200 г/м2.",
    },
    "nakleyka": {
        "name": "Наклейка",
        "price": 50,
        "duration": "A5 (148x210 мм)",
        "description": "Виниловая самоклеящаяся плёнка с защитной ламинацией и контурной резкой.",
    },
}


@app.get("/")
def menu():
    return render_template("menu.html", services=SERVICES)


@app.get("/services/<slug>")
def service_detail(slug):
    service = SERVICES.get(slug)
    if service is None:
        abort(404)
    return render_template("drink.html", service=service)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404