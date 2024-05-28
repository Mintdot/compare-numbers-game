import random
from tkinter import *

def Large():
    if eval(One) > eval(Two):
        Explation.configure(text="정답입니다!!")
        Compare()
    else:
        Explation.configure(text="오답입니다..")


def Equal():
    if eval(One) == eval(Two):
        Explation.configure(text="정답입니다!!")
        Compare()
    else:
        Explation.configure(text="오답입니다..")

def Small():

    if eval(One) < eval(Two):
        Explation.configure(text="정답입니다!!")
        Compare()
    else:
        Explation.configure(text="오답입니다..")


def FirstNumber():
    One = random.randint(0, 100)
    Three = random.randint(0, 100)
    Arithmetic = ['+', '-', '*', '/']
    ASMD = random.choice(Arithmetic)
    First = str(One) + ASMD + str(Three)

    return First

def SecondNumber():
    Two = random.randint(0, 100)
    Four = random.randint(0, 100)
    Arithmetic = ['+', '-', '*', '/']
    ASMD = random.choice(Arithmetic)
    Second = str(Two) + ASMD + str(Four)

    return Second

One = FirstNumber()
Two = SecondNumber()

def Compare():
    global One, Two

    One = FirstNumber()
    Two = SecondNumber()
    FirstLabel.configure(text=One)
    SecondLabel.configure(text=Two)



game = Tk()
game.title("숫자 비교 게임")
Answer = Frame(game)
Number = Frame(game)
Inequality = Frame(game)
Explation = Label(Answer, text="숫자 비교 게임", font=("", 15))
FirstLabel = Label(Number, text=One, font=("", 20))
SecondLabel = Label(Number, text=Two, font=("", 20))
LeftButton = Button(Inequality, text=" > ", command=Large, width=6, height=2)
MiddleButton = Button(Inequality, text=" = ", command=Equal, width=6, height=2)
RightButton = Button(Inequality, text=" < ", command=Small, width=6, height=2)

Answer.pack()
Number.pack()
Inequality.pack(pady=5)
Explation.pack()
FirstLabel.pack(side=LEFT, padx=10, pady=10)
SecondLabel.pack(side=LEFT, padx=10, pady=10)
LeftButton.pack(side=LEFT, padx=10)
MiddleButton.pack(side=LEFT, padx=10)
RightButton.pack(side=LEFT, padx=10)


game.mainloop()
