# These instructions below are copied from the other example, the adjustments are a space after Instructions: Create
# a variable of any name and set it equal to 10. The first if statement should read: if 10 (but use our variable,
# not the number 10) is greater than 12, print out "10 is greater than 12" The second if/else should read: Else if 10
# is greater than 11, print out "10 is greater than 11" The third if/else should read: Else if 10 is equal to 10,
# print out "10 is equal to 10" The else should read: Else print out "10 is less than 10"


# additional instructions: instead of setting our variable to 10, what if we asked the user for the variable and used
# that value in our comparisons?
def main():
    random_var_name = int(input("Gimme a number to compare or I swear I'm gonna quit my job\n"))
    if random_var_name > 12:
        print(random_var_name, "is greater than 12")
    elif random_var_name > 11:
        print(random_var_name, "is greater than 11")
    elif random_var_name == 10:
        print(random_var_name, "is equal to 10")
    else:
        print(random_var_name, "is less than 10")


main()
