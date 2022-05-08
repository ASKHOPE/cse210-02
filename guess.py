from card import Card
from scores import Scores
#card = Card()
#from game import Game
class Guess:

    def get_user_input(self):
        card = Card()
        print(f"The Card is : {card.get_random_card()}")

        input_loop = ""
        while input_loop != True:
           # print(f"The Card is : {self.rand_value}")
            guess_input = input("Higher or Lower?[h, l]")
            if guess_input.lower() == "h" or guess_input.lower() == "l":
                picked_card = guess_input
                #self.user_input = picked_card
                
              ##  print("Test guess "+ picked_card)
                input_loop = True
            else:
                print()
        ##        print("Invalid input please try again l for low and h for high")
                input_loop = False

            self.previous = card.get_random_card()
        ##    print(f"print previous check {self.previous}")
            card = Card()

            self.rand_value = card.get_random_card()
            
        ##    print(f"self rand test guess {self.rand_value}")
            
            while True:
                #game = Game()
                if self.previous != self.rand_value:

                    break
                else:
                    self.rand_value = card.get_random_card()
            
            return