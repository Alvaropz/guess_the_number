import random
import math

class Find():
    def __init__(self, **kargs):
        self.player_name = kargs.get('name', None)
        self.r_number = random.randrange(1, 1000)
        self.i_number = None
        self.score = 1000
        self.attempt = 2
        self.test = kargs.get('test', False)

    def choose_name(self, name):
        if name:
            self.player_name = name
        else:
            self.player_name = input("What is your player name?: ")
        
    def choose_number_manual(self):
        self.i_number = input("What is your number? ")
        if self.i_number.isdigit():
            self.i_number = int(self.i_number)
            self.smaller_greater()
        else:
            print("That's not a valid number.")

    def choose_number_test(self):
        self.i_number = -1
        range = [0, 1000]
        while self.i_number != self.r_number:
            self.i_number = math.floor((range[1]-range[0]) / 2) + range[0]
            if self.i_number > self.r_number:
                range = [range[0], self.i_number]
                self.smaller_greater()
            elif self.i_number < self.r_number:
                range = [self.i_number, range[1]]
                self.smaller_greater()
    
    def smaller_greater(self):
        if self.attempt < 1:
            self.score -= (math.floor(abs(self.r_number-self.i_number)**(1/2)))*3
        else:
            self.attempt -= 1
        if self.i_number > self.r_number:
            print("The chosen number is smaller than yours!")
        else:
            print("The chosen number is greater than yours!")

    def guess_the_number(self):
        print("This game is about guessing a random chosen number between 1 and 1000. Your initial score is 1000. You will lose some points depending on how far you are from the right number. You will have some feedback about how far you are from the right number. The first two tries won't take any point from you. Good luck!")
        self.choose_name(self.player_name)
        while self.i_number != self.r_number:
            if self.test:
                self.choose_number_test()
            else:
                self.choose_number_manual()
            print("Your current score is {}.".format(self.score))
        with open("scores.txt", "a") as myfile:
            myfile.write("{}: Score {}\n".format(self.player_name, self.score))
        with open("scores.txt", "r") as myfile:
            print(myfile.read())
