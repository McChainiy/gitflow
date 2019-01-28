import unittest
from yandex_testing_lesson import reverse


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_onesym(self):
        self.assertEqual(reverse('1'), '1')

    def test_pal(self):
        self.assertEqual(reverse('123'), '321')

    def test_unpal(self):
        self.assertEqual(reverse('stroka'), 'akorts')

    def test_wrong_type_uniter(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_iter(self):
        with self.assertRaises(TypeError):
            reverse([1, 2, 4])


if __name__ == '__main__':
     unittest.main()