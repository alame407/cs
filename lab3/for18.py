import re

# 2

tests = ["А ты знал, что ВТ - лучшая кафедра в ИТМО?",  # ВТ лучшая кафедра в ИТМО
         "ВТ лучшая но более 4 слов кафедра ИТМО",  #
         "ВТ и ровно 4 слова ИТМО",  # ВТ и ровно 4 слова ИТМО
         "2 раза ВТ - лучшая кафедра в ИТМО ВТ это лучшая кафедра в ИТМО",  # ВТ лучшая кафедра в ИТМО, ВТ это лучшая кафедра в ИТМО
         "нет слов между ВТ ИТМО",  # ВТ ИТМО
         "ВТ ВТ ИТМО ИТМО",  # ВТ ИТМО, ВТ ВТ ИТМО, ВТ ИТМО ИТМО, ВТ ВТ ИТМО ИТМО
        "ВТ              ИТМО",
        "ВТ - - -- - - - - -ИТМО",
        "ВТ это ВТ ИТМО не ВТ ИТМО",
         ]

for i in range(len(tests)):
    print(tests[i])
    tests[i] = r"\B{%s}{%s}[^\s\w]+\B" % (i, i)
    print(tests[i])
    tests[i] = re.sub(r'\b\w*[^\s\w]+\w*\b', '', tests[i])
    tests[i] = re.sub(r'[^\s\w]', '', tests[i]).split()
    ans = []
    pattern = re.compile(r'\bВТ\b\s(?:\b\w+\b\s){0,4}\bИТМО\b')
    for j in range(len(tests[i])):
        if tests[i][j] == "ВТ":
            current_string = tests[i][j]
            for k in range(1, min(6, len(tests[i]) - j)):
                current_string += ' ' + tests[i][j + k]
                if pattern.fullmatch(current_string):
                    ans.append(re.search(pattern, current_string)[0])
    for el in ans:
        print(el)
    print('--------------------')
