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

d1 = Dog('Azor')
d2 = Dog('Rex')
print(d1.speak())
print(d2.speak())
d2.rename('Młokos')
print(d2.speak())
