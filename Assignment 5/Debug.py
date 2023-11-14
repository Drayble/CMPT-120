def main():
    #good working example!
    stringInput = input("enter a string: ")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int: ")
    if intInput.isnumeric():
        print("int!")
    else:
        print("not int :(")
    
    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers: ")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")
       
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")
        
    #now write code to check if the input was either an asterisk OR an ampersand (&)
    astoramp = input("Enter either an asterisk or an ampersand, please: ")
    if astoramp == "*" or astoramp == "&":
        print("You followed basic instructions correctly. Nice job!")
    else:
        print("Learn what the keys on the keyboard are")
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    x = 1
    while True:
        gimmepossiblyanint = input("Gimme an integer, now! ")
        if gimmepossiblyanint.isnumeric():
            print("Epic you did it the right way")
            x = int(gimmepossiblyanint)
            break
        else:
            print("Do it again and look it up if you're stuck")
    print("Here's your new integer:", x)

    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
    gotmarist = input("Enter a string of text that contains \"marist\" somewhere: ")
    if "marist" in gotmarist:
        print("It got \"marist\"")
    else:
        print("It no got \"marist\"")
        # i found 2 different ways
    if gotmarist.__contains__("marist"):
        print("It got \"marist\"")
    else:
        print("It no got \"marist\"")
    
main()
