import pytest

from src.item import Item
from src.phone import Phone


def test_phone_property():
    phone = Phone("iPhone 14", 120000, 5, 2)

    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_item_add():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(TypeError):
        phone1 + 5


def test_phone_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2

    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3

    phone1.number_of_sim = 0
    assert ValueError
