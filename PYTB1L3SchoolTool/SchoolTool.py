weekdag = 'Maandag'
weekdag = weekdag.lower()

schooldagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag']

school = False

for dag in schooldagen:
    if(dag == weekdag):
        school = True
        break

if(school):
    print('Tijd voor school!')
else:
    print('Je kan lekker thuis viben!')