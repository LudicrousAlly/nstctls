imya = ['']*3

for i in range(3):
    imya[i] = input("Введите имя {0}-го файла: ".format(i+1))

lengths = [0]*len(imya)

for i in range(len(lengths)):
    with open(imya[i]) as f:
        for line in f:
            for j in range(len(line)):
                if line[j] != ' ' and line[j] != '\n':
                    lengths[i] += 1

print(lengths)

for i in range(len(imya)):
    if lengths[i] == min(lengths):
        for j in range(len(imya)):
            if lengths[j] == max(lengths):
                filemin = open(imya[i], 'r')
                filemax = open(imya[j], 'w')
                text = filemin.readlines()
                print(text)
                for k in range(len(text)):
                    filemax.write(text[k])
                break

        break

