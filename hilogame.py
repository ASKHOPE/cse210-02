# A play_again code has been placed.
# If a player choose to play again
# A while loop has been added
#  in case a wrong number was selected
# Author Sandra Asamoah 

import random as r
rand_num = r.randint(1, 13)
print (rand_num)
guess = input("Enter a number:  ")

while int(guess) != rand_num:
        print("Incorrect! please try another number")  
        if int(guess)>random_num:
            print("Too High")
        else:
            print("Too low")    

        guess = input("Enter a number: ")  
print("congratulations!!! you are right")       

def keepPlaying(self):
    ''
    play_again = input("play again [y/n")
play_again ="yes"

while play_again == "yes" :
    random_num = r.randomint(1-13)
    gues= input("Enter a number :")

while int(guess) != rand_num:
        print("Incorrect! please try another number")  
        if int(guess)>random_num:
            print("Too High")
        else:
            print("Too low")    

        guess = input("Enter a number: ")  
print("congratulations!!! you are right")  