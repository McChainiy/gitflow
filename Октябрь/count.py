from yandex_testing_lesson import count_chars


def test_normal():
    assert count_chars('abc') == {'c': 1, 'a': 1, 'b': 1}


def test_empty():
    assert count_chars('') == {}


def test_one_sym():
    assert count_chars('1') == {'1': 1}


def test_manysym():
    assert count_chars('DED') == {'D': 2, 'E': 1}


def test_uniter():
    try:
        count_chars(1)
    except TypeError:
        pass


def test_iter():
    try:
        count_chars([1, 4, 8])
    except TypeError:
        pass