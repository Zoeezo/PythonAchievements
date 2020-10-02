groceryList = ['Kaas', 'Chips', 'Ramen']
shoppingCart = ['Kaas', 'Chips', 'Ramen']

klaarMetShoppen = False

for item in groceryList:
    for product in shoppingCart:
        if(item == product):
            klaarMetShoppen = True
        else:
            klaarMetShoppen = False
    
    if(not klaarMetShoppen):
        break

if(klaarMetShoppen):
    print('Done shopping')
else:
    print('Continue shopping')