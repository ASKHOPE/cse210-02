
#from card import Card

class Scores:
        
    def score_update(self,userinput,rand_value,previous,score):
        #print(userinput)
      ##  print(f"printing the impotes guess into updates {guess}")
        if userinput == "h" and rand_value > previous:
            print(f"Next Card was: {rand_value}")
            print("You selected higher and the card was higher")
            #score += 100
            self.scored = score + 100
           # print(score)
            print(self.scored)

            return self.scored

           #return score

        elif userinput == "l" and rand_value < previous:
            print(f"Next Card was: {rand_value}")
            print("You selected lower and the card was lower")
            #score += 100
          #  self.scored = score
            self.scored = score + 100

           # print(score)
            print(self.scored)

            return self.scored
            #return score

        else:
            print(f"Next Card was: {rand_value}")
            score -= 75
            self.scored = score - 75 

            print(self.scored)
          #  self.scored = score

            return self.scored
        
     #   self.scored =score    
           
    #     def score_update(self):
    #   ##  print(f"printing the impotes guess into updates {guess}")
    #         if self.userinput == "h" and self.rand_value > self.previous:
    #             print(f"Next Card was: {self.rand_value}")
    #             print("You selected higher and the card was higher")
    #             self.score += 100
    #         elif self.userinput == "l" and self.rand_value < self.previous:
    #             print(f"Next Card was: {self.rand_value}")
    #             print("You selected lower and the card was lower")
    #             self.score += 100
    #         else:
    #             print(f"Next Card was: {self.rand_value}")
    #             self.score -= 75
    