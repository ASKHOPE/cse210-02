print()
"Hi there welcome to the Hilo game.Bet we are going to have a wounderful time playing this game together. Lets play!!! "

play_again ="yes"

while play_again == "yes" :
    random_num = r.random_num(1-13)
    gues= input("Enter a number :")

while int(gues) !=random_num:
    print("Incorrect! please try another number")  
    if int(gues)>random_num:
        print()  