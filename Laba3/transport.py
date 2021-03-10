from abc import abstractmethod


class TRANSPART():
    marka = ""
    nomer = ""
    speed = 0
    gruz = 0

    @abstractmethod
    def display(self):
        print("Не тот класс!!")
        return

    @abstractmethod
    def gruzopodyomnost(self):
        return

class avto(TRANSPART):

    def __init__(self, b):
        self.marka = b.marka
        self.nomer = b.nomer
        self.speed = b.speed
        self.gruz = b.gruz

    @abstractmethod
    def display(self):
        print("----------------------------------------------------\n"
              "Марка: ", self.marka, "\nНомер: ", self.nomer, "\nСкорость: ", self.speed, "\nГрузоподъемность: ", self.gruz)
        return

    @abstractmethod
    def gruzopodyomnost(self):
        print("Грузоподъемность равна ", self.gruz, " кг")
        return

class moto(TRANSPART):

    kolyaska = False

    def __init__(self, b):
        self.marka = b.marka
        self.nomer = b.nomer
        self.speed = b.speed
        self.gruz = b.gruz
        self.kolyaska = b.kolyaska

    @abstractmethod
    def display(self):
        print("----------------------------------------------------\n"
              "Марка: ", self.marka, "\nНомер: ", self.nomer, "\nСкорость: ", self.speed, "\nГрузоподъемность: ", self.gruz)

        if self.kolyaska == True:
            print("Коляска присутствует")
        else:
            print("Коляска отсутствует")
        return

    @abstractmethod
    def gruzopodyomnost(self):

        if self.kolyaska == False:
            self.gruz = 0

        print("Грузоподъемность равна ", self.gruz, " кг")
        return int(self.gruz)

class gruzo(TRANSPART):

    pricep = False

    def __init__(self, b):
        self.marka = b.marka
        self.nomer = b.nomer
        self.speed = b.speed
        self.gruz = b.gruz
        self.pricep = b.pricep


    @abstractmethod
    def display(self):
        print("----------------------------------------------------\n"
              "Марка: ", self.marka, "\nНомер: ", self.nomer, "\nСкорость: ", self.speed, "\nГрузоподъемность: ", self.gruz)

        if self.pricep == True:
            print("Прицеп присутствует")
        else:
            print("Прицеп отсутствует")
        return

    def gruzopodyomnost(self):

        if self.pricep == True:
            self.gruz *= 2

        return int(self.gruz)



dlina = int(input("Введите кол-во машин: "))

mashini = []

for i in range(dlina):
    mashini.append(TRANSPART())

for i in range(len(mashini)):

    temp = ''
    while len(temp) == 0:
        temp = input("Введите марку: ")
        mashini[i].marka = temp

    temp = ''
    while len(temp) == 0:
        temp = input("Введите номер: ")
        mashini[i].nomer = temp

    temp = ''
    while len(temp) == 0:
        temp = input("Введите скорость: ")
        mashini[i].speed = int(temp)

    temp = ''
    while len(temp) == 0:
        temp = input("Введите грузоподъемность: ")
        mashini[i].gruz = int(temp)

    temp = ''
    temp = input("Есть ли коляска?(Y/N): ")
    if temp == 'Y':
        mashini[i].kolyaska = True
        mashini[i] = moto(mashini[i])
    elif temp == 'N':
        mashini[i].kolyaska = False
        mashini[i] = moto(mashini[i])
    elif len(temp) == 0:
        temp = input("Есть ли прицеп?(Y/N): ")
        if temp == 'Y':
            mashini[i].pricep = True
            mashini[i] = gruzo(mashini[i])
        elif temp == 'N':
            mashini[i].pricep = False
            mashini[i] = gruzo(mashini[i])
        elif len(temp) == 0:
            mashini[i] = avto(mashini[i])
            continue

print("\n\n")
for i in range(len(mashini)):
    mashini[i].gruzopodyomnost()
    mashini[i].display()

podyom = int(input("\n\nВведите необходимую грузоподъемность: "))

print("\n\n")
for i in range(len(mashini)):
    if mashini[i].gruz >= podyom:
        mashini[i].display()