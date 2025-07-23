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
            print(str(self.boardSize - i) + ("|" if self.boardSize - i > 9 else " |") + " " * 2 , end = "")
            for k in range (len(self.board)):
                if self.board[i][k].revealed == False:
                    print("x" + " " * 2, end = "")
                else:
                    print(str(self.board[i][k].value ) + " " * 2, end = "")
            print()
        
        # TODO: fix the issue where it only prints the 5 digits for the columns
        print(" " * 4 + "_" * (self.boardSize * 3))
        print(" " * 3, end = "")
        for i in range (self.boardSize):
            print ((" " * 2 if i < 10 else " ") + str(i + 1), end = "")
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