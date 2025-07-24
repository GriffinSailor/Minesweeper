from square import Square
import random

class Board(Square):

    # Constructor that determines the boards difficulty and builds it
    def __init__(self, bombCount, boardSize):
        self.bombCount = bombCount
        self.boardSize = boardSize
        self.board = []

        bombLocations = []
        while len(bombLocations) != bombCount:
            x = random.randrange(0, boardSize)
            y = random.randrange(0, boardSize)
            
            if (x,y) not in bombLocations:
                bombLocations.append(tuple((x, y)))

        for i in range (boardSize):
            self.board.append([])
            for k in range (boardSize):
                # currCordinate = (k, i)
                if (k, i) in bombLocations:
                    self.board[i].append(Square(9, False))
                else:
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
        if self.board[col][row].value == 9:
            for i in range (self.boardSize):
                for k in range (self.boardSize):
                    self.board[i][k]. revealed = True

            return "bomb"
        else:
            self.board[col][row].revealed = True
            return "clear"