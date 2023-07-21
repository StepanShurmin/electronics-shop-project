import csv
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent
PATH = Path.joinpath(ROOT_PATH, '../src/items.csv')



class InstantiateCSVError(Exception):
    """Класс-исключение, возвращает сообщение об ошибке."""
    def __init__(self, message):
        self.message = message

    def __str__(self) -> str:
        return self.message


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

    def __add__(self, other):
        """Складывает экземпляры классов."""
        if isinstance(other, self.__class__):
            # if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError('Нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов')

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
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла items.csv.
        """
        cls.all = []
        try:
            with open(PATH, 'r', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if not all(key in row for key in ['name', 'price', 'quantity']):
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except InstantiateCSVError as err:
            raise InstantiateCSVError(err.message)

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
