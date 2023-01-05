import random



animals = ['dog', 'tiger', 'elephant', 'butterfly', 'horse']
cars = ['bmw', 'mercedes', 'audi', 'mazda', 'ferrari']
countrys = ['France', 'Germany', 'Sweden', 'Italy', 'Spain']
colors = ['green', 'red', 'blue', 'purple', 'yellow']


#def game():
   # a1 = random.choice(animals)
    #b2 = random.choice(cars)
  #  c3 = random.choice(countrys)
  #  d4 = random.choice(colors)


def checkinput(word):
    if word == 'exit':
        exit()

    if word == 'hint':
        print("onder voorbehoud")



def a1():
    global animals
    wrd = checkinput(input("Choose your first letter: "))
    animals = random.choice(animals)
    print(animals)




cat = input("Choose category: (animals, cars, countrys, colors) ")


if cat == 'animals':
    a1()

elif cat == 'cars':
    b2()

elif cat == 'countrys':
    c3()

elif cat == 'colors':
    d4()

#game()
