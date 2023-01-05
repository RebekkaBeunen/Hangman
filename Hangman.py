import random
from tkinter import *
#from tkinter.ttk import *

window = Tk()
window.geometry('300x300')

animals = ['dog', 'tiger', 'elephant', 'butterfly', 'horse']
cars = ['bmw', 'mercedes', 'audi', 'mazda', 'ferrari']
countrys = ['France', 'Germany', 'Sweden', 'Italy', 'Spain']
colors = ['green', 'red', 'blue', 'purple', 'yellow']

def game():
    a = random.choice(animals)
    b = random.choice(cars)
    c = random.choice(countrys)
    d = random.choice(colors)


b1 = Button(window, text = "Animals", activeforeground = 'black', activebackground = 'green', bd = '1', command = a)
b2 = Button(window, text = "Cars", activeforeground = 'black', activebackground = 'gray', bd = '1', command = b)
b3 = Button(window, text = "Country's", activeforeground = 'black', activebackground = 'blue', bd = '1', command = c)
b4 = Button(window, text = "Colors", activeforeground = 'black', activebackground = 'red', bd = '1', command = d)



b1.pack(side = TOP)
b2.pack(side = LEFT)
b3.pack(side = RIGHT)
b4.pack(side = BOTTOM)




window.mainloop()
