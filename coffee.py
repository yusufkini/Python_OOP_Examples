# there will be 5 different coffe types here
# Filter, Americano, White Chocolate Mocha, Latte, Hot Chocolate (Coffee Type)
class Coffe():
    brand = "Kadikoy"
    coffeName = " "
    coffeeStatus = " "  #Hot or Cold?
    milkStatus = " "
    makeTheCoffee = " "
    price = 0
    coffeeGlassStatus = " "  # There will be a material of glass which it hold the coffee inside (plastic or paper glass)
    sugarStatus = " "  # Coffee that someone makes it will be with sugar or without sugar?
    coffeStatusNamesList = ["milkStatus","coffeeStatus", "sugarStatus", "coffeeGlassStatus"]

    def __init__(self):
        pass
    def coffeeStatusInfo(self,list):
        for index, status in enumerate(list):
            print(f"{index + 1}. {self.coffeStatusNamesList[index]}: {status}")
    def opinionChangeMethod(self):
        while True:
            changingCoffeStatus = input("You wanna change your coffee status? (Y/N): ")
            changingCoffeStatus = changingCoffeStatus.upper()

            if changingCoffeStatus == "Y":
                coffeStatusList = [self.milkStatus, self.coffeeStatus, self.sugarStatus, self.coffeeGlassStatus]
                self.coffeeStatusInfo(coffeStatusList)

                changeCoffeAttribute = input("Which status you wanna chance please enter between 1 - 4: ")

                if changeCoffeAttribute == "1":
                    if self.milkStatus == "Yes":
                        self.milkStatus = "No"
                    else:
                        self.milkStatus = "Yes"

                elif changeCoffeAttribute == "2":
                    if self.coffeeStatus == "Hot":
                        self.coffeeStatus = "Cold"
                    else:
                        self.coffeeStatus = "Hot"

                elif changeCoffeAttribute == "3":
                    if self.sugarStatus == "Yes":
                        self.sugarStatus = "No"
                    else:
                        self.sugarStatus = "Yes"

                elif changeCoffeAttribute == "4":
                    if self.coffeeGlassStatus == "Paper":
                        self.coffeeGlassStatus = "Glass"
                    else:
                        self.coffeeGlassStatus = "Paper"

                else:
                    print("Please enter an integer between 1 - 4 !!!")

            elif changingCoffeStatus == "N":
                print("\nProcess continuing... \n")
                self.coffeeMaterials()
                break
            else:
                print("Wrong answer. Please enter a letter between Y or N !!!")
                continue

class FilterCoffe(Coffe):
    coffeName = "Filter Coffe"
    milkStatus = "No"
    coffeeStatus = "Hot"
    sugarStatus = "No"
    coffeeGlassStatus = "Paper"
    makeTheCoffee = "Filter coffee is made by brewing coffee beans"
    def coffeeMaterials(self):
        print(f"Filter Coffee Materials:\nMilk: {self.milkStatus} \n"
              f"Coffe Status: {self.coffeeStatus} \nSugar Status: {self.sugarStatus}\n"
              f"Type of the Glass: {self.coffeeGlassStatus} \nHint: {self.makeTheCoffee}")
    def calculateCoffeePrice(self,coffee_size):
        if coffee_size == "L":
            self.price = 85
        elif coffee_size == "M":
            self.price = 70
        elif coffee_size == "S":
            self.price = 55

        return self.price
class Americano(Coffe):
    coffeName = "Americano"
    milkStatus = "No"
    coffeeStatus = "Hot"
    sugarStatus = "No"
    coffeeGlassStatus = "Paper"
    makeTheCoffee = "Americano is made by adding water to espresso"
    def coffeeMaterials(self):
        print(f"Americano Coffee Materials:\nMilk Status: {self.milkStatus} \n"
              f"Coffe Status: {self.coffeeStatus} \nSugar Status: {self.sugarStatus}\n"
              f"Type of the Glass: {self.coffeeGlassStatus} \nHint: {self.makeTheCoffee}")
    def calculateCoffeePrice(self,coffee_size):
        if coffee_size == "L":
            self.price = 90
        elif coffee_size == "M":
            self.price = 75
        elif coffee_size == "S":
            self.price = 65

        return self.price
class WhiteChocolateMocha(Coffe):
    coffeName = "White Chocolate Coffee"
    milkStatus = "Yes"
    coffeeStatus = "Hot"
    sugarStatus = "Yes"
    coffeeGlassStatus = "Paper"
    makeTheCoffee = "White Chocolate is made with milk, white chocolate and espresso"
    def coffeeMaterials(self):
        print(f"White Chocolate Coffee Materials:\nMilk: {self.milkStatus} \n"
              f"Coffe Status: {self.coffeeStatus} \nSugar Status: {self.sugarStatus}\n"
              f"Type of the Glass: {self.coffeeGlassStatus} \nHint: {self.makeTheCoffee}")
    def calculateCoffeePrice(self,coffee_size):
        if coffee_size == "L":
            self.price = 135
        elif coffee_size == "M":
            self.price = 120
        elif coffee_size == "S":
            self.price = 105

        return self.price
class Latte(Coffe):
    coffeName = "Latte"
    milkStatus = "Yes"
    coffeeStatus = "Hot"
    sugarStatus = "Yes"
    coffeeGlassStatus = "Paper"
    makeTheCoffee = "Latte is made with milk and espresso"
    def coffeeMaterials(self):
        print(f"Latte Materials:\nMilk: {self.milkStatus} \n"
              f"Coffe Status: {self.coffeeStatus} \nSugar Status: {self.sugarStatus}\n"
              f"Type of the Glass: {self.coffeeGlassStatus} \nHint: {self.makeTheCoffee}")
    def calculateCoffeePrice(self,coffee_size):
        if coffee_size == "L":
            self.price = 120
        elif coffee_size == "M":
            self.price = 105
        elif coffee_size == "S":
            self.price = 90

        return self.price
class HotChocolate(Coffe):
    coffeName = "Hot Chocolate"
    milkStatus = "Yes"
    coffeeStatus = "Hot"
    sugarStatus = "Yes"
    coffeeGlassStatus = "Paper"
    makeTheCoffee = "Hot chocolate is made with milk and chocolate"
    def coffeeMaterials(self):
        print(f"Hot Chocolate Materials:\nMilk: {self.milkStatus} \n"
              f"Coffe Status: {self.coffeeStatus} \nSugar Status: {self.sugarStatus}\n"
              f"Type of the Glass: {self.coffeeGlassStatus} \nHint: {self.makeTheCoffee}")
    def calculateCoffeePrice(self,coffee_size):
        if coffee_size == "L":
            self.price = 125
        elif coffee_size == "M":
            self.price = 115
        elif coffee_size == "S":
            self.price = 105

        return self.price