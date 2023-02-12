# ----------------------------- Cow Bull Game ----------------------------------------------

import random as rdm
P = 0
P1 = []
P2 = []
Bull = []
Cow = []
Total_Bull = []

for i in range(0, 4):
    P1.append(rdm.randint(0, 9))
print(P1)


class cowBullGame:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def cbRule(self, c, d):
        self.c = c
        self.d = d
        while True:
            if self.b == self.a:
                print("You Win!")
                self.c.append(self.b)
                break
            del self.b[0:4]  # deleting first 4 digit
            P = input("Enter 4 digit Number: ")
            for j in range(0, len(P)):
                x = int(P[j])
                self.b.append(x)
            print(self.b)
            print(self.a)
            if len(self.b) > 4:
                print("Invalid Number! Game Over")
                break
            if self.b != self.a:
                for k in range(len(self.b)):
                    if self.b[k] == self.a[k]:  # with same position (e.g. P1 = 1234, P2 = 1432 means 2 bulls)
                        self.c.append(self.b[k])
                        print(f"One Bull! Match Digit is: {self.b[k]}")
                    elif self.b[k] in self.a:
                        if self.b[k] != self.a[k]:  # with different position (e.g. P1 = 1234, P2 = 4321 means 4 cows)
                            self.d.append(self.b[k])
                            print(f"One Cow! Match Digit is: {self.b[k]}")
                    else:
                        print("No Bull, No Cow")
                print("Yoy lose! Try again")


cbGame = cowBullGame(P1, P2)
cbGame.cbRule(Bull,Cow)
print(f"Bull: {Bull}")
print(f"Cow list: {Cow}")

for cnt in range(0,len(Bull)):
    if type(Bull[cnt]) == list:
        for flist in range(0,len(Bull[cnt])):
            cbLength = Bull[cnt]
            Total_Bull.append(cbLength[flist])
    else:
        Total_Bull.append(Bull[cnt])

print(f"Bull list: {Total_Bull}")
print(f"Number of Bulls are: {len(Total_Bull)}")
print(f"Number of Cows are: {len(Cow)}")
print(f"Number of Bulls and Cows are: {len(Total_Bull) + len(Cow)}")