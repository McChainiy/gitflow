from yandex_testing_lesson import Rectangle
from pytest import raises


def test_init_type():
    for i in ['2', [1, 2], {3: 4}]:
        with raises(TypeError):
            Rectangle(3, i)


def test_init_value():
    with raises(ValueError):
        Rectangle(3, -1)


def test_area():
    assert Rectangle(3, 4).get_area() == 12
    assert Rectangle(3.5, 4).get_area() == 14


def test_perimeter():
    assert Rectangle(3, 4).get_perimeter() == 14
    assert Rectangle(3.5, 4).get_perimeter() == 15
