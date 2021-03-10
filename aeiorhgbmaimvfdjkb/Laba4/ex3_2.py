with open('abonents.txt') as f:
    text = f.readlines()
    size = len(text)

text = []

with open('abonents.txt') as f:
    for s in f:
        s = s.split()
        text.append(s)

abonenti = []
for i in range(len(text)):
    abonenti.append(text[i][0])

imena = [0] * len(abonenti)


for i in range(len(text)):
    if text[i][0] in abonenti:
        imena[abonenti.index(text[i][0])] = text[i][1]

for i in range(len(abonenti)):
    if abonenti[i] in abonenti:
        print("У абонента ", imena[abonenti.index(text[i][0])], " номер телефона  ", abonenti[i])

imya = input("Введите фамилию для вывода телефона: ")

for i in range(len(abonenti)):
    if imena[i] == imya:
        print("У абонента ", imya, " номер: ", abonenti[i])