from flask import Flask, render_template
from flask import request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Dunk",
        "description": "Представляем мужские качественные кроссовки Nike Dunk 1 High Satin Black Toe. Силуэт создан крупным брендом и баскетболистом по имени Майкл Джордан.",
        "price": "19000 руб.",
        "image": "product1.1.jpg",
        "details": "Подробная информация о товаре 1",
        "sizes" : [37, 38, 39, 40, 41, 42],
        'thumbnails': [  # Список миниатюр
            'product1.2.jpg',
            'product1.3.jpg',
            'product1.4.jpg',
            'product1.5.jpg'
        ]
    },
    {
        "id": 2,
        "name": "Rick Owens",
        "description": "Высокие розовые кеды с контрастными мысками из гладкой натуральной кожи. Светлая прошитая подошва из термополиуретана с мелким протектором shark tooth, плоская шнуровка с серебристыми люверсами, кожаная подкладка.",
        "price": "120000 руб.",
        "image": "product2.jpg",
        "details": "Подробная информация о товаре 2",
        "sizes" : [37, 38, 39, 40, 41, 42],
        'thumbnails': [  # Список миниатюр
            'product1.2.jpg',
            'product1.3.jpg',
            'product1.4.jpg',
            'product1.5.jpg'
        ]
    },
    {
        "id": 3,
        "name": "New Balance",
        "description": "Верх из натуральной замши Текстильные элементы сетчатого плетения Стабилизирующая вставка в пяточной зоне.",
        "price": "10000 руб.",
        "image": "product3.jpg",
        "details": "Подробная информация о товаре 3",
        "sizes" : [37, 38, 39, 40, 41, 42],
        'thumbnails': [  # Список миниатюр
            'product1.2.jpg',
            'product1.3.jpg',
            'product1.4.jpg',
            'product1.5.jpg'
        ]
    }
]


@app.route("/")
def index():
    return render_template(r'index.html', products=products)


# Маршрут для страницы с подробной информацией о товаре
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Находим товар по его id
    product = next((item for item in products if item["id"] == product_id), None)

    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "<h1>Товар не найден</h1>", 404


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()

    filtered_products = [product for product in products if
                         query in product['name'].lower() or query in product['description'].lower()]

    return render_template('index.html', products=filtered_products)


app.run(port=80, debug=True)
