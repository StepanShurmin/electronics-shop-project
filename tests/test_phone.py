import pytest

from src.item import Item
from src.phone import Phone


def test_phone_property():
    phone = Phone("iPhone 14", 120000, 5, 2)

    assert str(phone) == 'iPhone 14'
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2

    phone1.number_of_sim = 15
    assert phone1.number_of_sim == 15

    phone1.number_of_sim = 0
    assert ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
