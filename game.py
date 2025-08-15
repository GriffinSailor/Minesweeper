from board import Board

class game (Board):

    # Collect the users first move and generate the board afterwards to avoid an immediate game over
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
                        x = int(move[0]) - 1
                        y = boardSize - int(move[1])
                        if x > boardSize or y > boardSize:
                            print("Invalid move: Only enter numbers in the range of the board")
                        else:
                            # Generate the board and move on from the first move
                            firstMove = False
                            gameBoard = Board(bombCount, boardSize, y, x)
                            gameBoard.pickSquare(y, x)
                            return gameBoard
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
            gameBoard = game.makeFirstMove(40, 15, firstMove)
            gameBoard.printBoard()
        elif str(userIn) == "3":
            gameBoard = game.makeFirstMove(99, 24, firstMove)
            gameBoard.printBoard()
        else:
            print("Invalid Input")
            game.play()

        # Make moves
        while activeGame:
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
                        # Passed input sanitization, make the move and verify if it ended the game
                        if gameBoard.pickSquare(y, x) == "clear":
                            gameBoard.printBoard()
                        else:
                            gameBoard.printBoard()
                            print("BOOM!!!\nYou Lose!")
                            activeGame = False
                except ValueError:
                    print("Invalid move: Only enter numbers")

# Play game!
game.play()