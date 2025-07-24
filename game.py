from board import Board

class game (Board):

    # Play the game
    def play():
        gameDifficulty = 0
        activeGame = True

        # Create the board
        while gameDifficulty == 0:
            userIn = input("What difficulty would you prefer?\n1. Easy\n2. Medium\n3. Hard\n")
            if str(userIn) == "1" or userIn.lower == "easy":
                gameDifficulty = 1
                gameBoard = Board(10, 10)
                gameBoard.printBoard()
            elif str(userIn) == "2" or userIn.lower == "medium":
                gameDifficulty = 2
                gameBoard = Board(40, 15)
                gameBoard.printBoard()
            elif str(userIn) == "3" or userIn.lower == "hard":
                gameDifficulty = 3
                gameBoard = Board(99, 24)
                gameBoard.printBoard()
            else:
                print("Invalid Input")
                game.play()

        # Make moves
        while activeGame:
            squareValue = "blank"
            userIn = input("Pick a square to try to reveal with the format 'x,y':\n")
            userIn = userIn.replace(" ", "",)
            userIn = userIn.replace(",", "",)
            if len(userIn) != 2:
                print ("Invalid move, only enter a number for each row/column")
            else:
                # TODO: add the catch here for data type/unable to cast/one of the values is out of range
                # TODO: make the filter more strict and require a comma to allow for 2 digit x's and y's
                # The minus five and swapped x/y is to facilitate how the 2d arrays cordinates are handled
                x = int(userIn[0]) - 1
                y = gameBoard.boardSize - int(userIn[1])
                squareValue = gameBoard.pickSquare(y, x)
            
            # Check if the move ended the game or not
            if squareValue == "clear":
                gameBoard.printBoard()
            elif squareValue == "bomb":
                print(" " * 5 + "BOOM!!!\nYou Lose!")
            
# Play game!
game.play()