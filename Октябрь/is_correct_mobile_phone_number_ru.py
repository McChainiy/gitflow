from yandex_testing_lesson import is_correct_mobile_phone_number_ru


tests = [('+79261897698', True), ('89262779801', True), ('99999', False),
         ('+7912311111111111', False), ('+7(926)1889292', True), ('+792(6)1231111', False),
         ('abbcga', False), ('+7 999 123-45-67', True), ('+23221232233', False)]

for i in tests:
    if is_correct_mobile_phone_number_ru(i[0]) != i[1]:
        print('NO')
        break
else:
    print('YES')