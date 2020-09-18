print("Type een zin en ik zal gaan stutteren!")
sentence = input(">>> ")

wordList = sentence.split()

newSentence = ""

for word in wordList:
    if (len(word) > 3):
        temp = word[:2] + "... "
        newSentence += temp * 2
    
    newSentence += word + " "

print()
print(newSentence)