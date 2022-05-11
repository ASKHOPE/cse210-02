"""Import the card from the card file
and call a game class to control the sequence of the game."""
from card import Card

class Game:
    
    def __init__(self):
        """Define the init to get
        an instance of a new director"""
        self.is_playing = True
        self.score = 300
        self.previous = 0
        self.rand_value= 0
        
    def start_game(self):
        """Define start game to run the main file of the game"""
        card = Card()
        self.rand_value = card.get_random_card()
        while self.is_playing:
            self.get_user_input()
            self.do_updates()
            
    def get_user_input(self):
        """Define the get user input to ask users
        which card they want to pick, add
        an instance to run the loop statements
        to know if the card is higher or lower."""
        print()
        input_loop = ""
        while input_loop != True:
            print(f"The Card is : {self.rand_value}")
            pick_card = input("Higher or Lower?[h, l]")
            if pick_card.lower() == "h" or pick_card.lower() == "l":
                pick_card = pick_card
                input_loop = True
            else:
                print()
                print("Invalid input please try again l for low and h for high")
                input_loop = False

        card = Card()
        self.previous = self.rand_value

        self.rand_value = card.get_random_card()
        while True:
            if self.previous != self.rand_value:
                break
            else:
                self.rand_value = card.get_random_card()
        self.update_score(pick_card)

    def update_score(self, pick_card):
        """Define the update score
        to display the player's score."""
      
        if pick_card.lower() == "h" and self.rand_value > self.previous:
            print(f"Next Card was: {self.rand_value}")
            print("You selected higher and the card was higher")
            self.score += 100
        elif pick_card.lower() == "l" and self.rand_value < self.previous:
            print(f"Next Card was: {self.rand_value}")
            print("You selected lower and the card was lower")
            self.score += 100
        else:
            print(f"Next Card was: {self.rand_value}")
            self.score -= 75
            
    def do_updates(self):
      
        if not self.is_playing:
            return

        if self.score <= 0:
            print("Game Over")
            self.is_playing = False
        print(f"Your score is: {self.score}")
        play_loop = ""
        while play_loop != True:
            play_again = input("Play again ? [y/n]: ")
            if play_again.lower() == "y":
                self.is_playing = True
                return
            elif play_again.lower() == "n":
                self.is_playing = False
                #print('Thanks for playing. Goodbye.')
                return
        print()
