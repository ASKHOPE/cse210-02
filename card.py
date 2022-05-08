import random
# Call the random.choice function which will choose
# one number from the numbers list. Store the chosen
# number in a variable named number.
# Author:Karrass


class Card:
    """
    Responsibility of the Card class is to get a random number for displayed card 

    Attibutes:

      value(int): it will store the random number from 1 to 13 

    """
# Author:Karrass

    def __init__(self):
        self.value = 0

    def get_random_card(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        number = random.choice(numbers)
        self.value = number
