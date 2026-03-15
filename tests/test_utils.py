from src.utils import uploading_data_from_json_file


def test_uploading_data_from_json_file(sample_json: str) -> None:
    categories = uploading_data_from_json_file(sample_json)

    assert len(categories) == 1
    category = categories[0]

    # Проверяем свойства категории
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории смартфонов"
    assert str(category.products[0]) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
