from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    products = [
        {
            "id": 1,
            "name": "Nike Jordan",
            "price": "19000 руб.",
            "image": "product1.jpg"
        },
        {
            "id": 2,
            "name": "Rick Owens",
            "price": "120000 руб.",
            "image": "product2.jpg"
        },
        {
            "id": 3,
            "name": "New Balance",
            "price": "10000 руб.",
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
            "name": "Nike Jordan",
            "description": "Представляем мужские качественные кроссовки Nike Air Jordan 1 High Satin Black Toe. Силуэт создан крупным брендом и баскетболистом по имени Майкл Джордан.",
            "price": "19000 руб.",
            "image": "product1.jpg",
            "details": "Подробная информация о товаре 1"
        },
        {
            "id": 2,
            "name": "Rick Owens",
            "description": "Высокие розовые кеды с контрастными мысками из гладкой натуральной кожи. Светлая прошитая подошва из термополиуретана с мелким протектором shark tooth, плоская шнуровка с серебристыми люверсами, кожаная подкладка.",
            "price": "120000 руб.",
            "image": "product2.jpg",
            "details": "Подробная информация о товаре 2"
        },
        {
            "id": 3,
            "name": "New Balance",
            "description": "Верх из натуральной замши Текстильные элементы сетчатого плетения Стабилизирующая вставка в пяточной зоне.",
            "price": "10000 руб.",
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


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
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

    filtered_products = [product for product in products if
                         query in product['name'].lower() or query in product['description'].lower()]

    return render_template('index.html', products=filtered_products)


app.run(port=80, debug=True)
