def div(a, b):
    return a/b


if __name__ == '__main__':
    # asercja - można poniższe 4 linijki zastąpić assercją - assert
    #if div(5, 10) == 0.5:
     #   print('PASSED')
    #else:
     #   raise Exception('FAILED')
    assert div(1, 2) == 0.5, 'FAILED'
    print('PASSED')

    assert div(2, 1) == 2, 'FAILED'
    print('PASSED')

    assert div(100, 50) == 2, 'Failed'
    print('Passed')

# obsługa wyjątku:
    try:
        div(5, 0)
    except:
        print('Passed')



def area(c, d):
    return (c + d) ** 2


if __name__ == '__main__':

    assert area(3, 3) == 36
    print('area Passed')

    assert area(1, 1) == 4
    print('area Passed')



def factorial(n): # silnia

    result = 1  # zaczynamy od jeden, ponieważ nie możemy podstawić '0' do pętli
    if n in (0, 1):  # gdy n = 0 lub 1: zwróć 1
        return 1
    for i in range(2, n + 1):  # gdy n>1 mnóż przez kolejne liczby od 2 do n
        result = result * i
    return result


if __name__ == '__main__':

    assert factorial(3) == 7, 'factorial Failed'
    print('factorial Passed')