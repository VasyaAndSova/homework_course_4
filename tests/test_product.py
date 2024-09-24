from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_create():
    product = Product('55" QLED 4K', "Фоновая подсветка", 800, 7)
    product.name = '55" QLED 4K'
    product.description = "Фоновая подсветка"
    product.price = 800
    product.quantity = 7


def test_product_price_update(capsys, product):
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product.price = 800
    assert product.price == 800
