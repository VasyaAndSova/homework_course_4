import pytest


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products_in_list) == 3

    assert second_category.name == "Телевизоры"
    assert (
        second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(second_category.products_in_list) == 1

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 4
    assert second_category.product_count == 4


def test_category_add_product(first_category):
    assert first_category.products_in_list[0].name == "Samsung Galaxy S23 Ultra"
    assert first_category.products_in_list[0].description == "256GB, Серый цвет, 200MP камера"
    assert first_category.products_in_list[0].price == 180000.0
    assert first_category.products_in_list[0].quantity == 5


def test_category_add_product_count(first_category, product):
    assert len(first_category.products_in_list) == 3
    first_category.add_product(product)
    assert len(first_category.products_in_list) == 4


def test_user_product_property(first_category):
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_str(second_category):
    assert str(second_category) == "Телевизоры, количество продуктов: 7 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == '55" QLED 4K'

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_add_product_count_error(first_category, product):
    with pytest.raises(TypeError):
        first_category.add_product("Не продукт")
