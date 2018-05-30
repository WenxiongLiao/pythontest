from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root = Tk()
w = Label(root,text='Guess Number Game')
w.pack()
mb.showinfo('Welcome','Welcom Guess Number Game')

number =59
while True:
    guess = dl.askinteger('Number','what is your guess')
    if guess == number:
        output = 'bego!'
    elif guess>number:
        output = 'you guess bigger'
    else:
        output = 'you guess smaller'
    mb.showinfo('output', output)