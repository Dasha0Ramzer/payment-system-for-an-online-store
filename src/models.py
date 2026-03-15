from typing import Any


class Product:
    """
    Класс для представления товара
    """

    name: str
    description: str
    quantity: int

    all_products: list["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products.append(self)

    @property
    def price(self) -> float:
        """
        Метод-геттер, возвращающий цену продукта
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Метод-сеттер, изменяющий цену продукта
        """
        if new_price < self.__price:
            print("Цена снижается!")
            user_answer = input('Хотите изменить цену? ("y" = да, "n" = нет): ')
            if user_answer != "y":
                return
        while new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            new_price = float(input("Введите новую цену: "))

        self.__price = new_price

    @classmethod
    def new_product(cls, dict_: Any) -> "Product":
        """
        Класс-метод, создающий новый объект класса
        """
        new_product = cls(**dict_)
        for product in Product.all_products:
            if new_product.name == product.name:
                product.quantity += new_product.quantity
                if product.__price < new_product.__price:
                    product.__price = new_product.__price
                return product
        return new_product


class Category:
    """
    Класс для представления категории товаров
    """

    name: str
    description: str

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.__products = products
        self.name = name
        self.description = description

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """
        Метод, добавляющий новый продукт категории
        """
        self.__products.append(product)

        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Метод-геттер, возвращающий цену и количество продукта
        """
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
