def main():
    # Can you print out "Hello" 8 times? I gave you a tiny hint to start...
    for x in range(8):
        print("\"Hello\"") \
            # yes i know i'm being a smartass here

    print("\n")

    # What about as a while loop?
    loops = 0
    while (loops < 8):
        print("\"Hello\"")
        loops += 1

    print("\n")

    # The loop iterations are one behind in a non-programming counting way... how can we fix this?
    count = 0
    while (count < 3):
        print("While loop iteration", (count + 1))
        count += 1

    print("\n")

    # Same deal here!
    for x in range(3):
        print("For loop iteration:", (x + 1))

    print("\n")
    # Uh oh I messed up and made an infinite loop... so silly of me!
    endless = 4
    while (endless < 5):
        print("I'm stuck in this loop!!!!")
        endless += 1

    print("\n")
    # print out your last name one letter at a time
    for x in "Ames":
        print(x)

    print("\n")
    # aw i suck i made another infinite loop.. use that thing I taught you about to get out once it prints once...
    # starts with a b... br....
    found = False
    while found == False:
        print("i only printed once")
        break

    print("\n")
    # can you fill this out so that it prints found when it hits the letter r?
    for x in "Marist":
        if x == "r":
            print("found")

    print("\n")

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # you could print out the list using print(numbers) OR you could go the long way and use a for loop to print out the value of each index :)
    for x in numbers:
        print(x)

    print("\n")
    # what if I wanted you to print out only the even numbers in this range I made?
    for x in range(20, 501):
        # i feeeeel like modulooooooo is neededddd
        if (x % 2 == 0):
            print(x)


main()
