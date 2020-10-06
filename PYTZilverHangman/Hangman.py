import random

woorden = ['Hallo', 'Soep', 'Boot', 'Stad', 'Olifanten']
woord = None
displayWoord = []
guessedLetters = []
lives = 6
running = True

def check(letter):
    global guessedLetters
    global displayWoord

    guessedLetters.append(letter)

    x = 0
    while(x < len(woord)):
        if(woord[x] == letter):
            correct = True
            displayWoord[x] == letter

    if(not correct):
        lives -= 1

def userInput():

    while True:
        userInput = input('Raad een letter: \n').lower()

        if(userInput == 'exit'):
            running = False
            return None

        if(len(userInput) > 1):
            print('\nDat is geen letter!\n')
            continue

        try:
            int(userInput)
            print('\nDat is een cijfer!\n')
            continue
        except:
            ok = 'ok'

        isUsed = False
        for letter in guessedLetters:
            if(userInput == letter):
                isUsed = True
                break
        
        if(isUsed):
            print('\nDie letter heb je al geraden!!\n')
            continue

        return userInput

def render():
    print('----------- Hangman -----------')
    print('Lives: ', lives)
    print()

    temp = ''
    for letter in displayWoord:
        temp += letter + ' '

    print(temp)
    print()
    print('-------------------------------')

    temp = ''
    for letter in guessedLetters:
        temp += letter + ', '

    print(temp)
    print()   
    

def getWord():
    index = random.randint(1, len(woorden))
    woord = woorden[index]

    x = 0
    while(x != len(woord)):
        displayWoord.append('_')

def gameLoop():
    getWord()
    while running:
        render()
        temp = userInput()

        if(temp != None):
            check()
    #stop()

gameLoop()