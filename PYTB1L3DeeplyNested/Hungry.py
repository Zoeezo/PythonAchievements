hungry = True
wannaCook = False
leftovers = False
money = 50

if (hungry and not wannaCook):
    if (not leftovers and money > 100):
        print("niet koken!")
    else:
        print('koken!')