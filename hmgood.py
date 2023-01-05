import random

empty = ['Nice, but no']
animals = ['dog', 'tiger', 'elephant', 'butterfly', 'horse']
cars = ['bmw', 'mercedes', 'audi', 'mazda', 'ferrari']
countrys = ['France', 'Germany', 'Sweden', 'Italy', 'Spain']
colors = ['green', 'red', 'blue', 'purple', 'yellow']
list = [empty, animals, cars, countrys, colors]

HangmanArrey = ['h', 'a', 'n', 'g', 'm', 'a', 'n']

HangmanWord = ''
Tries = 0

def Game(category):
    global Tries
    global HangmanWord
    RandomWord = random.choice(list[category])

    while True:
        print(RandomWord)
        PlayerGuess = input("Guess the letter or word: ")

        if PlayerGuess in RandomWord:
            print("Correct!")
        else:
            HangmanWord = HangmanWord + HangmanArrey[Tries]
            Tries = Tries + 1
            print("Try again")
            print(HangmanWord)






print("1) animals")
print("2) cars")
print("3) countrys")
print("4) colors")
category = input("Choose category:  ")
if category == '' or category.isdigit() == False:
    print("please enter valid number!")
else:
    category = int(category)
    Game(category)
