print("Hallo, wat wil je op je broodje?\n")

butter = input("Wil je boter? (ja/nee)\n>>> ").lower()
print()

if (butter == "ja"):
    butter = "met"
elif (butter == "nee"):
    butter = "met geen"
else:
    butter = "zonder"

meat = input("Wat voor vlees wil je?\n>>> ").lower()
print()

vegetable1 = input("Wat voor groente wil je?\n>>> ").lower()
print()

vegetable2 = input("Wat voor groente wil je nog meer?\n>>> ").lower()
print()

vegetable3 = input("Wat is de laatste groente die je wil?\n>>> ").lower()
print()

sauce = input("wat voor saus wil je?\n>>> ").lower()
print()

print("Hier is je broodje " + butter + " boter en met " + meat + ", " + vegetable1 + ", " + vegetable2 + ", " + vegetable3 + " en " + sauce + "!")