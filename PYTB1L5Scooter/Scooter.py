verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

def bereken_maandkosten(km_per_maand):
    return km_per_maand * liter_per_kilometer * benzine_kosten_per_liter + verzekering_per_maand

kilometers = 0
validAnswer = False
while not validAnswer:
    userInput = input('Hoeveel km per maand rijd je? \n')

    try:
        userInput = int(userInput)

        kilometers = userInput
        validAnswer = True

    except:
        print('\nDat is ongeldig, probeer het opnieuw!\n')

maandkosten = bereken_maandkosten(kilometers)

print('\nJe maandkosten zijn: €' + str(maandkosten))
