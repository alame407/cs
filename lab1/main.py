AL = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
CONST_FIB = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]


def from_any_to_dec(x, sys):
    x = str(x)
    res = 0
    picture = f'{x} = '
    for i in range(len(x)):
        if x[i].isdigit():
            tmp = int(x[i])
        else:
            tmp = ord(x[i])-ord('A')+10
        res += tmp*sys**(len(x)-i-1)
        picture += f'{tmp}*{sys}^{len(x)-i-1}+'
    picture = picture[0:-1]
    picture += f' = {res}'
    print(picture)
    return res


def from_dec_to_any(x, sys):
    x = int(x)
    res = ''
    while x > 0:
        print(f'{x} mod {sys} = {x%sys}')
        print(f'{x} div {sys} = {x // sys}')
        if x % sys > 9:
            tmp = AL[x % sys-10]
        else:
            tmp = str(x % sys)
        res += tmp
        x = x//sys
    res = res[::-1]
    return res


def from_any_to_any(x, sys1, sys2):
    return from_dec_to_any(from_any_to_dec(x, sys1), sys2)


def from_dec_to_fact(x):
    tmp = 2
    res = ''
    while x > 0:
        res += str(x % tmp)
        print(f'{x} mod {tmp} = {x%tmp}')
        print(f'{x} div {tmp} = {x//tmp}')
        x = x//tmp
        tmp += 1

    res = res[::-1]
    return res


def from_fib_to_dec(x):
    x = str(x)
    res = 0
    resstr =f'{x} = '
    for i in range(len(x)):
        res += int(x[-i-1])*CONST_FIB[i]
        resstr += f'{int(x[-i-1])}*{CONST_FIB[i]}+'
    resstr=resstr[:(-1)]
    resstr += f' = {res}'
    print(resstr)
    return res


def from_anyfloat_to_dec(x, sys):
    x = str(x)
    picture = f'{x} = '
    integer, fractional = x.split(',')
    res = 0
    for i in range(len(integer)):
        if integer[i].isdigit():
            tmp = int(integer[i])
        else:
            tmp = ord(integer[i]) - ord('A') + 10
        res += tmp * sys ** (len(integer) - i - 1)
        picture += f'{tmp}*{sys}^{len(integer) - i - 1}+'
    for i in range(len(fractional)):
        if fractional[i].isdigit():
            tmp = int(fractional[i])
        else:
            tmp = ord(fractional[i]) - ord('A') + 10
        res += tmp * sys ** (-i-1)
        picture += f'{tmp}*{sys}^{(-i-1)}+'
    picture = picture[0:-1]
    picture += f' = {res}'
    print(picture)
    return res


def from_dec_to_anyfloat(x, sys):
    x = str(x)
    integer, fractional = x.split(',')
    integer = int(integer)
    res = ''
    while integer > 0:
        if integer % sys > 9:
            tmp = AL[integer % sys - 10]
        else:
            tmp = str(integer % sys)
        res += tmp
        integer = integer // sys
    res = res[::-1]
    print(x.split(',')[0] + f' = {res}')
    res += ','
    resfrac = ''
    fractional = 10**(-len(fractional))*int(fractional)
    for i in range(6):
        if fractional == 0:
            break
        print(f'{fractional}*{sys} = {fractional*sys}')
        fractional *= sys
        tmp = int(fractional // 1)
        if tmp > 9:
            tmp = AL[tmp % sys - 10]
        else:
            tmp = str(tmp)
        resfrac += tmp
        fractional -= int(fractional)
    res += resfrac
    return res


def main():
    print('№1')
    print(from_dec_to_any(83932, 15))
    print('------------------------------')
    print('№2')
    print(from_any_to_dec(87238, 13))
    print('------------------------------')
    print('№3')
    print(from_any_to_any('4945C', 13, 7))
    print('------------------------------')
    print('№4')
    print(from_dec_to_anyfloat("46,33", 2))
    print('------------------------------')
    print('№8')
    print(from_anyfloat_to_dec("0,010001", 2))
    print('------------------------------')
    print('№9')
    print(from_anyfloat_to_dec("8F,41", 16))
    print('------------------------------')
    print('№10')
    print(from_dec_to_fact(676))
    print('------------------------------')
    print('№11')
    print(from_fib_to_dec(1001001))
    print('------------------------------')
    print('№13')
    print(from_dec_to_fact(3088))
    print('------------------------------')


if __name__ == '__main__':
    main()