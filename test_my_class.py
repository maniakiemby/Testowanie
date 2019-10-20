import math # 1 blok importu - biblioteki standardowe
            # oddzielamy te bloki importów
import pytest   # 2 blok - biblioteki, które trzeba zainstalować

import my_class     # 3 blok -  importy naszego projektu

def test_dog_initialization():
    d = my_class.Dog('Azor')
    assert d.name == 'Azor'
def test_dog_speak():
    d = my_class.Dog('Azor')
    assert d.speak() == 'Jestem Azor "hau-hau"'


def test_lamp_off_initialization():
    l = my_class.Lamp(False)
    assert l.is_ligtening() == False
def test_lamp_on_initialization():
    l = my_class.Lamp(True)
    assert l.is_ligtening() == True


def test_bicycle_initialization():
    foo = my_class.Bicycle('black', 'Romet')
    assert foo.bike_info() == 'This is a black Romet with 2 wheels.'
def test_bicycle_initialization_2():
    bar = my_class.Bicycle('Yellow', 'Fuji')
    assert bar.bike_info() == 'This is a Yellow Fuji with 2 wheels.'


@pytest.fixture
def calc():
    calc = my_class.Calc()
    return calc

 # w nawiasach wskazujemy parametry
@pytest.mark.parametrize('num1,num2, res',
                         [
                            (5, 10, 15),
                            (0, 0, 0),
                            (-3, -7, -10),
                            ('ab', 'cd', 'abcd'),
                            ('', '', '')
                         ])
def test_calc_add_initialization_integer_and_strings(num1, num2, res, calc):
    assert calc.add(num1, num2) == res
def test_calc_add_initialization_float(calc):
    assert calc.add(5.2, 5.2) == 10.4
    assert calc.add(-7, -3) == -10
    assert pytest.approx(calc.add(1.21351, 2.45678), 0.00001) == 3.67029


def test_area():
    assert pytest.approx(my_class.circle_area(1), 0.0001) == math.pi
    assert my_class.circle_area(0) == 0
    assert pytest.approx(my_class.circle_area(2.1), 0.0001) == math.pi * (2.1 ** 2)
def test_area_exceptions():
    with pytest.raises(ValueError):
        my_class.circle_area(-3)
def test_area_type_exception():
    with pytest.raises(ValueError):
        my_class.circle_area(3 + 5j)
        my_class.circle_area(True)
        my_class.circle_area('radius')
