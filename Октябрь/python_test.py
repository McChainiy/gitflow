from yandex_testing_lesson import reverse
from pytest import raises


def test_normal():
    assert reverse('abc') == 'cba'


def test_empty():
    assert reverse('') == ''


def test_one_sym():
    assert reverse('1') == '1'


def test_pal():
    assert reverse('DED') == 'DED'


def test_uniter():
    with raises(TypeError):
        reverse(1)


def test_iter():
    with raises(TypeError):
        reverse([1, 25])
