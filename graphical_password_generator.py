import random
from tkinter import *
symbols=['!','@','#','$','%','^','&','*','(',')','~','`']
numbers=[1,2,3,4,5,6,7,8,9,0]
words=['a','b','c','d','e''f','g','h','i','j','k','l','m','n','o','p']


def generate():

   print(str(random.choice(numbers))+
         random.choice(words)+
         random.choice(symbols)+
         str(random.choice(numbers))+
         random.choice(words)+
         random.choice(words)+
         str(random.choice(numbers))+
         random.choice(symbols)+
         random.choice(words))

screen = Tk()
screen.title("Graphical Password generator")
screen.geometry('400x400')

welcome_text=Label(screen, text = "Welcome to my graphical password generator" ,fg='red', bg='yellow')
welcome_text.pack()

generate=Button(screen, text='Generate', fg='red', bg='yellow', command=generate)
generate.place(x=30, y=40)

name_storage=StringVar()
name=Entry(screen, textvariable=name_storage)
name.pack()
screen.mainloop()
