import sys

def sort_ (a, b):
    a = a.lower()
    b = b.lower()
    if a > b:
        return True
    return False

fname = sys.argv[1]

text = []
with open(fname) as f:
    for s in f:
        s = s.split()
        if len(s) != 0:
            text.append(s)

with open(fname, 'w') as f:
    for i in range(len(text)):
        for j in range(len(text[i])):
            if j < len(text[i]) - 1:
                f.write(text[i][j] + " ")
            else:
                f.write(text[i][j])
        f.write("\n")

lines = len(text)
letters = 0
words = 0

for line in text:
    words += len(line)
    for i in range(len(line)):
        for j in range(len(line[i])):
            if 'a' <= line[i][j] <= 'z' or 'A' <= line[i][j] <= 'Z':
                letters += 1

max_len = 0
max_str = ""
lines_one_ch_start_end = 0

for line in text:
    dlina = 0
    for i in range(len(line)):
        dlina += len(line[i])
    if dlina > max_len:
        max_str = ""
        max_len = dlina
        for i in range(len(line)):
            max_str += line[i] + ' '

for line in text:
    if line[0][0] == line[len(line)-1][len(line[len(line)-1])-1]:
        lines_one_ch_start_end += 1

for k in range(len(text)):
    pup = []

    for i in range(len(text[k])):
        for j in range(len(text[k][i])):
            pup.append(text[k][i][j])

    pup.sort()

    text[k] = pup

    for i in range(len(text[k])-1):
        for j in range(len(text[k])-1-i):
            if sort_(text[k][j], text[k][j+1]):
                text[k][j], text[k][j+1] = text[k][j+1], text[k][j]


    text[k] = ''.join(text[k])

print('Количесто непустых строк:', lines)
print('Количество букв:', letters)
print('Количество слов:', words)
print('Самая длинная строка:', max_str)
print('Колво строк, начинающихся и заканчивающихся на один символ:', lines_one_ch_start_end)
print('Отсортированный текст файла:', text)