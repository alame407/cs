import re
# 2

tests = ["А ты знал, что ВТ - - лучшая кафедра в ИТМО?",  # ВТ лучшая кафедра в ИТМО
         "ВТ лучшая но более 4 слов кафедра ИТМО",  #
         "ВТ и ровно 4 слова ИТМО",  # ВТ и ровно 4 слова ИТМО
         "2 раза ВТ - лучшая кафедра в ИТМО ВТ это лучшая кафедра в ИТМО",  # ВТ лучшая кафедра в ИТМО, ВТ это лучшая кафедра в ИТМО
         "нет слов между ВТ ИТМО",  # ВТ ИТМО
         "ВТ много ;;;;;; не %%%% слов --- ИТМО",  # ВТ много не слов ИТМО
         "ВТ ВТ ИТМО ИТМО",  # ВТ ИТМО, ВТ ВТ ИТМО, ВТ ИТМО ИТМО, ВТ ВТ ИТМО ИТМО
         ]

for i in range(len(tests)):
    print(tests[i])
    tests[i] = re.sub(r'\s{2,}', ' ', re.sub(r'[^ \w]', '', tests[i]))
    ans = []
    ans += re.findall(r'(?=(\bВТ\b\s(?:\b\w*\b\s){0,4}\bИТМО\b))', tests[i])
    for el in ans:
        print(el)
    print('--------------------')