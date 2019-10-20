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


def test_add_initialization_1():
    foo = my_class.Calc()
    assert foo.add(5, 10) == 15
def test_add_initialization_2():
    q = my_class.Calc()
    assert q.add(-10, 100) == 90
def test_add_initialization_3():
    w = my_class.Calc()
    assert w.add(100, -150) == -50
def test_add_initialization_4():
    e = my_class.Calc()
    assert e.add(10000, 11000) == 21000