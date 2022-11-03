import re
# 225

tests = ["X-{/X-{/X-{/",  # 3
         "X-{/X-{P/X-{/",  # 2
         "X-{X-{/PX-{/",  # 2
         "X<P8-{([-{/",  # 0
         "X-P{/XX-{/-{/"  # 1
         ]
for i in range(len(tests)):
    pattern = re.compile(r"X-{/")
    ans = len(pattern.findall(tests[i]))
    print(f'Тест: {tests[i]}, количество = {ans}')
