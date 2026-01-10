from square import Square
import random

class Board(Square):

    # Extends a list of coordinates with those of the squares that touch the given row and column
    def connectingSquares(self, row, col, connectedSquares):
        if (row - 1, col + 1) not in connectedSquares and row >= 0 and col < self.boardSize:
            connectedSquares.append((row - 1, col + 1))

        if (row, col + 1) not in connectedSquares and col < self.boardSize:
            connectedSquares.append((row, col + 1))

        if (row + 1, col + 1) not in connectedSquares and row < self.boardSize and col < self.boardSize:
            connectedSquares.append((row + 1, col + 1))

        if (row - 1, col) not in connectedSquares and row >= 0:
            connectedSquares.append((row - 1, col))

        if (row + 1, col) not in connectedSquares and row < self.boardSize:
            connectedSquares.append((row + 1, col))

        if (row - 1, col - 1) not in connectedSquares and row >= 0 and col >= 0:
            connectedSquares.append((row - 1, col - 1))

        if (row, col - 1) not in connectedSquares and col >= 0:
            connectedSquares.append((row, col - 1))

        if (row + 1, col - 1) not in connectedSquares and row < self.boardSize and col >= 0:
            connectedSquares.append((row + 1, col - 1))

    # Display the board to the user
    def printBoard(self):
        print()
        for row in range (len(self.board)):
            print(str(self.boardSize - row) + ("|" if self.boardSize - row > 9 else " |") + " " * 2 , end = "")
            for col in range (len(self.board)):
                if self.board[row][col].revealed == False:
                    print("x" + " " * 2, end = "")
                else:
                    print(str(self.board[row][col].value ) + " " * 2, end = "")
            print()
        
        print(" " * 4 + "_" * (self.boardSize * 3))
        print(" " * 3, end = "")
        for i in range (self.boardSize):
            print ((" " * 2 if i < 10 else " ") + str(i + 1), end = "")
        print() 

    # Reveal a square or a group of squares
    def pickSquare(self, row, col):
        if self.board[row][col].value == 9:
            for i in range (self.boardSize):
                for k in range (self.boardSize):
                    self.board[i][k].revealed = True
            return "bomb"
        elif self.board[row][col].value == 0:
            # Reveal all connecting 0 squares
            self.board[row][col].revealed = True
            zeroSquares = list()
            self.board.connectingSquares(row, col, zeroSquares)

            # Loop through the coordinates
            for cord in zeroSquares:
                cordRow = cord[0]
                cordCol = cord[1]
                self.board[cordRow][cordCol].revealed = True
                if self.board[cordRow][cordCol].value == 0:
                    self.board.connectingSquares(cordRow, cordCol, zeroSquares) 
            return "clear"
        else:
            self.board[row][col].revealed = True
            return "clear"
        
    # Constructor that determines the boards difficulty and builds it
    def __init__(self, bombCount, boardSize, blockedRow, blockedCol):
        self.bombCount = bombCount
        self.boardSize = boardSize

        self.board = []
        blockedSquares = list()
        self.connectingSquares(blockedRow, blockedCol, blockedSquares)

        # Initialize the board as a 2D array
        for i in range (boardSize):
            self.board.append([])
            for k in range (boardSize):
                self.board[i].append(Square(0, False))

        # Determine the bomb locations
        bombLocations = []
        while len(bombLocations) != bombCount:
            row = random.randrange(0, boardSize)
            col = random.randrange(0, boardSize)
            
            # Ensure the first move is a 0 square to ensure a fair start to the game
            if (row, col) not in bombLocations and (row, col) not in blockedSquares:
                bombLocations.append((row, col))

        # Set the bomb locations and increment local square values
        for i in range (len(bombLocations)):
            cordinate = bombLocations[i]
            row = cordinate[0]
            col = cordinate[1]
            self.board[row][col].value = 9

            # Increment the values of all squares touching the bomb
            touchingBomb = list()
            self.connectingSquares(row, col, touchingBomb)
            for cord in touchingBomb:
                if self.board[cord[0]][cord[1]].value != 9:
                    self.board[cord[0]][cord[1]].value += 1