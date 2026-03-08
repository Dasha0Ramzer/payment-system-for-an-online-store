from src.models import Category, Product


def test_product_init(product_fixture: Product) -> None:
    assert product_fixture.name == "Помидор"
    assert product_fixture.description == "Красный"
    assert product_fixture.price == 123.45
    assert product_fixture.quantity == 10


def test_category_init(category_fixture: Category) -> None:
    assert category_fixture.name == "Овощи"
    assert category_fixture.description == "Вкусные и полезные"
    assert category_fixture.products[0].name == "Помидор"
    assert category_fixture.product_count == 1
    assert category_fixture.category_count == 1
