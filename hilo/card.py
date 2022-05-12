import random
class Card:
    """Contains a random card nunmber generator between 1 to 13
    
     Args:
            self(card) ab instance of Card
    """
    def __init__(self):
        self.rand_value = 0

    def get_random_card(self):
        """Picks a random number between 1 and 13
        
        Args:
            self(card) ab instance of Card
        """
        number = random.randint(1,13)
        self.rand_value = number
        #print(self.rand_value) # For test purposes
        return self.rand_value