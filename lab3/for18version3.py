import re

# 2

tests = ["А ты знал, что ВТ - лучшая ка-федра в ИТМО?",  # ВТ лучшая кафедра в ИТМО
         "ВТ лучшая но более 4 слов кафедра ИТМО",  #
         "ВТ и ровно 4 слова ИТМО",  # ВТ и ровно 4 слова ИТМО
         "2 раза ВТ - лучшая кафедра в ИТМО ВТ это лучшая кафедра в ИТМО",  # ВТ лучшая кафедра в ИТМО, ВТ это лучшая кафедра в ИТМО
         "нет слов между ВТ ИТМО",  # ВТ ИТМО
         "ВТ ВТ ИТМО ИТМО",  # ВТ ИТМО, ВТ ВТ ИТМО, ВТ ИТМО ИТМО, ВТ ВТ ИТМО ИТМО
         ]

for i in range(len(tests)):
    print(tests[i])
    tests[i] = re.sub(r'\B[^\s\w]+\B', ' ', tests[i]).split()
    print(tests[i])
    ans = []
    pattern = re.compile(r'\bВТ\b\s(?:\b\w+\b\s){0,4}\bИТМО\b')
    for j in range(len(tests[i])):
        if tests[i][j] == "ВТ":
            currentString = tests[i][j]
            k = 1
            f = 1
            while k < len(tests[i]) - j and f < 6:
                if re.fullmatch(r'\w+', tests[i][j+k]):
                    currentString += ' ' + tests[i][j + k]
                    if pattern.fullmatch(currentString):
                        ans.append(re.search(pattern, currentString)[0])
                    f = 1
                k += 1

    for el in ans:
        print(el)
    print('--------------------')