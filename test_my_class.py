import pytest
import my_class

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
def c():
    calc = my_class.Calc()
    return calc


def test_calc_add_initialization_integer(c):
    assert c.add(5, 10) == 15
    assert c.add(-10, 100) == 90
    assert c.add(100, -150) == -50
    assert c.add(10000, 11000) == 21000
def test_calc_add_initialization_float(c):
    assert c.add(5.2, 5.2) == 10.4
    assert c.add(-7, -3) == -10
    assert pytest.approx(c.add(1.21351, 2.45678), 0.00001) == 3.67029
def test_calc_add_initialization_str(c):
    assert c.add('ab', 'cd') == 'abcd'
    assert c.add('', '') == ''
