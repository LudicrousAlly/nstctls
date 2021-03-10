with open('studenti.txt') as f:
    text = f.readlines()
    size = len(text)

print(text)

text = []

with open('studenti.txt') as f:
    for s in f:
        s = s.split()
        text.append(s)


studenti = []

for i in range(len(text)):
    studenti.append(text[i][0])

n = len(studenti)

marks = []

for i in range(n):
    tmp = []
    marks.append(tmp)

for i in range(n):
    marks[i].append(int(text[i][1]))
    marks[i].append(int(text[i][2]))
    marks[i].append(int(text[i][3]))
    marks[i].append(int(text[i][4]))

print("Список всех студентов:")
for i in range(n):
    print("\nСтудент: ", studenti[i],
          "\nОценки : {0},{1},{2},{3}".format(marks[i][0], marks[i][1], marks[i][2], marks[i][3]))

avrgmarks = [0]*n

for i in range(n):
    avrgmarks[i] = (marks[i][0]+marks[i][1]+marks[i][2]+marks[i][3])/4


print("---------------------------------------------"
      "\nСтуденты со средним баллом меньше 4:")

for i in range(n):
    if avrgmarks[i] < 4:
        print("\nСтудент: ", studenti[i],
              "\nОценки : {0},{1},{2},{3}".format(marks[i][0], marks[i][1], marks[i][2], marks[i][3]),
              "\nСредний балл: ", avrgmarks[i])

korr = input("\nВведите фамилию студента, инфу о котором хотите отредачить: ")
if len(korr) == 0:
    print("Выход...")
else:

    for i in range(n):
        if studenti[i] == korr:
            familiya = input("Введите фамилию: ")
            print("Введите 4 оценки: ")
            mark = [0]*n
            mark[0] = input()
            mark[1] = input()
            mark[2] = input()
            mark[3] = input()
            studenti[i] = familiya
            marks[i] = mark

    with open('studenti.txt', 'w') as f:
        for i in range(n):
            f.write(studenti[i] + " " + str(marks[i][0]) + " " + str(marks[i][1]) + " " + str(marks[i][2]) + " " + str(marks[i][3]) + "\n")
