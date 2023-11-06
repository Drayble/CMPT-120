# if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
# this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21,
 return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''
import random


def bust(x, y, z):
    s = (x + y + z)
    if (s <= 21):
        return s
    else:
        if (x == 11 or y == 11 or z == 11):
            return (s - 10)
        else:
            return 0


def main():
    card1 = random.randrange(1, 12)
    card2 = random.randrange(1, 12)
    card3 = random.randrange(1, 12)
    print(card1, card2, card3)
    print(bust(card1, card2, card3))


main()
