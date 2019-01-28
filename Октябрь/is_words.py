from yandex_testing_lesson import strip_punctuation_ru


tests = [('Кое-кто зазнался', 'Кое-кто зазнался'), ("Привет, 'мир'.?!;", "Привет мир"),
         ('Тут есть все: "грибы", яблоки, ананасы - не очень',
          'Тут есть все грибы яблоки ананасы не очень')]

for i in tests:
    if strip_punctuation_ru(i[0]) != i[1]:
        print('NO')
        break
else:
    print('YES')