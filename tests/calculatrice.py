
class Calculatrice:
    def addition(self, a, b):
        return a + b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Division par zéro interdite.")
        return a / b