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
            move = userIn.split(",")
            if len(move) != 2:
                print("Invalid move: Only enter one number for each row/column")
            else:
                try:
                    x = int(move[0]) - 1
                    y = gameBoard.boardSize - int(move[1])
                    if x > gameBoard.boardSize or y > gameBoard.boardSize:
                        print("Invalid move: Only enter numbers in the range of the board")
                    else:
                        # Passed input sanitization, make the move
                        squareValue = gameBoard.pickSquare(y, x)
                except ValueError:
                    print("Invalid move: Only enter numbers")
            
            # Check if the move ended the game or not
            if squareValue == "clear":
                gameBoard.printBoard()
            elif squareValue == "bomb":
                print(" " * 5 + "BOOM!!!\nYou Lose!")
                return
            
# Play game!
game.play()