from src.item import Item


class Phone(Item):
    """Дочерний класс."""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        """Инициализация класса Phone, с атрибутами класса `Item` и дополнительным атрибутом."""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Возвращает отображение экземпляра класса, в режиме отладки."""
        return f"{self.__class__.__name__}(" \
               f"'{self.name}', {self.price}, {str(self.quantity)}," \
               f" {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """Возвращает количество поддерживаемых сим-карт."""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count_sim):
        """Проверяет количество поддерживаемых сим-карт(целое, положительное число)."""
        if count_sim > 0:
            self.__number_of_sim = count_sim
        print('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
