from src.item import Item


class MixinLanguage:
    """Класс для хранения и изменения раскладки клавиатуры."""

    def __init__(self, *args, language='EN', **kwargs):
        super().__init__(*args, **kwargs)
        self.language = language

    @property
    def language(self):
        """Возвращает язык раскладки клавиатуры."""
        return self.__language

    @language.setter
    def language(self, lang):
        if lang not in ("EN", "RU"):
            print("AttributeError: property 'language' of 'KeyBoard' object has no setter")
        else:
            self.__language = lang

    def change_lang(self):
        """Изменяет язык (раскладки клавиатуры)."""
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class Keyboard(MixinLanguage, Item):
    """Класс для товара 'клавиатура'."""
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        """Метод для отображения информации об объекте класса для пользователей"""
        return super().__str__()
