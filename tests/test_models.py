from unittest.mock import Mock, patch

from src.models import Category, Product


def test_product(product_fixture: Product) -> None:
    assert product_fixture.name == "Помидор"
    assert product_fixture.description == "Красный"
    assert product_fixture.price == 123.45
    assert product_fixture.quantity == 10


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
    assert new_product.price == 50.0
    assert new_product.quantity == 10


def test_category(category_fixture: Category, product_fixture_2: Product) -> None:
    assert category_fixture.name == "Овощи"
    assert category_fixture.description == "Вкусные и полезные"
    assert category_fixture.products == ["Помидор, 123.45 руб. Остаток: 10 шт.\n"]
    assert Category.product_count == 1
    assert Category.category_count == 1
    category_fixture.add_product(product_fixture_2)
    assert category_fixture.products == [
        "Помидор, 123.45 руб. Остаток: 10 шт.\n",
        "Огурец, 120.0 руб. Остаток: 15 шт.\n",
    ]
