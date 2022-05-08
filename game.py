from card import Card
from guess import Guess
from scores import Scores
from play_update import Updates


class Game:
    
    def __init__(self):
        self.is_playing = True
        self.scored = 300
        self.previous = 0
        self.rand_value= 0
        self.userinput = ""
        
    def start_game(self):
        guess = Guess()
        card = Card()
        scores = Scores()
        updates = Updates()
        self.rand_value = card.get_random_card()
        while self.is_playing:
            
        #    print(f"This is print from game {self.rand_value}")
            guess.get_user_input()
            #inpie = guess.get_user_input(self.rand_value)
            #updates.score_update()
            #self.do_updates()
            #guess = Guess()
            scores.score_update(guess.get_user_input(),self.rand_value,self.previous,self.scored)
            #scores.score_update()
            updates.do_updates(self.is_playing,self.scored)


        
    