from square import Square
import random

class Board(Square):

    # Constructor that determines the boards difficulty and builds it
    def __init__(self, bombCount, boardSize, blockedX, blockedY):
        self.bombCount = bombCount
        self.boardSize = boardSize
        self.board = []

        # Initialize the board
        for i in range (boardSize):
            self.board.append([])
            for k in range (boardSize):
                self.board[i].append(Square(0, False))

        # Determine the bomb locations
        bombLocations = []
        while len(bombLocations) != bombCount:
            x = random.randrange(0, boardSize)
            y = random.randrange(0, boardSize)
            
            # Ensure the first move is a 0 square to ensure a fair start to the game
            if (x,y) not in bombLocations and not (x == blockedX and y == blockedY) \
                and not (x == blockedX + 1 and y == blockedY) and not (x == blockedX + 1 and y == blockedY + 1) \
                and not (x == blockedX + 1 and y == blockedY - 1) and not (x == blockedX and y == blockedY + 1) \
                and not (x == blockedX - 1 and y == blockedY) and not (x == blockedX and y == blockedY - 1) \
                and not (x == blockedX - 1 and y == blockedY + 1) and not (x == blockedX - 1 and y == blockedY - 1):
                bombLocations.append(tuple((x, y)))

        # Set the bomb locations
        for i in range (len(bombLocations)):
            cordinate = bombLocations[i]
            x = cordinate[0]
            y = cordinate[1]
            self.board[y][x].value = 9

            # Increment the values of all squares touching the bomb
            if x + 1 <= boardSize - 1:
                if self.board[y][x + 1].value != 9:
                    self.board[y][x + 1].value += 1
                if y + 1 <= boardSize - 1:
                    if self.board[y + 1][x + 1].value != 9:
                        self.board[y + 1][x + 1].value += 1
                if y - 1 >= 0:
                    if self.board[y - 1][x + 1].value != 9:
                        self.board[y - 1][x + 1].value += 1
            if x - 1 >= 0:
                if self.board[y][x - 1].value != 9:
                    self.board[y][x - 1].value += 1
                if y + 1 <= boardSize - 1:
                    if self.board[y + 1][x - 1].value != 9:
                        self.board[y + 1][x - 1].value += 1
                if y - 1 >= 0:
                    if self.board[y - 1][x - 1].value != 9:
                        self.board[y - 1][x - 1].value += 1
            if y - 1 >= 0:
                if self.board[y - 1][x].value != 9:
                    self.board[y - 1][x].value += 1
            if y + 1 <= boardSize - 1:
                if self.board[y + 1][x].value != 9:
                    self.board[y + 1][x].value += 1

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
        
        print(" " * 4 + "_" * (self.boardSize * 3))
        print(" " * 3, end = "")
        for i in range (self.boardSize):
            print ((" " * 2 if i < 10 else " ") + str(i + 1), end = "")
        print() 
    
    # Reveal all squares around a sepcified coordinate and return a list of the ones that are 0 values
    @staticmethod
    def revealBlock(self, x, y):
        # Add coordinates that touch the primary zero square
        zeroSquares = [(x,y)]
        if x + 1 <= self.boardSize:
            zeroSquares.append(x + 1, y)
        if x + 1 <= self.boardSize and y + 1 <= self.boardSize:
            zeroSquares.append(x + 1, y + 1)
        if x + 1 <= self.boardSize and y - 1 >= 0:
            zeroSquares.append(x + 1, y - 1)
        if x - 1 >= 0:
            zeroSquares.append(x - 1, y)
        if x - 1 >= 0 and y + 1 <= self.boardSize:
            zeroSquares.append(x - 1, y + 1)
        if x - 1 >= 0 and y - 1 >= 0:
            zeroSquares.append(x - 1, y - 1)
        if y - 1 >= 0:
            zeroSquares.append(x, y - 1)
        if y + 1 <= self.boardSize:
            zeroSquares.append(x, y + 1)

        # Loop through the coordinates
        list.remove[(x,y)]
        for cord in zeroSquares:
            self.board[cord[0]][cord[1]].revealed = True
            if self.board[cord[0]][cord[1]].value == 0:
                # When hitting another zero, add the touching coordinates to the list without duplicating values
                if (cord[0], cord[1] + 1) not in zeroSquares and cord[1] + 1 <= self.boardSize:
                    zeroSquares.append((cord[0], cord[1] + 1))
                if (cord[0], cord[1] - 1) not in zeroSquares and cord[1] - 1 >= 0:
                    zeroSquares.append((cord[0], cord[1] - 1))
                if (cord[0] + 1, cord[1] + 1) not in zeroSquares and cord[1] + 1 <= self.boardSize and cord[0] + 1 <= self.boardSize:
                    zeroSquares.append((cord[0] + 1, cord[1] + 1))
                if (cord[0] + 1, cord[1] - 1) not in zeroSquares and cord[1] - 1 >= 0 and cord[0] + 1 <= self.boardSize:
                    zeroSquares.append((cord[0], cord[1] + 1))
                if (cord[0] + 1, cord[1]) not in zeroSquares and cord[0] + 1 <= self.boardSize:
                    zeroSquares.append((cord[0] + 1, cord[1]))
                if (cord[0] - 1, cord[1] + 1) not in zeroSquares and cord[1] + 1 <= self.boardSize and cord[0] - 1 >= 0:
                    zeroSquares.append((cord[0] - 1, cord[1] + 1))
                if (cord[0] - 1, cord[1] - 1) not in zeroSquares and cord[1] - 1 >= 0 and cord[0] - 1 >= 0:
                    zeroSquares.append((cord[0] - 1, cord[1] - 1))
                if (cord[0] - 1, cord[1] + 1) not in zeroSquares and cord[0] - 1 >= 0:
                    zeroSquares.append((cord[0] - 1, cord[1]))

    # Select a square to expose
    def pickSquare(self, col, row):
        if self.board[col][row].value == 9:
            for i in range (self.boardSize):
                for k in range (self.boardSize):
                    self.board[i][k].revealed = True
            return "bomb"
        elif self.board[col][row].value == 0:
            # Reveal all connecting 0 squares
            self.board[col][row].revealed = True
            
            # TODO: make sure this is working as intended
            self.revealBlock(self, col, row)
            return "clear"
        else:
            self.board[col][row].revealed = True
            return "clear"