from src.utils import uploading_data_from_json_file


def test_uploading_data_from_json_file(sample_json: str) -> None:
    categories = uploading_data_from_json_file(sample_json)

    # Проверяем, что получен список с одним объектом Category
    assert len(categories) == 1
    category = categories[0]

    # Проверяем свойства категории
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории смартфонов"

    # Проверяем, что у категории есть один продукт
    assert len(category.products) == 1
    product = category.products[0]

    # Проверяем свойства продукта
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
