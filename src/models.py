from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """
    Абстрактный класс
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: "Product") -> float:
        pass


class MixinInit:
    """
    Класс-миксин
    """

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self._price}, {self.quantity})"


class Product(BaseProduct, MixinInit):
    """
    Класс для представления товара
    """

    name: str
    description: str
    quantity: int

    all_products: list["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        BaseProduct.__init__(self, name, description, price, quantity)  # Реализация абстрактного метода
        MixinInit.__init__(self)  # Вызов init миксина
        self.all_products.append(self)

    # def __init__(self, name: str, description: str, price: float, quantity: int):
    #     super(BaseProduct, self).__init__(name, description, price, quantity)
    #     MixinInit.__init__(self)
    #     self.name = name
    #     self.description = description
    #     self.__price = price
    #     self.quantity = quantity
    #
    #     Product.all_products.append(self)

    @property
    def price(self) -> float:
        """
        Метод-геттер, возвращающий цену продукта
        """
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Метод-сеттер, изменяющий цену продукта
        """
        if new_price < self._price:
            print("Цена снижается!")
            user_answer = input('Хотите изменить цену? ("y" = да, "n" = нет): ')
            if user_answer != "y":
                return
        while new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            new_price = float(input("Введите новую цену: "))

        self._price = new_price

    @classmethod
    def new_product(cls, dict_: Any) -> "Product":
        """
        Класс-метод, создающий новый объект класса
        """
        new_product = cls(**dict_)
        for product in Product.all_products:
            if new_product.name == product.name:
                product.quantity += new_product.quantity
                if product._price < new_product._price:
                    product._price = new_product._price
                return product
        return new_product

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строковое отображение
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Магический метод, возвращающий стоимость всех продуктов на складе, в соответствии с типом продукта
        """
        if type(self) == type(other):
            return (self._price * self.quantity) + (other._price * other.quantity)
        raise TypeError("Складывать можно только одинаковые типы продуктов")


class Smartphone(Product):
    """
    Класс товара смартфоны
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс товара трава газонная
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class BaseEntity(ABC):
    """
    Абстрактный класс
    """

    @abstractmethod
    def __init__(self) -> None:
        pass


class Category(BaseEntity):
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
        if not isinstance(product_, Product):
            raise ValueError("Складывать можно только объекты Product и дочерние от них.")
        Category.product_count += 1
        return self.__products.append(product_)

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
    Вспомогательный класс перебора товаров одной категории
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
            self.index += 1
            return str(result)
        else:
            raise StopIteration

    def __str__(self) -> str:
        if self.data.products:
            return str(self.data.products[0])
        return ""


class Order(BaseEntity):
    """
    Вспомогательный класс для создания заказа
    """

    def __init__(self, product: "Product", quantity: int) -> None:
        self.product = product
        self.quantity = quantity
        self.total_price = quantity * self.product.price
