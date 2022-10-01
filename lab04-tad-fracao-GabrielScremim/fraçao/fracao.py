class Fracao:
    numerador = 1
    denominador = 1

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def add(self, fracao):
        num = (self.numerador * fracao.denominador) + (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def sub(self, fracao):
        num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def mul(self, fracao):
        num = (self.numerador * fracao.numerador)
        den = (self.denominador * fracao.denominador)
        return Fracao (num, den)

    def simplify(self, fracao):
        
        return Fracao (num, den)

    def __str__(self):
        return f"{self.numerador} / {self.denominador}"


fracao1 = Fracao(1, 2)
fracao2 = Fracao(3, 5)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.mul(fracao2)
#fracao6 = fracao1.simplify(fracao2)
print(f"fracao1: {fracao1}")
print(f"fracao2: {fracao2}")
print(F"fracao3: {fracao3}")
print(f"fracao4: {fracao4}")
print(f"fracao5: {fracao5}")
#print(f"fracao6: {fracao6}")
