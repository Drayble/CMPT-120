'''
mkay so
I talked a lot about helping but not fixing the problem
In this code, if you run this and enter not an integer, it throws an error, as we're aware, as you solved this problem in the debug file
can you google a way to help or even fix this problem that isn't the way we were doing it before?
hint: there's try/catch statements that i didn't teach but is somewhat straightforward to try. There's a thing called regex, etc. 
You can also go much much simpler if you want to, I just want you guys to keep practicing your google skills
and ofc, if you're stuck, don't hesitate to email
'''


def main():
    new_input = input("Gimme an int. Right here --> ")
    new_int = 1
    try:
        new_int = int(new_input)
        print("It worked you goofball! Your value is now set to", new_int)
    except ValueError:
        print("You did not enter an int correctly. You are now a certified goofball.")
    except:
        print("I don't know what the heck you entered but you caused the special error! Yay you!")


main()
