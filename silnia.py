def factorial(n): # silnia

    result = 1  # zaczynamy od jeden, ponieważ nie możemy podstawić '0' do pętli
    if n in (0, 1):  # gdy n = 0 lub 1: zwróć 1
        return 1
    for i in range(2, n + 1):  # gdy n>1 mnóż przez kolejne liczby od 2 do n
        result = result * i
    return result


if __name__ == '__main__':

    assert factorial(3) == 6, 'factorial Failed'
    print('factorial Passed')