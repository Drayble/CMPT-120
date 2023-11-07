class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department


class Cake:
    # can you fill out the rest of this for me? im dumb
    # the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting


class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length

    def breedGuess(self):
        if self.fur_length == "long":
            return ("Domestic Longhair")
        else:
            return ("Domestic Shorthair")


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    # create your own function! what do you want it to do?
    def getCarInfo(self):
        return ("This car is a " + str(self.color) + " " + str(self.year) + " " + str(self.model) + ".")


def main():
    # fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Ash", 8)
    print(newDog.name, newDog.age)

    # and what about a new employee
    newEmployee = Employee("Burt", 1294, "Human Resources")
    # how would we print out each of the variables from newEmployee?
    print("Hi my name is " + str(newEmployee.name) + ", I work in " + str(
        newEmployee.department) + " and my ID number is " + str(newEmployee.idNumber) + ".\n")

    # now create and print out a cake you make
    cake1 = Cake("Chocolate", "Vanilla")
    print("My cake is", cake1.flavor, "with a", cake1.frosting, "frosting\n")

    # and now create another cake and print it out
    cake2 = Cake("Vanilla", "Buttercream")
    print("My cake is", cake2.flavor, "with a", cake2.frosting, "frosting\n")

    # create a cat!
    cat1 = Cat("Timmy", 50, "short")
    # create another cat!
    cat2 = Cat("Walter", 4, "long")
    # What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())

    # create a car!
    myCar = Car("Shelby Cobra", 1965, "red")
    # Now print out the function you made for car :)
    print(myCar.getCarInfo())


main()
