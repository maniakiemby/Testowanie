class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        result = 1
        for item in args:
            result *= item
        return result

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'inf'




