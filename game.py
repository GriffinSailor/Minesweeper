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
                gameBoard = Board(5, 5)
                gameBoard.printBoard()
            elif str(userIn) == "2" or userIn.lower == "medium":
                gameDifficulty = 2
                gameBoard = Board(7, 5)
                gameBoard.printBoard()
            elif str(userIn) == "3" or userIn.lower == "hard":
                gameDifficulty = 3
                gameBoard = Board(12, 5)
                gameBoard.printBoard()
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
                # TODO: add the catch here for data type/unable to cast
                x = int(userIn[0])
                y = int(userIn[1])

                squareValue = gameBoard.pickSquare(x, y)
            
            # Check if the move ended the game or not
            if squareValue == "clear":
                Board.printBoard()
            elif squareValue == "bomb":
                print(" " * 5 + "BOOM!!!\nYou Lose!")
            
# Play game!
game.play()