from board import Board
from square import Square

class game (Board):

    # Collect the users first move and generate the board afterwards to ensure a fair start
    def makeFirstMove(boardSize, bombCount, firstMove):
            # Printing an empty board
            print()
            for i in range (boardSize):
                print(str(boardSize - i) + ("|" if boardSize - i > 9 else " |") + " " * 2 , end = "")
                for k in range (boardSize):
                    print("x" + " " * 2, end = "")
                print()
            print(" " * 4 + "_" * (boardSize * 3))
            print(" " * 3, end = "")
            for i in range (boardSize):
                print ((" " * 2 if i < 10 else " ") + str(i + 1), end = "")
            print() 

            # Collecting the users first move
            while firstMove:
                userIn = input("Pick a square to try to reveal with the format 'x,y':\n")
                userIn = userIn.replace(" ", "",)
                move = userIn.split(",")
                if len(move) != 2:
                    print("Invalid move: Only enter one number for each row/column")
                else:
                    try:
                        col = int(move[0]) - 1
                        row = boardSize - int(move[1])
                        if row >= 0 and row < boardSize and col >= 0 and col < boardSize:
                            # Generate the board and move on from the first move
                            firstMove = False
                            gameBoard = Board(bombCount, boardSize, row, col)
                            gameBoard.pickSquare(row, col)
                            return gameBoard
                        else:
                            print("Invalid move: Only enter numbers in the range of the board")
                    except ValueError:
                        print("Invalid move: Only enter numbers")

    # Play the game
    def play():
        activeGame = True
        firstMove = True

        # Create the board
        userIn = input("What difficulty would you prefer?\n1. Easy\n2. Medium\n3. Hard\n")
        if str(userIn) == "1":
            gameBoard = game.makeFirstMove(10, 10, firstMove)
            gameBoard.printBoard()
        elif str(userIn) == "2":
            gameBoard = game.makeFirstMove(15, 40, firstMove)
            gameBoard.printBoard()
        elif str(userIn) == "3":
            gameBoard = game.makeFirstMove(24, 99, firstMove)
            gameBoard.printBoard()
        else:
            print("Invalid Input")
            game.play()

        # TODO: implement a tracker to give a game over when the user has won
        # Make moves
        while activeGame:
            userIn = input("Pick a square to try to reveal with the format 'x,y':\n")
            userIn = userIn.replace(" ", "",)
            move = userIn.split(",")
            if len(move) != 2:
                print("Invalid move: Only enter one number for each row/column")
            else:
                try:
                    col = int(move[0]) - 1
                    row = gameBoard.boardSize - int(move[1])
                    if row >= 0 and row < gameBoard.boardSize and col >= 0 and col < gameBoard.boardSize:
                        print("Invalid move: Only enter numbers in the range of the board")
                    else:
                        # Passed input sanitization, make the move and verify if it ended the game
                        if gameBoard.pickSquare(row, col) == "clear":
                            gameBoard.printBoard()
                        else:
                            gameBoard.printBoard()
                            print("BOOM!!!\nYou Lose!")
                            activeGame = False
                except ValueError:
                    print("Invalid move: Only enter numbers")

# Play game!
game.play()