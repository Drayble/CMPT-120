# instructions: Something about these if statements aren't giving the desired effect. Look at them and see how to fix
# them. (Run them yourself and see what the output is!) also, we have some input practice!

def main():
    # this is a nice solid working one!
    name = input("Your name is? ")
    print("Hello,", name)

    # this isn't printing anything :( so sad. what's wrong with her? Why is it not printing out?
    color = input("What's your favorite color? ")
    print("Your favorite color is,", color)

    # I thought I did this right :( can you fix it for me?
    age = input("How old are you? ")
    print("You are " + str(age) + " years old")

    # Start with this one! We have a compilation error :(
    # Side note: you can put these statements in parentheses or not. it's up to you.
    if 5 > 3:
        print("5 is greater than 3")

    # There are multiple correct answers and adjustments to this one
    isFive = 5
    if isFive > 5:
        print(str(isFive), "is greater than 5")
    elif isFive < 5:
        print(str(isFive), "is less than 5")
    else:
        print(str(isFive), "is equal to 5")

    # more multiple correct answers. Similar to the first. Adjust as perceived
    toCheck = 4
    if toCheck >= 5:
        print(str(toCheck), "is greater  or equal to 5.")
    elif toCheck <= 3:
        print(str(toCheck), "is less than or equal to 3.")
    else:
        print(toCheck, "is equal to 4 (between 5 and 3)")

    # Is it really printing the BEST option though? Rearrange these as you see fit
    toCheck = 5
    if toCheck == 5:
        print("toCheck (" + str(toCheck) + ") is equal to 5")
    elif toCheck > 7:
        print("toCheck (" + str(toCheck) + ") is greater than 7")
    elif toCheck < 6:
        print("toCheck (" + str(toCheck) + ") is less than 6")
    else:
        print("toCheck (" + str(toCheck) + ") is invalid")


main()
