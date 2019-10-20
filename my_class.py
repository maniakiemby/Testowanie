class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'Jestem {self.name} "hau-hau"'


    def rename(self, new_name):
        self.name = new_name


class Lamp:
    def __init__(self, light):
        self.light = light

    def turn_on(self):
        self.light = True

    def turn_off(self):
        self.light = False

    def is_ligtening(self):
        return self.light


class Bicycle:
    number_of_wheels = 2

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def bike_info(self):
        return f'This is a {self.color} {self.brand} '\
               f'with {self.number_of_wheels} wheels.'


class Calc:
    def add(self, x, y):
        return x + y


my_bike = Bicycle('black','Romet')
print(my_bike.bike_info)
your_bike = Bicycle('Yellow', 'Fuji')
print(your_bike.bike_info)


d1 = Dog('Azor')
d2 = Dog('Rex')
print(d1.speak())
print(d2.speak())
d2.rename('Młokos')
print(d2.speak())
