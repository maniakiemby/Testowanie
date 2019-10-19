import my_class

def test_dog_initialization():
    d = my_class.Dog('Azor')
    assert d.name == 'Azor'

def test_dog_speak():
    d = my_class.Dog('Azor')
    assert d.speak() == 'Jestem Azor "hau-hau"'


def test_lamp_off_initialization():
    l = my_class.Lamp()
    assert l.is_ligtening() == False

def test_lamp_on_initialization():
    l = my_class.Lamp()
    assert l.is_ligtening() == True


# Zadanie: stworzyć klasę i ją przetestować