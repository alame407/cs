import re
# 0

tests = ["students.spam@yandex.ru",  # yandex.ru
         "example@example",  # Fail
         "fgdg'sada@yandex.ru",  # Fail
         "dsdad_sads@google.com",  # google.com
         "fdhdfh@go_gle.com",  # Fail
         "dsd@yandex.ru@",  # Fail
"dsd@@@yandex.ru",
"dsd@yan@dex.ru",
"dsd@yandex.ru.ty",
"dsd@yandex.kz",
"d123sd@yandex.ru",
"dsd@yand345ex.ru",
"_dsd@.......yndex",
         ]

for i in range(len(tests)):
    print(tests[i])
    pattern_for_check = re.compile(r'[.a-zA-Z0-9_]+@[a-zA-Z.]+\.[a-zA-Z]+')
    pattern_for_search = re.compile(r'(?<=@)[\w.]*')
    if pattern_for_check.fullmatch(tests[i]):
        print(pattern_for_search.search(tests[i])[0])
    else:
        print('Fail')
    print('--------------------')