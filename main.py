from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    products = [
        {
            "id": 1,
            "name": "Товар 1",
            "description": "Описание товара 1",
            "price": "1000 руб.",
            "image": "product1.jpg"
        },
        {
            "id": 2,
            "name": "Товар 2",
            "description": "Описание товара 2",
            "price": "1200 руб.",
            "image": "product2.jpg"
        },
        {
            "id": 3,
            "name": "Товар 3",
            "description": "Описание товара 3",
            "price": "1500 руб.",
            "image": "product3.jpg"
        }
    ]
    return render_template(r'index.html', products=products)


# Маршрут для страницы с подробной информацией о товаре
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Пример поиска товара по id (в реальном приложении, вероятно, будут использоваться база данных)
    products = [
        {
            "id": 1,
            "name": "Товар 1",
            "description": "Описание товара 1",
            "price": "1000 руб.",
            "image": "product1.jpg",
            "details": "Подробная информация о товаре 1"
        },
        {
            "id": 2,
            "name": "Товар 2",
            "description": "Описание товара 2",
            "price": "1200 руб.",
            "image": "product2.jpg",
            "details": "Подробная информация о товаре 2"
        },
        {
            "id": 3,
            "name": "Товар 3",
            "description": "Описание товара 3",
            "price": "1500 руб.",
            "image": "product3.jpg",
            "details": "Подробная информация о товаре 3"
        }
    ]

    # Находим товар по его id
    product = next((item for item in products if item["id"] == product_id), None)

    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "<h1>Товар не найден</h1>", 404


app.run(port=80, debug=True)
