from unittest.mock import Mock, patch

from src.models import Category, Product, ProductSearch


def test_product(product_fixture: Product, product_fixture_2: Product) -> None:
    assert product_fixture.name == "Помидор"
    assert product_fixture.description == "Красный"
    assert product_fixture.price == 123.45
    assert product_fixture.quantity == 10
    sum_products = product_fixture_2 + product_fixture
    assert sum_products == 3034.5


@patch("builtins.input", side_effect="y")
def test_price_decrease(mock_input: Mock, product_fixture: Product) -> None:
    product_fixture.price = 50
    assert product_fixture.price == 50


@patch("builtins.input", side_effect="n")
def test_price(mock_input: Mock, product_fixture: Product) -> None:
    assert product_fixture.price == 123.45


def test_new_product_creation() -> None:
    product_dict = {"name": "Огурец", "description": "Зеленый", "price": 50.0, "quantity": 5}
    new_product = Product.new_product(product_dict)
    assert new_product.name == "Огурец"
    assert new_product.description == "Зеленый"
    assert new_product.price == 120.0
    assert new_product.quantity == 20


def test_category(category_fixture: Category, product_fixture_2: Product) -> None:
    assert category_fixture.name == "Овощи"
    assert category_fixture.description == "Вкусные и полезные"
    assert [str(product) for product in category_fixture.products] == ["Помидор, 123.45 руб. Остаток: 10 шт."]
    assert Category.product_count == 1
    assert Category.category_count == 1
    category_fixture.add_product(product_fixture_2)
    assert [str(product) for product in category_fixture.products] == [
        "Помидор, 123.45 руб. Остаток: 10 шт.",
        "Огурец, 120.0 руб. Остаток: 15 шт.",
    ]
    assert str(category_fixture) == "Овощи, количество продуктов: 25 шт."


def test_product_search() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Смартфоны", "Описание категории", [product1, product2, product3])

    search = ProductSearch(category)
    results = [str(product) for product in search]

    assert results[0] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert results[1] == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
