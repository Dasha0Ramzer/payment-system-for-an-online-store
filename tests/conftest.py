import json
from pathlib import Path

import pytest

from src.models import Category, Product


@pytest.fixture
def product_fixture() -> Product:
    return Product("Помидор", "Красный", 123.45, 10)


@pytest.fixture
def product_fixture_2() -> Product:
    return Product("Огурец", "Зеленый", 50.0, 15)


@pytest.fixture
def category_fixture(product_fixture: Product) -> Category:
    return Category("Овощи", "Вкусные и полезные", [product_fixture])


@pytest.fixture
def sample_json(tmp_path: Path) -> Path:
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание категории смартфонов",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]
    file_path = tmp_path / "test_data.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path
