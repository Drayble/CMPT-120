# oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

import random


class Student:
    def __init__(self, name, studentID, year, major, gpa):
        self.name = name
        self.id = studentID
        self.year = year
        self.major = major
        self.gpa = gpa

    def checkHonors(self):
        if (self.gpa >= 3.5):
            return "" + str(self.name) + " qualifies for the honors program with a gpa of " + str(self.gpa) + "."
        else:
            return "" + str(self.name) + " does not qualify for the honors program due to a gpa of " + str(self.gpa) + "."

    def lotteryForPoverty(self):
        lucky_num = random.randrange(0, 10000)
        if (lucky_num == self.id):
            return "Winner! " + str(self.name) + " gets free lunch!\n"
        else:
            return "Loser! No free lunch for " + str(self.name) + " today.\n"


def main():
    # create three students and check if they get free lunch and if they qualify for honors
    x = Student("Petunia", 4800, "Sophomore", "Communications", 2.8)
    y = Student("Enrique", 7883, "Sophomore", "Computer Science", 3.9)
    z = Student("Bartholomew", 2971, "Sophomore", "Business", 3.5)

    print(x.checkHonors())
    print(x.lotteryForPoverty())

    print(y.checkHonors())
    print(y.lotteryForPoverty())

    print(z.checkHonors())
    print(z.lotteryForPoverty())


main()
