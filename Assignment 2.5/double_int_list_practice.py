def main():
    # set this to any double
    doubleValue = 8.0

    # set this to any int
    intValue = 4

    # print out addition, subtraction, multiplication, and division of these two values
    print(doubleValue + intValue)
    print(doubleValue - intValue)
    print(doubleValue * intValue)
    print(doubleValue / intValue)

    # populate this list
    myFriends = ["Caden", "Joe", "Jo", "Ryan"]

    # print out your friends at index 2 and index 3
    print("\n", myFriends[2], ", ", myFriends[3], "\n")

    # populate this list with five numbers
    fiveNumbers = [25, 24, 33, 1, 98]

    # do each of the four equations with different numbers each time.
    print(fiveNumbers[1] + fiveNumbers[3])
    print(fiveNumbers[0] - fiveNumbers[1])
    print(fiveNumbers[2] * fiveNumbers[4])
    print(fiveNumbers[0] / fiveNumbers[3])

    # now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting
    # the fiveNumber list)
    fiveNumbers[1] = 72
    fiveNumbers[4] = 9

    # print out the list
    print(fiveNumbers)


main()
