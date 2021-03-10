import random

def upr1(arr):
    maxCountDigits = 0
    for i in range(0, len(arr)):
        countDigits = len(str(arr[i]))
        if maxCountDigits < countDigits:
            maxCountDigits = countDigits

    countRepeatArr = [0] * len(arr)
    for j in range(0, len(arr)):
        countRepeatArr[j] = maxCountDigits - len(str(arr[j]))
        firstDigit = int(arr[j]) % 10
        arr[j] = str(arr[j]) + str(firstDigit) * countRepeatArr[j]

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                countRepeatArr[i], countRepeatArr[j] = countRepeatArr[j], countRepeatArr[i]

    for i in range(0, len(arr)):
        temp = 10 ** countRepeatArr[i]
        arr[i] = int(arr[i]) // int(temp)

    chislo = ""
    for i in arr:
        chislo += str(i)
    print("Максимальное возможное число = ", chislo)


def upr2():
    operators = ['+', '-']

    target = 100

    lines = ["1"]
    for i in range(2, 10):
        for j in range(len(lines)):
            for op in operators:
                lines.append(lines[j] + op + str(i))
            lines[j] += str(i)

    n = 1

    for line in lines:
        if eval(line) == target:
            print(n, " ", line, '=', target)
            n += 1


def upr3():
    chisl1 = '1001'
    chisl2 = '10100'

    def bin_to_dec(digit):
        dlina = len(digit)
        chislo_dec = 0
        for i in range(0, dlina):
            chislo_dec = chislo_dec + int(digit[i]) * (2 ** (dlina - i - 1))
        return chislo_dec

    chisl3 = bin_to_dec(chisl1) + bin_to_dec(chisl2)

    print(chisl3)

    new_chisl = ''

    while chisl3 > 0:
        new_chisl = str(chisl3 % 2) + new_chisl
        chisl3 = chisl3 // 2

    print(new_chisl)


def upr4():
    matr = []

    for i in range(10):
        temp = [0] * 10
        for j in range(10):
            temp[j] = int(random.random() * 2)
        matr.append(temp)

    for i in range(0, 10):
        print(' '.join(map(str, matr[i])))

    longest = {'hor': 0, 'ver': 0, 'dia': 0}

    for i in range(len(matr)):
        curr = 0
        for j in range(len(matr)):
            if matr[i][j] == 0 and j == 0:
                curr += 1
            elif matr[i][j] == 0 and j == (len(matr)-1) and matr[i][j-1] == 0:
                curr += 1
            elif matr[i][j] == 0 and matr[i][j-1] == 0:
                curr += 1
            elif matr[i][j] == 0:
                curr = 1
            else: curr = 0
            if curr > longest['hor']:
                longest['hor'] = int(curr)

    print("hor = ", longest['hor'])

    for i in range(len(matr)):
        curr = 0
        for j in range(len(matr)):
            if matr[j][i] == 0 and j == 0:
                curr += 1
            elif matr[j][i] == 0 and j == (len(matr)-1) and matr[j][i-1] == 0:
                curr += 1
            elif matr[j][i] == 0 and matr[j-1][i] == 0:
                curr += 1
            elif matr[j][i] == 0:
                curr = 1
            else: curr = 0
            if curr > longest['ver']:
                longest['ver'] = int(curr)

    print("ver = ", longest['ver'])

    for i in range(len(matr)):
        curr = 0
        k = i
        if k == 0:
            for j in range(len(matr)):
                curr = 0
                for l in range(j, -1, -1):


                    if matr[k][l] == 0 and k == 0:
                        curr += 1
                    elif matr[k][l] == 0 and matr[k - 1][l + 1] == 0:
                        curr += 1
                    elif matr[k][l] == 0:
                        curr = 1
                    else:
                        curr = 0

                    k += 1
                    if curr > longest['dia']:
                        longest['dia'] = int(curr)
                k = 0

        else:
            l = len(matr)-1
            curr = 0

            while k < len(matr):

                if matr[k][l] == 0 and l == len(matr)-1:
                    curr += 1
                elif matr[k][l] == 0 and matr[k - 1][l + 1] == 0:
                    curr += 1
                elif matr[k][l] == 0:
                    curr = 1
                else:
                    curr = 0

                k += 1
                l -= 1
                if curr > longest['dia']:
                    longest['dia'] = int(curr)


    print("dia = ", longest['dia'])

    print("Самая длинная цепочка состоит из ", max(longest['ver'], longest['hor'], longest['dia']), " нулей")




class stud:

    def __init__(self, info):
        info = info.split(' ')
        self.surname = info[1]
        self.name = info[0]
        self.mark = info[2]
    def display(self):
        print("Фамилия+имя: ", self.surname, " ", self.name, "\nБалл: ", self.mark)


def upr5():
    kol_vo = int(input("Введите кол-во студентов: "))
    students = [0] * kol_vo

    pers = ["Антон Рысь 8", "Иван Корпатов 5",
             "Джонатан Кра 6", "Опан Юоп 10",
             "Илья Пикнут 8"]

    for i in range(len(pers)):
        students[i] = stud(pers[i])

    print("\nStudenti: ")
    for i in range(len(students)):
        students[i].display()

    mid = 0

    for i in range(len(students)):
        mid += int(students[i].mark)

    mid /= kol_vo

    print("\nsredniy ball = ", mid)

    print("\nStudenti s balom > srednego: ")
    for i in range(len(students)):
        if int(students[i].mark) > mid:
            students[i].display()

def upr6():

    m = int(input("Введите m:"))
    n = int(input("Введите n:"))
    matr = []

    for i in range(m):
        temp = [0] * n
        for j in range(n):
            temp[j] = int(random.random() * 2)
        matr.append(temp)

    for i in range(m):
        print(' '.join(map(str, matr[i])))

    side = 0
    for i in range(len(matr)):
        for j in range(len(matr)):
            if matr[i][j] == 0:
                continue
            if matr[i][j] == 1:
                matr[i][j] = min(matr[i][j - 1], matr[i - 1][j], matr[i - 1][j - 1]) + 1
            if matr[i][j] > side:
                side = matr[i][j]

    print("Максимальный порядок:", side)


array = [5, 22, 1, 7, 3, 1, 95]

upr1(array)

print('\n')
upr2()

print('\n')
upr3()

print('\n')
upr4()

print('\n')
upr5()

print('\n')
upr6()

