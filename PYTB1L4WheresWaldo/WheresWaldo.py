import random

people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

print(people)

def findPerson(person):
    x = 0

    for seat in people:
        if(seat == person):
            print(person + ' is gevonden!')
            break
        else:
            x += 1

    return x + 1

stoel = findPerson('Waldo')

print('Waldo zit op stoel nummer: ' + str(stoel))