import random

def ex_1():
    N = 10
    arr = [0] * N
    for i in range(N):
        arr[i] = int(random.random() * 20)
    print(arr)

    setarr = set(arr)
    if len(arr) == len(setarr):
        print("Все элементы уникальны")
    else:
        print("Есть одинаковые")
        return

    for i in range(N - 1):
        for j in range(i + 1, N):
            if arr[i] == arr[j]:
                print("Есть одинаковые")
                return
    print('Все элементы уникальны')


def ex_2():
    N = 20
    arr = [0] * N
    for i in range(0, len(arr)):
        arr[i] = int(random.random() * 100)
    print(arr)

    n = 0

    for i in range(len(arr)):
        if 35 < arr[i] < 65:
            n += 1
    print(n)

    arr2 = []
    j = 0
    i = 0

    while i < len(arr):
        if 35 < arr[i] < 65:
            arr2.append(arr[i])
            del arr[i]
            i -= 1
            j += 1
        i += 1

    print(arr)
    print(arr2)

def ex_3():
    N = 300
    count = 0

    for i in range(1, N+1):
        j = int(i)
        while j:
            if j < 10:
                count += 1
                break
            else:
                count += 1
                j /= 10

    print(count)

    pages = 0
    n = 0

    while True:
        if n == 0:
            if count > 9:
                pages += 9
                count -= 9
            else:
                pages += count
                break
        else:
            if (count - 9*(n+1)*10**(n))>0:
                pages += (9*(n+1)*10**(n))/(n+1)
                count -= 9*(n+1)*10**(n)
            else:
                pages += count/(n+1)
                break
        n += 1

    print("pages = ", pages)

def ex_4():
    text = "qwetqwerty, qwqd qwet qweqwrqwr qwqd"

    text = text.replace(", ", ' ')
    text = text.replace('.', ' ')
    text = text.replace(':', ' ')
    text = text.replace(';', ' ')
    text = text.replace('!', ' ')
    text = text.replace('?', ' ')

    print(text)
    array = text.split(' ')
    array.sort()

    words = set(array)

    count = [0] * len(words)
    words = list(words)
    words.reverse()

    for i in range(0, len(array)):
        for j in range(0, len(words)):
            if words[j] == array[i]:
                count[j] += 1


    for i in range(0, len(words)):
        print(words[i], " - встречается ", count[i], " раз")

def ex_5():
    matr = []

    for i in range(5):
        temp = [0] * 5
        for j in range(5):
            temp[j] = int(random.random() * 10)
        matr.append(temp)

    for i in range(0, 5):
        print(' '.join(map(str, matr[i])))

    matr[3], matr[4] = matr[4], matr[3]
    print("\n\n")

    for i in range(0, 5):
        print(' '.join(map(str, matr[i])))

def ex_6():
    array = []
    array = input("Введите последовательность: ").split(' ')
    miss = 0

    for i in range(len(array)):
        array[i] = int(array[i])

    array.sort()

    for i in range(1, len(array)+2):
        if i in array:
            continue
        else:
            miss = i
            break

    print("В последовательности отстутсвует элемент ", miss)

def ex_7():
    d1 = {'year': 2003, 'month': 12}
    d2 = {'year': 2014, 'month': 6}
    du = {}

    while True:
        du['year'] = int(input('Год: '))
        if 0 <= du['year'] <= 3000:
            break
    while True:
        du['month'] = int(input('Месяц: '))
        if 0 < du['month'] < 13:
            break
    if d1['year'] < du['year'] < d2['year']:
        print('Да')
    elif du['year'] == d1['year']:
        if du['month'] >= d1['month']:
            print('Да')
        else:
            print('Нет')
    elif du['year'] == d2['year']:
        if du['month'] <= d2['month']:
            print('Да')
        else:
            print('Нет')
    else:
        print('Нет')

while True:
    choice = input("Введите номер задания(или exit): ")

    if choice == "1":
        ex_1()
    elif choice == "2":
        ex_2()
    elif choice == "3":
        ex_3()
    elif choice == "4":
        ex_4()
    elif choice == "5":
        ex_5()
    elif choice == "6":
        ex_6()
    elif choice == "7":
        ex_7()
    elif choice == "exit":
        break
    else:
        print("Введите корректный номер задания(или exit для выхода)")