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

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строковое отображение
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Магический метод, возвращающий стоимость всех продуктов на складе
        """
        return (self.__price * self.quantity) + (other.__price * other.quantity)


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

    def add_product(self, product_: Product) -> None:
        """
        Метод, добавляющий новый продукт категории
        """
        self.__products.append(product_)

        Category.product_count += 1

    @property
    def products(self) -> list[Product]:
        """
        Метод-геттер, возвращающий список продуктов
        """
        return self.__products

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строковое отображение
        """
        sum_product = 0
        for product_ in self.__products:
            sum_product += product_.quantity
        return f"{self.name}, количество продуктов: {sum_product} шт."


class ProductSearch:
    """
    Вспомогательный класс
    """

    def __init__(self, data: Category):
        self.data = data
        self.index = 0

    def __iter__(self) -> "ProductSearch":
        self.index = 0
        return self

    def __next__(self) -> str:
        if self.index < len(self.data.products):
            result = self.data.products[self.index]
            # print(self.data.products)
            # print((result))
            self.index += 1
            return str(result)
        else:
            raise StopIteration

    def __str__(self) -> str:
        if self.data.products:
            return str(self.data.products[0])
        return ""
