import my_math      # importujemy funkcję z pliku my_math (modułu my_math)


def test_add():     # zgrupowanie assercji w funkcji (funkcję trzeba wywołać)
    assert my_math.add(7, 3) == 10
    assert my_math.add(10, 3) == 13
    assert my_math.add(20, 50) == 70



def test_product():
    assert my_math.product(3, 3) == 9
    assert my_math.product(10, 1) == 10
    assert my_math.product(20, 0.5) == 10
    assert my_math.product(10, -1) == -10
    assert my_math.product(10, 0) == 0


def test_reversal():
    assert my_math.reversal('tak') == 'kat'
    assert my_math.reversal('parara') == 'ararap'
    assert my_math.reversal('Marcin') == 'nicram'

def test_is_palindrom():
    assert my_math.is_palindrom('ala')
    assert not my_math.is_palindrom('as')     # to samo co: assert my_math.is_palindrom('as') == False


test_add()
test_product()
test_reversal()
test_is_palindrom()
