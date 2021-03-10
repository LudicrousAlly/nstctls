import numpy as np


class money:
    rubli = np.long(0)
    kopeyki = np.ubyte(0)

    def display(self):
        print("{0},{1:02d}".format(str(self.rubli), int(self.kopeyki)))

    def __float__(self):
        a = float(self.rubli)
        b = float(self.kopeyki)
        b /= 100
        return a+b

    def __add__(self, b):
        c = money()
        c.rubli = self.rubli
        c.kopeyki = self.kopeyki

        c.rubli = np.long(c.rubli + b.rubli)
        c.kopeyki = np.ubyte(c.kopeyki + b.kopeyki)

        c.rubli += c.kopeyki // 100
        c.kopeyki %= 100

        return c

    def __sub__(self, b):
        c = money()
        c.rubli = self.rubli
        c.kopeyki = self.kopeyki

        c.rubli = np.long(c.rubli - b.rubli)
        raznost = int(c.kopeyki) - int(b.kopeyki)

        if raznost < 0:
            c.rubli -= 1
            raznost = 100 + raznost

        c.kopeyki = np.ubyte(raznost)

        return c

    def __truediv__(self, b):
        d = money()
        d.rubli = self.rubli
        d.kopeyki = self.kopeyki


        a = float(self)
        b = float(b)
        c = a/b

        d.rubli = np.long(c // 1)


        temp = list(str(c%1))
        del temp[0]
        del temp[0]
        temp2 = ""
        temp2 += temp[0]
        temp2 += temp[1]

        d.kopeyki = np.ubyte(int(temp2))

        return d

    def __mul__(self, b):

        d = money()
        d.rubli = self.rubli
        d.kopeyki = self.kopeyki

        a = float(self)
        b = float(b)
        c = a * b

        d.rubli = np.long(c // 1)

        temp = list(str(c % 1))
        del temp[0]
        del temp[0]
        temp2 = ""
        temp2 += temp[0]
        temp2 += temp[1]

        d.kopeyki = np.ubyte(int(temp2))

        return d

    def __eq__(self, b):

        if self.rubli == b.rubli and self.kopeyki == b.kopeyki:
            return True
        else:
            return False


a = money()
b = money()
c = money()

a.rubli = 3
a.kopeyki = 50

b.rubli = 4
b.kopeyki = 50

c = a + b
c.display()

c = a - b
c.display()

c = a*b
c.display()

c = a/b
c.display()

c = a / 14.67
c.display()

c = a * 13.15
c.display()

if a == b:
    print("True")
else:
    print("False")


