from src.item import Item


class MixinLanguage:
    """Класс для хранения и изменения раскладки клавиатуры."""
    __language = 'EN'

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        """Возвращает язык раскладки клавиатуры."""
        return self.__language

    def change_lang(self):
        """Изменяет язык (раскладки клавиатуры)."""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLanguage):
    """Класс для товара 'клавиатура'."""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return super().__str__()
