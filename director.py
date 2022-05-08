# Hilo Game
#Team Assigment

class Director:
    
    def __init__(self):
        self.card=0        

    
    def inputs(self):
        
        again_play=""
        while not again_play in ("y", "n"):
            again_play = input("Do you want to play again (Y/N)")
            if again_play =="n":
                print("Game is over")
            if not again_play in ("y", "n"):
                print("Pick y or n please")
                return                 
            
        
            
        