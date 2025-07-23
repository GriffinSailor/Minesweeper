from square import Square

class Board(Square):

    # Constructor that determines the boards difficulty and builds it
    def __init__(self, bombCount, boardSize):
        self.bombCount = bombCount
        self.boardSize = boardSize
        self.board = []

        # TODO: create an array of randomly selected cordinates within range of the board size
        # then set that coordinate to a bomb in the loop below if the current value being set is within the array

        for i in range (boardSize):
            self.board.append([])
            for k in range (boardSize):
                self.board[i].append(Square(1, False))

    # Display the board to the user with appropriate square values
    def printBoard(self):
        print()
        for i in range (len(self.board)):
            print(str(self.boardSize - i) + "|" + " " * 2, end = "")
            for k in range (len(self.board)):
                if self.board[i][k].revealed == False:
                    print("x" + " " * 2, end = "")
                else:
                    print(str(self.board[i][k].value ) + " " * 2, end = "")
            print()
        
        # TODO: turn this into a bit of code that can change the number of prints based off difficulty
        print(" " * 3 + "_" * 15)
        print(" " * 4 + "1" + " " * 2 + "2" + " " * 2 + "3" + " " * 2 + "4" + " " * 2 + "5")
        print() 

    # Select a square to expose
    def pickSquare(self, col, row):
        if self.board[col][row].revealed == True:
            return "clear"
        elif self.board[col][row].value == 10:
            return "bomb"
        else:
            self.board[col][row].revealed = True
            return "clear"