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
        print()
        for i in range (len(self.board)):
            print(str(i + 1) + "|" + " " * 2, end = "")
            for k in range (len(self.board)):
                if self.board[i][k].revealed == False:
                    print("x" + " " * 2, end = "")
                else:
                    print(str(self.board[i][k].value ) + " " * 2, end = "")
            print()
        print(" " * 3 + "_" * 15)
        print(" " * 4 + "1" + " " * 2 + "2" + " " * 2 + "3" + " " * 2 + "4" + " " * 2 + "5")
        print() 

    # Select a square to expose
    def pickSquare(self, col, row):
        if self.board[col][row].revealed == True:
            print("That square has already been revealed, pick another")
            self.printBoard()
            return "clear"
        elif self.board[col][row].value == 10:
            return "bomb"
        else:

            # TODO: the printboard here throws an error saying its missing a parameter
            self.board[col][row].revealed = True
            self.printBoard()
            return "clear"