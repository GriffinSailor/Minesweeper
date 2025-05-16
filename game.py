from board import Board

class game (Board):

    # Play the game
    def play():
        gameDifficulty = 0
        activeGame = True

        # Create the board
        while gameDifficulty == 0:
            userIn = input("What difficulty would you prefer?\n1. Easy\n2.Medium\n3.Hard\n")
            if str(userIn) == "1" or userIn.lower == "easy":
                gameDifficulty = 1
                Board.startGame(5, 5)
            elif str(userIn) == "2" or userIn.lower == "medium":
                gameDifficulty = 2
                Board.startGame(7, 5)
            elif str(userIn) == "3" or userIn.lower == "hard":
                gameDifficulty = 3
                Board.startGame(12, 5)
            else:
                print("Invalid Input")
                game.play()

        # Make moves
        while activeGame:
            squareValue = "blank"
            userIn = input("Pick a square to try to reveal (use the format x,y):\n")
            userIn = userIn.replace(" ", "",)
            userIn = userIn.replace(",", "",)
            if len(userIn) != 2:
                print ("Invalid move, only enter a number for each row/column")
            else:
                x = userIn[0]
                y = userIn[1]

                # Make sure the input is valid and make the move
                try:
                    int(x)
                    int(y)
                    # The issue is with this function call, specifically with the number of params
                    # for some reason it is requiring 3 even tho one of the 3 is 'self'
                    # squareValue = Board.pickSquare(x, y)
                except:
                    print(str(x) + str(y))
                    print("Invalid move, only enter a number for each row/column")
            
            # Check if the move ended the game or not
            if squareValue == "clear":
                Board.printBoard()
            elif squareValue == "bomb":
                print(" " * 5 + "BOOM!!!\nYou Lose!")
            
# Play game!
game.play()