from abc import abstractmethod
from datetime import timedelta, datetime

class Soft():
    name = ""
    producter = ""

    @abstractmethod
    def display(self):
        return

class Free(Soft):

    def __init__(self, b):
        self.name= b.name
        self.producter = b.producter


    @abstractmethod
    def display(self):
        print("Название: ", self.name, "\nПроизводитель: ", self.producter)
        print("----------------------------------------------------")
        return



class Free_Trial(Soft):

    install_date = datetime(2000, 1, 1)
    time_use = timedelta(0)

    def __init__(self, name, prod, year, month, day, freetime):
        self.name = name
        self.producter = prod
        self.install_date = datetime(year, month, day)
        self.time_use = timedelta(freetime)

    def __init__(self, b):
        self.name = b.name
        self.producter = b.producter
        self.install_date = b.install_date
        self.time_use = b.time_use

    @abstractmethod
    def display(self):
        print("Название: ", self.name, "\nПроизводитель: ", self.producter, "\nДата установки: ", self.install_date.date(), "\nСрок бесплатного использования: ", self.time_use)
        print("----------------------------------------------------")
        return



class Commercial(Soft):

    install_date = datetime.now()
    time_use = timedelta(0)
    price = 0

    def __init__(self, name, prod, year, month, day, time_use, price):
        self.name = name
        self.producter = prod
        self.install_date = datetime(year, month, day)
        self.time_use = timedelta(time_use)
        self.price = price

    def __init__(self, b):
        self.name = b.name
        self.producter = b.producter
        self.install_date = b.install_date
        self.time_use = b.time_use
        self.price = b.price

    @abstractmethod
    def display(self):
        print("Название: ", self.name, "\nПроизводитель: ", self.producter,"\nЦена($): ", self.price, "\nДата установки: ", self.install_date.date(), "\nСрок использования: ", self.time_use)
        print("----------------------------------------------------")
        return

dlina = int(input('Сколько программ? '))
progs = []

for i in range(dlina):
    progs.append(Soft())

for i in range(dlina):
    print("\n\n")

    temp = ''
    while len(temp) == 0:
        temp = input("Введите название программы: ")
        progs[i].name = temp

    temp = ''
    while len(temp) == 0:
        temp = input("Введите производителя: ")
        progs[i].producter = temp

    temp = ''
    temp = input("Введите дату установки YYYY-MM-DD (если надо): ")

    if len(temp) == 0:
        progs[i] = Free(progs[i])
        continue
    else:
        progs[i].install_date = datetime.strptime(temp, '%Y-%m-%d')

        temp = ''
        while len(temp) == 0:
            temp = input("Введите срок использования: ")
            progs[i].time_use = timedelta(int(temp))

        temp = ''
        temp = input("Введите цену (если надо): ")

        if len(temp) == 0:
            progs[i] = Free_Trial(progs[i])
        else:
            progs[i].price = int(temp)
            progs[i] = Commercial(progs[i])


print("\n\nВсе программы:")
for i in range(dlina):
    progs[i].display()

print('\n///////////////////////////////////////////////\nПрограммы, доступные сегодня:')
for i in range(len(progs)):
    if type(progs[i]) == Free:
        progs[i].display()
    elif (progs[i].install_date + progs[i].time_use) >= datetime.now():
        progs[i].display()