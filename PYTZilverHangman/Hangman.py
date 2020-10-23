from time import sleep
import random
from os import name, system

def endScreen(word, guessedWord, guessedLetters, hasWon):
    clearScreen()

    print('->->-> Hangman <-<-<-')
    print()
    if(hasWon):
        print('GG You won! You truly are amazing!')
    else:
        print('GG You were so close! Better luck next time!')
    print()
    print('The word was: ' + word)
    
    temp = ''
    for char in guessedWord:
        temp += char + ' '
    print('You had: ' + temp)

    temp = ''
    for char in guessedLetters:
        temp += char + ', '
    print('You guessed the letters: ' + temp)

    print('--------------------')
    print()

def checkWord(guessedWord):
    for char in guessedWord:
        if(char == '_'):
            return False
    
    return True

# I stole findAll from stackoverflow <3
def findAll(string, sub):
    start = 0
    while True:
        start = string.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def updateGuessedWord(guessedWord, word, playerInput):
    indexes = list(findAll(word, playerInput))

    for index in indexes:
        guessedWord[index] = playerInput

    return guessedWord


def checkInput(playerInput, word):
    if playerInput in word:
        return True
    else:
        return False

def getInput(guessedLetters):
    while True:
        userInput = input('Guess: ').lower()

        if (userInput == 'exit'):
            return userInput
        
        if (len(userInput) > 1 or len(userInput) < 1):
            print('ERROR: That is not a valid character!')
            print()
            continue
            
        used = False
        for letter in guessedLetters:
            if(userInput == letter.lower()):
                print('ERROR: You already guessed that letter!')
                print()
                used = True
                continue
        
        if(used):
            continue

        return userInput

def clearScreen():
    if name == 'nt': # Windows
        _ = system('cls')
    else: # Mac/Linux
        _ = system('clear')

def updateScreen(guessedWord, guessedLetters, lives):
    clearScreen()

    print('->->-> Hangman <-<-<-')
    print()
    print('Lives:', lives)
    print()

    temp = ''
    for char in guessedWord:
        temp += char + ' '
    print(temp)

    temp = ''
    for char in guessedLetters:
        temp += char + ', '
    print('Guessed: ' + temp)

    print('--------------------')
    print()

def gameLoop(wordInfo):
    word = wordInfo[0]
    guessedWord = wordInfo[1]
    guessedLetters = []
    lives = 5
    hasWon = False

    while True:
        updateScreen(guessedWord, guessedLetters, lives)
        playerInput = getInput(guessedLetters)

        if (playerInput == 'exit'):
            break

        guessedLetters.append(playerInput.upper())

        isCorrect = checkInput(playerInput, word)

        if(isCorrect):
            guessedWord = updateGuessedWord(guessedWord, word, playerInput)
        else:
            lives -= 1
            
            if(lives == 0):
                break

        isCompleted = checkWord(guessedWord)

        if(isCompleted):
            hasWon = True
            break
    
    endScreen(word, guessedWord, guessedLetters, hasWon)

def generateWord():
    words = ['ijs', 'koffie', 'olifant', 'huis', 'hoi', 'planeet', 'school']
    wordInfo = []

    index = random.randint(0, len(words) - 1)
    wordInfo.append(words[index])

    guessedWord = []

    for char in wordInfo[0]:
        guessedWord.append('_')

    wordInfo.append(guessedWord)

    return wordInfo

def beginScherm():
    print('''
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
    ''')

  
    print()
    print('Welcome to Hangman!\nYou have to guess letters till you have the entire word.\nBut make sure your lives dont run out!')
    print()

    input('     Press enter to start')
  
    wordInfo = generateWord()
    gameLoop(wordInfo)



beginScherm()