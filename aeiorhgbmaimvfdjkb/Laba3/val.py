from abc import abstractmethod

class Valuta():
    value = 0

    @abstractmethod
    def to_ruble(self):
        return

    @abstractmethod
    def display(self):
        return

class Dollar(Valuta):

    def __init__(self, n):
        self.value = n

    def to_ruble(self):
        return self.value * 2.58

    def display(self):
        print('Доллары:', self.value)


class Euro(Valuta):
    def __init__(self, n):
        self.value = n

    def to_ruble(self):
        return self.value * 3.04

    def display(self):
        print('Евро:', self.value)


Valuts = []

Valuts.append(Dollar(7))
Valuts.append(Euro(8))

for i in range(len(Valuts)):
    Valuts[i].display()
    print('В рублях: ', Valuts[i].to_ruble(), '\n--------------------')
