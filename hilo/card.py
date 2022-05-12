import random
# Call the random.choice function which will choose
# one number from the numbers list. Store the chosen
# number in a variable named number.


class Card:

    def __init__(self):
        self.rand_value = 0

    def get_random_card(self):
        number = random.randint(1,13)
        self.rand_value = number
        #print(self.rand_value)
        return self.rand_value
    
