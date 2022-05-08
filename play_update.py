from scores import Scores

class Updates:
   def do_updates(self,is_playing,score):

        if not is_playing:
            return

        if score <= 0:
            print("Game Over")
            is_playing = False
        print(f"Your score is: {score}")
        play_loop = ""
        while play_loop != True:
            play_again = input("Play again ? [y/n]: ")
            if play_again.lower() == "y":
                is_playing = True
                return
            elif play_again.lower() == "n":
                is_playing = False
                print('Thanks for playing. Goodbye.')
                return
        print()
