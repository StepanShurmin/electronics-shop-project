import csv
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent
PATH = Path.joinpath(ROOT_PATH, '../src/items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        """Возвращает отображение экземпляра класса, в режиме отладки."""
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """Возвращает строковое представление экземпляра класса."""
        return f'{self.__name}'

    @property
    def name(self) -> str:
        """
        Возвращает название товара.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает название товара.

        :param name: Новое название товара.
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из файла items.csv.
        """
        cls.all = []
        with open(PATH, 'r', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Возвращает число из числа-строки.

        :param value: Число-строка.
        :return: Число.
        """
        return int(float(value))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = (self.price * self.quantity) * Item.pay_rate
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
