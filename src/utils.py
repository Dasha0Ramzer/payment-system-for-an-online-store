import json

from src.models import Category, Product


def uploading_data_from_json_file(file_path: str) -> list[Category]:
    """
    Функция, осуществляющая подгрузку данных из файла JSON
    :param file_path: путь к файлу
    :return: список объектов класса Category
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    categories = []
    for obj in data:
        products = [Product(**product) for product in obj["products"]]
        category = Category(obj["name"], obj["description"], products)
        categories.append(category)
    return categories


# print(uploading_data_from_json_file('../data/products.json'))
