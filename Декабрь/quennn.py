from yandex_testing_lesson import is_under_queen_attack
from pytest import raises


def test_diag():
    assert is_under_queen_attack('d3', 'b1')


def test_undiag():
    assert not is_under_queen_attack('e2', 'g1')


def test_vert():
    assert is_under_queen_attack('e8', 'e1')


def test_horiz():
    assert is_under_queen_attack('f3', 'a3')


def test_same():
    assert is_under_queen_attack('a3', 'a3')


def test_1():
    assert not is_under_queen_attack('d3', 'c5')


def test_digit():
    with raises(TypeError):
        is_under_queen_attack('a3', 23)


def test_list():
    with raises(TypeError):
        is_under_queen_attack([1, 2], 'a3')


def test_dict():
    with raises(TypeError):
        is_under_queen_attack({'ya': 'naruto'}, 'e4')


def test_notcorrect1():
    with raises(ValueError):
        is_under_queen_attack('abc', 'e3')


def test_notcorrect2():
    with raises(ValueError):
        is_under_queen_attack('e2', 'd9')


def test_notcorrect3():
    with raises(ValueError):
        is_under_queen_attack('e0', 'j3')