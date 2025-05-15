from square import Square

class Board(Square):

    # Constructor that determines the boards difficulty and builds it
    def __init__(self, bombCount, boardSize):
        self.bombCount = bombCount
        self.board = []

        for i in range (boardSize):
            self.board.append([])
            for k in range (boardSize):
                self.board[i].append(Square(1, False))

    # Display the board to the user with appropriate square values
    def printBoard(self):
        for i in range (len(self.board)):
            for k in range (len(self.board)):
                if self.board[i][k].revealed == False:
                    print("x", end = "")
                else:
                    print(str(self.board[i][k].value ) + " " * 2, end = "")
            print()

    # Select a square to expose
    def pickSquare(self, col, row):
        if self.board[col][row].revealed == True:
            print("That square has already been revealed, pick another")
            self.printBoard()
            return True
        elif self.board[col][row].value == 10:
            print(" " * 5 + "BOOM!!!\nYou Lose!")
            return False
        else:
            self.board[col][row].revealed = True
            self.printBoard()
            return True
    
    # Begin new game
    def startGame(bombCount, boardSize):
        gameBoard = Board(bombCount, boardSize)
        gameBoard.printBoard()