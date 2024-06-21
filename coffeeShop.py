from coffee import Coffe
from coffee import Americano
from coffee import FilterCoffe
from coffee import HotChocolate
from coffee import Latte
from coffee import WhiteChocolateMocha

# there will be 5 different coffe types here
# Filter, Americano, White Chocolate Mocha, Latte, Hot Chocolate (Coffee Type), these will be hot or cold?
coffeeTypeList = ["Filter Coffee","Americano","White Chocolate Mocha","Latte","Hot Chocolate"]
coffeePriceList = [85,70,55 ,90,75,65 ,135,120,105 ,120,105,90 ,125,115,105]

coffee1 = Coffe()

print(f"\nWelcome to {coffee1.brand} Coffee Shop \nWould you like something to drink? There is a menu below: \n")

def startFunction():
    i = 0
    j = 0
    # The menu
    while j <= 14:
        print(f"{coffeeTypeList[i]} L:{coffeePriceList[j]} M:{coffeePriceList[j + 1]} S:{coffeePriceList[j + 2]}")
        i += 1
        j += 3

startFunction()

while True:
    chosenCoffe = 0
    coffePrice = 0

    userCoffeeChoose = input("\nWhat drink would you like to drink today? (Please enter an integer (1 - 5):")

    if userCoffeeChoose == "1":
        filterCoffe1 = FilterCoffe()
        chosenCoffe = filterCoffe1

    elif userCoffeeChoose == "2":
        americano1 = Americano()
        chosenCoffe = americano1

    elif userCoffeeChoose == "3":
        whiteChocCoffe1 = WhiteChocolateMocha()
        chosenCoffe = whiteChocCoffe1

    elif userCoffeeChoose == "4":
        latte1 = Latte()
        chosenCoffe = latte1

    elif userCoffeeChoose == "5":
        hotChocolate1 = HotChocolate()
        chosenCoffe = hotChocolate1
    else:
        print("Please enter an integer between 1 - 5\n")
        print("The Menu:")
        startFunction()
        continue

    print(f"\nYou have chosen {chosenCoffe.coffeName} \n")
    chosenCoffe.coffeeMaterials()
    print()
    chosenCoffe.opinionChangeMethod()

    while True:
        sizeOfCoffe = input("\nWhich size would you like to choose? (L - M - S):")
        sizeOfCoffe = sizeOfCoffe.upper()

        if ((sizeOfCoffe == "L") or (sizeOfCoffe == "M")) or (sizeOfCoffe == "S"):
            coffePrice = chosenCoffe.calculateCoffeePrice(sizeOfCoffe)
            break
        else:
            print("Please enter an letter like (L - M - S)! ")
            continue

    print(f"\nThe coffee price is: {coffePrice} \nEnjoy your drink :)")
    break
































