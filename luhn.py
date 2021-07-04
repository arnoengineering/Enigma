import numpy as np

damm_sq = np.array([
    [0, 3, 1, 7, 5, 9, 8, 6, 4, 2],
    [7, 0, 9, 2, 1, 5, 4, 8, 6, 3],
    [4, 2, 0, 6, 8, 7, 1, 3, 5, 9],
    [1, 7, 5, 0, 9, 8, 3, 4, 2, 6],
    [6, 1, 2, 3, 0, 4, 5, 9, 7, 8],
    [3, 6, 7, 4, 2, 0, 9, 5, 8, 1],
    [5, 8, 6, 9, 7, 2, 0, 1, 3, 4],
    [8, 9, 4, 5, 3, 6, 2, 0, 1, 7],
    [9, 4, 3, 8, 6, 1, 7, 2, 0, 5],
    [2, 5, 8, 1, 4, 3, 6, 7, 9, 0]
])


def check_val(v):
    if v == 0:
        print('Valid number')
    else:
        print('Invalid number')


def luhn_multi(n):
    n *= 2
    if n > 9:
        n -= 9
    return n


def lu(num, val=False):
    num = str(num)

    tot = 0
    val_n = 0
    if val:
        val_n = 1
    for n, i in enumerate(reversed(num)):
        i = int(i)
        if (n + val_n) % 2 == 0:  # second dig
            luhn_multi(i)
        tot += i

    check = tot % 10
    if val:
        check_val(check)
    else:
        ch_n = 10 - check
        num += str(ch_n)
        print('Luhn generated number:', num)


def damm(num, val=False):
    in_dig = 0
    num = str(num)

    for n in num:
        n = int(n)
        in_dig = damm_sq[in_dig, n]
    if val:
        check_val(in_dig)
    else:
        num += str(in_dig)
        print('Damm generated number:', num)


def luhn_solve(num, pos):  # todo check multi
    num = str(num)

    tot = 0
    for n, i in enumerate(reversed(num), 1):
        if n != len(num) - pos:
            # sym x
            i = int(i)
            if n % 2 == 0:  # second dig
                i *= 2
                if i > 9:
                    i -= 9
            tot += i
    rem = tot % 10
    pos = 10 - rem
    if pos % 2...-len():
        do multiple
        +9, /2

print("\U0001f600")
ch = input('Generate Number (y,[N]): ')
if ch == 'y':
    w = 'Generating for'
    g = False
else:
    g = True
    w = 'Checking'
nu = input(w + ' number: ')
lu(nu, g)
damm(nu, g)
