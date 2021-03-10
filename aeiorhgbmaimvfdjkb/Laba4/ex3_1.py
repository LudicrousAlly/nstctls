
with open('zadolzhenosti.txt') as f:
    text = f.readlines()
    size = len(text)

text = []

with open('zadolzhenosti.txt') as f:
    for s in f:
        s = s.split()
        text.append(s)
        print(list(s))

abonenti = []
for i in range(len(text)):
    abonenti.append(text[i][0])



abonenti = set(abonenti)
abonenti = list(abonenti)

zadolzhenosti = [0] * len(abonenti)

for i in range(len(text)):
    if text[i][0] in abonenti:
        zadolzhenosti[abonenti.index(text[i][0])] += int(text[i][1])

for i in range(len(abonenti)):
    print("У абонента ",abonenti[i], " задолженость равна ", zadolzhenosti[i])
